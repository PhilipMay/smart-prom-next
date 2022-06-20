# S.M.A.R.T. Prometheus Metrics Exporter

## Configuration Options / Environment Variables

smart-prom-next can be configured by the following environment variables:

- `PROMETHEUS_METRIC_PORT`: port number over which the Prometheus metrics are exposed (default: 9902)
- `SMART_INFO_READ_INTERVAL_SECONDS`: time interval in seconds at which the SMART values of the hard disk are read
  (default: 60)

## docker-compose Example

Below is an example of how smart-prom-next can be used with [docker-compose](https://docs.docker.com/compose/):

```yaml
  smart-prom-next:
    # see https://github.com/PhilipMay/smart-prom-next/pkgs/container/smart-prom-next
    image: ghcr.io/philipmay/smart-prom-next:0.0.1rc9
    container_name: "smart-prom-next"
    restart: unless-stopped
    privileged: true
    networks:
      - monitor
```

The `privileged: true` permission is absolutely necessary so that smartctl can also access the hard disks from
within the container.

To adjust the environment variables, the following settings can be added, for example:

```yaml
    environment:
      - PROMETHEUS_METRIC_PORT=9009
      - SMART_INFO_READ_INTERVAL_SECONDS=120
```

## Licensing

Copyright (c) 2022 Philip May

Licensed under the **MIT License** (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License by reviewing the file
[LICENSE](https://github.com/PhilipMay/smart-prom-next/blob/main/LICENSE) in the repository.
