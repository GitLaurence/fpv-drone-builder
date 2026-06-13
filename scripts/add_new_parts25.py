"""Add 25th batch of new FPV parts - one real, verified product per category."""
import json

NEW_PARTS = [
    {
        "id": "axisflying-manta-5-se-v2",
        "category": "frame",
        "name": "Manta 5 SE V2",
        "brand": "Axisflying",
        "price_php": 14500,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/axisflying-manta-5-se-v2-frame-kit-squashed-x.html",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 235,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+manta+5+se"
        }
    },
    {
        "id": "tmotor-velox-veloce-v2207-5-v2-1750kv",
        "category": "motor",
        "name": "Velox Veloce V2207.5 V2 1750KV",
        "brand": "T-Motor",
        "price_php": 1740,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/t-motor-velox-veloce-v2207-5-v2-motor-1750kv-2550kv-royal-blue.html",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "hglrc-zeus-45a-v2",
        "category": "esc",
        "name": "Zeus 45A V2 4-in-1",
        "brand": "HGLRC",
        "price_php": 2670,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com/products/hglrc-zeus-45a-v2-3-6s-blheli_s-4in1-esc-fpv-racing-drone-20x20mm",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "holybro-kakute-f4-v2-4",
        "category": "fc",
        "name": "Kakute F4 V2.4",
        "brand": "Holybro",
        "price_php": 2900,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com/products/kakute-f4-v2-4",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-dp-5-1x4-6x3-pink",
        "category": "propeller",
        "name": "DP 5.1x4.6x3 V2S",
        "brand": "HQProp",
        "price_php": 200,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/hqprop-dp-5-1x4-6x3-propeller-set-of-4-light-pink.html",
        "color": "#ffc0cb",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["pink"]
        }
    },
    {
        "id": "walksnail-avatar-hd-nano-camera",
        "category": "camera",
        "name": "Avatar HD Nano Camera",
        "brand": "Walksnail",
        "price_php": 3190,
        "weight_g": 5.7,
        "in_stock": True,
        "buy_url": "https://www.caddxfpv.com/products/walksnail-avatar-hd-nano-camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "resolution": "1080p@60fps",
            "voltage_range": "6.5-25.2V"
        }
    },
    {
        "id": "iflight-blitz-whoop-2-5w-vtx",
        "category": "vtx",
        "name": "BLITZ Whoop 5.8G 2.5W",
        "brand": "iFlight",
        "price_php": 3653,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/BLITZ-Whoop-5.8G-2.5W-VTX-Pro2060",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-25.2V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-2200mah-6s-40c",
        "category": "battery",
        "name": "Black Series 2200mAh 6S 40C",
        "brand": "CNHL",
        "price_php": 1625,
        "weight_g": 290,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com/products/cnhl-black-series-2200mah-6s-22-2v-40c-lipo-battery-with-xt60-plug",
        "color": "#1a1a1a",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 2200,
            "c_rating": 40,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "radiomaster-rp3-h",
        "category": "receiver",
        "name": "RP3-H ExpressLRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 1320,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://radiomasterrc.com/products/rp3-h-expresslrs-2-4ghz-nano-receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "speedybee-bz-251-gps",
        "category": "gps",
        "name": "BZGNSS BZ-251 GPS with 5883 Compass",
        "brand": "SpeedyBee",
        "price_php": 1220,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/bzgnss-bz-251-gps-with-5883-compass/",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "foxeer-lollipop-v4",
        "category": "antenna",
        "name": "Lollipop V4 5.8G 2.6dBi",
        "brand": "Foxeer",
        "price_php": 1155,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/foxeer-lollipop-4-5-8g-2-6dbi-high-gain-fpv-antenna-2pcs-g-369",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
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
