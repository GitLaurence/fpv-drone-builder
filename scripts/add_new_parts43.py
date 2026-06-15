#!/usr/bin/env python3
"""Add 43rd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-nazgul-evoque-f6x-frame",
        "category": "frame",
        "name": "Nazgul Evoque F6X 6\" Frame",
        "brand": "iFlight",
        "price_php": 3480,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Nazgul+Evoque+F6X",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 280,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 6,
            "material": "carbon fiber",
            "stack_mount_mm": 30
        }
    },
    {
        "id": "tmotor-f60-pro-v-2207-5-1900kv",
        "category": "motor",
        "name": "F60 PRO V 2207.5 1900KV",
        "brand": "T-Motor",
        "price_php": 1910,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F60+PRO+V+2207.5+1900KV",
        "color": "#0d0d0d",
        "specs": {
            "kv": 1900,
            "stator_size": "2207.5",
            "motor_mount_mm": 16,
            "max_voltage_s": 6
        }
    },
    {
        "id": "iflight-blitz-e55-v3-4in1",
        "category": "esc",
        "name": "BLITZ E55 V3 4-in-1 55A ESC",
        "brand": "iFlight",
        "price_php": 2610,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+BLITZ+E55+V3+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": "3-6S",
            "protocol": "AM32",
            "form_factor_mm": 30
        }
    },
    {
        "id": "foxeer-reaper-f722-v3-aio",
        "category": "fc",
        "name": "Reaper F722 V3 AIO Flight Controller",
        "brand": "Foxeer",
        "price_php": 2610,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Reaper+F722+V3+AIO",
        "color": "#0d0d0d",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30
        }
    },
    {
        "id": "gemfan-hurricane-5125-4-4blade",
        "category": "propeller",
        "name": "Hurricane 5125-4 4-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 200,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+5125-4+4-Blade",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.5,
            "blade_count": 4,
            "shaft_mm": 5
        }
    },
    {
        "id": "foxeer-razer-mini-v4",
        "category": "camera",
        "name": "Razer Mini V4 FPV Camera",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Razer+Mini+V4",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "NTSC/PAL switchable",
            "video_system": "analog"
        }
    },
    {
        "id": "foxeer-tm25-pro-vtx",
        "category": "vtx",
        "name": "TM25 Pro 5.8GHz VTX",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+TM25+Pro+VTX",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 600,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },
    {
        "id": "tattu-rline-4-1100mah-4s-150c",
        "category": "battery",
        "name": "R-Line 4.0 1100mAh 4S 150C",
        "brand": "Tattu",
        "price_php": 1280,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Tattu+R-Line+4.0+1100mAh+4S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1100,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "happymodel-pocketrx-elrs",
        "category": "receiver",
        "name": "PocketRX ELRS 2.4GHz Receiver",
        "brand": "HappyModel",
        "price_php": 700,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+PocketRX+ELRS",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "speedybee-m10-gps-lite",
        "category": "gps",
        "name": "M10 GPS Lite",
        "brand": "SpeedyBee",
        "price_php": 1050,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+M10+GPS+Lite",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "immersionrc-slipstream-5-8",
        "category": "antenna",
        "name": "SlipStream 5.8GHz Antenna",
        "brand": "ImmersionRC",
        "price_php": 460,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SlipStream+5.8GHz",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "SMA",
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
