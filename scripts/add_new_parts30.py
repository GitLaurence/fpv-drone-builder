"""Add 30th batch of new FPV parts - real, verified products across categories."""
import json

NEW_PARTS = [
    {
        "id": "armattan-rooster-5-frame",
        "category": "frame",
        "name": "Rooster 5\" Frame",
        "brand": "Armattan",
        "price_php": 5200,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster"
        }
    },
    {
        "id": "tmotor-velox-v2806-1300kv-motor",
        "category": "motor",
        "name": "Velox V2806 V2 1300KV Motor",
        "brand": "T-Motor",
        "price_php": 1700,
        "weight_g": 32.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Velox+V2806+V2+1300KV",
        "color": "#2e2e2e",
        "specs": {
            "kv": 1300,
            "stator_size": "2806",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 32
        }
    },
    {
        "id": "holybro-tekko32-f4-45a-esc",
        "category": "esc",
        "name": "Tekko32 F4 4-in-1 45A ESC",
        "brand": "Holybro",
        "price_php": 2550,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Tekko32+F4+45A",
        "color": "#0f0f0f",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "diatone-mamba-f405-mk4-fc",
        "category": "fc",
        "name": "Mamba F405 Mk4 Flight Controller",
        "brand": "Diatone",
        "price_php": 2000,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F405+Mk4",
        "color": "#121212",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": True,
            "diagram_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F405+Mk4"
        }
    },
    {
        "id": "gemfan-hurricane-51466-propeller",
        "category": "propeller",
        "name": "Hurricane 51466 Tri-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 180,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466",
        "color": "#1c1c1c",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.66,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "black", "green"]
        }
    },
    {
        "id": "caddx-polar-vista-camera",
        "category": "camera",
        "name": "Polar Vista Digital HD Camera",
        "brand": "Caddx",
        "price_php": 3950,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Polar+Vista",
        "color": "#171717",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 150,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "7.4-25.2V"
        }
    },
    {
        "id": "tbs-unify-pro32-hv-vtx",
        "category": "vtx",
        "name": "Unify Pro32 HV VTX",
        "brand": "TBS",
        "price_php": 2550,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=Unify+Pro32+HV",
        "color": "#202020",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race band",
            "voltage_range": "7-36V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-black-series-1500mah-6s-battery",
        "category": "battery",
        "name": "Black Series 1500mAh 6S 100C LiPo",
        "brand": "CNHL",
        "price_php": 1700,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1500mAh+6S+100C",
        "color": "#5c0a0a",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tbs-crossfire-nano-rx-se-receiver",
        "category": "receiver",
        "name": "Crossfire Nano RX SE",
        "brand": "TBS",
        "price_php": 1420,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=Crossfire+Nano+RX+SE",
        "color": "#2a2a2a",
        "specs": {
            "protocol": "CRSF",
            "frequency_mhz": 915,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "holybro-ub10-gps",
        "category": "gps",
        "name": "UB10 GPS Module",
        "brand": "Holybro",
        "price_php": 1420,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+UB10+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "tbs-triumph-pagoda-antenna",
        "category": "antenna",
        "name": "Triumph Pagoda Pro Antenna",
        "brand": "TBS",
        "price_php": 850,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=Triumph+Pagoda+Pro",
        "color": "#181818",
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
