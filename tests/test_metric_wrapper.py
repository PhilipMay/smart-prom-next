# Copyright (c) 2023 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

import time
from math import isclose

from prometheus_client import REGISTRY

from smart_prom_next.metric_wrapper import GaugeWrapper


def test_gauge_is_removed_after_age():
    gw = GaugeWrapper("test_gw", "this is a test", ["a", "b"], 1)

    l1 = {"a": "a1", "b": "b1"}
    gw.set(1, **l1)

    l2 = {"a": "a2", "b": "b2"}
    gw.set(2, **l2)

    g1 = REGISTRY.get_sample_value("test_gw", labels=l1)
    assert g1 is not None
    assert isclose(g1, 1.0)

    g2 = REGISTRY.get_sample_value("test_gw", labels=l2)
    assert g2 is not None
    assert isclose(g2, 2.0)

    time.sleep(0.6)

    gw.set(11, **l1)

    time.sleep(0.6)

    gw.set(12, **l1)

    g1 = REGISTRY.get_sample_value("test_gw", labels=l1)
    assert g1 is not None
    assert isclose(g1, 12.0)

    g2 = REGISTRY.get_sample_value("test_gw", labels=l2)
    assert g2 is None
