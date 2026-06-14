#!/usr/bin/env python3
"""Add 40th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "armattan-rooster-5-frame",
        "category": "frame",
        "name": "Rooster 5\" Frame",
        "brand": "Armattan",
        "price_php": 3550,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+5"
        }
    },
    {
        "id": "tmotor-velox-v2807",
        "category": "motor",
        "name": "Velox V2807 1300KV",
        "brand": "T-Motor",
        "price_php": 1350,
        "weight_g": 46,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Velox+V2807+1300KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "flycolor-x-cross-60a-v2",
        "category": "esc",
        "name": "X-Cross 60A V2 4-in-1 ESC",
        "brand": "Flycolor",
        "price_php": 2250,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+X-Cross+60A+V2",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "mateksys-f405-wmn",
        "category": "fc",
        "name": "F405-WMN Flight Controller",
        "brand": "Matek",
        "price_php": 1950,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F405-WMN+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-86344-3blade-propeller",
        "category": "propeller",
        "name": "8634-4 8.6\" Tri-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 260,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+8634-4+Tri-Blade+Propeller",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 8.6,
            "pitch": 4.4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "black"
            ]
        }
    },
    {
        "id": "runcam-racer-3-camera",
        "category": "camera",
        "name": "Racer 3 FPV Camera",
        "brand": "RunCam",
        "price_php": 1480,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Racer+3",
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
        "id": "rush-tank-max-vtx",
        "category": "vtx",
        "name": "TANK Max 1.6W VTX",
        "brand": "RUSH",
        "price_php": 2450,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RUSH+TANK+Max+VTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-1500mah-4s",
        "category": "battery",
        "name": "Black Series 1500mAh 4S 100C LiPo",
        "brand": "CNHL",
        "price_php": 1150,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1500mAh+4S+100C",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "frsky-r9-mm-rx",
        "category": "receiver",
        "name": "R9 MM 900MHz Receiver",
        "brand": "FrSky",
        "price_php": 1850,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R9+MM+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "holybro-st-m10-gps",
        "category": "gps",
        "name": "ST M10 GPS Module",
        "brand": "Holybro",
        "price_php": 1380,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+ST+M10+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "interface": "UART",
            "compass": True,
            "weight_g": 5,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "rush-cherry-2-antenna",
        "category": "antenna",
        "name": "Cherry 2 5.8GHz Antenna",
        "brand": "RUSH",
        "price_php": 620,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RUSH+Cherry+2+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "MMCX",
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
