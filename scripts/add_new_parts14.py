#!/usr/bin/env python3
"""Add a fourteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "impulserc-apex",
        "category": "frame",
        "name": "Apex 5\" Frame",
        "brand": "ImpulseRC",
        "price_php": 4519,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://impulserc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=impulserc+apex"
        }
    },
    {
        "id": "armattan-rooster",
        "category": "frame",
        "name": "Rooster 5\" Frame",
        "brand": "Armattan",
        "price_php": 5239,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://armattanquads.com/",
        "color": "#0d0d0d",
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
        "id": "brotherhobby-rocket-v3-2306",
        "category": "motor",
        "name": "Rocket V3 2306",
        "brand": "BrotherHobby",
        "price_php": 1149,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://brotherhobby.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 43
        }
    },
    {
        "id": "iflight-xing-e-2207",
        "category": "motor",
        "name": "XING-E 2207",
        "brand": "iFlight",
        "price_php": 999,
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
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "hobbywing-xrotor-micro-60a-v4",
        "category": "esc",
        "name": "XRotor Micro 60A 4-in-1 V4",
        "brand": "Hobbywing",
        "price_php": 3199,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.hobbywing.com",
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
        "id": "tmotor-f45a-pro-iii",
        "category": "esc",
        "name": "F45A PRO III 4-in-1",
        "brand": "T-Motor",
        "price_php": 3799,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "flywoo-goku-f745-aio",
        "category": "fc",
        "name": "Goku F745 AIO",
        "brand": "Flywoo",
        "price_php": 3499,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://flywoo.net"
        }
    },
    {
        "id": "iflight-blitz-mini-f7-v2",
        "category": "fc",
        "name": "BLITZ Mini F7 V2",
        "brand": "iFlight",
        "price_php": 2899,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
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
            "diagram_url": "https://shop.iflight.com"
        }
    },
    {
        "id": "hqprop-5x4x3-v2",
        "category": "propeller",
        "name": "5X4X3 V2",
        "brand": "HQProp",
        "price_php": 229,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray",
                "orange"
            ]
        }
    },
    {
        "id": "dal-cyclone-t5046c-v2",
        "category": "propeller",
        "name": "Cyclone T5046C V2",
        "brand": "DAL",
        "price_php": 245,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray"
            ]
        }
    },
    {
        "id": "runcam-phoenix-2-vista",
        "category": "camera",
        "name": "Phoenix 2 Vista",
        "brand": "RunCam",
        "price_php": 4519,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 145,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "caddx-ratel-3-pro",
        "category": "camera",
        "name": "Ratel 3 Pro",
        "brand": "Caddx",
        "price_php": 1959,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-pro-v3",
        "category": "vtx",
        "name": "Avatar HD Pro Kit V3",
        "brand": "Walksnail",
        "price_php": 8959,
        "weight_g": 17,
        "in_stock": True,
        "buy_url": "https://www.caddxfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital HD",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "rush-tank-solo",
        "category": "vtx",
        "name": "Tank Solo",
        "brand": "Rush",
        "price_php": 1679,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-6s-1500",
        "category": "battery",
        "name": "Black Series 1500mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1679,
        "weight_g": 255,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-r-line-v5-4s-1300",
        "category": "battery",
        "name": "R-Line V5 1300mAh 4S 150C",
        "brand": "Tattu",
        "price_php": 1849,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tbs-crossfire-micro-rx-v3",
        "category": "receiver",
        "name": "Crossfire Micro RX V3",
        "brand": "TBS",
        "price_php": 2519,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "radiomaster-rp4",
        "category": "receiver",
        "name": "RP4 ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 839,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "flywoo-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "Flywoo",
        "price_php": 1119,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "betafpv-m10-mini-gps",
        "category": "gps",
        "name": "M10 Mini GPS",
        "brand": "BetaFPV",
        "price_php": 979,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "tbs-triumph-pro",
        "category": "antenna",
        "name": "Triumph Pro 5.8GHz",
        "brand": "TBS",
        "price_php": 1399,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
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
        "id": "getfpv-stubby-antenna",
        "category": "antenna",
        "name": "5.8GHz Stubby Antenna",
        "brand": "GetFPV",
        "price_php": 419,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "MMCX",
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
