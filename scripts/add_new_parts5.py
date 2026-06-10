#!/usr/bin/env python3
"""Add a fifth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "armattan-marmotte-5",
        "category": "frame",
        "name": "Marmotte 5\" Frame",
        "brand": "Armattan",
        "price_php": 6380,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.armattanquads.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 224,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "impulserc-apex-5",
        "category": "frame",
        "name": "Apex 5\" Frame",
        "brand": "ImpulseRC",
        "price_php": 5220,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://impulserc.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "emax-eco-ii-2306-1700kv",
        "category": "motor",
        "name": "ECO II 2306 1700KV",
        "brand": "EMAX",
        "price_php": 986,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1700,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "iflight-xing2-2207-2750kv",
        "category": "motor",
        "name": "XING2 2207 2750KV",
        "brand": "iFlight",
        "price_php": 1160,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-45a",
        "category": "esc",
        "name": "Tekko32 F4 4-in-1 45A",
        "brand": "Holybro",
        "price_php": 2610,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "speedybee-f405-v4-50a",
        "category": "esc",
        "name": "F405 V4 4-in-1 50A ESC",
        "brand": "SpeedyBee",
        "price_php": 2900,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ─────────────────────────────────────────────────
    {
        "id": "speedybee-f405-v4-fc",
        "category": "fc",
        "name": "F405 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2320,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "holybro-kakute-f7-hdv",
        "category": "fc",
        "name": "Kakute F7 HDV",
        "brand": "Holybro",
        "price_php": 3770,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM20689",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-51466",
        "category": "propeller",
        "name": "Hurricane 51466",
        "brand": "Gemfan",
        "price_php": 174,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "dal-cyclone-t5046c",
        "category": "propeller",
        "name": "Cyclone T5046C",
        "brand": "DAL",
        "price_php": 203,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white"]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────────
    {
        "id": "foxeer-razer-mini",
        "category": "camera",
        "name": "Razer Mini",
        "brand": "Foxeer",
        "price_php": 1160,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ratel-2",
        "category": "camera",
        "name": "Ratel 2",
        "brand": "Caddx",
        "price_php": 1450,
        "weight_g": 7.5,
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

    # ─── VIDEO TRANSMITTERS (2) ─────────────────────────────────────────────────
    {
        "id": "iflight-tranzvr-58",
        "category": "vtx",
        "name": "TranzVR 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 1276,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-sky-1s2",
        "category": "vtx",
        "name": "Sky 1S2 VTX",
        "brand": "HGLRC",
        "price_php": 1044,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "tattu-rline4-1300mah-4s",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 4S 120C",
        "brand": "Tattu",
        "price_php": 1450,
        "weight_g": 162,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "cnhl-black-series-1300mah-6s",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1856,
        "weight_g": 240,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────────
    {
        "id": "tbs-crossfire-nano-rx",
        "category": "receiver",
        "name": "Crossfire Nano RX",
        "brand": "TBS",
        "price_php": 1450,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "radiomaster-rp1-elrs",
        "category": "receiver",
        "name": "RP1 ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 870,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "beitian-bn-220",
        "category": "gps",
        "name": "BN-220 GPS Module",
        "brand": "Beitian",
        "price_php": 870,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m10-gps",
        "category": "gps",
        "name": "Micro M10 GPS",
        "brand": "Holybro",
        "price_php": 1740,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://holybro.com",
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

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────────
    {
        "id": "foxeer-lollipop-4-plus",
        "category": "antenna",
        "name": "Lollipop 4 Plus",
        "brand": "Foxeer",
        "price_php": 580,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omnidirectional"
        }
    },
    {
        "id": "immersionrc-spironet-58",
        "category": "antenna",
        "name": "SpiroNet 5.8GHz Antenna",
        "brand": "ImmersionRC",
        "price_php": 580,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
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
