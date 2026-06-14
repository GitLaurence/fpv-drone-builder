#!/usr/bin/env python3
"""Add 39th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "tbs-source-one-v5-5-frame",
        "category": "frame",
        "name": "Source One V5 5\" Frame",
        "brand": "TBS",
        "price_php": 1650,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Source+One+V5+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+v5"
        }
    },
    {
        "id": "brotherhobby-avenger-2807-5-1500kv",
        "category": "motor",
        "name": "Avenger 2807.5 1500KV",
        "brand": "BrotherHobby",
        "price_php": 1450,
        "weight_g": 47,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2807.5+1500KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1500,
            "stator_size": "2807",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "tmotor-f55a-pro-iii-4in1-esc",
        "category": "esc",
        "name": "F55A PRO III 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 2750,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F55A+PRO+III+4-in-1+ESC",
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
        "id": "diatone-mamba-mk4-f405-fc",
        "category": "fc",
        "name": "MAMBA MK4 F405 Flight Controller",
        "brand": "Diatone",
        "price_php": 2650,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+MK4+F405+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-dp5x4-3x3-v1s-triblade-propeller",
        "category": "propeller",
        "name": "DP5X4.3X3 V1S 5\" Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 210,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP5X4.3X3+V1S",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "black",
                "orange"
            ]
        }
    },
    {
        "id": "caddx-baby-ratel-2-camera",
        "category": "camera",
        "name": "Baby Ratel 2 FPV Camera",
        "brand": "Caddx",
        "price_php": 1650,
        "weight_g": 7.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Baby+Ratel+2",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "iflight-ts5g-v3-vtx",
        "category": "vtx",
        "name": "TS5G V3 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 1480,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+TS5G+V3+VTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-r-line-1300mah-4s-130c",
        "category": "battery",
        "name": "R-Line 1300mAh 4S 130C LiPo",
        "brand": "Tattu",
        "price_php": 1480,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+1300mAh+4S+130C",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "radiomaster-rp4-elrs-rx",
        "category": "receiver",
        "name": "RP4 2.4GHz ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 780,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RadioMaster+RP4+ELRS+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "foxeer-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "Foxeer",
        "price_php": 1180,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+M10+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "interface": "UART",
            "compass": True,
            "weight_g": 6,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "truerc-xair-5-8ghz-antenna",
        "category": "antenna",
        "name": "X-Air 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 650,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+X-Air+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.9,
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
