#!/usr/bin/env python3
"""Add a sixteenth batch of new FPV parts to parts.json (covering categories
that were skipped as duplicates in batch 15)"""
import json

NEW_PARTS = [
    {
        "id": "armattan-chameleon-ti5-frame",
        "category": "frame",
        "name": "Chameleon Ti5 Frame",
        "brand": "Armattan",
        "price_php": 6479,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://armattanquads.com/",
        "color": "#3a3a3a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "titanium / carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+chameleon"
        }
    },
    {
        "id": "speedybee-f405-v4-mini-aio",
        "category": "fc",
        "name": "F405 V4 Mini AIO",
        "brand": "SpeedyBee",
        "price_php": 2599,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com/f405-v4-mini-aio"
        }
    },
    {
        "id": "hqprop-voyager-5x4-3x3",
        "category": "propeller",
        "name": "Voyager 5x4.3x3",
        "brand": "HQProp",
        "price_php": 229,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey"
            ]
        }
    },
    {
        "id": "gemfan-hurricane-x5",
        "category": "propeller",
        "name": "Hurricane X5",
        "brand": "Gemfan",
        "price_php": 219,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.9,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "blue",
                "grey"
            ]
        }
    },
    {
        "id": "runcam-phoenix-oscar",
        "category": "camera",
        "name": "Phoenix Oscar",
        "brand": "RunCam",
        "price_php": 1899,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-split-4-nano",
        "category": "camera",
        "name": "Split 4 Nano",
        "brand": "RunCam",
        "price_php": 2999,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 145,
            "format": "Analog + 1080p DVR",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-reaper-mini-v2",
        "category": "vtx",
        "name": "Reaper Mini V2",
        "brand": "Foxeer",
        "price_php": 1899,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-rline-v5-1300mah-6s",
        "category": "battery",
        "name": "R-Line V5 1300mAh 6S",
        "brand": "Tattu",
        "price_php": 1899,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://genstattu.com",
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
        "id": "radiomaster-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "RadioMaster",
        "price_php": 1099,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "foxeer-m10-gps-mini",
        "category": "gps",
        "name": "M10 GPS Mini",
        "brand": "Foxeer",
        "price_php": 1099,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 27,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "immersionrc-spironet-v4",
        "category": "antenna",
        "name": "SpiroNet V4 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 1599,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "lumenier-axii-pro-rhcp",
        "category": "antenna",
        "name": "AXII Pro RHCP 5.8GHz",
        "brand": "Lumenier",
        "price_php": 1799,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
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
