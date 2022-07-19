# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT


import json

from json_fixtures import ATA_FAILES_NOW
from prometheus_client import REGISTRY

from smart_prom_next.smart_prom_next import normalize_str, scrape_ata_metrics


def test_normalize_str__happy_case():
    string = " AB- ./:#*+~xy "
    output = normalize_str(string)
    assert output == "ab_________xy"


def test_normalize_str__non_str_type():
    string = 77
    output = normalize_str(string)
    assert string == output


def test_scrape_ata_metrics_failed_now():
    device_info = json.loads(ATA_FAILES_NOW)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    scrape_ata_metrics(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_info",
        labels={
            "attr_id": "5",
            "attr_name": "reallocated_sector_ct",
            "attr_type": "failed_now",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_smart_info_gauge is not None
    assert smart_prom_smart_info_gauge == 1
