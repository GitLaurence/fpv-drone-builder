#!/usr/bin/env python3
"""Add 43rd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-avant-5-frame",
        "category": "frame",
        "name": "Avant 5\" Freestyle Frame",
        "brand": "GEPRC",
        "price_php": 3629,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Avant+5+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5.1,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+avant+5"
        }
    },
    {
        "id": "hakrc-flashhobby-2306-1900kv",
        "category": "motor",
        "name": "FlashHobby 2306 1900KV",
        "brand": "HAKRC",
        "price_php": 1055,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HAKRC+FlashHobby+2306+1900KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 43
        }
    },
    {
        "id": "hakrc-f4-60a-4in1-esc",
        "category": "esc",
        "name": "F4 60A 4-in-1 ESC",
        "brand": "HAKRC",
        "price_php": 2177,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HAKRC+F4+60A+4-in-1+ESC",
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
        "id": "diatone-mamba-f411-mini-fc",
        "category": "fc",
        "name": "Mamba F411 Mini Flight Controller",
        "brand": "Diatone",
        "price_php": 1649,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F411+Mini+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 1,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/products/mamba-f411-mini-mk2-flight-controller"
        }
    },
    {
        "id": "hqprop-dt5.1x4.6x3",
        "category": "propeller",
        "name": "DT5.1X4.6X3 Durable Tri-Blade",
        "brand": "HQProp",
        "price_php": 230,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DT5.1X4.6X3",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey"
            ]
        }
    },
    {
        "id": "foxeer-cat-3-nano-camera",
        "category": "camera",
        "name": "Cat 3 Nano FPV Camera",
        "brand": "Foxeer",
        "price_php": 1319,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Cat+3+Nano+FPV+Camera",
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
        "id": "iflight-ts832-vtx",
        "category": "vtx",
        "name": "TS832 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 1253,
        "weight_g": 5.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+TS832+5.8GHz+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "authenticrc-pulse-1300mah-4s",
        "category": "battery",
        "name": "Pulse 1300mAh 4S 100C",
        "brand": "AuthenticRC",
        "price_php": 1517,
        "weight_g": 170,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=AuthenticRC+Pulse+1300mAh+4S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "frsky-r-xsr-receiver",
        "category": "receiver",
        "name": "R-XSR 2.4GHz Receiver",
        "brand": "FrSky",
        "price_php": 923,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R-XSR+2.4GHz+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "FrSky D16",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 1.5
        }
    },
    {
        "id": "speedybee-gps-m10-pro-v2",
        "category": "gps",
        "name": "GPS M10 Pro V2",
        "brand": "SpeedyBee",
        "price_php": 1320,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+GPS+M10+Pro+V2",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 22,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "aomway-5.8ghz-cp-antenna",
        "category": "antenna",
        "name": "5.8GHz Circular Polarized Antenna",
        "brand": "Aomway",
        "price_php": 330,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Aomway+5.8GHz+Circular+Polarized+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
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
