#!/usr/bin/env python3
"""Add 32nd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "armattan-rooster-x-5",
        "category": "frame",
        "name": "Rooster X 5\" Freestyle Frame",
        "brand": "Armattan",
        "price_php": 8450,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+X",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+x"
        }
    },
    {
        "id": "tmotor-velox-v2806-v2",
        "category": "motor",
        "name": "Velox V2806.5 V2 1300KV",
        "brand": "T-Motor",
        "price_php": 1450,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Velox+V2806.5+V2",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2806.5",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "diatone-mamba-f40-45a-v2",
        "category": "esc",
        "name": "Mamba F40 45A 4-in-1 ESC V2",
        "brand": "Diatone",
        "price_php": 1650,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F40+45A+V2",
        "color": "#1a0000",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 50
        }
    },
    {
        "id": "geprc-taker-f745-v2",
        "category": "fc",
        "name": "TAKER F745 V2 Flight Controller",
        "brand": "GEPRC",
        "price_php": 2100,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+TAKER+F745+V2",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-ethix-s6-5x4-3x3",
        "category": "propeller",
        "name": "Ethix S6 5\" Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 220,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S6",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "runcam-phoenix-2-vision",
        "category": "camera",
        "name": "Phoenix 2 Vision FPV Camera",
        "brand": "RunCam",
        "price_php": 1750,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Phoenix+2+Vision",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Switchable NTSC/PAL",
            "tvl": 1000,
            "voltage_range": "5-22V"
        }
    },
    {
        "id": "fxt-pard-pro-1-6w",
        "category": "vtx",
        "name": "PARD Pro 1.6W Smart Audio VTX",
        "brand": "FXT",
        "price_php": 1450,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FXT+PARD+Pro+1.6W",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-black-series-1800mah-6s-100c",
        "category": "battery",
        "name": "Black Series 1800mAh 6S 100C LiPo",
        "brand": "CNHL",
        "price_php": 1750,
        "weight_g": 290,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1800mAh+6S+100C",
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
        "id": "happymodel-ep2-elrs-nano-rx",
        "category": "receiver",
        "name": "EP2 ELRS Nano RX",
        "brand": "HappyModel",
        "price_php": 620,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ELRS",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "matek-m9n-5883-v4",
        "category": "gps",
        "name": "M9N-5883 V4 GPS+Compass",
        "brand": "Matek",
        "price_php": 1450,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M9N-5883+V4",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "immersionrc-steadyview-patch",
        "category": "antenna",
        "name": "SteadyView Patch Antenna 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 950,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SteadyView+Patch",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 9,
            "polarization": "LHCP",
            "connector": "SMA",
            "type": "directional"
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
