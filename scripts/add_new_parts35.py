#!/usr/bin/env python3
"""Add 35th batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-explorer-lr4-pro-frame",
        "category": "frame",
        "name": "Explorer LR4 Pro Frame",
        "brand": "Flywoo",
        "price_php": 3600,
        "weight_g": 112,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Explorer+LR4+Pro",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4+pro"
        }
    },
    {
        "id": "tmotor-velox-v2207-v2-1950kv",
        "category": "motor",
        "name": "Velox V2207 V2 1950KV",
        "brand": "T-Motor",
        "price_php": 1700,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Velox+V2207+V2+1950KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "flycolor-x-cross-50a-4in1",
        "category": "esc",
        "name": "X-Cross 50A 4-in-1 ESC",
        "brand": "Flycolor",
        "price_php": 1800,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+X-Cross+50A+4-in-1",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "hakrc-f745-aio",
        "category": "fc",
        "name": "F745 AIO Flight Controller",
        "brand": "HAKRC",
        "price_php": 1900,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HAKRC+F745+AIO",
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
        "id": "hqprop-dt-51463-prop",
        "category": "propeller",
        "name": "DT 5.1X4.6X3 Durable Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 180,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DT+5.1X4.6X3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "white"]
        }
    },
    {
        "id": "caddx-ratel-pro-camera",
        "category": "camera",
        "name": "Ratel Pro",
        "brand": "Caddx",
        "price_php": 1600,
        "weight_g": 6.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ratel+Pro",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "tbs-unify-pro42",
        "category": "vtx",
        "name": "Unify Pro42",
        "brand": "TBS",
        "price_php": 2800,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro42",
        "color": "#222222",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-black-series-1500mah-6s",
        "category": "battery",
        "name": "Black Series 1500mAh 6S",
        "brand": "CNHL",
        "price_php": 1500,
        "weight_g": 235,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1500mAh+6S",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "betafpv-elrs-lite-nano-rx",
        "category": "receiver",
        "name": "ELRS Lite Nano Receiver",
        "brand": "BetaFPV",
        "price_php": 750,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+ELRS+Lite+Nano",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "beitian-bn-880t-gps",
        "category": "gps",
        "name": "BN-880T GPS+Compass",
        "brand": "Beitian",
        "price_php": 1000,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880T",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "tbs-triumph-antenna",
        "category": "antenna",
        "name": "Triumph Antenna",
        "brand": "TBS",
        "price_php": 1400,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Triumph+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
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
