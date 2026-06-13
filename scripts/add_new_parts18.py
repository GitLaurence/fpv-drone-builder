"""Add another batch of real FPV parts across all categories."""
import json

NEW_PARTS = [
    {
        "id": "axisflying-manta5-se",
        "category": "frame",
        "name": "Manta5 SE",
        "brand": "AxisFlying",
        "price_php": 3299,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+manta5"
        }
    },
    {
        "id": "impulserc-helix-5",
        "category": "frame",
        "name": "Helix 5\"",
        "brand": "ImpulseRC",
        "price_php": 4850,
        "weight_g": 102,
        "in_stock": True,
        "buy_url": "https://www.impulserc.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 230,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=impulserc+helix"
        }
    },
    {
        "id": "betafpv-1404-3700kv",
        "category": "motor",
        "name": "1404 3700KV",
        "brand": "BetaFPV",
        "price_php": 950,
        "weight_g": 11.2,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 3700,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 14
        }
    },
    {
        "id": "flywoo-nin-2207.5-1900kv",
        "category": "motor",
        "name": "NIN 2207.5 1900KV",
        "brand": "Flywoo",
        "price_php": 1450,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "mamba-f45-mini-45a",
        "category": "esc",
        "name": "F45_Mini 45A 4-in-1",
        "brand": "Mamba",
        "price_php": 2399,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "flywoo-goku-gn745-60a",
        "category": "esc",
        "name": "GOKU GN745 60A 4-in-1",
        "brand": "Flywoo",
        "price_php": 3450,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 70
        }
    },
    {
        "id": "speedybee-f405-v4-bls",
        "category": "fc",
        "name": "F405 V4 BLS 45A AIO",
        "brand": "SpeedyBee",
        "price_php": 4599,
        "weight_g": 9.6,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "mamba-mk4-h743",
        "category": "fc",
        "name": "MK4 H743 Mini",
        "brand": "Mamba",
        "price_php": 3899,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-3x3x3",
        "category": "propeller",
        "name": "3X3X3",
        "brand": "HQProp",
        "price_php": 175,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 3,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["black", "gray", "orange"]
        }
    },
    {
        "id": "gemfan-hurricane-5125-3",
        "category": "propeller",
        "name": "Hurricane 5125-3",
        "brand": "Gemfan",
        "price_php": 240,
        "weight_g": 5.4,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "white"]
        }
    },
    {
        "id": "foxeer-nightwolf-v2",
        "category": "camera",
        "name": "Nightwolf V2",
        "brand": "Foxeer",
        "price_php": 1850,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ratel2-pro",
        "category": "camera",
        "name": "Ratel 2 Pro",
        "brand": "Caddx",
        "price_php": 2100,
        "weight_g": 8.2,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-pro",
        "category": "vtx",
        "name": "Avatar HD V3 Pro VTX",
        "brand": "Walksnail",
        "price_php": 6499,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital",
            "video_system": "Walksnail",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tbs-unify-pro32-nano-hv",
        "category": "vtx",
        "name": "Unify Pro32 Nano HV",
        "brand": "TBS",
        "price_php": 2750,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/U",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "gensace-1100mah-6s-100c",
        "category": "battery",
        "name": "1100mAh 6S 100C",
        "brand": "Gens Ace",
        "price_php": 1599,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-ministar-850mah-6s-100c",
        "category": "battery",
        "name": "MiniStar 850mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1290,
        "weight_g": 155,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 850,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tbs-nano-rx",
        "category": "receiver",
        "name": "Crossfire Nano RX",
        "brand": "TBS",
        "price_php": 1850,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "CRSF",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "happymodel-ep2-rx",
        "category": "receiver",
        "name": "EP2 ELRS Receiver",
        "brand": "HappyModel",
        "price_php": 850,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "holybro-m10-mini-gps",
        "category": "gps",
        "name": "M10 Mini GPS",
        "brand": "Holybro",
        "price_php": 1450,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 22,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "beitian-bn-220q",
        "category": "gps",
        "name": "BN-220Q GPS Module",
        "brand": "Beitian",
        "price_php": 750,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.beitian.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 5,
            "fix_time_s": 30,
            "compass": False,
            "connector": "JST-GH 4-pin"
        }
    },
    {
        "id": "tbs-triumph",
        "category": "antenna",
        "name": "Triumph 5.8GHz",
        "brand": "TBS",
        "price_php": 980,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "foxeer-lollipop-2-plus",
        "category": "antenna",
        "name": "Lollipop 2 Plus",
        "brand": "Foxeer",
        "price_php": 380,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
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
