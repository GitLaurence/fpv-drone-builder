#!/usr/bin/env python3
"""Add 22 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────
    {
        "id": "flywoo-firefly-baby-quad-nano-3",
        "category": "frame",
        "name": "Firefly Baby Quad Nano 3\"",
        "brand": "Flywoo",
        "price_php": 1450,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 130,
            "motor_mount_mm": 13,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 16,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 18,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+firefly+baby+quad"
        }
    },
    {
        "id": "axisflying-manta-7-lr",
        "category": "frame",
        "name": "Manta 7\" Long Range",
        "brand": "AxisFlying",
        "price_php": 5200,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 300,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+manta+7"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────
    {
        "id": "betafpv-1404-4500kv-v4",
        "category": "motor",
        "name": "1404 4500KV V4",
        "brand": "BetaFPV",
        "price_php": 620,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 4500,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 18
        }
    },
    {
        "id": "iflight-xing-e-pro-2207-1960kv",
        "category": "motor",
        "name": "XING-E Pro 2207 1960KV",
        "brand": "iFlight",
        "price_php": 1450,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1960,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },

    # ─── ESC (2) ────────────────────────────────────────────────────────────
    {
        "id": "tmotor-f45a-mini-v2",
        "category": "esc",
        "name": "F45A Mini V2 4-in-1",
        "brand": "T-Motor",
        "price_php": 3200,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "flywoo-goku-60a-x4",
        "category": "esc",
        "name": "GOKU 60A X4 4-in-1",
        "brand": "Flywoo",
        "price_php": 3850,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ────────────────────────────────────────────
    {
        "id": "flywoo-goku-f745-aio-v2",
        "category": "fc",
        "name": "GOKU F745 AIO V2",
        "brand": "Flywoo",
        "price_php": 4200,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
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
        "id": "betafpv-f4-2-3s-aio",
        "category": "fc",
        "name": "F4 2-3S AIO Brushless FC",
        "brand": "BetaFPV",
        "price_php": 1350,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 16,
            "stack_mount_mm": 16,
            "barometer": False,
            "blackbox": False,
            "uart_count": 3,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────
    {
        "id": "gemfan-71433-tri-blade",
        "category": "propeller",
        "name": "71433 Tri-Blade",
        "brand": "Gemfan",
        "price_php": 195,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 2.8,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": [
                "gray",
                "green",
                "purple"
            ]
        }
    },
    {
        "id": "hqprop-7x4x3-bullnose",
        "category": "propeller",
        "name": "7X4X3 Bullnose",
        "brand": "HQProp",
        "price_php": 380,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray"
            ]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────
    {
        "id": "walksnail-avatar-hd-v3",
        "category": "camera",
        "name": "Avatar HD V3 Camera",
        "brand": "Walksnail",
        "price_php": 3800,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "resolution": "1080p60",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "runcam-hybrid-3",
        "category": "camera",
        "name": "Hybrid 3",
        "brand": "RunCam",
        "price_php": 4480,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 145,
            "format": "Analog + DVR",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },

    # ─── VIDEO TRANSMITTERS (2) ─────────────────────────────────────────────
    {
        "id": "walksnail-avatar-hd-vtx-v3",
        "category": "vtx",
        "name": "Avatar HD VTX V3",
        "brand": "Walksnail",
        "price_php": 4500,
        "weight_g": 9,
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
        "id": "hdzero-race-vtx-v2",
        "category": "vtx",
        "name": "Race VTX V2",
        "brand": "HDZero",
        "price_php": 3360,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Digital",
            "bands": "HDZero",
            "voltage_range": "7.4-26.4V",
            "connector": "U.FL",
            "video_system": "HDZero"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────
    {
        "id": "cnhl-black-series-2200mah-6s",
        "category": "battery",
        "name": "Black Series 2200mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2100,
        "weight_g": 295,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 2200,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-rline-3-1400mah-6s",
        "category": "battery",
        "name": "R-Line V3 1400mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2950,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────
    {
        "id": "happymodel-ep2-elrs-2.4g",
        "category": "receiver",
        "name": "EP2 ELRS 2.4GHz Nano RX",
        "brand": "Happymodel",
        "price_php": 750,
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
        "id": "radiomaster-rp4tg-elrs",
        "category": "receiver",
        "name": "RP4TG ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 980,
        "weight_g": 2.1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 35
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────
    {
        "id": "holybro-st-m9n-gps",
        "category": "gps",
        "name": "ST M9N GPS",
        "brand": "Holybro",
        "price_php": 2400,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#222",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 25,
            "fix_time_s": 20,
            "compass": True,
            "connector": "GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-l1l5",
        "category": "gps",
        "name": "M10Q-L1L5 GPS+Compass",
        "brand": "Matek",
        "price_php": 1800,
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

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────
    {
        "id": "rushfpv-cherry-lite-mmcx",
        "category": "antenna",
        "name": "Cherry Lite 5.8GHz MMCX",
        "brand": "RushFPV",
        "price_php": 450,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#cc0000",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "foxeer-lollipop-3-rhcp",
        "category": "antenna",
        "name": "Lollipop 3 5.8GHz RHCP",
        "brand": "Foxeer",
        "price_php": 380,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.1,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
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
