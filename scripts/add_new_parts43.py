#!/usr/bin/env python3
"""Add 43rd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-chimera7-pro-v2-lr-frame",
        "category": "frame",
        "name": "Chimera7 Pro V2 LR Frame",
        "brand": "iFlight",
        "price_php": 5200,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Chimera7+Pro+V2",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 305,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+chimera7+pro"
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-v3",
        "category": "motor",
        "name": "Avenger 2306.5 V3",
        "brand": "BrotherHobby",
        "price_php": 1450,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2306.5+V3",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2306.5",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "tmotor-f55a-pro-iv-4in1-esc",
        "category": "esc",
        "name": "F55A PRO IV 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 3800,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F55A+PRO+IV+4-in-1+ESC",
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
        "id": "mamba-f722-mini-apex-fc",
        "category": "fc",
        "name": "F722 Mini Apex Flight Controller",
        "brand": "Mamba",
        "price_php": 3200,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Mamba+F722+Mini+Apex+Flight+Controller",
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
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/products/mamba-f722-mini-apex-flight-controller"
        }
    },
    {
        "id": "hqprop-ethix-s5-v2",
        "category": "propeller",
        "name": "Ethix S5 V2",
        "brand": "HQProp",
        "price_php": 220,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S5+V2",
        "color": "#cccccc",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "white",
                "purple"
            ]
        }
    },
    {
        "id": "caddx-ratel2-pro-camera",
        "category": "camera",
        "name": "Ratel 2 Pro FPV Camera",
        "brand": "Caddx",
        "price_php": 2100,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ratel+2+Pro+Camera",
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
        "id": "rush-tank-solo-rx5-vtx",
        "category": "vtx",
        "name": "Tank Solo RX5 VTX",
        "brand": "Rush",
        "price_php": 2400,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rush+Tank+Solo+RX5+VTX",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "SmartAudio",
            "video_system": "Analog",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "gaoneng-gnb-1300mah-6s-100c-hv",
        "category": "battery",
        "name": "GNB 1300mAh 6S 100C HV LiPo",
        "brand": "Gaoneng",
        "price_php": 2200,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Gaoneng+GNB+1300mAh+6S+100C+HV",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-elrs-pp10-nano-rx",
        "category": "receiver",
        "name": "ELRS PP10 Nano Receiver",
        "brand": "Happymodel",
        "price_php": 850,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Happymodel+ELRS+PP10+Nano+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "beitian-bn-220-gps-module",
        "category": "gps",
        "name": "BN-220 GPS Module",
        "brand": "Beitian",
        "price_php": 950,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-220+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8030",
            "update_rate_hz": 10,
            "fix_time_s": 27,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "immersionrc-skyhawk-mini-antenna",
        "category": "antenna",
        "name": "SkyHawk Mini 5.8GHz Antenna",
        "brand": "ImmersionRC",
        "price_php": 550,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SkyHawk+Mini+Antenna",
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
