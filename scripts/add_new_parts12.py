#!/usr/bin/env python3
"""Add a twelfth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "axisflying-reaper-f5-v3",
        "category": "frame",
        "name": "Reaper F5 V3 Frame",
        "brand": "AxisFlying",
        "price_php": 3499,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+reaper+f5"
        }
    },
    {
        "id": "geprc-mark5-hd-v2-6inch",
        "category": "frame",
        "name": "Mark5 HD V2 6\" Frame",
        "brand": "GEPRC",
        "price_php": 3899,
        "weight_g": 135,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 247,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5+hd"
        }
    },
    {
        "id": "brotherhobby-returner-r5-2306-5-1500kv",
        "category": "motor",
        "name": "Returner R5 2306.5 1500KV",
        "brand": "BrotherHobby",
        "price_php": 1199,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1500,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 38
        }
    },
    {
        "id": "iflight-xinge-pro-2207-1500kv",
        "category": "motor",
        "name": "XING-E Pro 2207 1500KV",
        "brand": "iFlight",
        "price_php": 1049,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1500,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 40
        }
    },
    {
        "id": "aikon-ak32f-50a-4in1",
        "category": "esc",
        "name": "AK32F 50A 4-in-1 ESC",
        "brand": "Aikon",
        "price_php": 2799,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#001a00",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "hobbywing-xrotor-micro-70a-4in1",
        "category": "esc",
        "name": "XRotor Micro 70A 4-in-1",
        "brand": "Hobbywing",
        "price_php": 3299,
        "weight_g": 35,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 70,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 80
        }
    },
    {
        "id": "jhemcu-ghf722aio",
        "category": "fc",
        "name": "GHF722AIO FC+ESC",
        "brand": "JHEMCU",
        "price_php": 2899,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://jhemcu.com"
        }
    },
    {
        "id": "speedybee-f745-aio-v2",
        "category": "fc",
        "name": "F745 AIO V2",
        "brand": "SpeedyBee",
        "price_php": 4199,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 4,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com"
        }
    },
    {
        "id": "tmotor-t5147s-v2-3blade",
        "category": "propeller",
        "name": "T5147S V2 3-Blade",
        "brand": "T-Motor",
        "price_php": 249,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "azurepower-pegasus-5x4-8x3",
        "category": "propeller",
        "name": "Pegasus 5×4.8×3",
        "brand": "Azure Power",
        "price_php": 239,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "grey"]
        }
    },
    {
        "id": "foxeer-toothless-3-pro",
        "category": "camera",
        "name": "Toothless 3 Pro",
        "brand": "Foxeer",
        "price_php": 1899,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
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
        "id": "caddx-ant-lite-v2",
        "category": "camera",
        "name": "Ant Lite V2",
        "brand": "Caddx",
        "price_php": 1299,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "3.3-5.5V"
        }
    },
    {
        "id": "akk-fx2-ultimate-v2",
        "category": "vtx",
        "name": "FX2 Ultimate V2",
        "brand": "AKK",
        "price_php": 1599,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-parrotvtx-1-6w",
        "category": "vtx",
        "name": "ParrotVTX 1.6W",
        "brand": "iFlight",
        "price_php": 2199,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
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
        "id": "cnhl-ministar-pro-1300mah-6s-120c",
        "category": "battery",
        "name": "MiniStar Pro 1300mAh 6S 120C",
        "brand": "CNHL",
        "price_php": 1799,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-rline5-1400mah-6s-150c",
        "category": "battery",
        "name": "R-Line 5.0 1400mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2099,
        "weight_g": 225,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-epw2-elrs-rx",
        "category": "receiver",
        "name": "EPW2 ELRS RX",
        "brand": "Happymodel",
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
        "id": "flywoo-elrs-nano-rx-v3",
        "category": "receiver",
        "name": "ELRS Nano RX V3",
        "brand": "Flywoo",
        "price_php": 949,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 28
        }
    },
    {
        "id": "matek-m8q-5883-v2",
        "category": "gps",
        "name": "M8Q-5883 V2 GPS+Compass",
        "brand": "Matek",
        "price_php": 1450,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m8q-5883",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "beitian-be-180-gps-module",
        "category": "gps",
        "name": "BE-180 GPS Module",
        "brand": "Beitian",
        "price_php": 990,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "foxeer-pagoda-3-pro",
        "category": "antenna",
        "name": "Pagoda 3 Pro",
        "brand": "Foxeer",
        "price_php": 690,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
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
        "id": "truerc-singularity-v4-5-8ghz",
        "category": "antenna",
        "name": "Singularity V4 5.8GHz",
        "brand": "TrueRC",
        "price_php": 1299,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
