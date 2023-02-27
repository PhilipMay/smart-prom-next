# Copyright (c) 2022 - 2023 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

import json
from math import isclose

from json_fixtures import ATA_FAILED_NOW, ATA_FAILED_PAST, NVME, SCSI
from prometheus_client import REGISTRY

from smart_prom_next.smart_prom_next import (
    init_metrics,
    normalize_str,
    scrape_ata_metrics,
    scrape_metrics_for_device,
    scrape_nvme_metrics,
    scrape_scsi_metrics,
    scrape_smart_status,
    scrape_temperature,
)


def test_normalize_str__happy_case():
    string = " AB- ./:#*+~xy "
    output = normalize_str(string)
    assert output == "ab_________xy"


def test_normalize_str__non_str_type():
    string = 77
    output = normalize_str(string)
    assert string == output


def test_scrape_ata_metrics_failed_now():
    device_info = json.loads(ATA_FAILED_NOW)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
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
    assert isclose(smart_prom_smart_info_gauge, 1.0)


def test_scrape_ata_metrics_failed_past():
    device_info = json.loads(ATA_FAILED_PAST)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_ata_metrics(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_info",
        labels={
            "attr_id": "3",
            "attr_name": "spin_up_time",
            "attr_type": "failed_past",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_smart_info_gauge is not None
    assert isclose(smart_prom_smart_info_gauge, 1.0)


def test_scrape_ata_metrics_value():
    device_info = json.loads(ATA_FAILED_PAST)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_ata_metrics(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_info",
        labels={
            "attr_id": "3",
            "attr_name": "spin_up_time",
            "attr_type": "value",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_smart_info_gauge is not None
    assert isclose(smart_prom_smart_info_gauge, 67.0)


def test_scrape_ata_metrics_raw():
    device_info = json.loads(ATA_FAILED_PAST)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_ata_metrics(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_info",
        labels={
            "attr_id": "3",
            "attr_name": "spin_up_time",
            "attr_type": "raw",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_smart_info_gauge is not None
    assert isclose(smart_prom_smart_info_gauge, 10175.0)


def test_scrape_temperature():
    device_info = json.loads(ATA_FAILED_NOW)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_temperature(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_temperature_gauge = REGISTRY.get_sample_value(
        "smart_prom_temperature",
        labels={
            "temperature_type": "current",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_temperature_gauge is not None
    assert isclose(smart_prom_temperature_gauge, 27.0)


def test_scrape_smart_status():
    device_info = json.loads(ATA_FAILED_NOW)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_smart_status(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_smart_status_failed_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_status_failed",
        labels={
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_smart_status_failed_gauge is not None
    assert isclose(smart_prom_smart_status_failed_gauge, 1.0)


def test_scrape_nvme_metrics():
    device_info = json.loads(NVME)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_nvme_metrics(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_nvme_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_nvme_smart_info",
        labels={
            "attr_name": "unsafe_shutdowns",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_nvme_smart_info_gauge is not None
    assert isclose(smart_prom_nvme_smart_info_gauge, 132.0)


def test_scrape_scsi_metrics_write_str_as_float():
    device_info = json.loads(SCSI)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_scsi_metrics(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_scsi_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_scsi_smart_info",
        labels={
            "attr_name": "gigabytes_processed",
            "attr_type": "write",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_scsi_smart_info_gauge is not None
    assert isclose(smart_prom_scsi_smart_info_gauge, 29929.585)


def test_scrape_scsi_metrics_read_str_as_float():
    device_info = json.loads(SCSI)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_scsi_metrics(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_scsi_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_scsi_smart_info",
        labels={
            "attr_name": "gigabytes_processed",
            "attr_type": "read",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_scsi_smart_info_gauge is not None
    assert isclose(smart_prom_scsi_smart_info_gauge, 1661147.727)


def test_scrape_scsi_metrics_read_int():
    device_info = json.loads(SCSI)
    labels = {
        "device": "test_device",
        "type": normalize_str("test_type"),
        "model": "test_model",
        "serial": "test_serial_number",
    }
    init_metrics(30)
    scrape_scsi_metrics(
        device_info=device_info,
        labels=labels,
    )
    smart_prom_scsi_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_scsi_smart_info",
        labels={
            "attr_name": "errors_corrected_by_eccdelayed",
            "attr_type": "read",
            "device": "test_device",
            "type": normalize_str("test_type"),
            "model": "test_model",
            "serial": "test_serial_number",
        },
    )
    assert smart_prom_scsi_smart_info_gauge is not None
    assert isclose(smart_prom_scsi_smart_info_gauge, 173.0)


def test_scrape_metrics_for_device_nvme():
    init_metrics(30)
    scrape_metrics_for_device(
        device_name="test_device",
        device_type="test_type",
        device_info_json=NVME,
        returncode=99,
    )

    # test scrape_nvme_metrics - normal case
    smart_prom_nvme_smart_info_gause = REGISTRY.get_sample_value(
        "smart_prom_nvme_smart_info",
        labels={
            "attr_name": "data_units_written",
            "device": "test_device",
            "type": "test_type",
            "model": "KXG6AZNV512G TOSHIBA",
            "serial": "Y9SF71LHFWZL",
        },
    )
    assert smart_prom_nvme_smart_info_gause is not None
    assert isclose(smart_prom_nvme_smart_info_gause, 13927418.0)

    # test scrape_nvme_metrics - temperature case
    smart_prom_nvme_smart_info_gause = REGISTRY.get_sample_value(
        "smart_prom_nvme_smart_info",
        labels={
            "attr_name": "temperature_sensors_1",
            "device": "test_device",
            "type": "test_type",
            "model": "KXG6AZNV512G TOSHIBA",
            "serial": "Y9SF71LHFWZL",
        },
    )
    assert smart_prom_nvme_smart_info_gause is not None
    assert isclose(smart_prom_nvme_smart_info_gause, 35.0)

    # test scrape_temperature
    smart_prom_temperature_gauge = REGISTRY.get_sample_value(
        "smart_prom_temperature",
        labels={
            "temperature_type": "current",
            "device": "test_device",
            "type": "test_type",
            "model": "KXG6AZNV512G TOSHIBA",
            "serial": "Y9SF71LHFWZL",
        },
    )
    assert smart_prom_temperature_gauge is not None
    assert isclose(smart_prom_temperature_gauge, 35.0)

    # test scrape_smart_status
    smart_prom_smart_status_failed_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_status_failed",
        labels={
            "device": "test_device",
            "type": "test_type",
            "model": "KXG6AZNV512G TOSHIBA",
            "serial": "Y9SF71LHFWZL",
        },
    )
    assert smart_prom_smart_status_failed_gauge is not None
    assert isclose(smart_prom_smart_status_failed_gauge, 0.0)

    # test smart_prom_smartctl_exit_status
    smart_prom_smartctl_exit_status_gauge = REGISTRY.get_sample_value(
        "smart_prom_smartctl_exit_status",
        labels={
            "device": "test_device",
            "type": "test_type",
            "model": "KXG6AZNV512G TOSHIBA",
            "serial": "Y9SF71LHFWZL",
        },
    )
    assert smart_prom_smartctl_exit_status_gauge is not None
    assert isclose(smart_prom_smartctl_exit_status_gauge, 99.0)


def test_scrape_metrics_for_device_ata():
    init_metrics(30)
    scrape_metrics_for_device(
        device_name="test_device",
        device_type="test_type",
        device_info_json=ATA_FAILED_PAST,
        returncode=99,
    )

    # test scrape_ata_metrics - failed past
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

    # test scrape_ata_metrics - thresh
    smart_prom_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_info",
        labels={
            "attr_id": "5",
            "attr_name": "reallocated_sector_ct",
            "attr_type": "thresh",
            "device": "test_device",
            "type": "test_type",
            "model": "SAMSUNG HD204UI",
            "serial": "S2H7J9FB203635",
        },
    )
    assert smart_prom_smart_info_gauge is not None
    assert isclose(smart_prom_smart_info_gauge, 10.0)

    # test scrape_ata_metrics - raw
    smart_prom_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_info",
        labels={
            "attr_id": "9",
            "attr_name": "power_on_hours",
            "attr_type": "raw",
            "device": "test_device",
            "type": "test_type",
            "model": "SAMSUNG HD204UI",
            "serial": "S2H7J9FB203635",
        },
    )
    assert smart_prom_smart_info_gauge is not None
    assert isclose(smart_prom_smart_info_gauge, 3830.0)

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
    smart_prom_smart_status_failed_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_status_failed",
        labels={
            "device": "test_device",
            "type": "test_type",
            "model": "SAMSUNG HD204UI",
            "serial": "S2H7J9FB203635",
        },
    )
    assert smart_prom_smart_status_failed_gauge is not None
    assert isclose(smart_prom_smart_status_failed_gauge, 0.0)

    # test smart_prom_smartctl_exit_status
    smart_prom_smartctl_exit_status_gauge = REGISTRY.get_sample_value(
        "smart_prom_smartctl_exit_status",
        labels={
            "device": "test_device",
            "type": "test_type",
            "model": "SAMSUNG HD204UI",
            "serial": "S2H7J9FB203635",
        },
    )
    assert smart_prom_smartctl_exit_status_gauge is not None
    assert isclose(smart_prom_smartctl_exit_status_gauge, 99.0)


def test_scrape_metrics_for_device_scsi():
    init_metrics(30)
    scrape_metrics_for_device(
        device_name="test_device",
        device_type="test_type",
        device_info_json=SCSI,
        returncode=99,
    )

    # test scrape_ata_metrics
    smart_prom_smart_info_gauge = REGISTRY.get_sample_value(
        "smart_prom_scsi_smart_info",
        labels={
            "attr_name": "errors_corrected_by_eccdelayed",
            "attr_type": "read",
            "device": "test_device",
            "type": "test_type",
            "model": "<model name>",
            "serial": "<serial number>",
        },
    )
    assert smart_prom_smart_info_gauge is not None
    assert isclose(smart_prom_smart_info_gauge, 173.0)

    # test scrape_temperature
    smart_prom_temperature_gauge = REGISTRY.get_sample_value(
        "smart_prom_temperature",
        labels={
            "temperature_type": "current",
            "device": "test_device",
            "type": "test_type",
            "model": "<model name>",
            "serial": "<serial number>",
        },
    )
    assert smart_prom_temperature_gauge is not None
    assert isclose(smart_prom_temperature_gauge, 27.0)

    # test scrape_smart_status
    smart_prom_smart_status_failed_gauge = REGISTRY.get_sample_value(
        "smart_prom_smart_status_failed",
        labels={
            "device": "test_device",
            "type": "test_type",
            "model": "<model name>",
            "serial": "<serial number>",
        },
    )
    assert smart_prom_smart_status_failed_gauge is not None
    assert isclose(smart_prom_smart_status_failed_gauge, 0.0)

    # test smart_prom_smartctl_exit_status
    smart_prom_smartctl_exit_status_gauge = REGISTRY.get_sample_value(
        "smart_prom_smartctl_exit_status",
        labels={
            "device": "test_device",
            "type": "test_type",
            "model": "<model name>",
            "serial": "<serial number>",
        },
    )
    assert smart_prom_smartctl_exit_status_gauge is not None
    assert isclose(smart_prom_smartctl_exit_status_gauge, 99.0)
