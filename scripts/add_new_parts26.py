"""Add 26th batch of new FPV parts - real, verified products across categories."""
import json

NEW_PARTS = [
    {
        "id": "skystars-star-load-228",
        "category": "frame",
        "name": "Star-Load 228 5\" Frame Kit",
        "brand": "Skystars",
        "price_php": 2870,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://usa.banggood.com/Skystars-Star-load-228-Part-228mm-6mm-Arn-Carbon-Fiber-Frame-Kit-for-RC-Drone-FPV-Racing-p-1393744.html",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 228,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=skystars+star-load+228"
        }
    },
    {
        "id": "sunnysky-r2207-2450kv",
        "category": "motor",
        "name": "R2207 2450KV Racing",
        "brand": "SunnySky",
        "price_php": 980,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SunnySky+R2207+2450KV",
        "color": "#b8860b",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "siyi-hm30-digital-vtx",
        "category": "vtx",
        "name": "HM30 Digital HD Air Unit",
        "brand": "SIYI",
        "price_php": 20670,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://shop.siyi.biz/products/siyi-hm30-digital-image-transmission",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 320,
            "protocol": "Digital",
            "bands": "5.1-5.825GHz",
            "voltage_range": "7-25.2V",
            "connector": "SMA"
        }
    },
    {
        "id": "insta360-go3s",
        "category": "camera",
        "name": "GO 3S Action Camera",
        "brand": "Insta360",
        "price_php": 14650,
        "weight_g": 39,
        "in_stock": True,
        "buy_url": "https://www.insta360.com/product/insta360-go3s",
        "color": "#2a2a2a",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 142,
            "format": "Digital",
            "resolution": "4K30",
            "voltage_range": "5V USB-C"
        }
    },
    {
        "id": "dinogy-ultra-graphene-2-4s-1300mah-80c",
        "category": "battery",
        "name": "Ultra Graphene 2.0 1300mAh 4S 80C",
        "brand": "Dinogy",
        "price_php": 1650,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.rcpapa.com/products/dinogy-ultra-graphene-2-0-14-8v-4s-1300mah-80c-lipo-battery",
        "color": "#1a1a1a",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 80,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "siyi-fm30-2-4ghz-receiver",
        "category": "receiver",
        "name": "FM30 2.4GHz Long Range Receiver Module",
        "brand": "SIYI",
        "price_php": 2930,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.banggood.com/search/siyi-fm30.html",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "SIYI 2.4GHz",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
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
