#!/usr/bin/env python3
"""Add a fifteenth batch of new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "tbs-source-one-v5-7inch",
        "category": "frame",
        "name": "Source One V5 7\" Frame",
        "brand": "TBS",
        "price_php": 3919,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 300,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+v5+7"
        }
    },
    {
        "id": "flywoo-explorer-lr4-v2-frame",
        "category": "frame",
        "name": "Explorer LR4 V2 Frame",
        "brand": "Flywoo",
        "price_php": 3399,
        "weight_g": 86,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2a2a2a",
        "specs": {
            "size_mm": 188,
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
        "id": "tmotor-f90-2507",
        "category": "motor",
        "name": "F90 2507",
        "brand": "T-Motor",
        "price_php": 1849,
        "weight_g": 44,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2507",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "brotherhobby-avenger-2812",
        "category": "motor",
        "name": "Avenger 2812",
        "brand": "BrotherHobby",
        "price_php": 1599,
        "weight_g": 58,
        "in_stock": True,
        "buy_url": "https://brotherhobby.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1100,
            "stator_size": "2812",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },
    {
        "id": "diatone-mamba-f40-40a-4in1",
        "category": "esc",
        "name": "Mamba F40 40A 4-in-1",
        "brand": "Diatone",
        "price_php": 2199,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002200",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 50
        }
    },
    {
        "id": "holybro-tekko32-f4-50a-4in1-v2",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 V2",
        "brand": "Holybro",
        "price_php": 3299,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "holybro-kakute-f4-v3",
        "category": "fc",
        "name": "Kakute F4 V3",
        "brand": "Holybro",
        "price_php": 2199,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://holybro.com/products/kakute-f4-v3"
        }
    },
    {
        "id": "matek-f411-wse",
        "category": "fc",
        "name": "F411-WSE",
        "brand": "Matek",
        "price_php": 1799,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": False,
            "uart_count": 3,
            "5v_pad_count": 1,
            "curr_sensor": True,
            "diagram_url": "https://www.mateksys.com/?portfolio=f411-wse"
        }
    },
    {
        "id": "gemfan-flash-5055",
        "category": "propeller",
        "name": "Flash 5055",
        "brand": "Gemfan",
        "price_php": 209,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 5.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "white",
                "grey"
            ]
        }
    },
    {
        "id": "dal-cyclone-t5051c",
        "category": "propeller",
        "name": "Cyclone T5051C",
        "brand": "DAL",
        "price_php": 239,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 5.1,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey",
                "orange"
            ]
        }
    },
    {
        "id": "foxeer-falkor-3-camera",
        "category": "camera",
        "name": "Falkor 3",
        "brand": "Foxeer",
        "price_php": 1499,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ant-lite-fpv",
        "category": "camera",
        "name": "Ant Lite",
        "brand": "Caddx",
        "price_php": 899,
        "weight_g": 3.3,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "tbs-unify-evo-hv",
        "category": "vtx",
        "name": "Unify Evo HV",
        "brand": "TBS",
        "price_php": 3199,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "7-36V",
            "connector": "MMCX"
        }
    },
    {
        "id": "foxeer-reaper-v2-vtx",
        "category": "vtx",
        "name": "Reaper V2",
        "brand": "Foxeer",
        "price_php": 2399,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-ministar-1700mah-6s",
        "category": "battery",
        "name": "MiniStar 1700mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1759,
        "weight_g": 234,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1700,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gnb-4s-1300mah-100c",
        "category": "battery",
        "name": "4S 1300mAh 100C",
        "brand": "Gens Ace",
        "price_php": 999,
        "weight_g": 142,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
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
        "id": "radiomaster-rp3-pro-elrs",
        "category": "receiver",
        "name": "RP3 Pro ELRS",
        "brand": "RadioMaster",
        "price_php": 1299,
        "weight_g": 2.1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 35
        }
    },
    {
        "id": "happymodel-ep2-elrs-pro-rx",
        "category": "receiver",
        "name": "EP2 ELRS Pro",
        "brand": "HappyModel",
        "price_php": 899,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "holybro-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "Holybro",
        "price_php": 1299,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com",
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
        "id": "speedybee-m10-gps-pro",
        "category": "gps",
        "name": "M10 GPS Pro",
        "brand": "SpeedyBee",
        "price_php": 1199,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "truerc-singularity-5-8ghz",
        "category": "antenna",
        "name": "Singularity 5.8GHz",
        "brand": "TrueRC",
        "price_php": 1499,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "rushfpv-cherry-v2-5-8",
        "category": "antenna",
        "name": "Cherry V2 5.8GHz",
        "brand": "RushFPV",
        "price_php": 699,
        "weight_g": 5,
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
