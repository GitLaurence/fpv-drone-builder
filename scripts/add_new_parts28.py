"""Add 28th batch of new FPV parts - real, verified products across categories."""
import json

NEW_PARTS = [
    {
        "id": "iflight-evoque-x5-v2-frame",
        "category": "frame",
        "name": "Evoque X5 V2 Frame Kit",
        "brand": "iFlight",
        "price_php": 3450,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Evoque+X5+V2",
        "color": "#161616",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+evoque+x5"
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-1800kv",
        "category": "motor",
        "name": "Avenger 2306.5 1800KV Brushless Motor",
        "brand": "BrotherHobby",
        "price_php": 1085,
        "weight_g": 32.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2306.5+1800KV",
        "color": "#2f2f2f",
        "specs": {
            "kv": 1800,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "holybro-tekko32-f4-4in1-60a-esc",
        "category": "esc",
        "name": "Tekko32 F4 4-in-1 60A ESC",
        "brand": "Holybro",
        "price_php": 3350,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Tekko32+F4+4in1+60A",
        "color": "#1d1d1d",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "speedybee-f405-wing-mini-fc",
        "category": "fc",
        "name": "F405 Wing Mini Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2480,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+F405+Wing+Mini",
        "color": "#0f0f0f",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com/f405-wing-mini-flight-controller-manual/"
        }
    },
    {
        "id": "gemfan-hurricane-51466-prop",
        "category": "propeller",
        "name": "Hurricane 51466 Durable Tri-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 230,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "blue"]
        }
    },
    {
        "id": "caddx-ratel-2-camera",
        "category": "camera",
        "name": "Ratel 2 FPV Camera",
        "brand": "Caddx",
        "price_php": 1450,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ratel+2",
        "color": "#101010",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-tx1200-vtx",
        "category": "vtx",
        "name": "TX1200 Analog VTX",
        "brand": "Foxeer",
        "price_php": 1180,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=TX1200",
        "color": "#202020",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race band",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-r-line-4-1550mah-6s-130c",
        "category": "battery",
        "name": "R-Line Version 4.0 1550mAh 6S 130C LiPo",
        "brand": "Tattu",
        "price_php": 2950,
        "weight_g": 270,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+4.0+1550mAh+6S",
        "color": "#0a3d62",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1550,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tbs-crossfire-nano-rx-se-2",
        "category": "receiver",
        "name": "Crossfire Nano RX SE V2",
        "brand": "TBS",
        "price_php": 1480,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/search?q=Crossfire+Nano+RX+SE",
        "color": "#262626",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 868,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "holybro-pixhawk-gps-module-m9n",
        "category": "gps",
        "name": "Pixhawk GPS Module M9N",
        "brand": "Holybro",
        "price_php": 2950,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Pixhawk+GPS+Module+M9N",
        "color": "#1c1c1c",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "axii-2-antenna-rhcp-sma",
        "category": "antenna",
        "name": "AXII 2 RHCP Antenna",
        "brand": "ImmersionRC",
        "price_php": 890,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+AXII+2",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.9,
            "polarization": "RHCP",
            "connector": "SMA",
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
