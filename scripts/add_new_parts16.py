#!/usr/bin/env python3
"""Add 16th batch of 22 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────
    {
        "id": "axisflying-cinerace-v3",
        "category": "frame",
        "name": "Cinerace V3 5\"",
        "brand": "Axisflying",
        "price_php": 4200,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 235,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+cinerace"
        }
    },
    {
        "id": "ummagawd-ferrite-5",
        "category": "frame",
        "name": "Ferrite 5\" Freestyle",
        "brand": "UmmaGawd",
        "price_php": 3360,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=ummagawd+ferrite"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────
    {
        "id": "tmotor-velox-v2306",
        "category": "motor",
        "name": "Velox V2306.5",
        "brand": "T-Motor",
        "price_php": 1512,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "flywoo-nin-1404",
        "category": "motor",
        "name": "NIN 1404",
        "brand": "Flywoo",
        "price_php": 448,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "kv": 4600,
            "stator_size": "1404",
            "motor_mount_mm": 16,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 15
        }
    },

    # ─── ESC (2) ────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-60a",
        "category": "esc",
        "name": "Tekko32 F4 60A 4-in-1",
        "brand": "Holybro",
        "price_php": 2520,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "iflight-blitz-e55-esc",
        "category": "esc",
        "name": "BLITZ E55 4-in-1",
        "brand": "iFlight",
        "price_php": 2240,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#000000",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ─────────────────────────────────────────────
    {
        "id": "mamba-f405-mk4",
        "category": "fc",
        "name": "F405 MK4",
        "brand": "Diatone",
        "price_php": 1960,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/products/mamba-f405-mk4-flight-controller"
        }
    },
    {
        "id": "speedybee-f405-v3-stack",
        "category": "fc",
        "name": "F405 V3 BLS Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 1680,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#0a0a2a",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com/speedybee-f405-v3-flight-controller/"
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────
    {
        "id": "hqprop-dt-7x4x3",
        "category": "propeller",
        "name": "DT 7×4×3",
        "brand": "HQProp",
        "price_php": 224,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-floppy-proppy-5128",
        "category": "propeller",
        "name": "Floppy Proppy 5128",
        "brand": "Gemfan",
        "price_php": 196,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.8,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["gray", "green", "pink"]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────
    {
        "id": "foxeer-night-cat-4",
        "category": "camera",
        "name": "Night Cat 4",
        "brand": "Foxeer",
        "price_php": 1456,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 165,
            "format": "Analog Starlight",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ant-nano-v5",
        "category": "camera",
        "name": "Ant Nano V5",
        "brand": "Caddx",
        "price_php": 1064,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },

    # ─── VTX (2) ────────────────────────────────────────────────────────────
    {
        "id": "tbs-unify-pro32-nano-vtx",
        "category": "vtx",
        "name": "Unify Pro32 Nano",
        "brand": "Team BlackSheep",
        "price_php": 3360,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "6.5-25.2V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rushfpv-tank-nano-vtx",
        "category": "vtx",
        "name": "Tank Nano VTX",
        "brand": "Rush",
        "price_php": 1680,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────
    {
        "id": "tattu-r-line-4-4s-1800",
        "category": "battery",
        "name": "R-Line V4.0 1800mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1456,
        "weight_g": 196,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1800,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gnb-6s-1300mah-lipo",
        "category": "battery",
        "name": "6S 1300mAh 100C",
        "brand": "GNB",
        "price_php": 1568,
        "weight_g": 232,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#0a0a1a",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────
    {
        "id": "betafpv-elrs-receiver-lite",
        "category": "receiver",
        "name": "ELRS Nano Receiver Lite",
        "brand": "BetaFPV",
        "price_php": 560,
        "weight_g": 0.6,
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
    {
        "id": "radiomaster-er8-elrs-rx",
        "category": "receiver",
        "name": "ER8 ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 896,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 40
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────
    {
        "id": "holybro-st01-gps-v2",
        "category": "gps",
        "name": "ST01 GPS V2",
        "brand": "Holybro",
        "price_php": 1232,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "iflight-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "iFlight",
        "price_php": 1064,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────
    {
        "id": "rushfpv-cherry-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz Antenna",
        "brand": "Rush",
        "price_php": 672,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#cc0033",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "truerc-singularity-antenna",
        "category": "antenna",
        "name": "Singularity 5.8GHz",
        "brand": "TrueRC",
        "price_php": 1568,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 11,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
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
