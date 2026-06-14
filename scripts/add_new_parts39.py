#!/usr/bin/env python3
"""Add 39th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-hexmix7-hd-frame",
        "category": "frame",
        "name": "Hex Mix 7\" HD Freestyle Frame",
        "brand": "Flywoo",
        "price_php": 3200,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Hex+Mix+7+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+hex+mix+7"
        }
    },
    {
        "id": "brotherhobby-avenger-2807.5-1300kv",
        "category": "motor",
        "name": "Avenger 2807.5 1300KV",
        "brand": "BrotherHobby",
        "price_php": 1450,
        "weight_g": 56,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2807.5+1300KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807.5",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "spedix-sx40-50a-4in1-esc",
        "category": "esc",
        "name": "SX40 50A 4-in-1 ESC",
        "brand": "Spedix",
        "price_php": 2350,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Spedix+SX40+50A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "diatone-mamba-mk4-f722-mini-fc",
        "category": "fc",
        "name": "Mamba MK4 F722 Mini Flight Controller",
        "brand": "Diatone",
        "price_php": 2890,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+MK4+F722+Mini+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-ethix-s5-propeller",
        "category": "propeller",
        "name": "Ethix S5 5\" Propeller",
        "brand": "HQProp",
        "price_php": 240,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S5",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "grey",
                "lime"
            ]
        }
    },
    {
        "id": "runcam-racer-4-camera",
        "category": "camera",
        "name": "Racer 4 FPV Camera",
        "brand": "RunCam",
        "price_php": 1850,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Racer+4",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "diatone-mamba-tx800-vtx",
        "category": "vtx",
        "name": "Mamba TX800 5.8GHz VTX",
        "brand": "Diatone",
        "price_php": 1480,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+TX800+VTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "tattu-r-line-4.0-1300mah-6s",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S 130C LiPo",
        "brand": "Tattu",
        "price_php": 2450,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+4.0+1300mAh+6S",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "frsky-r9-slim-plus-ota-rx",
        "category": "receiver",
        "name": "R9 Slim+ OTA 900MHz Receiver",
        "brand": "FrSky",
        "price_php": 1650,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R9+Slim+Plus+OTA+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "bn-220-gps",
        "category": "gps",
        "name": "BN-220 GPS+Compass Module",
        "brand": "Beitian",
        "price_php": 980,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-220+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "axii-2-antenna",
        "category": "antenna",
        "name": "AXII 2 5.8GHz Antenna",
        "brand": "ImmersionRC",
        "price_php": 850,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+AXII+2+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
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
