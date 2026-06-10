#!/usr/bin/env python3
"""Add 66 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (6) ────────────────────────────────────────────────────────────
    {
        "id": "iflight-cidora-sl5",
        "category": "frame",
        "name": "Cidora SL5 5\" Freestyle",
        "brand": "iFlight",
        "price_php": 5320,
        "weight_g": 79,
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
    {
        "id": "lumenier-qav-s",
        "category": "frame",
        "name": "QAV-S 5\" Race Frame",
        "brand": "Lumenier",
        "price_php": 2520,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
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
        "id": "hglrc-sector-5-v5",
        "category": "frame",
        "name": "Sector 5 V5 Freestyle",
        "brand": "HGLRC",
        "price_php": 3920,
        "weight_g": 76,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
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
        "id": "tbs-source-one-v6",
        "category": "frame",
        "name": "Source One V6 5\"",
        "brand": "TBS",
        "price_php": 1400,
        "weight_g": 70,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
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
        "id": "impulserc-apex",
        "category": "frame",
        "name": "Apex 5\" Freestyle",
        "brand": "ImpulseRC",
        "price_php": 3920,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://impulserc.com",
        "color": "#1a1a2e",
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
        "id": "flywoo-explorer-lr5",
        "category": "frame",
        "name": "Explorer LR5 Long Range",
        "brand": "Flywoo",
        "price_php": 4200,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a2e",
        "specs": {
            "size_mm": 232,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30
        }
    },

    # ─── MOTORS (6) ────────────────────────────────────────────────────────────
    {
        "id": "tmotor-velox-v2807",
        "category": "motor",
        "name": "Velox V2807 1300KV",
        "brand": "T-Motor",
        "price_php": 1680,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "iflight-xing2-2207",
        "category": "motor",
        "name": "XING2 2207 1800KV",
        "brand": "iFlight",
        "price_php": 1232,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5",
        "category": "motor",
        "name": "Avenger 2306.5 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1120,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#001a22",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "flywoo-robo-rs2207",
        "category": "motor",
        "name": "ROBO RS2207 1800KV",
        "brand": "Flywoo",
        "price_php": 1064,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a2e",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "iflight-xing-x2806-5",
        "category": "motor",
        "name": "XING-E Pro 2806.5 1300KV",
        "brand": "iFlight",
        "price_php": 1400,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "kv": 1300,
            "stator_size": "2806",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "tmotor-velox-v2306",
        "category": "motor",
        "name": "Velox V2306 1950KV",
        "brand": "T-Motor",
        "price_php": 1344,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "kv": 1950,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },

    # ─── ESC (6) ───────────────────────────────────────────────────────────────
    {
        "id": "iflight-succex-e-f4-45a",
        "category": "esc",
        "name": "SucceX-E F4 45A 4-in-1",
        "brand": "iFlight",
        "price_php": 2520,
        "weight_g": 28,
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
        "id": "holybro-tekko32-f4-50a",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1",
        "brand": "Holybro",
        "price_php": 3360,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#004400",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "flywoo-goku-gn-745-50a",
        "category": "esc",
        "name": "GOKU GN745 50A 4-in-1",
        "brand": "Flywoo",
        "price_php": 3080,
        "weight_g": 23,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a2e",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "speedybee-f405-v4-50a-esc",
        "category": "esc",
        "name": "BLS 50A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2800,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#001a33",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "geprc-span-f4-45a",
        "category": "esc",
        "name": "SPAN F4 45A AIO ESC",
        "brand": "GEPRC",
        "price_php": 2688,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://geprc.com",
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
        "id": "tmotor-f45a-pro-iii",
        "category": "esc",
        "name": "F45A PRO III 4-in-1",
        "brand": "T-Motor",
        "price_php": 3640,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },

    # ─── FLIGHT CONTROLLERS (6) ────────────────────────────────────────────────
    {
        "id": "speedybee-f405-v4-aio-fc",
        "category": "fc",
        "name": "F405 V4 AIO Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2520,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#001a33",
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
        "id": "mateksys-f405-wing",
        "category": "fc",
        "name": "F405-WING Flight Controller",
        "brand": "Matek",
        "price_php": 1960,
        "weight_g": 11,
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
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "diatone-mamba-mk4-f405",
        "category": "fc",
        "name": "Mamba MK4 F405 AIO FC",
        "brand": "Diatone",
        "price_php": 2240,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002222",
        "specs": {
            "gyro": "MPU6000",
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
    {
        "id": "iflight-succex-e-f7-v2",
        "category": "fc",
        "name": "SucceX-E F7 V2.1 Flight Controller",
        "brand": "iFlight",
        "price_php": 2800,
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
        "id": "geprc-takerg4-fc",
        "category": "fc",
        "name": "TAKER G4 Flight Controller",
        "brand": "GEPRC",
        "price_php": 1680,
        "weight_g": 6,
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
        "id": "flywoo-goku-f745-aio-v2",
        "category": "fc",
        "name": "GOKU F745 AIO V2 Flight Controller",
        "brand": "Flywoo",
        "price_php": 3080,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a2e",
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

    # ─── PROPELLERS (6) ────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-51433",
        "category": "propeller",
        "name": "Hurricane 51433 3-Blade",
        "brand": "Gemfan",
        "price_php": 196,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.33,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "blue"]
        }
    },
    {
        "id": "hqprop-dt5x4-5x3",
        "category": "propeller",
        "name": "DT5X4.5X3 5\" 3-Blade",
        "brand": "HQProp",
        "price_php": 168,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "ethix-s5-v2-prop",
        "category": "propeller",
        "name": "S5 V2 5\" 3-Blade",
        "brand": "Ethix",
        "price_php": 252,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "green", "purple"]
        }
    },
    {
        "id": "iflight-nazgul-5128",
        "category": "propeller",
        "name": "Nazgul 5128 3-Blade",
        "brand": "iFlight",
        "price_php": 196,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "dal-t7056-7inch",
        "category": "propeller",
        "name": "Cyclone T7056 7\" 3-Blade",
        "brand": "DAL",
        "price_php": 280,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 5.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "gemfan-2015-durable",
        "category": "propeller",
        "name": "2015 Durable 2\" 3-Blade",
        "brand": "Gemfan",
        "price_php": 140,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 2,
            "pitch": 1.5,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["black", "white", "yellow"]
        }
    },

    # ─── CAMERAS (6) ───────────────────────────────────────────────────────────
    {
        "id": "runcam-phoenix-2-cam",
        "category": "camera",
        "name": "Phoenix 2 1000TVL Analog",
        "brand": "RunCam",
        "price_php": 1680,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-razer-mini-cam",
        "category": "camera",
        "name": "Razer Mini 1200TVL",
        "brand": "Foxeer",
        "price_php": 1120,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ratel-2-cam",
        "category": "camera",
        "name": "Ratel 2 1200TVL",
        "brand": "Caddx",
        "price_php": 1400,
        "weight_g": 7.6,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" STARVIS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-pro-v2",
        "category": "camera",
        "name": "Avatar HD Pro Kit V2",
        "brand": "Walksnail",
        "price_php": 9520,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "video_system": "Walksnail",
            "resolution": "4K@60fps",
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "hdzero-eco-camera",
        "category": "camera",
        "name": "Eco Digital Camera",
        "brand": "HDZero",
        "price_php": 2520,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 145,
            "format": "Digital",
            "video_system": "HDZero",
            "resolution": "720p90fps",
            "voltage_range": "5V"
        }
    },
    {
        "id": "dji-o4-air-unit-lite",
        "category": "camera",
        "name": "O4 Air Unit Lite",
        "brand": "DJI",
        "price_php": 10024,
        "weight_g": 19,
        "in_stock": True,
        "buy_url": "https://www.dji.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "video_system": "DJI O4",
            "resolution": "4K@60fps",
            "voltage_range": "7.2-26V"
        }
    },

    # ─── VTX (6) ───────────────────────────────────────────────────────────────
    {
        "id": "tbs-unify-pro32-hv-nano",
        "category": "vtx",
        "name": "Unify Pro32 HV Nano VTX",
        "brand": "TBS",
        "price_php": 2240,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#220000",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "foxeer-echo-pit-25-600",
        "category": "vtx",
        "name": "Echo Pit 25-600mW VTX",
        "brand": "Foxeer",
        "price_php": 1008,
        "weight_g": 5,
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
        "id": "rush-tank-solo",
        "category": "vtx",
        "name": "Tank Solo 5.8G VTX",
        "brand": "Rush",
        "price_php": 1960,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "hglrc-sirius-1000-vtx",
        "category": "vtx",
        "name": "Sirius 1000mW 5.8G VTX",
        "brand": "HGLRC",
        "price_php": 1400,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002244",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-tranfpv-vtx",
        "category": "vtx",
        "name": "TranFPV 5.8G 1000mW VTX",
        "brand": "iFlight",
        "price_php": 1232,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "foxeer-tm25-pit-vtx",
        "category": "vtx",
        "name": "TM25 25mW Micro VTX",
        "brand": "Foxeer",
        "price_php": 672,
        "weight_g": 1.5,
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

    # ─── BATTERIES (6) ─────────────────────────────────────────────────────────
    {
        "id": "cnhl-4s-1300mah-100c-mini",
        "category": "battery",
        "name": "MiniStar 4S 1300mAh 100C",
        "brand": "CNHL",
        "price_php": 1008,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com",
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
        "id": "tattu-rline-4-1300mah-4s",
        "category": "battery",
        "name": "R-Line 4.0 4S 1300mAh 150C",
        "brand": "Tattu",
        "price_php": 1232,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://genstattu.com",
        "color": "#220011",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "betafpv-4s-1300mah-75c-batt",
        "category": "battery",
        "name": "4S 1300mAh 75C LiPo",
        "brand": "BetaFPV",
        "price_php": 840,
        "weight_g": 140,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 75,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "authenticrc-6s-1300mah",
        "category": "battery",
        "name": "Authentic RC 6S 1300mAh 100C",
        "brand": "RDQ",
        "price_php": 1400,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#001a00",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "iflight-fullsend-4s-1500mah",
        "category": "battery",
        "name": "FullSend 4S 1500mAh 120C",
        "brand": "iFlight",
        "price_php": 1120,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "smc-4s-1800mah-batt",
        "category": "battery",
        "name": "4S 1800mAh 100C LiPo",
        "brand": "SMC",
        "price_php": 1344,
        "weight_g": 210,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0022",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1800,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },

    # ─── RECEIVERS (6) ─────────────────────────────────────────────────────────
    {
        "id": "betafpv-elrs-nano-rx-v2",
        "category": "receiver",
        "name": "ELRS Nano RX V2",
        "brand": "BetaFPV",
        "price_php": 728,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "radiomaster-rp1-elrs-rx",
        "category": "receiver",
        "name": "RP1 ELRS Nano RX",
        "brand": "RadioMaster",
        "price_php": 560,
        "weight_g": 1,
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
        "id": "iflight-elrs-2-4g-rx",
        "category": "receiver",
        "name": "ELRS 2.4GHz Nano RX",
        "brand": "iFlight",
        "price_php": 672,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "flysky-fgr4-rx",
        "category": "receiver",
        "name": "FGr4 2.4GHz Receiver",
        "brand": "FlySky",
        "price_php": 448,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#001a22",
        "specs": {
            "protocol": "AFHDS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 5
        }
    },
    {
        "id": "jumper-r1-mini-elrs",
        "category": "receiver",
        "name": "R1 Mini ELRS RX",
        "brand": "Jumper",
        "price_php": 616,
        "weight_g": 1,
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
        "id": "expresslrs-rp4td-rx",
        "category": "receiver",
        "name": "RP4TD ELRS Diversity RX",
        "brand": "Happymodel",
        "price_php": 840,
        "weight_g": 2.3,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a0011",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True,
            "range_km": 30
        }
    },

    # ─── GPS MODULES (6) ───────────────────────────────────────────────────────
    {
        "id": "speedybee-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module+Compass",
        "brand": "SpeedyBee",
        "price_php": 1232,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#001a33",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "betafpv-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module+Compass",
        "brand": "BetaFPV",
        "price_php": 1120,
        "weight_g": 10,
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
        "id": "foxeer-m10-mini-gps",
        "category": "gps",
        "name": "M10 Mini GPS+Compass",
        "brand": "Foxeer",
        "price_php": 1064,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#220000",
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
        "id": "tmotor-gps-m8n",
        "category": "gps",
        "name": "M8N GPS Module+Compass",
        "brand": "T-Motor",
        "price_php": 1680,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M8N",
            "update_rate_hz": 18,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "diatone-m10-gps-compass",
        "category": "gps",
        "name": "M10 GPS+Compass Module",
        "brand": "Diatone",
        "price_php": 1176,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002222",
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
        "id": "radiomaster-m9n-gps",
        "category": "gps",
        "name": "M9N GPS Module+Compass",
        "brand": "RadioMaster",
        "price_php": 1568,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 18,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── ANTENNAS (6) ──────────────────────────────────────────────────────────
    {
        "id": "tbs-triumph-antenna",
        "category": "antenna",
        "name": "Triumph 5.8GHz RHCP SMA",
        "brand": "TBS",
        "price_php": 840,
        "weight_g": 10,
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
        "id": "foxeer-lollipop-4-antenna",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP SMA",
        "brand": "Foxeer",
        "price_php": 560,
        "weight_g": 9,
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
        "id": "iflight-microspeedy-antenna",
        "category": "antenna",
        "name": "Microspeedy 5.8GHz RHCP U.FL",
        "brand": "iFlight",
        "price_php": 448,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
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
        "id": "betafpv-lollipop-antenna",
        "category": "antenna",
        "name": "Lollipop 3 5.8GHz RHCP U.FL",
        "brand": "BetaFPV",
        "price_php": 504,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
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
        "id": "hglrc-t-shape-antenna",
        "category": "antenna",
        "name": "T-Shape 5.8GHz RHCP SMA",
        "brand": "HGLRC",
        "price_php": 448,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "rushfpv-tank-antenna",
        "category": "antenna",
        "name": "Tank 5.8GHz RHCP SMA",
        "brand": "RushFPV",
        "price_php": 672,
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
