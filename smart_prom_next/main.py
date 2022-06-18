# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""smart-prom-next main module."""
import json
from subprocess import PIPE, Popen
from typing import List

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


def main():
    """Main function."""
    print(f"start smart-prom-next version: {__version__}")
    devices = scan_devices()
    print("devices:", devices)


if __name__ == "__main__":
    main()
