#!/usr/bin/env python3
"""Add 32nd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "axisflying-cinepro-v2-5inch",
        "category": "frame",
        "name": "Cinepro V2 5\" Freestyle Frame",
        "brand": "AxisFlying",
        "price_php": 3300,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+Cinepro+V2",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "flywoo-nin-v2-2207-5-1900kv",
        "category": "motor",
        "name": "NIN V2 2207.5 1900KV",
        "brand": "Flywoo",
        "price_php": 950,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+NIN+V2+2207.5",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207.5",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 38
        }
    },
    {
        "id": "sunnysky-as-v2-50a-esc",
        "category": "esc",
        "name": "AS V2 50A 4-in-1 ESC",
        "brand": "SunnySky",
        "price_php": 1700,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SunnySky+AS+V2+50A",
        "color": "#1a0000",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "foxeer-f405-v3-aio-fc",
        "category": "fc",
        "name": "F405 V3 AIO Flight Controller",
        "brand": "Foxeer",
        "price_php": 2400,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+F405+V3+AIO",
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
            "curr_sensor": True
        }
    },
    {
        "id": "azure-power-tornado-t5046",
        "category": "propeller",
        "name": "Tornado T5046 3-Blade",
        "brand": "Azure Power",
        "price_php": 190,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Azure+Power+Tornado+T5046",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "runcam-hawk-pro-3-camera",
        "category": "camera",
        "name": "Hawk Pro 3 FPV Camera",
        "brand": "RunCam",
        "price_php": 1600,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Hawk+Pro+3",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "diatone-tina-whoop-vtx",
        "category": "vtx",
        "name": "Tina Whoop VTX",
        "brand": "Diatone",
        "price_php": 750,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Tina+Whoop+VTX",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "3.3-5V",
            "connector": "U.FL"
        }
    },
    {
        "id": "tattu-rline-5-0-4s-1300",
        "category": "battery",
        "name": "R-Line 5.0 4S 1300mAh 130C LiPo",
        "brand": "Tattu",
        "price_php": 1450,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+5.0+4S+1300mAh",
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
        "id": "happymodel-ep2-elrs-rx-v2",
        "category": "receiver",
        "name": "EP2 ELRS RX V2",
        "brand": "HappyModel",
        "price_php": 700,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ELRS+RX",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 18
        }
    },
    {
        "id": "geprc-gp-m10-gps",
        "category": "gps",
        "name": "GP-M10 GPS Module",
        "brand": "GEPRC",
        "price_php": 1050,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+GP-M10+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 24,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "akk-cp5-5-8-antenna",
        "category": "antenna",
        "name": "CP5 5.8GHz RHCP Antenna",
        "brand": "AKK",
        "price_php": 350,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+CP5+5.8GHz",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "SMA",
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
