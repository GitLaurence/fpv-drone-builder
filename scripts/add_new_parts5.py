#!/usr/bin/env python3
"""Add a fifth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "geprc-domain3-6-frame",
        "category": "frame",
        "name": "DoMain3.6 Frame Kit",
        "brand": "GEPRC",
        "price_php": 3192,
        "weight_g": 110,
        "in_stock": True,
        "buy_url": "https://geprc.com/product/gep-domain3-6-frame/",
        "color": "#9a9a9a",
        "specs": {
            "size_mm": 170,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3.6,
            "stack_mount_mm": 25.5,
            "material": "aluminum alloy",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "flywoo-explorer-lr7-v2",
        "category": "frame",
        "name": "Explorer LR7 V2 7\" Long Range Frame",
        "brand": "Flywoo",
        "price_php": 3360,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "brotherhobby-avenger-2812-1300kv",
        "category": "motor",
        "name": "Avenger 2812.5 1300KV",
        "brand": "BrotherHobby",
        "price_php": 1680,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1300,
            "stator_size": "2812",
            "motor_mount_mm": 25,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 30
        }
    },
    {
        "id": "tmotor-velox-v3-2807-1300kv",
        "category": "motor",
        "name": "Velox V3 2807.5 1300KV",
        "brand": "T-Motor",
        "price_php": 1960,
        "weight_g": 48,
        "in_stock": True,
        "buy_url": "https://www.tmotor.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 25,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 32
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "diatone-mamba-f60-pro-60a-4in1",
        "category": "esc",
        "name": "Mamba F60 Pro 60A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 3080,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
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
        "id": "speedybee-bl32-35a-4in1-20x20",
        "category": "esc",
        "name": "BL32 35A 4-in-1 ESC 20x20",
        "brand": "SpeedyBee",
        "price_php": 1736,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 35,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 40
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ─────────────────────────────────────────────────
    {
        "id": "diatone-mamba-h743-v2",
        "category": "fc",
        "name": "Mamba H743 V2 Flight Controller",
        "brand": "Diatone",
        "price_php": 4480,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002200",
        "specs": {
            "gyro": "ICM42688-P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },
    {
        "id": "flywoo-goku-f745-aio-v2",
        "category": "fc",
        "name": "GOKU F745 AIO V2 Flight Controller",
        "brand": "Flywoo",
        "price_php": 3640,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#002200",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-51499-4blade",
        "category": "propeller",
        "name": "Hurricane 51499 4-Blade",
        "brand": "Gemfan",
        "price_php": 224,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.99,
            "blade_count": 4,
            "shaft_mm": 5
        }
    },
    {
        "id": "hqprop-ethix-s5-pro-v2",
        "category": "propeller",
        "name": "Ethix S5 Pro V2",
        "brand": "HQProp",
        "price_php": 280,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#3a3a3a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },

    # ─── CAMERAS (2) ────────────────────────────────────────────────────────────
    {
        "id": "caddx-ratel-2x-pro-2026",
        "category": "camera",
        "name": "Ratel 2X Pro",
        "brand": "Caddx",
        "price_php": 1736,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.caddxfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS Starlight",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-walnut-digital-cam",
        "category": "camera",
        "name": "Walnut Digital HD Camera",
        "brand": "Caddx",
        "price_php": 2576,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.caddxfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 155,
            "format": "Digital",
            "resolution": "1080p60",
            "voltage_range": "6-25.2V",
            "video_system": "Walksnail"
        }
    },

    # ─── VTX (2) ────────────────────────────────────────────────────────────────
    {
        "id": "rushfpv-tank-max-2-vtx",
        "category": "vtx",
        "name": "Tank Max 2.0 VTX",
        "brand": "RushFPV",
        "price_php": 1904,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://rushfpv.net",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Raceband",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tbs-unify-pro-5g8-hv",
        "category": "vtx",
        "name": "Unify Pro 5G8 HV VTX",
        "brand": "TBS",
        "price_php": 1568,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Raceband",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "betafpv-lava-1s-260mah",
        "category": "battery",
        "name": "LAVA 1S 260mAh 80C",
        "brand": "BetaFPV",
        "price_php": 504,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#ff4500",
        "specs": {
            "cell_count_s": 1,
            "capacity_mah": 260,
            "c_rating": 80,
            "connector": "PH2.0",
            "voltage_nominal": 3.7
        }
    },
    {
        "id": "betafpv-lava-4s-850mah",
        "category": "battery",
        "name": "LAVA 4S 850mAh 100C",
        "brand": "BetaFPV",
        "price_php": 1736,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#ff4500",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 850,
            "c_rating": 100,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },

    # ─── RECEIVERS (2) ──────────────────────────────────────────────────────────
    {
        "id": "radiomaster-er6g-elrs-pwm",
        "category": "receiver",
        "name": "ER6G 2.4GHz ELRS PWM Receiver",
        "brand": "RadioMaster",
        "price_php": 728,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://radiomasterrc.com",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "betafpv-elrs-nano-rx-pro",
        "category": "receiver",
        "name": "ELRS Nano RX Pro",
        "brand": "BetaFPV",
        "price_php": 728,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "holybro-m9n-ubx-gps",
        "category": "gps",
        "name": "M9N-UBX GPS Module",
        "brand": "Holybro",
        "price_php": 2576,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 25,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "holybro-m10-pro-gps-2026",
        "category": "gps",
        "name": "M10 Pro GPS Module",
        "brand": "Holybro",
        "price_php": 1568,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },

    # ─── ANTENNAS (2) ───────────────────────────────────────────────────────────
    {
        "id": "foxeer-lollipop-5-5g8",
        "category": "antenna",
        "name": "Lollipop 5 5.8GHz",
        "brand": "Foxeer",
        "price_php": 560,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "truerc-x-air-2-4ghz",
        "category": "antenna",
        "name": "X-Air 2.4GHz ELRS",
        "brand": "TrueRC",
        "price_php": 952,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 2400,
            "gain_dbi": 4.5,
            "polarization": "linear",
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
    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"SKIP (duplicate id): {part['id']}")
            continue
        data["parts"].append(part)
        added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added {added} new parts. Total parts: {len(data['parts'])}")


if __name__ == "__main__":
    main()
