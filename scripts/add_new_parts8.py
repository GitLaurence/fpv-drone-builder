#!/usr/bin/env python3
"""Add an eighth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "armattan-rooster-5-v2",
        "category": "frame",
        "name": "Rooster 5\" V2 Frame",
        "brand": "Armattan",
        "price_php": 4200,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.armattanproductions.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+5"
        }
    },
    {
        "id": "impulserc-apex-frame",
        "category": "frame",
        "name": "Apex 5\" Frame",
        "brand": "ImpulseRC",
        "price_php": 5200,
        "weight_g": 100,
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
        "id": "tmotor-velox-v2807-v2",
        "category": "motor",
        "name": "Velox V2807 V2 1300KV",
        "brand": "T-Motor",
        "price_php": 1850,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 43
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-2450kv",
        "category": "motor",
        "name": "Avenger 2306.5 2450KV",
        "brand": "BrotherHobby",
        "price_php": 1320,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2450,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-50a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3100,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "iflight-succex-e-50a-4in1",
        "category": "esc",
        "name": "SucceX-E 50A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 2400,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ──────────────────────────────────────────────────
    {
        "id": "speedybee-f405-v4-fc",
        "category": "fc",
        "name": "F405 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2350,
        "weight_g": 8.4,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com/speedybee-f405-v4-flight-controller/"
        }
    },
    {
        "id": "diatone-mamba-f405-mk4",
        "category": "fc",
        "name": "Mamba F405 MK4 Flight Controller",
        "brand": "Diatone",
        "price_php": 2150,
        "weight_g": 7.8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/products/mamba-f405-mk4-flight-controller"
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-51499-3",
        "category": "propeller",
        "name": "Hurricane 51499 3-Blade",
        "brand": "Gemfan",
        "price_php": 245,
        "weight_g": 5.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.99,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray",
                "green",
                "white"
            ]
        }
    },
    {
        "id": "dal-cyclone-t5047c",
        "category": "propeller",
        "name": "Cyclone T5047C",
        "brand": "DAL",
        "price_php": 215,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "blue",
                "purple"
            ]
        }
    },

    # ─── FPV CAMERAS (2) ─────────────────────────────────────────────────────────
    {
        "id": "foxeer-razer-mini",
        "category": "camera",
        "name": "Razer Mini",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 5.4,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
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
        "price_php": 1750,
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

    # ─── VIDEO TRANSMITTERS (2) ──────────────────────────────────────────────────
    {
        "id": "hglrc-sirius-5-8-1000mw-vtx",
        "category": "vtx",
        "name": "Sirius 5.8GHz 1000mW VTX",
        "brand": "HGLRC",
        "price_php": 1950,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-forcevtx-pro-5-8",
        "category": "vtx",
        "name": "ForceVTX Pro 5.8GHz",
        "brand": "iFlight",
        "price_php": 2100,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "6-27V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "cnhl-black-series-1300mah-6s",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1750,
        "weight_g": 245,
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
    {
        "id": "gensace-tattu-rline-1400mah-4s",
        "category": "battery",
        "name": "Tattu R-Line V4.0 1400mAh 4S 130C",
        "brand": "Gens Ace",
        "price_php": 1450,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1400,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────────
    {
        "id": "tbs-crossfire-nano-rx",
        "category": "receiver",
        "name": "Crossfire Nano RX",
        "brand": "TBS",
        "price_php": 1450,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 868,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "radiomaster-rp1-elrs-rx",
        "category": "receiver",
        "name": "RP1 2.4GHz ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 950,
        "weight_g": 1.2,
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

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "beitian-bn-220-gps",
        "category": "gps",
        "name": "BN-220 GPS+Compass Module",
        "brand": "Beitian",
        "price_php": 900,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 29,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "radiolink-se100-gps",
        "category": "gps",
        "name": "SE100 GPS Module",
        "brand": "RadioLink",
        "price_php": 1350,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────────
    {
        "id": "immersionrc-spironet-antenna",
        "category": "antenna",
        "name": "SpiroNET 5.8GHz Antenna",
        "brand": "ImmersionRC",
        "price_php": 650,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "RP-SMA",
            "type": "omnidirectional"
        }
    },
    {
        "id": "lumenier-axii-2-antenna",
        "category": "antenna",
        "name": "AXII 2 5.8GHz Antenna",
        "brand": "Lumenier",
        "price_php": 720,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
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
