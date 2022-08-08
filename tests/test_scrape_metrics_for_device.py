# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT
from math import isclose

from json_fixtures import ATA_FAILED_PAST
from prometheus_client import REGISTRY

from smart_prom_next.smart_prom_next import scrape_metrics_for_device


# This function must remain the only one in this module.
def test_scrape_metrics_for_device_ata():
    scrape_metrics_for_device(
        device_name="test_device",
        device_type="test_type",
        device_info_json=ATA_FAILED_PAST,
        returncode=0,
    )
    metric_names = [metric.name for metric in REGISTRY.collect()]
    # assert "smart_prom_scrape_iterations_total" in metric_names  # this is not set for this test
    assert "smart_prom_temperature" in metric_names
    assert "smart_prom_smart_status_failed" in metric_names
    assert "smart_prom_smartctl_exit_status" in metric_names
    assert "smart_prom_nvme_smart_info" not in metric_names
    assert "smart_prom_scsi_smart_info" not in metric_names
    assert "smart_prom_smart_info" in metric_names

    # test scrape_ata_metrics
    smart_prom_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_info",
        labels={
            "attr_id": "3",
            "attr_name": "spin_up_time",
            "attr_type": "failed_past",
            "device": "test_device",
            "type": "test_type",
            "model": "SAMSUNG HD204UI",
            "serial": "S2H7J9FB203635",
        },
    )
    assert smart_prom_smart_info_gauge is not None
    assert isclose(smart_prom_smart_info_gauge, 1.0)

    # test scrape_temperature
    smart_prom_temperature_gauge = REGISTRY.get_sample_value(
        "smart_prom_temperature",
        labels={
            "temperature_type": "current",
            "device": "test_device",
            "type": "test_type",
            "model": "SAMSUNG HD204UI",
            "serial": "S2H7J9FB203635",
        },
    )
    assert smart_prom_temperature_gauge is not None
    assert isclose(smart_prom_temperature_gauge, 27.0)

    # test scrape_smart_status

    # test smart_prom_smartctl_exit_status
