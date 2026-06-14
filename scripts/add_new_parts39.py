"""Add a new batch of real FPV parts not yet present in data/parts.json."""
import json

NEW_PARTS = [
    {
        "id": "flywoo-firefly-hex-nano",
        "category": "frame",
        "name": "Firefly Hex Nano Frame",
        "brand": "Flywoo",
        "price_php": 940,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Firefly+Hex+Nano+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 130,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 20,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+firefly+hex+nano"
        }
    },
    {
        "id": "iflight-xl5-v5",
        "category": "frame",
        "name": "XL5 V5 Freestyle Frame",
        "brand": "iFlight",
        "price_php": 2650,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+XL5+V5+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+xl5"
        }
    },
    {
        "id": "iflight-xinge2-2207-2700kv",
        "category": "motor",
        "name": "XING-E2 2207 2700KV",
        "brand": "iFlight",
        "price_php": 1590,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+XING-E2+2207+2700KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2700,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "speedybee-f405-v4-mini-40a-aio",
        "category": "fc",
        "name": "F405 V4 Mini 40A AIO",
        "brand": "SpeedyBee",
        "price_php": 3240,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/?s=F405+V4+Mini+40A+AIO",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "esc_amp_rating": 40
        }
    },
    {
        "id": "hglrc-zeus-f745-v2-aio",
        "category": "fc",
        "name": "Zeus F745 V2 AIO",
        "brand": "HGLRC",
        "price_php": 3530,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Zeus+F745+V2+AIO",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "esc_amp_rating": 45
        }
    },
    {
        "id": "hqprop-5x4x3-v1s-durable",
        "category": "propeller",
        "name": "5x4x3 V1S Durable",
        "brand": "HQProp",
        "price_php": 180,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+5x4x3+V1S+Durable",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "orange"]
        }
    },
    {
        "id": "walksnail-avatar-nano-vtx-pro",
        "category": "vtx",
        "name": "Avatar Nano VTX Pro",
        "brand": "Walksnail",
        "price_php": 9499,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+Nano+VTX+Pro",
        "color": "#221100",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Digital",
            "bands": "Walksnail",
            "voltage_range": "7.4-26.4V",
            "connector": "U.FL",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "tattu-rline-v5-1300mah-6s-150c",
        "category": "battery",
        "name": "R-Line V5 1300mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2060,
        "weight_g": 200,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5+1300mAh+6S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "betafpv-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "BetaFPV",
        "price_php": 1180,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=M10+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BDS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 1.0 6-pin"
        }
    },
    {
        "id": "foxeer-lollipop-3-plus",
        "category": "antenna",
        "name": "Lollipop 3 Plus 5.8GHz",
        "brand": "Foxeer",
        "price_php": 470,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Lollipop+3+Plus+5.8GHz",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "omni"
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
