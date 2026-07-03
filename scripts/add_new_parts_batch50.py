#!/usr/bin/env python3
"""Add a new batch of real, current-production FPV parts across all 11 categories."""
import json

NEW_PARTS = [
    # ========== FRAMES ==========
    {
        "id": "tmotor-velox-fr5-frame",
        "category": "frame",
        "name": "Velox FR5 5\" Freestyle Frame",
        "brand": "T-Motor",
        "price_php": 4480,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=Velox+FR5+Freestyle+Frame",
        "color": "#141414",
        "specs": {
            "size_mm": 227,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tmotor+velox+fr5"
        }
    },
    {
        "id": "hglrc-sector-6-v6-frame",
        "category": "frame",
        "name": "Sector 6 V6 Freestyle Frame",
        "brand": "HGLRC",
        "price_php": 2688,
        "weight_g": 112,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Sector+6+V6+Freestyle+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 254,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5.5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=hglrc+sector+6+v6"
        }
    },
    {
        "id": "geprc-diamond-ace5-frame",
        "category": "frame",
        "name": "Diamond Ace5 5\" Frame",
        "brand": "GEPRC",
        "price_php": 3024,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=Diamond+Ace5+Frame",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 27,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+diamond+ace5"
        }
    },
    {
        "id": "flywoo-firefly-x5-frame",
        "category": "frame",
        "name": "Firefly X5 5\" Frame",
        "brand": "Flywoo",
        "price_php": 2352,
        "weight_g": 84,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Firefly+X5+Frame",
        "color": "#111111",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+firefly+x5"
        }
    },
    {
        "id": "iflight-blitz-ex5-frame",
        "category": "frame",
        "name": "BLITZ EX5 5\" Freestyle Frame",
        "brand": "iFlight",
        "price_php": 2912,
        "weight_g": 94,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=BLITZ+EX5+Freestyle+Frame",
        "color": "#151515",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+blitz+ex5"
        }
    },
    {
        "id": "armattan-rooster-5-frame",
        "category": "frame",
        "name": "Rooster 5\" Freestyle Frame",
        "brand": "Armattan",
        "price_php": 6720,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+5+Freestyle+Frame",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 226,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+5"
        }
    },
    {
        "id": "axisflying-c210-frame",
        "category": "frame",
        "name": "C210 5\" Cinewhoop Frame",
        "brand": "AxisFlying",
        "price_php": 3696,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/search?q=C210+Cinewhoop+Frame",
        "color": "#101010",
        "specs": {
            "size_mm": 210,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+c210+cinewhoop"
        }
    },
    {
        "id": "diatone-roma-f5-v3-frame",
        "category": "frame",
        "name": "Roma F5 V3 Freestyle Frame",
        "brand": "Diatone",
        "price_php": 2576,
        "weight_g": 91,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Roma+F5+V3+Freestyle+Frame",
        "color": "#131313",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 27,
            "thingiverse_url": "https://www.thingiverse.com/search?q=diatone+roma+f5+v3"
        }
    },
    # ========== MOTORS ==========
    {
        "id": "tmotor-velox-2306-5-1900kv",
        "category": "motor",
        "name": "Velox 2306.5 1900KV",
        "brand": "T-Motor",
        "price_php": 1904,
        "weight_g": 31.5,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=Velox+2306.5+1900KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "iflight-xing2-x2306-2700kv",
        "category": "motor",
        "name": "XING2 X2306 2700KV",
        "brand": "iFlight",
        "price_php": 1288,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=XING2+X2306+2700KV",
        "color": "#0d0d0d",
        "specs": {
            "kv": 2700,
            "stator_size": "2306",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "brotherhobby-avenger-2207-2500kv",
        "category": "motor",
        "name": "Avenger 2207.5 2500KV V4",
        "brand": "BrotherHobby",
        "price_php": 1176,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=Avenger+2207.5+2500KV+V4",
        "color": "#141414",
        "specs": {
            "kv": 2500,
            "stator_size": "2207.5",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "flywoo-nin-2207-1750kv",
        "category": "motor",
        "name": "NIN 2207 1750KV",
        "brand": "Flywoo",
        "price_php": 1064,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=NIN+2207+1750KV",
        "color": "#101010",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "hqprop-hglrc-m1808-2450kv",
        "category": "motor",
        "name": "MOTUS M1808 2450KV",
        "brand": "HGLRC",
        "price_php": 896,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=MOTUS+M1808+2450KV",
        "color": "#121212",
        "specs": {
            "kv": 2450,
            "stator_size": "1808",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 4,
            "peak_current_a": 22
        }
    },
    {
        "id": "geprc-speedx-2306-5-1850kv",
        "category": "motor",
        "name": "SPEEDX 2306.5 1850KV",
        "brand": "GEPRC",
        "price_php": 1120,
        "weight_g": 30.5,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=SPEEDX+2306.5+1850KV",
        "color": "#0f0f0f",
        "specs": {
            "kv": 1850,
            "stator_size": "2306.5",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 43
        }
    },
    {
        "id": "emax-eco-ii-2306-1900kv",
        "category": "motor",
        "name": "ECO II 2306 1900KV",
        "brand": "EMAX",
        "price_php": 728,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com/search?q=ECO+II+2306+1900KV",
        "color": "#181818",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "diatone-star-x2306-5-1800kv",
        "category": "motor",
        "name": "STAR X2306.5 1800KV",
        "brand": "Diatone",
        "price_php": 952,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=STAR+X2306.5+1800KV",
        "color": "#141414",
        "specs": {
            "kv": 1800,
            "stator_size": "2306.5",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },
    # ========== ESC ==========
    {
        "id": "tmotor-f60-pro-v-60a-4in1",
        "category": "esc",
        "name": "F60 PRO V 60A 4-in-1",
        "brand": "T-Motor",
        "price_php": 3808,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F60+PRO+V+60A+4-in-1",
        "color": "#000022",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "speedybee-f405-v4-55a-4in1",
        "category": "esc",
        "name": "F405 V4 55A BLHeli_32 4-in-1",
        "brand": "SpeedyBee",
        "price_php": 3136,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=F405+V4+55A+4-in-1+ESC",
        "color": "#001133",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "iflight-blitz-e55-4in1",
        "category": "esc",
        "name": "BLITZ E55 55A 4-in-1",
        "brand": "iFlight",
        "price_php": 3360,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=BLITZ+E55+55A+4-in-1+ESC",
        "color": "#111133",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "holybro-tekko32-f4-50a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1",
        "brand": "Holybro",
        "price_php": 2856,
        "weight_g": 12.5,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Tekko32+F4+50A+4-in-1+ESC",
        "color": "#000f22",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "hglrc-fd45-45a-4in1",
        "category": "esc",
        "name": "FD45 45A BL32 4-in-1",
        "brand": "HGLRC",
        "price_php": 2296,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=FD45+45A+4-in-1+ESC",
        "color": "#111122",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "flywoo-goku-gn-745-45a-4in1",
        "category": "esc",
        "name": "GOKU GN 745 45A 4-in-1",
        "brand": "Flywoo",
        "price_php": 2016,
        "weight_g": 10.5,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=GOKU+GN+745+45A+4-in-1+ESC",
        "color": "#0d0d1a",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    # ========== FLIGHT CONTROLLERS ==========
    {
        "id": "speedybee-f405-v4-stack-fc",
        "category": "fc",
        "name": "F405 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2072,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=F405+V4+Flight+Controller",
        "color": "#001133",
        "specs": {
            "gyro": "ICM42688P",
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
        "id": "holybro-kakute-h7-mini-v3-fc",
        "category": "fc",
        "name": "Kakute H7 Mini V3 Flight Controller",
        "brand": "Holybro",
        "price_php": 2744,
        "weight_g": 6.2,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Kakute+H7+Mini+V3+Flight+Controller",
        "color": "#000f22",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "iflight-blitz-f7-pro-fc",
        "category": "fc",
        "name": "BLITZ F7 Pro Flight Controller",
        "brand": "iFlight",
        "price_php": 2408,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=BLITZ+F7+Pro+Flight+Controller",
        "color": "#111133",
        "specs": {
            "gyro": "ICM42688P",
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
        "id": "hglrc-zeus-f745-fc",
        "category": "fc",
        "name": "Zeus F745 Flight Controller",
        "brand": "HGLRC",
        "price_php": 2184,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Zeus+F745+Flight+Controller",
        "color": "#111122",
        "specs": {
            "gyro": "ICM42688P",
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
        "id": "matek-f405-teensy-v2-fc",
        "category": "fc",
        "name": "F405-TeensyV2 Flight Controller",
        "brand": "Matek",
        "price_php": 1848,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F405-TeensyV2+Flight+Controller",
        "color": "#0a0a0a",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": False
        }
    },
    # ========== PROPELLERS ==========
    {
        "id": "hqprop-r38-5x3-8x3-tri",
        "category": "propeller",
        "name": "R38 5.3x3.8x3 Tri-Blade",
        "brand": "HQProp",
        "price_php": 336,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+R38+5.3x3.8x3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.3,
            "pitch": 3.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "black"]
        }
    },
    {
        "id": "gemfan-hurricane-51466-tri",
        "category": "propeller",
        "name": "Hurricane 51466 Tri-Blade",
        "brand": "Gemfan",
        "price_php": 280,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466",
        "color": "#151515",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.66,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "green", "gray"]
        }
    },
    {
        "id": "azure-power-vanover-v2-5148",
        "category": "propeller",
        "name": "Vanover V2 5148 Tri-Blade",
        "brand": "Azure",
        "price_php": 252,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Azure+Vanover+V2+5148",
        "color": "#181818",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    {
        "id": "dalprop-cyclone-t5049c",
        "category": "propeller",
        "name": "Cyclone T5049C Tri-Blade",
        "brand": "DAL",
        "price_php": 224,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DALProp+Cyclone+T5049C",
        "color": "#141414",
        "specs": {
            "diameter_inch": 5.0,
            "pitch": 4.9,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "hqprop-6x4-5x3-6inch",
        "category": "propeller",
        "name": "6x4.5x3 6\" Tri-Blade",
        "brand": "HQProp",
        "price_php": 364,
        "weight_g": 6.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+6x4.5x3",
        "color": "#191919",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "black"]
        }
    },
    # ========== CAMERAS ==========
    {
        "id": "walksnail-avatar-hd-v3-nano-cam",
        "category": "camera",
        "name": "Avatar HD V3 Nano Camera",
        "brand": "Walksnail",
        "price_php": 4032,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+V3+Nano+Camera",
        "color": "#0a0a0a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 155,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "6-28V"
        }
    },
    {
        "id": "caddx-ratel-3-analog-cam",
        "category": "camera",
        "name": "Ratel 3 1200TVL Analog Camera",
        "brand": "Caddx",
        "price_php": 1400,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ratel+3+1200TVL+Analog+Camera",
        "color": "#121212",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-phoenix-3-nano-cam",
        "category": "camera",
        "name": "Phoenix 3 Nano Camera",
        "brand": "RunCam",
        "price_php": 1288,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Phoenix+3+Nano+Camera",
        "color": "#101010",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-razer-4k-cam",
        "category": "camera",
        "name": "Razer 4K Micro Camera",
        "brand": "Foxeer",
        "price_php": 3248,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Razer+4K+Micro+Camera",
        "color": "#0f0f0f",
        "specs": {
            "sensor": "1/2.3\" CMOS",
            "fov_deg": 145,
            "format": "Digital 4K",
            "tvl": 1600,
            "voltage_range": "5-25V"
        }
    },
    # ========== VTX ==========
    {
        "id": "walksnail-avatar-hd-v3-vtx",
        "category": "vtx",
        "name": "Avatar HD V3 1W VTX",
        "brand": "Walksnail",
        "price_php": 7280,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+V3+1W+VTX",
        "color": "#0a0a0a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Digital HD",
            "bands": "N/A",
            "voltage_range": "6-28V",
            "connector": "U.FL"
        }
    },
    {
        "id": "hdzero-freestyle-v2-vtx",
        "category": "vtx",
        "name": "Freestyle V2 VTX",
        "brand": "HDZero",
        "price_php": 4256,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Freestyle+V2+VTX",
        "color": "#101010",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Digital HD",
            "bands": "N/A",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "tbs-unify-evo-nano-vtx",
        "category": "vtx",
        "name": "Unify Evo Nano VTX",
        "brand": "TBS",
        "price_php": 3080,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Evo+Nano+VTX",
        "color": "#151515",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rush-tank-solo-vtx",
        "category": "vtx",
        "name": "Tank Solo 500mW VTX",
        "brand": "RUSH",
        "price_php": 1904,
        "weight_g": 5.4,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Tank+Solo+500mW+VTX",
        "color": "#121212",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    # ========== BATTERIES ==========
    {
        "id": "tattu-rline-v5-6s-1400mah",
        "category": "battery",
        "name": "R-Line V5 1400mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 3080,
        "weight_g": 265,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5+1400mAh+6S+130C",
        "color": "#003322",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-mini-black-series-4s-1500mah",
        "category": "battery",
        "name": "MiniStar Black Series 1500mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1512,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniStar+Black+Series+1500mAh+4S+100C",
        "color": "#111111",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gnb-6s-1300mah-120c",
        "category": "battery",
        "name": "6S 1300mAh 120C",
        "brand": "GNB",
        "price_php": 2688,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+6S+1300mAh+120C",
        "color": "#0d0d0d",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-mini-tank-6s-1100mah",
        "category": "battery",
        "name": "MiniTank 1100mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2408,
        "weight_g": 205,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniTank+1100mAh+6S+100C",
        "color": "#151515",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-rline-v5-4s-1300mah",
        "category": "battery",
        "name": "R-Line V5 1300mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1736,
        "weight_g": 158,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5+1300mAh+4S+130C",
        "color": "#003322",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    # ========== RECEIVERS ==========
    {
        "id": "radiomaster-rp4-elrs-receiver",
        "category": "receiver",
        "name": "RP4 ExpressLRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 784,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RP4+ExpressLRS+Nano+Receiver",
        "color": "#222266",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-el24e-elrs-receiver",
        "category": "receiver",
        "name": "EL24E ExpressLRS 2.4GHz Receiver",
        "brand": "HappyModel",
        "price_php": 672,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EL24E+ExpressLRS+2.4GHz+Receiver",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "tbs-crossfire-diversity-nano-rx",
        "category": "receiver",
        "name": "Crossfire Diversity Nano RX SE",
        "brand": "TBS",
        "price_php": 1848,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Diversity+Nano+RX+SE",
        "color": "#151515",
        "specs": {
            "protocol": "TBS Crossfire",
            "frequency_mhz": 915,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "betafpv-elrs-nano-rx-v3",
        "category": "receiver",
        "name": "ELRS Nano Receiver V3",
        "brand": "BetaFPV",
        "price_php": 616,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=BetaFPV+ELRS+Nano+Receiver+V3",
        "color": "#111",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    # ========== GPS ==========
    {
        "id": "holybro-m10-gps-compass",
        "category": "gps",
        "name": "M10 GPS + Compass",
        "brand": "Holybro",
        "price_php": 1904,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=M10+GPS+Compass",
        "color": "#000f22",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 11,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "speedybee-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1568,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=M10+GPS+Module",
        "color": "#001133",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 12,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS + Compass",
        "brand": "Matek",
        "price_php": 1736,
        "weight_g": 9.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-5883+GPS+Compass",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 11,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    # ========== ANTENNAS ==========
    {
        "id": "rushfpv-cherry-lollipop-sma",
        "category": "antenna",
        "name": "Cherry Lollipop 5.8GHz SMA Antenna",
        "brand": "Rush",
        "price_php": 560,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Cherry+Lollipop+5.8GHz+SMA+Antenna",
        "color": "#121212",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.3,
            "type": "cloverleaf"
        }
    },
    {
        "id": "tbs-triumph-pro-sma",
        "category": "antenna",
        "name": "Triumph Pro 5.8GHz SMA Antenna",
        "brand": "TBS",
        "price_php": 896,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Triumph+Pro+5.8GHz+SMA+Antenna",
        "color": "#151515",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.6,
            "type": "cloverleaf"
        }
    },
    {
        "id": "walksnail-5-8ghz-omni-sma",
        "category": "antenna",
        "name": "5.8GHz Omni Antenna SMA",
        "brand": "Walksnail",
        "price_php": 448,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=5.8GHz+Omni+Antenna+SMA",
        "color": "#0a0a0a",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.0,
            "type": "cloverleaf"
        }
    },
    {
        "id": "foxeer-lollipop-4-sma",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz SMA Antenna",
        "brand": "Foxeer",
        "price_php": 588,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Lollipop+4+SMA+Antenna",
        "color": "#151515",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.4,
            "type": "cloverleaf"
        }
    },
]


def main():
    with open("data/parts.json", "r") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    added = 0
    skipped = 0

    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"  SKIP (duplicate): {part['id']}")
            skipped += 1
        else:
            data["parts"].append(part)
            existing_ids.add(part["id"])
            added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = len(data["parts"])
    print(f"\nAdded {added} new parts (skipped {skipped} duplicates)")
    print(f"Total parts now: {total}")

    from collections import Counter
    cats = Counter(p["category"] for p in data["parts"])
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
