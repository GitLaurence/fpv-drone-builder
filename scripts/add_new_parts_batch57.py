#!/usr/bin/env python3
"""Batch 57: real, current-production FPV parts across all 11 categories,
adding more brand/model coverage on top of batch56 (filling gaps in FC/GPS)."""
import json

NEW_PARTS = [
    # ========== FC ==========
    {
        "id": "mateksys-h743-slim-fc",
        "category": "fc",
        "name": "H743-SLIM Flight Controller",
        "brand": "Matek",
        "price_php": 3696,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+H743-SLIM+Flight+Controller",
        "color": "#002233",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "iflight-blitz-f7-pro-fc",
        "category": "fc",
        "name": "Blitz F7 Pro Flight Controller",
        "brand": "iFlight",
        "price_php": 2856,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=Blitz+F7+Pro+Flight+Controller",
        "color": "#181818",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "diatone-mamba-f405-mk4-fc",
        "category": "fc",
        "name": "Mamba F405 Mk4 Flight Controller",
        "brand": "Diatone",
        "price_php": 1848,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Mamba+F405+Mk4+Flight+Controller",
        "color": "#0f1115",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": False,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    # ========== GPS ==========
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS + Compass Module",
        "brand": "Matek",
        "price_php": 1568,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-5883+GPS+Compass+Module",
        "color": "#0a2233",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 15,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "holybro-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "Holybro",
        "price_php": 1904,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=M10+GPS+Module",
        "color": "#101010",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 16,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    # ========== ANTENNA ==========
    {
        "id": "rushfpv-cherry-nano-mmcx-antenna",
        "category": "antenna",
        "name": "Cherry Nano 5.8GHz RHCP MMCX",
        "brand": "RushFPV",
        "price_php": 448,
        "weight_g": 3.2,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Cherry+Nano+5.8GHz+RHCP+MMCX",
        "color": "#1a1a1a",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "MMCX",
            "gain_dbi": 1.9,
            "type": "cloverleaf"
        }
    },
    # ========== CAMERA ==========
    {
        "id": "caddx-ratel-2-camera",
        "category": "camera",
        "name": "Ratel 2 1200TVL Analog",
        "brand": "Caddx",
        "price_php": 1288,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ratel+2+1200TVL",
        "color": "#141414",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    # ========== VTX ==========
    {
        "id": "rushfpv-tank-max-vtx",
        "category": "vtx",
        "name": "Tank Max 5.8GHz 1.6W VTX",
        "brand": "RushFPV",
        "price_php": 4368,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Tank+Max+5.8GHz+1.6W+VTX",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-27V",
            "connector": "MMCX"
        }
    },
    # ========== BATTERY ==========
    {
        "id": "gnb-6s-1400mah-battery",
        "category": "battery",
        "name": "6S 1400mAh 90C",
        "brand": "GNB",
        "price_php": 2296,
        "weight_g": 232,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+6S+1400mAh+90C",
        "color": "#151515",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 90,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    # ========== PROPELLER ==========
    {
        "id": "ethix-s5-propeller",
        "category": "propeller",
        "name": "S5 5x4.6x3 Tri-blade",
        "brand": "Ethix",
        "price_php": 252,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+S5+Propeller",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "purple",
                "grey"
            ]
        }
    },
    # ========== MOTOR ==========
    {
        "id": "xing2-2306-1800kv-motor",
        "category": "motor",
        "name": "XING2 2306 1800KV",
        "brand": "iFlight",
        "price_php": 1288,
        "weight_g": 31.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=XING2+2306+1800KV",
        "color": "#181818",
        "specs": {
            "kv": 1800,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },
    # ========== ESC ==========
    {
        "id": "hglrc-fd60-60a-esc",
        "category": "esc",
        "name": "FD60 60A 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 2744,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=FD60+60A+4-in-1+ESC",
        "color": "#0f0f0f",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    # ========== RECEIVER ==========
    {
        "id": "betafpv-elrs-nano-2-4g-receiver",
        "category": "receiver",
        "name": "ELRS Nano 2.4G Receiver",
        "brand": "BetaFPV",
        "price_php": 728,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=BetaFPV+ELRS+Nano+2.4G+Receiver",
        "color": "#111111",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    # ========== FRAME ==========
    {
        "id": "flywoo-hexplorer-lr4-frame",
        "category": "frame",
        "name": "Hexplorer LR4 Frame",
        "brand": "Flywoo",
        "price_php": 2408,
        "weight_g": 84,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Hexplorer+LR4+Frame",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 20.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 3.5,
            "standoff_height_mm": 22
        }
    },
]


def main():
    with open("data/parts.json", "r") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    added = 0
    skipped = 0

    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"  SKIP (duplicate): {part['id']}")
            skipped += 1
        else:
            data["parts"].append(part)
            existing_ids.add(part["id"])
            added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = len(data["parts"])
    print(f"\nAdded {added} new parts (skipped {skipped} duplicates)")
    print(f"Total parts now: {total}")

    from collections import Counter
    cats = Counter(p["category"] for p in data["parts"])
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
