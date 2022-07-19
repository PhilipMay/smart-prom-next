# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT


"""JSON fixtures."""


ATA_FAILED_PAST = """
{
  "json_format_version": [
    1,
    0
  ],
  "smartctl": {
    "version": [
      7,
      2
    ],
    "svn_revision": "5155",
    "platform_info": "x86_64-linux-5.10.0-15-amd64",
    "build_info": "(local build)",
    "argv": [
      "smartctl",
      "--json",
      "-x",
      "/dev/sdb"
    ],
    "exit_status": 96
  },
  "device": {
    "name": "/dev/sdb",
    "info_name": "/dev/sdb [USB Sunplus]",
    "type": "usbsunplus",
    "protocol": "ATA"
  },
  "model_family": "SAMSUNG SpinPoint F4 EG (AF)",
  "model_name": "SAMSUNG HD204UI",
  "serial_number": "S2H7J9FB203635",
  "wwn": {
    "naa": 5,
    "oui": 9449,
    "id": 8667472330
  },
  "firmware_version": "1AQ10001",
  "user_capacity": {
    "blocks": 3907029168,
    "bytes": 2000398934016
  },
  "logical_block_size": 512,
  "physical_block_size": 512,
  "rotation_rate": 5400,
  "form_factor": {
    "ata_value": 2,
    "name": "3.5 inches"
  },
  "trim": {
    "supported": false
  },
  "in_smartctl_database": true,
  "ata_version": {
    "string": "ATA8-ACS T13/1699-D revision 6",
    "major_value": 511,
    "minor_value": 40
  },
  "sata_version": {
    "string": "SATA 2.6",
    "value": 31
  },
  "interface_speed": {
    "max": {
      "sata_value": 6,
      "string": "3.0 Gb/s",
      "units_per_second": 30,
      "bits_per_unit": 100000000
    }
  },
  "local_time": {
    "time_t": 1655571110,
    "asctime": "Sat Jun 18 18:51:50 2022 CEST"
  },
  "ata_aam": {
    "enabled": false
  },
  "ata_apm": {
    "enabled": false
  },
  "read_lookahead": {
    "enabled": true
  },
  "write_cache": {
    "enabled": true
  },
  "ata_security": {
    "state": 33,
    "string": "Disabled, NOT FROZEN [SEC1]",
    "enabled": false,
    "frozen": false
  },
  "smart_status": {
    "passed": true
  },
  "ata_smart_data": {
    "offline_data_collection": {
      "status": {
        "value": 0,
        "string": "was never started"
      },
      "completion_seconds": 20280
    },
    "self_test": {
      "status": {
        "value": 0,
        "string": "completed without error",
        "passed": true
      },
      "polling_minutes": {
        "short": 2,
        "extended": 338
      }
    },
    "capabilities": {
      "values": [
        91,
        3
      ],
      "exec_offline_immediate_supported": true,
      "offline_is_aborted_upon_new_cmd": false,
      "offline_surface_scan_supported": true,
      "self_tests_supported": true,
      "conveyance_self_test_supported": false,
      "selective_self_test_supported": true,
      "attribute_autosave_enabled": true,
      "error_logging_supported": true,
      "gp_logging_supported": true
    }
  },
  "ata_sct_capabilities": {
    "value": 63,
    "error_recovery_control_supported": true,
    "feature_control_supported": true,
    "data_table_supported": true
  },
  "ata_smart_attributes": {
    "revision": 16,
    "table": [
      {
        "id": 1,
        "name": "Raw_Read_Error_Rate",
        "value": 100,
        "worst": 100,
        "thresh": 51,
        "when_failed": "",
        "flags": {
          "value": 47,
          "string": "POSR-K ",
          "prefailure": true,
          "updated_online": true,
          "performance": true,
          "error_rate": true,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 2,
        "name": "Throughput_Performance",
        "value": 56,
        "worst": 56,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 38,
          "string": "-OS--K ",
          "prefailure": false,
          "updated_online": true,
          "performance": true,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 18475,
          "string": "18475"
        }
      },
      {
        "id": 3,
        "name": "Spin_Up_Time",
        "value": 67,
        "worst": 1,
        "thresh": 25,
        "when_failed": "past",
        "flags": {
          "value": 35,
          "string": "PO---K ",
          "prefailure": true,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 10175,
          "string": "10175"
        }
      },
      {
        "id": 4,
        "name": "Start_Stop_Count",
        "value": 97,
        "worst": 97,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 3860,
          "string": "3860"
        }
      },
      {
        "id": 5,
        "name": "Reallocated_Sector_Ct",
        "value": 252,
        "worst": 252,
        "thresh": 10,
        "when_failed": "",
        "flags": {
          "value": 51,
          "string": "PO--CK ",
          "prefailure": true,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 7,
        "name": "Seek_Error_Rate",
        "value": 252,
        "worst": 252,
        "thresh": 51,
        "when_failed": "",
        "flags": {
          "value": 46,
          "string": "-OSR-K ",
          "prefailure": false,
          "updated_online": true,
          "performance": true,
          "error_rate": true,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 8,
        "name": "Seek_Time_Performance",
        "value": 252,
        "worst": 252,
        "thresh": 15,
        "when_failed": "",
        "flags": {
          "value": 36,
          "string": "--S--K ",
          "prefailure": false,
          "updated_online": false,
          "performance": true,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 9,
        "name": "Power_On_Hours",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 3830,
          "string": "3830"
        }
      },
      {
        "id": 10,
        "name": "Spin_Retry_Count",
        "value": 252,
        "worst": 252,
        "thresh": 51,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 11,
        "name": "Calibration_Retry_Count",
        "value": 252,
        "worst": 252,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 12,
        "name": "Power_Cycle_Count",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 79,
          "string": "79"
        }
      },
      {
        "id": 181,
        "name": "Program_Fail_Cnt_Total",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 34,
          "string": "-O---K ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 1169339,
          "string": "1169339"
        }
      },
      {
        "id": 191,
        "name": "G-Sense_Error_Rate",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 34,
          "string": "-O---K ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 4,
          "string": "4"
        }
      },
      {
        "id": 192,
        "name": "Power-Off_Retract_Count",
        "value": 252,
        "worst": 252,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 34,
          "string": "-O---K ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 194,
        "name": "Temperature_Celsius",
        "value": 64,
        "worst": 64,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 2,
          "string": "-O---- ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": false,
          "auto_keep": false
        },
        "raw": {
          "value": 158914314267,
          "string": "27 (Min/Max 8/37)"
        }
      },
      {
        "id": 195,
        "name": "Hardware_ECC_Recovered",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 58,
          "string": "-O-RCK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": true,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 196,
        "name": "Reallocated_Event_Count",
        "value": 252,
        "worst": 252,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 197,
        "name": "Current_Pending_Sector",
        "value": 252,
        "worst": 252,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 198,
        "name": "Offline_Uncorrectable",
        "value": 252,
        "worst": 252,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 48,
          "string": "----CK ",
          "prefailure": false,
          "updated_online": false,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 199,
        "name": "UDMA_CRC_Error_Count",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 54,
          "string": "-OS-CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": true,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 1,
          "string": "1"
        }
      },
      {
        "id": 200,
        "name": "Multi_Zone_Error_Rate",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 42,
          "string": "-O-R-K ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": true,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 5,
          "string": "5"
        }
      },
      {
        "id": 223,
        "name": "Load_Retry_Count",
        "value": 252,
        "worst": 252,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 225,
        "name": "Load_Cycle_Count",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 3868,
          "string": "3868"
        }
      }
    ]
  },
  "power_on_time": {
    "hours": 3830
  },
  "power_cycle_count": 79,
  "temperature": {
    "current": 27,
    "power_cycle_min": 22,
    "power_cycle_max": 28,
    "lifetime_min": 8,
    "lifetime_max": 62,
    "op_limit_max": 80,
    "op_limit_min": -5,
    "limit_min": -10,
    "limit_max": 85
  },
  "ata_log_directory": {
    "gp_dir_version": 1,
    "smart_dir_version": 1,
    "smart_dir_multi_sector": true,
    "table": [
      {
        "address": 0,
        "name": "Log Directory",
        "read": true,
        "write": false,
        "gp_sectors": 1,
        "smart_sectors": 1
      },
      {
        "address": 1,
        "name": "Summary SMART error log",
        "read": true,
        "write": false,
        "smart_sectors": 1
      },
      {
        "address": 2,
        "name": "Comprehensive SMART error log",
        "read": true,
        "write": false,
        "smart_sectors": 2
      },
      {
        "address": 3,
        "name": "Ext. Comprehensive SMART error log",
        "read": true,
        "write": false,
        "gp_sectors": 2
      },
      {
        "address": 6,
        "name": "SMART self-test log",
        "read": true,
        "write": false,
        "smart_sectors": 1
      },
      {
        "address": 7,
        "name": "Extended self-test log",
        "read": true,
        "write": false,
        "gp_sectors": 2
      },
      {
        "address": 8,
        "name": "Power Conditions log",
        "read": true,
        "write": false,
        "gp_sectors": 2
      },
      {
        "address": 9,
        "name": "Selective self-test log",
        "read": true,
        "write": true,
        "smart_sectors": 1
      },
      {
        "address": 16,
        "name": "NCQ Command Error log",
        "read": true,
        "write": false,
        "gp_sectors": 1
      },
      {
        "address": 17,
        "name": "SATA Phy Event Counters log",
        "read": true,
        "write": false,
        "gp_sectors": 1
      },
      {
        "address": 128,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 129,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 130,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 131,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 132,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 133,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 134,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 135,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 136,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 137,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 138,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 139,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 140,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 141,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 142,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 143,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 144,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 145,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 146,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 147,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 148,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 149,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 150,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 151,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 152,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 153,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 154,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 155,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 156,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 157,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 158,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 159,
        "name": "Host vendor specific log",
        "read": true,
        "write": true,
        "gp_sectors": 16,
        "smart_sectors": 16
      },
      {
        "address": 224,
        "name": "SCT Command/Status",
        "read": true,
        "write": true,
        "gp_sectors": 1,
        "smart_sectors": 1
      },
      {
        "address": 225,
        "name": "SCT Data Transfer",
        "read": true,
        "write": true,
        "gp_sectors": 1,
        "smart_sectors": 1
      }
    ]
  },
  "ata_smart_error_log": {
    "extended": {
      "revision": 1,
      "sectors": 2,
      "count": 1,
      "logged_count": 1,
      "table": [
        {
          "error_number": 1,
          "log_index": 0,
          "lifetime_hours": 3502,
          "device_state": {
            "value": 3,
            "string": "active or idle"
          },
          "completion_registers": {
            "error": 132,
            "status": 81,
            "count": 136,
            "lba": 1126194944,
            "device": 64,
            "device_control": 0
          },
          "error_description": "Error: ICRC, ABRT 136 sectors at LBA = 0x43205f00 = 1126194944",
          "previous_commands": [
            {
              "registers": {
                "command": 37,
                "features": 37632,
                "count": 224,
                "lba": 1126194856,
                "device": 64,
                "device_control": 0
              },
              "powerup_milliseconds": 48,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 37,
                "features": 37632,
                "count": 8,
                "lba": 1126194832,
                "device": 64,
                "device_control": 0
              },
              "powerup_milliseconds": 48,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 37,
                "features": 37632,
                "count": 8,
                "lba": 1126194848,
                "device": 64,
                "device_control": 0
              },
              "powerup_milliseconds": 48,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 37,
                "features": 37632,
                "count": 8,
                "lba": 1126194840,
                "device": 64,
                "device_control": 0
              },
              "powerup_milliseconds": 48,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 37,
                "features": 37632,
                "count": 240,
                "lba": 1126194592,
                "device": 64,
                "device_control": 0
              },
              "powerup_milliseconds": 48,
              "command_name": "READ DMA EXT"
            }
          ]
        }
      ]
    }
  },
  "ata_smart_self_test_log": {
    "extended": {
      "revision": 1,
      "sectors": 2,
      "table": [
        {
          "type": {
            "value": 2,
            "string": "Extended offline"
          },
          "status": {
            "value": 0,
            "string": "Completed without error",
            "passed": true
          },
          "lifetime_hours": 3624
        },
        {
          "type": {
            "value": 1,
            "string": "Short offline"
          },
          "status": {
            "value": 0,
            "string": "Completed without error",
            "passed": true
          },
          "lifetime_hours": 33
        },
        {
          "type": {
            "value": 1,
            "string": "Short offline"
          },
          "status": {
            "value": 0,
            "string": "Completed without error",
            "passed": true
          },
          "lifetime_hours": 1
        }
      ],
      "count": 3,
      "error_count_total": 0,
      "error_count_outdated": 0
    }
  },
  "ata_smart_selective_self_test_log": {
    "revision": 0,
    "table": [
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Completed",
          "remaining_percent": 0
        },
        "current_lba_min": 0,
        "current_lba_max": 65535
      },
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      },
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      },
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      },
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      }
    ],
    "flags": {
      "value": 0,
      "remainder_scan_enabled": false
    },
    "power_up_scan_resume_minutes": 0
  },
  "ata_sct_status": {
    "format_version": 2,
    "sct_version": 256,
    "device_state": {
      "value": 0,
      "string": "Active"
    },
    "temperature": {
      "current": 27,
      "power_cycle_min": 22,
      "power_cycle_max": 28,
      "lifetime_min": 8,
      "lifetime_max": 62,
      "op_limit_max": 80,
      "under_limit_count": 0,
      "over_limit_count": 0
    }
  },
  "ata_sct_temperature_history": {
    "version": 2,
    "sampling_period_minutes": 5,
    "logging_interval_minutes": 5,
    "temperature": {
      "op_limit_min": -5,
      "op_limit_max": 80,
      "limit_min": -10,
      "limit_max": 85
    },
    "size": 128,
    "index": 48,
    "table": [
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      28,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      28,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27,
      27
    ]
  },
  "ata_sct_erc": {
    "read": {
      "enabled": false
    },
    "write": {
      "enabled": false
    }
  },
  "sata_phy_event_counters": {
    "table": [
      {
        "id": 1,
        "name": "Command failed due to ICRC error",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 2,
        "name": "R_ERR response for data FIS",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 3,
        "name": "R_ERR response for device-to-host data FIS",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 4,
        "name": "R_ERR response for host-to-device data FIS",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 5,
        "name": "R_ERR response for non-data FIS",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 6,
        "name": "R_ERR response for device-to-host non-data FIS",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 7,
        "name": "R_ERR response for host-to-device non-data FIS",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 8,
        "name": "Device-to-host non-data FIS retries",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 9,
        "name": "Transition from drive PhyRdy to drive PhyNRdy",
        "size": 4,
        "value": 1,
        "overflow": false
      },
      {
        "id": 10,
        "name": "Device-to-host register FISes sent due to a COMRESET",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 11,
        "name": "CRC errors within host-to-device FIS",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 13,
        "name": "Non-CRC errors within host-to-device FIS",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 15,
        "name": "R_ERR response for host-to-device data FIS, CRC",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 16,
        "name": "R_ERR response for host-to-device data FIS, non-CRC",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 18,
        "name": "R_ERR response for host-to-device non-data FIS, CRC",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 19,
        "name": "R_ERR response for host-to-device non-data FIS, non-CRC",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36352,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36353,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36354,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36355,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36356,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36357,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36358,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36359,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36360,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36361,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36362,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36363,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36364,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36365,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36366,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36367,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36368,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      },
      {
        "id": 36369,
        "name": "Vendor specific",
        "size": 4,
        "value": 0,
        "overflow": false
      }
    ],
    "reset": false
  }
}
"""


ATA_FAILED_NOW = """
{
  "json_format_version": [
    1,
    0
  ],
  "smartctl": {
    "version": [
      7,
      3
    ],
    "svn_revision": "5338",
    "platform_info": "x86_64-linux-5.18.2-arch1-1",
    "build_info": "(local build)",
    "argv": [
      "smartctl",
      "-a",
      "/dev/sdb",
      "--json"
    ],
    "drive_database_version": {
      "string": "7.3/5319"
    },
    "exit_status": 216
  },
  "local_time": {
    "time_t": 1655619202,
    "asctime": "Sun Jun 19 08:13:22 2022 CEST"
  },
  "device": {
    "name": "/dev/sdb",
    "info_name": "/dev/sdb [USB JMicron]",
    "type": "usbjmicron",
    "protocol": "ATA"
  },
  "model_family": "Western Digital Scorpio Blue Serial ATA",
  "model_name": "WDC WD3200BEVT-60ZCT0",
  "serial_number": "WD-WXE708D44602",
  "wwn": {
    "naa": 5,
    "oui": 5358,
    "id": 8620323940
  },
  "firmware_version": "12.01A12",
  "user_capacity": {
    "blocks": 625142448,
    "bytes": 320072933376
  },
  "logical_block_size": 512,
  "physical_block_size": 512,
  "rotation_rate": 5400,
  "trim": {
    "supported": false
  },
  "in_smartctl_database": true,
  "ata_version": {
    "string": "ATA8-ACS (minor revision not indicated)",
    "major_value": 510,
    "minor_value": 0
  },
  "sata_version": {
    "string": "SATA 2.5",
    "value": 14
  },
  "interface_speed": {
    "max": {
      "sata_value": 6,
      "string": "3.0 Gb/s",
      "units_per_second": 30,
      "bits_per_unit": 100000000
    }
  },
  "smart_support": {
    "available": true,
    "enabled": true
  },
  "smart_status": {
    "passed": false
  },
  "ata_smart_data": {
    "offline_data_collection": {
      "status": {
        "value": 0,
        "string": "was never started"
      },
      "completion_seconds": 10800
    },
    "self_test": {
      "status": {
        "value": 0,
        "string": "completed without error",
        "passed": true
      },
      "polling_minutes": {
        "short": 2,
        "extended": 127
      }
    },
    "capabilities": {
      "values": [
        81,
        3
      ],
      "exec_offline_immediate_supported": true,
      "offline_is_aborted_upon_new_cmd": false,
      "offline_surface_scan_supported": false,
      "self_tests_supported": true,
      "conveyance_self_test_supported": false,
      "selective_self_test_supported": true,
      "attribute_autosave_enabled": true,
      "error_logging_supported": true,
      "gp_logging_supported": true
    }
  },
  "ata_sct_capabilities": {
    "value": 12351,
    "error_recovery_control_supported": true,
    "feature_control_supported": true,
    "data_table_supported": true
  },
  "ata_smart_attributes": {
    "revision": 16,
    "table": [
      {
        "id": 1,
        "name": "Raw_Read_Error_Rate",
        "value": 200,
        "worst": 200,
        "thresh": 51,
        "when_failed": "",
        "flags": {
          "value": 47,
          "string": "POSR-K ",
          "prefailure": true,
          "updated_online": true,
          "performance": true,
          "error_rate": true,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 129,
          "string": "129"
        }
      },
      {
        "id": 3,
        "name": "Spin_Up_Time",
        "value": 186,
        "worst": 185,
        "thresh": 21,
        "when_failed": "",
        "flags": {
          "value": 39,
          "string": "POS--K ",
          "prefailure": true,
          "updated_online": true,
          "performance": true,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 1691,
          "string": "1691"
        }
      },
      {
        "id": 4,
        "name": "Start_Stop_Count",
        "value": 92,
        "worst": 92,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 8971,
          "string": "8971"
        }
      },
      {
        "id": 5,
        "name": "Reallocated_Sector_Ct",
        "value": 133,
        "worst": 133,
        "thresh": 140,
        "when_failed": "now",
        "flags": {
          "value": 51,
          "string": "PO--CK ",
          "prefailure": true,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 535,
          "string": "535"
        }
      },
      {
        "id": 7,
        "name": "Seek_Error_Rate",
        "value": 100,
        "worst": 253,
        "thresh": 51,
        "when_failed": "",
        "flags": {
          "value": 47,
          "string": "POSR-K ",
          "prefailure": true,
          "updated_online": true,
          "performance": true,
          "error_rate": true,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 9,
        "name": "Power_On_Hours",
        "value": 78,
        "worst": 78,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 16402,
          "string": "16402"
        }
      },
      {
        "id": 10,
        "name": "Spin_Retry_Count",
        "value": 100,
        "worst": 100,
        "thresh": 51,
        "when_failed": "",
        "flags": {
          "value": 51,
          "string": "PO--CK ",
          "prefailure": true,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 11,
        "name": "Calibration_Retry_Count",
        "value": 100,
        "worst": 100,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 12,
        "name": "Power_Cycle_Count",
        "value": 97,
        "worst": 97,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 3440,
          "string": "3440"
        }
      },
      {
        "id": 187,
        "name": "Reported_Uncorrect",
        "value": 98,
        "worst": 36,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 84,
          "string": "84"
        }
      },
      {
        "id": 188,
        "name": "Command_Timeout",
        "value": 100,
        "worst": 94,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 132,
          "string": "132"
        }
      },
      {
        "id": 190,
        "name": "Airflow_Temperature_Cel",
        "value": 73,
        "worst": 31,
        "thresh": 40,
        "when_failed": "past",
        "flags": {
          "value": 34,
          "string": "-O---K ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 27,
          "string": "27"
        }
      },
      {
        "id": 192,
        "name": "Power-Off_Retract_Count",
        "value": 200,
        "worst": 200,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 93,
          "string": "93"
        }
      },
      {
        "id": 193,
        "name": "Load_Cycle_Count",
        "value": 153,
        "worst": 153,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 141118,
          "string": "141118"
        }
      },
      {
        "id": 194,
        "name": "Temperature_Celsius",
        "value": 120,
        "worst": 78,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 34,
          "string": "-O---K ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": false,
          "auto_keep": true
        },
        "raw": {
          "value": 27,
          "string": "27"
        }
      },
      {
        "id": 196,
        "name": "Reallocated_Event_Count",
        "value": 199,
        "worst": 199,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 1,
          "string": "1"
        }
      },
      {
        "id": 197,
        "name": "Current_Pending_Sector",
        "value": 200,
        "worst": 200,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 1,
          "string": "1"
        }
      },
      {
        "id": 198,
        "name": "Offline_Uncorrectable",
        "value": 100,
        "worst": 253,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 48,
          "string": "----CK ",
          "prefailure": false,
          "updated_online": false,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 199,
        "name": "UDMA_CRC_Error_Count",
        "value": 200,
        "worst": 200,
        "thresh": 0,
        "when_failed": "",
        "flags": {
          "value": 50,
          "string": "-O--CK ",
          "prefailure": false,
          "updated_online": true,
          "performance": false,
          "error_rate": false,
          "event_count": true,
          "auto_keep": true
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      },
      {
        "id": 200,
        "name": "Multi_Zone_Error_Rate",
        "value": 100,
        "worst": 253,
        "thresh": 51,
        "when_failed": "",
        "flags": {
          "value": 9,
          "string": "P--R-- ",
          "prefailure": true,
          "updated_online": false,
          "performance": false,
          "error_rate": true,
          "event_count": false,
          "auto_keep": false
        },
        "raw": {
          "value": 0,
          "string": "0"
        }
      }
    ]
  },
  "power_on_time": {
    "hours": 16402
  },
  "power_cycle_count": 3440,
  "temperature": {
    "current": 27
  },
  "ata_smart_error_log": {
    "summary": {
      "revision": 1,
      "count": 84,
      "logged_count": 5,
      "table": [
        {
          "error_number": 84,
          "lifetime_hours": 16402,
          "completion_registers": {
            "error": 64,
            "status": 81,
            "count": 8,
            "lba": 4385280,
            "device": 224
          },
          "error_description": "Error: UNC 8 sectors at LBA = 0x0042ea00 = 4385280",
          "previous_commands": [
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 4385280,
                "device": 37,
                "device_control": 0
              },
              "powerup_milliseconds": 8145,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 4385280,
                "device": 37,
                "device_control": 0
              },
              "powerup_milliseconds": 5093,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 1,
                "lba": 0,
                "device": 0,
                "device_control": 0
              },
              "powerup_milliseconds": 5074,
              "command_name": "IDENTIFY DEVICE"
            },
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 0,
                "device": 0,
                "device_control": 0
              },
              "powerup_milliseconds": 5005,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 239,
                "features": 3,
                "count": 69,
                "lba": 0,
                "device": 0,
                "device_control": 0
              },
              "powerup_milliseconds": 3563,
              "command_name": "SET FEATURES [Set transfer mode]"
            }
          ]
        },
        {
          "error_number": 83,
          "lifetime_hours": 16402,
          "completion_registers": {
            "error": 64,
            "status": 81,
            "count": 8,
            "lba": 4385280,
            "device": 224
          },
          "error_description": "Error: UNC 8 sectors at LBA = 0x0042ea00 = 4385280",
          "previous_commands": [
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 4385280,
                "device": 37,
                "device_control": 0
              },
              "powerup_milliseconds": 5093,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 1,
                "lba": 0,
                "device": 0,
                "device_control": 0
              },
              "powerup_milliseconds": 5074,
              "command_name": "IDENTIFY DEVICE"
            },
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 0,
                "device": 0,
                "device_control": 0
              },
              "powerup_milliseconds": 5005,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 239,
                "features": 3,
                "count": 69,
                "lba": 0,
                "device": 0,
                "device_control": 0
              },
              "powerup_milliseconds": 3563,
              "command_name": "SET FEATURES [Set transfer mode]"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 0,
                "lba": 0,
                "device": 0,
                "device_control": 0
              },
              "powerup_milliseconds": 3555,
              "command_name": "IDENTIFY DEVICE"
            }
          ]
        },
        {
          "error_number": 82,
          "lifetime_hours": 16397,
          "completion_registers": {
            "error": 64,
            "status": 81,
            "count": 8,
            "lba": 8049112,
            "device": 224
          },
          "error_description": "Error: UNC 8 sectors at LBA = 0x007ad1d8 = 8049112",
          "previous_commands": [
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 8049112,
                "device": 29,
                "device_control": 8
              },
              "powerup_milliseconds": 860418758,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 0,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860418731,
              "command_name": "IDENTIFY DEVICE"
            },
            {
              "registers": {
                "command": 239,
                "features": 3,
                "count": 69,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860418731,
              "command_name": "SET FEATURES [Set transfer mode]"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 0,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860418717,
              "command_name": "IDENTIFY DEVICE"
            },
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 8049112,
                "device": 29,
                "device_control": 8
              },
              "powerup_milliseconds": 860414879,
              "command_name": "READ DMA EXT"
            }
          ]
        },
        {
          "error_number": 81,
          "lifetime_hours": 16397,
          "completion_registers": {
            "error": 64,
            "status": 81,
            "count": 8,
            "lba": 8049112,
            "device": 224
          },
          "error_description": "Error: UNC 8 sectors at LBA = 0x007ad1d8 = 8049112",
          "previous_commands": [
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 8049112,
                "device": 29,
                "device_control": 8
              },
              "powerup_milliseconds": 860414879,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 0,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860414852,
              "command_name": "IDENTIFY DEVICE"
            },
            {
              "registers": {
                "command": 239,
                "features": 3,
                "count": 69,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860414852,
              "command_name": "SET FEATURES [Set transfer mode]"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 0,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860414838,
              "command_name": "IDENTIFY DEVICE"
            },
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 8049112,
                "device": 29,
                "device_control": 8
              },
              "powerup_milliseconds": 860410990,
              "command_name": "READ DMA EXT"
            }
          ]
        },
        {
          "error_number": 80,
          "lifetime_hours": 16397,
          "completion_registers": {
            "error": 64,
            "status": 81,
            "count": 8,
            "lba": 8049112,
            "device": 224
          },
          "error_description": "Error: UNC 8 sectors at LBA = 0x007ad1d8 = 8049112",
          "previous_commands": [
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 8049112,
                "device": 29,
                "device_control": 8
              },
              "powerup_milliseconds": 860410990,
              "command_name": "READ DMA EXT"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 0,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860410963,
              "command_name": "IDENTIFY DEVICE"
            },
            {
              "registers": {
                "command": 239,
                "features": 3,
                "count": 69,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860410963,
              "command_name": "SET FEATURES [Set transfer mode]"
            },
            {
              "registers": {
                "command": 236,
                "features": 0,
                "count": 0,
                "lba": 0,
                "device": 0,
                "device_control": 8
              },
              "powerup_milliseconds": 860410949,
              "command_name": "IDENTIFY DEVICE"
            },
            {
              "registers": {
                "command": 37,
                "features": 0,
                "count": 8,
                "lba": 8049112,
                "device": 29,
                "device_control": 8
              },
              "powerup_milliseconds": 860407101,
              "command_name": "READ DMA EXT"
            }
          ]
        }
      ]
    }
  },
  "ata_smart_self_test_log": {
    "standard": {
      "revision": 1,
      "table": [
        {
          "type": {
            "value": 1,
            "string": "Short offline"
          },
          "status": {
            "value": 121,
            "string": "Completed: read failure",
            "remaining_percent": 90,
            "passed": false
          },
          "lifetime_hours": 16402,
          "lba": 494591083
        },
        {
          "type": {
            "value": 2,
            "string": "Extended offline"
          },
          "status": {
            "value": 121,
            "string": "Completed: read failure",
            "remaining_percent": 90,
            "passed": false
          },
          "lifetime_hours": 16400,
          "lba": 494591083
        },
        {
          "type": {
            "value": 1,
            "string": "Short offline"
          },
          "status": {
            "value": 121,
            "string": "Completed: read failure",
            "remaining_percent": 90,
            "passed": false
          },
          "lifetime_hours": 16400,
          "lba": 494591083
        }
      ],
      "count": 3,
      "error_count_total": 3,
      "error_count_outdated": 0
    }
  },
  "ata_smart_selective_self_test_log": {
    "revision": 1,
    "table": [
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      },
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      },
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      },
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      },
      {
        "lba_min": 0,
        "lba_max": 0,
        "status": {
          "value": 0,
          "string": "Not_testing"
        }
      }
    ],
    "flags": {
      "value": 0,
      "remainder_scan_enabled": false
    },
    "power_up_scan_resume_minutes": 0
  }
}
"""


NVME = """
{
  "json_format_version": [
    1,
    0
  ],
  "smartctl": {
    "version": [
      7,
      3
    ],
    "svn_revision": "5338",
    "platform_info": "x86_64-linux-5.18.2-arch1-1",
    "build_info": "(local build)",
    "argv": [
      "smartctl",
      "-x",
      "--json",
      "/dev/nvme0"
    ],
    "exit_status": 0
  },
  "local_time": {
    "time_t": 1655567945,
    "asctime": "Sat Jun 18 17:59:05 2022 CEST"
  },
  "device": {
    "name": "/dev/nvme0",
    "info_name": "/dev/nvme0",
    "type": "nvme",
    "protocol": "NVMe"
  },
  "model_name": "KXG6AZNV512G TOSHIBA",
  "serial_number": "Y9SF71LHFWZL",
  "firmware_version": "5108AGLA",
  "nvme_pci_vendor": {
    "id": 4473,
    "subsystem_id": 4473
  },
  "nvme_ieee_oui_identifier": 9233294,
  "nvme_total_capacity": 512110190592,
  "nvme_unallocated_capacity": 0,
  "nvme_controller_id": 0,
  "nvme_version": {
    "string": "1.3",
    "value": 66304
  },
  "nvme_number_of_namespaces": 1,
  "nvme_namespaces": [
    {
      "id": 1,
      "size": {
        "blocks": 1000215216,
        "bytes": 512110190592
      },
      "capacity": {
        "blocks": 1000215216,
        "bytes": 512110190592
      },
      "utilization": {
        "blocks": 1000215216,
        "bytes": 512110190592
      },
      "formatted_lba_size": 512,
      "eui64": {
        "oui": 9233294,
        "ext_id": 21476127755
      }
    }
  ],
  "user_capacity": {
    "blocks": 1000215216,
    "bytes": 512110190592
  },
  "logical_block_size": 512,
  "smart_support": {
    "available": true,
    "enabled": true
  },
  "smart_status": {
    "passed": true,
    "nvme": {
      "value": 0
    }
  },
  "nvme_smart_health_information_log": {
    "critical_warning": 0,
    "temperature": 35,
    "available_spare": 100,
    "available_spare_threshold": 10,
    "percentage_used": 3,
    "data_units_read": 11686529,
    "data_units_written": 13927418,
    "host_reads": 340880444,
    "host_writes": 180419925,
    "controller_busy_time": 391,
    "power_cycles": 3021,
    "power_on_hours": 1767,
    "unsafe_shutdowns": 132,
    "media_errors": 0,
    "num_err_log_entries": 0,
    "warning_temp_time": 0,
    "critical_comp_time": 0,
    "temperature_sensors": [
      35
    ]
  },
  "temperature": {
    "current": 35
  },
  "power_cycle_count": 3021,
  "power_on_time": {
    "hours": 1767
  }
}
"""
