#!/usr/bin/env python3
"""Add new real FPV parts to parts.json - Batch 47: 88 new parts across all 11 categories."""
import json

NEW_PARTS = [
    # ========== FRAMES ==========
    {
        "id": "ummagawd-og-v2-5",
        "category": "frame",
        "name": "OG V2 5\" Frame",
        "brand": "Ummagawd",
        "price_php": 5040,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Ummagawd+OG+V2",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=ummagawd+og"
        }
    },
    {
        "id": "flywoo-mr-croc-35-hd-frame",
        "category": "frame",
        "name": "Mr.Croc 3.5\" HD Frame Kit",
        "brand": "Flywoo",
        "price_php": 3500,
        "weight_g": 45,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+Mr.Croc+3.5+HD",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 22,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+mr+croc"
        }
    },
    {
        "id": "geprc-cinelog25-v2-frame",
        "category": "frame",
        "name": "Cinelog25 V2 Frame",
        "brand": "GEPRC",
        "price_php": 3080,
        "weight_g": 60,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+Cinelog25+V2",
        "color": "#111111",
        "specs": {
            "size_mm": 135,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 18,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+cinelog25"
        }
    },
    {
        "id": "iflight-nazgul-evoque-f6-frame",
        "category": "frame",
        "name": "Nazgul Evoque F6 6\" Frame",
        "brand": "iFlight",
        "price_php": 4480,
        "weight_g": 115,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+Nazgul+Evoque+F6",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 260,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+nazgul+evoque+f6"
        }
    },
    {
        "id": "lumenier-qav-s-5-frame",
        "category": "frame",
        "name": "QAV-S 5\" Racing Frame",
        "brand": "Lumenier",
        "price_php": 3640,
        "weight_g": 85,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com/search?q=Lumenier+QAV-S+5",
        "color": "#151515",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=lumenier+qav-s"
        }
    },
    {
        "id": "hglrc-sector5-v5-frame",
        "category": "frame",
        "name": "Sector5 V5 Frame",
        "brand": "HGLRC",
        "price_php": 2800,
        "weight_g": 87,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Sector5+V5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=hglrc+sector5"
        }
    },
    {
        "id": "axisflying-manta-5-frame",
        "category": "frame",
        "name": "Manta 5\" Frame",
        "brand": "AxisFlying",
        "price_php": 4200,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/search?q=AxisFlying+Manta+5",
        "color": "#101010",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+manta"
        }
    },
    {
        "id": "armattan-marmotte-6-hd-frame",
        "category": "frame",
        "name": "Marmotte 6\" HD Frame",
        "brand": "Armattan",
        "price_php": 5600,
        "weight_g": 110,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Armattan+Marmotte+6+HD",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 260,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+marmotte+6"
        }
    },
    # ========== MOTORS ==========
    {
        "id": "tmotor-velox-2207-5-1750kv",
        "category": "motor",
        "name": "Velox 2207.5 1750KV",
        "brand": "T-Motor",
        "price_php": 2240,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=T-Motor+Velox+2207.5+1750KV",
        "color": "#440000",
        "specs": {
            "kv": 1750,
            "stator_size": "2207.5",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "iflight-xing2-2306-1700kv",
        "category": "motor",
        "name": "XING2 2306 1700KV",
        "brand": "iFlight",
        "price_php": 1680,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+XING2+2306+1700KV",
        "color": "#003366",
        "specs": {
            "kv": 1700,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "brotherhobby-avenger-2-2306-5-1900kv",
        "category": "motor",
        "name": "Avenger 2 2306.5 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1848,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=BrotherHobby+Avenger+2+2306.5+1900KV",
        "color": "#222222",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },
    {
        "id": "emax-eco-ii-2306-1900kv",
        "category": "motor",
        "name": "ECO II 2306 1900KV",
        "brand": "EMAX",
        "price_php": 1064,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com/search?q=EMAX+ECO+II+2306+1900KV",
        "color": "#333333",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "rcinpower-gts-v2-2207-2450kv",
        "category": "motor",
        "name": "GTS V2 2207 2450KV",
        "brand": "RCINPower",
        "price_php": 1512,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RCINPower+GTS+V2+2207+2450KV",
        "color": "#003300",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 37
        }
    },
    {
        "id": "hobbywing-xrotor-2207-2400kv",
        "category": "motor",
        "name": "XRotor 2207 2400KV",
        "brand": "Hobbywing",
        "price_php": 1680,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Hobbywing+XRotor+2207+2400KV",
        "color": "#004488",
        "specs": {
            "kv": 2400,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "flywoo-robo-2306-5-1600kv",
        "category": "motor",
        "name": "ROBO 2306.5 1600KV",
        "brand": "Flywoo",
        "price_php": 1400,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+ROBO+2306.5+1600KV",
        "color": "#1c1c1c",
        "specs": {
            "kv": 1600,
            "stator_size": "2306.5",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "hglrc-speed-master-2207-5-1755kv",
        "category": "motor",
        "name": "Speed Master 2207.5 1755KV",
        "brand": "HGLRC",
        "price_php": 1288,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Speed+Master+2207.5+1755KV",
        "color": "#111111",
        "specs": {
            "kv": 1755,
            "stator_size": "2207.5",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    # ========== ESC ==========
    {
        "id": "hobbywing-xrotor-micro-60a-4in1",
        "category": "esc",
        "name": "XRotor Micro 60A 4-in-1",
        "brand": "Hobbywing",
        "price_php": 2800,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Hobbywing+XRotor+Micro+60A+4-in-1",
        "color": "#004488",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 70
        }
    },
    {
        "id": "tmotor-f55a-pro-ii-4in1",
        "category": "esc",
        "name": "F55A PRO II 4-in-1",
        "brand": "T-Motor",
        "price_php": 3920,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=T-Motor+F55A+PRO+II+4-in-1",
        "color": "#440000",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "flycolor-raptor-60a-4in1",
        "category": "esc",
        "name": "Raptor 60A 4-in-1",
        "brand": "Flycolor",
        "price_php": 2464,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+Raptor+60A+4-in-1",
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
        "id": "speedybee-55a-4in1-bls",
        "category": "esc",
        "name": "55A 4-in-1 BLS ESC",
        "brand": "SpeedyBee",
        "price_php": 2688,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+55A+4-in-1+BLS+ESC",
        "color": "#0055aa",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "diatone-mamba-f50-50a-4in1",
        "category": "esc",
        "name": "Mamba F50 50A 4-in-1",
        "brand": "Diatone",
        "price_php": 2240,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Diatone+Mamba+F50+50A+4-in-1",
        "color": "#111133",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 60
        }
    },
    {
        "id": "foxeer-reaper-50a-4in1-mini",
        "category": "esc",
        "name": "Reaper 50A 4-in-1 Mini",
        "brand": "Foxeer",
        "price_php": 2016,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Reaper+50A+4-in-1+Mini",
        "color": "#660000",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 60
        }
    },
    {
        "id": "geprc-taker-g4-45a-4in1",
        "category": "esc",
        "name": "TAKER G4 45A 4-in-1",
        "brand": "GEPRC",
        "price_php": 1960,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+TAKER+G4+45A+4-in-1",
        "color": "#111111",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "iflight-blitz-e55-4in1",
        "category": "esc",
        "name": "BLITZ E55 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 2632,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+BLITZ+E55+4-in-1+ESC",
        "color": "#003366",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    # ========== FLIGHT CONTROLLERS ==========
    {
        "id": "foxeer-f722-mini-v4-fc",
        "category": "fc",
        "name": "F722 Mini V4 Flight Controller",
        "brand": "Foxeer",
        "price_php": 2464,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+F722+Mini+V4+Flight+Controller",
        "color": "#660000",
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
    {
        "id": "holybro-kakute-h7-v2-fc",
        "category": "fc",
        "name": "Kakute H7 V2 Flight Controller",
        "brand": "Holybro",
        "price_php": 3808,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+Kakute+H7+V2+Flight+Controller",
        "color": "#0033aa",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "geprc-taker-f722-mini-fc",
        "category": "fc",
        "name": "TAKER F722 Mini Flight Controller",
        "brand": "GEPRC",
        "price_php": 2352,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+TAKER+F722+Mini+Flight+Controller",
        "color": "#111111",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "matek-f405-wing-fc",
        "category": "fc",
        "name": "F405-Wing Flight Controller",
        "brand": "Matek",
        "price_php": 2800,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F405-Wing+Flight+Controller",
        "color": "#222222",
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
        "id": "iflight-blitz-mini-f7-fc",
        "category": "fc",
        "name": "BLITZ Mini F7 Flight Controller",
        "brand": "iFlight",
        "price_php": 2688,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+BLITZ+Mini+F7+Flight+Controller",
        "color": "#003366",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "hglrc-zeus-f745-v2-fc",
        "category": "fc",
        "name": "Zeus F745 V2 Flight Controller",
        "brand": "HGLRC",
        "price_php": 3136,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Zeus+F745+V2+Flight+Controller",
        "color": "#111111",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "flywoo-goku-f745-aio-fc",
        "category": "fc",
        "name": "GOKU F745 AIO Flight Controller",
        "brand": "Flywoo",
        "price_php": 3360,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+GOKU+F745+AIO+Flight+Controller",
        "color": "#1c1c1c",
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
        "id": "airbot-f7-hd-fc",
        "category": "fc",
        "name": "F7 HD Flight Controller",
        "brand": "Airbot",
        "price_php": 2912,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Airbot+F7+HD+Flight+Controller",
        "color": "#000044",
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
        "id": "hqprop-ethix-s5-v2-5x4-3x3",
        "category": "propeller",
        "name": "Ethix S5 V2 5x4.3x3",
        "brand": "HQProp",
        "price_php": 336,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S5+V2+5x4.3x3",
        "color": "#7700cc",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "purple",
                "grey"
            ]
        }
    },
    {
        "id": "gemfan-hurricane-51477-5",
        "category": "propeller",
        "name": "Hurricane 51477 5\"",
        "brand": "Gemfan",
        "price_php": 280,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51477+5",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.77,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey"
            ]
        }
    },
    {
        "id": "dal-cyclone-t5040c",
        "category": "propeller",
        "name": "Cyclone T5040C",
        "brand": "DAL",
        "price_php": 224,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T5040C",
        "color": "#222222",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black"
            ]
        }
    },
    {
        "id": "azure-power-reaper-5",
        "category": "propeller",
        "name": "Reaper 5\"",
        "brand": "Azure Power",
        "price_php": 252,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Azure+Power+Reaper+5",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black"
            ]
        }
    },
    {
        "id": "hqprop-dp5x4-5x3-v1s",
        "category": "propeller",
        "name": "DP5X4.5X3 V1S",
        "brand": "HQProp",
        "price_php": 308,
        "weight_g": 5.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP5X4.5X3+V1S",
        "color": "#333333",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey"
            ]
        }
    },
    {
        "id": "gemfan-windancer-5152-3",
        "category": "propeller",
        "name": "Windancer 5152-3",
        "brand": "Gemfan",
        "price_php": 280,
        "weight_g": 5.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Windancer+5152-3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black"
            ]
        }
    },
    {
        "id": "ethix-p4-purple-4",
        "category": "propeller",
        "name": "P4 Purple 4\"",
        "brand": "Ethix",
        "price_php": 336,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+P4+Purple+4",
        "color": "#7700cc",
        "specs": {
            "diameter_inch": 4,
            "pitch": 3.9,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "purple"
            ]
        }
    },
    {
        "id": "hqprop-silverware-31x31x3",
        "category": "propeller",
        "name": "Silverware 3.1x3.1x3",
        "brand": "HQProp",
        "price_php": 168,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Silverware+3.1x3.1x3",
        "color": "#cccccc",
        "specs": {
            "diameter_inch": 3.1,
            "pitch": 3.1,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": [
                "grey",
                "clear"
            ]
        }
    },
    # ========== BATTERIES ==========
    {
        "id": "tattu-rline-v5-6s-1300mah-130c",
        "category": "battery",
        "name": "R-Line V5.0 6S 1300mAh 130C",
        "brand": "Tattu",
        "price_php": 3808,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5.0+6S+1300mAh+130C",
        "color": "#cc0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-black-series-4s-1550mah-100c",
        "category": "battery",
        "name": "Black Series 4S 1550mAh 100C",
        "brand": "CNHL",
        "price_php": 1904,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com/search?q=CNHL+Black+Series+4S+1550mAh+100C",
        "color": "#111111",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1550,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gnb-6s-1300mah-90c",
        "category": "battery",
        "name": "6S 1300mAh 90C",
        "brand": "GNB",
        "price_php": 2464,
        "weight_g": 230,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+6S+1300mAh+90C",
        "color": "#003300",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 90,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "ovonic-4s-1800mah-120c",
        "category": "battery",
        "name": "4S 1800mAh 120C",
        "brand": "Ovonic",
        "price_php": 1848,
        "weight_g": 190,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ovonic+4S+1800mAh+120C",
        "color": "#ff6600",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1800,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "authentic-rc-hv-6s-1100mah-130c",
        "category": "battery",
        "name": "High Voltage 6S 1100mAh 130C",
        "brand": "Authentic RC",
        "price_php": 2688,
        "weight_g": 205,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Authentic+RC+High+Voltage+6S+1100mAh+130C",
        "color": "#003366",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 25.2
        }
    },
    {
        "id": "gens-ace-tattu-3s-850mah-75c",
        "category": "battery",
        "name": "TATTU 3S 850mAh 75C",
        "brand": "Gens Ace",
        "price_php": 616,
        "weight_g": 75,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gens+Ace+TATTU+3S+850mAh+75C",
        "color": "#cc0000",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 850,
            "c_rating": 75,
            "connector": "XT30",
            "voltage_nominal": 11.1
        }
    },
    {
        "id": "cnhl-ministar-4s-850mah-100c",
        "category": "battery",
        "name": "MiniStar 4S 850mAh 100C",
        "brand": "CNHL",
        "price_php": 1120,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com/search?q=CNHL+MiniStar+4S+850mAh+100C",
        "color": "#111111",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 850,
            "c_rating": 100,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-rline-v6-4s-1400mah-150c",
        "category": "battery",
        "name": "R-Line V6.0 4S 1400mAh 150C",
        "brand": "Tattu",
        "price_php": 2576,
        "weight_g": 170,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V6.0+4S+1400mAh+150C",
        "color": "#cc0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1400,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    # ========== RECEIVERS ==========
    {
        "id": "tbs-crossfire-nano-rx-v3",
        "category": "receiver",
        "name": "Crossfire Nano RX V3",
        "brand": "TBS",
        "price_php": 1904,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Crossfire+Nano+RX+V3",
        "color": "#111111",
        "specs": {
            "protocol": "TBS Crossfire",
            "frequency_mhz": 915,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-ep2-elrs-nano-rx",
        "category": "receiver",
        "name": "EP2 ExpressLRS 2.4GHz Nano Receiver",
        "brand": "HappyModel",
        "price_php": 672,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ExpressLRS+2.4GHz+Nano+Receiver",
        "color": "#00aa44",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "radiomaster-rp4td-elrs-diversity-rx",
        "category": "receiver",
        "name": "RP4TD ExpressLRS 2.4G Diversity RX",
        "brand": "RadioMaster",
        "price_php": 1176,
        "weight_g": 2.1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RadioMaster+RP4TD+ExpressLRS+2.4G+Diversity",
        "color": "#dd0000",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "betafpv-superd-elrs-diversity-rx",
        "category": "receiver",
        "name": "SuperD ELRS Diversity Receiver",
        "brand": "BetaFPV",
        "price_php": 1400,
        "weight_g": 1.9,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=BetaFPV+SuperD+ELRS+Diversity+Receiver",
        "color": "#111",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "frsky-r9-mx-mini-rx",
        "category": "receiver",
        "name": "R9 MX Mini Receiver",
        "brand": "FrSky",
        "price_php": 1568,
        "weight_g": 2.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R9+MX+Mini+Receiver",
        "color": "#000000",
        "specs": {
            "protocol": "FrSky ACCESS",
            "frequency_mhz": 900,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "immersionrc-ghost-atto-rx",
        "category": "receiver",
        "name": "Ghost Atto Receiver",
        "brand": "ImmersionRC",
        "price_php": 1288,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+Ghost+Atto+Receiver",
        "color": "#333333",
        "specs": {
            "protocol": "Ghost",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-el24e-elrs-nano-rx",
        "category": "receiver",
        "name": "EL24E ELRS Nano Receiver",
        "brand": "Happymodel",
        "price_php": 728,
        "weight_g": 0.65,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+EL24E+ELRS+Nano+Receiver",
        "color": "#00aa44",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "tbs-tracer-diversity-micro-rx",
        "category": "receiver",
        "name": "Tracer Diversity Micro RX",
        "brand": "TBS",
        "price_php": 2072,
        "weight_g": 2.4,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Tracer+Diversity+Micro+RX",
        "color": "#111111",
        "specs": {
            "protocol": "TBS Tracer",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    # ========== GPS ==========
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1568,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-5883+GPS",
        "color": "#222222",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 5,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m10-gps",
        "category": "gps",
        "name": "Micro M10 GPS",
        "brand": "Holybro",
        "price_php": 1904,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+Micro+M10+GPS",
        "color": "#0033aa",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 5,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "betafpv-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "BetaFPV",
        "price_php": 1288,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=BetaFPV+M10+GPS+Module",
        "color": "#111",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 6,
            "compass": False,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "beitian-bn-880q-gps",
        "category": "gps",
        "name": "BN-880Q GPS+Compass",
        "brand": "Beitian",
        "price_php": 896,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880Q+GPS+Compass",
        "color": "#333333",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 8,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "speedybee-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1400,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+M10+GPS+Module",
        "color": "#0055aa",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 5,
            "compass": False,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "radiolink-se100-gps-module",
        "category": "gps",
        "name": "SE100 GPS Module",
        "brand": "Radiolink",
        "price_php": 1120,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Radiolink+SE100+GPS+Module",
        "color": "#cc3300",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 8,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m9n-5883-gps",
        "category": "gps",
        "name": "M9N-5883 GPS",
        "brand": "Matek",
        "price_php": 1344,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M9N-5883+GPS",
        "color": "#222222",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 6,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "hglrc-m100-5883-gps",
        "category": "gps",
        "name": "M100-5883 GPS Module",
        "brand": "HGLRC",
        "price_php": 1232,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+M100-5883+GPS+Module",
        "color": "#111111",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 5,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    # ========== CAMERAS ==========
    {
        "id": "runcam-phoenix-2-vision-1000tvl",
        "category": "camera",
        "name": "Phoenix 2 Vision 1000TVL",
        "brand": "RunCam",
        "price_php": 1064,
        "weight_g": 5.6,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=RunCam+Phoenix+2+Vision+1000TVL",
        "color": "#222222",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "3.3-5.5V"
        }
    },
    {
        "id": "foxeer-falkor-3-micro-1200tvl",
        "category": "camera",
        "name": "Falkor 3 Micro 1200TVL",
        "brand": "Foxeer",
        "price_php": 1176,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Falkor+3+Micro+1200TVL",
        "color": "#660000",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-nebula-pro-nova-digital-cam",
        "category": "camera",
        "name": "Nebula Pro Nova Digital Camera",
        "brand": "Caddx",
        "price_php": 3080,
        "weight_g": 7.6,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Caddx+Nebula+Pro+Nova+Digital+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "tvl": 0,
            "voltage_range": "6.5-25V"
        }
    },
    {
        "id": "foxeer-digisight-3-micro-cam",
        "category": "camera",
        "name": "Digisight 3 Micro Camera",
        "brand": "Foxeer",
        "price_php": 2464,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Digisight+3+Micro+Camera",
        "color": "#660000",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 155,
            "format": "Digital",
            "tvl": 0,
            "voltage_range": "6.5-25V"
        }
    },
    {
        "id": "runcam-racer-3-nano",
        "category": "camera",
        "name": "Racer 3 Nano",
        "brand": "RunCam",
        "price_php": 840,
        "weight_g": 3.2,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=RunCam+Racer+3+Nano",
        "color": "#222222",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "caddx-ratel-pro-118-starlight",
        "category": "camera",
        "name": "Ratel Pro 1/1.8\" Starlight",
        "brand": "Caddx",
        "price_php": 1680,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Caddx+Ratel+Pro+1.8+Starlight",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-nano-camera-v2",
        "category": "camera",
        "name": "Avatar HD Nano Camera V2",
        "brand": "Walksnail",
        "price_php": 2800,
        "weight_g": 5.7,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Walksnail+Avatar+HD+Nano+Camera+V2",
        "color": "#111111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "tvl": 0,
            "voltage_range": "6.5-27V"
        }
    },
    {
        "id": "hdzero-nyxi-nano-camera",
        "category": "camera",
        "name": "Nyxi Nano Camera",
        "brand": "HDZero",
        "price_php": 2688,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Nyxi+Nano+Camera",
        "color": "#111111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 145,
            "format": "Digital",
            "tvl": 0,
            "voltage_range": "6.5-25V"
        }
    },
    # ========== VTX ==========
    {
        "id": "tbs-unify-evo-pro-vtx",
        "category": "vtx",
        "name": "Unify Evo Pro 5.8GHz VTX",
        "brand": "TBS",
        "price_php": 3360,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Unify+Evo+Pro",
        "color": "#111111",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rush-tank-ultimate-vtx",
        "category": "vtx",
        "name": "Tank Ultimate VTX",
        "brand": "Rush",
        "price_php": 2800,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Rush+Tank+Ultimate+VTX",
        "color": "#cc0000",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "akk-fx3-ultimate-vtx",
        "category": "vtx",
        "name": "FX3 Ultimate 5.8GHz VTX",
        "brand": "AKK",
        "price_php": 1568,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+FX3+Ultimate+5.8GHz+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "hglrc-sirius-1200mw-vtx",
        "category": "vtx",
        "name": "Sirius 1200mW VTX",
        "brand": "HGLRC",
        "price_php": 1904,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Sirius+1200mW+VTX",
        "color": "#111111",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "foxeer-reaper-1w-vtx",
        "category": "vtx",
        "name": "Reaper 1W VTX",
        "brand": "Foxeer",
        "price_php": 2240,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Reaper+1W+VTX",
        "color": "#660000",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "matek-5-8ghz-vtx-hv",
        "category": "vtx",
        "name": "5.8GHz VTX-HV",
        "brand": "Matek",
        "price_php": 1512,
        "weight_g": 5.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+5.8GHz+VTX-HV",
        "color": "#222222",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "immersionrc-tramp-hv-vtx",
        "category": "vtx",
        "name": "Tramp HV VTX",
        "brand": "ImmersionRC",
        "price_php": 2688,
        "weight_g": 6.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+Tramp+HV+VTX",
        "color": "#333333",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "walksnail-avatar-hd-vtx-kit-v3-lite",
        "category": "vtx",
        "name": "Avatar HD VTX Kit V3 Lite",
        "brand": "Walksnail",
        "price_php": 5600,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Walksnail+Avatar+HD+VTX+Kit+V3+Lite",
        "color": "#111111",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "6.5-27V",
            "connector": "U.FL"
        }
    },
    # ========== ANTENNAS ==========
    {
        "id": "truerc-singularity-5-8ghz-rhcp",
        "category": "antenna",
        "name": "Singularity 5.8GHz RHCP",
        "brand": "TrueRC",
        "price_php": 1120,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Singularity+5.8GHz+RHCP",
        "color": "#1a1a1a",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.6,
            "type": "cloverleaf"
        }
    },
    {
        "id": "immersionrc-spironet-5-8ghz-rhcp",
        "category": "antenna",
        "name": "SpiroNET 5.8GHz RHCP",
        "brand": "ImmersionRC",
        "price_php": 672,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SpiroNET+5.8GHz+RHCP",
        "color": "#333333",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.2,
            "type": "cloverleaf"
        }
    },
    {
        "id": "foxeer-lollipop-4-plus-5-8ghz",
        "category": "antenna",
        "name": "Lollipop 4 Plus 5.8GHz",
        "brand": "Foxeer",
        "price_php": 392,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Lollipop+4+Plus+5.8GHz",
        "color": "#660000",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2,
            "type": "omni"
        }
    },
    {
        "id": "rush-cherry-pro-5-8ghz",
        "category": "antenna",
        "name": "Cherry Pro 5.8GHz RHCP",
        "brand": "Rush",
        "price_php": 728,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Rush+Cherry+Pro+5.8GHz+RHCP",
        "color": "#cc0000",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.3,
            "type": "cloverleaf"
        }
    },
    {
        "id": "akk-co2-5-8ghz-straight",
        "category": "antenna",
        "name": "CO2 5.8GHz Straight",
        "brand": "AKK",
        "price_php": 224,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+CO2+5.8GHz+Straight",
        "color": "#221100",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 1.5,
            "type": "omni"
        }
    },
    {
        "id": "hglrc-t-shape-5-8ghz-stubby",
        "category": "antenna",
        "name": "T-Shape 5.8GHz Stubby",
        "brand": "HGLRC",
        "price_php": 280,
        "weight_g": 3.8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+T-Shape+5.8GHz+Stubby",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 1.8,
            "type": "omni"
        }
    },
    {
        "id": "tbs-triumph-pro-5-8ghz",
        "category": "antenna",
        "name": "Triumph Pro 5.8GHz",
        "brand": "TBS",
        "price_php": 896,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Triumph+Pro",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 3.5,
            "type": "directional"
        }
    },
    {
        "id": "lumenier-axii-2-stubby-5-8ghz",
        "category": "antenna",
        "name": "AXII 2 Stubby 5.8GHz",
        "brand": "Lumenier",
        "price_php": 616,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com/search?q=Lumenier+AXII+2+Stubby+5.8GHz",
        "color": "#151515",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2,
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
