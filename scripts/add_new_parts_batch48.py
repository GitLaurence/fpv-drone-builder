#!/usr/bin/env python3
"""Add new real FPV parts to parts.json - Batch 48: new parts across all 11 categories."""
import json

NEW_PARTS = [
    # ========== FRAMES ==========
    {
        "id": "tbs-source-one-v5-frame",
        "category": "frame",
        "name": "Source One V5 5\" Frame",
        "brand": "TBS",
        "price_php": 1680,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Source+One+V5",
        "color": "#111111",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+v5"
        }
    },
    {
        "id": "armattan-rooster-5-frame",
        "category": "frame",
        "name": "Rooster 5\" Frame",
        "brand": "Armattan",
        "price_php": 6440,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+5",
        "color": "#151515",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 27,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster"
        }
    },
    {
        "id": "diatone-roma-f5-frame",
        "category": "frame",
        "name": "Roma F5 Frame",
        "brand": "Diatone",
        "price_php": 2660,
        "weight_g": 74,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Diatone+Roma+F5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=diatone+roma+f5"
        }
    },
    {
        "id": "flywoo-explorer-lr4-frame",
        "category": "frame",
        "name": "Explorer LR4 4\" Long Range Frame",
        "brand": "Flywoo",
        "price_php": 2380,
        "weight_g": 56,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+Explorer+LR4",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 190,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 22,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "iflight-chimera7-pro-frame",
        "category": "frame",
        "name": "Chimera7 Pro Frame",
        "brand": "iFlight",
        "price_php": 3920,
        "weight_g": 128,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+Chimera7+Pro",
        "color": "#111111",
        "specs": {
            "size_mm": 300,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+chimera7"
        }
    },
    {
        "id": "geprc-mark5-hd-frame",
        "category": "frame",
        "name": "Mark5 HD Frame",
        "brand": "GEPRC",
        "price_php": 3220,
        "weight_g": 108,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+Mark5+HD",
        "color": "#151515",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 27,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5"
        }
    },
    {
        "id": "hglrc-sector-cx3-frame",
        "category": "frame",
        "name": "Sector CX3 3\" Frame",
        "brand": "HGLRC",
        "price_php": 1400,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Sector+CX3",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 150,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 18,
            "thingiverse_url": "https://www.thingiverse.com/search?q=hglrc+sector+cx3"
        }
    },
    # ========== MOTORS ==========
    {
        "id": "tmotor-f60-pro-iv-2500kv",
        "category": "motor",
        "name": "F60 Pro IV 2500KV",
        "brand": "T-Motor",
        "price_php": 1064,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=T-Motor+F60+Pro+IV+2500KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2500,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "emax-eco-ii-2807-1500kv",
        "category": "motor",
        "name": "ECO II 2807 1500KV",
        "brand": "EMAX",
        "price_php": 896,
        "weight_g": 44,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com/search?q=EMAX+ECO+II+2807+1500KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1500,
            "stator_size": "2807",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 32
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-1900kv",
        "category": "motor",
        "name": "Avenger 2306.5 1900KV",
        "brand": "BrotherHobby",
        "price_php": 952,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=BrotherHobby+Avenger+2306.5+1900KV",
        "color": "#151515",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "iflight-xing2-2207-1800kv",
        "category": "motor",
        "name": "XING2 2207 1800KV",
        "brand": "iFlight",
        "price_php": 924,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+XING2+2207+1800KV",
        "color": "#1c1c1c",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 37
        }
    },
    {
        "id": "flywoo-nin-1404-4750kv",
        "category": "motor",
        "name": "NIN 1404 4750KV",
        "brand": "Flywoo",
        "price_php": 616,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+NIN+1404+4750KV",
        "color": "#111111",
        "specs": {
            "kv": 4750,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 18
        }
    },
    {
        "id": "rcinpower-gts-v3-2207-1950kv",
        "category": "motor",
        "name": "GTS V3 2207 1950KV",
        "brand": "RCINPOWER",
        "price_php": 980,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RCINPOWER+GTS+V3+2207+1950KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    # ========== ESCs ==========
    {
        "id": "holybro-tekko32-f4-60a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 60A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3080,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+Tekko32+F4+60A+4in1",
        "color": "#111111",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "diatone-mamba-f45-45a-4in1",
        "category": "esc",
        "name": "Mamba F45 45A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 1960,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Diatone+Mamba+F45+45A+4in1",
        "color": "#151515",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 25.5,
            "burst_amp": 55
        }
    },
    {
        "id": "speedybee-bls-50a-4in1",
        "category": "esc",
        "name": "BLS 50A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2240,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+BLS+50A+4in1",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "hglrc-zeus-60a-4in1",
        "category": "esc",
        "name": "Zeus 60A 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 2660,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Zeus+60A+4in1",
        "color": "#111111",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "flycolor-raptor-blheli32-45a-4in1",
        "category": "esc",
        "name": "Raptor BLHeli_32 45A 4-in-1 ESC",
        "brand": "Flycolor",
        "price_php": 1680,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+Raptor+BLHeli_32+45A+4in1",
        "color": "#1c1c1c",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 25.5,
            "burst_amp": 55
        }
    },
    # ========== FLIGHT CONTROLLERS ==========
    {
        "id": "holybro-kakute-f7-hdv-fc",
        "category": "fc",
        "name": "Kakute F7 HDV Flight Controller",
        "brand": "Holybro",
        "price_php": 3360,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+Kakute+F7+HDV",
        "color": "#111111",
        "specs": {
            "gyro": "ICM20689",
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
        "id": "speedybee-f405-v4-fc",
        "category": "fc",
        "name": "F405 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 1848,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+F405+V4",
        "color": "#151515",
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
        "id": "matek-f405-wing-fc",
        "category": "fc",
        "name": "F405-Wing Flight Controller",
        "brand": "Matek",
        "price_php": 2520,
        "weight_g": 7.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F405-Wing",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 36,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "iflight-succex-e-f4-fc",
        "category": "fc",
        "name": "SucceX-E F4 Flight Controller",
        "brand": "iFlight",
        "price_php": 1400,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+SucceX-E+F4",
        "color": "#111111",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "geprc-f411-12a-aio-fc",
        "category": "fc",
        "name": "F411 12A AIO Flight Controller",
        "brand": "GEPRC",
        "price_php": 1288,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+F411+12A+AIO",
        "color": "#151515",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": False,
            "uart_count": 4,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    # ========== PROPELLERS ==========
    {
        "id": "hqprop-5x4-3x3-v1s",
        "category": "propeller",
        "name": "5X4.3X3 V1S Propeller (4pc)",
        "brand": "HQProp",
        "price_php": 196,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+5X4.3X3+V1S",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-hurricane-51466-tri-blade",
        "category": "propeller",
        "name": "Hurricane 5146-6 Tri-Blade Propeller (4pc)",
        "brand": "Gemfan",
        "price_php": 224,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+5146-6",
        "color": "#111111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "green"]
        }
    },
    {
        "id": "dal-cyclone-t5047c-propeller",
        "category": "propeller",
        "name": "Cyclone T5047C Propeller (4pc)",
        "brand": "DAL",
        "price_php": 168,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T5047C",
        "color": "#151515",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    {
        "id": "ethix-s3-5inch-propeller",
        "category": "propeller",
        "name": "S3 5\" Propeller (4pc)",
        "brand": "Ethix",
        "price_php": 252,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+S3+5inch",
        "color": "#1c1c1c",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["purple", "gray"]
        }
    },
    {
        "id": "gemfan-71433-7inch-tri-blade",
        "category": "propeller",
        "name": "7143-3 7\" Tri-Blade Propeller (4pc)",
        "brand": "Gemfan",
        "price_php": 280,
        "weight_g": 8.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+7143-3",
        "color": "#111111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    # ========== FPV CAMERAS ==========
    {
        "id": "runcam-phoenix-2-camera",
        "category": "camera",
        "name": "Phoenix 2 FPV Camera",
        "brand": "RunCam",
        "price_php": 1568,
        "weight_g": 7.9,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=RunCam+Phoenix+2",
        "color": "#111111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 150,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-predator-5-camera",
        "category": "camera",
        "name": "Predator 5 FPV Camera",
        "brand": "Foxeer",
        "price_php": 1344,
        "weight_g": 6.8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Predator+5",
        "color": "#151515",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ratel-2-camera",
        "category": "camera",
        "name": "Ratel 2 FPV Camera",
        "brand": "Caddx",
        "price_php": 1400,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Caddx+Ratel+2",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-nano-camera",
        "category": "camera",
        "name": "Avatar HD Nano Camera",
        "brand": "Walksnail",
        "price_php": 3080,
        "weight_g": 5.4,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Walksnail+Avatar+HD+Nano",
        "color": "#111111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "tvl": 0,
            "voltage_range": "6-25V"
        }
    },
    {
        "id": "caddx-ratel-pro-camera",
        "category": "camera",
        "name": "Ratel Pro FPV Camera",
        "brand": "Caddx",
        "price_php": 1176,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Caddx+Ratel+Pro",
        "color": "#151515",
        "specs": {
            "sensor": "1/2.7\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    # ========== VIDEO TRANSMITTERS ==========
    {
        "id": "tbs-unify-pro32-nano-vtx",
        "category": "vtx",
        "name": "Unify Pro32 Nano 5.8GHz VTX",
        "brand": "TBS",
        "price_php": 2352,
        "weight_g": 4.4,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Unify+Pro32+Nano",
        "color": "#111111",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rushfpv-tank-solo-vtx",
        "category": "vtx",
        "name": "Tank Solo 5.8GHz VTX",
        "brand": "RushFPV",
        "price_php": 1904,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=RushFPV+Tank+Solo",
        "color": "#151515",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "immersionrc-ghost-atto-vtx",
        "category": "vtx",
        "name": "Ghost Atto 5.8GHz VTX",
        "brand": "ImmersionRC",
        "price_php": 1568,
        "weight_g": 3.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+Ghost+Atto",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "hglrc-titan-vtx-1w",
        "category": "vtx",
        "name": "Titan 5.8GHz 1W VTX",
        "brand": "HGLRC",
        "price_php": 1680,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Titan+VTX+1W",
        "color": "#111111",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "walksnail-avatar-hd-vtx-nano",
        "category": "vtx",
        "name": "Avatar HD VTX Nano Kit",
        "brand": "Walksnail",
        "price_php": 5320,
        "weight_g": 6.3,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Walksnail+Avatar+HD+VTX+Nano",
        "color": "#151515",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Digital",
            "bands": "N/A",
            "voltage_range": "6-25V",
            "connector": "U.FL"
        }
    },
    # ========== BATTERIES ==========
    {
        "id": "cnhl-black-series-1550mah-4s",
        "category": "battery",
        "name": "Black Series 1550mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1148,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1550mAh+4S+100C",
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
        "id": "tattu-r-line-v5-1300mah-6s",
        "category": "battery",
        "name": "R-Line V5 1300mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2240,
        "weight_g": 236,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5+1300mAh+6S",
        "color": "#151515",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gnb-2200mah-4s-95c",
        "category": "battery",
        "name": "2200mAh 4S 95C LiPo",
        "brand": "GNB",
        "price_php": 1512,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+2200mAh+4S+95C",
        "color": "#1a1a1a",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 2200,
            "c_rating": 95,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gensace-tattu-850mah-3s-75c",
        "category": "battery",
        "name": "Tattu 850mAh 3S 75C LiPo",
        "brand": "Gens Ace",
        "price_php": 616,
        "weight_g": 84,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gens+Ace+Tattu+850mAh+3S+75C",
        "color": "#151515",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 850,
            "c_rating": 75,
            "connector": "XT30",
            "voltage_nominal": 11.1
        }
    },
    {
        "id": "cnhl-mini-star-3300mah-6s",
        "category": "battery",
        "name": "Mini Star 3300mAh 6S 60C",
        "brand": "CNHL",
        "price_php": 3360,
        "weight_g": 452,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Mini+Star+3300mAh+6S+60C",
        "color": "#111111",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 3300,
            "c_rating": 60,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    # ========== RC RECEIVERS ==========
    {
        "id": "tbs-crossfire-nano-rx-se",
        "category": "receiver",
        "name": "Crossfire Nano RX SE",
        "brand": "TBS",
        "price_php": 1904,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Crossfire+Nano+RX+SE",
        "color": "#111111",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-exlrs-pico-rx",
        "category": "receiver",
        "name": "EP2 ExpressLRS Pico Receiver",
        "brand": "HappyModel",
        "price_php": 728,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ExpressLRS+Pico",
        "color": "#151515",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "frsky-r9-mm-receiver",
        "category": "receiver",
        "name": "R9 MM 900MHz Receiver",
        "brand": "FrSky",
        "price_php": 1400,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R9+MM+900MHz",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ACCST",
            "frequency_mhz": 900,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "radiomaster-rp3-exlrs-rx",
        "category": "receiver",
        "name": "RP3 ExpressLRS Receiver",
        "brand": "RadioMaster",
        "price_php": 896,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RadioMaster+RP3+ExpressLRS",
        "color": "#151515",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "tbs-crossfire-diversity-nano-rx",
        "category": "receiver",
        "name": "Crossfire Diversity Nano RX",
        "brand": "TBS",
        "price_php": 2016,
        "weight_g": 2.1,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Crossfire+Diversity+Nano+RX",
        "color": "#111111",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915,
            "diversity": True,
            "telemetry": True
        }
    },
    # ========== GPS MODULES ==========
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS + Compass",
        "brand": "Matek",
        "price_php": 1568,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-5883",
        "color": "#111111",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 12,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-m10-gps-standard",
        "category": "gps",
        "name": "M10 GPS Standard Module",
        "brand": "Holybro",
        "price_php": 1848,
        "weight_g": 9.2,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+M10+GPS+Standard",
        "color": "#151515",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 11,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "beitian-bn-880-gps",
        "category": "gps",
        "name": "BN-880 GPS + Compass Module",
        "brand": "Beitian",
        "price_php": 896,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 15,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "iflight-m8n-gps-module",
        "category": "gps",
        "name": "M8N GPS Module",
        "brand": "iFlight",
        "price_php": 1064,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+M8N+GPS",
        "color": "#111111",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 13,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    # ========== VTX ANTENNAS ==========
    {
        "id": "truerc-x-air-sma-antenna",
        "category": "antenna",
        "name": "X-Air 5.8GHz SMA Antenna",
        "brand": "TrueRC",
        "price_php": 728,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+X-Air+5.8GHz",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.6,
            "type": "cloverleaf"
        }
    },
    {
        "id": "foxeer-lollipop-4-sma-antenna",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz SMA Antenna",
        "brand": "Foxeer",
        "price_php": 560,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Lollipop+4",
        "color": "#151515",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.3,
            "type": "cloverleaf"
        }
    },
    {
        "id": "rushfpv-cherry-sma-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz SMA Antenna",
        "brand": "RushFPV",
        "price_php": 616,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=RushFPV+Cherry+5.8GHz",
        "color": "#1a1a1a",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.5,
            "type": "cloverleaf"
        }
    },
    {
        "id": "tbs-triumph-plus-sma-antenna",
        "category": "antenna",
        "name": "Triumph Plus 5.8GHz SMA Antenna",
        "brand": "TBS",
        "price_php": 952,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Triumph+Plus",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 4,
            "type": "directional"
        }
    },
    {
        "id": "hglrc-tslrs-2-4ghz-antenna",
        "category": "antenna",
        "name": "T-Antenna 2.4GHz ExpressLRS Antenna",
        "brand": "HGLRC",
        "price_php": 336,
        "weight_g": 2.8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+T-Antenna+2.4GHz",
        "color": "#151515",
        "specs": {
            "frequency_ghz": 2.4,
            "polarization": "LHCP",
            "connector": "IPEX",
            "gain_dbi": 1.5,
            "type": "dipole"
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
