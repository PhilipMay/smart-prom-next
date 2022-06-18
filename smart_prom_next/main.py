# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""smart-prom-next main module."""
import json
import os
import time
from subprocess import PIPE, Popen
from typing import List

from prometheus_client import start_http_server

from smart_prom_next import __version__


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
                print(error_text)
                raise Exception(error_text)

    except FileNotFoundError:
        print(
            "The smartctl program cannot be found. "
            "Maybe smartctl (smartmontools) still needs to be installed."
        )
        raise

    return stdout.decode("utf-8")


def scan_devices():
    """Return relevant devices."""
    results_json = call_smartctl(["--scan-open", "--json"])
    results = json.loads(results_json)
    devices = results.get("devices", [])
    return devices


def refresh_metrics():
    devices = scan_devices()
    print("devices:", devices)


def main():
    """Main function."""
    print(f"Start smart-prom-next. version: {__version__}")

    prometheus_client_port = int(os.environ.get("PROMETHEUS_METRIC_PORT", 9902))
    print(f"Start prometheus client. port: {prometheus_client_port}")
    start_http_server(prometheus_client_port)

    smart_info_refresh_interval = int(os.environ.get("SMART_INFO_READ_INTERVAL_SECONDS", 60))
    print(f"Enter metrics refresh loop. smart_info_refresh_interval: {smart_info_refresh_interval}")

    while True:
        refresh_metrics()
        time.sleep(smart_info_refresh_interval)


if __name__ == "__main__":
    main()
