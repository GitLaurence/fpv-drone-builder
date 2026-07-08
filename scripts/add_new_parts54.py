"""Batch 54: adds real, currently-shipping FPV parts across all 11 categories
that were missing from the catalog, following the existing schema and
buy_url conventions (retailer/brand search URLs, never dead product links).
"""
import json

NEW_PARTS = [
    # ========== FRAME ==========
    {
        "id": "axisflying-cinelog25-v2-frame",
        "category": "frame",
        "name": "Cinelog25 V2 Frame Kit",
        "brand": "Axisflying",
        "price_php": 3920,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/search?q=Cinelog25+V2+Frame",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 250,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "iflight-chimera7-pro-v2-frame",
        "category": "frame",
        "name": "Chimera7 Pro V2 Frame Kit",
        "brand": "iFlight",
        "price_php": 5040,
        "weight_g": 128,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=Chimera7+Pro+V2+Frame",
        "color": "#141414",
        "specs": {
            "size_mm": 305,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "flywoo-hex-frame",
        "category": "frame",
        "name": "Hex 3.5\" HD Frame Kit",
        "brand": "Flywoo",
        "price_php": 2016,
        "weight_g": 54,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Hex+3.5+HD+Frame",
        "color": "#0f0f0f",
        "specs": {
            "size_mm": 156,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber"
        }
    },
    {
        "id": "tbs-source-one-v6-frame",
        "category": "frame",
        "name": "Source One V6 5\" Frame Kit",
        "brand": "TBS",
        "price_php": 1904,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Source+One+V6+5+Frame",
        "color": "#202020",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "armattan-rooster-6-frame",
        "category": "frame",
        "name": "Rooster 6\" Frame Kit",
        "brand": "Armattan",
        "price_php": 6720,
        "weight_g": 118,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+6+Frame",
        "color": "#181818",
        "specs": {
            "size_mm": 260,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },

    # ========== MOTOR ==========
    {
        "id": "tmotor-velox-v2807-5-v2",
        "category": "motor",
        "name": "Velox V2807.5 V2 1300KV",
        "brand": "T-Motor",
        "price_php": 1568,
        "weight_g": 32.5,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=Velox+V2807.5+V2+1300KV",
        "color": "#2b2b2b",
        "specs": {
            "kv": 1300,
            "stator_size": "2807.5",
            "motor_mount_mm": 25.5,
            "max_voltage_s": 6
        }
    },
    {
        "id": "brotherhobby-avenger-v4-2306",
        "category": "motor",
        "name": "Avenger V4 2306 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1064,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=Avenger+V4+2306+1900KV",
        "color": "#333333",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "max_voltage_s": 6
        }
    },
    {
        "id": "flywoo-nin-2216-v2",
        "category": "motor",
        "name": "NIN 2216 V2 900KV",
        "brand": "Flywoo",
        "price_php": 1288,
        "weight_g": 47,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=NIN+2216+V2+900KV",
        "color": "#101010",
        "specs": {
            "kv": 900,
            "stator_size": "2216",
            "motor_mount_mm": 25.5,
            "max_voltage_s": 8
        }
    },
    {
        "id": "iflight-xing2-2807-v2",
        "category": "motor",
        "name": "XING2 2807 1300KV V2",
        "brand": "iFlight",
        "price_php": 1176,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=XING2+2807+1300KV+V2",
        "color": "#262626",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 25.5,
            "max_voltage_s": 6
        }
    },
    {
        "id": "emax-eco-ii-2807",
        "category": "motor",
        "name": "ECO II 2807 1300KV",
        "brand": "EMAX",
        "price_php": 952,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com/search?q=ECO+II+2807+1300KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 25.5,
            "max_voltage_s": 6
        }
    },

    # ========== ESC ==========
    {
        "id": "speedybee-bls-60a-4in1",
        "category": "esc",
        "name": "BLS 60A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2464,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=BLS+60A+4-in-1+ESC",
        "color": "#0d0d0d",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 30.5
        }
    },
    {
        "id": "diatone-tekko32-f4-65a",
        "category": "esc",
        "name": "Tekko32 F4 65A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 2856,
        "weight_g": 13.5,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Tekko32+F4+65A+4-in-1+ESC",
        "color": "#111111",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 30.5
        }
    },
    {
        "id": "foxeer-reaper-55a-4in1",
        "category": "esc",
        "name": "Reaper 55A 4-in-1 ESC",
        "brand": "Foxeer",
        "price_php": 2184,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Reaper+55A+4-in-1+ESC",
        "color": "#151515",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 25.5
        }
    },
    {
        "id": "mamba-f405-45a-esc",
        "category": "esc",
        "name": "Mamba F45_128K 45A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 1848,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Mamba+F45_128K+45A+4-in-1+ESC",
        "color": "#1f1f1f",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 4,
            "protocol": "DShot600",
            "form_factor_mm": 20
        }
    },
    {
        "id": "hglrc-zeus-60a-4in1-esc",
        "category": "esc",
        "name": "Zeus 60A 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 2296,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Zeus+60A+4-in-1+ESC",
        "color": "#0a0a0a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 30.5
        }
    },

    # ========== FLIGHT CONTROLLER ==========
    {
        "id": "speedybee-f405-v4-aio",
        "category": "fc",
        "name": "F405 V4 AIO Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2352,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=F405+V4+AIO+Flight+Controller",
        "color": "#0e0e0e",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5
        }
    },
    {
        "id": "diatone-mamba-f722-mk3",
        "category": "fc",
        "name": "Mamba F722 Mk3 Flight Controller",
        "brand": "Diatone",
        "price_php": 2688,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Mamba+F722+Mk3+Flight+Controller",
        "color": "#131313",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5
        }
    },
    {
        "id": "hglrc-zeus-f745-v2-fc",
        "category": "fc",
        "name": "Zeus F745 V2 Flight Controller",
        "brand": "HGLRC",
        "price_php": 2912,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Zeus+F745+V2+Flight+Controller",
        "color": "#0c0c0c",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 25.5,
            "stack_mount_mm": 25.5
        }
    },
    {
        "id": "iflight-blitz-mini-f7-fc",
        "category": "fc",
        "name": "BLITZ Mini F7 Flight Controller",
        "brand": "iFlight",
        "price_php": 2464,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=BLITZ+Mini+F7+Flight+Controller",
        "color": "#171717",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },
    {
        "id": "holybro-kakute-h7-mini-v2-fc",
        "category": "fc",
        "name": "Kakute H7 Mini V2 Flight Controller",
        "brand": "Holybro",
        "price_php": 3080,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Kakute+H7+Mini+V2+Flight+Controller",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },

    # ========== PROPELLER ==========
    {
        "id": "hqprop-dt5-1x3-v1s",
        "category": "propeller",
        "name": "DT5.1X3 V1S Tri-Blade Prop",
        "brand": "HQProp",
        "price_php": 196,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DT5.1X3+V1S",
        "color": "#404040",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "azure-power-ap-race-5-prop",
        "category": "propeller",
        "name": "AP-Race 5\" Tri-Blade Prop",
        "brand": "Azure Power",
        "price_php": 224,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Azure+Power+AP-Race+5+Prop",
        "color": "#383838",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "dalprop-cyclone-t5047c",
        "category": "propeller",
        "name": "Cyclone T5047C Tri-Blade Prop",
        "brand": "DALPROP",
        "price_php": 168,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DALPROP+Cyclone+T5047C",
        "color": "#454545",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "gemfan-hurricane-2015-3-prop",
        "category": "propeller",
        "name": "Hurricane 2015-3 Micro Prop",
        "brand": "Gemfan",
        "price_php": 112,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+2015-3",
        "color": "#4a4a4a",
        "specs": {
            "diameter_inch": 2,
            "pitch": 1.5,
            "blade_count": 3,
            "shaft_mm": 1.5
        }
    },

    # ========== CAMERA ==========
    {
        "id": "runcam-link-wasp-camera",
        "category": "camera",
        "name": "Link Wasp HD Camera",
        "brand": "RunCam",
        "price_php": 3808,
        "weight_g": 7.2,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Link+Wasp+HD+Camera",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "digital",
            "video_system": "runcam-link"
        }
    },
    {
        "id": "foxeer-toothless-2-nano-camera",
        "category": "camera",
        "name": "Toothless 2 Nano Camera",
        "brand": "Foxeer",
        "price_php": 1568,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Toothless+2+Nano+Camera",
        "color": "#121212",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "caddx-ratel-3-camera",
        "category": "camera",
        "name": "Ratel 3 FPV Camera",
        "brand": "Caddx",
        "price_php": 1904,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ratel+3+FPV+Camera",
        "color": "#151515",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 165,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "walksnail-avatar-hd-pro-v3-camera",
        "category": "camera",
        "name": "Avatar HD Pro Kit V3 Camera",
        "brand": "Walksnail",
        "price_php": 5152,
        "weight_g": 10.5,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+Pro+Kit+V3+Camera",
        "color": "#0f0f0f",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 150,
            "format": "digital",
            "video_system": "walksnail"
        }
    },

    # ========== VTX ==========
    {
        "id": "rushfpv-tank-ultimate-2-vtx",
        "category": "vtx",
        "name": "Tank Ultimate 2 VTX",
        "brand": "RushFPV",
        "price_php": 3696,
        "weight_g": 17,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Tank+Ultimate+2+VTX",
        "color": "#191919",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },
    {
        "id": "iflight-forcevtx-2-5w",
        "category": "vtx",
        "name": "ForceVTX 2.5W",
        "brand": "iFlight",
        "price_php": 3024,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=ForceVTX+2.5W",
        "color": "#0b0b0b",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },
    {
        "id": "hglrc-titan-vtx-1w",
        "category": "vtx",
        "name": "Titan 1W VTX",
        "brand": "HGLRC",
        "price_php": 1120,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Titan+1W+VTX",
        "color": "#101010",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "TrampHV",
            "video_system": "analog"
        }
    },

    # ========== BATTERY ==========
    {
        "id": "cnhl-ministar-1500-6s-battery",
        "category": "battery",
        "name": "MiniStar 1500mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2072,
        "weight_g": 254,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniStar+1500mAh+6S+100C",
        "color": "#2a2a2a",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60"
        }
    },
    {
        "id": "tattu-rline-v5-1300-6s-battery",
        "category": "battery",
        "name": "R-Line V5.0 1300mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2408,
        "weight_g": 232,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5.0+1300mAh+6S+150C",
        "color": "#252525",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60"
        }
    },
    {
        "id": "gnb-850-4s-battery",
        "category": "battery",
        "name": "850mAh 4S 100C",
        "brand": "GNB",
        "price_php": 896,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+850mAh+4S+100C",
        "color": "#2f2f2f",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 850,
            "c_rating": 100,
            "connector": "XT30"
        }
    },

    # ========== RECEIVER ==========
    {
        "id": "tbs-crossfire-nano-rx-se",
        "category": "receiver",
        "name": "Crossfire Nano RX SE",
        "brand": "TBS",
        "price_php": 1568,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+RX+SE",
        "color": "#111111",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915
        }
    },
    {
        "id": "radiomaster-er6-elrs-rx",
        "category": "receiver",
        "name": "ER6 ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 784,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=ER6+ELRS+Receiver",
        "color": "#1c1c1c",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400
        }
    },
    {
        "id": "happymodel-elrs-pp-rx",
        "category": "receiver",
        "name": "EP2 ExpressLRS PWM/PPM RX",
        "brand": "HappyModel",
        "price_php": 616,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ExpressLRS+RX",
        "color": "#222222",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400
        }
    },

    # ========== GPS ==========
    {
        "id": "matek-m10-5883-gps",
        "category": "gps",
        "name": "M10-5883 GPS + Compass",
        "brand": "Matek",
        "price_php": 1512,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10-5883+GPS+Compass",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 16,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "betafpv-m10-lite-gps",
        "category": "gps",
        "name": "M10 Lite GPS Module",
        "brand": "BetaFPV",
        "price_php": 896,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=M10+Lite+GPS+Module",
        "color": "#141414",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },

    # ========== ANTENNA ==========
    {
        "id": "truerc-singularity-rhcp-antenna",
        "category": "antenna",
        "name": "Singularity 5.8GHz RHCP SMA",
        "brand": "TrueRC",
        "price_php": 1120,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Singularity+5.8GHz+RHCP",
        "color": "#0d0d0d",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 4.5,
            "type": "patch"
        }
    },
    {
        "id": "foxeer-pagoda-pro-rhcp-antenna",
        "category": "antenna",
        "name": "Pagoda Pro 5.8GHz RHCP SMA",
        "brand": "Foxeer",
        "price_php": 560,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Pagoda+Pro+5.8GHz+RHCP",
        "color": "#131313",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.3,
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
