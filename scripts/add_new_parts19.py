#!/usr/bin/env python3
"""Add a nineteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "armattan-rooster-5-frame",
        "category": "frame",
        "name": "Rooster 5\"",
        "brand": "Armattan",
        "price_php": 7500,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://armattanproductions.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+5"
        }
    },
    {
        "id": "flywoo-explorer-lr4-mini-frame",
        "category": "frame",
        "name": "Explorer LR4 Mini",
        "brand": "Flywoo",
        "price_php": 2400,
        "weight_g": 75,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "tmotor-velox-v2806-1300kv",
        "category": "motor",
        "name": "Velox V2806 1300KV",
        "brand": "T-Motor",
        "price_php": 2400,
        "weight_g": 56,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2806",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 30
        }
    },
    {
        "id": "rcinpower-gts-v3-2407",
        "category": "motor",
        "name": "GTS V3 2407",
        "brand": "RCINPOWER",
        "price_php": 1750,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.rcinpower.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1850,
            "stator_size": "2407",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "hglrc-sector30-30a-esc",
        "category": "esc",
        "name": "Sector30 30A 4-in-1",
        "brand": "HGLRC",
        "price_php": 1400,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 30,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 35
        }
    },
    {
        "id": "iflight-blitz-e55-esc",
        "category": "esc",
        "name": "BLITZ E55 55A 4-in-1",
        "brand": "iFlight",
        "price_php": 3200,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 65
        }
    },
    {
        "id": "holybro-kakute-f7-hdv-fc",
        "category": "fc",
        "name": "Kakute F7 HDV",
        "brand": "Holybro",
        "price_php": 4500,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM20689",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://holybro.com/products/kakute-f7-hdv"
        }
    },
    {
        "id": "hglrc-zeus-f760-fc",
        "category": "fc",
        "name": "Zeus F760 AIO",
        "brand": "HGLRC",
        "price_php": 3800,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://www.hglrc.com"
        }
    },
    {
        "id": "hqprop-7x4x3-tri",
        "category": "propeller",
        "name": "7X4X3 Tri-Blade",
        "brand": "HQProp",
        "price_php": 300,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "gemfan-5152s-prop",
        "category": "propeller",
        "name": "Hurricane 5152S",
        "brand": "Gemfan",
        "price_php": 180,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "green"]
        }
    },
    {
        "id": "walksnail-avatar-hd-nano-camera",
        "category": "camera",
        "name": "Avatar HD Nano Camera",
        "brand": "Walksnail",
        "price_php": 3200,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#222",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "resolution": "1080p60",
            "voltage_range": "6-25V",
            "video_system": "Walksnail Avatar HD"
        }
    },
    {
        "id": "foxeer-cat-3-cam",
        "category": "camera",
        "name": "Cat 3",
        "brand": "Foxeer",
        "price_php": 2200,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS Starlight",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "rush-cherry2-vtx",
        "category": "vtx",
        "name": "Cherry2",
        "brand": "Rush",
        "price_php": 2800,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-24V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tbs-unify-evo-vtx",
        "category": "vtx",
        "name": "Unify Evo",
        "brand": "TBS",
        "price_php": 3500,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "Race/A/B/E/F",
            "voltage_range": "6-23V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-4s-1300-battery",
        "category": "battery",
        "name": "1300mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 950,
        "weight_g": 158,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "rdq-series-6s-1300-battery",
        "category": "battery",
        "name": "RDQ Series 6S 1300mAh 100C",
        "brand": "RDQ",
        "price_php": 1500,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-ep1-receiver",
        "category": "receiver",
        "name": "EP1 ELRS",
        "brand": "Happymodel",
        "price_php": 650,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "frsky-r-xsr-receiver",
        "category": "receiver",
        "name": "R-XSR",
        "brand": "FrSky",
        "price_php": 900,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "FrSky D16",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "matek-m9n-v2-gps",
        "category": "gps",
        "name": "M9N-V2 GPS",
        "brand": "Matek",
        "price_php": 1700,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m9n-v2",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "jhemcu-m10-gps",
        "category": "gps",
        "name": "M10 GPS",
        "brand": "JHEMCU",
        "price_php": 1100,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.jhemcu.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BDS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "aomway-5.8g-leaf-antenna",
        "category": "antenna",
        "name": "5.8GHz Leaf Antenna",
        "brand": "Aomway",
        "price_php": 450,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.aomway.com",
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
        "id": "tbs-triumph-antenna",
        "category": "antenna",
        "name": "Triumph",
        "brand": "TBS",
        "price_php": 1100,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
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
    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            raise ValueError(f"Duplicate id: {part['id']}")
        data["parts"].append(part)
        added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added {added} new parts. Total parts: {len(data['parts'])}")


if __name__ == "__main__":
    main()
