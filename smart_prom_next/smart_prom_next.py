# Copyright (c) 2022 - 2023 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""smart-prom-next main module."""

import json
import os
import sys
import time
from subprocess import PIPE, Popen
from typing import Any, Dict, List, Tuple

from prometheus_client import Counter, start_http_server

from smart_prom_next.metric_wrapper import GaugeWrapper


# Counter how often the SMART values were scraped.
SCRAPE_ITERATIONS_COUNTER: Counter = Counter(
    "smart_prom_scrape_iterations_total", "Total number of SMART scrape iterations."
)

first_scrape_interval: bool = True
init_metrics_done: bool = False


def normalize_str(the_str: str) -> str:
    """Normalize a string.

    If anything other than a ``str`` is passed, then the same value is returned unchanged.
    This is useful to prepare and clean Prometheus labels.
    """
    result = the_str
    if isinstance(the_str, str):
        result = the_str.strip().lower()
        replace_cars = ["-", " ", ".", "/", ":", "#", "*", "+", "~"]
        for replace_car in replace_cars:
            result = result.replace(replace_car, "_")
    return result


def call_smartctl(options: List[str]) -> Tuple[str, int]:
    """Execute a child program in a new process."""
    args = ["smartctl"]
    args.extend(options)
    if first_scrape_interval:
        print(f"DEBUG: Output of the first scraping iteration: call: {args}")
    try:
        with Popen(args, stdout=PIPE, stderr=PIPE) as popen:
            stdout, stderr = popen.communicate()

            # returncode can be != 0 even if the command returned valid data
            # see EXIT STATUS in
            # https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in

            returncode = popen.returncode
            result = None
            if stdout is not None:
                result = stdout.decode("utf-8")

            if returncode != 0:
                stderr_text = (
                    stderr.decode("utf-8")
                    if (stderr is not None and stderr.decode("utf-8") != "")
                    else "not set"
                )
                print(
                    f"WARNING: Calling {args} returned non zero returncode! "
                    f"returncode: {popen.returncode} stderr: '{stderr_text}' "
                    "This is only a warning. Not an error. "
                    "smartctl permits a non-zero return code even under normal circumstances."
                )

            if isinstance(result, str) and len(result) > 0:  # we have a result
                if first_scrape_interval:
                    print(f"DEBUG: Output of the first scraping iteration: result: {result}")
                return result, returncode
            else:
                raise RuntimeError(
                    f"Calling {args} returned no result! "
                    f"returncode: {popen.returncode} stderr: '{stderr_text}'"
                )

    except FileNotFoundError:
        print(
            "ERROR: The smartctl program cannot be found. "
            "Maybe smartctl (smartmontools) still needs to be installed.",
            file=sys.stderr,
        )
        raise


def scan_devices() -> List[Dict[str, str]]:
    """Return relevant devices.

    Returns:
        The ``name`` key contains the device name.
    """
    results_json, _ = call_smartctl(["--scan-open", "--json"])
    results = json.loads(results_json)
    devices = results.get("devices", [])
    assert isinstance(devices, list)
    return devices


def scrape_smart_status(device_info: Dict[str, Any], labels: Dict[str, str]) -> None:
    """Scrape SMART status."""
    smart_status = device_info.get("smart_status", None)
    if isinstance(smart_status, dict):
        smart_status_passed = smart_status.get("passed", None)
        if isinstance(smart_status_passed, bool):
            smart_status_failed_value = 0 if smart_status_passed else 1
            _SMART_STATUS_FAILED_GAUGE.set(  # type: ignore
                value=smart_status_failed_value, **labels
            )
        else:
            print(
                f"WARNING: SMART status is present but cannot read the value! "
                f"smart_status_passed: {smart_status_passed}"
            )


def scrape_temperature(device_info: Dict[str, Any], labels: Dict[str, str]) -> None:
    """Scrape temperature status."""
    temperature = device_info.get("temperature", None)
    if isinstance(temperature, dict):
        for temperature_type, temperature_value in temperature.items():
            if isinstance(temperature_type, str) and isinstance(temperature_value, int):
                temperature_labels = labels.copy()  # copy so we do not change labels
                temperature_labels["temperature_type"] = normalize_str(temperature_type)
                _TEMPERATURE_GAUGE.set(  # type: ignore
                    value=temperature_value, **temperature_labels
                )
            else:
                print(
                    f"WARNING: Temperature is present but cannot read the value! "
                    f"temperature_type: {temperature_type} temperature_value: {temperature_value}"
                )


def scrape_nvme_metrics(device_info: Dict[str, Any], labels: Dict[str, str]) -> None:
    """Scrape nvme specific info."""
    nvme_smart_info = device_info.get("nvme_smart_health_information_log", None)
    if isinstance(nvme_smart_info, dict):
        for smart_key, smart_value in nvme_smart_info.items():
            if isinstance(smart_key, str):
                smart_key = normalize_str(smart_key)
                if smart_key == "temperature_sensors":
                    if isinstance(smart_value, list):
                        for temp_sensor_nr, temp_sensor_value in enumerate(smart_value, start=1):
                            smart_info_labels = labels.copy()
                            smart_info_labels["attr_name"] = f"{smart_key}_{temp_sensor_nr}"
                            _NVME_SMART_INFO_GAUGE.set(  # type: ignore
                                value=temp_sensor_value, **smart_info_labels
                            )
                else:
                    if isinstance(smart_value, int):
                        smart_info_labels = labels.copy()
                        smart_info_labels["attr_name"] = smart_key
                        _NVME_SMART_INFO_GAUGE.set(  # type: ignore
                            value=smart_value, **smart_info_labels
                        )


def scrape_scsi_metrics(device_info: Dict[str, Any], labels: Dict[str, str]) -> None:
    """Scrape sata specific info."""
    sata_smart_info = device_info.get("scsi_error_counter_log", None)
    if isinstance(sata_smart_info, dict):
        for attr_type, values_dict in sata_smart_info.items():
            if isinstance(attr_type, str) and isinstance(values_dict, dict):
                for attr_name, value in values_dict.items():
                    if isinstance(value, str):
                        try:
                            value = float(value)
                        except ValueError:
                            # nothing we can do here
                            pass
                    if isinstance(attr_name, str) and isinstance(value, (int, float)):
                        smart_info_labels = labels.copy()
                        smart_info_labels["attr_name"] = attr_name
                        smart_info_labels["attr_type"] = attr_type
                        _SCSI_SMART_INFO_GAUGE.set(  # type: ignore
                            value=value, **smart_info_labels
                        )


def scrape_ata_metrics(device_info: Dict[str, Any], labels: Dict[str, str]) -> None:
    """Scrape sat specific info."""
    sat_smart_info = device_info.get("ata_smart_attributes", None)
    if isinstance(sat_smart_info, dict):
        sat_smart_info_table = sat_smart_info.get("table", None)
        if isinstance(sat_smart_info_table, list):
            for smart_info_item in sat_smart_info_table:
                if isinstance(smart_info_item, dict):
                    _flags = smart_info_item.get("flags", None)
                    if isinstance(_flags, dict):
                        _id = smart_info_item.get("id", None)
                        _name = smart_info_item.get("name", None)

                        # id and name must be available
                        if isinstance(_id, int) and isinstance(_name, str):
                            sat_labels = labels.copy()
                            sat_labels["attr_id"] = str(_id)  # no further normalization
                            sat_labels["attr_name"] = normalize_str(_name)

                            # check when_failed (now and past)
                            _when_failed = smart_info_item.get("when_failed", None)
                            _when_failed = normalize_str(_when_failed)
                            # always call this without condition
                            for _when_failed_value in ["now", "past"]:
                                gauge_value = 1 if _when_failed == _when_failed_value else 0
                                _SMART_INFO_GAUGE.set(  # type: ignore
                                    value=gauge_value,
                                    **sat_labels,
                                    attr_type=f"failed_{_when_failed_value}",
                                )

                            # read value, worst and thresh
                            for attr_type in ["value", "worst", "thresh"]:
                                _value = smart_info_item.get(attr_type, None)
                                if isinstance(_value, int):
                                    _SMART_INFO_GAUGE.set(  # type: ignore
                                        value=_value, **sat_labels, attr_type=attr_type
                                    )

                            # read raw value
                            _raw = smart_info_item.get("raw", None)
                            if isinstance(_raw, dict):
                                _value = _raw.get("value", None)
                                if isinstance(_value, int):
                                    _SMART_INFO_GAUGE.set(  # type: ignore
                                        value=_value, **sat_labels, attr_type="raw"
                                    )


def scrape_metrics_for_device(
    device_name: str, device_type: str, device_info_json: str, returncode: int
) -> None:
    """Scrape metrics for given device."""
    device_info = json.loads(device_info_json)

    model_name = device_info.get("model_name", "unknown")
    serial_number = device_info.get("serial_number", "unknown")

    labels = {
        "device": device_name,  # no normalization
        "type": normalize_str(device_type),
        "model": model_name,  # no normalization
        "serial": serial_number,  # no normalization
    }

    _SMART_SMARTCTL_EXIT_STATUS_GAUGE.set(value=returncode, **labels)  # type: ignore

    scrape_smart_status(
        device_info=device_info,
        labels=labels,
    )
    scrape_temperature(
        device_info=device_info,
        labels=labels,
    )
    scrape_nvme_metrics(
        device_info=device_info,
        labels=labels,
    )
    scrape_ata_metrics(
        device_info=device_info,
        labels=labels,
    )
    scrape_scsi_metrics(
        device_info=device_info,
        labels=labels,
    )


def refresh_metrics() -> None:
    """Refresh the metrics."""
    devices = scan_devices()
    for device in devices:
        device_name = device.get("name", None)
        if isinstance(device_name, str) and len(device_name) > 0:
            device_info_json, returncode = call_smartctl(["--xall", "--json", device_name])
            device_type = str(device.get("type", "unknown"))
            scrape_metrics_for_device(
                device_name, device_type, device_info_json, returncode=returncode
            )
        else:
            print(
                f"WARNING: Device name is present but cannot read the value! "
                f"device_name: {device_name}"
            )


def init_metrics(smart_info_refresh_interval):
    """Init the metrics."""
    global init_metrics_done
    if not init_metrics_done:
        init_metrics_done = True
        global _SMART_INFO_GAUGE
        _SMART_INFO_GAUGE = GaugeWrapper(
            "smart_prom_smart_info",
            "SMART health information log",
            ["device", "type", "model", "serial", "attr_name", "attr_type", "attr_id"],
            smart_info_refresh_interval * 4,
        )

        global _NVME_SMART_INFO_GAUGE
        _NVME_SMART_INFO_GAUGE = GaugeWrapper(
            "smart_prom_nvme_smart_info",
            "nvme SMART health information log",
            ["device", "type", "model", "serial", "attr_name"],
            smart_info_refresh_interval * 4,
        )

        global _SCSI_SMART_INFO_GAUGE
        _SCSI_SMART_INFO_GAUGE = GaugeWrapper(
            "smart_prom_scsi_smart_info",
            "scsi SMART health information log",
            ["device", "type", "model", "serial", "attr_name", "attr_type"],
            smart_info_refresh_interval * 4,
        )

        global _TEMPERATURE_GAUGE
        _TEMPERATURE_GAUGE = GaugeWrapper(
            "smart_prom_temperature",
            "The temperature of a particular type.",
            ["device", "type", "model", "serial", "temperature_type"],
            smart_info_refresh_interval * 4,
        )

        global _SMART_STATUS_FAILED_GAUGE
        _SMART_STATUS_FAILED_GAUGE = GaugeWrapper(
            "smart_prom_smart_status_failed",
            "1 if SMART status check failed, otherwise 0",
            ["device", "type", "model", "serial"],
            smart_info_refresh_interval * 4,
        )

        global _SMART_SMARTCTL_EXIT_STATUS_GAUGE
        _SMART_SMARTCTL_EXIT_STATUS_GAUGE = GaugeWrapper(
            "smart_prom_smartctl_exit_status",
            "exit status of the smartctl call",
            ["device", "type", "model", "serial"],
            smart_info_refresh_interval * 4,
        )


def main() -> None:
    """Main function."""
    global first_scrape_interval
    print("INFO: Start smart-prom-next.")

    prometheus_client_port = int(os.environ.get("PROMETHEUS_METRIC_PORT", 9902))
    print(f"INFO: Start prometheus client. port: {prometheus_client_port}")
    start_http_server(prometheus_client_port)

    smart_info_refresh_interval = int(os.environ.get("SMART_INFO_READ_INTERVAL_SECONDS", 60))

    init_metrics(smart_info_refresh_interval)

    print(
        "INFO: Enter metrics refresh loop. "
        f"smart_info_refresh_interval: {smart_info_refresh_interval}"
    )

    while True:
        refresh_metrics()
        SCRAPE_ITERATIONS_COUNTER.inc()
        first_scrape_interval = False
        _SMART_INFO_GAUGE.remove_old_metrics()  # type: ignore
        _NVME_SMART_INFO_GAUGE.remove_old_metrics()  # type: ignore
        _SCSI_SMART_INFO_GAUGE.remove_old_metrics()  # type: ignore
        _TEMPERATURE_GAUGE.remove_old_metrics()  # type: ignore
        _SMART_STATUS_FAILED_GAUGE.remove_old_metrics()  # type: ignore
        _SMART_SMARTCTL_EXIT_STATUS_GAUGE.remove_old_metrics()  # type: ignore
        time.sleep(smart_info_refresh_interval)


if __name__ == "__main__":
    main()
