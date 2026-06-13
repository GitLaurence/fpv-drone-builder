"""24th batch: 11 new real FPV parts, one per category, with verified pricing and links."""
import json

NEW_PARTS = [
    {
        "id": "axisflying-manta-v2-5",
        "category": "frame",
        "name": "Manta V2 5\"",
        "brand": "Axisflying",
        "price_php": 4650,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/products/axisflying-manta5-5inch-fpv-freestyle-squashed-x-frame-kit",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 238,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+manta"
        }
    },
    {
        "id": "rcinpower-gts-v2-2306",
        "category": "motor",
        "name": "GTS V2 2306",
        "brand": "RCINPower",
        "price_php": 1100,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com/collections/rcinpower-motors",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2750,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "holybro-tekko32-f4-60a",
        "category": "esc",
        "name": "Tekko32 F4 4-in-1 60A",
        "brand": "Holybro",
        "price_php": 4000,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://holybro.com/products/tekko32-f4-4in1-60a-esc",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "mamba-f405-mini-mk2",
        "category": "fc",
        "name": "F405 Mini MK2",
        "brand": "Mamba",
        "price_php": 2500,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/diatone-mamba-dji-f405-mk2-flight-controller-mini-20x20.html",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-freestyle-dp-5x4.3x3-v2s",
        "category": "propeller",
        "name": "Freestyle DP 5x4.3x3 V2S",
        "brand": "HQProp",
        "price_php": 175,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/hqprop-freestyle-dp-5x4-3x3v2s-propeller-set-of-4.html",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "orange", "green"]
        }
    },
    {
        "id": "walksnail-avatar-hd-nano-camera-v3",
        "category": "camera",
        "name": "Avatar HD Nano Camera V3",
        "brand": "Walksnail",
        "price_php": 2500,
        "weight_g": 5.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/walksnail-avatar-nano-camera-v3.html",
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
        "id": "rushfpv-tank-iii-ultimate",
        "category": "vtx",
        "name": "Tank III Ultimate",
        "brand": "RushFPV",
        "price_php": 2100,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://rushfpv.net/products/tank-iii-ultimate-vtx",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-v2-1500-6s",
        "category": "battery",
        "name": "Black Series V2.0 1500mAh 6S 130C",
        "brand": "CNHL",
        "price_php": 1650,
        "weight_g": 190,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/cnhl-black-series-v2-0-1500mah-22-2v-6s-130c-lipo-battery-xt60.html",
        "color": "#1a1a1a",
        "specs": {
            "capacity_mah": 1500,
            "voltage_s": 6,
            "discharge_rate_c": 130,
            "connector": "XT60",
            "chemistry": "LiPo"
        }
    },
    {
        "id": "radiomaster-r161",
        "category": "receiver",
        "name": "R161 16CH Receiver",
        "brand": "RadioMaster",
        "price_php": 1050,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/radiomaster-r161-16ch-frsky-d16-compatible-sbus-receiver-w-s-port.html",
        "color": "#1a001a",
        "specs": {
            "protocol": "FrSky D16",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 2
        }
    },
    {
        "id": "readytosky-neo-m8n-gps",
        "category": "gps",
        "name": "NEO-M8N GPS Module",
        "brand": "Readytosky",
        "price_php": 800,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.readytosky.com/e_products/M8N-GPS-3-19.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "foxeer-micro-lollipop-2.5dbi",
        "category": "antenna",
        "name": "Micro Lollipop 2.5dBi",
        "brand": "Foxeer",
        "price_php": 1000,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com/products/foxeer-micro-lollipop-fpv-antenna-5-8g-2-5dbi-high-gain-sma-rhcp",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
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
