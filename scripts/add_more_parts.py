#!/usr/bin/env python3
"""Add 120 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (11) ───────────────────────────────────────────────────────────
    {
        "id": "geprc-mark4-h5-v2",
        "category": "frame",
        "name": "Mark4 H5 V2 5\" HD",
        "brand": "GEPRC",
        "price_php": 3534,
        "weight_g": 70,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#002200",
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
        "id": "armattan-chameleon-ti-5",
        "category": "frame",
        "name": "Chameleon Ti 5\" Freestyle",
        "brand": "Armattan",
        "price_php": 8208,
        "weight_g": 62,
        "in_stock": True,
        "buy_url": "https://armattanquads.com",
        "color": "#1a0a00",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "titanium",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "flywoo-explorer-lr4-hd",
        "category": "frame",
        "name": "Explorer LR 4\" HD Long Range",
        "brand": "Flywoo",
        "price_php": 2964,
        "weight_g": 60,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d1a0d",
        "specs": {
            "size_mm": 170,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 20
        }
    },
    {
        "id": "ummagawd-remix-v2-5",
        "category": "frame",
        "name": "Remix V2 5\" Freestyle",
        "brand": "Ummagawd",
        "price_php": 5130,
        "weight_g": 58,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#0a0a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 28
        }
    },
    {
        "id": "iflight-chimera4-pro-v2",
        "category": "frame",
        "name": "Chimera4 Pro V2 4\" Cinematic",
        "brand": "iFlight",
        "price_php": 3420,
        "weight_g": 72,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "hglrc-wind5-lite-5",
        "category": "frame",
        "name": "Wind5 Lite 5\" Freestyle",
        "brand": "HGLRC",
        "price_php": 2394,
        "weight_g": 66,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#001a44",
        "specs": {
            "size_mm": 218,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 26
        }
    },
    {
        "id": "betafpv-hx100-se-2-5",
        "category": "frame",
        "name": "HX100 SE 2.5\" Whoop",
        "brand": "BetaFPV",
        "price_php": 1254,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "size_mm": 100,
            "motor_mount_mm": 9,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 15
        }
    },
    {
        "id": "diatone-gt-m3-3inch",
        "category": "frame",
        "name": "GT-M3 3\" Stretch X",
        "brand": "Diatone",
        "price_php": 1938,
        "weight_g": 42,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 130,
            "motor_mount_mm": 9,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 16
        }
    },
    {
        "id": "flywoo-flylens-85-2inch",
        "category": "frame",
        "name": "FlyLens 85 2\" HD Whoop",
        "brand": "Flywoo",
        "price_php": 2394,
        "weight_g": 35,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 85,
            "motor_mount_mm": 9,
            "prop_clearance_inch": 2,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 14
        }
    },
    {
        "id": "emax-hawk-pro-5",
        "category": "frame",
        "name": "Hawk Pro 5\" Long Range",
        "brand": "Emax",
        "price_php": 2736,
        "weight_g": 80,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com",
        "color": "#1a0000",
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
        "id": "tbs-source-one-mini-v3",
        "category": "frame",
        "name": "Source One Mini V3 3.5\"",
        "brand": "TBS",
        "price_php": 1596,
        "weight_g": 48,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 155,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 20
        }
    },

    # ─── MOTORS (11) ───────────────────────────────────────────────────────────
    {
        "id": "iflight-xing2-2207-1855kv",
        "category": "motor",
        "name": "XING2 2207 1855KV Freestyle",
        "brand": "iFlight",
        "price_php": 1482,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "kv": 1855,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 46
        }
    },
    {
        "id": "emax-eco-ii-2306-2400kv",
        "category": "motor",
        "name": "ECO II 2306 2400KV",
        "brand": "Emax",
        "price_php": 798,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com",
        "color": "#1a0000",
        "specs": {
            "kv": 2400,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "tmotor-velox-v2-2207-2450kv",
        "category": "motor",
        "name": "Velox V2 V2207 2450KV",
        "brand": "T-Motor",
        "price_php": 1938,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "hyperlite-floss3-2207-2522kv",
        "category": "motor",
        "name": "Floss 3 2207 2522KV Freestyle",
        "brand": "Hyperlite",
        "price_php": 1824,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2522,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 46
        }
    },
    {
        "id": "rcin-power-gts-v2-2207-2550kv",
        "category": "motor",
        "name": "GTS V2 2207 2550KV Race",
        "brand": "RCINPower",
        "price_php": 1596,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#220000",
        "specs": {
            "kv": 2550,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 46
        }
    },
    {
        "id": "brotherhobby-avenger-2208-1700kv",
        "category": "motor",
        "name": "Avenger 2208 1700KV 6S",
        "brand": "BrotherHobby",
        "price_php": 1368,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#001a22",
        "specs": {
            "kv": 1700,
            "stator_size": "2208",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "ethix-mr-steele-silk-2207-1922kv",
        "category": "motor",
        "name": "Mr Steele Silk 2207 1922KV",
        "brand": "Ethix",
        "price_php": 1710,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#001122",
        "specs": {
            "kv": 1922,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "cobra-champion-2207-2450kv",
        "category": "motor",
        "name": "Champion 2207 2450KV Race",
        "brand": "Cobra",
        "price_php": 1254,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.innov8tivedesigns.com",
        "color": "#220000",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "sunnysky-r2205-2350kv",
        "category": "motor",
        "name": "R2205 2350KV Racing",
        "brand": "Sunnysky",
        "price_php": 912,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://sunnyskyusa.com",
        "color": "#1a1a00",
        "specs": {
            "kv": 2350,
            "stator_size": "2205",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "happymodel-rs1408-3600kv",
        "category": "motor",
        "name": "EX1404 3600KV Toothpick",
        "brand": "Happymodel",
        "price_php": 741,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a0011",
        "specs": {
            "kv": 3600,
            "stator_size": "1404",
            "motor_mount_mm": 12,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 2,
            "peak_current_a": 18
        }
    },
    {
        "id": "iflight-xing-e-2207-2450kv",
        "category": "motor",
        "name": "XING-E 2207 2450KV Pro",
        "brand": "iFlight",
        "price_php": 1140,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },

    # ─── ESC (11) ──────────────────────────────────────────────────────────────
    {
        "id": "iflight-blitz-e45-4in1",
        "category": "esc",
        "name": "BLITZ E45 4-in-1 45A",
        "brand": "iFlight",
        "price_php": 3762,
        "weight_g": 23,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "speedybee-bls55a-4in1",
        "category": "esc",
        "name": "BLS 55A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 3420,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#001a00",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 68
        }
    },
    {
        "id": "holybro-kotleta20-4in1",
        "category": "esc",
        "name": "Kotleta20 4-in-1 20A",
        "brand": "Holybro",
        "price_php": 2736,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#002244",
        "specs": {
            "amp_rating": 20,
            "input_voltage_s": 4,
            "protocol": "DSHOT300",
            "form_factor_mm": 20,
            "burst_amp": 25
        }
    },
    {
        "id": "tmotor-f55a-pro-iii-4in1",
        "category": "esc",
        "name": "F55A PRO III 4-in-1 55A",
        "brand": "T-Motor",
        "price_php": 5130,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "foxeer-reaper-45a-4in1",
        "category": "esc",
        "name": "Reaper F745 45A 4-in-1",
        "brand": "Foxeer",
        "price_php": 3135,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#220000",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "diatone-mamba-f45-mk4-4in1",
        "category": "esc",
        "name": "Mamba F45 MK4 4-in-1 45A",
        "brand": "Diatone",
        "price_php": 2964,
        "weight_g": 21,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002222",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 56
        }
    },
    {
        "id": "geprc-stable-f4-30a-aio",
        "category": "esc",
        "name": "Stable F4 30A AIO FC+ESC",
        "brand": "GEPRC",
        "price_php": 2394,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 30,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 40
        }
    },
    {
        "id": "hglrc-speedy-f4-35a-aio",
        "category": "esc",
        "name": "Speedy F4 35A AIO Stack",
        "brand": "HGLRC",
        "price_php": 2736,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "amp_rating": 35,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 45
        }
    },
    {
        "id": "betafpv-f4-25a-2-4s-aio",
        "category": "esc",
        "name": "F4 2-4S 25A AIO Whoop",
        "brand": "BetaFPV",
        "price_php": 2166,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "amp_rating": 25,
            "input_voltage_s": 4,
            "protocol": "DSHOT300",
            "form_factor_mm": 25,
            "burst_amp": 30
        }
    },
    {
        "id": "speedybee-f405-v3-55a-esc",
        "category": "esc",
        "name": "F405 V3 55A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 3762,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#001a00",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "axisflying-argus-45a-4in1",
        "category": "esc",
        "name": "ARGUS 45A 4-in-1 BLHeli_32",
        "brand": "AxisFlying",
        "price_php": 3135,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a0022",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },

    # ─── FLIGHT CONTROLLERS (11) ───────────────────────────────────────────────
    {
        "id": "matek-h743-wlite",
        "category": "fc",
        "name": "H743-WLITE ArduPilot FC",
        "brand": "Matek",
        "price_php": 4788,
        "weight_g": 14,
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
            "5v_pad_count": 4,
            "curr_sensor": True,
            "diagram_url": "https://www.mateksys.com/?portfolio=h743-wlite"
        }
    },
    {
        "id": "holybro-kakute-h7-mini",
        "category": "fc",
        "name": "Kakute H7 Mini Betaflight FC",
        "brand": "Holybro",
        "price_php": 3990,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#002244",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://docs.holybro.com/fpv-flight-controller/kakute-h7-mini"
        }
    },
    {
        "id": "speedybee-f405-v3-fc",
        "category": "fc",
        "name": "F405 V3 Betaflight FC",
        "brand": "SpeedyBee",
        "price_php": 2964,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#001a00",
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
        "id": "iflight-blitz-f7-pro",
        "category": "fc",
        "name": "BLITZ F7 Pro Betaflight FC",
        "brand": "iFlight",
        "price_php": 3648,
        "weight_g": 10,
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
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "diatone-mamba-h743-mini",
        "category": "fc",
        "name": "Mamba H743-Mini MK2 ArduPilot",
        "brand": "Diatone",
        "price_php": 4332,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002222",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "ArduPilot",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "axisflying-argus-f7-pro",
        "category": "fc",
        "name": "ARGUS F7 Pro FC",
        "brand": "AxisFlying",
        "price_php": 3876,
        "weight_g": 11,
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
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "flywoo-goku-f7-pro-fc",
        "category": "fc",
        "name": "GOKU GN745 F7 Pro FC",
        "brand": "Flywoo",
        "price_php": 3762,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
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
        "id": "betafpv-pavo-pico-f4-aio",
        "category": "fc",
        "name": "Pavo Pico F4 AIO Whoop FC",
        "brand": "BetaFPV",
        "price_php": 2622,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 25,
            "stack_mount_mm": 25,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "iflight-succex-d-mini-f7",
        "category": "fc",
        "name": "SUCCEX-D Mini F7 Twin G",
        "brand": "iFlight",
        "price_php": 4104,
        "weight_g": 11,
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
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "matek-f722-mini-se",
        "category": "fc",
        "name": "F722-Mini SE Betaflight FC",
        "brand": "Matek",
        "price_php": 3420,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
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
        "id": "geprc-taker-g4-f4-aio",
        "category": "fc",
        "name": "TAKER G4 F4 AIO 2-6S",
        "brand": "GEPRC",
        "price_php": 3078,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#002200",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 25,
            "stack_mount_mm": 25,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (11) ───────────────────────────────────────────────────────
    {
        "id": "hqprop-5x4x3-v1s-3b",
        "category": "propeller",
        "name": "5X4X3 V1S 3-Blade PC",
        "brand": "HQProp",
        "price_php": 222,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "red", "blue"]
        }
    },
    {
        "id": "gemfan-5152s-2b-race",
        "category": "propeller",
        "name": "5152S 2-Blade Race",
        "brand": "Gemfan",
        "price_php": 194,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.2,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["black", "white", "orange"]
        }
    },
    {
        "id": "dal-dp-5045v3-3b",
        "category": "propeller",
        "name": "Cyclone DP 5045V3 3-Blade",
        "brand": "DAL",
        "price_php": 194,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "smoke"]
        }
    },
    {
        "id": "ethix-p3-pineapple-5145",
        "category": "propeller",
        "name": "P3 Pineapple 5145 3-Blade",
        "brand": "Ethix",
        "price_php": 251,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "yellow", "green"]
        }
    },
    {
        "id": "hqprop-4x4x3-4inch-3b",
        "category": "propeller",
        "name": "4X4X3 4\" 3-Blade Durable",
        "brand": "HQProp",
        "price_php": 194,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 4,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white"]
        }
    },
    {
        "id": "gemfan-3052-3inch-3b",
        "category": "propeller",
        "name": "3052 3\" 3-Blade Durable",
        "brand": "Gemfan",
        "price_php": 142,
        "weight_g": 2.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 3,
            "pitch": 5.2,
            "blade_count": 3,
            "shaft_mm": 2,
            "color_options": ["black", "white", "pink"]
        }
    },
    {
        "id": "hqprop-3x3x3-3inch-3b",
        "category": "propeller",
        "name": "3X3X3 3\" 3-Blade Light",
        "brand": "HQProp",
        "price_php": 142,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 3,
            "pitch": 3.0,
            "blade_count": 3,
            "shaft_mm": 2,
            "color_options": ["black", "white", "blue"]
        }
    },
    {
        "id": "dal-cyclone-6030-3b-6inch",
        "category": "propeller",
        "name": "Cyclone 6030 6\" 3-Blade",
        "brand": "DAL",
        "price_php": 251,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 6,
            "pitch": 3.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "smoke"]
        }
    },
    {
        "id": "tmotor-t4943-4-9-3b",
        "category": "propeller",
        "name": "T4943 4.9\" 3-Blade Cinema",
        "brand": "T-Motor",
        "price_php": 279,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 4.9,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    {
        "id": "gemfan-4023-4inch-2b",
        "category": "propeller",
        "name": "4023 4\" 2-Blade Efficiency",
        "brand": "Gemfan",
        "price_php": 165,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 4,
            "pitch": 2.3,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["black", "white"]
        }
    },
    {
        "id": "hqprop-7x3-5x3-7inch",
        "category": "propeller",
        "name": "7X3.5X3 7\" 3-Blade Long Range",
        "brand": "HQProp",
        "price_php": 308,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 3.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },

    # ─── CAMERAS (11) ──────────────────────────────────────────────────────────
    {
        "id": "runcam-phoenix2-sp-1200tvl",
        "category": "camera",
        "name": "Phoenix 2 SP 1200TVL",
        "brand": "RunCam",
        "price_php": 1596,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" STARVIS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V",
            "video_system": "Analog"
        }
    },
    {
        "id": "caddx-ratel2-1200tvl",
        "category": "camera",
        "name": "Ratel 2 1200TVL Starlight",
        "brand": "Caddx",
        "price_php": 1482,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" STARVIS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V",
            "video_system": "Analog"
        }
    },
    {
        "id": "foxeer-razer-mini-1200tvl",
        "category": "camera",
        "name": "Razer Mini 1200TVL FPV",
        "brand": "Foxeer",
        "price_php": 1368,
        "weight_g": 3.8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V",
            "video_system": "Analog"
        }
    },
    {
        "id": "runcam-wasp-fpv-racing",
        "category": "camera",
        "name": "Wasp FPV Racing Camera",
        "brand": "RunCam",
        "price_php": 1254,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" STARVIS",
            "fov_deg": 150,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-36V",
            "video_system": "Analog"
        }
    },
    {
        "id": "caddx-nebula-pro-nano-hd",
        "category": "camera",
        "name": "Nebula Pro Nano HD DJI",
        "brand": "Caddx",
        "price_php": 7296,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "video_system": "DJI",
            "resolution": "1080p60fps",
            "voltage_range": "7.4-26V"
        }
    },
    {
        "id": "foxeer-cat3-fpv-low-light",
        "category": "camera",
        "name": "Cat 3 FPV Low-Light 1200TVL",
        "brand": "Foxeer",
        "price_php": 1710,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" STARVIS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V",
            "video_system": "Analog"
        }
    },
    {
        "id": "caddx-polar-nano-starlight",
        "category": "camera",
        "name": "Polar Nano Starlight Digital",
        "brand": "Caddx",
        "price_php": 8550,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" STARVIS",
            "fov_deg": 155,
            "format": "Digital",
            "video_system": "DJI",
            "resolution": "1080p60fps",
            "voltage_range": "7.4-26V"
        }
    },
    {
        "id": "runcam-swift-mini-3-600tvl",
        "category": "camera",
        "name": "Swift Mini 3 600TVL CCD",
        "brand": "RunCam",
        "price_php": 1140,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CCD",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 600,
            "voltage_range": "5-40V",
            "video_system": "Analog"
        }
    },
    {
        "id": "foxeer-micro-predator5",
        "category": "camera",
        "name": "Micro Predator 5 Racing 1000TVL",
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
            "tvl": 1000,
            "voltage_range": "5-40V",
            "video_system": "Analog"
        }
    },
    {
        "id": "walksnail-avatar-v3-nano",
        "category": "camera",
        "name": "Avatar Nano V3 Digital Camera",
        "brand": "Walksnail",
        "price_php": 6840,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2.7\" CMOS",
            "fov_deg": 135,
            "format": "Digital",
            "video_system": "Walksnail",
            "resolution": "1080p60fps",
            "voltage_range": "5V"
        }
    },
    {
        "id": "hdzero-eco-camera",
        "category": "camera",
        "name": "Eco Camera 1080p HDZero",
        "brand": "HDZero",
        "price_php": 4788,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2.3\" CMOS",
            "fov_deg": 140,
            "format": "Digital",
            "video_system": "HDZero",
            "resolution": "1080p30fps",
            "voltage_range": "5V"
        }
    },

    # ─── VTX (11) ──────────────────────────────────────────────────────────────
    {
        "id": "tbs-unify-pro32-hv-5g8",
        "category": "vtx",
        "name": "Unify Pro32 HV 5G8 SmartAudio",
        "brand": "TBS",
        "price_php": 3420,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#220000",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "immersionrc-tramp-hv-vtx",
        "category": "vtx",
        "name": "Tramp HV 5.8G 600mW VTX",
        "brand": "ImmersionRC",
        "price_php": 2850,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#220044",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "foxeer-pit-25mw-nano",
        "category": "vtx",
        "name": "Pit 25mW 5.8G Nano VTX",
        "brand": "Foxeer",
        "price_php": 684,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#220000",
        "specs": {
            "power_mw_max": 25,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-9V",
            "connector": "U.FL"
        }
    },
    {
        "id": "speedybee-tx500-500mw",
        "category": "vtx",
        "name": "TX500 5.8G 500mW VTX",
        "brand": "SpeedyBee",
        "price_php": 1824,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#001a00",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-36V",
            "connector": "SMA"
        }
    },
    {
        "id": "betafpv-m02-5-8g-25mw",
        "category": "vtx",
        "name": "M02 5.8G 25mW Nano VTX",
        "brand": "BetaFPV",
        "price_php": 684,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "power_mw_max": 25,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-9V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rushfpv-rush-solo-1w",
        "category": "vtx",
        "name": "Rush Solo 5.8G 1W VTX",
        "brand": "RushFPV",
        "price_php": 1938,
        "weight_g": 7,
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
        "id": "hglrc-at-nx-nano-25mw",
        "category": "vtx",
        "name": "AT-NX 5.8G 25mW Nano VTX",
        "brand": "HGLRC",
        "price_php": 570,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "power_mw_max": 25,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-9V",
            "connector": "U.FL"
        }
    },
    {
        "id": "eachine-tx805-600mw",
        "category": "vtx",
        "name": "TX805 5.8G 600mW VTX OSD",
        "brand": "Eachine",
        "price_php": 798,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#001a1a",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },
    {
        "id": "hdzero-eco-vtx-1w",
        "category": "vtx",
        "name": "Eco 1W Digital HD VTX",
        "brand": "HDZero",
        "price_php": 5700,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Digital",
            "video_system": "HDZero",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "walksnail-avatar-vtx-v3",
        "category": "vtx",
        "name": "Avatar HD VTX V3 Kit",
        "brand": "Walksnail",
        "price_php": 9804,
        "weight_g": 20,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 700,
            "protocol": "Digital",
            "video_system": "Walksnail",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-mini-400mw-smartaudio",
        "category": "vtx",
        "name": "Mini 400mW 5.8G SmartAudio VTX",
        "brand": "HGLRC",
        "price_php": 1254,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-36V",
            "connector": "U.FL"
        }
    },

    # ─── BATTERIES (11) ────────────────────────────────────────────────────────
    {
        "id": "tattu-rline-v3-6s-1050mah",
        "category": "battery",
        "name": "R-Line V3.0 6S 1050mAh 120C",
        "brand": "Tattu",
        "price_php": 2736,
        "weight_g": 193,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#220000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1050,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gens-ace-g-tech-4s-1300mah",
        "category": "battery",
        "name": "G-Tech 4S 1300mAh 100C Smart",
        "brand": "Gens Ace",
        "price_php": 1824,
        "weight_g": 152,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#001a00",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "cnhl-ministar-4s-1500mah-120c",
        "category": "battery",
        "name": "MiniStar 4S 1500mAh 120C",
        "brand": "CNHL",
        "price_php": 1710,
        "weight_g": 182,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "ovonic-6s-1050mah-100c",
        "category": "battery",
        "name": "6S 1050mAh 100C Racing LiPo",
        "brand": "Ovonic",
        "price_php": 1938,
        "weight_g": 194,
        "in_stock": True,
        "buy_url": "https://www.amazon.com",
        "color": "#1a0022",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1050,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "dogcom-6s-1300mah-120c",
        "category": "battery",
        "name": "6S 1300mAh 120C High Voltage",
        "brand": "DOGCOM",
        "price_php": 2394,
        "weight_g": 242,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#001a22",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "turnigy-nano-4s-2200mah-65c",
        "category": "battery",
        "name": "Nano-Tech 4S 2200mAh 65C",
        "brand": "Turnigy",
        "price_php": 1824,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://hobbyking.com",
        "color": "#1a1a00",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 2200,
            "c_rating": 65,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gens-ace-soaring-4s-1800mah",
        "category": "battery",
        "name": "Soaring 4S 1800mAh 60C LiPo",
        "brand": "Gens Ace",
        "price_php": 2052,
        "weight_g": 198,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#001a00",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1800,
            "c_rating": 60,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "zeee-4s-1500mah-100c",
        "category": "battery",
        "name": "4S 1500mAh 100C LiPo Hardcase",
        "brand": "Zeee",
        "price_php": 1482,
        "weight_g": 174,
        "in_stock": True,
        "buy_url": "https://www.amazon.com",
        "color": "#220000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "vant-4s-1300mah-75c",
        "category": "battery",
        "name": "4S 1300mAh 75C Race Pack",
        "brand": "Vant",
        "price_php": 1596,
        "weight_g": 155,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0011",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 75,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-4s-1300mah-75c",
        "category": "battery",
        "name": "4S 1300mAh 75C FPV LiPo",
        "brand": "Tattu",
        "price_php": 1710,
        "weight_g": 156,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#220000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 75,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "cnhl-6s-1100mah-100c",
        "category": "battery",
        "name": "6S 1100mAh 100C Black Series",
        "brand": "CNHL",
        "price_php": 2166,
        "weight_g": 206,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── RECEIVERS (11) ────────────────────────────────────────────────────────
    {
        "id": "expresslrs-ep1-nano-2-4g",
        "category": "receiver",
        "name": "EP1 Nano 2.4GHz ELRS RX",
        "brand": "ExpressLRS",
        "price_php": 627,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#001a22",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "radiomaster-rp1-nano-elrs",
        "category": "receiver",
        "name": "RP1 Nano ELRS 2.4GHz RX",
        "brand": "RadioMaster",
        "price_php": 456,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "betafpv-elrs-lite-2-4g",
        "category": "receiver",
        "name": "ELRS Lite 2.4GHz Nano RX",
        "brand": "BetaFPV",
        "price_php": 456,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "happymodel-ep2-elrs-2-4g",
        "category": "receiver",
        "name": "EP2 ELRS 2.4GHz Ultra Nano",
        "brand": "Happymodel",
        "price_php": 513,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a0011",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "tbs-crossfire-nano-rx-900",
        "category": "receiver",
        "name": "Crossfire Nano RX 900MHz",
        "brand": "TBS",
        "price_php": 1938,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#220000",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 60
        }
    },
    {
        "id": "flysky-fgr4-nano-rx",
        "category": "receiver",
        "name": "FGr4 Nano FlySky RX 2.4GHz",
        "brand": "FlySky",
        "price_php": 570,
        "weight_g": 1.9,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#001a22",
        "specs": {
            "protocol": "AFHDS 3",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 5
        }
    },
    {
        "id": "matek-elrs-r24-d-diversity",
        "category": "receiver",
        "name": "ELRS-R24-D Diversity 2.4GHz",
        "brand": "Matek",
        "price_php": 1026,
        "weight_g": 2.4,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "geprc-elrs-nano-2-4g",
        "category": "receiver",
        "name": "ELRS Nano 2.4GHz GEPRC RX",
        "brand": "GEPRC",
        "price_php": 513,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#002200",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "frsky-r9mx-access-900",
        "category": "receiver",
        "name": "R9MX ACCESS 900MHz Long Range",
        "brand": "FrSky",
        "price_php": 1824,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com",
        "color": "#001a22",
        "specs": {
            "protocol": "FrSky ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "radiomaster-rp4td-diversity",
        "category": "receiver",
        "name": "RP4TD ELRS Diversity 2.4GHz",
        "brand": "RadioMaster",
        "price_php": 912,
        "weight_g": 3.2,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "iflight-elrs-nano-2-4g",
        "category": "receiver",
        "name": "ELRS 2.4GHz Nano RX iFlight",
        "brand": "iFlight",
        "price_php": 570,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },

    # ─── GPS MODULES (11) ──────────────────────────────────────────────────────
    {
        "id": "bn-880-gps-compass-m8n",
        "category": "gps",
        "name": "BN-880 GPS+Compass M8N",
        "brand": "Beitian",
        "price_php": 1026,
        "weight_g": 21,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 35,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "bn-220-gps-mini-m8n",
        "category": "gps",
        "name": "BN-220 GPS Mini Dual Module",
        "brand": "Beitian",
        "price_php": 798,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 40,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "speedybee-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS+Compass Module",
        "brand": "SpeedyBee",
        "price_php": 1596,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#001a00",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 18,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m8n-gps",
        "category": "gps",
        "name": "Micro M8N GPS Module",
        "brand": "Holybro",
        "price_php": 1824,
        "weight_g": 20,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#002244",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 32,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-sam-m10q-gps",
        "category": "gps",
        "name": "SAM-M10Q Compact GPS",
        "brand": "Matek",
        "price_php": 1482,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox SAM-M10Q",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "hglrc-m100-mini-gps",
        "category": "gps",
        "name": "M100 Mini GPS+Compass M10",
        "brand": "HGLRC",
        "price_php": 1596,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
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
        "id": "betafpv-m10-gps-nano",
        "category": "gps",
        "name": "M10 GPS Nano Lite Module",
        "brand": "BetaFPV",
        "price_php": 1368,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "constellation": "GPS+GLONASS+BDS",
            "chipset": "u-blox M10",
            "update_rate_hz": 18,
            "fix_time_s": 30,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "foxeer-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Foxeer",
        "price_php": 1824,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#220000",
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
        "id": "diatone-mamba-gps-m10",
        "category": "gps",
        "name": "Mamba GPS M10 Mini Module",
        "brand": "Diatone",
        "price_php": 1482,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002222",
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
        "id": "emax-gps-nano-m8n",
        "category": "gps",
        "name": "Nano GPS Module M8N+Compass",
        "brand": "Emax",
        "price_php": 1254,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com",
        "color": "#1a0000",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 35,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "cuav-c-rtk-9ps-gnss",
        "category": "gps",
        "name": "C-RTK 9Ps RTK GNSS Module",
        "brand": "CUAV",
        "price_php": 9120,
        "weight_g": 36,
        "in_stock": True,
        "buy_url": "https://www.cuav.net",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox F9P",
            "update_rate_hz": 20,
            "fix_time_s": 60,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── ANTENNAS (11) ─────────────────────────────────────────────────────────
    {
        "id": "foxeer-lollipop4-rhcp-sma",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP SMA",
        "brand": "Foxeer",
        "price_php": 912,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
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
        "id": "truerc-singularity-5-8-sma",
        "category": "antenna",
        "name": "Singularity 5.8GHz RHCP SMA",
        "brand": "TrueRC",
        "price_php": 1254,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://truerc.ca",
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
        "id": "rushfpv-max-gorilla-5-8",
        "category": "antenna",
        "name": "MAX Gorilla 5.8GHz RHCP SMA",
        "brand": "RushFPV",
        "price_php": 1140,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
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
        "id": "tbs-triumph-pro-rhcp-sma",
        "category": "antenna",
        "name": "Triumph Pro RHCP 5.8GHz SMA",
        "brand": "TBS",
        "price_php": 1596,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#220000",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "lumenier-axii-2-long-5-8",
        "category": "antenna",
        "name": "AXII 2 Long 5.8GHz RHCP SMA",
        "brand": "Lumenier",
        "price_php": 1026,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.1,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "pagoda2-ufl-5-8-rhcp",
        "category": "antenna",
        "name": "Pagoda 2 5.8GHz RHCP U.FL",
        "brand": "GEPRC",
        "price_php": 684,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://geprc.com",
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
        "id": "matek-ant-m5g8-rh-mini",
        "category": "antenna",
        "name": "ANT-M5G8-RH 5.8GHz Mini MMCX",
        "brand": "Matek",
        "price_php": 570,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.5,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "stubby"
        }
    },
    {
        "id": "foxeer-lollipop4-ufl",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP U.FL",
        "brand": "Foxeer",
        "price_php": 798,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "stubby"
        }
    },
    {
        "id": "rushfpv-cherry-pro-ufl",
        "category": "antenna",
        "name": "Cherry Pro 5.8GHz RHCP U.FL",
        "brand": "RushFPV",
        "price_php": 684,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "stubby"
        }
    },
    {
        "id": "hglrc-5-8g-lhcp-sma",
        "category": "antenna",
        "name": "5.8GHz LHCP Linear SMA VTX",
        "brand": "HGLRC",
        "price_php": 456,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "LHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "truerc-x2-5-8-patch",
        "category": "antenna",
        "name": "X2 5.8GHz RHCP Patch 9dBi",
        "brand": "TrueRC",
        "price_php": 2166,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://truerc.ca",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 9.0,
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
