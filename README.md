# S.M.A.R.T. Prometheus Metrics Exporter

## Configuration Options / Environment Variables

smart-prom-next can be configured by the following environment variables:

- `PROMETHEUS_METRIC_PORT`: port number over which the Prometheus metrics are exposed (default: 9902)
- `SMART_INFO_READ_INTERVAL_SECONDS`: time interval in seconds at which the SMART values of the hard disk are read
  (default: 60)

## Licensing

Copyright (c) 2022 Philip May

Licensed under the **MIT License** (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License by reviewing the file
[LICENSE](https://github.com/PhilipMay/smart-prom-next/blob/main/LICENSE) in the repository.
