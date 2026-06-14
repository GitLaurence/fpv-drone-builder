#!/usr/bin/env python3
"""Add 31st batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-explorer-lr4-v3",
        "category": "frame",
        "name": "Explorer LR4 V3 4\" HD Long Range Frame",
        "brand": "Flywoo",
        "price_php": 3250,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Explorer+LR4+V3",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 188,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "brotherhobby-avenger-2806-5-v4",
        "category": "motor",
        "name": "Avenger 2806.5 V4 1500KV",
        "brand": "BrotherHobby",
        "price_php": 1380,
        "weight_g": 58,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2806.5+V4",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1500,
            "stator_size": "2806.5",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "geprc-span-f4-45a-esc",
        "category": "esc",
        "name": "SPAN F4 45A 4-in-1 ESC",
        "brand": "GEPRC",
        "price_php": 1880,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+SPAN+F4+45A",
        "color": "#1a0000",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "iflight-succex-d-f7-v2-1",
        "category": "fc",
        "name": "SucceX-D F7 V2.1 Flight Controller",
        "brand": "iFlight",
        "price_php": 2650,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=SucceX-D+F7+V2.1",
        "color": "#000033",
        "specs": {
            "gyro": "ICM20689",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-flash-5052-3",
        "category": "propeller",
        "name": "Flash 5052 3-Blade",
        "brand": "Gemfan",
        "price_php": 180,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Flash+5052",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 5.2,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "foxeer-razer-mini-camera",
        "category": "camera",
        "name": "Razer Mini Pro 2 1/1.2\" Starlight Camera",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Razer+Mini+Pro+2",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/1.2\" CMOS Starlight",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "tbs-unify-pro32-hv-nano",
        "category": "vtx",
        "name": "Unify Pro32 HV Nano VTX",
        "brand": "TBS",
        "price_php": 3250,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "gensace-1100mah-6s-100c",
        "category": "battery",
        "name": "1100mAh 6S 100C LiPo",
        "brand": "Gens Ace",
        "price_php": 1380,
        "weight_g": 190,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gens+Ace+1100mAh+6S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-elrs-pwm-nano-rx",
        "category": "receiver",
        "name": "ELRS PWM Nano RX",
        "brand": "HappyModel",
        "price_php": 650,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+ELRS+PWM+Nano+RX",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "axisflying-m8-gps",
        "category": "gps",
        "name": "M8 GPS Module",
        "brand": "AxisFlying",
        "price_php": 980,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+M8+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "lumenier-axii-pro-5-8",
        "category": "antenna",
        "name": "AXII Pro 5.8GHz RHCP",
        "brand": "Lumenier",
        "price_php": 660,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+AXII+Pro",
        "color": "#0d0d0d",
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
