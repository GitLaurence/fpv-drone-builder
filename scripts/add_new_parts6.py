#!/usr/bin/env python3
"""Add a sixth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "armattan-rooster-5-frame",
        "category": "frame",
        "name": "Rooster 5\" Frame",
        "brand": "Armattan",
        "price_php": 7627,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://armattanquads.com/products/rooster-1",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5.1,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster"
        }
    },
    {
        "id": "impulserc-apex-evo-5-frame",
        "category": "frame",
        "name": "Apex EVO 5\" HD Frame Kit",
        "brand": "ImpulseRC",
        "price_php": 9604,
        "weight_g": 101,
        "in_stock": True,
        "buy_url": "https://impulserc.com/collections/apex/frames",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=impulserc+apex"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "tmotor-velox-v2-2207-5-1750kv",
        "category": "motor",
        "name": "Velox V2 2207.5 1750KV",
        "brand": "T-Motor",
        "price_php": 1299,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/goods-1139-V22075+V2.html",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "brotherhobby-avenger-v3-2812-1115kv",
        "category": "motor",
        "name": "Avenger V3 2812 1115KV",
        "brand": "BrotherHobby",
        "price_php": 2146,
        "weight_g": 46,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/c/fpv-motor_0072",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1115,
            "stator_size": "2812",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "diatone-mamba-f45-128k-esc",
        "category": "esc",
        "name": "Mamba F45_128K 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 2570,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/products/mb-f45_128k-bl32-esc",
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
        "id": "holybro-tekko32-f4-50a-esc",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3559,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://holybro.com/products/tekko32-f4-4in1-50a-esc",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ────────────────────────────────────────────────
    {
        "id": "speedybee-f405-v4-bls-55a-stack",
        "category": "fc",
        "name": "F405 V4 BLS 55A Stack",
        "brand": "SpeedyBee",
        "price_php": 3954,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/speedybee-f405-v4-bls-55a-30x30-fc-esc-stack/",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688-P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "diatone-mamba-mk4-h743-v2-fc",
        "category": "fc",
        "name": "Mamba MK4 H743 V2 FC",
        "brand": "Diatone",
        "price_php": 3107,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/products/mamba-mk4-h743-v2-flight-control-30mm-m3",
        "color": "#000055",
        "specs": {
            "gyro": "Dual ICM42688-P",
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
        "id": "hqprop-dp-5x4.3x3-v1s",
        "category": "propeller",
        "name": "DP 5×4.3×3 V1S",
        "brand": "HQProp",
        "price_php": 225,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com/hq-durable-prop-5x43x3v1s-2cw2ccw-poly-carbonate-p0048.html",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "light green", "light blue", "light pink"]
        }
    },
    {
        "id": "hqprop-ethix-s5",
        "category": "propeller",
        "name": "Ethix S5 5×4×3",
        "brand": "HQProp",
        "price_php": 225,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/prod:ethix_s5_props",
        "color": "#cccccc",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["light grey"]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────────
    {
        "id": "runcam-phoenix-2",
        "category": "camera",
        "name": "Phoenix 2",
        "brand": "RunCam",
        "price_php": 2203,
        "weight_g": 8.6,
        "in_stock": True,
        "buy_url": "https://shop.runcam.com/runcam-phoenix-2/",
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
        "id": "walksnail-avatar-hd-nano-camera-v3",
        "category": "camera",
        "name": "Avatar HD Nano Camera V3",
        "brand": "Walksnail",
        "price_php": 2824,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.caddxfpv.com/products/walksnail-avatar-hd-nano-camera-v3",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "video_system": "Walksnail Avatar",
            "voltage_range": "6-25V"
        }
    },

    # ─── VTX (2) ────────────────────────────────────────────────────────────────
    {
        "id": "rushfpv-tank-solo-vtx",
        "category": "vtx",
        "name": "Tank Solo VTX",
        "brand": "RushFPV",
        "price_php": 2598,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://rushfpv.net/products/tank-solo-vtx",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "walksnail-avatar-hd-mini-vtx-v3",
        "category": "vtx",
        "name": "Avatar HD Mini VTX Module V3",
        "brand": "Walksnail",
        "price_php": 4464,
        "weight_g": 8.3,
        "in_stock": True,
        "buy_url": "https://www.caddxfpv.com/products/walksnail-avatar-hd-mini-vtx-v3",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Digital",
            "video_system": "Walksnail Avatar",
            "voltage_range": "6-25V",
            "connector": "Built-in"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "cnhl-black-series-4s-1300mah-100c",
        "category": "battery",
        "name": "Black Series 1300mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 903,
        "weight_g": 160,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com/products/4-packs-cnhl-black-series-1300mah-14-8v-4s-100c-lipo-battery-with-xt60-plug",
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
        "id": "tattu-r-line-4-6s-1400mah",
        "category": "battery",
        "name": "R-Line 4.0 1400mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2711,
        "weight_g": 230,
        "in_stock": True,
        "buy_url": "https://genstattu.com/TA-RL4-130C-1400-6S1P",
        "color": "#cc0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── ADDITIONAL PARTS (6) ───────────────────────────────────────────────────
    {
        "id": "brotherhobby-avenger-2806-5-1700kv",
        "category": "motor",
        "name": "Avenger 2806.5 1700KV",
        "brand": "BrotherHobby",
        "price_php": 1525,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com/products/brotherhobby-avenger-2806-5-1300kv-1700kv-motor",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2806.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "speedybee-f405-v4-bls-60a-stack",
        "category": "fc",
        "name": "F405 V4 BLS 60A Stack",
        "brand": "SpeedyBee",
        "price_php": 4293,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/speedybee-f405-v4-bls-60a-30x30-fc-esc-stack/",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688-P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-ethix-s4-lemon-lime",
        "category": "propeller",
        "name": "Ethix S4 Lemon Lime 5×3.7×3",
        "brand": "HQProp",
        "price_php": 203,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://flyhighfpv.com/products/ethix-s4-props-lemon-lime-hqprop",
        "color": "#ccff00",
        "specs": {
            "diameter_inch": 5,
            "pitch": 3.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["lemon lime"]
        }
    },
    {
        "id": "caddx-ratel-2-pro",
        "category": "camera",
        "name": "Ratel 2 Pro",
        "brand": "Caddx",
        "price_php": 3367,
        "weight_g": 9.6,
        "in_stock": True,
        "buy_url": "https://www.diyfpv.com/catalog/caddx-ratel-2-pro-fpv-camera-for-drones",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" Starlight CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "radiomaster-rp1-v2-elrs-rx",
        "category": "receiver",
        "name": "RP1 V2 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 1288,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://radiomasterrc.com/products/rp1-expresslrs-2-4ghz-nano-receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "holybro-m9n-m10-gps-v2",
        "category": "gps",
        "name": "M9N & M10 GPS V2 (IP67)",
        "brand": "Holybro",
        "price_php": 2486,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://holybro.com/products/m9n-m10-gps-v2",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── RECEIVERS (2) ──────────────────────────────────────────────────────────
    {
        "id": "happymodel-ep2-elrs-rx",
        "category": "receiver",
        "name": "EP2 ELRS Receiver",
        "brand": "Happymodel",
        "price_php": 960,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com/products/happymodel-2-4g-expresslrs-ep2-tcxo-rx-receiver-module",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "radiomaster-er8-elrs-rx",
        "category": "receiver",
        "name": "ER8 ELRS PWM Receiver",
        "brand": "RadioMaster",
        "price_php": 903,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://radiomasterrc.com/products/er8-2-4ghz-elrs-pwm-receiver",
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
        "id": "holybro-micro-m8n-gps",
        "category": "gps",
        "name": "Micro M8N GPS Module",
        "brand": "Holybro",
        "price_php": 2141,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://holybro.com/products/micro-m8n-gps",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-5883-gnss-compass",
        "category": "gps",
        "name": "M10Q-5883 GNSS & Compass Module",
        "brand": "Matek",
        "price_php": 2259,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/mateksys-m10q-5883-gnss-compass.html",
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
        "id": "lumenier-axii2-long-range-antenna",
        "category": "antenna",
        "name": "AXII 2 Long Range 5.8GHz Antenna",
        "brand": "Lumenier",
        "price_php": 1836,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com/collections/antennas",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    },
    {
        "id": "truerc-xair-mk2-antenna",
        "category": "antenna",
        "name": "X-AIR MK II 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 2543,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/truerc-x-air-mk-ii-5-8ghz-antenna-for-dji-fpv-lhcp.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 9,
            "polarization": "LHCP",
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
