"""Batch 57: fills in ESC, GPS, and receiver categories that batch 56 missed
due to id collisions, adding real, currently-shipping parts not yet in the
catalog, following the existing schema and buy_url conventions.
"""
import json

NEW_PARTS = [
    {
        "id": "skystars-ko25-4in1",
        "category": "esc",
        "name": "KO25 25A 4-in-1 ESC",
        "brand": "Skystars",
        "price_php": 728,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Skystars+KO25+25A+4-in-1+ESC",
        "color": "#1b1b1b",
        "specs": {
            "amp_rating": 25,
            "input_voltage_s": 4,
            "protocol": "DShot600",
            "form_factor_mm": 16
        }
    },
    {
        "id": "speedybee-gps-m9",
        "category": "gps",
        "name": "GPS M9 Module",
        "brand": "SpeedyBee",
        "price_php": 1232,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=GPS+M9+Module",
        "color": "#131313",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "betafpv-superg-nano-rx",
        "category": "receiver",
        "name": "SuperG Nano Receiver",
        "brand": "BetaFPV",
        "price_php": 896,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+SuperG+Nano+Receiver",
        "color": "#171717",
        "specs": {
            "protocol": "SuperG",
            "frequency_mhz": 2400
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
