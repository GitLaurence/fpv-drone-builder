#!/usr/bin/env python3
"""Add new FPV parts across all 11 categories to parts.json (long-range / niche variants)"""
import json

NEW_PARTS = [
    # ─── FRAMES (6) ─────────────────────────────────────────────────────────
    {
        "id": "flywoo-firefly-2-cinewhoop-frame",
        "category": "frame",
        "name": "Firefly 2\" Cinewhoop Frame",
        "brand": "Flywoo",
        "price_php": 1450,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://flywoo.net/collections/frame-kits",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 100,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 2,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 15,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+firefly+2+cinewhoop"
        }
    },
    {
        "id": "geprc-cinelog20-frame",
        "category": "frame",
        "name": "CineLog20 2\" Cinewhoop Frame",
        "brand": "GEPRC",
        "price_php": 1700,
        "weight_g": 42,
        "in_stock": True,
        "buy_url": "https://geprc.com/collections/frame-kits",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 105,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 2,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 15,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+cinelog20"
        }
    },
    {
        "id": "iflight-bumblebee-6-frame",
        "category": "frame",
        "name": "BumbleBee 6\" Frame",
        "brand": "iFlight",
        "price_php": 4200,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/collections/frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 260,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+bumblebee"
        }
    },
    {
        "id": "armattan-marmotte-7-frame",
        "category": "frame",
        "name": "Marmotte 7\" Long Range Frame",
        "brand": "Armattan",
        "price_php": 7200,
        "weight_g": 135,
        "in_stock": True,
        "buy_url": "https://www.armattanproductions.com/collections/frames",
        "color": "#2b2b2b",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+marmotte"
        }
    },
    {
        "id": "tbs-source-one-v5-7",
        "category": "frame",
        "name": "Source One V5 7\" Long Range",
        "brand": "TBS",
        "price_php": 1950,
        "weight_g": 110,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/cat:source_one",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+7"
        }
    },
    {
        "id": "flywoo-explorer-lr6-frame",
        "category": "frame",
        "name": "Explorer LR6 6\" Long Range",
        "brand": "Flywoo",
        "price_php": 3800,
        "weight_g": 128,
        "in_stock": True,
        "buy_url": "https://flywoo.net/collections/frame-kits",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 255,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr6"
        }
    },

    # ─── MOTORS (6) ─────────────────────────────────────────────────────────
    {
        "id": "tmotor-mn3110-700kv",
        "category": "motor",
        "name": "MN3110 700KV Long Range",
        "brand": "T-Motor",
        "price_php": 2400,
        "weight_g": 68,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/collections/multi-rotor",
        "color": "#c0c0c0",
        "specs": {
            "kv": 700,
            "stator_size": "3110",
            "motor_mount_mm": 19,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 30
        }
    },
    {
        "id": "iflight-xing-e-pro-2806-1300kv",
        "category": "motor",
        "name": "XING-E Pro 2806 1300KV",
        "brand": "iFlight",
        "price_php": 1450,
        "weight_g": 49,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/collections/motor",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1300,
            "stator_size": "2806",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },
    {
        "id": "brotherhobby-avenger-2812-920kv",
        "category": "motor",
        "name": "Avenger 2812 920KV",
        "brand": "BrotherHobby",
        "price_php": 1550,
        "weight_g": 62,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/motors.html",
        "color": "#3a3a3a",
        "specs": {
            "kv": 920,
            "stator_size": "2812",
            "motor_mount_mm": 19,
            "min_voltage_s": 5,
            "max_voltage_s": 8,
            "shaft_mm": 5,
            "peak_current_a": 33
        }
    },
    {
        "id": "flywoo-robo-1606-3300kv",
        "category": "motor",
        "name": "ROBO 1606 3300KV",
        "brand": "Flywoo",
        "price_php": 620,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://flywoo.net/collections/motor",
        "color": "#1a1a1a",
        "specs": {
            "kv": 3300,
            "stator_size": "1606",
            "motor_mount_mm": 9,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 18
        }
    },
    {
        "id": "tmotor-f100-2807-1300kv",
        "category": "motor",
        "name": "F100 2807 1300KV",
        "brand": "T-Motor",
        "price_php": 1700,
        "weight_g": 51,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/collections/fpv-freestyle-series",
        "color": "#101010",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "xnova-lightning-2806-1300kv",
        "category": "motor",
        "name": "Lightning 2806 1300KV",
        "brand": "Xnova",
        "price_php": 1600,
        "weight_g": 50,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/motors.html",
        "color": "#0a0a0a",
        "specs": {
            "kv": 1300,
            "stator_size": "2806",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },

    # ─── ESC (5) ────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-65a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 65A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3100,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://holybro.com/collections/esc",
        "color": "#0d0d0d",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "mamba-f80-80a-4in1",
        "category": "esc",
        "name": "Mamba F80 80A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 3400,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/collections/esc",
        "color": "#1c1c1c",
        "specs": {
            "amp_rating": 80,
            "input_voltage_s": 8,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 95
        }
    },
    {
        "id": "iflight-blitz-e80-4in1",
        "category": "esc",
        "name": "BLITZ E80 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 3300,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/collections/esc",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 80,
            "input_voltage_s": 8,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 90
        }
    },
    {
        "id": "flywoo-goku-gn-405-30a",
        "category": "esc",
        "name": "GOKU GN405 30A 4-in-1 ESC",
        "brand": "Flywoo",
        "price_php": 1400,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://flywoo.net/collections/esc",
        "color": "#0d0d0d",
        "specs": {
            "amp_rating": 30,
            "input_voltage_s": 4,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 38
        }
    },
    {
        "id": "speedybee-bls-50a-4in1",
        "category": "esc",
        "name": "BLS 50A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 1850,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/collections/esc",
        "color": "#101820",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },

    # ─── FLIGHT CONTROLLERS (5) ─────────────────────────────────────────────
    {
        "id": "happymodel-crazybee-f4-aio",
        "category": "fc",
        "name": "CrazyBee F4 AIO FC",
        "brand": "HappyModel",
        "price_php": 950,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn/index.php/product-category/flight-controller/",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 16,
            "barometer": False,
            "blackbox": False,
            "uart_count": 3,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "speedybee-f745-v3-aio-fc",
        "category": "fc",
        "name": "F745 V3 AIO FC",
        "brand": "SpeedyBee",
        "price_php": 1500,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/collections/flight-controller",
        "color": "#101820",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "matek-f722-wing-fc",
        "category": "fc",
        "name": "F722-WING FC",
        "brand": "Matek",
        "price_php": 2900,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?p=4014",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 36,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "iflight-blitz-f7-pro-fc",
        "category": "fc",
        "name": "BLITZ F7 Pro FC",
        "brand": "iFlight",
        "price_php": 2500,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/collections/flight-controller",
        "color": "#1a1a1a",
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
    {
        "id": "holybro-kakute-f7-hdv-fc",
        "category": "fc",
        "name": "Kakute F7 HDV FC",
        "brand": "Holybro",
        "price_php": 2800,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com/collections/flight-controllers",
        "color": "#0d0d0d",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (6) ─────────────────────────────────────────────────────
    {
        "id": "hqprop-9x4-5x3-v1s",
        "category": "propeller",
        "name": "9X4.5X3 V1S 9-inch",
        "brand": "HQProp",
        "price_php": 320,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com/collections/9-inch-prop",
        "color": "#111111",
        "specs": {
            "diameter_inch": 9,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 6,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "gemfan-10x4-5x4-hd",
        "category": "propeller",
        "name": "10X4.5X4 10-inch",
        "brand": "Gemfan",
        "price_php": 380,
        "weight_g": 12.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/propellers.html",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 10,
            "pitch": 4.5,
            "blade_count": 4,
            "shaft_mm": 6,
            "color_options": ["black"]
        }
    },
    {
        "id": "dal-cyclone-t9045",
        "category": "propeller",
        "name": "Cyclone T9045 9-inch",
        "brand": "DAL",
        "price_php": 310,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/collections/propellers",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 9,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 6,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "gemfan-2015-2-blade-whoop",
        "category": "propeller",
        "name": "2015 2-Blade Whoop Prop",
        "brand": "Gemfan",
        "price_php": 90,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/propellers.html",
        "color": "#111111",
        "specs": {
            "diameter_inch": 2,
            "pitch": 1.5,
            "blade_count": 2,
            "shaft_mm": 1,
            "color_options": ["black", "grey", "transparent"]
        }
    },
    {
        "id": "hqprop-10x5x3-v1s",
        "category": "propeller",
        "name": "10X5X3 V1S 10-inch",
        "brand": "HQProp",
        "price_php": 400,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com/collections/10-inch-prop",
        "color": "#111111",
        "specs": {
            "diameter_inch": 10,
            "pitch": 5,
            "blade_count": 3,
            "shaft_mm": 6,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "dal-cyclone-t7056-tri-blade",
        "category": "propeller",
        "name": "Cyclone T7056 Tri-Blade 7-inch",
        "brand": "DAL",
        "price_php": 240,
        "weight_g": 7.2,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/collections/propellers",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 7,
            "pitch": 5.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },

    # ─── FPV CAMERAS (4) ────────────────────────────────────────────────────
    {
        "id": "walksnail-avatar-hd-v3-camera",
        "category": "camera",
        "name": "Avatar HD V3 Camera",
        "brand": "Walksnail",
        "price_php": 2900,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com/collections/avatar-hd-system",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 150,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "6.5-27V"
        }
    },
    {
        "id": "hdzero-mini-v3-camera",
        "category": "camera",
        "name": "HDZero Mini V3 Camera",
        "brand": "HDZero",
        "price_php": 2600,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com/collections/cameras",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 150,
            "format": "Digital HD",
            "tvl": 1000,
            "voltage_range": "6.5-25.2V"
        }
    },
    {
        "id": "runcam-night-eagle-3-camera",
        "category": "camera",
        "name": "Night Eagle 3 FPV Camera",
        "brand": "RunCam",
        "price_php": 1700,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/collections/fpv-camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-falkor-3-camera",
        "category": "camera",
        "name": "Falkor 3 FPV Camera",
        "brand": "Foxeer",
        "price_php": 1300,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/collections/fpv-camera",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },

    # ─── VIDEO TRANSMITTERS (4) ─────────────────────────────────────────────
    {
        "id": "walksnail-avatar-hd-vtx-v3",
        "category": "vtx",
        "name": "Avatar HD VTX V3",
        "brand": "Walksnail",
        "price_php": 4200,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com/collections/avatar-hd-system",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital HD",
            "bands": "5.8GHz",
            "voltage_range": "7-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hdzero-whoop-vtx",
        "category": "vtx",
        "name": "HDZero Whoop VTX",
        "brand": "HDZero",
        "price_php": 2400,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com/collections/vtx",
        "color": "#0d0d0d",
        "specs": {
            "power_mw_max": 200,
            "protocol": "Digital HD",
            "bands": "5.8GHz",
            "voltage_range": "3.5-6.5V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rushfpv-tank-ultimate-v5",
        "category": "vtx",
        "name": "Tank Ultimate V5 VTX",
        "brand": "RushFPV",
        "price_php": 3300,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/collections/video-transmitters",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "6-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-onair-vtx-pro",
        "category": "vtx",
        "name": "OnAir VTX Pro",
        "brand": "iFlight",
        "price_php": 1950,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/collections/fpv-system",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (6) ──────────────────────────────────────────────────────
    {
        "id": "tattu-8s-1300mah-120c",
        "category": "battery",
        "name": "8S 1300mAh 120C",
        "brand": "Tattu",
        "price_php": 3500,
        "weight_g": 320,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com/tattu-r-line.html",
        "color": "#1a1a2e",
        "specs": {
            "cell_count_s": 8,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 29.6
        }
    },
    {
        "id": "cnhl-8s-1500mah-100c",
        "category": "battery",
        "name": "8S 1500mAh 100C",
        "brand": "CNHL",
        "price_php": 3700,
        "weight_g": 365,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/batteries.html",
        "color": "#000000",
        "specs": {
            "cell_count_s": 8,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 29.6
        }
    },
    {
        "id": "gensace-8s-1100mah-100c",
        "category": "battery",
        "name": "8S 1100mAh 100C",
        "brand": "Gens Ace",
        "price_php": 3300,
        "weight_g": 290,
        "in_stock": True,
        "buy_url": "https://www.gensace.de/lipo-battery",
        "color": "#0a3d62",
        "specs": {
            "cell_count_s": 8,
            "capacity_mah": 1100,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 29.6
        }
    },
    {
        "id": "ovonic-6s-2200mah-100c",
        "category": "battery",
        "name": "6S 2200mAh 100C",
        "brand": "Ovonic",
        "price_php": 2700,
        "weight_g": 340,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/batteries.html",
        "color": "#1a1a1a",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 2200,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-2s-650mah-100c-whoop",
        "category": "battery",
        "name": "2S 650mAh 100C Whoop",
        "brand": "CNHL",
        "price_php": 380,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/batteries.html",
        "color": "#000000",
        "specs": {
            "cell_count_s": 2,
            "capacity_mah": 650,
            "c_rating": 100,
            "connector": "PH2.0",
            "voltage_nominal": 7.4
        }
    },
    {
        "id": "tattu-12s-1400mah-100c",
        "category": "battery",
        "name": "12S 1400mAh 100C",
        "brand": "Tattu",
        "price_php": 5200,
        "weight_g": 480,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com/tattu-r-line.html",
        "color": "#1a1a2e",
        "specs": {
            "cell_count_s": 12,
            "capacity_mah": 1400,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 44.4
        }
    },

    # ─── RC RECEIVERS (4) ───────────────────────────────────────────────────
    {
        "id": "happymodel-ep2-elrs-900-rx",
        "category": "receiver",
        "name": "EP2 ELRS 900MHz RX",
        "brand": "HappyModel",
        "price_php": 850,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn/index.php/product-category/elrs-series/",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "radiomaster-rp4td-900-rx",
        "category": "receiver",
        "name": "RP4TD 900MHz True Diversity ELRS RX",
        "brand": "RadioMaster",
        "price_php": 1650,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/collections/receivers",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 35
        }
    },
    {
        "id": "immersionrc-ghost-lite-rx",
        "category": "receiver",
        "name": "Ghost Lite RX",
        "brand": "ImmersionRC",
        "price_php": 950,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com/fpv-products/ghost/",
        "color": "#0d0d0d",
        "specs": {
            "protocol": "Ghost",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 18
        }
    },
    {
        "id": "frsky-r9-slim-mx-receiver",
        "category": "receiver",
        "name": "R9 Slim MX Receiver",
        "brand": "FrSky",
        "price_php": 1500,
        "weight_g": 2.5,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com/product-category/receivers/",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 18
        }
    },

    # ─── GPS MODULES (4) ────────────────────────────────────────────────────
    {
        "id": "holybro-here3-plus-rtk-gps",
        "category": "gps",
        "name": "Here3+ RTK GNSS GPS",
        "brand": "Holybro",
        "price_php": 8200,
        "weight_g": 37,
        "in_stock": True,
        "buy_url": "https://holybro.com/collections/gps",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox F9P RTK",
            "update_rate_hz": 10,
            "fix_time_s": 15,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "cuav-neo-3-pro-gps",
        "category": "gps",
        "name": "NEO 3 Pro GPS",
        "brand": "CUAV",
        "price_php": 3200,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.cuav.net/en/neo3/",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS",
        "brand": "Matek",
        "price_php": 1450,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?p=4992",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "beitian-bn-880t-gps",
        "category": "gps",
        "name": "BN-880T GPS+Compass",
        "brand": "Beitian",
        "price_php": 980,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/gps.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 24,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (5) ───────────────────────────────────────────────────
    {
        "id": "truerc-x-air-helical-antenna",
        "category": "antenna",
        "name": "X-Air Helical Antenna 5.8GHz",
        "brand": "TrueRC",
        "price_php": 1300,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/antennas.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "helical"
        }
    },
    {
        "id": "foxeer-cloverleaf-antenna",
        "category": "antenna",
        "name": "Cloverleaf Antenna 5.8GHz",
        "brand": "Foxeer",
        "price_php": 380,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/collections/antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    },
    {
        "id": "menace-rc-patch-antenna",
        "category": "antenna",
        "name": "Patch Antenna 5.8GHz 14dBi",
        "brand": "Menace Antennas",
        "price_php": 2200,
        "weight_g": 60,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/antennas.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 14,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
        }
    },
    {
        "id": "rushfpv-cherry-omni-antenna-set",
        "category": "antenna",
        "name": "Cherry Omni Antenna Set 5.8GHz",
        "brand": "RushFPV",
        "price_php": 850,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/collections/antennas",
        "color": "#aa1133",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omnidirectional"
        }
    },
    {
        "id": "tbs-triumph-pro-antenna",
        "category": "antenna",
        "name": "Triumph Pro Antenna 5.8GHz",
        "brand": "TBS",
        "price_php": 800,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/cat:antennas",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.2,
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
    new_ids = [p["id"] for p in NEW_PARTS]

    if len(new_ids) != len(set(new_ids)):
        seen = set()
        dupes = set()
        for i in new_ids:
            if i in seen:
                dupes.add(i)
            seen.add(i)
        raise SystemExit(f"Duplicate IDs within new parts: {dupes}")

    dupes = existing_ids & set(new_ids)
    if dupes:
        raise SystemExit(f"Duplicate IDs found: {dupes}")

    data["parts"].extend(NEW_PARTS)

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

    print(f"Added {len(NEW_PARTS)} new parts. Total now: {len(data['parts'])}")


if __name__ == "__main__":
    main()
