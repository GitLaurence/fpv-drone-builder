#!/usr/bin/env python3
"""Add a nineteenth batch of 11 new FPV parts to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-xl5-v5",
        "category": "frame",
        "name": "Nazgul XL5 V5.1 Frame Kit",
        "brand": "iFlight",
        "price_php": 3350,
        "weight_g": 128,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 230,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+xl5+v5"
        }
    },
    {
        "id": "speedybee-f405-v3",
        "category": "fc",
        "name": "F405 V3 30x30 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 1750,
        "weight_g": 8,
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
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com/speedybee-f405-v3-30x30-flight-controller/"
        }
    },
    {
        "id": "hqprop-ethix-s5-pure",
        "category": "propeller",
        "name": "Ethix S5 Pure",
        "brand": "HQProp",
        "price_php": 220,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#ccc",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["light grey", "black"]
        }
    },
    {
        "id": "foxeer-falkor-2-mini",
        "category": "camera",
        "name": "Falkor 2 Mini",
        "brand": "Foxeer",
        "price_php": 1900,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "runcam-swift-3",
        "category": "camera",
        "name": "Micro Swift 3",
        "brand": "RunCam",
        "price_php": 1800,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" Super HAD II CCD",
            "fov_deg": 150,
            "format": "Analog",
            "tvl": 600,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "rushfpv-max-solo-vtx",
        "category": "vtx",
        "name": "Max Solo VTX 2.5W",
        "brand": "RushFPV",
        "price_php": 2500,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://rushfpv.net",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-20V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-zeus-800mw-vtx",
        "category": "vtx",
        "name": "Zeus 800mW VTX",
        "brand": "HGLRC",
        "price_php": 1250,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-25.2V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-ministar-6s-1300mah",
        "category": "battery",
        "name": "MiniStar 1300mAh 6S 120C",
        "brand": "CNHL",
        "price_php": 1450,
        "weight_g": 246,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com",
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
        "id": "radiomaster-rp1-elrs-receiver",
        "category": "receiver",
        "name": "RP1 V2 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 1150,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "tbs-m10-gps-glonass",
        "category": "gps",
        "name": "M10 GPS Glonass Module",
        "brand": "TBS",
        "price_php": 1050,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 18,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m9n-gps",
        "category": "gps",
        "name": "M9N-5883 GNSS & Compass",
        "brand": "Matek",
        "price_php": 2300,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 25,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 6-pin"
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
