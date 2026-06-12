#!/usr/bin/env python3
"""Add a fourteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "tbs-source-one-v5-frame",
        "category": "frame",
        "name": "Source One V5",
        "brand": "TBS",
        "price_php": 1899,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/prod:source_one_v5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+v5"
        }
    },
    {
        "id": "flywoo-explorer-lr4-v2-frame",
        "category": "frame",
        "name": "Explorer LR4 V2 Frame",
        "brand": "Flywoo",
        "price_php": 2399,
        "weight_g": 75,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "iflight-xinge-pro-2207-1800kv",
        "category": "motor",
        "name": "XING-E Pro 2207 1800KV",
        "brand": "iFlight",
        "price_php": 950,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 40
        }
    },
    {
        "id": "iflight-xing2-2807-1300kv",
        "category": "motor",
        "name": "XING2 2807 1300KV",
        "brand": "iFlight",
        "price_php": 1650,
        "weight_g": 56,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 5,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },
    {
        "id": "mamba-f45-mini-4in1-esc",
        "category": "esc",
        "name": "F45_Mini 45A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 2299,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#001a00",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "holybro-tekko32-f4-45a-v2-4in1",
        "category": "esc",
        "name": "Tekko32 F4 45A V2 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3199,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#001a00",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "diatone-mamba-mk4-f722-fc",
        "category": "fc",
        "name": "Mamba MK4 F722 FC",
        "brand": "Diatone",
        "price_php": 3099,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "tmotor-f7-pro-mini-fc",
        "category": "fc",
        "name": "F7 PRO Mini FC",
        "brand": "T-Motor",
        "price_php": 2799,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-dc-5x4-3x3-v1s",
        "category": "propeller",
        "name": "DC-5X4.3X3 V1S",
        "brand": "HQProp",
        "price_php": 230,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-hurricane-5128-5inch",
        "category": "propeller",
        "name": "Hurricane 5128",
        "brand": "Gemfan",
        "price_php": 195,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 2.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "gray"]
        }
    },
    {
        "id": "foxeer-razer-mini-camera",
        "category": "camera",
        "name": "Razer Mini",
        "brand": "Foxeer",
        "price_php": 1300,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-v2-camera",
        "category": "camera",
        "name": "Avatar HD V2 Camera",
        "brand": "Walksnail",
        "price_php": 2899,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 170,
            "format": "Digital",
            "video_system": "Walksnail Avatar",
            "resolution": "1080p60"
        }
    },
    {
        "id": "rush-tank-ultimate-pro-vtx",
        "category": "vtx",
        "name": "Tank Ultimate Pro VTX",
        "brand": "Rush",
        "price_php": 2699,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "walksnail-avatar-hd-v2-vtx",
        "category": "vtx",
        "name": "Avatar HD V2 VTX",
        "brand": "Walksnail",
        "price_php": 4199,
        "weight_g": 19,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital",
            "video_system": "Walksnail Avatar",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-1500mah-4s-100c",
        "category": "battery",
        "name": "Black Series 1500mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 950,
        "weight_g": 168,
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
        "id": "tattu-rline-4-1300mah-6s",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S",
        "brand": "Tattu",
        "price_php": 2399,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
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
        "id": "radiomaster-er4-2-4ghz-rx",
        "category": "receiver",
        "name": "ER4 2.4GHz ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 750,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "happymodel-elrs-pnp-900mhz-rx",
        "category": "receiver",
        "name": "ELRS PNP 900MHz Receiver",
        "brand": "Happymodel",
        "price_php": 900,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 915,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "beitian-bn880-gps",
        "category": "gps",
        "name": "BN-880 GPS+Compass",
        "brand": "Beitian",
        "price_php": 850,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-5883l-gps",
        "category": "gps",
        "name": "M10Q-5883L GPS+Compass",
        "brand": "Matek",
        "price_php": 1550,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-5883l",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "foxeer-lollipop-4-antenna",
        "category": "antenna",
        "name": "Lollipop 4 Antenna",
        "brand": "Foxeer",
        "price_php": 450,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "tbs-triumph-spw-antenna",
        "category": "antenna",
        "name": "Triumph SPW Antenna",
        "brand": "TBS",
        "price_php": 1699,
        "weight_g": 23,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 8,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
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
