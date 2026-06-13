#!/usr/bin/env python3
"""Add a nineteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-mark5-hd7-pro",
        "category": "frame",
        "name": "Mark5 HD7 Pro 7\" Freestyle",
        "brand": "GEPRC",
        "price_php": 5500,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 300,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5+hd7"
        }
    },
    {
        "id": "flywoo-explorer-lr6-6in",
        "category": "frame",
        "name": "Explorer LR6 6\" Long Range",
        "brand": "Flywoo",
        "price_php": 3400,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://www.flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 254,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr6"
        }
    },
    {
        "id": "brotherhobby-avenger-2807-1300kv",
        "category": "motor",
        "name": "Avenger 2807 1300KV",
        "brand": "BrotherHobby",
        "price_php": 1900,
        "weight_g": 58,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "tmotor-f90-pro-iii-1500kv",
        "category": "motor",
        "name": "F90 Pro III 2806.5 1500KV",
        "brand": "T-Motor",
        "price_php": 2100,
        "weight_g": 52,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1500,
            "stator_size": "2806.5",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "iflight-blitz-e80-80a-4in1",
        "category": "esc",
        "name": "BLITZ E80 80A 4-in-1",
        "brand": "iFlight",
        "price_php": 4800,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 80,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 100
        }
    },
    {
        "id": "hglrc-zeus-f745-80a-aio",
        "category": "esc",
        "name": "Zeus F745 80A AIO",
        "brand": "HGLRC",
        "price_php": 5800,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 80,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 100
        }
    },
    {
        "id": "iflight-blitz-mini-f7-pro-aio",
        "category": "fc",
        "name": "BLITZ Mini F7 Pro AIO",
        "brand": "iFlight",
        "price_php": 3200,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
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
        "id": "holybro-kakute-h7-v2-30x30",
        "category": "fc",
        "name": "Kakute H7 V2 30x30",
        "brand": "Holybro",
        "price_php": 5400,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
            "curr_sensor": True,
            "diagram_url": "https://docs.holybro.com/flight-controller/kakute-h7-v2"
        }
    },
    {
        "id": "gemfan-7050-3blade-lr",
        "category": "propeller",
        "name": "7050 3-Blade Long Range",
        "brand": "Gemfan",
        "price_php": 280,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 5.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "black"]
        }
    },
    {
        "id": "hqprop-6x4x3-v1s",
        "category": "propeller",
        "name": "6X4X3 V1S",
        "brand": "HQProp",
        "price_php": 230,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "foxeer-falkor3-pro-micro-starlight",
        "category": "camera",
        "name": "Falkor 3 Pro Micro Starlight",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS Starlight",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-25V"
        }
    },
    {
        "id": "runcam-night-eagle-3-mini-pro",
        "category": "camera",
        "name": "Night Eagle 3 Mini Pro",
        "brand": "RunCam",
        "price_php": 1950,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.2\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "rush-tank-max-2w",
        "category": "vtx",
        "name": "Tank Max 2W VTX",
        "brand": "RushFPV",
        "price_php": 3800,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "akk-x2-ultimate-5.8",
        "category": "vtx",
        "name": "X2 Ultimate 5.8GHz VTX",
        "brand": "AKK",
        "price_php": 2600,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-30V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-rline-4500mah-6s-100c",
        "category": "battery",
        "name": "R-Line 4500mAh 6S 100C",
        "brand": "Tattu",
        "price_php": 6800,
        "weight_g": 620,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 4500,
            "c_rating": 100,
            "connector": "XT90",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-ministar-2200mah-4s-100c",
        "category": "battery",
        "name": "MiniStar 2200mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1650,
        "weight_g": 230,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 2200,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tbs-crossfire-diversity-rx",
        "category": "receiver",
        "name": "Crossfire Diversity RX",
        "brand": "TBS",
        "price_php": 2800,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 868,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "radiomaster-rp3-elrs-nano-rx",
        "category": "receiver",
        "name": "RP3 ELRS Nano RX",
        "brand": "RadioMaster",
        "price_php": 850,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "holybro-m9n-mini-gps",
        "category": "gps",
        "name": "M9N Mini GPS",
        "brand": "Holybro",
        "price_php": 1450,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "foxeer-m9n-gps-compass",
        "category": "gps",
        "name": "M9N GPS+Compass",
        "brand": "Foxeer",
        "price_php": 1550,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "lumenier-axii2-rhcp-long",
        "category": "antenna",
        "name": "AXII 2 RHCP Long Range",
        "brand": "Lumenier",
        "price_php": 750,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "tbs-triumph-pro-nano-5.8",
        "category": "antenna",
        "name": "Triumph Pro Nano 5.8GHz",
        "brand": "TBS",
        "price_php": 550,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "U.FL",
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
