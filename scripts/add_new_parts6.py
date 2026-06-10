#!/usr/bin/env python3
"""Add a sixth batch of 6 new FPV parts to round out categories missed in batch 5"""
import json

NEW_PARTS = [
    {
        "id": "xilo-stax-5",
        "category": "frame",
        "name": "Stax 5\" Frame",
        "brand": "Xilo",
        "price_php": 4640,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "diatone-mamba-f405-mk2",
        "category": "fc",
        "name": "Mamba F405 MK2 Flight Controller",
        "brand": "Diatone",
        "price_php": 2552,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-t5x-5x4.8x3",
        "category": "propeller",
        "name": "T5X 5×4.8×3",
        "brand": "HQProp",
        "price_php": 232,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "orange"]
        }
    },
    {
        "id": "runcam-racer-4",
        "category": "camera",
        "name": "Racer 4",
        "brand": "RunCam",
        "price_php": 1276,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "frsky-r9-mm",
        "category": "receiver",
        "name": "R9 MM Receiver",
        "brand": "FrSky",
        "price_php": 1334,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "matek-m10q-5883",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1624,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-5883",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 24,
            "compass": True,
            "connector": "JST-SH 4-pin"
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
