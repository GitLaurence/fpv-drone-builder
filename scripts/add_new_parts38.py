#!/usr/bin/env python3
"""Add 38th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "axisflying-cinepro-v2-5-frame",
        "category": "frame",
        "name": "Cinepro V2 5\" Freestyle Frame",
        "brand": "Axisflying",
        "price_php": 2050,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Axisflying+Cinepro+V2+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+cinepro+v2"
        }
    },
    {
        "id": "iflight-xing2-2807-1300kv",
        "category": "motor",
        "name": "XING2 2807 1300KV",
        "brand": "iFlight",
        "price_php": 1380,
        "weight_g": 46,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+XING2+2807+1300KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },
    {
        "id": "geprc-smart32-60a-4in1",
        "category": "esc",
        "name": "SMART32 60A 4-in-1 ESC",
        "brand": "GEPRC",
        "price_php": 2180,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+SMART32+60A+4-in-1+ESC",
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
        "id": "hglrc-zeus-f745-v2-fc",
        "category": "fc",
        "name": "Zeus F745 V2 Flight Controller",
        "brand": "HGLRC",
        "price_php": 3450,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Zeus+F745+V2+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-mark2-5152-propeller",
        "category": "propeller",
        "name": "Mark2 5152 5\" Bi-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 200,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Mark2+5152",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 5.2,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray",
                "green"
            ]
        }
    },
    {
        "id": "foxeer-razer-nano-2-camera",
        "category": "camera",
        "name": "Razer Nano 2 FPV Camera",
        "brand": "Foxeer",
        "price_php": 1430,
        "weight_g": 5.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Razer+Nano+2",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "eachine-vtx03-super-mini-vtx",
        "category": "vtx",
        "name": "VTX03 Super Mini 5.8GHz VTX",
        "brand": "Eachine",
        "price_php": 860,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Eachine+VTX03+Super+Mini",
        "color": "#222222",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "ovonic-1400mah-4s-75c",
        "category": "battery",
        "name": "1400mAh 4S 75C LiPo",
        "brand": "Ovonic",
        "price_php": 750,
        "weight_g": 155,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ovonic+1400mAh+4S+75C",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1400,
            "c_rating": 75,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "flysky-fs-x6b-rx",
        "category": "receiver",
        "name": "FS-X6B 2.4GHz Receiver",
        "brand": "FlySky",
        "price_php": 690,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FlySky+FS-X6B+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "AFHDS 2A",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 1.5
        }
    },
    {
        "id": "ublox-neo-m9n-gps",
        "category": "gps",
        "name": "NEO-M9N GPS Module",
        "brand": "u-blox",
        "price_php": 1550,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=u-blox+NEO-M9N+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "interface": "UART",
            "compass": True,
            "weight_g": 7,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "foxeer-lollipop-8-5.8ghz-antenna",
        "category": "antenna",
        "name": "Lollipop 8 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 460,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Lollipop+8+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
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
