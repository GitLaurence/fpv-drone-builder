#!/usr/bin/env python3
"""Add a nineteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-hex-4-nano-baby-quad-frame",
        "category": "frame",
        "name": "Hex 4 Nano Baby Quad Frame",
        "brand": "Flywoo",
        "price_php": 1100,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 100,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 1.5,
            "standoff_height_mm": 15,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+hex+4+nano"
        }
    },
    {
        "id": "armattan-rooster-x-5",
        "category": "frame",
        "name": "Rooster X 5\"",
        "brand": "Armattan",
        "price_php": 3850,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+x"
        }
    },
    {
        "id": "iflight-xing2-2807-1300kv",
        "category": "motor",
        "name": "XING2 2807 1300KV",
        "brand": "iFlight",
        "price_php": 1750,
        "weight_g": 49,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "brotherhobby-avenger-2807.5-1300kv",
        "category": "motor",
        "name": "Avenger 2807.5 1300KV",
        "brand": "BrotherHobby",
        "price_php": 1650,
        "weight_g": 47,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "speedybee-f60a-v3-4in1-esc",
        "category": "esc",
        "name": "F60A V3 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 4600,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "iflight-succex-e-f4-45a",
        "category": "esc",
        "name": "SucceX-E F4 45A",
        "brand": "iFlight",
        "price_php": 3100,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
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
        "id": "mamba-f405-mk4",
        "category": "fc",
        "name": "F405 MK4",
        "brand": "Mamba",
        "price_php": 2400,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/pages/mamba-f405-mk4-betaflight-flight-controller"
        }
    },
    {
        "id": "axisflying-f7-pro-v2-aio",
        "category": "fc",
        "name": "F7 Pro V2 AIO",
        "brand": "Axisflying",
        "price_php": 5400,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "hqprop-7x4x3-v1s",
        "category": "propeller",
        "name": "7X4X3 V1S",
        "brand": "HQProp",
        "price_php": 320,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-hurricane-5125-3",
        "category": "propeller",
        "name": "Hurricane 5125-3",
        "brand": "Gemfan",
        "price_php": 235,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "white", "purple"]
        }
    },
    {
        "id": "foxeer-micro-razer-2",
        "category": "camera",
        "name": "Micro Razer 2",
        "brand": "Foxeer",
        "price_php": 2400,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
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
        "id": "runcam-race-4",
        "category": "camera",
        "name": "Race 4",
        "brand": "RunCam",
        "price_php": 2200,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-v2-vtx",
        "category": "vtx",
        "name": "Avatar HD V2 VTX",
        "brand": "Walksnail",
        "price_php": 7200,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Walksnail Avatar",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "rush-tank-max-solo-vtx",
        "category": "vtx",
        "name": "Tank Max Solo VTX",
        "brand": "Rush",
        "price_php": 2200,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "ovonic-1400mah-6s-100c",
        "category": "battery",
        "name": "1400mAh 6S 100C",
        "brand": "Ovonic",
        "price_php": 2050,
        "weight_g": 225,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-r-line-4.0-1400mah-6s",
        "category": "battery",
        "name": "R-Line 4.0 1400mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2950,
        "weight_g": 250,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-pp-pro-elrs-rx",
        "category": "receiver",
        "name": "PP-Pro ELRS Receiver",
        "brand": "HappyModel",
        "price_php": 700,
        "weight_g": 0.9,
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
        "id": "betafpv-superd-rx",
        "category": "receiver",
        "name": "SuperD RX",
        "brand": "BetaFPV",
        "price_php": 850,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "iflight-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "iFlight",
        "price_php": 1300,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 23,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "speedybee-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1450,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 21,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "tbs-triumph-antenna",
        "category": "antenna",
        "name": "Triumph",
        "brand": "TBS",
        "price_php": 950,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
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
        "id": "foxeer-lollipop-5",
        "category": "antenna",
        "name": "Lollipop 5",
        "brand": "Foxeer",
        "price_php": 420,
        "weight_g": 3.2,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
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
