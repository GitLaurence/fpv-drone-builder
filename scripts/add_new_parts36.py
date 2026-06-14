#!/usr/bin/env python3
"""Add 36th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-mark5-hd7-v3-frame",
        "category": "frame",
        "name": "Mark5 HD7 V3 7\" Frame",
        "brand": "GEPRC",
        "price_php": 4200,
        "weight_g": 158,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Mark5+HD7+V3",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5+hd7"
        }
    },
    {
        "id": "brotherhobby-avenger-2407.5-2400kv",
        "category": "motor",
        "name": "Avenger 2407.5 2400KV",
        "brand": "BrotherHobby",
        "price_php": 1450,
        "weight_g": 31.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2407.5+2400KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2400,
            "stator_size": "2407",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "iflight-blitz-e55-v2-55a-4in1",
        "category": "esc",
        "name": "BLITZ E55 V2 55A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 2600,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+BLITZ+E55+V2+55A+4-in-1",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "diatone-mamba-h743-mk9",
        "category": "fc",
        "name": "Mamba H743 Mk9 Flight Controller",
        "brand": "Diatone",
        "price_php": 4100,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+H743+Mk9",
        "color": "#000033",
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
        "id": "gemfan-hurricane-51499-v2-5blade-prop",
        "category": "propeller",
        "name": "Hurricane 51499 V2 5-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 230,
        "weight_g": 5.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51499+V2+5-Blade",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.99,
            "blade_count": 5,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "transparent"]
        }
    },
    {
        "id": "foxeer-razer-mini-v3-camera",
        "category": "camera",
        "name": "Razer Mini V3",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 5.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Razer+Mini+V3",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "rush-tank-nano-pro-vtx",
        "category": "vtx",
        "name": "Tank Nano Pro VTX",
        "brand": "RUSH",
        "price_php": 1900,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RUSH+Tank+Nano+Pro+VTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-ministar-1400mah-4s",
        "category": "battery",
        "name": "MiniStar 1400mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1250,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniStar+1400mAh+4S+100C",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1400,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "happymodel-ep2-elrs-pwm-rx",
        "category": "receiver",
        "name": "EP2 ELRS PWM Receiver",
        "brand": "Happymodel",
        "price_php": 700,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+EP2+ELRS+PWM",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "matek-m9n-5883-v5-gps",
        "category": "gps",
        "name": "M9N-5883 V5 GPS+Compass",
        "brand": "Matek",
        "price_php": 1550,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M9N-5883+V5+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "tbs-triumph-pro-v2-antenna",
        "category": "antenna",
        "name": "Triumph Pro V2 5.8GHz",
        "brand": "TBS",
        "price_php": 1500,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Triumph+Pro+V2+5.8GHz",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "RHCP",
            "connector": "U.FL",
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
