#!/usr/bin/env python3
"""Add 43rd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "diatone-roma-f5-frame",
        "category": "frame",
        "name": "Roma F5 Freestyle Frame",
        "brand": "Diatone",
        "price_php": 3050,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Roma+F5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=diatone+roma+f5"
        }
    },
    {
        "id": "t-motor-velox-v2-2807",
        "category": "motor",
        "name": "Velox V2 2807",
        "brand": "T-Motor",
        "price_php": 1980,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Velox+V2+2807",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 55
        }
    },
    {
        "id": "t-motor-f55a-pro-ii-4in1-esc",
        "category": "esc",
        "name": "F55A Pro II 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 3850,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F55A+Pro+II+4-in-1+ESC",
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
        "id": "mamba-f722-mk5-fc",
        "category": "fc",
        "name": "F722 MK5 Flight Controller",
        "brand": "Mamba",
        "price_php": 3200,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Mamba+F722+MK5+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/products/mamba-f722-mk5-flight-controller"
        }
    },
    {
        "id": "hqprop-ethix-s5-propeller",
        "category": "propeller",
        "name": "Ethix S5 Propeller",
        "brand": "HQProp",
        "price_php": 260,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S5",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "grey",
                "black"
            ]
        }
    },
    {
        "id": "caddx-ratel-2-pro-camera",
        "category": "camera",
        "name": "Ratel 2 Pro FPV Camera",
        "brand": "Caddx",
        "price_php": 1950,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ratel+2+Pro",
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
        "id": "rush-tank-ultimate-vtx",
        "category": "vtx",
        "name": "Tank Ultimate VTX",
        "brand": "Rush",
        "price_php": 2950,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rush+Tank+Ultimate+VTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "5.8GHz 40CH",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-1800mah-6s",
        "category": "battery",
        "name": "Black Series 1800mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2450,
        "weight_g": 268,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=CNHL+Black+Series+1800mAh+6S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1800,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "foxeer-reaper-elrs-rx",
        "category": "receiver",
        "name": "Reaper ELRS Receiver",
        "brand": "Foxeer",
        "price_php": 1050,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Foxeer+Reaper+ELRS+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "beitian-bn-220-v2-gps",
        "category": "gps",
        "name": "BN-220 GPS Module",
        "brand": "Beitian",
        "price_php": 850,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-220+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 27,
            "compass": False,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "truerc-x-air-antenna",
        "category": "antenna",
        "name": "X-Air 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 620,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+X-Air+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.9,
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
