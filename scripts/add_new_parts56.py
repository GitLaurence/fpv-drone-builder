"""Batch 56: follow-up round adding a few more real, currently-shipping FPV
parts in categories that had heavy overlap with the existing catalog in
batch 55 (antenna, fc, camera, gps), following the existing schema and
buy_url conventions.
"""
import json

NEW_PARTS = [
    {
        "id": "truerc-singularity-2-rhcp-antenna",
        "category": "antenna",
        "name": "Singularity 2 5.8GHz RHCP SMA",
        "brand": "TrueRC",
        "price_php": 1288,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Singularity+2+5.8GHz+RHCP",
        "color": "#0e0e0e",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 4.8,
            "type": "patch"
        }
    },
    {
        "id": "hglrc-tslot-58-rhcp-antenna",
        "category": "antenna",
        "name": "T-Slot 5.8GHz RHCP SMA",
        "brand": "HGLRC",
        "price_php": 392,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=T-Slot+5.8GHz+RHCP+Antenna",
        "color": "#151515",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2,
            "type": "cloverleaf"
        }
    },
    {
        "id": "holybro-kakute-h7-v2-fc",
        "category": "fc",
        "name": "Kakute H7 V2 Flight Controller",
        "brand": "Holybro",
        "price_php": 3416,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Kakute+H7+V2+Flight+Controller",
        "color": "#191919",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5
        }
    },
    {
        "id": "flywoo-goku-gn745-fc",
        "category": "fc",
        "name": "GOKU GN745 Nano Flight Controller",
        "brand": "Flywoo",
        "price_php": 2576,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=GOKU+GN745+Nano+Flight+Controller",
        "color": "#101010",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },
    {
        "id": "runcam-hybrid-3-camera",
        "category": "camera",
        "name": "Hybrid 3 Dual FPV/HD Camera",
        "brand": "RunCam",
        "price_php": 5488,
        "weight_g": 20,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Hybrid+3+Dual+FPV+HD+Camera",
        "color": "#141414",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "caddx-ratel-2-pro-camera",
        "category": "camera",
        "name": "Ratel 2 Pro FPV Camera",
        "brand": "Caddx",
        "price_php": 2072,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ratel+2+Pro+FPV+Camera",
        "color": "#101010",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "matek-m9n-5883-gps",
        "category": "gps",
        "name": "M9N-5883 GPS + Compass",
        "brand": "Matek",
        "price_php": 1848,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M9N-5883+GPS+Compass",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 16,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "hglrc-m100-5883-gps",
        "category": "gps",
        "name": "M100-5883 GPS + Compass",
        "brand": "HGLRC",
        "price_php": 1344,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=M100-5883+GPS+Compass",
        "color": "#111111",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-SH 6-pin"
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
