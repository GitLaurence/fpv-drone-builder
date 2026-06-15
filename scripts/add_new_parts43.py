#!/usr/bin/env python3
"""Add 43rd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "darwinfpv-dart-frame",
        "category": "frame",
        "name": "DART 5\" Frame",
        "brand": "DarwinFPV",
        "price_php": 1980,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DarwinFPV+DART+5+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=darwinfpv+dart"
        }
    },
    {
        "id": "flywoo-nin-2207-1800kv-v2",
        "category": "motor",
        "name": "NIN 2207 1800KV V2",
        "brand": "Flywoo",
        "price_php": 1450,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+NIN+2207+1800KV+V2",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "tmotor-f55a-pro-50a-esc",
        "category": "esc",
        "name": "F55A Pro 50A 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 3650,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F55A+Pro+50A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "diatone-mamba-f405-mk2-fc",
        "category": "fc",
        "name": "MAMBA F405 MK2 Flight Controller",
        "brand": "Diatone",
        "price_php": 2480,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F405+MK2+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/products/mamba-f405-mk2-flight-controller"
        }
    },
    {
        "id": "hqprop-ethix-s5-propeller",
        "category": "propeller",
        "name": "Ethix S5 5\" Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 260,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S5+Propeller",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "grey",
                "black",
                "white"
            ]
        }
    },
    {
        "id": "runcam-racer-nano-3-camera",
        "category": "camera",
        "name": "Racer Nano 3 FPV Camera",
        "brand": "RunCam",
        "price_php": 1650,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Racer+Nano+3+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "rush-tank-solo-5800-vtx",
        "category": "vtx",
        "name": "Tank Solo 5.8GHz VTX",
        "brand": "RUSH",
        "price_php": 2800,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RUSH+Tank+Solo+5.8GHz+VTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "5.8GHz 40CH",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-rline-4-0-1300mah-6s130c",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S 130C LiPo",
        "brand": "Tattu",
        "price_php": 2480,
        "weight_g": 235,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Tattu+R-Line+4.0+1300mAh+6S+130C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-elrs-ep2-rx",
        "category": "receiver",
        "name": "ELRS EP2 Nano Receiver",
        "brand": "Happymodel",
        "price_php": 850,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Happymodel+ELRS+EP2+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "holybro-micro-m9n-gps-module",
        "category": "gps",
        "name": "Micro M9N GPS Module",
        "brand": "Holybro",
        "price_php": 1980,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Micro+M9N+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "lumenier-axii2-cyl-antenna",
        "category": "antenna",
        "name": "AXII 2 Cylindrical 5.8GHz Antenna",
        "brand": "Lumenier",
        "price_php": 540,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+AXII+2+Cylindrical+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    }
]


def main():
    with open("data/parts.json") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            raise ValueError(f"Duplicate id: {part['id']}")

    data["parts"].extend(NEW_PARTS)

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added {len(NEW_PARTS)} parts. Total parts: {len(data['parts'])}")


if __name__ == "__main__":
    main()
