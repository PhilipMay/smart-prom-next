# S.M.A.R.T. Prometheus Metrics Exporter

[![MIT License](https://img.shields.io/github/license/PhilipMay/smart-prom-next)](https://github.com/PhilipMay/smart-prom-next/blob/main/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/smart-prom-next)](https://www.python.org)
[![pypi](https://img.shields.io/pypi/v/smart-prom-next.svg)](https://pypi.python.org/pypi/smart-prom-next)
[![GitHub issues](https://img.shields.io/github/issues-raw/PhilipMay/smart-prom-next)](https://github.com/PhilipMay/smart-prom-next/issues)\
[![pytest status](https://github.com/PhilipMay/smart-prom-next/actions/workflows/pytest.yml/badge.svg)](https://github.com/PhilipMay/smart-prom-next/actions/workflows/pytest.yml)
[![Static Code Checks status](https://github.com/PhilipMay/smart-prom-next/actions/workflows/static_checks.yml/badge.svg)](https://github.com/PhilipMay/smart-prom-next/actions/workflows/static_checks.yml)\
[![Docker build Debian image](https://github.com/PhilipMay/smart-prom-next/actions/workflows/docker-build-debian.yml/badge.svg)](https://github.com/PhilipMay/smart-prom-next/actions/workflows/docker-build-debian.yml)
[![Docker build Alpine image](https://github.com/PhilipMay/smart-prom-next/actions/workflows/docker-build-alpine.yml/badge.svg)](https://github.com/PhilipMay/smart-prom-next/actions/workflows/docker-build-alpine.yml)
[![trivy](https://github.com/PhilipMay/smart-prom-next/actions/workflows/trivy.yml/badge.svg)](https://github.com/PhilipMay/smart-prom-next/actions/workflows/trivy.yml)

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
It is built for multiple platforms:\
linux/386, linux/amd64, linux/arm/v5, linux/arm/v7, linux/arm64/v8

The second option is an [Alpine](https://www.alpinelinux.org/) based image.
It is built for multiple platforms:\
linux/386, linux/amd64, linux/arm/v6, linux/arm/v7, linux/arm64/v8

## Configuration Options / Environment Variables

smart-prom-next can be configured by the following environment variables:

- `PROMETHEUS_METRIC_PORT` - port number over which the Prometheus metrics are exposed (default: 9902)
- `SMART_INFO_READ_INTERVAL_SECONDS` - time interval in seconds at which the SMART values of the hard disk are read
  (default: 60)

## Docker / docker-compose

The images, which are based on Debian Bullseye slim, can be accessed using:
`ghcr.io/philipmay/smart-prom-next:<version>-slim-bullseye` or `ghcr.io/philipmay/smart-prom-next:latest`

The images, which are based on Alpine, can be accessed using: `ghcr.io/philipmay/smart-prom-next:<version>-alpine`

The latest versions are visible in
[smart-prom-next GitHub packages](https://github.com/PhilipMay/smart-prom-next/pkgs/container/smart-prom-next).

Below is an example of a complete minimal `docker-compose.yml`, how smart-prom-next can be used with [docker-compose](https://docs.docker.com/compose/):

```yaml
version: "3.0"
services:
  smart-prom-next:
    # see https://github.com/PhilipMay/smart-prom-next/pkgs/container/smart-prom-next
    image: ghcr.io/philipmay/smart-prom-next:latest
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

### `smart_prom_smart_status_failed`

The SMART health status of the device. A value of 0 indicates a healthy state.
A value of 1 means that the device has not passed the health check and there is a problem.

List of labels used (description see below): "device", "type", "model", "serial"

### `smart_prom_smartctl_exit_status`

The exit status (aka exit code or return code) of the `smartctl` tool.
Any value other than zero indicates an issue.
A more detailed description can be found in the EXIT STATUS chapter of the
[smartctl man pages](https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in).

List of labels used (description see below): "device", "type", "model", "serial"

### `smart_prom_smart_info`

The SMART Attributes.
A more detailed description can be found in the `-A, --attributes` chapter of the
[smartctl man pages](https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in).

List of labels used (description see below): "device", "type", "model", "serial", "attr_name", "attr_type", "attr_id"

### `smart_prom_nvme_smart_info`

[NVMe](https://en.wikipedia.org/wiki/NVM_Express) specific SMART attributes obtained from
the SMART/Health Information log.
A more detailed description can be found in the `-A, --attributes` chapter of the
[smartctl man pages](https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in).

List of labels used (description see below): "device", "type", "model", "serial", "attr_name"

### `smart_prom_scsi_smart_info`

[SCSI](https://en.wikipedia.org/wiki/SCSI) specific SMART attributes obtained from
the SMART/Health Information log.
A more detailed description can be found in the `-A, --attributes` chapter of the
[smartctl man pages](https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in).

List of labels used (description see below): "device", "type", "model", "serial", "attr_name", "attr_type"

### `smart_prom_temperature`

The temperature values of the device. These include not only the current temperature but also other values.

List of labels used (description see below): "device", "type", "model", "serial", "temperature_type"

### `smart_prom_scrape_iterations_total`

Counter how often the SMART values were scraped.

## Metrics Label

In this project, we use different labels on the metrics. These are described here:

- `device` - device file, e.g.: `/dev/nvme0`, `/dev/sda`
- `type` -  type of the device, e.g.: `ata`, `nvme`, `usbjmicron`
- `model` - model name, e.g.: `KXG6AZNV512G TOSHIBA`, `WDC WD3200BEVT-60ZCT0`
- `serial` - serial number, e.g.: `WD-WXE708D44703`, `Y9SF71LHFWZL`
- `temperature_type` - type of the temperature value, e.g.: `current`, `power_cycle_max`, `lifetime_max`, `op_limit_max`
- `attr_name` - SMART attribute name, e.g.: `raw_read_error_rate`, `reallocated_sector_ct`, `critical_warning`
- `attr_id` - SMART attribute id, e.g.: `1`, `3`, `4`
- `attr_type` - type of the respective SMART attribute - value is one of this: `value`, `worst`, `thresh`, `raw`, `failed_now`, `failed_past` -
  a detailed description can be found in the `-A, --attributes` chapter of the
  [smartctl man pages](https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in)

## Prometheus Alerts

Based on the metrics, [Prometheus alerts](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
can be defined. Below are a few suggestions for `prometheus_rules.yml`:

```yaml
groups:
  - name: alert_rules
    rules:
  
      - alert: DiskFailing
        expr: smart_prom_smart_info{attr_type="failed_now"} == 1
        labels:
          severity: critical
        annotations:
          summary: "disk failing"

      - alert: DiskTemperatureHigh
        expr: smart_prom_temperature{temperature_type="current"} > 50
        labels:
          severity: warning
        annotations:
          summary: "disk temperature > 50"

      - alert: SMARTStatusFailing
        expr: smart_prom_smart_status_failed == 1
        labels:
          severity: critical
        annotations:
          summary: "SMART status failing"
```

## Release History

**2022-07-28 with version `0.0.4`**

- add additional Alpine based image [#40](https://github.com/PhilipMay/smart-prom-next/issues/40)
- fix typo [#42](https://github.com/PhilipMay/smart-prom-next/issues/42)
- make Alpine image smaller [#45](https://github.com/PhilipMay/smart-prom-next/issues/45)
- add -slim-bullseye suffix to image [#44](https://github.com/PhilipMay/smart-prom-next/issues/44)
- improve logs with "error" and "warning" prefix [#43](https://github.com/PhilipMay/smart-prom-next/issues/43)

**2022-07-27 with pre-release version `0.0.4rc1`**

- add additional Alpine based image [#40](https://github.com/PhilipMay/smart-prom-next/issues/40)
- fix typo [#42](https://github.com/PhilipMay/smart-prom-next/issues/42)

**2022-07-20 with version `0.0.3`**

- [add scsi disk handling](https://github.com/PhilipMay/smart-prom-next/issues/12) - thanks to
  [Jopaul-John](https://github.com/Jopaul-John)

**2022-06-23 with version `0.0.2`**

- breaking change on `smart_prom_nvme_smart_info`
- additional `smart_prom_scrape_iterations_total` metric
- more doc

**2022-06-20 with pre-release version `0.0.1rc9`**

- first pre-release

## Special Thanks

A special thanks goes to the following contributors:

- [@Jopaul-John](https://github.com/Jopaul-John) for his help in
  [adding scsi disk handling](https://github.com/PhilipMay/smart-prom-next/issues/12)
- [Michal Harakal (@michalharakal)](https://github.com/michalharakal)
  for the first PR of this project to
  [improve the docker-compose example](https://github.com/PhilipMay/smart-prom-next/pull/29)
- [Diego Heras (@ngosang)](https://github.com/ngosang) for his
  [help in adding the Alpine image](https://github.com/PhilipMay/smart-prom-next/issues/40#issuecomment-1197198019)

## Licensing

Copyright (c) 2022 Philip May

Licensed under the **MIT License** (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License by reviewing the file
[LICENSE](https://github.com/PhilipMay/smart-prom-next/blob/main/LICENSE) in the repository.
