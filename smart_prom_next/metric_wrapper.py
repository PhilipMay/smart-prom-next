# Copyright (c) 2023 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""Wrapper for metrics to add remove functionality."""

import time
from numbers import Number
from typing import Any, List

from prometheus_client import Gauge


class GaugeWrapper:
    def __init__(
        self,
        name: str,
        documentation: str,
        labelnames: List[str],
        max_metric_age: Number,
    ) -> None:
        # TODO: check parameters
        self._gauge = Gauge(name, documentation, labelnames)
        self._labelnames = labelnames
        self._max_metric_age = max_metric_age
        self._metric_to_age = {}

    def remove_old_metrics(self):
        for metric_key, metric_age in self._metric_to_age.copy().items():
            current_metric_age = time.time() - metric_age
            if current_metric_age > self._max_metric_age:
                self._gauge.remove(*metric_key)
                del self._metric_to_age[metric_key]

    def set(self, value: float, **labelkwargs: Any) -> None:
        if len(labelkwargs) != len(self._labelnames):
            raise ValueError("Incorrect label count")
        self._gauge.labels(**labelkwargs).set(value)
        metric_key = tuple(str(labelkwargs[l]) for l in self._labelnames)
        self._metric_to_age[metric_key] = time.time()
        self.remove_old_metrics()