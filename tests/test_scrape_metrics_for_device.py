# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT


from json_fixtures import ATA_FAILED_PAST
from prometheus_client import REGISTRY

from smart_prom_next.smart_prom_next import scrape_metrics_for_device


# TODO: integrate this with test_smart_prom_next.py again
# this is a hack - no other tests must be executed in this script
# https://stackoverflow.com/questions/73198616/how-do-i-reset-python-runtime-between-pytest-test-functions?utm_source=pocket_mylist


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
