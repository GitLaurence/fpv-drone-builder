#!/usr/bin/env python3
"""Add a nineteenth batch of 11 new FPV parts (1 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-firefly16-nano-baby-v3-1s",
        "category": "frame",
        "name": "Firefly16 Nano Baby V3 1S Frame Kit",
        "brand": "Flywoo",
        "price_php": 951,
        "weight_g": 7.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/flywoo-firefly16-nano-baby-v3-1s-frame-kit-analog-walksnail-hdzero.html",
        "color": "#0f0f0f",
        "specs": {
            "size_mm": 66,
            "motor_mount_mm": 9,
            "prop_clearance_inch": 1.6,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 1.5,
            "standoff_height_mm": 12,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+firefly16+nano+baby"
        }
    },
    {
        "id": "tmotor-velox-v2306-v3-1750kv",
        "category": "motor",
        "name": "VELOX V2306 V3 1750KV",
        "brand": "T-Motor",
        "price_php": 1679,
        "weight_g": 33.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/t-motor-velox-v2306-v3-motor-1500kv-1750kv-1950kv-2550kv.html",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },
    {
        "id": "holybro-tekko32-f4-45a-mini",
        "category": "esc",
        "name": "Tekko32 F4 45A Mini 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3079,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/holybro-tekko32-mini-f4-45a-blheli32-2-6s-4-in-1-esc.html",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "AM32",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "iflight-beast-f7-v1-2-45a-aio",
        "category": "fc",
        "name": "Beast F7 V1.2 45A AIO",
        "brand": "iFlight",
        "price_php": 3359,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/iflight-beast-f7-45a-aio-25-5x25-5mm-flight-controller.html",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 25.5,
            "stack_mount_mm": 25.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-freestyle-4s-5136",
        "category": "propeller",
        "name": "Freestyle 4S 5.1x3.6x3",
        "brand": "Gemfan",
        "price_php": 223,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/gemfan-freestyle-4s-5-1x3-6x3-3-blade-propeller-set-of-4.html",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "green", "pink"]
        }
    },
    {
        "id": "caddx-ratel-2-starlight",
        "category": "camera",
        "name": "Ratel 2 Micro Starlight 1200TVL",
        "brand": "Caddx",
        "price_php": 1735,
        "weight_g": 5.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/caddx-ratel-2-micro-starlight-1200tvl-low-latency-fpv-camera.html",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" Starlight CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-mini-vtx-v3",
        "category": "vtx",
        "name": "Avatar HD Mini VTX V3",
        "brand": "Walksnail",
        "price_php": 3920,
        "weight_g": 6.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/walksnail-avatar-hd-mini-vtx-v3.html",
        "color": "#221100",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Digital",
            "bands": "Walksnail",
            "voltage_range": "3.1-13V",
            "connector": "MMCX",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "cnhl-black-series-6s-1300mah-130c",
        "category": "battery",
        "name": "Black Series V2.0 1300mAh 6S 130C",
        "brand": "CNHL",
        "price_php": 1511,
        "weight_g": 223,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/cnhl-black-series-v2-0-1300mah-22-2v-130c-6s-lipo-battery-xt60.html",
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
        "id": "betafpv-superd-elrs-2-4ghz-diversity",
        "category": "receiver",
        "name": "SuperD ELRS 2.4GHz Diversity Receiver",
        "brand": "BetaFPV",
        "price_php": 1399,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/betafpv-superd-elrs-2-4ghz-diversity-receiver.html",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "iflight-m8q-5883-v2",
        "category": "gps",
        "name": "M8Q-5883 V2.0 GPS Module w/ Compass",
        "brand": "iFlight",
        "price_php": 2239,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/iflight-m8q-5883-v2-0-gps-module-w-compass.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "truerc-singularity-5-8-rhcp",
        "category": "antenna",
        "name": "Singularity 5.8 SMA90 (RHCP)",
        "brand": "TrueRC",
        "price_php": 1119,
        "weight_g": 6.45,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/truerc-singularity-5-8-sma90-antenna-rhcp.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.9,
            "polarization": "RHCP",
            "connector": "SMA90",
            "type": "omni"
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
