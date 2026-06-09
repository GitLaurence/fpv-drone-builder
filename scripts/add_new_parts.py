#!/usr/bin/env python3
"""Add 110 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (10) ───────────────────────────────────────────────────────────
    {
        "id": "lumenier-qav-rzr-5",
        "category": "frame",
        "name": "QAV-RZR 5\" Freestyle",
        "brand": "Lumenier",
        "price_php": 4560,
        "weight_g": 58,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#0a0a0a",
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
        "id": "diatone-roma-l5-v3",
        "category": "frame",
        "name": "Roma L5 V3 5\"",
        "brand": "Diatone",
        "price_php": 2736,
        "weight_g": 72,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 218,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 28
        }
    },
    {
        "id": "rdq-mach5-framekit",
        "category": "frame",
        "name": "Mach 5 Race Frame",
        "brand": "RaceDayQuads",
        "price_php": 2565,
        "weight_g": 65,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#141414",
        "specs": {
            "size_mm": 212,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "betafpv-x-knight-5",
        "category": "frame",
        "name": "X-Knight 5\" Freestyle",
        "brand": "BetaFPV",
        "price_php": 1824,
        "weight_g": 70,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "flywoo-mr-croc-5-hd",
        "category": "frame",
        "name": "MrCroc 5\" HD",
        "brand": "Flywoo",
        "price_php": 3021,
        "weight_g": 66,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
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
        "id": "skystars-goblin-5",
        "category": "frame",
        "name": "Goblin 5\" Freestyle",
        "brand": "Skystars",
        "price_php": 1995,
        "weight_g": 74,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#222222",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "rotor-riot-siren-5",
        "category": "frame",
        "name": "Siren 5\" Freestyle",
        "brand": "Rotor Riot",
        "price_php": 4560,
        "weight_g": 60,
        "in_stock": True,
        "buy_url": "https://rotorriot.com",
        "color": "#1a0000",
        "specs": {
            "size_mm": 218,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "rekon-5-hd-frame",
        "category": "frame",
        "name": "Rekon 5 HD Long Range",
        "brand": "GEPRC",
        "price_php": 3705,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#161616",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "geprc-cinelog25-v3",
        "category": "frame",
        "name": "CineLog25 V3 2.5\" Cinewhoop",
        "brand": "GEPRC",
        "price_php": 2622,
        "weight_g": 55,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 112,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 20
        }
    },
    {
        "id": "iflight-evoque-f5x-v2",
        "category": "frame",
        "name": "Nazgul Evoque F5X V2 5\"",
        "brand": "iFlight",
        "price_php": 3534,
        "weight_g": 74,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
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

    # ─── MOTORS (10) ───────────────────────────────────────────────────────────
    {
        "id": "flywoo-ninja-2305",
        "category": "motor",
        "name": "NINJA 2305.5 2000KV",
        "brand": "Flywoo",
        "price_php": 1140,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a2e",
        "specs": {
            "kv": 2000,
            "stator_size": "2305",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "racerstar-mr2306-2400kv",
        "category": "motor",
        "name": "MR2306 2400KV",
        "brand": "Racerstar",
        "price_php": 513,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#2a0a0a",
        "specs": {
            "kv": 2400,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "hglrc-specter-2207-1750kv",
        "category": "motor",
        "name": "Specter 2207 1750KV",
        "brand": "HGLRC",
        "price_php": 1140,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "betafpv-1105-5000kv",
        "category": "motor",
        "name": "1105 5000KV Micro Brushless",
        "brand": "BetaFPV",
        "price_php": 741,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "kv": 5000,
            "stator_size": "1105",
            "motor_mount_mm": 16,
            "min_voltage_s": 2,
            "max_voltage_s": 3,
            "shaft_mm": 2,
            "peak_current_a": 12
        }
    },
    {
        "id": "xnova-2207-2450kv",
        "category": "motor",
        "name": "Thunderbolt 2207 2450KV",
        "brand": "Xnova",
        "price_php": 1596,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.xnovamotor.com",
        "color": "#1a2a1a",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 46
        }
    },
    {
        "id": "geprc-gr2207-5-1750kv",
        "category": "motor",
        "name": "GR2207.5 1750KV Speed",
        "brand": "GEPRC",
        "price_php": 1083,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#002200",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 46
        }
    },
    {
        "id": "emax-rs3108-900kv",
        "category": "motor",
        "name": "RS3108 900KV Long Range",
        "brand": "Emax",
        "price_php": 1197,
        "weight_g": 41,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com",
        "color": "#1a0000",
        "specs": {
            "kv": 900,
            "stator_size": "3108",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "brotherhobby-returner-r5-2207",
        "category": "motor",
        "name": "Returner R5 2207 1700KV",
        "brand": "BrotherHobby",
        "price_php": 1254,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#001a22",
        "specs": {
            "kv": 1700,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 43
        }
    },
    {
        "id": "dys-samguk-2306-2550kv",
        "category": "motor",
        "name": "Samguk Wei 2306 2550KV",
        "brand": "DYS",
        "price_php": 912,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#002222",
        "specs": {
            "kv": 2550,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "azure-power-2207-1750kv",
        "category": "motor",
        "name": "AP Silk 2207 1750KV",
        "brand": "Azure Power",
        "price_php": 1368,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#00001a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 43
        }
    },

    # ─── ESC (10) ──────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f3-65a",
        "category": "esc",
        "name": "Tekko32 F3 Metal 65A 4-in-1",
        "brand": "Holybro",
        "price_php": 4560,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#004400",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 80
        }
    },
    {
        "id": "hobbywing-xrotor-pro-45a",
        "category": "esc",
        "name": "XRotor Pro 4-in-1 45A",
        "brand": "Hobbywing",
        "price_php": 3420,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.hobbywing.com",
        "color": "#220022",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "diatone-mamba-f60-mk2",
        "category": "esc",
        "name": "Mamba F60 Mk2 60A 4-in-1",
        "brand": "Diatone",
        "price_php": 3990,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002222",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "betafpv-f4-nano-12a",
        "category": "esc",
        "name": "F4 Nano 12A 4-in-1",
        "brand": "BetaFPV",
        "price_php": 1311,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "amp_rating": 12,
            "input_voltage_s": 4,
            "protocol": "DSHOT300",
            "form_factor_mm": 20,
            "burst_amp": 15
        }
    },
    {
        "id": "airbot-wraith32-55a-v3",
        "category": "esc",
        "name": "WRAITH32 55A V3 4-in-1",
        "brand": "Airbot",
        "price_php": 3591,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.airbot-systems.com",
        "color": "#220000",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "flycolor-raptor-390-45a",
        "category": "esc",
        "name": "Raptor 390 45A 4-in-1",
        "brand": "Flycolor",
        "price_php": 2280,
        "weight_g": 21,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#001a00",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "jhemcu-blheli32-60a-4in1",
        "category": "esc",
        "name": "BLHeli_32 60A 4-in-1",
        "brand": "JHEMCU",
        "price_php": 3135,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#001a1a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "spedix-gs30a-4in1",
        "category": "esc",
        "name": "GS30A 4-in-1 BLHeli_32",
        "brand": "Spedix",
        "price_php": 2280,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0011",
        "specs": {
            "amp_rating": 30,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 40
        }
    },
    {
        "id": "diatone-mamba-f40-4in1",
        "category": "esc",
        "name": "Mamba F40 4-in-1 BLHeli_32",
        "brand": "Diatone",
        "price_php": 2736,
        "weight_g": 20,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002222",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 50
        }
    },
    {
        "id": "skystars-star-f7-45a",
        "category": "esc",
        "name": "Star F7 45A 4-in-1",
        "brand": "Skystars",
        "price_php": 3306,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#001122",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },

    # ─── FLIGHT CONTROLLERS (10) ───────────────────────────────────────────────
    {
        "id": "geprc-taker-f411-mini",
        "category": "fc",
        "name": "TAKER F411 Mini AIO",
        "brand": "GEPRC",
        "price_php": 2736,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#002200",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "tmotor-f7-fc",
        "category": "fc",
        "name": "F7 Flight Controller",
        "brand": "T-Motor",
        "price_php": 3648,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "hglrc-zeus-f7-mini",
        "category": "fc",
        "name": "Zeus F7 Mini FC",
        "brand": "HGLRC",
        "price_php": 3990,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 25,
            "stack_mount_mm": 25,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "betafpv-f7-pro-fc",
        "category": "fc",
        "name": "F7 Pro 30x30 Flight Controller",
        "brand": "BetaFPV",
        "price_php": 3192,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "foxeer-reaper-f7-pro",
        "category": "fc",
        "name": "Reaper F7 Pro FC",
        "brand": "Foxeer",
        "price_php": 3876,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#220000",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "lumenier-mini-f4-fc",
        "category": "fc",
        "name": "Mini F4 Flight Controller",
        "brand": "Lumenier",
        "price_php": 3705,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#001a00",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "jhemcu-ghf411-aio-2s",
        "category": "fc",
        "name": "GHF411 AIO 2S Whoop FC",
        "brand": "JHEMCU",
        "price_php": 1254,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#001a1a",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": False,
            "uart_count": 3,
            "5v_pad_count": 1,
            "curr_sensor": False
        }
    },
    {
        "id": "axisflying-af6-f4-mini",
        "category": "fc",
        "name": "AF6 F4 Mini FC",
        "brand": "AxisFlying",
        "price_php": 3135,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a0022",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "holybro-pix32-v6-fc",
        "category": "fc",
        "name": "Pix32 V6 ArduPilot/PX4",
        "brand": "Holybro",
        "price_php": 4845,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#002244",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "ArduPilot",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 4,
            "curr_sensor": True,
            "diagram_url": "https://docs.holybro.com/autopilot/pix32-v6"
        }
    },
    {
        "id": "radiomaster-nexus-f4-aio",
        "category": "fc",
        "name": "Nexus F4 AIO Flight Controller",
        "brand": "Radiomaster",
        "price_php": 3306,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (10) ───────────────────────────────────────────────────────
    {
        "id": "gemfan-51466-v2-3blade",
        "category": "propeller",
        "name": "51466 V2 3-Blade Freestyle",
        "brand": "Gemfan",
        "price_php": 251,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.66,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "orange", "blue"]
        }
    },
    {
        "id": "hqprop-5152-v1s",
        "category": "propeller",
        "name": "5.1x5.2x3 V1S 3-Blade",
        "brand": "HQProp",
        "price_php": 222,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "blue", "red"]
        }
    },
    {
        "id": "dalcyclone-t5147-3blade",
        "category": "propeller",
        "name": "Cyclone T5147 3-Blade",
        "brand": "DAL",
        "price_php": 194,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "smoke", "orange"]
        }
    },
    {
        "id": "ethix-stingy-5150",
        "category": "propeller",
        "name": "Mr Steele Stingy 5150 3-Blade",
        "brand": "Ethix",
        "price_php": 251,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "green"]
        }
    },
    {
        "id": "master-airscrew-5040-3blade",
        "category": "propeller",
        "name": "5040 3-Blade Bullnose",
        "brand": "Master Airscrew",
        "price_php": 194,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.masterairscrew.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white"]
        }
    },
    {
        "id": "tmotor-t6143-cinema",
        "category": "propeller",
        "name": "T6143 6\" Cinema 3-Blade",
        "brand": "T-Motor",
        "price_php": 308,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    {
        "id": "gemfan-6040-3blade",
        "category": "propeller",
        "name": "6040 6\" 3-Blade Long Range",
        "brand": "Gemfan",
        "price_php": 279,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "hqprop-6x4x3-6inch",
        "category": "propeller",
        "name": "6x4x3 6\" 3-Blade",
        "brand": "HQProp",
        "price_php": 251,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "blue"]
        }
    },
    {
        "id": "azure-power-51533-race",
        "category": "propeller",
        "name": "51533 3-Blade Race",
        "brand": "Azure Power",
        "price_php": 251,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "red"]
        }
    },
    {
        "id": "betafpv-75mm-3blade",
        "category": "propeller",
        "name": "75mm 3-Blade Whoop Props",
        "brand": "BetaFPV",
        "price_php": 142,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 2.95,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 2,
            "color_options": ["black", "white", "yellow", "pink"]
        }
    },

    # ─── CAMERAS (10) ──────────────────────────────────────────────────────────
    {
        "id": "runcam-thumb-pro-4k",
        "category": "camera",
        "name": "Thumb Pro 4K Action",
        "brand": "RunCam",
        "price_php": 5472,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2.3\" CMOS",
            "fov_deg": 150,
            "format": "HD Action",
            "resolution": "4K@30fps",
            "voltage_range": "5V USB-C"
        }
    },
    {
        "id": "caddx-peanut-4k",
        "category": "camera",
        "name": "Peanut 4K Action Camera",
        "brand": "Caddx",
        "price_php": 6840,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2.3\" CMOS",
            "fov_deg": 170,
            "format": "HD Action",
            "resolution": "4K@30fps",
            "voltage_range": "5V USB-C"
        }
    },
    {
        "id": "walksnail-avatar-pro-kit",
        "category": "camera",
        "name": "Avatar Pro Full Kit",
        "brand": "Walksnail",
        "price_php": 13680,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "video_system": "Walksnail",
            "resolution": "1080p60fps",
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "hdzero-freestyle-v3",
        "category": "camera",
        "name": "Freestyle V3 Digital Camera",
        "brand": "HDZero",
        "price_php": 8208,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2.3\" CMOS",
            "fov_deg": 140,
            "format": "Digital",
            "video_system": "HDZero",
            "resolution": "1080p60fps",
            "voltage_range": "5V"
        }
    },
    {
        "id": "foxeer-mix-4",
        "category": "camera",
        "name": "Mix 4 FPV 1200TVL",
        "brand": "Foxeer",
        "price_php": 1596,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ant-starlight",
        "category": "camera",
        "name": "Ant Starlight 1200TVL Nano",
        "brand": "Caddx",
        "price_php": 1254,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" STARVIS",
            "fov_deg": 170,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "dji-o4-pro-air-unit",
        "category": "camera",
        "name": "O4 Pro Air Unit",
        "brand": "DJI",
        "price_php": 15960,
        "weight_g": 35,
        "in_stock": True,
        "buy_url": "https://www.dji.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.3\" CMOS",
            "fov_deg": 155,
            "format": "Digital",
            "video_system": "DJI O4",
            "resolution": "4K@60fps",
            "voltage_range": "7.2-26V"
        }
    },
    {
        "id": "walksnail-avatar-micro-v3",
        "category": "camera",
        "name": "Avatar Micro V3 Kit",
        "brand": "Walksnail",
        "price_php": 10260,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2.7\" CMOS",
            "fov_deg": 155,
            "format": "Digital",
            "video_system": "Walksnail",
            "resolution": "1080p60fps",
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "betafpv-c01-analog",
        "category": "camera",
        "name": "C01 1200TVL Analog Nano",
        "brand": "BetaFPV",
        "price_php": 912,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-falkor-3-nano",
        "category": "camera",
        "name": "Falkor 3 Nano 1200TVL",
        "brand": "Foxeer",
        "price_php": 1482,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },

    # ─── VTX (10) ──────────────────────────────────────────────────────────────
    {
        "id": "foxeer-reaper-extreme",
        "category": "vtx",
        "name": "Reaper Extreme 2.5W VTX",
        "brand": "Foxeer",
        "price_php": 3420,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#220000",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "vifly-tx100-25mw",
        "category": "vtx",
        "name": "TX100 25mW Nano VTX",
        "brand": "Vifly",
        "price_php": 684,
        "weight_g": 2.5,
        "in_stock": True,
        "buy_url": "https://viflydrone.com",
        "color": "#111111",
        "specs": {
            "power_mw_max": 25,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-9V",
            "connector": "U.FL"
        }
    },
    {
        "id": "caddx-vista-digital-vtx",
        "category": "vtx",
        "name": "Vista Digital HD VTX",
        "brand": "Caddx",
        "price_php": 8550,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111111",
        "specs": {
            "power_mw_max": 700,
            "protocol": "Digital",
            "video_system": "DJI",
            "voltage_range": "7.4-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-zeus-2000mw",
        "category": "vtx",
        "name": "Zeus 2000mW 5.8G VTX",
        "brand": "HGLRC",
        "price_php": 2736,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "power_mw_max": 2000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },
    {
        "id": "foxeer-echo-600mw",
        "category": "vtx",
        "name": "Echo 5.8G 600mW VTX",
        "brand": "Foxeer",
        "price_php": 1596,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#220000",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-36V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rushfpv-tiny-tank",
        "category": "vtx",
        "name": "Tiny Tank 200mW 5.8G VTX",
        "brand": "RushFPV",
        "price_php": 1140,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-9V",
            "connector": "U.FL"
        }
    },
    {
        "id": "matek-vtx-h3433",
        "category": "vtx",
        "name": "VTX-H3433 5.8G 25-800mW",
        "brand": "Matek",
        "price_php": 1995,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "5-36V",
            "connector": "MMCX"
        }
    },
    {
        "id": "rush-tank-race-v2",
        "category": "vtx",
        "name": "Tank Race V2 5.8G 1W VTX",
        "brand": "Rush",
        "price_php": 2565,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },
    {
        "id": "dji-o3-vtx-module",
        "category": "vtx",
        "name": "O3 Air Unit Digital VTX",
        "brand": "DJI",
        "price_php": 10260,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://www.dji.com",
        "color": "#111111",
        "specs": {
            "power_mw_max": 700,
            "protocol": "Digital",
            "video_system": "DJI",
            "voltage_range": "7.2-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-zeus-3000mw",
        "category": "vtx",
        "name": "Zeus 3000mW 5.8G VTX",
        "brand": "HGLRC",
        "price_php": 3306,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "power_mw_max": 3000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },

    # ─── BATTERIES (10) ────────────────────────────────────────────────────────
    {
        "id": "gnb-hv-4s-1400mah",
        "category": "battery",
        "name": "4S 1400mAh 100C LiHV",
        "brand": "GNB",
        "price_php": 1482,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1400,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 15.2
        }
    },
    {
        "id": "rdq-sessanta-6s-1050mah",
        "category": "battery",
        "name": "Sessanta 6S 1050mAh 110C",
        "brand": "RDQ",
        "price_php": 2508,
        "weight_g": 198,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#001a00",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1050,
            "c_rating": 110,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "pyrodrone-4s-1500mah",
        "category": "battery",
        "name": "4S 1500mAh 130C LiPo",
        "brand": "Pyrodrone",
        "price_php": 1596,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com",
        "color": "#220011",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "lumenier-n2o-4s-1500mah",
        "category": "battery",
        "name": "N2O 4S 1500mAh 95C LiPo",
        "brand": "Lumenier",
        "price_php": 2052,
        "weight_g": 192,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#001a00",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 95,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "goldbat-4s-1300mah-75c",
        "category": "battery",
        "name": "4S 1300mAh 75C LiPo",
        "brand": "Goldbat",
        "price_php": 855,
        "weight_g": 158,
        "in_stock": True,
        "buy_url": "https://www.amazon.com",
        "color": "#1a1a00",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 75,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "hglrc-6s-1300mah-100c",
        "category": "battery",
        "name": "6S 1300mAh 100C HV LiPo",
        "brand": "HGLRC",
        "price_php": 2166,
        "weight_g": 238,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.8
        }
    },
    {
        "id": "cnhl-3s-1300mah-100c",
        "category": "battery",
        "name": "3S 1300mAh 100C Black Series",
        "brand": "CNHL",
        "price_php": 969,
        "weight_g": 126,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 11.1
        }
    },
    {
        "id": "newbeedrone-4s-1500mah",
        "category": "battery",
        "name": "4S 1500mAh 100C LiPo",
        "brand": "NewBeeDrone",
        "price_php": 1596,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.newbeedrone.com",
        "color": "#001a22",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "smc-racing-6s-1050mah",
        "category": "battery",
        "name": "6S 1050mAh 120C Racing LiPo",
        "brand": "SMC",
        "price_php": 2394,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0022",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1050,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "pyrodrone-6s-1050mah",
        "category": "battery",
        "name": "6S 1050mAh 130C LiPo",
        "brand": "Pyrodrone",
        "price_php": 2280,
        "weight_g": 196,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com",
        "color": "#220011",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1050,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── RECEIVERS (10) ────────────────────────────────────────────────────────
    {
        "id": "frsky-r9-mini-900mhz",
        "category": "receiver",
        "name": "R9 Mini 900MHz Long Range RX",
        "brand": "FrSky",
        "price_php": 1938,
        "weight_g": 2.5,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com",
        "color": "#001a22",
        "specs": {
            "protocol": "FrSky",
            "frequency_mhz": 900,
            "diversity": False,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "radiomaster-rp2-2400",
        "category": "receiver",
        "name": "RP2 2.4GHz ELRS Nano RX",
        "brand": "RadioMaster",
        "price_php": 570,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "happymodel-es24tx-slim",
        "category": "receiver",
        "name": "ES24TX Slim Pro 2.4GHz ELRS",
        "brand": "Happymodel",
        "price_php": 1026,
        "weight_g": 2,
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
    {
        "id": "geprc-elrs-900-nano",
        "category": "receiver",
        "name": "ELRS 900MHz Nano RX",
        "brand": "GEPRC",
        "price_php": 912,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#002200",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 900,
            "diversity": False,
            "telemetry": True,
            "range_km": 50
        }
    },
    {
        "id": "matek-elrs-r900-m",
        "category": "receiver",
        "name": "ELRS-R900-M 900MHz RX",
        "brand": "Matek",
        "price_php": 912,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 900,
            "diversity": False,
            "telemetry": True,
            "range_km": 50
        }
    },
    {
        "id": "frsky-r-xsr",
        "category": "receiver",
        "name": "R-XSR ACCESS 16CH Ultra Mini",
        "brand": "FrSky",
        "price_php": 1482,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com",
        "color": "#001a22",
        "specs": {
            "protocol": "FrSky",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 8
        }
    },
    {
        "id": "tbs-tracer-nano",
        "category": "receiver",
        "name": "Tracer Nano RX 2.4GHz",
        "brand": "TBS",
        "price_php": 2052,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#220000",
        "specs": {
            "protocol": "TBS Tracer",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "jumper-aion-mini-elrs",
        "category": "receiver",
        "name": "Aion Mini ELRS 2.4GHz RX",
        "brand": "Jumper",
        "price_php": 570,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.jumper-rc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "immersionrc-ghost-nano-rx",
        "category": "receiver",
        "name": "Ghost Nano RX 2.4GHz",
        "brand": "ImmersionRC",
        "price_php": 1995,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#220044",
        "specs": {
            "protocol": "Ghost",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "frsky-rx4r-access",
        "category": "receiver",
        "name": "RX4R ACCESS 4-16CH SBUS",
        "brand": "FrSky",
        "price_php": 1254,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com",
        "color": "#001a22",
        "specs": {
            "protocol": "FrSky",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 8
        }
    },

    # ─── GPS MODULES (10) ──────────────────────────────────────────────────────
    {
        "id": "cuav-neo-3x-gps",
        "category": "gps",
        "name": "NEO-3X GPS+Compass",
        "brand": "CUAV",
        "price_php": 2736,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.cuav.net",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 25,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "cubepilot-here3-gnss",
        "category": "gps",
        "name": "Here3 CAN GNSS+Compass",
        "brand": "CubePilot",
        "price_php": 6840,
        "weight_g": 48,
        "in_stock": True,
        "buy_url": "https://www.cubepilot.org",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M8P",
            "update_rate_hz": 18,
            "fix_time_s": 26,
            "compass": True,
            "connector": "CAN DroneCAN"
        }
    },
    {
        "id": "radiomaster-m100-gps",
        "category": "gps",
        "name": "M100 GPS+Compass Module",
        "brand": "RadioMaster",
        "price_php": 1596,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 18,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "flywoo-gm10-nano-v2",
        "category": "gps",
        "name": "GM10 Nano V2 GPS+Compass",
        "brand": "Flywoo",
        "price_php": 1710,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
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
        "id": "lumenier-m10-gps",
        "category": "gps",
        "name": "GPS M10 Module+Compass",
        "brand": "Lumenier",
        "price_php": 1596,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#001a00",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 18,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "iflight-m10-gps-v2",
        "category": "gps",
        "name": "M10 Mini GPS V2+Compass",
        "brand": "iFlight",
        "price_php": 1710,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "ardusimple-simplertk2b",
        "category": "gps",
        "name": "simpleRTK2B RTK GPS",
        "brand": "ArduSimple",
        "price_php": 11400,
        "weight_g": 52,
        "in_stock": True,
        "buy_url": "https://www.ardusimple.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox ZED-F9P",
            "update_rate_hz": 20,
            "fix_time_s": 60,
            "compass": False,
            "connector": "JST-GH"
        }
    },
    {
        "id": "matek-m10-5883-gps",
        "category": "gps",
        "name": "M10-5883 GPS+QMC5883 Compass",
        "brand": "Matek",
        "price_php": 1824,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "geprc-m10-express-v2",
        "category": "gps",
        "name": "M10 Express V2 GPS+Compass",
        "brand": "GEPRC",
        "price_php": 1482,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#002200",
        "specs": {
            "constellation": "GPS+GLONASS+BDS",
            "chipset": "u-blox M10",
            "update_rate_hz": 18,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "axisflying-m100-mini-gps",
        "category": "gps",
        "name": "M100 Mini GPS+Compass",
        "brand": "AxisFlying",
        "price_php": 1482,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a0022",
        "specs": {
            "constellation": "GPS+GLONASS+BDS",
            "chipset": "u-blox M10",
            "update_rate_hz": 18,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },

    # ─── ANTENNAS (10) ─────────────────────────────────────────────────────────
    {
        "id": "truerc-diamond-5-8",
        "category": "antenna",
        "name": "Diamond 5.8GHz RHCP SMA",
        "brand": "TrueRC",
        "price_php": 1710,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://truerc.ca",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 4.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "lumenier-axii-stubby",
        "category": "antenna",
        "name": "AXII Stubby 5.8GHz RHCP SMA",
        "brand": "Lumenier",
        "price_php": 855,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "vas-camel-5-8",
        "category": "antenna",
        "name": "Camel 5.8GHz RHCP SMA",
        "brand": "VAS",
        "price_php": 1140,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "pagoda-pro-5-8",
        "category": "antenna",
        "name": "Pagoda Pro 5.8GHz RHCP SMA",
        "brand": "IBCrazy",
        "price_php": 855,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "patch"
        }
    },
    {
        "id": "rushfpv-cherry-blossom",
        "category": "antenna",
        "name": "Cherry Blossom 5.8GHz RHCP",
        "brand": "RushFPV",
        "price_php": 912,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "foxeer-echo-patch",
        "category": "antenna",
        "name": "Echo Patch 5.8GHz RHCP SMA",
        "brand": "Foxeer",
        "price_php": 1254,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 10.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "patch"
        }
    },
    {
        "id": "realacc-pagoda-pro",
        "category": "antenna",
        "name": "Pagoda Pro 5.8GHz RHCP U.FL",
        "brand": "Realacc",
        "price_php": 570,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "patch"
        }
    },
    {
        "id": "ethix-stubby-5-8",
        "category": "antenna",
        "name": "Stubby 5.8GHz RHCP SMA",
        "brand": "Ethix",
        "price_php": 855,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "betafpv-ufl-antenna",
        "category": "antenna",
        "name": "5.8GHz U.FL RHCP Whoop Antenna",
        "brand": "BetaFPV",
        "price_php": 456,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.5,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "stubby"
        }
    },
    {
        "id": "skyviper-patch-5-8",
        "category": "antenna",
        "name": "5.8GHz Patch 8.5dBi RHCP SMA",
        "brand": "Skyviper",
        "price_php": 1710,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 8.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "patch"
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
