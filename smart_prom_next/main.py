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

from smart_prom_next import __version__


SMART_STATUS_FAILED_GAUGE = Gauge(
    "smart_prom_smart_status_failed",
    "1 if SMART status check failed, otherwise 0",
    ["device_name", "model_name", "serial_number"],
)


def call_smartctl(options: List[str]):
    """Execute a child program in a new process."""
    args = ["smartctl"]
    args.extend(options)
    try:
        with Popen(args, stdout=PIPE, stderr=PIPE) as popen:
            stdout, stderr = popen.communicate()

            if popen.returncode != 0:
                stderr_text = (
                    stderr.decode("utf-8")
                    if (stderr is not None and stderr.decode("utf-8") != "")
                    else "not set"
                )
                error_text = (
                    f"Error calling {args}! returncode: {popen.returncode} stderr: '{stderr_text}'"
                )
                print(error_text, file=sys.stderr)
                raise Exception(error_text)

    except FileNotFoundError:
        print(
            "The smartctl program cannot be found. "
            "Maybe smartctl (smartmontools) still needs to be installed.",
            file=sys.stderr,
        )
        raise

    return stdout.decode("utf-8")


def scan_devices() -> List[Dict[str, str]]:
    """Return relevant devices.

    Returns:
        The ``name`` key contains the device name.
    """
    results_json = call_smartctl(["--scan-open", "--json"])
    results = json.loads(results_json)
    devices = results.get("devices", [])
    return devices


def read_device_info_json(device_name: str):
    """Read SMART info from device."""
    device_info_json = call_smartctl(["--xall", "--json", device_name])
    return device_info_json


def scrape_smart_status(
    device_name: str, device_info: Dict[str, Any], model_name: str, serial_number: str
):
    """Scrape SMART status."""
    smart_status = device_info.get("smart_status", None)
    if smart_status is not None and isinstance(smart_status, dict):  # TODO: add warning when else?
        smart_status_passed = smart_status.get("passed", None)
        print("smart_status_passed", smart_status_passed)  # TODO: delete me later
        if smart_status_passed is not None and isinstance(
            smart_status_passed, bool
        ):  # TODO: add warning when else?
            smart_status_failed_value = 0 if smart_status_passed else 1
            print("smart_status_failed_value", smart_status_failed_value)  # TODO: delete me later

            SMART_STATUS_FAILED_GAUGE.labels(
                device_name=device_name, model_name=model_name, serial_number=serial_number
            ).set(smart_status_failed_value)


def scrape_nvme_metrics(device_name: str, device_info_json: str):
    """Scrape metrics for nvme device."""
    device_info = json.loads(device_info_json)

    model_name = device_info.get("model_name", "unknown model name")
    serial_number = device_info.get("serial_number", "unknown serial number")

    scrape_smart_status(
        device_name=device_name,
        device_info=device_info,
        model_name=model_name,
        serial_number=serial_number,
    )


def refresh_metrics():
    """Refresh the metrics."""
    devices = scan_devices()
    print("devices:", devices)  # TODO: delete me later
    for device in devices:
        device_name = device.get("name", None)
        if device_name is not None and isinstance(device_name, str) and len(device_name) > 0:
            device_info_json = read_device_info_json(device_name)
            device_type = device.get("type", None)
            if device_type == "nvme":
                scrape_nvme_metrics(device_name, device_info_json)
            else:
                pass
                # TODO: should we handle this?


def main():
    """Main function."""
    print(f"Start smart-prom-next. version: {__version__}")

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
