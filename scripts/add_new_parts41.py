#!/usr/bin/env python3
"""Add 41st batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "impulserc-apex-5-frame",
        "category": "frame",
        "name": "Apex 5\" Frame",
        "brand": "ImpulseRC",
        "price_php": 4200,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImpulseRC+Apex+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=impulserc+apex+5"
        }
    },
    {
        "id": "tmotor-f40-pro-iv-2400kv",
        "category": "motor",
        "name": "F40 Pro IV 2400KV",
        "brand": "T-Motor",
        "price_php": 980,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F40+Pro+IV+2400KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2400,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 35
        }
    },
    {
        "id": "tmotor-f55a-pro-ii-4in1-esc",
        "category": "esc",
        "name": "F55A PRO II 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 2980,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F55A+PRO+II+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "iflight-succex-e-f4-fc",
        "category": "fc",
        "name": "SucceX-E F4 Flight Controller",
        "brand": "iFlight",
        "price_php": 1450,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+SucceX-E+F4+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-5x4x3-v1s-propeller",
        "category": "propeller",
        "name": "5X4X3 V1S Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 220,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+5X4X3+V1S",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "black",
                "white"
            ]
        }
    },
    {
        "id": "caddx-ant-lite-camera",
        "category": "camera",
        "name": "Ant Lite FPV Camera",
        "brand": "Caddx",
        "price_php": 1180,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ant+Lite",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-25V"
        }
    },
    {
        "id": "tbs-unify-pro32-hv-vtx",
        "category": "vtx",
        "name": "Unify Pro32 HV VTX",
        "brand": "TBS",
        "price_php": 3450,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro32+HV",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "7-36V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-r-line-v4-1300mah-4s",
        "category": "battery",
        "name": "R-Line Version 4.0 1300mAh 4S 120C LiPo",
        "brand": "Tattu",
        "price_php": 1480,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+Version+4.0+1300mAh+4S",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tbs-crossfire-nano-rx-diversity",
        "category": "receiver",
        "name": "Crossfire Nano RX Diversity",
        "brand": "TBS",
        "price_php": 1750,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+RX+Diversity",
        "color": "#1a001a",
        "specs": {
            "protocol": "CRSF",
            "frequency_mhz": 868,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "bn-880-gps-module",
        "category": "gps",
        "name": "BN-880 GPS Module",
        "brand": "Beitian",
        "price_php": 980,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "interface": "UART",
            "compass": True,
            "weight_g": 12,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "lumenier-axii-2-stubby-antenna",
        "category": "antenna",
        "name": "AXII 2 Stubby 5.8GHz Antenna",
        "brand": "Lumenier",
        "price_php": 750,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+AXII+2+Stubby+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omnidirectional"
        }
    },
]


def main():
    with open("data/parts.json") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    added = 0
    skipped = 0

    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"SKIP (exists): {part['id']}")
            skipped += 1
        else:
            data["parts"].append(part)
            existing_ids.add(part["id"])
            added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone: added {added} parts, skipped {skipped} duplicates")
    print(f"Total parts now: {len(data['parts'])}")


if __name__ == "__main__":
    main()
