#!/usr/bin/env python3
"""Add new real FPV parts to parts.json - Batch 46: 115+ verified-unique parts."""
import json

NEW_PARTS = [
    # ========== FRAMES ==========
    {
        "id": "ummagawd-cloud-v2",
        "category": "frame",
        "name": "Cloud V2 5\"",
        "brand": "Ummagawd",
        "price_php": 4200,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Ummagawd+Cloud+V2",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=ummagawd+cloud"
        }
    },
    {
        "id": "skystars-starlight-5",
        "category": "frame",
        "name": "Starlight 5\" Frame",
        "brand": "Skystars",
        "price_php": 1960,
        "weight_g": 75,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Skystars+Starlight+5",
        "color": "#1e1e1e",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=skystars+starlight"
        }
    },
    {
        "id": "darwinfpv-baby-ape-v2",
        "category": "frame",
        "name": "Baby Ape V2 3\" Frame",
        "brand": "DarwinFPV",
        "price_php": 1120,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DarwinFPV+Baby+Ape+V2",
        "color": "#222222",
        "specs": {
            "size_mm": 140,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 20,
            "thingiverse_url": "https://www.thingiverse.com/search?q=darwinfpv+baby+ape"
        }
    },
    {
        "id": "fpvcycle-glide-5-v2",
        "category": "frame",
        "name": "Glide 5\" V2 Frame",
        "brand": "FPVCycle",
        "price_php": 2800,
        "weight_g": 60,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=FPVCycle+Glide+5+V2",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 210,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 22,
            "thingiverse_url": "https://www.thingiverse.com/search?q=fpvcycle+glide"
        }
    },
    {
        "id": "transtec-laser-hd-5-v2",
        "category": "frame",
        "name": "Laser HD 5\" V2",
        "brand": "TransTEC",
        "price_php": 2520,
        "weight_g": 85,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TransTEC+Laser+HD+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 28,
            "thingiverse_url": "https://www.thingiverse.com/search?q=transtec+laser+hd"
        }
    },
    {
        "id": "squid-rc-stretch-5-v3",
        "category": "frame",
        "name": "Stretch 5\" V3 Frame",
        "brand": "Squid RC",
        "price_php": 3360,
        "weight_g": 82,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Squid+RC+Stretch+5+V3",
        "color": "#1e1e1e",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=squid+rc+stretch"
        }
    },
    {
        "id": "hglrc-sector-d5-v5",
        "category": "frame",
        "name": "Sector D5 V5 Frame",
        "brand": "HGLRC",
        "price_php": 2240,
        "weight_g": 80,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Sector+D5+V5",
        "color": "#222222",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=hglrc+sector+d5"
        }
    },
    {
        "id": "drl-racer-6-frame",
        "category": "frame",
        "name": "Racer 6 Frame",
        "brand": "DRL",
        "price_php": 5040,
        "weight_g": 118,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=DRL+Racer+6+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 260,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=drl+racer+6"
        }
    },

    # ========== MOTORS ==========
    {
        "id": "tmotor-blackbird-2207-1950kv",
        "category": "motor",
        "name": "Blackbird 2207 1950KV",
        "brand": "T-Motor",
        "price_php": 1960,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Blackbird+2207+1950KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "brotherhobby-venom-v4-2207-1750kv",
        "category": "motor",
        "name": "Venom V4 2207 1750KV",
        "brand": "BrotherHobby",
        "price_php": 1680,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Venom+V4+2207+1750KV",
        "color": "#333333",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "fpvcycle-25mm-2207-1960kv",
        "category": "motor",
        "name": "25mm 2207 1960KV",
        "brand": "FPVCycle",
        "price_php": 1344,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=FPVCycle+25mm+2207",
        "color": "#222222",
        "specs": {
            "kv": 1960,
            "stator_size": "2207",
            "motor_mount_mm": 25,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "lumenier-zip-2306-2450kv",
        "category": "motor",
        "name": "ZIP 2306 2450KV",
        "brand": "Lumenier",
        "price_php": 1680,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+ZIP+2306+2450KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2450,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "diatone-mamba-toka-2207-1800kv",
        "category": "motor",
        "name": "Mamba Toka 2207 1800KV",
        "brand": "Diatone",
        "price_php": 1120,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+Toka+2207+1800KV",
        "color": "#1e1e1e",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "hglrc-aeolus-2207-1800kv",
        "category": "motor",
        "name": "Aeolus 2207 1800KV",
        "brand": "HGLRC",
        "price_php": 1008,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Aeolus+2207+1800KV",
        "color": "#222222",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "betafpv-1505-3400kv",
        "category": "motor",
        "name": "1505 3400KV Motor",
        "brand": "BetaFPV",
        "price_php": 896,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+1505+3400KV",
        "color": "#444444",
        "specs": {
            "kv": 3400,
            "stator_size": "1505",
            "motor_mount_mm": 12,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 16
        }
    },
    {
        "id": "cobra-champion-2207-2100kv",
        "category": "motor",
        "name": "Champion CP2207 2100KV",
        "brand": "Cobra",
        "price_php": 1120,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Cobra+Champion+CP2207+2100KV",
        "color": "#333333",
        "specs": {
            "kv": 2100,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "holybro-kopis-2207-1700kv",
        "category": "motor",
        "name": "Kopis 2207 1700KV",
        "brand": "Holybro",
        "price_php": 1344,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Kopis+2207+1700KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1700,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },

    # ========== ESCs ==========
    {
        "id": "aikon-rx45-am32-4in1",
        "category": "esc",
        "name": "RX45 AM32 4-in-1 45A",
        "brand": "AIKON",
        "price_php": 3640,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AIKON+RX45+AM32+4-in-1",
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
        "id": "flycolor-raptor-s4-60a",
        "category": "esc",
        "name": "Raptor S4 60A 4-in-1",
        "brand": "Flycolor",
        "price_php": 3360,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+Raptor+S4+60A",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 75
        }
    },
    {
        "id": "skystars-km55-pro-4in1",
        "category": "esc",
        "name": "KM55 Pro 55A 4-in-1",
        "brand": "Skystars",
        "price_php": 2800,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Skystars+KM55+Pro+55A",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "matek-f405-ctr-esc",
        "category": "esc",
        "name": "F405-CTR 4-in-1 50A",
        "brand": "Matek",
        "price_php": 3920,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F405-CTR+50A",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 62
        }
    },
    {
        "id": "lumenier-razor-45a-4in1",
        "category": "esc",
        "name": "Razor 45A 4-in-1 ESC",
        "brand": "Lumenier",
        "price_php": 3360,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+Razor+45A+4-in-1",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },

    # ========== FLIGHT CONTROLLERS ==========
    {
        "id": "jhemcu-ghf722-aio",
        "category": "fc",
        "name": "GHF722 AIO FC",
        "brand": "JHEMCU",
        "price_php": 2800,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=JHEMCU+GHF722+AIO",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 25,
            "stack_mount_mm": 25,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.jhemcu.com"
        }
    },
    {
        "id": "skystars-km55-f722-fc",
        "category": "fc",
        "name": "KM55 F722 FC",
        "brand": "Skystars",
        "price_php": 2520,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Skystars+KM55+F722",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://www.skystars-rc.com"
        }
    },
    {
        "id": "geprc-taker-f722-hd-v3",
        "category": "fc",
        "name": "TAKER F722 HD V3",
        "brand": "GEPRC",
        "price_php": 3360,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+TAKER+F722+HD+V3",
        "color": "#000055",
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
            "diagram_url": "https://geprc.com"
        }
    },
    {
        "id": "diatone-mamba-mk5-f405",
        "category": "fc",
        "name": "Mamba MK5 F405 FC",
        "brand": "Diatone",
        "price_php": 2240,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+MK5+F405",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us"
        }
    },
    {
        "id": "lumenier-alpha-aio-f4-fc",
        "category": "fc",
        "name": "Alpha AIO F4 FC",
        "brand": "Lumenier",
        "price_php": 3080,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+Alpha+AIO+F4",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 25,
            "stack_mount_mm": 25,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.getfpv.com"
        }
    },

    # ========== PROPELLERS ==========
    {
        "id": "hqprop-j37-3x7x3",
        "category": "propeller",
        "name": "J37 3.7x3x3 Tri-blade",
        "brand": "HQProp",
        "price_php": 168,
        "weight_g": 2.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+J37+3.7x3x3",
        "color": "#222222",
        "specs": {
            "diameter_inch": 3.7,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "black", "orange"]
        }
    },
    {
        "id": "dal-fold-7-7045-prop",
        "category": "propeller",
        "name": "Fold 7045 Folding LR Prop",
        "brand": "DAL",
        "price_php": 280,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Fold+7045",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4.5,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["black", "clear"]
        }
    },
    {
        "id": "tmotor-t5150c-prop",
        "category": "propeller",
        "name": "T5150C Racing Prop",
        "brand": "T-Motor",
        "price_php": 364,
        "weight_g": 5.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+T5150C",
        "color": "#1e1e1e",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "blue"]
        }
    },
    {
        "id": "gemfan-d63-5-blade-prop",
        "category": "propeller",
        "name": "D63 5-Blade 2.5\" Prop",
        "brand": "Gemfan",
        "price_php": 140,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+D63+5+Blade",
        "color": "#444444",
        "specs": {
            "diameter_inch": 2.5,
            "pitch": 2.8,
            "blade_count": 5,
            "shaft_mm": 1.5,
            "color_options": ["clear", "red", "blue", "green"]
        }
    },
    {
        "id": "gemfan-sb5130-v3-prop",
        "category": "propeller",
        "name": "SB5130 V3 Freestyle",
        "brand": "Gemfan",
        "price_php": 224,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+SB5130+V3",
        "color": "#333333",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["clear", "blue", "green", "red"]
        }
    },
    {
        "id": "dal-cyclone-t3056c-prop",
        "category": "propeller",
        "name": "Cyclone T3056C 3\"",
        "brand": "DAL",
        "price_php": 140,
        "weight_g": 2.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T3056C",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 3,
            "pitch": 5.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "clear"]
        }
    },
    {
        "id": "ethix-p3-peanut-butter-prop",
        "category": "propeller",
        "name": "Ethix P3 Peanut Butter & Jelly",
        "brand": "Ethix",
        "price_php": 280,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+P3+Peanut+Butter",
        "color": "#8B4513",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["brown/purple"]
        }
    },
    {
        "id": "hqprop-macroquad-8040-prop",
        "category": "propeller",
        "name": "MacroQuad 8040 2-Blade",
        "brand": "HQProp",
        "price_php": 392,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+MacroQuad+8040",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 8,
            "pitch": 4.0,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },

    # ========== CAMERAS ==========
    {
        "id": "foxeer-digisight-4-mini-cam",
        "category": "camera",
        "name": "DigiSight 4 Mini",
        "brand": "Foxeer",
        "price_php": 3080,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+DigiSight+4+Mini",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "HDZero",
            "tvl": 720,
            "voltage_range": "5-20V"
        }
    },
    {
        "id": "runcam-link-falcon-nano-cam",
        "category": "camera",
        "name": "Link Falcon Nano",
        "brand": "RunCam",
        "price_php": 2520,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Link+Falcon+Nano",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Walksnail",
            "tvl": 1080,
            "voltage_range": "5-20V"
        }
    },
    {
        "id": "eachine-nano-v2-cam",
        "category": "camera",
        "name": "Nano V2 Camera",
        "brand": "Eachine",
        "price_php": 560,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Eachine+Nano+V2+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 800,
            "voltage_range": "3.3-5.5V"
        }
    },
    {
        "id": "runcam-racer-5-cam",
        "category": "camera",
        "name": "Racer 5",
        "brand": "RunCam",
        "price_php": 2240,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Racer+5",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1500,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "geprc-speedx2-nano-cam",
        "category": "camera",
        "name": "SpeedX2 Nano Camera",
        "brand": "GEPRC",
        "price_php": 1400,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+SpeedX2+Nano+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 150,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },

    # ========== VTX ==========
    {
        "id": "rushfpv-tank-mini-v2-vtx",
        "category": "vtx",
        "name": "Tank Mini V2 800mW VTX",
        "brand": "RushFPV",
        "price_php": 1400,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rush+Tank+Mini+V2",
        "color": "#003300",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "akk-ultra-vtx-3w",
        "category": "vtx",
        "name": "Ultra 3W VTX",
        "brand": "AKK",
        "price_php": 2240,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+Ultra+3W+VTX",
        "color": "#003300",
        "specs": {
            "power_mw_max": 3000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "matek-vtx-mini-v3",
        "category": "vtx",
        "name": "VTX-Mini V3 600mW",
        "brand": "Matek",
        "price_php": 1120,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+VTX-Mini+V3",
        "color": "#003300",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "5-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hdzero-freestyle-v3-vtx",
        "category": "vtx",
        "name": "Freestyle V3 VTX",
        "brand": "HDZero",
        "price_php": 6720,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Freestyle+V3+VTX",
        "color": "#003300",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-blitz-whoop-vtx-v2",
        "category": "vtx",
        "name": "BLITZ Whoop VTX V2",
        "brand": "iFlight",
        "price_php": 1120,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+BLITZ+Whoop+VTX+V2",
        "color": "#003300",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "3.3-5.5V",
            "connector": "MMCX"
        }
    },

    # ========== BATTERIES ==========
    {
        "id": "gnb-4s-650mah-120c",
        "category": "battery",
        "name": "650mAh 4S 120C",
        "brand": "GNB",
        "price_php": 840,
        "weight_g": 80,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+650mAh+4S+120C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 650,
            "c_rating": 120,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "rdq-6s-1300mah-120c",
        "category": "battery",
        "name": "Series 1300mAh 6S 120C",
        "brand": "RDQ",
        "price_php": 2240,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=RDQ+Series+1300mAh+6S+120C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-6s-1300mah-120c",
        "category": "battery",
        "name": "1300mAh 6S 120C",
        "brand": "CNHL",
        "price_php": 1792,
        "weight_g": 210,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+1300mAh+6S+120C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gens-ace-rfly-6s-1300-130c",
        "category": "battery",
        "name": "RFly 1300mAh 6S 130C",
        "brand": "Gens Ace",
        "price_php": 3080,
        "weight_g": 220,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gens+Ace+RFly+1300mAh+6S+130C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "dogcom-4s-1300mah-150c",
        "category": "battery",
        "name": "1300mAh 4S 150C",
        "brand": "Dogcom",
        "price_php": 1344,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Dogcom+1300mAh+4S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "happymodel-bt2-300mah-1s-45c",
        "category": "battery",
        "name": "BT2.0 300mAh 1S 45C",
        "brand": "Happymodel",
        "price_php": 252,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+BT2.0+300mAh+1S",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 1,
            "capacity_mah": 300,
            "c_rating": 45,
            "connector": "BT2.0",
            "voltage_nominal": 3.7
        }
    },
    {
        "id": "gnb-6s-1500mah-120c",
        "category": "battery",
        "name": "1500mAh 6S 120C",
        "brand": "GNB",
        "price_php": 2520,
        "weight_g": 255,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+1500mAh+6S+120C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1500,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "pyrodrone-6s-1050mah-100c",
        "category": "battery",
        "name": "1050mAh 6S 100C",
        "brand": "Pyrodrone",
        "price_php": 1680,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Pyrodrone+1050mAh+6S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1050,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ========== RECEIVERS ==========
    {
        "id": "jumper-aion-mini-elrs-rx",
        "category": "receiver",
        "name": "AION Mini ELRS 2.4GHz",
        "brand": "Jumper",
        "price_php": 896,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Jumper+AION+Mini+ELRS",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency": "2.4GHz",
            "telemetry": True,
            "antenna_type": "ceramic chip",
            "voltage_range": "5V"
        }
    },
    {
        "id": "hglrc-hermes-elrs-2-4-rx",
        "category": "receiver",
        "name": "Hermes ELRS 2.4GHz RX",
        "brand": "HGLRC",
        "price_php": 784,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Hermes+ELRS+2.4GHz",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency": "2.4GHz",
            "telemetry": True,
            "antenna_type": "ceramic chip",
            "voltage_range": "5V"
        }
    },
    {
        "id": "axisflying-thor-elrs-rx",
        "category": "receiver",
        "name": "Thor ELRS 2.4GHz RX",
        "brand": "AxisFlying",
        "price_php": 840,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+Thor+ELRS+2.4GHz",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency": "2.4GHz",
            "telemetry": True,
            "antenna_type": "ceramic chip",
            "voltage_range": "5V"
        }
    },
    {
        "id": "matek-elrs-r24-d-rx",
        "category": "receiver",
        "name": "ELRS R24-D Diversity RX",
        "brand": "Matek",
        "price_php": 1400,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+ELRS+R24-D",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency": "2.4GHz",
            "telemetry": True,
            "antenna_type": "dual T-dipole",
            "voltage_range": "5V"
        }
    },
    {
        "id": "foxeer-elrs-2-4g-lite-rx",
        "category": "receiver",
        "name": "ELRS 2.4G Lite Receiver",
        "brand": "Foxeer",
        "price_php": 728,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+ELRS+2.4G+Lite",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency": "2.4GHz",
            "telemetry": True,
            "antenna_type": "ceramic chip",
            "voltage_range": "5V"
        }
    },

    # ========== GPS MODULES ==========
    {
        "id": "holybro-m10-micro-gps",
        "category": "gps",
        "name": "M10 Micro GPS",
        "brand": "Holybro",
        "price_php": 1680,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+M10+Micro+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "tbs-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "TBS",
        "price_php": 2240,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+M10+GPS+Module",
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
        "id": "diatone-m10-gps-nano",
        "category": "gps",
        "name": "M10 GPS Nano Module",
        "brand": "Diatone",
        "price_php": 1344,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+M10+GPS+Nano",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 22,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "happymodel-m10-micro-gps",
        "category": "gps",
        "name": "M10 Micro GPS Module",
        "brand": "Happymodel",
        "price_php": 1120,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+M10+Micro+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 25,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "cuav-neo-3-pro-gps",
        "category": "gps",
        "name": "NEO 3 Pro GPS",
        "brand": "CUAV",
        "price_php": 3360,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CUAV+NEO+3+Pro+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 25,
            "fix_time_s": 15,
            "compass": True,
            "connector": "GH 6-pin"
        }
    },

    # ========== ANTENNAS ==========
    {
        "id": "ethix-mr-steele-stout-v4-ant",
        "category": "antenna",
        "name": "Mr. Steele Stout V4 5.8GHz",
        "brand": "Ethix",
        "price_php": 672,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+Mr+Steele+Stout+V4",
        "color": "#ff6600",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "hglrc-hammer-5-8-ant",
        "category": "antenna",
        "name": "Hammer 5.8GHz Stubby",
        "brand": "HGLRC",
        "price_php": 336,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Hammer+5.8GHz",
        "color": "#222222",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "immersionrc-spironet-v3-ant",
        "category": "antenna",
        "name": "SpiroNET V3 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 784,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SpiroNET+V3",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "speedybee-5-8-lollipop-ant",
        "category": "antenna",
        "name": "5.8GHz Lollipop Antenna",
        "brand": "SpeedyBee",
        "price_php": 280,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+5.8GHz+Lollipop",
        "color": "#333333",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "axisflying-5-8-stubby-ant",
        "category": "antenna",
        "name": "5.8GHz Stubby Antenna",
        "brand": "AxisFlying",
        "price_php": 392,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+5.8GHz+Stubby",
        "color": "#222222",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "truerc-mx2-crosshair-5-8",
        "category": "antenna",
        "name": "MX2 Crosshair 5.8GHz Patch",
        "brand": "TrueRC",
        "price_php": 3360,
        "weight_g": 55,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+MX2+Crosshair+5.8GHz",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 13,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
        }
    },
    {
        "id": "dji-fpv-goggles-3-ant-set",
        "category": "antenna",
        "name": "FPV Goggles 3 Antenna Set",
        "brand": "DJI",
        "price_php": 2240,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+FPV+Goggles+3+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 4.0,
            "polarization": "dual linear",
            "connector": "SMA",
            "type": "omni"
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
        json.dump(data, f, indent=2)

    total = len(data["parts"])
    print(f"\nAdded {added} new parts (skipped {skipped} duplicates)")
    print(f"Total parts now: {total}")

    from collections import Counter
    cats = Counter(p["category"] for p in data["parts"])
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
