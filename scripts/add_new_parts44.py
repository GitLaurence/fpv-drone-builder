#!/usr/bin/env python3
"""Add 44th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-mark5-hd-o4-frame",
        "category": "frame",
        "name": "Mark5 HD O4 5\" Frame",
        "brand": "GEPRC",
        "price_php": 2150,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Mark5+HD+O4+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5+hd+o4"
        }
    },
    {
        "id": "tmotor-velox-v2306-v3-1900kv",
        "category": "motor",
        "name": "Velox V2306 V3 1900KV",
        "brand": "T-Motor",
        "price_php": 1620,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Velox+V2306+V3+1900KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "iflight-succex-e-mini-50a-esc",
        "category": "esc",
        "name": "SucceX-E Mini 50A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 1980,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+SucceX-E+Mini+50A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 60
        }
    },
    {
        "id": "diatone-mamba-h743-mk4-fc",
        "category": "fc",
        "name": "Mamba H743 MK4 Flight Controller",
        "brand": "Diatone",
        "price_php": 4250,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+H743+MK4+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/products/mamba-h743-mk4-flight-controller"
        }
    },
    {
        "id": "dalprop-cyclone-t5249c-propeller",
        "category": "propeller",
        "name": "Cyclone T5249C 5\" Tri-Blade Propeller",
        "brand": "DALProp",
        "price_php": 245,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DALProp+Cyclone+T5249C+Propeller",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.9,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "grey",
                "black",
                "green"
            ]
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-pro-camera",
        "category": "camera",
        "name": "Avatar HD V3 Pro Camera",
        "brand": "Walksnail",
        "price_php": 5480,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+HD+V3+Pro+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 155,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "6.6-25V"
        }
    },
    {
        "id": "iflight-immortalt-vtx",
        "category": "vtx",
        "name": "ImmortalT 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 2380,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+ImmortalT+5.8GHz+VTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "5.8GHz 40CH",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-rline-5-0-1400mah-6s150c-v2",
        "category": "battery",
        "name": "R-Line 5.0 1400mAh 6S 150C LiPo V2",
        "brand": "Tattu",
        "price_php": 2980,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Tattu+R-Line+5.0+1400mAh+6S+150C+V2",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-elrs-lite-nano-rx",
        "category": "receiver",
        "name": "ELRS Lite Nano Receiver V2",
        "brand": "Happymodel",
        "price_php": 780,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+ELRS+Lite+Nano+Receiver+V2",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 18
        }
    },
    {
        "id": "betafpv-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module Lite",
        "brand": "BetaFPV",
        "price_php": 1420,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+M10+GPS+Module",
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
        "id": "axisflying-stubby-antenna",
        "category": "antenna",
        "name": "Stubby 5.8GHz RHCP Antenna",
        "brand": "AxisFlying",
        "price_php": 480,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+Stubby+5.8GHz+RHCP+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.5,
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
