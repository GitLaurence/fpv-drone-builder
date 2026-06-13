#!/usr/bin/env python3
"""Add a twenty-first batch of 11 new FPV parts (1 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "catalyst-superlight-norris-5inch",
        "category": "frame",
        "name": "SuperLight (Norris Edition) Frame 5\"",
        "brand": "Catalyst Machineworks",
        "price_php": 4480,
        "weight_g": 65,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalyst-machineworks-superlight-norris-edition-frame-5.html",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=catalyst+superlight+norris"
        }
    },
    {
        "id": "brotherhobby-returner-r5-2207-2700kv",
        "category": "motor",
        "name": "Returner R5 2207 Motor 2700KV",
        "brand": "BrotherHobby",
        "price_php": 1456,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/brotherhobby-returner-r5-2207-2700kv-brushless-motor.html",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2700,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 35
        }
    },
    {
        "id": "airbot-ori32-25a-4in1",
        "category": "esc",
        "name": "Ori32 BLHeli32 25A 4-in-1 ESC",
        "brand": "Airbot",
        "price_php": 2240,
        "weight_g": 7.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/airbot-ori32-blheli32-25a-4-in-1-esc.html",
        "color": "#002200",
        "specs": {
            "amp_rating": 25,
            "input_voltage_s": 4,
            "protocol": "BLHeli_32",
            "form_factor_mm": 20,
            "burst_amp": 30
        }
    },
    {
        "id": "holybro-kakute-f7-aio-v1-5",
        "category": "fc",
        "name": "Kakute F7 AIO V1.5 Flight Controller",
        "brand": "Holybro",
        "price_php": 3640,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/holybro-kakute-f7-aio-flight-controller.html",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 36,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "iflight-nazgul-r5-5x3.6x3",
        "category": "propeller",
        "name": "Nazgul R5 5.1\" 5x3.6x3 3-Blade Racing Propeller",
        "brand": "iFlight",
        "price_php": 672,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/iflight-nazgul-r5-5-1-5x3-6x3-3-blade-racing-propeller-set-of-4.html",
        "color": "#888888",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["cyan", "gray"]
        }
    },
    {
        "id": "caddx-gazer-analog",
        "category": "camera",
        "name": "Gazer Analog FPV Camera",
        "brand": "Caddx",
        "price_php": 4480,
        "weight_g": 20,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/caddx-gazer-analog-fpv-camera.html",
        "color": "#111111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "9-24V"
        }
    },
    {
        "id": "hglrc-forward-mt-vtx",
        "category": "vtx",
        "name": "Forward MT 25/100/200/400/800mW 5.8GHz VTX",
        "brand": "HGLRC",
        "price_php": 1680,
        "weight_g": 6.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/hglrc-forward-mt-25-100-200-400-800mw-5-8ghz-vtx-mmcx.html",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "lumenier-n2o-featherlite-1300mah-6s",
        "category": "battery",
        "name": "N2O Feather-Lite 1300mAh 6S 150C",
        "brand": "Lumenier",
        "price_php": 3920,
        "weight_g": 180,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/lumenier-n2o-feather-lite-1300mah-6s-150c-lipo-battery-xt-60.html",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "radiomaster-xr1-nano-elrs",
        "category": "receiver",
        "name": "XR1 Nano Multi-Frequency ELRS 2.4GHz Receiver",
        "brand": "RadioMaster",
        "price_php": 1232,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/radiomaster-xr1-nano-multi-frequency-receiver-elrs-2-4ghz.html",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "iflight-blitz-m10-gps",
        "category": "gps",
        "name": "BLITZ M10 GPS",
        "brand": "iFlight",
        "price_php": 1400,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/iflight-blitz-m10-gps.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+SBAS+Galileo+QZSS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 27,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "truerc-core-5-8-sma",
        "category": "antenna",
        "name": "CORE 5.8GHz Antenna - SMA",
        "brand": "TrueRC",
        "price_php": 952,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/truerc-core-5-8ghz-antenna-sma.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.9,
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
