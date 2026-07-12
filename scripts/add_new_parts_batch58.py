#!/usr/bin/env python3
"""Batch 58: real, current-production FPV parts, verified against live retailer
listings (name, spec and price cross-checked via web search) before adding.
The catalog is already near-exhaustive of real-market FPV components, so this
batch is intentionally small and limited to items confirmed genuinely absent
and genuinely real, rather than padding with more speculative variants."""
import json

NEW_PARTS = [
    # ========== MOTOR ==========
    {
        "id": "brotherhobby-vs-2207-2400kv-motor",
        "category": "motor",
        "name": "VS 2207 2400KV",
        "brand": "BrotherHobby",
        "price_php": 1188,
        "weight_g": 30.5,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=BrotherHobby+VS+2207+2400KV",
        "color": "#141414",
        "specs": {
            "kv": 2400,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },
    {
        "id": "brotherhobby-avenger-3120-500kv-motor",
        "category": "motor",
        "name": "Avenger 3120 500KV",
        "brand": "BrotherHobby",
        "price_php": 4001,
        "weight_g": 142.7,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=BrotherHobby+Avenger+3120+500KV",
        "color": "#141414",
        "specs": {
            "kv": 500,
            "stator_size": "3120",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 6,
            "max_voltage_s": 12,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    # ========== ESC ==========
    {
        "id": "tmotor-f55a-pro-ii-4in1-esc",
        "category": "esc",
        "name": "F55A Pro II 55A 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 4982,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F55A+Pro+II+55A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30.5,
            "burst_amp": 65
        }
    },
    # ========== FC ==========
    {
        "id": "hakrc-f411-20a-aio-fc",
        "category": "fc",
        "name": "F411 20A AIO Flight Controller",
        "brand": "HAKRC",
        "price_php": 3653,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HAKRC+F411+20A+AIO+Flight+Controller",
        "color": "#0f0f0f",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 26,
            "stack_mount_mm": 26,
            "barometer": True,
            "blackbox": False,
            "uart_count": 3,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    # ========== RECEIVER ==========
    {
        "id": "flysky-fs-ia6-receiver",
        "category": "receiver",
        "name": "FS-iA6 6CH Receiver",
        "brand": "FlySky",
        "price_php": 753,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FlySky+FS-iA6+Receiver+6CH",
        "color": "#e8e8e8",
        "specs": {
            "protocol": "AFHDS 2A",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": False
        }
    },
    # ========== BATTERY ==========
    {
        "id": "cnhl-black-series-3s-1300mah-100c-battery",
        "category": "battery",
        "name": "Black Series 3S 1300mAh 100C",
        "brand": "CNHL",
        "price_php": 927,
        "weight_g": 128,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+3S+1300mAh+100C",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 11.1
        }
    },
    # ========== FRAME ==========
    {
        "id": "iflight-xl10-v6-frame",
        "category": "frame",
        "name": "XL10 V6 10-inch Frame",
        "brand": "iFlight",
        "price_php": 6727,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+XL10+V6+10+inch+Frame",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 420,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 10,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
]


def main():
    with open("data/parts.json", "r") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    added = 0
    skipped = 0

    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"  SKIP (duplicate): {part['id']}")
            skipped += 1
        else:
            data["parts"].append(part)
            existing_ids.add(part["id"])
            added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = len(data["parts"])
    print(f"\nAdded {added} new parts (skipped {skipped} duplicates)")
    print(f"Total parts now: {total}")

    from collections import Counter
    cats = Counter(p["category"] for p in data["parts"])
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
