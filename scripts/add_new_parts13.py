#!/usr/bin/env python3
"""Add a thirteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-hex-mini-baby-quad",
        "category": "frame",
        "name": "Hex Mini Baby Quad Frame",
        "brand": "Flywoo",
        "price_php": 1399,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 130,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 18,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+hex+mini"
        }
    },
    {
        "id": "shendrones-frostbite-5",
        "category": "frame",
        "name": "Frostbite 5\" Frame",
        "brand": "ShenDrones",
        "price_php": 5599,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://shendrones.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=shendrones+frostbite"
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-1800kv",
        "category": "motor",
        "name": "Avenger 2306.5 1800KV",
        "brand": "BrotherHobby",
        "price_php": 1349,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 42
        }
    },
    {
        "id": "xnova-freestyle-2408-1700kv",
        "category": "motor",
        "name": "Freestyle 2408 1700KV",
        "brand": "Xnova",
        "price_php": 1799,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2408",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "speedybee-f55a-60a-4in1",
        "category": "esc",
        "name": "F55A 60A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 3599,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
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
        "id": "flywoo-goku-gn745-50a-aio",
        "category": "esc",
        "name": "GOKU GN745 50A AIO ESC",
        "brand": "Flywoo",
        "price_php": 3799,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 25.5,
            "burst_amp": 60
        }
    },
    {
        "id": "mamba-mk4-f722-mini",
        "category": "fc",
        "name": "MK4 F722 Mini",
        "brand": "Mamba",
        "price_php": 3199,
        "weight_g": 9,
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
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.getfpv.com"
        }
    },
    {
        "id": "foxeer-f722-v4-aio",
        "category": "fc",
        "name": "F722 V4 AIO",
        "brand": "Foxeer",
        "price_php": 3499,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
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
            "diagram_url": "https://www.foxeer.com"
        }
    },
    {
        "id": "gemfan-hurricane-5042-3blade",
        "category": "propeller",
        "name": "Hurricane 5042 3-Blade",
        "brand": "Gemfan",
        "price_php": 219,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "green"]
        }
    },
    {
        "id": "hqprop-ethix-s5-v2",
        "category": "propeller",
        "name": "Ethix S5 V2",
        "brand": "HQProp",
        "price_php": 269,
        "weight_g": 5.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "purple"]
        }
    },
    {
        "id": "foxeer-nano-mix-2",
        "category": "camera",
        "name": "Nano Mix 2",
        "brand": "Foxeer",
        "price_php": 1399,
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
        "id": "runcam-phoenix-2-vision",
        "category": "camera",
        "name": "Phoenix 2 Vision",
        "brand": "RunCam",
        "price_php": 1899,
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
        "id": "rushfpv-tank-nano-vtx",
        "category": "vtx",
        "name": "Tank Nano VTX",
        "brand": "Rush",
        "price_php": 1799,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://rushfpv.net",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "eachine-tx805s-vtx",
        "category": "vtx",
        "name": "TX805S VTX",
        "brand": "Eachine",
        "price_php": 1099,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },
    {
        "id": "cnhl-ministar-4s-1800mah-100c",
        "category": "battery",
        "name": "MiniStar 1800mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1299,
        "weight_g": 198,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1800,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-rlinev5-1300mah-4s-150c",
        "category": "battery",
        "name": "R-Line V5.0 1300mAh 4S 150C",
        "brand": "Tattu",
        "price_php": 1899,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
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
        "id": "tbs-crossfire-nano-se-rx",
        "category": "receiver",
        "name": "Crossfire Nano SE RX",
        "brand": "TBS",
        "price_php": 1959,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "CRSF",
            "frequency_mhz": 868,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "betafpv-elrs-2-4g-super-mini-rx",
        "category": "receiver",
        "name": "ELRS 2.4G Super Mini RX",
        "brand": "BetaFPV",
        "price_php": 849,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "matek-m10-5883",
        "category": "gps",
        "name": "M10-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1550,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10-5883",
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
        "id": "holybro-st-h160-m10-gps",
        "category": "gps",
        "name": "ST-H160 M10 GPS",
        "brand": "Holybro",
        "price_php": 1690,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 22,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "rushfpv-cherry-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz Antenna",
        "brand": "Rush",
        "price_php": 599,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://rushfpv.net",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "immersionrc-spironet-5-8ghz-v2",
        "category": "antenna",
        "name": "SpiroNet 5.8GHz V2",
        "brand": "ImmersionRC",
        "price_php": 1099,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
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
