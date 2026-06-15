#!/usr/bin/env python3
"""Add 43rd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-nazgul-evoque-f5-v3-frame",
        "category": "frame",
        "name": "Nazgul Evoque F5 V3 Frame",
        "brand": "iFlight",
        "price_php": 2890,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Nazgul+Evoque+F5+V3+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+nazgul+evoque+f5"
        }
    },
    {
        "id": "t-motor-f60-pro-v-wave-2207",
        "category": "motor",
        "name": "F60 Pro V Wave 2207",
        "brand": "T-Motor",
        "price_php": 1690,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F60+Pro+V+Wave+2207",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "spedix-ec45-aio-65a-esc",
        "category": "esc",
        "name": "EC45 AIO 65A 4-in-1 ESC",
        "brand": "Spedix",
        "price_php": 3650,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Spedix+EC45+AIO+65A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "mateksys-h743-slim-fc",
        "category": "fc",
        "name": "H743 SLIM Flight Controller",
        "brand": "Mateksys",
        "price_php": 4350,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Mateksys+H743+SLIM+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": "16MB flash",
            "uarts": 8
        }
    },
    {
        "id": "hqprop-5x4-3x3-v1s-prop",
        "category": "propeller",
        "name": "5X4.3X3 V1S Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 195,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+5X4.3X3+V1S+Propeller",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch_inch": 4.3,
            "blades": 3,
            "hub_mm": 5,
            "material": "polycarbonate"
        }
    },
    {
        "id": "runcam-phoenix-2-vista-camera",
        "category": "camera",
        "name": "Phoenix 2 Vista FPV Camera",
        "brand": "RunCam",
        "price_php": 2950,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Phoenix+2+Vista+FPV+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/2 inch CMOS",
            "resolution": "1280x960",
            "fov_deg": 165,
            "min_illumination_lux": 0.001,
            "voltage_input_v": "6-22"
        }
    },
    {
        "id": "rushfpv-tank-max-pro-vtx",
        "category": "vtx",
        "name": "Tank Max Pro 1.6W VTX",
        "brand": "RushFPV",
        "price_php": 4200,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RushFPV+Tank+Max+Pro+VTX",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "power_levels_mw": [25, 200, 400, 800, 1600],
            "channels": 40,
            "connector": "MMCX",
            "video_format": "Analog"
        }
    },
    {
        "id": "cnhl-mini-tank-1300mah-6s-battery",
        "category": "battery",
        "name": "MiniTank 1300mAh 6S 100C LiPo",
        "brand": "CNHL",
        "price_php": 2150,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniTank+1300mAh+6S+100C",
        "color": "#cc0000",
        "specs": {
            "capacity_mah": 1300,
            "voltage_s": 6,
            "discharge_rate_c": 100,
            "connector": "XT60",
            "dimensions_mm": "76x35x35"
        }
    },
    {
        "id": "team-blacksheep-crossfire-nano-rx",
        "category": "receiver",
        "name": "Crossfire Nano RX",
        "brand": "TBS",
        "price_php": 1750,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+RX",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency_mhz": 915,
            "antenna_count": 1,
            "telemetry": True,
            "voltage_input_v": "5"
        }
    },
    {
        "id": "beitian-bn-280-mini-gps",
        "category": "gps",
        "name": "BN-280 Mini GPS/Compass Module",
        "brand": "Beitian",
        "price_php": 980,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-280+Mini+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "chipset": "Ublox M8030",
            "channels": 32,
            "compass": True,
            "update_rate_hz": 10,
            "voltage_input_v": "3.3-5"
        }
    },
    {
        "id": "rushfpv-cherry-mushroom-antenna",
        "category": "antenna",
        "name": "Cherry Mushroom 5.8GHz Antenna",
        "brand": "RushFPV",
        "price_php": 380,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RushFPV+Cherry+Mushroom+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
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
