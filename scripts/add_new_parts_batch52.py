#!/usr/bin/env python3
"""Batch 52: real, current-production FPV parts across all 11 categories,
filling out brand/model coverage that was still thin after batch51."""
import json

NEW_PARTS = [
    # ========== FRAME ==========
    {
        "id": "geprc-mark5-hd-o3-frame",
        "category": "frame",
        "name": "Mark5 HD O3 Frame Kit",
        "brand": "GEPRC",
        "price_php": 2856,
        "weight_g": 118,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=Mark5+HD+O3+Frame+Kit",
        "color": "#1a1a1a",
        "specs": {
            "wheelbase_mm": 225,
            "type": "freestyle",
            "arm_thickness_mm": 4,
            "material": "3K carbon fiber",
            "camera_mount": "20x20/25.5x25.5"
        }
    },
    {
        "id": "iflight-marc4-hd-frame",
        "category": "frame",
        "name": "Marc4 HD Cinewhoop Frame Kit",
        "brand": "iFlight",
        "price_php": 2408,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=Marc4+HD+Cinewhoop+Frame+Kit",
        "color": "#202020",
        "specs": {
            "wheelbase_mm": 152,
            "type": "cinelifter",
            "arm_thickness_mm": 5,
            "material": "3K carbon fiber",
            "camera_mount": "19x19/20x20"
        }
    },
    {
        "id": "flywoo-explorer-lr4-o4-frame",
        "category": "frame",
        "name": "Explorer LR4 O4 Frame Kit",
        "brand": "Flywoo",
        "price_php": 3080,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Explorer+LR4+O4+Frame+Kit",
        "color": "#0f0f0f",
        "specs": {
            "wheelbase_mm": 175,
            "type": "long-range",
            "arm_thickness_mm": 4,
            "material": "3K carbon fiber",
            "camera_mount": "20x20/25.5x25.5"
        }
    },
    {
        "id": "armattan-marmotte-6-frame",
        "category": "frame",
        "name": "Marmotte 6\" Frame Kit",
        "brand": "Armattan",
        "price_php": 5320,
        "weight_g": 128,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Marmotte+6+Frame+Kit",
        "color": "#151515",
        "specs": {
            "wheelbase_mm": 254,
            "type": "freestyle",
            "arm_thickness_mm": 5,
            "material": "3K carbon fiber",
            "camera_mount": "20x20/30.5x30.5"
        }
    },
    {
        "id": "diatone-roma-l6-frame",
        "category": "frame",
        "name": "Roma L6 Frame Kit",
        "brand": "Diatone",
        "price_php": 2632,
        "weight_g": 112,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Roma+L6+Frame+Kit",
        "color": "#111318",
        "specs": {
            "wheelbase_mm": 235,
            "type": "long-range",
            "arm_thickness_mm": 4,
            "material": "3K carbon fiber",
            "camera_mount": "20x20/25.5x25.5"
        }
    },
    # ========== MOTOR ==========
    {
        "id": "tmotor-f60-pro-v3-motor",
        "category": "motor",
        "name": "F60 Pro V3 2550KV",
        "brand": "T-Motor",
        "price_php": 1288,
        "weight_g": 32.5,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F60+Pro+V3+2550KV",
        "color": "#1c1c1c",
        "specs": {
            "kv": 2550,
            "stator_size": "2207",
            "shaft_mm": 5,
            "max_thrust_g": 1980,
            "cell_count": "4-6S"
        }
    },
    {
        "id": "brotherhobby-avenger-2306-motor",
        "category": "motor",
        "name": "Avenger 2306.5 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1064,
        "weight_g": 33.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2306.5+1900KV",
        "color": "#202020",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "shaft_mm": 5,
            "max_thrust_g": 2100,
            "cell_count": "5-6S"
        }
    },
    {
        "id": "flywoo-nin-1404-motor",
        "category": "motor",
        "name": "NIN 1404 4600KV",
        "brand": "Flywoo",
        "price_php": 616,
        "weight_g": 10.2,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=NIN+1404+4600KV",
        "color": "#111111",
        "specs": {
            "kv": 4600,
            "stator_size": "1404",
            "shaft_mm": 1.5,
            "max_thrust_g": 420,
            "cell_count": "3-4S"
        }
    },
    {
        "id": "iflight-xing2-2306-motor",
        "category": "motor",
        "name": "XING2 2306 1800KV",
        "brand": "iFlight",
        "price_php": 952,
        "weight_g": 31.4,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=XING2+2306+1800KV",
        "color": "#0d0d0d",
        "specs": {
            "kv": 1800,
            "stator_size": "2306",
            "shaft_mm": 5,
            "max_thrust_g": 2050,
            "cell_count": "5-6S"
        }
    },
    {
        "id": "emax-eco-ii-2807-motor",
        "category": "motor",
        "name": "ECO II 2807 1300KV",
        "brand": "Emax",
        "price_php": 896,
        "weight_g": 41.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Emax+ECO+II+2807+1300KV",
        "color": "#101010",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "shaft_mm": 5,
            "max_thrust_g": 2450,
            "cell_count": "6S"
        }
    },
    {
        "id": "rcinpower-gts-v2-2306-motor",
        "category": "motor",
        "name": "GTS V2 2306.5 1960KV",
        "brand": "RCINPower",
        "price_php": 1008,
        "weight_g": 30.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RCINPower+GTS+V2+2306.5+1960KV",
        "color": "#161616",
        "specs": {
            "kv": 1960,
            "stator_size": "2306",
            "shaft_mm": 5,
            "max_thrust_g": 2000,
            "cell_count": "4-6S"
        }
    },
    # ========== ESC ==========
    {
        "id": "speedybee-blheli-s-45a-4in1-esc",
        "category": "esc",
        "name": "BLHeli_S 45A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 1512,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=BLHeli_S+45A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "current_rating_a": 45,
            "firmware": "BLHeli_S",
            "cell_count": "3-6S",
            "protocol": ["DShot600", "DShot300", "Multishot"],
            "size_mm": "30.5x30.5"
        }
    },
    {
        "id": "hglrc-f60-60a-4in1-esc",
        "category": "esc",
        "name": "F60 60A 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 2296,
        "weight_g": 14.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=F60+60A+4-in-1+ESC",
        "color": "#111122",
        "specs": {
            "current_rating_a": 60,
            "firmware": "BLHeli_32",
            "cell_count": "4-6S",
            "protocol": ["DShot600", "DShot300", "Multishot"],
            "size_mm": "30.5x30.5"
        }
    },
    {
        "id": "flywoo-goku-gn-745-55a-esc",
        "category": "esc",
        "name": "GOKU GN745 55A 4-in-1 ESC",
        "brand": "Flywoo",
        "price_php": 1848,
        "weight_g": 12.8,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=GOKU+GN745+55A+4-in-1+ESC",
        "color": "#0f0f0f",
        "specs": {
            "current_rating_a": 55,
            "firmware": "BLHeli_32",
            "cell_count": "4-6S",
            "protocol": ["DShot600", "DShot300", "Multishot"],
            "size_mm": "25.5x25.5"
        }
    },
    {
        "id": "diatone-mamba-f45-45a-esc",
        "category": "esc",
        "name": "Mamba F45 45A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 1400,
        "weight_g": 10.5,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Mamba+F45+45A+4-in-1+ESC",
        "color": "#101418",
        "specs": {
            "current_rating_a": 45,
            "firmware": "BLHeli_32",
            "cell_count": "3-6S",
            "protocol": ["DShot600", "DShot300", "Multishot"],
            "size_mm": "20x20"
        }
    },
    {
        "id": "tmotor-f55a-pro-ii-esc",
        "category": "esc",
        "name": "F55A PRO II 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 2072,
        "weight_g": 13.2,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F55A+PRO+II+4-in-1+ESC",
        "color": "#1c1c1c",
        "specs": {
            "current_rating_a": 55,
            "firmware": "BLHeli_32",
            "cell_count": "3-6S",
            "protocol": ["DShot600", "DShot300", "Multishot"],
            "size_mm": "30.5x30.5"
        }
    },
    # ========== FC ==========
    {
        "id": "matek-f411-wse-fc",
        "category": "fc",
        "name": "F411-WSE Flight Controller",
        "brand": "Matek",
        "price_php": 1288,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F411-WSE+Flight+Controller",
        "color": "#0a0a0a",
        "specs": {
            "mcu": "STM32F411",
            "gyro": "ICM42688-P",
            "uarts": 4,
            "blackbox": "16Mb onboard flash",
            "size_mm": "20x20"
        }
    },
    {
        "id": "speedybee-f745-v2-fc",
        "category": "fc",
        "name": "F745 V2 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 1960,
        "weight_g": 8.2,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=F745+V2+Flight+Controller",
        "color": "#171717",
        "specs": {
            "mcu": "STM32F745",
            "gyro": "ICM42688-P",
            "uarts": 6,
            "blackbox": "microSD",
            "size_mm": "20x20"
        }
    },
    {
        "id": "hglrc-formula-f411-fc",
        "category": "fc",
        "name": "Formula F411 Flight Controller",
        "brand": "HGLRC",
        "price_php": 1288,
        "weight_g": 5.1,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Formula+F411+Flight+Controller",
        "color": "#111122",
        "specs": {
            "mcu": "STM32F411",
            "gyro": "ICM42688-P",
            "uarts": 4,
            "blackbox": "16Mb onboard flash",
            "size_mm": "20x20"
        }
    },
    {
        "id": "flywoo-goku-f745-fc",
        "category": "fc",
        "name": "GOKU F745 AIO Flight Controller",
        "brand": "Flywoo",
        "price_php": 2856,
        "weight_g": 10.4,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=GOKU+F745+AIO+Flight+Controller",
        "color": "#0f0f0f",
        "specs": {
            "mcu": "STM32F745",
            "gyro": "ICM42688-P",
            "uarts": 8,
            "blackbox": "128Mb onboard flash",
            "size_mm": "30.5x30.5"
        }
    },
    {
        "id": "holybro-kakute-f7-1-5-fc",
        "category": "fc",
        "name": "Kakute F7 1.5 Flight Controller",
        "brand": "Holybro",
        "price_php": 3080,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Kakute+F7+1.5+Flight+Controller",
        "color": "#141414",
        "specs": {
            "mcu": "STM32F745",
            "gyro": "ICM42688-P",
            "uarts": 6,
            "blackbox": "microSD",
            "size_mm": "20x20"
        }
    },
    # ========== PROPELLER ==========
    {
        "id": "gemfan-hurricane-5152-3-prop",
        "category": "propeller",
        "name": "Hurricane 5152-3 Tri-Blade",
        "brand": "Gemfan",
        "price_php": 224,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+5152-3+Tri-Blade",
        "color": "#1a1a1a",
        "specs": {
            "diameter_in": 5.1,
            "pitch_in": 4.6,
            "blades": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    {
        "id": "hqprop-r38-3x8x3-prop",
        "category": "propeller",
        "name": "R38 3.8x3x3 Tri-Blade",
        "brand": "HQProp",
        "price_php": 196,
        "weight_g": 2.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+R38+3.8x3x3+Tri-Blade",
        "color": "#202020",
        "specs": {
            "diameter_in": 3.8,
            "pitch_in": 3,
            "blades": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    {
        "id": "dal-cyclone-t5049-prop",
        "category": "propeller",
        "name": "Cyclone T5049 Tri-Blade",
        "brand": "DAL",
        "price_php": 210,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T5049+Tri-Blade",
        "color": "#151515",
        "specs": {
            "diameter_in": 5.0,
            "pitch_in": 4.9,
            "blades": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    {
        "id": "ethix-s6-prop",
        "category": "propeller",
        "name": "S6 6\" Tri-Blade",
        "brand": "Ethix",
        "price_php": 280,
        "weight_g": 6.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+S6+Tri-Blade",
        "color": "#0d0d0d",
        "specs": {
            "diameter_in": 6.0,
            "pitch_in": 4.5,
            "blades": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    {
        "id": "gemfan-hulkie-7042-prop",
        "category": "propeller",
        "name": "Hulkie 7042 Bi-Blade",
        "brand": "Gemfan",
        "price_php": 252,
        "weight_g": 6.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hulkie+7042+Bi-Blade",
        "color": "#1a1a1a",
        "specs": {
            "diameter_in": 7.0,
            "pitch_in": 4.2,
            "blades": 2,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    # ========== CAMERA ==========
    {
        "id": "foxeer-razor-nano-camera",
        "category": "camera",
        "name": "Razor Nano Analog Camera",
        "brand": "Foxeer",
        "price_php": 1288,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Razor+Nano+Analog+Camera",
        "color": "#141414",
        "specs": {
            "sensor": "1/3\" Super HAD II CCD",
            "tvl": 1200,
            "fov_deg": 165,
            "min_illumination_lux": 0.001,
            "output": "analog PAL/NTSC"
        }
    },
    {
        "id": "runcam-split-4-camera",
        "category": "camera",
        "name": "Split 4 Analog + DVR Camera",
        "brand": "RunCam",
        "price_php": 1568,
        "weight_g": 5.8,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Split+4+Analog+DVR+Camera",
        "color": "#101010",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "tvl": 1000,
            "fov_deg": 155,
            "min_illumination_lux": 0.0001,
            "output": "analog PAL/NTSC"
        }
    },
    {
        "id": "caddx-ant-camera",
        "category": "camera",
        "name": "Ant Ultra-Lite Analog Camera",
        "brand": "Caddx",
        "price_php": 1120,
        "weight_g": 2.2,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ant+Ultra-Lite+Analog+Camera",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/1.8\" Super WDR CMOS",
            "tvl": 1200,
            "fov_deg": 166,
            "min_illumination_lux": 0.0001,
            "output": "analog PAL/NTSC"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-camera",
        "category": "camera",
        "name": "Avatar HD V3 Camera",
        "brand": "Walksnail",
        "price_php": 4256,
        "weight_g": 9.6,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+V3+Camera",
        "color": "#161616",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "resolution": "1080p@60fps",
            "fov_deg": 170,
            "min_illumination_lux": 0.001,
            "output": "digital HD"
        }
    },
    {
        "id": "hdzero-nyxus-nano-camera",
        "category": "camera",
        "name": "Nyxus Nano HD Camera",
        "brand": "HDZero",
        "price_php": 3640,
        "weight_g": 6.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Nyxus+Nano+HD+Camera",
        "color": "#111111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "resolution": "720p@100fps",
            "fov_deg": 150,
            "min_illumination_lux": 0.01,
            "output": "digital HD"
        }
    },
    # ========== VTX ==========
    {
        "id": "rushfpv-tank-solo-1w-vtx",
        "category": "vtx",
        "name": "TANK Solo 1W VTX",
        "brand": "RushFPV",
        "price_php": 3416,
        "weight_g": 13.5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=TANK+Solo+1W+VTX",
        "color": "#141414",
        "specs": {
            "max_power_mw": 1600,
            "frequency_band": "5.8GHz 40CH",
            "output": "analog",
            "connector": "MMCX",
            "smart_audio": True
        }
    },
    {
        "id": "hglrc-titan-1w-vtx",
        "category": "vtx",
        "name": "Titan 1W VTX",
        "brand": "HGLRC",
        "price_php": 1904,
        "weight_g": 9.8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Titan+1W+VTX",
        "color": "#111122",
        "specs": {
            "max_power_mw": 1000,
            "frequency_band": "5.8GHz 40CH",
            "output": "analog",
            "connector": "MMCX",
            "smart_audio": True
        }
    },
    {
        "id": "akk-bee-mini-vtx",
        "category": "vtx",
        "name": "Bee Mini VTX",
        "brand": "AKK",
        "price_php": 1176,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+Bee+Mini+VTX",
        "color": "#0f0f0f",
        "specs": {
            "max_power_mw": 25,
            "frequency_band": "5.8GHz 40CH",
            "output": "analog",
            "connector": "U.FL",
            "smart_audio": True
        }
    },
    {
        "id": "walksnail-avatar-hd-vtx-v3",
        "category": "vtx",
        "name": "Avatar HD VTX V3",
        "brand": "Walksnail",
        "price_php": 6720,
        "weight_g": 17.2,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+VTX+V3",
        "color": "#161616",
        "specs": {
            "max_power_mw": 1200,
            "frequency_band": "5.8GHz",
            "output": "digital HD",
            "connector": "MMCX",
            "smart_audio": True
        }
    },
    {
        "id": "speedybee-tx500-vtx",
        "category": "vtx",
        "name": "TX500 VTX",
        "brand": "SpeedyBee",
        "price_php": 1848,
        "weight_g": 8.9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=TX500+VTX",
        "color": "#171717",
        "specs": {
            "max_power_mw": 500,
            "frequency_band": "5.8GHz 40CH",
            "output": "analog",
            "connector": "MMCX",
            "smart_audio": True
        }
    },
    # ========== BATTERY ==========
    {
        "id": "cnhl-black-series-1300-6s-battery",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2016,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1300mAh+6S+100C",
        "color": "#0a0a0a",
        "specs": {
            "capacity_mah": 1300,
            "voltage": "6S",
            "c_rating": 100,
            "connector": "XT60",
            "weight_class": "standard"
        }
    },
    {
        "id": "tattu-r-line-v5-1400-6s-battery",
        "category": "battery",
        "name": "R-Line V5.0 1400mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2408,
        "weight_g": 258,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5.0+1400mAh+6S+150C",
        "color": "#101010",
        "specs": {
            "capacity_mah": 1400,
            "voltage": "6S",
            "c_rating": 150,
            "connector": "XT60",
            "weight_class": "standard"
        }
    },
    {
        "id": "gnb-1500-4s-battery",
        "category": "battery",
        "name": "1500mAh 4S 100C",
        "brand": "GNB",
        "price_php": 1288,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+1500mAh+4S+100C",
        "color": "#151515",
        "specs": {
            "capacity_mah": 1500,
            "voltage": "4S",
            "c_rating": 100,
            "connector": "XT60",
            "weight_class": "standard"
        }
    },
    {
        "id": "ovonic-2200-6s-battery",
        "category": "battery",
        "name": "2200mAh 6S 100C",
        "brand": "Ovonic",
        "price_php": 3080,
        "weight_g": 372,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ovonic+2200mAh+6S+100C",
        "color": "#0d0d0d",
        "specs": {
            "capacity_mah": 2200,
            "voltage": "6S",
            "c_rating": 100,
            "connector": "XT60",
            "weight_class": "long-range"
        }
    },
    {
        "id": "gens-ace-850-4s-battery",
        "category": "battery",
        "name": "850mAh 4S 100C",
        "brand": "Gens Ace",
        "price_php": 896,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gens+Ace+850mAh+4S+100C",
        "color": "#111111",
        "specs": {
            "capacity_mah": 850,
            "voltage": "4S",
            "c_rating": 100,
            "connector": "XT30",
            "weight_class": "micro"
        }
    },
    # ========== RECEIVER ==========
    {
        "id": "radiomaster-er6-elrs-receiver",
        "category": "receiver",
        "name": "ER6 ExpressLRS Receiver",
        "brand": "RadioMaster",
        "price_php": 728,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=ER6+ExpressLRS+Receiver",
        "color": "#222266",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_ghz": 2.4,
            "antenna_count": 2,
            "telemetry": True,
            "connector": "JST-SH"
        }
    },
    {
        "id": "happymodel-es24a-elrs-receiver",
        "category": "receiver",
        "name": "ES24A ExpressLRS Nano Receiver",
        "brand": "HappyModel",
        "price_php": 616,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+ES24A+ExpressLRS+Nano+Receiver",
        "color": "#0f0f0f",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_ghz": 2.4,
            "antenna_count": 1,
            "telemetry": True,
            "connector": "JST-SH"
        }
    },
    {
        "id": "tbs-crossfire-nano-se-receiver",
        "category": "receiver",
        "name": "Crossfire Nano SE Receiver",
        "brand": "TBS",
        "price_php": 1568,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+SE+Receiver",
        "color": "#161616",
        "specs": {
            "protocol": "Crossfire",
            "frequency_ghz": 0.868,
            "antenna_count": 1,
            "telemetry": True,
            "connector": "JST-SH"
        }
    },
    {
        "id": "betafpv-superd-elrs-receiver",
        "category": "receiver",
        "name": "SuperD ExpressLRS Diversity Receiver",
        "brand": "BetaFPV",
        "price_php": 560,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=SuperD+ExpressLRS+Diversity+Receiver",
        "color": "#101010",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_ghz": 2.4,
            "antenna_count": 1,
            "telemetry": True,
            "connector": "JST-SH"
        }
    },
    {
        "id": "frsky-rx8r-pro-receiver",
        "category": "receiver",
        "name": "RX8R Pro Receiver",
        "brand": "FrSky",
        "price_php": 784,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+RX8R+Pro+Receiver",
        "color": "#0d0d0d",
        "specs": {
            "protocol": "ACCST D16",
            "frequency_ghz": 2.4,
            "antenna_count": 2,
            "telemetry": True,
            "connector": "JST-SH"
        }
    },
    # ========== GPS ==========
    {
        "id": "matek-m8q-gps",
        "category": "gps",
        "name": "M8Q GPS Module",
        "brand": "Matek",
        "price_php": 1064,
        "weight_g": 7.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M8Q+GPS+Module",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 16,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "holybro-m9n-mini-gps",
        "category": "gps",
        "name": "M9N Mini GPS Module",
        "brand": "Holybro",
        "price_php": 1680,
        "weight_g": 6.8,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=M9N+Mini+GPS+Module",
        "color": "#141414",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 13,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "speedybee-m8n-gps",
        "category": "gps",
        "name": "M8N GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1120,
        "weight_g": 8.6,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=M8N+GPS+Module",
        "color": "#171717",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 15,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "beitian-be-222p-gps-module",
        "category": "gps",
        "name": "BE-222P GPS Module",
        "brand": "Beitian",
        "price_php": 672,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BE-222P+GPS+Module",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    # ========== ANTENNA ==========
    {
        "id": "truerc-singularity-sma-antenna",
        "category": "antenna",
        "name": "Singularity 5.8GHz RHCP SMA",
        "brand": "TrueRC",
        "price_php": 1344,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Singularity+5.8GHz+RHCP+SMA",
        "color": "#0a0a0a",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 3.5,
            "type": "patch"
        }
    },
    {
        "id": "lumenier-axii-2-rhcp-antenna",
        "category": "antenna",
        "name": "AXII 2 5.8GHz RHCP SMA",
        "brand": "Lumenier",
        "price_php": 896,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com/search?q=AXII+2+5.8GHz+RHCP+SMA",
        "color": "#141414",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.6,
            "type": "cloverleaf"
        }
    },
    {
        "id": "rushfpv-cherry-rhcp-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz RHCP SMA",
        "brand": "RushFPV",
        "price_php": 728,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Cherry+5.8GHz+RHCP+SMA",
        "color": "#161616",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.3,
            "type": "cloverleaf"
        }
    },
    {
        "id": "tbs-triumph-pro-rhcp-antenna",
        "category": "antenna",
        "name": "Triumph Pro 5.8GHz RHCP SMA",
        "brand": "TBS",
        "price_php": 1064,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Triumph+Pro+5.8GHz+RHCP+SMA",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.8,
            "type": "cloverleaf"
        }
    },
    {
        "id": "immersionrc-spironet-rhcp-antenna",
        "category": "antenna",
        "name": "SpiroNET 5.8GHz RHCP SMA",
        "brand": "ImmersionRC",
        "price_php": 784,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SpiroNET+5.8GHz+RHCP+SMA",
        "color": "#0d0d0d",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.2,
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
