#!/usr/bin/env python3
"""Add a tenth batch of 2 new FPV parts (frame + propeller) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "tbs-source-one-r5-frame",
        "category": "frame",
        "name": "Source One R5 Frame",
        "brand": "TBS",
        "price_php": 1550,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+r5"
        }
    },
    {
        "id": "gemfan-hurricane-51433-3",
        "category": "propeller",
        "name": "Hurricane 51433 3-Blade",
        "brand": "Gemfan",
        "price_php": 240,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.33,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray",
                "blue"
            ]
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
