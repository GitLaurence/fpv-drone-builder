#!/usr/bin/env python3
"""Add a fourth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "lumenier-qav-s-5",
        "category": "frame",
        "name": "QAV-S 5\" Frame",
        "brand": "Lumenier",
        "price_php": 3219,
        "weight_g": 95,
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
            "standoff_height_mm": 30
        }
    },
    {
        "id": "tbs-source-one-mini-frame",
        "category": "frame",
        "name": "Source One Mini 3.5\" Frame",
        "brand": "TBS",
        "price_php": 952,
        "weight_g": 48,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 156,
            "motor_mount_mm": 19,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "hobbywing-xrotor-2207-1960kv",
        "category": "motor",
        "name": "XRotor 2207 1960KV",
        "brand": "Hobbywing",
        "price_php": 1399,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.hobbywing.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1960,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "brotherhobby-rs2207-2400kv",
        "category": "motor",
        "name": "RS2207 Racing Edition 2400KV",
        "brand": "BrotherHobby",
        "price_php": 1119,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2400,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-45a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 45A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3199,
        "weight_g": 25,
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
        "id": "speedybee-f405-55a-4in1",
        "category": "esc",
        "name": "55A BLHeli_32 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2399,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
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
        "id": "hglrc-zeus-f722",
        "category": "fc",
        "name": "Zeus F722 Flight Controller",
        "brand": "HGLRC",
        "price_php": 2799,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
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
    {
        "id": "mamba-mk4-f405",
        "category": "fc",
        "name": "Mamba MK4 F405 Flight Controller",
        "brand": "Diatone",
        "price_php": 2199,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
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

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "dal-cyclone-t5047c",
        "category": "propeller",
        "name": "Cyclone T5047C",
        "brand": "DAL",
        "price_php": 251,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.dalprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "white"]
        }
    },
    {
        "id": "gemfan-flash-5152-3",
        "category": "propeller",
        "name": "Flash 5152-3",
        "brand": "Gemfan",
        "price_php": 229,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "blue"]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────────
    {
        "id": "runcam-racer-nano-3",
        "category": "camera",
        "name": "Racer Nano 3",
        "brand": "RunCam",
        "price_php": 1399,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "hdzero-freestyle-v2-cam",
        "category": "camera",
        "name": "Freestyle V2 Camera",
        "brand": "HDZero",
        "price_php": 3199,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "resolution": "720p60",
            "video_system": "HDZero"
        }
    },

    # ─── VIDEO TRANSMITTERS (2) ─────────────────────────────────────────────────
    {
        "id": "hglrc-sirius-1000",
        "category": "vtx",
        "name": "Sirius 1000 VTX",
        "brand": "HGLRC",
        "price_php": 1899,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "akk-fx2-vtx",
        "category": "vtx",
        "name": "FX2 5.8GHz VTX",
        "brand": "AKK",
        "price_php": 899,
        "weight_g": 5.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "gensace-6s-1300mah",
        "category": "battery",
        "name": "1300mAh 6S 100C",
        "brand": "Gens Ace",
        "price_php": 1899,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
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
        "id": "cnhl-blackseries-6s-1300mah",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1849,
        "weight_g": 240,
        "in_stock": True,
        "buy_url": "https://www.cnhl.com.cn",
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
        "id": "happymodel-ex1000-elrs-rx",
        "category": "receiver",
        "name": "EX1000 2.4GHz ELRS Receiver",
        "brand": "Happymodel",
        "price_php": 749,
        "weight_g": 1.2,
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
        "id": "betafpv-elrs-2-4g-nano-rx",
        "category": "receiver",
        "name": "ELRS 2.4GHz Nano Receiver",
        "brand": "BetaFPV",
        "price_php": 699,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "beitian-bn-220-gps",
        "category": "gps",
        "name": "BN-220 GPS+Compass",
        "brand": "Beitian",
        "price_php": 649,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.beitian.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox 7",
            "update_rate_hz": 10,
            "fix_time_s": 27,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "cuav-neo-3-pro-gps",
        "category": "gps",
        "name": "Neo 3 Pro GPS Module",
        "brand": "CUAV",
        "price_php": 3099,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.cuav.net",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M9N",
            "update_rate_hz": 25,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────────
    {
        "id": "foxeer-lollipop-4",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 449,
        "weight_g": 5,
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
        "id": "rushfpv-cherry",
        "category": "antenna",
        "name": "Cherry 5.8GHz Antenna",
        "brand": "RushFPV",
        "price_php": 499,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://rushfpv.com",
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
