#!/usr/bin/env python3
"""Add 30th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-mark5-hd5-frame",
        "category": "frame",
        "name": "Mark5 HD5 5\" Frame",
        "brand": "GEPRC",
        "price_php": 3120,
        "weight_g": 96,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Mark5+HD5",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "brotherhobby-avenger-2812-5",
        "category": "motor",
        "name": "Avenger 2812.5",
        "brand": "BrotherHobby",
        "price_php": 1320,
        "weight_g": 56,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2812.5",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2812.5",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 6,
            "max_voltage_s": 8,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "foxeer-reaper-f4-65a-esc",
        "category": "esc",
        "name": "Reaper F4 65A 4-in-1",
        "brand": "Foxeer",
        "price_php": 2790,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Reaper+F4+65A+4-in-1",
        "color": "#1a0000",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "iflight-blitz-f7-pro-v2",
        "category": "fc",
        "name": "Blitz F7 Pro V2",
        "brand": "iFlight",
        "price_php": 2980,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Blitz+F7+Pro+V2",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688-P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-mayfly-1631-prop",
        "category": "propeller",
        "name": "Mayfly 1631 Tri-Blade",
        "brand": "Gemfan",
        "price_php": 195,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Gemfan+Mayfly+1631",
        "color": "#111",
        "specs": {
            "diameter_inch": 1.6,
            "pitch": 3.1,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": [
                "black",
                "gray",
                "green"
            ]
        }
    },
    {
        "id": "foxeer-toothless-3-cam",
        "category": "camera",
        "name": "Toothless 3 Nano",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Toothless+3+Nano",
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
        "id": "walksnail-moonlight-vtx",
        "category": "vtx",
        "name": "Moonlight Digital VTX",
        "brand": "Walksnail",
        "price_php": 4550,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Moonlight+VTX",
        "color": "#1a1a2a",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital HD",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-ministar-1300-6s",
        "category": "battery",
        "name": "MiniStar 1300mAh 6S",
        "brand": "CNHL",
        "price_php": 1480,
        "weight_g": 196,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=CNHL+MiniStar+1300mAh+6S",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "radiomaster-rp1-rx",
        "category": "receiver",
        "name": "RP1 ELRS Nano",
        "brand": "RadioMaster",
        "price_php": 870,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=RadioMaster+RP1+ELRS",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "betafpv-m10-gps-mini",
        "category": "gps",
        "name": "M10 GPS Mini",
        "brand": "BetaFPV",
        "price_php": 1180,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=BetaFPV+M10+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "foxeer-lollipop-4-plus-antenna",
        "category": "antenna",
        "name": "Lollipop 4 Plus RHCP",
        "brand": "Foxeer",
        "price_php": 520,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Lollipop+4+Plus",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
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
