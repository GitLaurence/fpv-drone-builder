#!/usr/bin/env python3
"""Add an eighth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "lumenier-qav-r-5-frame",
        "category": "frame",
        "name": "QAV-R 5\" Racing Frame",
        "brand": "Lumenier",
        "price_php": 2450,
        "weight_g": 85,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=lumenier+qav-r"
        }
    },
    {
        "id": "impulserc-apex",
        "category": "frame",
        "name": "Apex 5\" Freestyle Frame",
        "brand": "ImpulseRC",
        "price_php": 3850,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://impulserc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=impulserc+apex"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "tmotor-f60-pro-iv-2207-1750kv",
        "category": "motor",
        "name": "F60 Pro IV 2207 1750KV",
        "brand": "T-Motor",
        "price_php": 1450,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-1900kv",
        "category": "motor",
        "name": "Avenger 2306.5 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1180,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 37
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-50a-4in1-esc",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 2950,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "current_rating_a": 50,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "firmware": "BLHeli_32",
            "mount_pattern_mm": 30,
            "protocols": "DShot1200/600/300"
        }
    },
    {
        "id": "iflight-succex-e-45a-4in1-esc",
        "category": "esc",
        "name": "SucceX-E 45A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 2150,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "current_rating_a": 45,
            "min_voltage_s": 2,
            "max_voltage_s": 6,
            "firmware": "BLHeli_32",
            "mount_pattern_mm": 30,
            "protocols": "DShot600/300/150"
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ──────────────────────────────────────────────────
    {
        "id": "matek-f405-wing-fc",
        "category": "fc",
        "name": "F405-Wing Flight Controller",
        "brand": "Matek",
        "price_php": 2750,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "mcu": "STM32F405",
            "gyro": "MPU6000",
            "mount_pattern_mm": 30.5,
            "uart_count": 7,
            "blackbox": "16MB flash",
            "betaflight_target": "MATEKF405"
        }
    },
    {
        "id": "iflight-succex-e-f4-v2-5-fc",
        "category": "fc",
        "name": "SucceX-E F4 V2.5 Flight Controller",
        "brand": "iFlight",
        "price_php": 1750,
        "weight_g": 7.6,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "mcu": "STM32F405",
            "gyro": "ICM20602",
            "mount_pattern_mm": 30.5,
            "uart_count": 6,
            "blackbox": "8MB flash",
            "betaflight_target": "IFLIGHT_F405"
        }
    },

    # ─── PROPELLERS (2) ──────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-5042-3blade",
        "category": "propeller",
        "name": "Hurricane 5042 3-Blade (4pcs)",
        "brand": "Gemfan",
        "price_php": 220,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_inch": 5,
            "pitch_inch": 4.2,
            "blade_count": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    {
        "id": "dal-cyclone-t5040c",
        "category": "propeller",
        "name": "Cyclone T5040C (4pcs)",
        "brand": "DAL",
        "price_php": 240,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a1a1a",
        "specs": {
            "size_inch": 5,
            "pitch_inch": 4,
            "blade_count": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },

    # ─── CAMERAS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "foxeer-razer-mini-camera",
        "category": "camera",
        "name": "Razer Mini FPV Camera",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/3\" CMOS",
            "tvl": 1200,
            "fov_deg": 160,
            "voltage_range": "5-40V",
            "format": "NTSC/PAL switchable"
        }
    },
    {
        "id": "caddx-ratel-2-camera",
        "category": "camera",
        "name": "Ratel 2 FPV Camera",
        "brand": "Caddx",
        "price_php": 1650,
        "weight_g": 8.8,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "tvl": 1200,
            "fov_deg": 166,
            "voltage_range": "5-40V",
            "format": "NTSC/PAL switchable"
        }
    },

    # ─── VIDEO TRANSMITTERS (2) ──────────────────────────────────────────────────
    {
        "id": "iflight-transtec-vega-vtx",
        "category": "vtx",
        "name": "TransTEC Vega 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 1850,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "6-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-sirius-1s-vtx",
        "category": "vtx",
        "name": "Sirius 1S 5.8GHz VTX",
        "brand": "HGLRC",
        "price_php": 1100,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "3.5-6V",
            "connector": "U.FL"
        }
    },

    # ─── BATTERIES (2) ───────────────────────────────────────────────────────────
    {
        "id": "cnhl-black-series-1300mah-4s-100c",
        "category": "battery",
        "name": "Black Series 1300mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1050,
        "weight_g": 152,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-1550mah-4s-75c",
        "category": "battery",
        "name": "Tattu 1550mAh 4S 75C",
        "brand": "Gens Ace",
        "price_php": 980,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1550,
            "c_rating": 75,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },

    # ─── RECEIVERS (2) ───────────────────────────────────────────────────────────
    {
        "id": "tbs-crossfire-nano-se-rx",
        "category": "receiver",
        "name": "Crossfire Nano SE Receiver",
        "brand": "TBS",
        "price_php": 1900,
        "weight_g": 1.6,
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
        "id": "radiomaster-rp3-elrs-rx",
        "category": "receiver",
        "name": "RP3 2.4GHz ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 850,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },

    # ─── GPS MODULES (2) ─────────────────────────────────────────────────────────
    {
        "id": "iflight-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "iFlight",
        "price_php": 1300,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 24,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "speedybee-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1250,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
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

    # ─── ANTENNAS (2) ────────────────────────────────────────────────────────────
    {
        "id": "truerc-xair-antenna",
        "category": "antenna",
        "name": "X-AIR 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 650,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://truerc.ca",
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
        "id": "lumenier-axii-2-antenna",
        "category": "antenna",
        "name": "AXII 2 5.8GHz Antenna",
        "brand": "Lumenier",
        "price_php": 580,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
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
