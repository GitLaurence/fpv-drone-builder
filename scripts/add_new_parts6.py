#!/usr/bin/env python3
"""Add a sixth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "impulsrc-apex-5",
        "category": "frame",
        "name": "Apex 5\" Frame",
        "brand": "ImpulseRC",
        "price_php": 7299,
        "weight_g": 89,
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
    {
        "id": "armattan-wraith-5",
        "category": "frame",
        "name": "Wraith 5\" Frame",
        "brand": "Armattan",
        "price_php": 6899,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://armattan.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+wraith"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "brotherhobby-avenger-2306-1900kv",
        "category": "motor",
        "name": "Avenger 2306 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1399,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.brotherhobbystore.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "iflight-xing2-2207-1800kv",
        "category": "motor",
        "name": "XING2 2207 1800KV",
        "brand": "iFlight",
        "price_php": 1299,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-4in1-50a",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 2899,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "iflight-blitz-e55-50a-4in1",
        "category": "esc",
        "name": "BLITZ E55 50A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 2649,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ─────────────────────────────────────────────────
    {
        "id": "mamba-f405-mk4-fc",
        "category": "fc",
        "name": "MAMBA F405 MK4 Flight Controller",
        "brand": "Diatone",
        "price_php": 1799,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
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
        "id": "speedybee-f745-v4-fc",
        "category": "fc",
        "name": "F745 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2199,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-51433",
        "category": "propeller",
        "name": "Hurricane 51433 Propeller",
        "brand": "Gemfan",
        "price_php": 259,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "white", "black"]
        }
    },
    {
        "id": "dal-cyclone-t5045c",
        "category": "propeller",
        "name": "Cyclone T5045C Propeller",
        "brand": "DAL",
        "price_php": 239,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────────
    {
        "id": "caddx-ratel2",
        "category": "camera",
        "name": "Ratel 2 Camera",
        "brand": "Caddx",
        "price_php": 1899,
        "weight_g": 8.5,
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
        "id": "walksnail-avatar-hd-camera",
        "category": "camera",
        "name": "Avatar HD V3 Camera",
        "brand": "Walksnail",
        "price_php": 3299,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 150,
            "format": "Digital HD",
            "tvl": 1080,
            "voltage_range": "6.5-25.2V"
        }
    },

    # ─── VIDEO TRANSMITTERS (2) ─────────────────────────────────────────────────
    {
        "id": "rush-tank-solo-vtx",
        "category": "vtx",
        "name": "Tank Solo VTX",
        "brand": "RUSH",
        "price_php": 2199,
        "weight_g": 6.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "6.5-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-sirius-1200-vtx",
        "category": "vtx",
        "name": "Sirius 1200 VTX",
        "brand": "HGLRC",
        "price_php": 1899,
        "weight_g": 7.2,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "cnhl-black-series-4s-1500mah",
        "category": "battery",
        "name": "Black Series 1500mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1399,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-rline-4s-1800mah",
        "category": "battery",
        "name": "R-Line V4.0 1800mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1799,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1800,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────────
    {
        "id": "betafpv-superd-elrs-rx",
        "category": "receiver",
        "name": "SuperD 2.4GHz ELRS Receiver",
        "brand": "BetaFPV",
        "price_php": 1099,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "tbs-r9-mm-rx",
        "category": "receiver",
        "name": "Crossfire R9 Mini Receiver",
        "brand": "TBS",
        "price_php": 1899,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 50
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "betafpv-m9-gps-lite",
        "category": "gps",
        "name": "M9 GPS Lite Module",
        "brand": "BetaFPV",
        "price_php": 999,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 16,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10-3100-gps",
        "category": "gps",
        "name": "M10-3100 GPS+Compass",
        "brand": "Matek",
        "price_php": 1499,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────────
    {
        "id": "foxeer-lollipop4-antenna",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 449,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
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
        "id": "tbs-axii2-antenna",
        "category": "antenna",
        "name": "Triumph Axii 2 5.8GHz Antenna",
        "brand": "TBS",
        "price_php": 799,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
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
