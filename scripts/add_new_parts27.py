"""Add 27th batch of new FPV parts - real, verified products across categories."""
import json

NEW_PARTS = [
    {
        "id": "betafpv-pavo-pico-hd-ready",
        "category": "frame",
        "name": "Pavo Pico Cinewhoop - HD Ready",
        "brand": "BetaFPV",
        "price_php": 3955,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/betafpv-pavo-pico-cinewhoop-hd-ready.html",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 81,
            "motor_mount_mm": 9,
            "prop_clearance_inch": 2,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 1.5,
            "standoff_height_mm": 15,
            "thingiverse_url": "https://www.thingiverse.com/search?q=betafpv+pavo+pico"
        }
    },
    {
        "id": "gemfan-d63-ducted-5-blade",
        "category": "propeller",
        "name": "D63 Ducted 5-Blade 63mm CineWhoop Propeller",
        "brand": "Gemfan",
        "price_php": 410,
        "weight_g": 1.76,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/gemfan-d63-ducted-5-blade-63mm-cinewhoop-propeller-set-of-8.html",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 2.5,
            "pitch": 3,
            "blade_count": 5,
            "shaft_mm": 1.5,
            "color_options": [
                "black",
                "yellow",
                "clear gray"
            ]
        }
    },
    {
        "id": "walksnail-avatar-hd-mini-1s-lite-kit",
        "category": "vtx",
        "name": "Avatar HD Mini 1S Lite Kit",
        "brand": "Walksnail",
        "price_php": 4465,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.caddxfpv.com/products/walksnail-avatar-hd-mini-1s-lite-kit",
        "color": "#111",
        "specs": {
            "power_mw_max": 200,
            "protocol": "Digital",
            "bands": "5.1-5.85GHz",
            "voltage_range": "3.5-9V",
            "connector": "IPEX"
        }
    },
    {
        "id": "speedybee-f405-aio-40a-bluejay",
        "category": "esc",
        "name": "F405 AIO 40A Bluejay 25.5x25.5",
        "brand": "SpeedyBee",
        "price_php": 3163,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/speedybee-f405-aio-40a-bluejay-25-5x25-5-3-6s-flight-controller/",
        "color": "#002200",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 25.5,
            "burst_amp": 55
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
