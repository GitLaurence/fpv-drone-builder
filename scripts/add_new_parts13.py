#!/usr/bin/env python3
"""Add a thirteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "armattan-marmotte-5inch",
        "category": "frame",
        "name": "Marmotte 5\" Frame",
        "brand": "Armattan",
        "price_php": 5599,
        "weight_g": 96,
        "in_stock": True,
        "buy_url": "https://armattanquads.com/",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+marmotte"
        }
    },
    {
        "id": "geprc-mark5-lr-frame",
        "category": "frame",
        "name": "Mark5 LR Frame",
        "brand": "GEPRC",
        "price_php": 3299,
        "weight_g": 128,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 244,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5+lr"
        }
    },
    {
        "id": "flywoo-nin-2207-1850kv",
        "category": "motor",
        "name": "NIN 2207 1850KV",
        "brand": "Flywoo",
        "price_php": 1059,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1850,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 42
        }
    },
    {
        "id": "brotherhobby-avenger-2207-2-1800kv",
        "category": "motor",
        "name": "Avenger 2207.2 1800KV",
        "brand": "BrotherHobby",
        "price_php": 999,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://brotherhobby.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 41
        }
    },
    {
        "id": "holybro-tekko32-f4-60a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 60A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3899,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#001a00",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "hglrc-zeus-60a-4in1-esc",
        "category": "esc",
        "name": "Zeus 60A 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 2599,
        "weight_g": 27,
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
        "id": "hglrc-zeus-f765-fc",
        "category": "fc",
        "name": "Zeus F765 Flight Controller",
        "brand": "HGLRC",
        "price_php": 3199,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
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
            "diagram_url": "https://www.hglrc.com"
        }
    },
    {
        "id": "flywoo-goku-f405-hd-fc",
        "category": "fc",
        "name": "GOKU F405 HD Flight Controller",
        "brand": "Flywoo",
        "price_php": 2899,
        "weight_g": 9,
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
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://flywoo.net"
        }
    },
    {
        "id": "gemfan-hurricane-51499-5inch",
        "category": "propeller",
        "name": "Hurricane 51499 5\"",
        "brand": "Gemfan",
        "price_php": 239,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.99,
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
        "id": "hqprop-7x4x3-7inch",
        "category": "propeller",
        "name": "7X4X3 7\"",
        "brand": "HQProp",
        "price_php": 299,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey"
            ]
        }
    },
    {
        "id": "foxeer-falkor-3-camera",
        "category": "camera",
        "name": "Falkor 3 Camera",
        "brand": "Foxeer",
        "price_php": 1899,
        "weight_g": 7,
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
        "id": "runcam-racer-nano-2",
        "category": "camera",
        "name": "Racer Nano 2",
        "brand": "RunCam",
        "price_php": 1399,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "hglrc-zeus-1-6w-vtx",
        "category": "vtx",
        "name": "Zeus 1.6W VTX",
        "brand": "HGLRC",
        "price_php": 2999,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
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
        "id": "iflight-readytostar-r46-vtx",
        "category": "vtx",
        "name": "ReadyToSky R46 VTX",
        "brand": "iFlight",
        "price_php": 1799,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-24V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-rline-4-0-1300mah-6s",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S",
        "brand": "Tattu",
        "price_php": 2399,
        "weight_g": 240,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
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
        "id": "cnhl-6s-1800mah-100c",
        "category": "battery",
        "name": "1800mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2199,
        "weight_g": 320,
        "in_stock": True,
        "buy_url": "https://cnhl-fpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1800,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-elrs-rp1-rx",
        "category": "receiver",
        "name": "ExpressLRS RP1 Receiver",
        "brand": "HappyModel",
        "price_php": 949,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "tbs-crossfire-nano-se-rx",
        "category": "receiver",
        "name": "Crossfire Nano SE Receiver",
        "brand": "TBS",
        "price_php": 1699,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "matek-m10q-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1499,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "axisflying-pico-gps",
        "category": "gps",
        "name": "Pico GPS Module",
        "brand": "AxisFlying",
        "price_php": 1299,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/collections/gps",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "foxeer-lollipop4-58-rhcp",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP",
        "brand": "Foxeer",
        "price_php": 599,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "axisflying-t-antenna",
        "category": "antenna",
        "name": "T-Shape 5.8GHz Antenna",
        "brand": "AxisFlying",
        "price_php": 699,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
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
