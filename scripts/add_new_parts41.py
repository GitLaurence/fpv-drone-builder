"""Add the 41st batch of new FPV parts (one per category)."""
import json

NEW_PARTS = [
    {
        "id": "armattan-rooster-2-5",
        "category": "frame",
        "name": "Rooster 2.5\" Frame",
        "brand": "Armattan",
        "price_php": 2950,
        "weight_g": 58,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+2.5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 130,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 20,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+2.5"
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5",
        "category": "motor",
        "name": "Avenger 2306.5 1850KV",
        "brand": "BrotherHobby",
        "price_php": 1280,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2306.5+1850KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1850,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 38
        }
    },
    {
        "id": "speedybee-60a-4in1-esc",
        "category": "esc",
        "name": "60A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2150,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+60A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "mamba-f405-mk4",
        "category": "fc",
        "name": "F405 MK4 Flight Controller",
        "brand": "Diatone",
        "price_php": 2050,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F405+MK4",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-5x4-3x3-durable",
        "category": "propeller",
        "name": "5X4.3X3 Durable Propeller",
        "brand": "HQProp",
        "price_php": 220,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+5X4.3X3+Durable",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "white"]
        }
    },
    {
        "id": "foxeer-mini-cat-3",
        "category": "camera",
        "name": "Mini Cat 3 FPV Camera",
        "brand": "Foxeer",
        "price_php": 1580,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Mini+Cat+3",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "iflight-twig-vtx",
        "category": "vtx",
        "name": "TwigVTX 1W",
        "brand": "iFlight",
        "price_php": 1750,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+TwigVTX",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-ministar-1300mah-6s",
        "category": "battery",
        "name": "MiniStar 1300mAh 6S 100C LiPo",
        "brand": "CNHL",
        "price_php": 1480,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniStar+1300mAh+6S+100C",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "rdq-stamina-elrs-rx",
        "category": "receiver",
        "name": "Stamina ELRS Nano Receiver",
        "brand": "RaceDayQuads",
        "price_php": 980,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=RDQ+Stamina+ELRS+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 10
        }
    },
    {
        "id": "holybro-micro-m8n-gps",
        "category": "gps",
        "name": "Micro M8N GPS Module",
        "brand": "Holybro",
        "price_php": 950,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Micro+M8N+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "interface": "UART",
            "compass": True,
            "weight_g": 4,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "truerc-axii-2-antenna",
        "category": "antenna",
        "name": "AXII 2 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 850,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+AXII+2+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.92,
            "polarization": "RHCP",
            "connector": "MMCX",
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
