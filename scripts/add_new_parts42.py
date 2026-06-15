#!/usr/bin/env python3
"""Add 42nd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-mark5-hd-v2-frame",
        "category": "frame",
        "name": "Mark5 HD V2 Freestyle Frame",
        "brand": "GEPRC",
        "price_php": 3120,
        "weight_g": 96,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Mark5+HD+V2",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5+hd"
        }
    },
    {
        "id": "axisflying-aurora5-v2-2207",
        "category": "motor",
        "name": "Aurora 5 V2 2207",
        "brand": "AxisFlying",
        "price_php": 1850,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+Aurora+5+V2+2207",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1960,
            "stator_size": "2207",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "flywoo-goku-gn745-aio-60a-esc",
        "category": "esc",
        "name": "Goku GN745 AIO 60A 4-in-1 ESC",
        "brand": "Flywoo",
        "price_php": 3400,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Goku+GN745+60A+4-in-1+ESC",
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
        "id": "holybro-kakute-h7-hdv-fc",
        "category": "fc",
        "name": "Kakute H7 HDV Flight Controller",
        "brand": "Holybro",
        "price_php": 4750,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Kakute+H7+HDV+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://holybro.com/products/kakute-h7-hdv"
        }
    },
    {
        "id": "gemfan-hurricane-51477-v2",
        "category": "propeller",
        "name": "Hurricane 51477 V2",
        "brand": "Gemfan",
        "price_php": 240,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51477+V2",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "black",
                "green"
            ]
        }
    },
    {
        "id": "foxeer-toothless-3-nano-camera",
        "category": "camera",
        "name": "Toothless 3 Nano FPV Camera",
        "brand": "Foxeer",
        "price_php": 1850,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Toothless+3+Nano+Camera",
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
        "id": "dji-o4-air-unit-lite-vtx",
        "category": "vtx",
        "name": "O4 Air Unit Lite",
        "brand": "DJI",
        "price_php": 9800,
        "weight_g": 19,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+O4+Air+Unit+Lite",
        "color": "#222222",
        "specs": {
            "power_mw_max": 800,
            "protocol": "DJI Digital",
            "bands": "5.8GHz/5.1GHz",
            "voltage_range": "7-26V",
            "connector": "Onboard"
        }
    },
    {
        "id": "tattu-rline-3.0-4s-1300mah",
        "category": "battery",
        "name": "R-Line 3.0 1300mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1740,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Tattu+R-Line+3.0+1300mAh+4S+130C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "radiomaster-rp4-elrs-nano-rx",
        "category": "receiver",
        "name": "RP4 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 980,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=RadioMaster+RP4+ELRS+Nano+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "speedybee-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1320,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+M10+GPS+Module",
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
        "id": "foxeer-lollipop-3-plus-antenna",
        "category": "antenna",
        "name": "Lollipop 3 Plus 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 450,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Lollipop+3+Plus+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
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
