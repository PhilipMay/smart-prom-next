# S.M.A.R.T. Prometheus Metrics Exporter

smart-prom-next is a [Prometheus](https://prometheus.io/docs/introduction/overview/) metric exporter for
[S.M.A.R.T.](https://en.wikipedia.org/wiki/S.M.A.R.T.) values of hard disks.
Python and the Linux tool [smartctl](https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in)
are used to read out the hard disk values. These are then exposed using
[Prometheus Python Client](https://github.com/prometheus/client_python) over network port 9902.

According to Wikipedia, the primary function of S.M.A.R.T. is to detect and report various indicators of drive
reliability with the intent of anticipating imminent hardware failures.

Currently, smart-prom-next is only
[available as a docker image](https://github.com/PhilipMay/smart-prom-next/pkgs/container/smart-prom-next).
The base is built from the slim version of the [official Python Docker image](https://hub.docker.com/_/python),
which uses [Debian Bullseye](https://www.debian.org/releases/bullseye/).
It is built for multiple platforms:</br>
linux/386, linux/amd64, linux/arm/v5, linux/arm/v7, linux/arm64/v8

## Configuration Options / Environment Variables

smart-prom-next can be configured by the following environment variables:

- `PROMETHEUS_METRIC_PORT` - port number over which the Prometheus metrics are exposed (default: 9902)
- `SMART_INFO_READ_INTERVAL_SECONDS` - time interval in seconds at which the SMART values of the hard disk are read
  (default: 60)

## Docker / docker-compose

Below is an example of a complete minimal `docker-compose.yml`, how smart-prom-next can be used with [docker-compose](https://docs.docker.com/compose/):

```yaml
version: "3.0"
services:
  smart-prom-next:
    # see https://github.com/PhilipMay/smart-prom-next/pkgs/container/smart-prom-next
    image: ghcr.io/philipmay/smart-prom-next:0.0.1
    container_name: "smart-prom-next"
    restart: unless-stopped
    privileged: true
    ports:
      - 9902:9902
```

The `privileged: true` permission is absolutely necessary so that smartctl can also access the hard disks from
within the container.

**Security note:** In the production environment, you should leave out the `ports:` part in the `docker-compose.yml`
in the vast majority of configurations so that it is not visible to the outside. Instead, the container should
be assigned to a network in which the prometheus container is located. This looks like this:

```yaml
    networks:
      - monitor
```

To adjust the environment variables, the following settings can be added, for example:

```yaml
    environment:
      - PROMETHEUS_METRIC_PORT=9009
      - SMART_INFO_READ_INTERVAL_SECONDS=120
```

## Available Metrics

### `smart_prom_smartctl_exit_status`

The exit status (aka exit code or return code) of the `smartctl` tool.
Any value other than zero indicates an issue.
The more detailed description can be found in the EXIT STATUS chapter of the
[smartctl man pages](https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in) pages.

### `smart_prom_smart_status_failed`

The SMART health status of the device. A value of 0 indicates a healthy state.
A value of 1 means that the device has not passed the health check and there is a problem.

### `smart_prom_temperature`

The current temperature of the device.

### `smart_prom_nvme_smart_info`

NVMe specific SMART attributes obtained from the SMART/Health Information log.

## Licensing

Copyright (c) 2022 Philip May

Licensed under the **MIT License** (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License by reviewing the file
[LICENSE](https://github.com/PhilipMay/smart-prom-next/blob/main/LICENSE) in the repository.
