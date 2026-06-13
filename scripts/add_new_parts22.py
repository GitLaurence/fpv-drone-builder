#!/usr/bin/env python3
"""Add a new batch of real-world FPV parts (2 per category) to data/parts.json."""
import json

NEW_PARTS = [
    {
        "id": "flywoo-explorer-lr4-v2",
        "category": "frame",
        "name": "Explorer LR4 V2 4\" Long Range Frame",
        "brand": "Flywoo",
        "price_php": 2100,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2b2b2b",
        "specs": {
            "size_mm": 178,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "geprc-mark5-hd-o4",
        "category": "frame",
        "name": "Mark5 HD O4 5\" Freestyle Frame",
        "brand": "GEPRC",
        "price_php": 3360,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5+hd"
        }
    },
    {
        "id": "iflight-xing2-2207-2450kv",
        "category": "motor",
        "name": "XING2 2207 2450KV",
        "brand": "iFlight",
        "price_php": 1064,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "brotherhobby-avenger-mini-1404.5-3800kv",
        "category": "motor",
        "name": "Avenger Mini 1404.5 3800KV",
        "brand": "BrotherHobby",
        "price_php": 750,
        "weight_g": 11.3,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#333333",
        "specs": {
            "kv": 3800,
            "stator_size": "1404.5",
            "motor_mount_mm": 9,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 16
        }
    },
    {
        "id": "speedybee-60a-4in1-blheli32",
        "category": "esc",
        "name": "60A 4-in-1 BLHeli32 ESC",
        "brand": "SpeedyBee",
        "price_php": 2659,
        "weight_g": 20,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#0a0a0a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "jhemcu-25a-4in1-blheli_s",
        "category": "esc",
        "name": "25A 4-in-1 ESC BLHeli_S",
        "brand": "JHEMCU",
        "price_php": 1450,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://jhemcu.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 25,
            "input_voltage_s": 4,
            "protocol": "DSHOT300",
            "form_factor_mm": 20,
            "burst_amp": 30
        }
    },
    {
        "id": "foxeer-f405-v2",
        "category": "fc",
        "name": "F405 V2 Flight Controller",
        "brand": "Foxeer",
        "price_php": 1850,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#0d0d0d",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.foxeer.com"
        }
    },
    {
        "id": "holybro-kakute-f4-aio-v3",
        "category": "fc",
        "name": "Kakute F4 AIO V3 Flight Controller",
        "brand": "Holybro",
        "price_php": 2575,
        "weight_g": 9.4,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://holybro.com"
        }
    },
    {
        "id": "hqprop-7x4x2",
        "category": "propeller",
        "name": "7X4X2 Bi-Blade Propeller",
        "brand": "HQProp",
        "price_php": 280,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#888888",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-hurricane-2015-3",
        "category": "propeller",
        "name": "Hurricane 2015-3 2\" Tri-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 145,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#888888",
        "specs": {
            "diameter_inch": 2,
            "pitch": 1.5,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["gray", "green"]
        }
    },
    {
        "id": "foxeer-toothless-3",
        "category": "camera",
        "name": "Toothless 3 Analog FPV Camera",
        "brand": "Foxeer",
        "price_php": 1064,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-phoenix-3-mini",
        "category": "camera",
        "name": "Phoenix 3 Mini Analog FPV Camera",
        "brand": "RunCam",
        "price_php": 1320,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "rush-tank-ultimate-pro",
        "category": "vtx",
        "name": "Tank Ultimate Pro 5.8GHz VTX",
        "brand": "Rush",
        "price_php": 3360,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://rushfpv.net",
        "color": "#1a0000",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "akk-fx3-ultimate-vtx",
        "category": "vtx",
        "name": "FX3 Ultimate 5.8GHz VTX",
        "brand": "AKK",
        "price_php": 1230,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.akktek.com",
        "color": "#0a0a0a",
        "specs": {
            "power_mw_max": 3000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },
    {
        "id": "tattu-rline5-1100mah-6s",
        "category": "battery",
        "name": "R-Line 5.0 1100mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 3640,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-ministar-1300mah-4s",
        "category": "battery",
        "name": "MiniStar 1300mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1450,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.chinahobbyline.com",
        "color": "#222222",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "radiomaster-rp4-nano",
        "category": "receiver",
        "name": "RP4 Nano ELRS 2.4GHz Receiver",
        "brand": "RadioMaster",
        "price_php": 952,
        "weight_g": 1.2,
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
        "id": "immersionrc-ghost-lite-rx",
        "category": "receiver",
        "name": "Ghost Lite Receiver",
        "brand": "ImmersionRC",
        "price_php": 1064,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "Ghost",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "betafpv-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "BetaFPV",
        "price_php": 980,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 29,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "iflight-m8q-5883-gps",
        "category": "gps",
        "name": "M8Q-5883 GPS/Compass Module",
        "brand": "iFlight",
        "price_php": 896,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "foxeer-albatross-2-pro",
        "category": "antenna",
        "name": "Albatross 2 Pro 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 728,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    },
    {
        "id": "lumenier-axii2-pro",
        "category": "antenna",
        "name": "AXII 2 Pro 5.8GHz Antenna",
        "brand": "Lumenier",
        "price_php": 952,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
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
