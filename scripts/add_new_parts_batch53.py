#!/usr/bin/env python3
"""Batch 53: real, current-production FPV parts across all 11 categories,
adding more brand/model coverage on top of batch52."""
import json

NEW_PARTS = [
    # ========== FRAME ==========
    {
        "id": "tbs-source-one-v5-frame",
        "category": "frame",
        "name": "Source One V5 5\" Frame Kit",
        "brand": "TBS",
        "price_php": 1904,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Source+One+V5+Frame+Kit",
        "color": "#131313",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "flywoo-firefly-baby-quad-frame",
        "category": "frame",
        "name": "Firefly Baby Quad 1S HD Frame",
        "brand": "Flywoo",
        "price_php": 896,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Firefly+Baby+Quad+1S+HD+Frame",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 65,
            "motor_mount_mm": 9,
            "prop_clearance_inch": 1.6,
            "stack_mount_mm": 16,
            "material": "carbon fiber",
            "arm_thickness_mm": 1.5,
            "standoff_height_mm": 12
        }
    },
    {
        "id": "iflight-chimera7-pro-frame",
        "category": "frame",
        "name": "Chimera7 Pro Frame Kit",
        "brand": "iFlight",
        "price_php": 3248,
        "weight_g": 138,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=Chimera7+Pro+Frame+Kit",
        "color": "#181818",
        "specs": {
            "size_mm": 320,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "armattan-rooster-6-frame",
        "category": "frame",
        "name": "Rooster 6\" Frame Kit",
        "brand": "Armattan",
        "price_php": 4816,
        "weight_g": 115,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+6+Frame+Kit",
        "color": "#141414",
        "specs": {
            "size_mm": 254,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28
        }
    },
    {
        "id": "diatone-taycan-mxc-frame",
        "category": "frame",
        "name": "Taycan MX-C Frame Kit",
        "brand": "Diatone",
        "price_php": 1736,
        "weight_g": 79,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Taycan+MX-C+Frame+Kit",
        "color": "#0f1115",
        "specs": {
            "size_mm": 235,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "geprc-smart35-frame",
        "category": "frame",
        "name": "Smart35 O3 Frame Kit",
        "brand": "GEPRC",
        "price_php": 2184,
        "weight_g": 68,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=Smart35+O3+Frame+Kit",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 150,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 20,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 18
        }
    },
    # ========== MOTOR ==========
    {
        "id": "tmotor-f40-pro-iv-motor",
        "category": "motor",
        "name": "F40 Pro IV 2400KV",
        "brand": "T-Motor",
        "price_php": 896,
        "weight_g": 30.5,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F40+Pro+IV+2400KV",
        "color": "#1c1c1c",
        "specs": {
            "kv": 2400,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "brotherhobby-returner-r6-motor",
        "category": "motor",
        "name": "Returner R6 2450KV",
        "brand": "BrotherHobby",
        "price_php": 1064,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://brotherhobby.com/search?q=Returner+R6+2450KV",
        "color": "#202020",
        "specs": {
            "kv": 2450,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "emax-eco-ii-2306-motor",
        "category": "motor",
        "name": "ECO II 2306 2400KV",
        "brand": "Emax",
        "price_php": 616,
        "weight_g": 31.6,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com/search?q=ECO+II+2306+2400KV",
        "color": "#151515",
        "specs": {
            "kv": 2400,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 34
        }
    },
    {
        "id": "flywoo-nin-1404-motor",
        "category": "motor",
        "name": "NIN 1404 3800KV",
        "brand": "Flywoo",
        "price_php": 728,
        "weight_g": 12.5,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=NIN+1404+3800KV",
        "color": "#0f0f0f",
        "specs": {
            "kv": 3800,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 18
        }
    },
    {
        "id": "iflight-xing2-2207-motor",
        "category": "motor",
        "name": "XING2 2207 1855KV",
        "brand": "iFlight",
        "price_php": 784,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=XING2+2207+1855KV",
        "color": "#1e1e1e",
        "specs": {
            "kv": 1855,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "sunnysky-r2306-motor",
        "category": "motor",
        "name": "R2306 2500KV",
        "brand": "SunnySky",
        "price_php": 672,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SunnySky+R2306+2500KV",
        "color": "#191919",
        "specs": {
            "kv": 2500,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },
    # ========== ESC ==========
    {
        "id": "holybro-tekko32-f4-60a-esc",
        "category": "esc",
        "name": "Tekko32 F4 60A 4-in-1",
        "brand": "Holybro",
        "price_php": 3416,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Tekko32+F4+60A+4-in-1",
        "color": "#0a1a2a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "diatone-mamba-f45-45a-esc",
        "category": "esc",
        "name": "Mamba F45 45A 4-in-1",
        "brand": "Diatone",
        "price_php": 1904,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Mamba+F45+45A+4-in-1",
        "color": "#111318",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "iflight-succex-e-50a-esc",
        "category": "esc",
        "name": "SucceX-E 50A 4-in-1",
        "brand": "iFlight",
        "price_php": 2072,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=SucceX-E+50A+4-in-1",
        "color": "#161616",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "speedybee-bls-50a-esc",
        "category": "esc",
        "name": "BLS 50A 4-in-1 32-bit",
        "brand": "SpeedyBee",
        "price_php": 1848,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://speedybee.com/search?q=BLS+50A+4-in-1+32-bit",
        "color": "#101010",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "hglrc-sky-f58-60a-esc",
        "category": "esc",
        "name": "Sky F58 60A 4-in-1",
        "brand": "HGLRC",
        "price_php": 2408,
        "weight_g": 11.5,
        "in_stock": True,
        "buy_url": "https://hglrc.com/search?q=Sky+F58+60A+4-in-1",
        "color": "#131313",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    # ========== FC ==========
    {
        "id": "matek-f722-se-fc",
        "category": "fc",
        "name": "F722-SE Flight Controller",
        "brand": "Matek",
        "price_php": 2464,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F722-SE+Flight+Controller",
        "color": "#001a33",
        "specs": {
            "gyro": "ICM42688-P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "speedybee-f7-v3-fc",
        "category": "fc",
        "name": "F7 V3 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 1680,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://speedybee.com/search?q=F7+V3+Flight+Controller",
        "color": "#0d0d0d",
        "specs": {
            "gyro": "ICM42688-P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
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
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Kakute+H7+V2+Flight+Controller",
        "color": "#0a1a2a",
        "specs": {
            "gyro": "ICM20689",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "iflight-succex-e-f7-fc",
        "category": "fc",
        "name": "SucceX-E F7 Flight Controller",
        "brand": "iFlight",
        "price_php": 1792,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=SucceX-E+F7+Flight+Controller",
        "color": "#181818",
        "specs": {
            "gyro": "ICM20689",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "hglrc-zeus-f722-fc",
        "category": "fc",
        "name": "Zeus F722 Mini Flight Controller",
        "brand": "HGLRC",
        "price_php": 2016,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://hglrc.com/search?q=Zeus+F722+Mini+Flight+Controller",
        "color": "#131313",
        "specs": {
            "gyro": "ICM42688-P",
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
    # ========== PROPELLER ==========
    {
        "id": "hqprop-dp5x43x3-propeller",
        "category": "propeller",
        "name": "DP5x4.3x3 5-inch Tri-Blade",
        "brand": "HQProp",
        "price_php": 224,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP5x4.3x3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "gemfan-hurricane-51466-propeller",
        "category": "propeller",
        "name": "Hurricane 51466 5-inch Tri-Blade",
        "brand": "Gemfan",
        "price_php": 235,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466",
        "color": "#141414",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "grey"]
        }
    },
    {
        "id": "dal-cyclone-t5047c-propeller",
        "category": "propeller",
        "name": "Cyclone T5047C 5-inch Tri-Blade",
        "brand": "DAL",
        "price_php": 213,
        "weight_g": 4.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T5047C",
        "color": "#0f0f0f",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    {
        "id": "hqprop-dp3x3x3-propeller",
        "category": "propeller",
        "name": "DP3x3x3 3-inch Tri-Blade",
        "brand": "HQProp",
        "price_php": 168,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP3x3x3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 3,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "gemfan-hurricane-2015-propeller",
        "category": "propeller",
        "name": "Hurricane 2015 2-inch Tri-Blade",
        "brand": "Gemfan",
        "price_php": 145,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+2015",
        "color": "#141414",
        "specs": {
            "diameter_inch": 2,
            "pitch": 1.5,
            "blade_count": 3,
            "shaft_mm": 0.8,
            "color_options": ["black", "grey", "green"]
        }
    },
    # ========== CAMERA ==========
    {
        "id": "runcam-phoenix2-analog-camera",
        "category": "camera",
        "name": "Phoenix 2 1000TVL Analog",
        "brand": "RunCam",
        "price_php": 1064,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://runcam.com/search?q=Phoenix+2+1000TVL",
        "color": "#111111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-razer-micro-camera",
        "category": "camera",
        "name": "Razer Micro 1200TVL Analog",
        "brand": "Foxeer",
        "price_php": 896,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://foxeer.com/search?q=Razer+Micro+1200TVL",
        "color": "#161616",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ratel2-camera",
        "category": "camera",
        "name": "Ratel 2 Starlight Analog",
        "brand": "Caddx",
        "price_php": 1512,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ratel+2+Starlight",
        "color": "#131313",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog Starlight",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-hybrid3-camera",
        "category": "camera",
        "name": "Hybrid 3 4K Analog/DVR",
        "brand": "RunCam",
        "price_php": 3696,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://runcam.com/search?q=Hybrid+3+4K",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Analog + 4K Digital DVR",
            "tvl": 1200,
            "voltage_range": "5-20V"
        }
    },
    {
        "id": "caddx-ratel-pro-camera",
        "category": "camera",
        "name": "Ratel Pro Analog",
        "brand": "Caddx",
        "price_php": 1176,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ratel+Pro",
        "color": "#181818",
        "specs": {
            "sensor": "1/2.8\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    # ========== VTX ==========
    {
        "id": "tbs-unify-pro32-hv-vtx",
        "category": "vtx",
        "name": "Unify Pro32 HV 800mW",
        "brand": "TBS",
        "price_php": 5040,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro32+HV",
        "color": "#111111",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "7-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "iflight-transtec-vega-vtx",
        "category": "vtx",
        "name": "TransTEC Vega 800mW",
        "brand": "iFlight",
        "price_php": 1904,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=TransTEC+Vega+800mW",
        "color": "#181818",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "rush-tank-solo-vtx",
        "category": "vtx",
        "name": "Tank Solo 800mW",
        "brand": "RushFPV",
        "price_php": 1568,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://rushfpv.com/search?q=Tank+Solo+800mW",
        "color": "#141414",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "hglrc-titan-vtx350-vtx",
        "category": "vtx",
        "name": "Titan VTX350 350mW",
        "brand": "HGLRC",
        "price_php": 1064,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://hglrc.com/search?q=Titan+VTX350+350mW",
        "color": "#131313",
        "specs": {
            "power_mw_max": 350,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "walksnail-avatar-hd-v2-vtx",
        "category": "vtx",
        "name": "Avatar HD V2 VTX 1W",
        "brand": "Walksnail",
        "price_php": 5488,
        "weight_g": 9.6,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+V2+VTX",
        "color": "#0d0d0d",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Walksnail Digital",
            "bands": "Digital",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    # ========== BATTERY ==========
    {
        "id": "cnhl-blackseries-1500mah-6s-battery",
        "category": "battery",
        "name": "Black Series 1500mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2016,
        "weight_g": 262,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1500mAh+6S+100C",
        "color": "#000000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-rline-1300mah-4s-battery",
        "category": "battery",
        "name": "R-Line V4 1300mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1624,
        "weight_g": 172,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V4+1300mAh+4S+130C",
        "color": "#003322",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gnb-850mah-4s-battery",
        "category": "battery",
        "name": "850mAh 4S 100C",
        "brand": "GNB",
        "price_php": 952,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+850mAh+4S+100C",
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
        "id": "cnhl-minired-650mah-4s-battery",
        "category": "battery",
        "name": "MiniRed 650mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 728,
        "weight_g": 76,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniRed+650mAh+4S+100C",
        "color": "#8b0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 650,
            "c_rating": 100,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "bonka-1300mah-6s-battery",
        "category": "battery",
        "name": "1300mAh 6S 100C",
        "brand": "Bonka",
        "price_php": 1848,
        "weight_g": 218,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Bonka+1300mAh+6S+100C",
        "color": "#1a1a1a",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    # ========== RECEIVER ==========
    {
        "id": "tbs-crossfire-nano-rx-receiver",
        "category": "receiver",
        "name": "Crossfire Nano RX",
        "brand": "TBS",
        "price_php": 1568,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+RX",
        "color": "#111111",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-elrs-ep2-receiver",
        "category": "receiver",
        "name": "EP2 ELRS 2.4GHz Nano Receiver",
        "brand": "HappyModel",
        "price_php": 616,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ELRS+2.4GHz",
        "color": "#222222",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "frsky-r9mm-receiver",
        "category": "receiver",
        "name": "R9 MM 900MHz Long Range RX",
        "brand": "FrSky",
        "price_php": 1400,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R9+MM+900MHz",
        "color": "#1c1c1c",
        "specs": {
            "protocol": "ACCST",
            "frequency_mhz": 900,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "radiomaster-rp1-elrs-receiver",
        "category": "receiver",
        "name": "RP1 ELRS 2.4GHz Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 672,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://radiomasterrc.com/search?q=RP1+ELRS+2.4GHz",
        "color": "#191919",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "team-blacksheep-tracer-nano-receiver",
        "category": "receiver",
        "name": "Tracer Nano RX",
        "brand": "TBS",
        "price_php": 1288,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://team-blacksheep.com/search?q=Tracer+Nano+RX",
        "color": "#151515",
        "specs": {
            "protocol": "Tracer",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    # ========== GPS ==========
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS + Compass",
        "brand": "Matek",
        "price_php": 1568,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-5883+GPS",
        "color": "#001a33",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m10-gps",
        "category": "gps",
        "name": "Micro M10 GPS Module",
        "brand": "Holybro",
        "price_php": 1288,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Micro+M10+GPS+Module",
        "color": "#0a1a2a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "beitian-bn-220-gps",
        "category": "gps",
        "name": "BN-220 GPS Module",
        "brand": "Beitian",
        "price_php": 728,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-220+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "iflight-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "iFlight",
        "price_php": 1120,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=M10+GPS+Module",
        "color": "#181818",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "speedybee-m10-gps",
        "category": "gps",
        "name": "M10 GPS + Compass Module",
        "brand": "SpeedyBee",
        "price_php": 1232,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://speedybee.com/search?q=M10+GPS+Compass+Module",
        "color": "#101010",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    # ========== ANTENNA ==========
    {
        "id": "foxeer-lollipop4-rhcp-antenna",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP SMA",
        "brand": "Foxeer",
        "price_php": 504,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://foxeer.com/search?q=Lollipop+4+5.8GHz+RHCP",
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
        "id": "truerc-xair-rhcp-antenna",
        "category": "antenna",
        "name": "X-Air 5.8GHz RHCP SMA",
        "brand": "TrueRC",
        "price_php": 896,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+X-Air+5.8GHz+RHCP",
        "color": "#0d0d0d",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 3.3,
            "type": "patch"
        }
    },
    {
        "id": "rushfpv-cherry-rhcp-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz RHCP SMA",
        "brand": "RushFPV",
        "price_php": 616,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://rushfpv.com/search?q=Cherry+5.8GHz+RHCP",
        "color": "#8b0000",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.1,
            "type": "cloverleaf"
        }
    },
    {
        "id": "hglrc-rhcp-cloverleaf-antenna",
        "category": "antenna",
        "name": "5.8GHz Cloverleaf RHCP MMCX",
        "brand": "HGLRC",
        "price_php": 392,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://hglrc.com/search?q=5.8GHz+Cloverleaf+RHCP+MMCX",
        "color": "#131313",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "MMCX",
            "gain_dbi": 1.8,
            "type": "cloverleaf"
        }
    },
    {
        "id": "lumenier-axii2-rhcp-antenna",
        "category": "antenna",
        "name": "AXII 2 5.8GHz RHCP SMA",
        "brand": "Lumenier",
        "price_php": 728,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://lumenier.com/search?q=AXII+2+5.8GHz+RHCP",
        "color": "#0f0f0f",
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
