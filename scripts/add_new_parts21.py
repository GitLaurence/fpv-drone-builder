#!/usr/bin/env python3
"""Add a twenty-first batch of 11 new FPV parts (1 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "pirat-hook-v2-5inch",
        "category": "frame",
        "name": "Hook V2 5\" Frame Kit",
        "brand": "PIRAT",
        "price_php": 3629,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/pirat-hook-v2-fpv-drone-frame-kit.html",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=pirat+hook"
        }
    },
    {
        "id": "brotherhobby-returner-r3-2207-2400kv",
        "category": "motor",
        "name": "Returner R3 2207 Motor 2400KV",
        "brand": "BrotherHobby",
        "price_php": 1056,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/brotherhobby-returner-r3-2207-2400kv-brushless-motor.html",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2400,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "xilo-stax-45a-4in1",
        "category": "esc",
        "name": "Stax 45A BLHeli_32 3-6S 4-in-1 ESC",
        "brand": "XILO",
        "price_php": 2177,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/xilo-stax-45a-blheli-32-3-6s-4-in-1-esc.html",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "BLHeli_32",
            "form_factor_mm": 30,
            "burst_amp": 50
        }
    },
    {
        "id": "lumenier-lux-f7-ultimate",
        "category": "fc",
        "name": "LUX F7 Ultimate Flight Controller (Dual Gyros)",
        "brand": "Lumenier",
        "price_php": 3629,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/lumenier-lux-f7-ultimate-flight-controller-dual-gyros.html",
        "color": "#000055",
        "specs": {
            "gyro": "Dual ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-freestyle-5x4.3x3-v2s",
        "category": "propeller",
        "name": "Freestyle 5x4.3x3 V2S Tri-Blade",
        "brand": "HQProp",
        "price_php": 231,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/hqprop-freestyle-5x4-3x3-v2s-tri-blade-propeller-set-of-4.html",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "foxeer-micro-cat-3-1200tvl",
        "category": "camera",
        "name": "Micro Cat 3 1200TVL Super Low Light Camera",
        "brand": "Foxeer",
        "price_php": 1649,
        "weight_g": 5.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/foxeer-micro-cat-3-1200tvl-super-low-light-fpv-night-camera.html",
        "color": "#111111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "fxt-ares-5-8ghz-vtx",
        "category": "vtx",
        "name": "ARES 5.8GHz VTX (PIT/25/200/600mW/1W)",
        "brand": "FXT",
        "price_php": 1847,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/fxt-ares-5-8ghz-pit-25mw-200mw-600mw-1w-vtx-w-smart-audio.html",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-v2-4s-1300mah-130c",
        "category": "battery",
        "name": "Black Series V2.0 1300mAh 4S 130C",
        "brand": "CNHL",
        "price_php": 1517,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/cnhl-black-series-130c-4s-lipo-battery-1300mah.html",
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
        "id": "betafpv-elrs-2-4ghz-nano-rx",
        "category": "receiver",
        "name": "ELRS 2.4GHz Nano Receiver",
        "brand": "BETAFPV",
        "price_php": 1056,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/betafpv-elrs-2-4ghz-nano-receiver.html",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "geprc-m10-dq-gps",
        "category": "gps",
        "name": "M10 DQ GPS Module",
        "brand": "GEPRC",
        "price_php": 1517,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/geprc-m10-dq-gps-module.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 29,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "orqa-fpv-p1-5-8ghz-antenna",
        "category": "antenna",
        "name": "FPV.P1 5.8GHz Patch Antenna (RHCP)",
        "brand": "ORQA",
        "price_php": 924,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/orqa-fpv-p1-5-8ghz-patch-antenna-rhcp.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 8.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "patch"
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
