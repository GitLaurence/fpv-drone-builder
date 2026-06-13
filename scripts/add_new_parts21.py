#!/usr/bin/env python3
"""Add a twenty-first batch of 11 new FPV parts (1 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "armattan-chameleon-ti-5-frame",
        "category": "frame",
        "name": "Chameleon Ti 5\" Frame",
        "brand": "Armattan",
        "price_php": 9000,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/armattan-chameleon-ti-5-frame.html",
        "color": "#2b2b2b",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "titanium/carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "flywoo-nin-2207",
        "category": "motor",
        "name": "NIN 2207 Motor 1800KV",
        "brand": "Flywoo",
        "price_php": 2430,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/flywoo-nin-2207-motor.html",
        "color": "#303030",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 35
        }
    },
    {
        "id": "iflight-blitz-e55-4in1-esc",
        "category": "esc",
        "name": "Blitz E55 55A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 4500,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/iflight-blitz-e55-55a-4-in-1-esc.html",
        "color": "#003300",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "BLHeli_32",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "mamba-f405-mk4",
        "category": "fc",
        "name": "Mamba F405 MK4 Flight Controller",
        "brand": "Diatone",
        "price_php": 3150,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/diatone-mamba-f405-mk4-flight-controller.html",
        "color": "#000044",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-hurricane-51499-3blade",
        "category": "propeller",
        "name": "Hurricane 51499 3-Blade Propeller Set of 4",
        "brand": "Gemfan",
        "price_php": 315,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/gemfan-hurricane-51499-3-blade-propeller-set-of-4.html",
        "color": "#2222aa",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.99,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "white"]
        }
    },
    {
        "id": "caddx-ant-lite-camera",
        "category": "camera",
        "name": "Ant Lite FPV Camera",
        "brand": "Caddx",
        "price_php": 1440,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/caddx-ant-lite-fpv-camera.html",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 150,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-25V"
        }
    },
    {
        "id": "rush-tank-nano-vtx",
        "category": "vtx",
        "name": "Tank Nano VTX",
        "brand": "Rush",
        "price_php": 2970,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/rush-tank-nano-vtx.html",
        "color": "#440000",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-20V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-1500mah-4s",
        "category": "battery",
        "name": "Black Series 1500mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1260,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/cnhl-black-series-100c-4s-lipo-battery-1500mah.html",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "happymodel-ep1-receiver",
        "category": "receiver",
        "name": "EP1 ELRS 2.4GHz Receiver",
        "brand": "Happymodel",
        "price_php": 900,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/happymodel-ep1-2-4ghz-elrs-receiver.html",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "ublox-neo-m8n-gps-module",
        "category": "gps",
        "name": "NEO-M8N GPS Module w/ Compass",
        "brand": "u-blox",
        "price_php": 1800,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/ublox-neo-m8n-gps-module-w-compass.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 35,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "lumenier-axii-2-antenna-rhcp",
        "category": "antenna",
        "name": "AXII 2 RHCP FPV Antenna",
        "brand": "Lumenier",
        "price_php": 1170,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/lumenier-axii-2-fpv-antenna-rhcp.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
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
