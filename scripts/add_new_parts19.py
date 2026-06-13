#!/usr/bin/env python3
"""Add a nineteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-hex-nano-frame",
        "category": "frame",
        "name": "Hex Nano Frame",
        "brand": "Flywoo",
        "price_php": 850,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 100,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 18,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+hex+nano"
        }
    },
    {
        "id": "armattan-rooster-frame",
        "category": "frame",
        "name": "Rooster 5\"",
        "brand": "Armattan",
        "price_php": 3100,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://armattanproductions.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster"
        }
    },
    {
        "id": "tmotor-f60-pro-iv-2207-1750kv",
        "category": "motor",
        "name": "F60 PRO IV 2207 1750KV",
        "brand": "T-Motor",
        "price_php": 1580,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "iflight-xing2-2807-1300kv",
        "category": "motor",
        "name": "XING2 2807 1300KV",
        "brand": "iFlight",
        "price_php": 1350,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "flycolor-pro-x-60a",
        "category": "esc",
        "name": "Pro X 60A 4-in-1",
        "brand": "Flycolor",
        "price_php": 2520,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "hglrc-zeus-60a-esc",
        "category": "esc",
        "name": "Zeus 60A 4-in-1",
        "brand": "HGLRC",
        "price_php": 2690,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "foxeer-f722-v4",
        "category": "fc",
        "name": "F722 V4",
        "brand": "Foxeer",
        "price_php": 2240,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "matek-f405-tex",
        "category": "fc",
        "name": "F405-TEX",
        "brand": "Matek",
        "price_php": 3080,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.mateksys.com/?portfolio=f405-tex"
        }
    },
    {
        "id": "hqprop-t5x4x3-durable",
        "category": "propeller",
        "name": "T5X4X3 Durable",
        "brand": "HQProp",
        "price_php": 175,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "white"]
        }
    },
    {
        "id": "gemfan-windancer-51466-durable",
        "category": "propeller",
        "name": "Windancer 5146 Durable",
        "brand": "Gemfan",
        "price_php": 220,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 6,
            "shaft_mm": 5,
            "color_options": ["gray", "green"]
        }
    },
    {
        "id": "walksnail-avatar-hd-pro-cam",
        "category": "camera",
        "name": "Avatar HD Pro Camera",
        "brand": "Walksnail",
        "price_php": 3900,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 165,
            "format": "Digital",
            "tvl": 1300,
            "voltage_range": "6-25V"
        }
    },
    {
        "id": "foxeer-cat-3-v2",
        "category": "camera",
        "name": "Cat 3 V2",
        "brand": "Foxeer",
        "price_php": 1680,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "iflight-onair-pro-vtx",
        "category": "vtx",
        "name": "OnAir Pro VTX",
        "brand": "iFlight",
        "price_php": 2520,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-tx200-vtx",
        "category": "vtx",
        "name": "TX200 VTX",
        "brand": "HGLRC",
        "price_php": 1680,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-1500mah-4s",
        "category": "battery",
        "name": "Black Series 1500mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1230,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-850mah-3s",
        "category": "battery",
        "name": "850mAh 3S 75C",
        "brand": "Tattu",
        "price_php": 840,
        "weight_g": 75,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 850,
            "c_rating": 75,
            "connector": "XT30",
            "voltage_nominal": 11.1
        }
    },
    {
        "id": "happymodel-eleres-pro-rx",
        "category": "receiver",
        "name": "ELERES Pro Receiver",
        "brand": "HappyModel",
        "price_php": 1400,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELERES",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "frsky-r9-mm-rx",
        "category": "receiver",
        "name": "R9 MM Receiver",
        "brand": "FrSky",
        "price_php": 1960,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "beitian-bn-280t-gps",
        "category": "gps",
        "name": "BN-280T GPS+Compass",
        "brand": "Beitian",
        "price_php": 1010,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8030",
            "update_rate_hz": 10,
            "fix_time_s": 27,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10-5883-uart2",
        "category": "gps",
        "name": "M10-5883 UART2 GPS+Compass",
        "brand": "Matek",
        "price_php": 1230,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
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
    {
        "id": "truerc-x-air",
        "category": "antenna",
        "name": "X-Air Omni 5.8GHz",
        "brand": "TrueRC",
        "price_php": 840,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "rushfpv-cherry-omni",
        "category": "antenna",
        "name": "Cherry Omni 5.8GHz",
        "brand": "RushFPV",
        "price_php": 450,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
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
