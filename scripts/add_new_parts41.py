#!/usr/bin/env python3
"""Add 41st batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "hglrc-sector-5-v5-frame",
        "category": "frame",
        "name": "Sector 5 V5 Freestyle Frame",
        "brand": "HGLRC",
        "price_php": 2350,
        "weight_g": 86,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Sector+5+V5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=hglrc+sector+5+v5"
        }
    },
    {
        "id": "flywoo-robo-rs2207-5-1750kv",
        "category": "motor",
        "name": "Robo RS2207.5 1750KV",
        "brand": "Flywoo",
        "price_php": 950,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Robo+RS2207.5+1750KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 35
        }
    },
    {
        "id": "diatone-mamba-f40-pro-iii-40a-esc",
        "category": "esc",
        "name": "Mamba F40 Pro III 40A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 1700,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F40+Pro+III+40A",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 45
        }
    },
    {
        "id": "geprc-taker-f405-fc",
        "category": "fc",
        "name": "Taker F405 Flight Controller",
        "brand": "GEPRC",
        "price_php": 1400,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Taker+F405+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-7x4x4-v1s-tri-blade",
        "category": "propeller",
        "name": "7X4X4 V1S Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 250,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+7X4X4+V1S+Tri-Blade",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "black"
            ]
        }
    },
    {
        "id": "foxeer-falkor-2-mini-camera",
        "category": "camera",
        "name": "Falkor 2 Mini FPV Camera",
        "brand": "Foxeer",
        "price_php": 1400,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Falkor+2+Mini+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "iflight-twig-vtx",
        "category": "vtx",
        "name": "TWIG 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 1700,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+TWIG+VTX",
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
        "id": "toolkitrc-gnb-1400mah-4s",
        "category": "battery",
        "name": "GNB 1400mAh 4S 100C LiPo",
        "brand": "ToolkitRC",
        "price_php": 850,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ToolkitRC+GNB+1400mAh+4S+100C",
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
        "id": "radiomaster-er5-elrs-nano-rx",
        "category": "receiver",
        "name": "ER5 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 700,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RadioMaster+ER5+ELRS+Nano+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 10
        }
    },
    {
        "id": "holybro-micro-m8n-gps",
        "category": "gps",
        "name": "Micro M8N GPS Module",
        "brand": "Holybro",
        "price_php": 1570,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Micro+M8N+GPS+Module",
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
        "id": "vas-crosshair-antenna",
        "category": "antenna",
        "name": "Crosshair 5.8GHz Antenna",
        "brand": "VAS",
        "price_php": 670,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=VAS+Crosshair+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omnidirectional"
        }
    }
]


def main():
    path = "data/parts.json"
    with open(path) as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            raise ValueError(f"Duplicate id: {part['id']}")

    data["parts"].extend(NEW_PARTS)

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added {len(NEW_PARTS)} parts. Total parts: {len(data['parts'])}")


if __name__ == "__main__":
    main()
