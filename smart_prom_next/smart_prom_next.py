# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""smart-prom-next main module."""

import json
import os
import sys
import time
from subprocess import PIPE, Popen
from typing import Any, Dict, List

from prometheus_client import Gauge, start_http_server


TEMPERATURE_GAUGE = Gauge(
    "smart_prom_temperature",
    "The temperature of a particular type.",
    ["device", "type", "model", "serial", "temperature_type"],
)

SMART_STATUS_FAILED_GAUGE = Gauge(
    "smart_prom_smart_status_failed",
    "1 if SMART status check failed, otherwise 0",
    ["device", "type", "model", "serial"],
)

NVME_SMART_INFO_GAUGE = Gauge(
    "smart_prom_nvme_smart_info",
    "nvme SMART health information log",
    ["device", "type", "model", "serial", "info_type"],
)

SMART_INFO_GAUGE = Gauge(
    "smart_prom_smart_info",
    "SMART health information log",
    ["device", "type", "model", "serial", "attr_name", "attr_type", "attr_id"],
)


def normalize_str(the_str) -> str:
    """Normalize a string.

    This is useful to prepare Prometheus labels.
    """
    return the_str.strip().lower()


def call_smartctl(options: List[str]):
    """Execute a child program in a new process."""
    args = ["smartctl"]
    args.extend(options)
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
                    f"Calling {args} resturned non zero returncode! "
                    f"returncode: {popen.returncode} stderr: '{stderr_text}'"
                )

            if isinstance(result, str) and len(result) > 0:  # we have a result
                return result
            else:
                raise Exception(f"Calling {args} resurned no result! returncode: {popen.returncode} stderr: '{stderr_text}'")

    except FileNotFoundError:
        print(
            "The smartctl program cannot be found. "
            "Maybe smartctl (smartmontools) still needs to be installed.",
            file=sys.stderr,
        )
        raise



def scan_devices() -> List[Dict[str, str]]:
    """Return relevant devices.

    Returns:
        The ``name`` key contains the device name.
    """
    results_json = call_smartctl(["--scan-open", "--json"])
    results = json.loads(results_json)
    devices = results.get("devices", [])
    assert isinstance(devices, list)
    return devices


def read_device_info_json(device_name: str):
    """Read SMART info from device."""
    device_info_json = call_smartctl(["--xall", "--json", device_name])
    return device_info_json


def scrape_smart_status(device_info: Dict[str, Any], labels: Dict[str, str]):
    """Scrape SMART status."""
    smart_status = device_info.get("smart_status", None)
    if isinstance(smart_status, dict):  # TODO: add warning when else?
        smart_status_passed = smart_status.get("passed", None)
        print("smart_status_passed", smart_status_passed)  # TODO: delete me later
        if isinstance(smart_status_passed, bool):  # TODO: add warning when else?
            smart_status_failed_value = 0 if smart_status_passed else 1
            print("smart_status_failed_value", smart_status_failed_value)  # TODO: delete me later
            SMART_STATUS_FAILED_GAUGE.labels(**labels).set(smart_status_failed_value)


def scrape_temperature(device_info: Dict[str, Any], labels: Dict[str, str]):
    """Scrape temperature status."""
    temperature = device_info.get("temperature", None)
    print("temperature:", temperature)  # TODO: del me later
    if isinstance(temperature, dict):  # TODO: what is not?
        for temperature_type, temperature_value in temperature.items():
            if isinstance(temperature_type, str) and isinstance(
                temperature_value, int
            ):  # TODO: what is not?
                temperature_labels = labels.copy()  # copy so we do not change labels
                temperature_labels["temperature_type"] = normalize_str(temperature_type)
                TEMPERATURE_GAUGE.labels(**temperature_labels).set(temperature_value)


def scrape_nvme_metrics(device_info: Dict[str, Any], labels: Dict[str, str]):
    """Scrape nvme specific info."""
    nvme_smart_info = device_info.get("nvme_smart_health_information_log", None)
    if isinstance(nvme_smart_info, dict):
        for smart_key, smart_value in nvme_smart_info.items():
            smart_key = normalize_str(smart_key)
            if isinstance(smart_key, str):
                if smart_key == "temperature_sensors":
                    if isinstance(smart_value, list):
                        for temp_sensor_nr, temp_sensor_value in enumerate(smart_value, start=1):
                            smart_info_labels = labels.copy()
                            smart_info_labels["info_type"] = f"{smart_key}_{temp_sensor_nr}"
                            NVME_SMART_INFO_GAUGE.labels(**smart_info_labels).set(
                                temp_sensor_value
                            )
                else:
                    if isinstance(smart_value, int):
                        smart_info_labels = labels.copy()
                        smart_info_labels["info_type"] = smart_key
                        NVME_SMART_INFO_GAUGE.labels(**smart_info_labels).set(smart_value)


def scrape_ata_metrics(device_info: Dict[str, Any], labels: Dict[str, str]):
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
                            sat_labels["attr_id"] = str(_id)
                            sat_labels["attr_name"] = _name

                            # check when_failed
                            _when_failed = smart_info_item.get("when_failed", None)
                            if _when_failed is not None:
                                # set now value:
                                now_value = 1 if _when_failed == "now" else 0
                                SMART_INFO_GAUGE.labels(**sat_labels, attr_type="failed_now").set(
                                    now_value
                                )

                                # set past value:
                                past_value = 1 if _when_failed == "past" else 0
                                SMART_INFO_GAUGE.labels(**sat_labels, attr_type="failed_past").set(
                                    past_value
                                )

                            # read value, worst and thresh
                            for attr_type in ["value", "worst", "thresh"]:
                                _value = smart_info_item.get(attr_type, None)
                                if isinstance(_value, int):
                                    SMART_INFO_GAUGE.labels(**sat_labels, attr_type=attr_type).set(
                                        _value
                                    )

                            # read raw value
                            _raw = smart_info_item.get("raw", None)
                            if isinstance(_raw, dict):
                                _value = _raw.get("value", None)
                                if isinstance(_value, int):
                                    SMART_INFO_GAUGE.labels(**sat_labels, attr_type="raw").set(
                                        _value
                                    )


def scrape_metrics_for_device(device_name: str, device_type: str, device_info_json: str):
    """Scrape metrics for given device."""
    device_info = json.loads(device_info_json)

    model_name = device_info.get("model_name", "unknown")
    serial_number = device_info.get("serial_number", "unknown")

    labels = {
        "device": device_name,
        "type": device_type,
        "model": model_name,
        "serial": serial_number,
    }

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


def refresh_metrics():
    """Refresh the metrics."""
    devices = scan_devices()
    print("devices:", devices)  # TODO: delete me later
    for device in devices:
        device_name = device.get("name", None)
        if isinstance(device_name, str) and len(device_name) > 0:  # TODO: what is not?
            device_info_json = read_device_info_json(device_name)
            device_type = device.get("type", None)
            if isinstance(device_type, str):  # TODO: what is not?
                scrape_metrics_for_device(device_name, device_type, device_info_json)


def main():
    """Main function."""
    print("Start smart-prom-next.")  # TODO: add version info when pip package available

    prometheus_client_port = int(os.environ.get("PROMETHEUS_METRIC_PORT", 9902))
    print(f"Start prometheus client. port: {prometheus_client_port}")
    start_http_server(prometheus_client_port)

    smart_info_refresh_interval = int(os.environ.get("SMART_INFO_READ_INTERVAL_SECONDS", 60))
    print(
        f"Enter metrics refresh loop. smart_info_refresh_interval: {smart_info_refresh_interval}"
    )

    while True:
        refresh_metrics()
        time.sleep(smart_info_refresh_interval)


if __name__ == "__main__":
    main()