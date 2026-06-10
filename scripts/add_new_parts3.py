#!/usr/bin/env python3
"""Add a third batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "armattan-wraith-5",
        "category": "frame",
        "name": "Wraith 5\" Freestyle Frame",
        "brand": "Armattan",
        "price_php": 5400,
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
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+wraith"
        }
    },
    {
        "id": "tbs-source-one-v5-5",
        "category": "frame",
        "name": "Source One V5 5\" Frame",
        "brand": "TBS",
        "price_php": 1450,
        "weight_g": 85,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+v5"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "xnova-lightning-2208-2150kv",
        "category": "motor",
        "name": "Lightning 2208 2150KV",
        "brand": "Xnova",
        "price_php": 1750,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2150,
            "stator_size": "2208",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "emax-eco-micro-1404-4500kv",
        "category": "motor",
        "name": "ECO Micro 1404 4500KV",
        "brand": "Emax",
        "price_php": 650,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://emax-usa.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 4500,
            "stator_size": "1404",
            "motor_mount_mm": 16,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 20
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "hglrc-aos-50a-4in1",
        "category": "esc",
        "name": "AOS 50A 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 2000,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": "3-6S",
            "protocol": "DShot600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "holybro-tekko32-f4-50a-4in1-30x30",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 (30x30)",
        "brand": "Holybro",
        "price_php": 2300,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": "3-6S",
            "protocol": "DShot600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ────────────────────────────────────────────────
    {
        "id": "foxeer-f722-v4-stack",
        "category": "fc",
        "name": "F722 V4 Stack FC",
        "brand": "Foxeer",
        "price_php": 2300,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM42688-P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.foxeer.com"
        }
    },
    {
        "id": "speedybee-f745-v4-stack",
        "category": "fc",
        "name": "F745 V4 Stack FC",
        "brand": "SpeedyBee",
        "price_php": 2600,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com"
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "gemfan-f5048-5-blade",
        "category": "propeller",
        "name": "F5048 5-Blade",
        "brand": "Gemfan",
        "price_php": 195,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 5,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "transparent"]
        }
    },
    {
        "id": "hqprop-dp5x4.3x3-v1s",
        "category": "propeller",
        "name": "DP 5x4.3x3 V1S",
        "brand": "HQProp",
        "price_php": 185,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "blue"]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────────
    {
        "id": "caddx-polar-vista-digital-camera",
        "category": "camera",
        "name": "Polar Vista Digital Camera",
        "brand": "Caddx",
        "price_php": 2300,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "tvl": 1000,
            "voltage_range": "6.5-25V"
        }
    },
    {
        "id": "runcam-night-eagle-3-pro",
        "category": "camera",
        "name": "Night Eagle 3 Pro",
        "brand": "RunCam",
        "price_php": 1900,
        "weight_g": 7.8,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },

    # ─── VIDEO TRANSMITTERS (2) ─────────────────────────────────────────────────
    {
        "id": "rush-tank-solo",
        "category": "vtx",
        "name": "Tank Solo VTX",
        "brand": "Rush",
        "price_php": 1450,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-sky-1.6w-vtx",
        "category": "vtx",
        "name": "Sky 1.6W VTX",
        "brand": "HGLRC",
        "price_php": 3400,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "cnhl-black-series-4s-1500mah-100c",
        "category": "battery",
        "name": "Black Series 4S 1500mAh 100C",
        "brand": "CNHL",
        "price_php": 1050,
        "weight_g": 172,
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
        "id": "authenticrc-pulse-4s-1400mah-100c",
        "category": "battery",
        "name": "Pulse 4S 1400mAh 100C",
        "brand": "Authentic RC",
        "price_php": 1100,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://authentic-rc.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1400,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────────
    {
        "id": "radiomaster-rp1-elrs-nano",
        "category": "receiver",
        "name": "RP1 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 580,
        "weight_g": 1,
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
    {
        "id": "tbs-tracer-diversity-rx",
        "category": "receiver",
        "name": "Tracer Diversity Receiver",
        "brand": "TBS",
        "price_php": 1700,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Tracer",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "matek-m10q-5883-v2",
        "category": "gps",
        "name": "M10Q-5883 V2 GPS+Compass",
        "brand": "Matek",
        "price_php": 1300,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-5883",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "geprc-gep-m10-mini-gps",
        "category": "gps",
        "name": "GEP-M10 Mini GPS",
        "brand": "GEPRC",
        "price_php": 850,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },

    # ─── ANTENNAS (2) ───────────────────────────────────────────────────────────
    {
        "id": "truerc-stubby-se-5.8",
        "category": "antenna",
        "name": "Stubby SE 5.8GHz",
        "brand": "TrueRC",
        "price_php": 870,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://truerc.ca",
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
        "id": "truerc-singularity-stubby-5.8",
        "category": "antenna",
        "name": "Singularity Stubby 5.8GHz",
        "brand": "TrueRC",
        "price_php": 980,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://truerc.ca",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.5,
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
    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            raise ValueError(f"Duplicate id: {part['id']}")

    data["parts"].extend(NEW_PARTS)

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=True)
        f.write("\n")

    print(f"Added {len(NEW_PARTS)} new parts. Total parts: {len(data['parts'])}")


if __name__ == "__main__":
    main()
