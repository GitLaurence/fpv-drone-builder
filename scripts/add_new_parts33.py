#!/usr/bin/env python3
"""Add 33rd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "armattan-marmotte-5-frame",
        "category": "frame",
        "name": "Marmotte 5\" Freestyle Frame",
        "brand": "Armattan",
        "price_php": 5000,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Marmotte",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+marmotte"
        }
    },
    {
        "id": "brotherhobby-avenger-2807-5-1300kv",
        "category": "motor",
        "name": "Avenger 2807.5 1300KV",
        "brand": "BrotherHobby",
        "price_php": 1500,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2807.5",
        "color": "#3a3a3a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807.5",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "iflight-succex-e-mini-f4-45a-4in1",
        "category": "esc",
        "name": "SucceX-E Mini F4 45A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 1700,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+SucceX-E+Mini+F4+45A",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 50
        }
    },
    {
        "id": "iflight-blitz-f7-pro-fc",
        "category": "fc",
        "name": "Blitz F7 Pro Flight Controller",
        "brand": "iFlight",
        "price_php": 2800,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Blitz+F7+Pro",
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
        "id": "gemfan-hurricane-51499-3blade",
        "category": "propeller",
        "name": "Hurricane 51499 5\" Tri-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 200,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51499",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.99,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "caddx-nebula-pro-nano-camera",
        "category": "camera",
        "name": "Nebula Pro Nano Digital Camera",
        "brand": "Caddx",
        "price_php": 2250,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Nebula+Pro+Nano",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },
    {
        "id": "tbs-unify-evo-pro32-nano-vtx",
        "category": "vtx",
        "name": "Unify Evo Pro32 Nano VTX",
        "brand": "TBS",
        "price_php": 2500,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Evo+Pro32+Nano",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "6-25V",
            "connector": "U.FL"
        }
    },
    {
        "id": "tattu-rline-4-1550mah-6s-130c",
        "category": "battery",
        "name": "R-Line 4.0 1550mAh 6S 130C LiPo",
        "brand": "Tattu",
        "price_php": 1800,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+4.0+1550mAh+6S",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1550,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "iflight-elrs-nano-rx",
        "category": "receiver",
        "name": "ELRS 2.4GHz Nano Receiver",
        "brand": "iFlight",
        "price_php": 850,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+ELRS+Nano+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "iflight-m10-gps-compass",
        "category": "gps",
        "name": "M10 GPS+Compass Module",
        "brand": "iFlight",
        "price_php": 1100,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+M10+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "truerc-singularity-5_8",
        "category": "antenna",
        "name": "Singularity 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 1400,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Singularity+5.8",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "LHCP/RHCP",
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
