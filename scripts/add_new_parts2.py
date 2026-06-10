#!/usr/bin/env python3
"""Add a second batch of 33 new FPV parts (3 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (3) ─────────────────────────────────────────────────────────────
    {
        "id": "armattan-rooster-5-v2",
        "category": "frame",
        "name": "Rooster V2 5\" Freestyle",
        "brand": "Armattan",
        "price_php": 4200,
        "weight_g": 92,
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
            "standoff_height_mm": 30
        }
    },
    {
        "id": "flywoo-vampire2-hd-5",
        "category": "frame",
        "name": "Vampire2 HD 5\" Frame",
        "brand": "Flywoo",
        "price_php": 3192,
        "weight_g": 92,
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
        "id": "iflight-chimera7-frame",
        "category": "frame",
        "name": "Chimera7 Pro 7\" Long Range Frame",
        "brand": "iFlight",
        "price_php": 4845,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35
        }
    },

    # ─── MOTORS (3) ─────────────────────────────────────────────────────────────
    {
        "id": "tmotor-velox-v2306-v2",
        "category": "motor",
        "name": "Velox V2306 V2 1900KV",
        "brand": "T-Motor",
        "price_php": 1425,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "iflight-xing-e-pro-2306-v2",
        "category": "motor",
        "name": "XING-E Pro 2306 1700KV",
        "brand": "iFlight",
        "price_php": 1197,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "kv": 1700,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "emax-eco-ii-2306-2700kv",
        "category": "motor",
        "name": "ECO II 2306 2700KV",
        "brand": "Emax",
        "price_php": 855,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com",
        "color": "#1a0000",
        "specs": {
            "kv": 2700,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },

    # ─── ESC (3) ────────────────────────────────────────────────────────────────
    {
        "id": "tmotor-f55a-pro-iii",
        "category": "esc",
        "name": "F55A PRO III 4-in-1 50A",
        "brand": "T-Motor",
        "price_php": 3819,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "speedybee-bls-50a-4in1",
        "category": "esc",
        "name": "BLS 50A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2622,
        "weight_g": 23,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#002244",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "iflight-blitz-e55-v2",
        "category": "esc",
        "name": "BLITZ E55 V2 4-in-1 55A ESC",
        "brand": "iFlight",
        "price_php": 2964,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },

    # ─── FLIGHT CONTROLLERS (3) ─────────────────────────────────────────────────
    {
        "id": "speedybee-f405-v4-aio",
        "category": "fc",
        "name": "F405 V4 AIO Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2280,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#002244",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "mateksys-h743-slim",
        "category": "fc",
        "name": "H743 SLIM Flight Controller",
        "brand": "Matek",
        "price_php": 4674,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "ArduPilot",
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
        "id": "iflight-blitz-f745-v2",
        "category": "fc",
        "name": "BLITZ F745 AIO V2 Flight Controller",
        "brand": "iFlight",
        "price_php": 3078,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (3) ─────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-3018",
        "category": "propeller",
        "name": "Hurricane 3018 3-Blade",
        "brand": "Gemfan",
        "price_php": 165,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 3.0,
            "pitch": 1.8,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["black", "grey", "green"]
        }
    },
    {
        "id": "hqprop-7x4x2-v1s",
        "category": "propeller",
        "name": "7x4x2 V1S 2-Blade",
        "brand": "HQProp",
        "price_php": 285,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4.0,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "azure-power-2540-3blade",
        "category": "propeller",
        "name": "2540 3-Blade Whoop Props",
        "brand": "Azure Power",
        "price_php": 137,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 2.5,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["black", "white", "orange"]
        }
    },

    # ─── CAMERAS (3) ────────────────────────────────────────────────────────────
    {
        "id": "runcam-phoenix-2-special",
        "category": "camera",
        "name": "Phoenix 2 Special Edition 1000TVL",
        "brand": "RunCam",
        "price_php": 1881,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS Starlight",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ratel-2-pro",
        "category": "camera",
        "name": "Ratel 2 Pro 1/1.8\" Starlight",
        "brand": "Caddx",
        "price_php": 1995,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
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
        "id": "walksnail-avatar-hd-v2-cam",
        "category": "camera",
        "name": "Avatar HD V2 Camera",
        "brand": "Walksnail",
        "price_php": 4332,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "video_system": "Walksnail",
            "resolution": "1080p60fps",
            "voltage_range": "6-25V"
        }
    },

    # ─── VTX (3) ────────────────────────────────────────────────────────────────
    {
        "id": "rushfpv-vtx-max-solo",
        "category": "vtx",
        "name": "VTX MAX Solo 5.8G 1.6W",
        "brand": "RushFPV",
        "price_php": 3990,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
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
        "id": "tbs-unify-evo-hv",
        "category": "vtx",
        "name": "Unify Evo HV VTX",
        "brand": "TBS",
        "price_php": 3192,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#220000",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race band",
            "voltage_range": "7-36V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hdzero-whoop-vtx",
        "category": "vtx",
        "name": "Whoop VTX",
        "brand": "HDZero",
        "price_php": 2850,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com",
        "color": "#111111",
        "specs": {
            "power_mw_max": 200,
            "protocol": "Digital",
            "video_system": "HDZero",
            "voltage_range": "5V",
            "connector": "U.FL"
        }
    },

    # ─── BATTERIES (3) ──────────────────────────────────────────────────────────
    {
        "id": "tattu-rline-v5-4s-1300",
        "category": "battery",
        "name": "R-Line V5 4S 1300mAh 150C",
        "brand": "Tattu",
        "price_php": 2052,
        "weight_g": 172,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "cnhl-mini-tank-6s-1300",
        "category": "battery",
        "name": "MiniTank 6S 1300mAh 100C",
        "brand": "CNHL",
        "price_php": 2280,
        "weight_g": 240,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com",
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
        "id": "betafpv-3s-450mah-75c",
        "category": "battery",
        "name": "3S 450mAh 75C LiPo",
        "brand": "BetaFPV",
        "price_php": 456,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 450,
            "c_rating": 75,
            "connector": "XT30",
            "voltage_nominal": 11.1
        }
    },

    # ─── RECEIVERS (3) ──────────────────────────────────────────────────────────
    {
        "id": "radiomaster-er6-elrs",
        "category": "receiver",
        "name": "ER6 2.4GHz ELRS Diversity RX",
        "brand": "RadioMaster",
        "price_php": 1140,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "tbs-crossfire-nano-rx-se-v2",
        "category": "receiver",
        "name": "Crossfire Nano RX SE",
        "brand": "TBS",
        "price_php": 1710,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#220000",
        "specs": {
            "protocol": "TBS Crossfire",
            "frequency_mhz": 900,
            "diversity": False,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "happymodel-eplrs-pro-rx",
        "category": "receiver",
        "name": "EP2 2.4GHz ELRS RX",
        "brand": "Happymodel",
        "price_php": 684,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a0011",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 30
        }
    },

    # ─── GPS MODULES (3) ────────────────────────────────────────────────────────
    {
        "id": "holybro-m9n-gps-v2",
        "category": "gps",
        "name": "M9N GPS Module",
        "brand": "Holybro",
        "price_php": 2394,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 25,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "betafpv-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "BetaFPV",
        "price_php": 1140,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "constellation": "GPS+GLONASS+BDS",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "speedybee-m10-gps-pro",
        "category": "gps",
        "name": "u-blox M10 GPS Pro",
        "brand": "SpeedyBee",
        "price_php": 1254,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#002244",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 27,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },

    # ─── ANTENNAS (3) ───────────────────────────────────────────────────────────
    {
        "id": "tbs-triumph-rhcp",
        "category": "antenna",
        "name": "Triumph 5.8GHz RHCP Omni",
        "brand": "TBS",
        "price_php": 1026,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "rushfpv-x-air-2",
        "category": "antenna",
        "name": "X-AIR 2 5.8GHz RHCP",
        "brand": "RushFPV",
        "price_php": 969,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "menace-micro-stubby",
        "category": "antenna",
        "name": "Menace Micro Stubby 5.8GHz RHCP",
        "brand": "ImmersionRC",
        "price_php": 627,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.5,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "stubby"
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
