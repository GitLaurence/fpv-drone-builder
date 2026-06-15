#!/usr/bin/env python3
"""Add 44th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-hex-7-frame",
        "category": "frame",
        "name": "Hex 7\" Frame",
        "brand": "Flywoo",
        "price_php": 2200,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Hex+7+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 40,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+hex+7"
        }
    },
    {
        "id": "flywoo-robo-2605-motor",
        "category": "motor",
        "name": "ROBO 2605 1500KV Motor",
        "brand": "Flywoo",
        "price_php": 1350,
        "weight_g": 41,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+ROBO+2605+Motor",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1500,
            "stator_size": "2605",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 8,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "mamba-f60-pro-v3-esc",
        "category": "esc",
        "name": "F60 Pro V3 60A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 3200,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F60+Pro+V3+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "iflight-succex-e-f405-v2-fc",
        "category": "fc",
        "name": "SucceX-E F405 V2.1 Flight Controller",
        "brand": "iFlight",
        "price_php": 1800,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+SucceX-E+F405+V2.1+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": True,
            "diagram_url": "https://shop.iflight.com/SucceX-E-F405-V2-1-Flight-Controller"
        }
    },
    {
        "id": "dalprop-t5048c-propeller",
        "category": "propeller",
        "name": "T5048C 5\" Tri-Blade Propeller",
        "brand": "DALPROP",
        "price_php": 220,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DALPROP+T5048C+Propeller",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "grey",
                "black",
                "transparent"
            ]
        }
    },
    {
        "id": "foxeer-mini-cat-3-camera",
        "category": "camera",
        "name": "Mini Cat 3 FPV Camera",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Mini+Cat+3+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "iflight-tt-race-58-vtx",
        "category": "vtx",
        "name": "TT Race 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 1600,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+TT+Race+5.8GHz+VTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "5.8GHz 40CH",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-rline-1400mah-4s-130c",
        "category": "battery",
        "name": "R-Line 1400mAh 4S 130C LiPo",
        "brand": "Tattu",
        "price_php": 1450,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Tattu+R-Line+1400mAh+4S+130C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1400,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "geprc-elrs-rx5-receiver",
        "category": "receiver",
        "name": "ELRS RX5 Nano Receiver",
        "brand": "GEPRC",
        "price_php": 750,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=GEPRC+ELRS+RX5+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "iflight-m8n-gps-module",
        "category": "gps",
        "name": "M8N GPS Module",
        "brand": "iFlight",
        "price_php": 1450,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+M8N+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 29,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "lumenier-pagoda-2-antenna",
        "category": "antenna",
        "name": "Pagoda 2 5.8GHz Antenna",
        "brand": "Lumenier",
        "price_php": 480,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+Pagoda+2+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    }
]


def main():
    with open("data/parts.json") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            raise ValueError(f"Duplicate id: {part['id']}")

    data["parts"].extend(NEW_PARTS)

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added {len(NEW_PARTS)} parts. Total parts: {len(data['parts'])}")


if __name__ == "__main__":
    main()
