#!/usr/bin/env python3
"""Add a third batch of 33 new FPV parts (3 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (3) ─────────────────────────────────────────────────────────────
    {
        "id": "flywoo-mek5-v2",
        "category": "frame",
        "name": "MEK5 V2 5\" Freestyle Frame",
        "brand": "Flywoo",
        "price_php": 3192,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "lumenier-cl1-5",
        "category": "frame",
        "name": "CL1 5\" Freestyle Frame",
        "brand": "Lumenier",
        "price_php": 4104,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "geprc-cinelog35-v2",
        "category": "frame",
        "name": "CineLog35 V2 3.5\" Cinewhoop Frame",
        "brand": "GEPRC",
        "price_php": 2548,
        "weight_g": 64,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 153,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 20
        }
    },

    # ─── MOTORS (3) ─────────────────────────────────────────────────────────────
    {
        "id": "brotherhobby-avenger-2306.5-v4",
        "category": "motor",
        "name": "Avenger 2306.5 V4 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1454,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "flywoo-nin-2207-1750kv",
        "category": "motor",
        "name": "NIN 2207 1750KV",
        "brand": "Flywoo",
        "price_php": 1287,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "tmotor-pacer-p1604-3800kv",
        "category": "motor",
        "name": "Pacer P1604 3800KV",
        "brand": "T-Motor",
        "price_php": 1148,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 3800,
            "stator_size": "1604",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 3,
            "peak_current_a": 22
        }
    },

    # ─── ESCs (3) ───────────────────────────────────────────────────────────────
    {
        "id": "iflight-blitz-whoop-esc",
        "category": "esc",
        "name": "BLITZ Whoop 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 1850,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 25,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 30
        }
    },
    {
        "id": "tmotor-f45a-v2-4in1",
        "category": "esc",
        "name": "F45A V2 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 2950,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
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
        "id": "diatone-mamba-f25-4in1",
        "category": "esc",
        "name": "Mamba F25 25A 4-in-1 Mini ESC",
        "brand": "Diatone",
        "price_php": 1650,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002200",
        "specs": {
            "amp_rating": 25,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 30
        }
    },

    # ─── FLIGHT CONTROLLERS (3) ─────────────────────────────────────────────────
    {
        "id": "iflight-blitz-mini-f722-v2",
        "category": "fc",
        "name": "BLITZ Mini F722 V2",
        "brand": "iFlight",
        "price_php": 2750,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "speedybee-f745-aio-v2",
        "category": "fc",
        "name": "F745 AIO V2 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 3450,
        "weight_g": 13,
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
    {
        "id": "flywoo-goku-f405-hd-aio",
        "category": "fc",
        "name": "Goku F405 HD AIO",
        "brand": "Flywoo",
        "price_php": 2950,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
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

    # ─── PROPELLERS (3) ─────────────────────────────────────────────────────────
    {
        "id": "azurepower-falcon-5x4.3x3",
        "category": "propeller",
        "name": "Falcon 5x4.3x3",
        "brand": "Azure Power",
        "price_php": 240,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "orange"]
        }
    },
    {
        "id": "hqprop-dt5.1x4.6x3",
        "category": "propeller",
        "name": "DT 5.1x4.6x3 Durable Tri-Blade",
        "brand": "HQProp",
        "price_php": 260,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "grey"]
        }
    },
    {
        "id": "gemfan-f7-hurricane-7040",
        "category": "propeller",
        "name": "F7 Hurricane 7040 3-Blade",
        "brand": "Gemfan",
        "price_php": 320,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },

    # ─── FPV CAMERAS (3) ────────────────────────────────────────────────────────
    {
        "id": "walksnail-avatar-hd-camera-v3",
        "category": "camera",
        "name": "Avatar HD Camera V3",
        "brand": "Walksnail",
        "price_php": 5208,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" STARVIS2",
            "fov_deg": 155,
            "format": "Digital",
            "resolution": "1440p60",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "foxeer-box-v2",
        "category": "camera",
        "name": "Box V2 Action Camera",
        "brand": "Foxeer",
        "price_php": 3192,
        "weight_g": 50,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2.8\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-17V"
        }
    },
    {
        "id": "runcam-hybrid-3",
        "category": "camera",
        "name": "Hybrid 3 Analog/4K Camera",
        "brand": "RunCam",
        "price_php": 4095,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },

    # ─── VIDEO TRANSMITTERS (3) ─────────────────────────────────────────────────
    {
        "id": "walksnail-avatar-hd-vtx-v3",
        "category": "vtx",
        "name": "Avatar HD VTX V3",
        "brand": "Walksnail",
        "price_php": 5208,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital",
            "bands": "Walksnail",
            "voltage_range": "7.4-26.4V",
            "connector": "U.FL",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "foxeer-bayonet-vtx",
        "category": "vtx",
        "name": "Bayonet 5.8GHz VTX",
        "brand": "Foxeer",
        "price_php": 1750,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-transport-v2-vtx",
        "category": "vtx",
        "name": "TranspoRT V2 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 1900,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (3) ──────────────────────────────────────────────────────────
    {
        "id": "tattu-rline-4.0-6s-1300mah",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2450,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "authenticrc-4s-1300mah-100c",
        "category": "battery",
        "name": "1300mAh 4S 100C",
        "brand": "Authentic RC",
        "price_php": 1150,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "cnhl-ministar-v2-6s-1100mah",
        "category": "battery",
        "name": "MiniStar V2 1100mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1450,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── RC RECEIVERS (3) ───────────────────────────────────────────────────────
    {
        "id": "tbs-crossfire-diversity-nano-rx-se",
        "category": "receiver",
        "name": "Crossfire Diversity Nano RX SE",
        "brand": "TBS",
        "price_php": 2350,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "TBS Crossfire",
            "frequency_mhz": 915,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "betafpv-elrs-nano-rx-3.0",
        "category": "receiver",
        "name": "ELRS Nano RX 3.0",
        "brand": "BetaFPV",
        "price_php": 950,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "happymodel-ep2-plus-elrs",
        "category": "receiver",
        "name": "EP2 Plus ELRS 2.4GHz",
        "brand": "Happymodel",
        "price_php": 880,
        "weight_g": 1.3,
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

    # ─── GPS MODULES (3) ────────────────────────────────────────────────────────
    {
        "id": "betafpv-m10-gps-v2",
        "category": "gps",
        "name": "M10 GPS Module V2",
        "brand": "BetaFPV",
        "price_php": 1250,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m10-gps",
        "category": "gps",
        "name": "Micro M10 GPS",
        "brand": "Holybro",
        "price_php": 1300,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://holybro.com",
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
        "id": "matek-m10q-5883-v2",
        "category": "gps",
        "name": "M10Q-5883 V2 GPS+Compass",
        "brand": "Matek",
        "price_php": 1450,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (3) ───────────────────────────────────────────────────────
    {
        "id": "axisflying-pagoda-pro-5.8",
        "category": "antenna",
        "name": "Pagoda Pro 5.8GHz",
        "brand": "AxisFlying",
        "price_php": 1150,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
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
        "id": "realacc-triumph-5.8",
        "category": "antenna",
        "name": "Triumph 5.8GHz",
        "brand": "Realacc",
        "price_php": 850,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    },
    {
        "id": "immersionrc-skew-planar-5.8",
        "category": "antenna",
        "name": "Skew Planar 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 1650,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3,
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
