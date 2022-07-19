"""JSON fixtures."""

ATA_FAILES_NOW = """
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
