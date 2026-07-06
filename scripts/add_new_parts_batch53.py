#!/usr/bin/env python3
"""Add a new batch of FPV drone parts across all 11 categories."""
import json

NEW_PARTS = [
    # ---- FRAME ----
    {
        "id": "geprc-cinelog35-v2-frame",
        "category": "frame",
        "name": "Cinelog35 V2 Frame",
        "brand": "GEPRC",
        "price_php": 2856,
        "weight_g": 62,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+Cinelog35+V2+Frame",
        "color": "#0f0f0f",
        "specs": {
            "size_mm": 142,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber + duct",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "flywoo-hex-explorer-lr6-6in-frame",
        "category": "frame",
        "name": "Hex Explorer LR6 6in Frame",
        "brand": "Flywoo",
        "price_php": 6720,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+Hex+Explorer+LR6+6in+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 254,
            "motor_mount_mm": 19,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "axisflying-manta5-v2-frame",
        "category": "frame",
        "name": "Manta5 V2 Frame",
        "brand": "Axisflying",
        "price_php": 3248,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/search?q=Axisflying+Manta5+V2+Frame",
        "color": "#202020",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28
        }
    },
    {
        "id": "transtec-force5-v2-frame",
        "category": "frame",
        "name": "Force5 V2 Frame",
        "brand": "TransTEC",
        "price_php": 2464,
        "weight_g": 80,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TransTEC+Force5+V2+Frame",
        "color": "#171717",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "armattan-rooster-x-5in-frame",
        "category": "frame",
        "name": "Rooster X 5in Frame",
        "brand": "Armattan",
        "price_php": 4816,
        "weight_g": 102,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+X+5in+Frame",
        "color": "#101010",
        "specs": {
            "size_mm": 227,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "source-one-v6-5in-frame",
        "category": "frame",
        "name": "Source One V6 5in Frame",
        "brand": "TBS",
        "price_php": 3920,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=Source+One+V6",
        "color": "#131313",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 27
        }
    },
    # ---- MOTOR ----
    {
        "id": "iflight-xing-e-pro-2207-2500kv",
        "category": "motor",
        "name": "XING-E Pro 2207 2500KV",
        "brand": "iFlight",
        "price_php": 1064,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+XING-E+Pro+2207+2500KV",
        "color": "#331100",
        "specs": {
            "kv": 2500,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "brotherhobby-avenger-2-pro-2207-1900kv",
        "category": "motor",
        "name": "Avenger 2 Pro 2207 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1260,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=BrotherHobby+Avenger+2+Pro+2207+1900KV",
        "color": "#220022",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "xnova-freestyle-pro-2408-1650kv",
        "category": "motor",
        "name": "Freestyle Pro 2408 1650KV",
        "brand": "Xnova",
        "price_php": 1736,
        "weight_g": 39,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Xnova+Freestyle+Pro+2408+1650KV",
        "color": "#002233",
        "specs": {
            "kv": 1650,
            "stator_size": "2408",
            "motor_mount_mm": 19,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "rcinpower-gts-v4-2306-5-1850kv",
        "category": "motor",
        "name": "GTS V4 2306.5 1850KV",
        "brand": "Rcinpower",
        "price_php": 1428,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rcinpower+GTS+V4+2306.5+1850KV",
        "color": "#113300",
        "specs": {
            "kv": 1850,
            "stator_size": "2306.5",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 39
        }
    },
    # ---- ESC ----
    {
        "id": "flycolor-raptor-s-tower-60a-4in1",
        "category": "esc",
        "name": "Raptor S-Tower 60A 4-in-1",
        "brand": "Flycolor",
        "price_php": 2688,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+Raptor+S-Tower+60A+4-in-1",
        "color": "#001a00",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "holybro-tekko32-f4-65a-4in1-v2",
        "category": "esc",
        "name": "Tekko32 F4 65A 4-in-1 V2",
        "brand": "Holybro",
        "price_php": 3584,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=HolyBro+Tekko32+F4+65A+4-in-1+V2",
        "color": "#002200",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "jhemcu-f45a-4in1-esc",
        "category": "esc",
        "name": "F45A 4-in-1 ESC",
        "brand": "JHEMCU",
        "price_php": 1792,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=JHEMCU+F45A+4-in-1+ESC",
        "color": "#111100",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "speedybee-bls-60a-4in1-esc-v4",
        "category": "esc",
        "name": "BLS 60A 4-in-1 ESC V4",
        "brand": "SpeedyBee",
        "price_php": 2576,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+BLS+60A+4-in-1+ESC+V4",
        "color": "#002211",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    # ---- FC ----
    {
        "id": "speedybee-f405-v4-1",
        "category": "fc",
        "name": "F405 V4.1 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2016,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+F405+V4.1",
        "color": "#000044",
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
        "id": "foxeer-f722-v4-aio",
        "category": "fc",
        "name": "F722 V4 AIO Flight Controller",
        "brand": "Foxeer",
        "price_php": 2240,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+F722+V4+AIO",
        "color": "#001133",
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
        "id": "airbot-f7-hd-mini-v2",
        "category": "fc",
        "name": "F7 HD Mini V2 Flight Controller",
        "brand": "Airbot",
        "price_php": 2856,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Airbot+F7+HD+Mini+V2",
        "color": "#000033",
        "specs": {
            "gyro": "ICM20689",
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
    {
        "id": "jhemcu-gf16-f745-aio",
        "category": "fc",
        "name": "GF16 F745 AIO Flight Controller",
        "brand": "JHEMCU",
        "price_php": 1904,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=JHEMCU+GF16+F745+AIO",
        "color": "#001122",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 16,
            "stack_mount_mm": 16,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "hglrc-zeus-f722-v2-mini",
        "category": "fc",
        "name": "Zeus F722 V2 Mini Flight Controller",
        "brand": "HGLRC",
        "price_php": 2128,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Zeus+F722+V2+Mini",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "diatone-mamba-f405-mini-mk5",
        "category": "fc",
        "name": "Mamba F405 Mini MK5 Flight Controller",
        "brand": "Diatone",
        "price_php": 1764,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Diatone+Mamba+F405+Mini+MK5",
        "color": "#000066",
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
    # ---- PROPELLER ----
    {
        "id": "hqprop-5-1x3-1x3-ethix-s6",
        "category": "propeller",
        "name": "5.1X3.1X3 Ethix S6",
        "brand": "HQProp",
        "price_php": 280,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+5.1X3.1X3+Ethix+S6",
        "color": "#999999",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.1,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "white"]
        }
    },
    {
        "id": "gemfan-hurricane-51477-v3",
        "category": "propeller",
        "name": "Hurricane 51477 V3",
        "brand": "Gemfan",
        "price_php": 252,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51477+V3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.77,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "dal-cyclone-t5047c-v2",
        "category": "propeller",
        "name": "Cyclone T5047C V2",
        "brand": "DAL",
        "price_php": 224,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T5047C+V2",
        "color": "#0d0d0d",
        "specs": {
            "diameter_inch": 5.0,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    # ---- CAMERA ----
    {
        "id": "caddx-ratel-air-2",
        "category": "camera",
        "name": "Ratel Air 2",
        "brand": "Caddx",
        "price_php": 1176,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Caddx+Ratel+Air+2",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" Starlight",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-micro-toothless-2-nano",
        "category": "camera",
        "name": "Micro Toothless 2 Nano",
        "brand": "Foxeer",
        "price_php": 1064,
        "weight_g": 3.2,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Micro+Toothless+2+Nano",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-hybrid-3s",
        "category": "camera",
        "name": "Hybrid 3S",
        "brand": "RunCam",
        "price_php": 3360,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Runcam+Hybrid+3S",
        "color": "#222",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Analog+4K",
            "tvl": 1000,
            "voltage_range": "6-22V"
        }
    },
    {
        "id": "foxeer-night-cat-3-nano",
        "category": "camera",
        "name": "Night Cat 3 Nano",
        "brand": "Foxeer",
        "price_php": 1288,
        "weight_g": 3.8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Night+Cat+3+Nano",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" Starlight",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-loris-4k-v2",
        "category": "camera",
        "name": "Loris 4K V2",
        "brand": "Caddx",
        "price_php": 5320,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Loris+4K+V2",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.7\" CMOS",
            "fov_deg": 145,
            "format": "Digital",
            "resolution": "4K60",
            "voltage_range": "7.4-26.4V",
            "video_system": "HD recording"
        }
    },
    # ---- VTX ----
    {
        "id": "rush-tank-ultimate-v2-vtx",
        "category": "vtx",
        "name": "Tank Ultimate V2 VTX",
        "brand": "RushFPV",
        "price_php": 3080,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=RushFPV+Tank+Ultimate+V2+VTX",
        "color": "#331100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "immersionrc-ghost-atto-vtx",
        "category": "vtx",
        "name": "Ghost Atto VTX",
        "brand": "ImmersionRC",
        "price_php": 1904,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+Ghost+Atto+VTX",
        "color": "#0d0d0d",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-20V",
            "connector": "U.FL"
        }
    },
    {
        "id": "walksnail-avatar-hd-mini-v4",
        "category": "vtx",
        "name": "Avatar HD Mini V4 VTX",
        "brand": "Walksnail",
        "price_php": 5600,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Walksnail+Avatar+HD+Mini+V4",
        "color": "#001122",
        "specs": {
            "power_mw_max": 900,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "6-17V",
            "connector": "U.FL"
        }
    },
    # ---- BATTERY ----
    {
        "id": "cnhl-ministar-1400mah-6s-120c",
        "category": "battery",
        "name": "MiniStar 1400mAh 6S 120C",
        "brand": "CNHL",
        "price_php": 1904,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniStar+1400mAh+6S+120C",
        "color": "#cc0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-r-line-v6-1300mah-6s-150c",
        "category": "battery",
        "name": "R-Line V6 1300mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2352,
        "weight_g": 200,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V6+1300mAh+6S+150C",
        "color": "#ffcc00",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gnb-fullymax-1300mah-6s-100c",
        "category": "battery",
        "name": "Fullymax 1300mAh 6S 100C",
        "brand": "GNB",
        "price_php": 1568,
        "weight_g": 190,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+Fullymax+1300mAh+6S+100C",
        "color": "#003366",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    # ---- RECEIVER ----
    {
        "id": "radiomaster-rp4td-v2-true-diversity",
        "category": "receiver",
        "name": "RP4TD V2 True Diversity Receiver",
        "brand": "RadioMaster",
        "price_php": 1064,
        "weight_g": 2.1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RadioMaster+RP4TD+V2+True+Diversity",
        "color": "#333399",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "tbs-crossfire-nano-rx-v6",
        "category": "receiver",
        "name": "Crossfire Nano RX V6",
        "brand": "TBS",
        "price_php": 1848,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Crossfire+Nano+RX+V6",
        "color": "#111111",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-ep2-elrs-2-4ghz-receiver",
        "category": "receiver",
        "name": "EP2 ELRS 2.4GHz Receiver",
        "brand": "HappyModel",
        "price_php": 728,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ELRS+2.4GHz+Receiver",
        "color": "#222222",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    # ---- GPS ----
    {
        "id": "matek-m10-5883-gps-module",
        "category": "gps",
        "name": "M10-5883 GPS Module",
        "brand": "Matek",
        "price_php": 1568,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10-5883+GPS+Module",
        "color": "#1a1a1a",
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
        "id": "hglrc-m100-5883-gps",
        "category": "gps",
        "name": "M100-5883 GPS",
        "brand": "HGLRC",
        "price_php": 1400,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+M100-5883+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 6,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    # ---- ANTENNA ----
    {
        "id": "tbs-triumph-pro-v2",
        "category": "antenna",
        "name": "Triumph Pro V2 5.8GHz RHCP SMA",
        "brand": "TBS",
        "price_php": 1120,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=TBS+Triumph+Pro+V2",
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
        "id": "rushfpv-cherry-v2-antenna",
        "category": "antenna",
        "name": "Cherry V2 5.8GHz RHCP SMA",
        "brand": "RushFPV",
        "price_php": 784,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=RushFPV+Cherry+V2+5.8GHz+RHCP+SMA",
        "color": "#161616",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.4,
            "type": "cloverleaf"
        }
    },
    {
        "id": "akk-bolt-5-8ghz-rhcp-antenna",
        "category": "antenna",
        "name": "Bolt 5.8GHz RHCP SMA",
        "brand": "AKK",
        "price_php": 392,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+Bolt+5.8GHz+RHCP+SMA",
        "color": "#003300",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 1.9,
            "type": "cloverleaf"
        }
    },
    {
        "id": "realacc-tx5090-5-8ghz-antenna",
        "category": "antenna",
        "name": "TX5090 5.8GHz RHCP SMA",
        "brand": "Realacc",
        "price_php": 336,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Realacc+TX5090+5.8GHz+RHCP+SMA",
        "color": "#222222",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.0,
            "type": "cloverleaf"
        }
    },
    {
        "id": "lumenier-axii-3-rhcp-antenna",
        "category": "antenna",
        "name": "AXII 3 5.8GHz RHCP SMA",
        "brand": "Lumenier",
        "price_php": 896,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com/search?q=Lumenier+AXII+3+5.8GHz+RHCP",
        "color": "#141414",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.5,
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
