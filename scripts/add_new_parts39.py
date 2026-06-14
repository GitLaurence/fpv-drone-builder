#!/usr/bin/env python3
"""Add 39th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-cidora-sl5-v2-5-frame",
        "category": "frame",
        "name": "Cidora SL5 V2.5 Frame",
        "brand": "iFlight",
        "price_php": 3190,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Cidora+SL5+V2.5+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+cidora+sl5"
        }
    },
    {
        "id": "tmotor-f60-pro-v-1750kv",
        "category": "motor",
        "name": "F60 PRO V 2207 1750KV",
        "brand": "T-Motor",
        "price_php": 1680,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F60+PRO+V+2207+1750KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "flycolor-x-cross-60a-4in1-esc",
        "category": "esc",
        "name": "X-Cross 60A 4-in-1 ESC",
        "brand": "Flycolor",
        "price_php": 2665,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+X-Cross+60A+4-in-1+ESC",
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
        "id": "mamba-f405-mk4-fc",
        "category": "fc",
        "name": "F405 MK4 Flight Controller",
        "brand": "Mamba",
        "price_php": 1915,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Mamba+F405+MK4+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-ethix-s6-5x4.3x3-propeller",
        "category": "propeller",
        "name": "Ethix S6 5×4.3×3",
        "brand": "HQProp",
        "price_php": 205,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S6+5x4.3x3",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "white",
                "grey"
            ]
        }
    },
    {
        "id": "foxeer-falkor-3-micro-camera",
        "category": "camera",
        "name": "Falkor 3 Micro Camera",
        "brand": "Foxeer",
        "price_php": 1680,
        "weight_g": 7.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Falkor+3+Micro+Camera",
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
        "id": "tbs-unify-pro32-nano-hv-vtx",
        "category": "vtx",
        "name": "Unify Pro32 Nano HV VTX",
        "brand": "TBS",
        "price_php": 2320,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro32+Nano+HV+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Raceband",
            "voltage_range": "7-36V",
            "connector": "U.FL"
        }
    },
    {
        "id": "tattu-rline-v5-1300mah-6s",
        "category": "battery",
        "name": "R-Line V5.0 1300mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2320,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5.0+1300mAh+6S+130C",
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
        "id": "happymodel-ep1-elrs-nano-rx",
        "category": "receiver",
        "name": "EP1 ELRS Nano Receiver",
        "brand": "Happymodel",
        "price_php": 755,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+EP1+ELRS+Nano+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "beitian-bn-880-gps",
        "category": "gps",
        "name": "BN-880 GPS+Compass",
        "brand": "Beitian",
        "price_php": 1335,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880+GPS",
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
        "id": "iflight-succex-e-f4-v2-5-fc",
        "category": "fc",
        "name": "SucceX-E F4 V2.5 Flight Controller",
        "brand": "iFlight",
        "price_php": 1450,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+SucceX-E+F4+V2.5+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": False,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "radiomaster-rp3-elrs-diversity-rx",
        "category": "receiver",
        "name": "RP3 ELRS Diversity Receiver",
        "brand": "RadioMaster",
        "price_php": 1450,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RadioMaster+RP3+ELRS+Diversity+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "speedybee-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1160,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+M10+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "akk-lollipop-3-5.8ghz-antenna",
        "category": "antenna",
        "name": "Lollipop 3 5.8GHz Antenna",
        "brand": "AKK",
        "price_php": 520,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+Lollipop+3+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "U.FL",
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
