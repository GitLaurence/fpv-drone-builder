#!/usr/bin/env python3
"""Add a ninth batch of 14 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "geprc-mark5-hd-frame",
        "category": "frame",
        "name": "Mark5 HD Frame",
        "brand": "GEPRC",
        "price_php": 3450,
        "weight_g": 108,
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
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5"
        }
    },
    {
        "id": "impulserc-reverb-frame",
        "category": "frame",
        "name": "Reverb Frame",
        "brand": "ImpulseRC",
        "price_php": 4800,
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
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=impulserc+reverb"
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "diatone-mamba-f45-128k-4in1",
        "category": "esc",
        "name": "Mamba F45_128K 45A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 2300,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "spedix-s12-v3-50a-4in1",
        "category": "esc",
        "name": "S12 V3 50A 4-in-1 ESC",
        "brand": "Spedix",
        "price_php": 2650,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ──────────────────────────────────────────────────
    {
        "id": "iflight-blitz-f7-pro-aio-fc",
        "category": "fc",
        "name": "BLITZ F7 Pro AIO Flight Controller",
        "brand": "iFlight",
        "price_php": 4100,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://shop.iflight.com/Blitz-F7-Pro-AIO-Flight-Controller"
        }
    },
    {
        "id": "foxeer-f722-v4-fc",
        "category": "fc",
        "name": "F722 V4 Flight Controller",
        "brand": "Foxeer",
        "price_php": 2450,
        "weight_g": 8.9,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.foxeer.com/products/foxeer-f722-v4-flight-controller"
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "hqprop-dp-5x4.3x3-v1s",
        "category": "propeller",
        "name": "DP 5x4.3x3 V1S",
        "brand": "HQProp",
        "price_php": 230,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
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
        "id": "azure-power-switchblade-5",
        "category": "propeller",
        "name": "Switchblade 5",
        "brand": "Azure Power",
        "price_php": 260,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "blue",
                "green"
            ]
        }
    },

    # ─── FPV CAMERAS (2) ─────────────────────────────────────────────────────────
    {
        "id": "runcam-link-wasp-camera",
        "category": "camera",
        "name": "Link Wasp Camera",
        "brand": "RunCam",
        "price_php": 3200,
        "weight_g": 7.4,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Digital",
            "tvl": 1000,
            "voltage_range": "6.5-28V"
        }
    },
    {
        "id": "dji-o4-air-unit-pro-camera",
        "category": "camera",
        "name": "O4 Air Unit Pro Camera",
        "brand": "DJI",
        "price_php": 8500,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.dji.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.3\" CMOS",
            "fov_deg": 162,
            "format": "Digital",
            "tvl": 1000,
            "voltage_range": "6-27V"
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────────
    {
        "id": "happymodel-ep1-elrs-rx",
        "category": "receiver",
        "name": "EP1 2.4GHz ELRS Receiver",
        "brand": "HappyModel",
        "price_php": 750,
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
        "id": "frsky-r9-mm-mini-rx",
        "category": "receiver",
        "name": "R9 MM Mini Receiver",
        "brand": "FrSky",
        "price_php": 1300,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 35
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "holybro-pixhawk-mini-gps-module",
        "category": "gps",
        "name": "Pixhawk Mini GPS Module",
        "brand": "Holybro",
        "price_php": 2200,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-osd-gps",
        "category": "gps",
        "name": "M10Q-OSD GPS",
        "brand": "Matek",
        "price_php": 1550,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-osd",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": False,
            "connector": "JST-SH 4-pin"
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
