#!/usr/bin/env python3
"""Add 37th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-explorer-lr5-v3",
        "category": "frame",
        "name": "Explorer LR5 V3 5\" Long Range Frame",
        "brand": "Flywoo",
        "price_php": 3450,
        "weight_g": 120,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Explorer+LR5+V3",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 235,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr5"
        }
    },
    {
        "id": "t-motor-velox-v2807",
        "category": "motor",
        "name": "VELOX V2807 1300KV",
        "brand": "T-Motor",
        "price_php": 1650,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+VELOX+V2807",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "speedybee-bls60a-60a-4in1",
        "category": "esc",
        "name": "BLS 60A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2750,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+BLS+60A+4-in-1",
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
        "id": "hglrc-zeus-f722-mini-v2-fc",
        "category": "fc",
        "name": "Zeus F722 Mini V2 Flight Controller",
        "brand": "HGLRC",
        "price_php": 3300,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Zeus+F722+Mini+V2",
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
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-5x4.3x3-voyager",
        "category": "propeller",
        "name": "Voyager 5x4.3x3 Propeller",
        "brand": "HQProp",
        "price_php": 210,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Voyager+5x4.3x3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "runcam-phoenix-2-vision-camera",
        "category": "camera",
        "name": "Phoenix 2 Vision FPV Camera",
        "brand": "RunCam",
        "price_php": 1650,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Phoenix+2+Vision",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "tbs-unify-pro-evo-hv-vtx",
        "category": "vtx",
        "name": "Unify Pro Evo HV VTX",
        "brand": "TBS",
        "price_php": 3400,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro+Evo+HV",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "7-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "tattu-r-line-1300mah-6s",
        "category": "battery",
        "name": "R-Line 1300mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2150,
        "weight_g": 222,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+1300mAh+6S+130C",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "frsky-r-xsr-rx",
        "category": "receiver",
        "name": "R-XSR Micro Receiver",
        "brand": "FrSky",
        "price_php": 950,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R-XSR+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCST D16",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 2
        }
    },
    {
        "id": "flywoo-goku-gn-m10-gps",
        "category": "gps",
        "name": "Goku GN M10 GPS+Compass",
        "brand": "Flywoo",
        "price_php": 1300,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Goku+GN+M10+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "tbs-axii-2-5.8ghz-antenna",
        "category": "antenna",
        "name": "AXII 2 5.8GHz Antenna",
        "brand": "TBS",
        "price_php": 980,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+AXII+2+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
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
