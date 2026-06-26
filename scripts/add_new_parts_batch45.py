#!/usr/bin/env python3
"""Add new real FPV parts to parts.json - Batch 45: 150+ new parts across all categories."""
import json

NEW_PARTS = [
    # ========== FRAMES ==========
    {
        "id": "geprc-mark6-hd",
        "category": "frame",
        "name": "Mark6 HD 5\"",
        "brand": "GEPRC",
        "price_php": 3920,
        "weight_g": 110,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Mark6+HD",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark6"
        }
    },
    {
        "id": "iflight-nazgul-evoque-f6d",
        "category": "frame",
        "name": "Nazgul Evoque F6D 6\"",
        "brand": "iFlight",
        "price_php": 4480,
        "weight_g": 135,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Nazgul+Evoque+F6D",
        "color": "#1e1e1e",
        "specs": {
            "size_mm": 265,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=nazgul+evoque+f6"
        }
    },
    {
        "id": "flywoo-explorer-lr4-v2",
        "category": "frame",
        "name": "Explorer LR4 V2 4\"",
        "brand": "Flywoo",
        "price_php": 2240,
        "weight_g": 52,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Explorer+LR4+V2",
        "color": "#222222",
        "specs": {
            "size_mm": 178,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 3.5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "axisflying-manta-3-5",
        "category": "frame",
        "name": "Manta 3.5\" Frame",
        "brand": "AxisFlying",
        "price_php": 2800,
        "weight_g": 48,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+Manta+3.5",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 155,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 3.5,
            "standoff_height_mm": 22,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+manta+3.5"
        }
    },
    {
        "id": "emax-hawk-pro-5-frame",
        "category": "frame",
        "name": "Hawk Pro 5\" Frame",
        "brand": "Emax",
        "price_php": 2520,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Emax+Hawk+Pro+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 210,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 28,
            "thingiverse_url": "https://www.thingiverse.com/search?q=emax+hawk+pro"
        }
    },
    {
        "id": "speedybee-fs225-v3",
        "category": "frame",
        "name": "FS225 V3 5\"",
        "brand": "SpeedyBee",
        "price_php": 1960,
        "weight_g": 82,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+FS225+V3",
        "color": "#1e1e1e",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=speedybee+fs225"
        }
    },
    {
        "id": "tbs-source-two-v2",
        "category": "frame",
        "name": "Source Two V2 5\"",
        "brand": "TBS",
        "price_php": 1680,
        "weight_g": 90,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=TBS+Source+Two+V2",
        "color": "#111111",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+two"
        }
    },
    {
        "id": "hyperlite-floss-3-race",
        "category": "frame",
        "name": "Floss 3.0 Race 5\"",
        "brand": "Hyperlite",
        "price_php": 3640,
        "weight_g": 65,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Hyperlite+Floss+3.0",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 22,
            "thingiverse_url": "https://www.thingiverse.com/search?q=hyperlite+floss+3"
        }
    },
    {
        "id": "lumenier-qav-r2-deadcat",
        "category": "frame",
        "name": "QAV-R2 Deadcat 7\"",
        "brand": "Lumenier",
        "price_php": 5040,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+QAV-R2+Deadcat+7",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 300,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=lumenier+qav-r2+deadcat"
        }
    },
    {
        "id": "newbeedrone-acrobee75-frame",
        "category": "frame",
        "name": "AcroBee75 HD Frame",
        "brand": "NewBeeDrone",
        "price_php": 1120,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=NewBeeDrone+AcroBee75+HD",
        "color": "#333333",
        "specs": {
            "size_mm": 75,
            "motor_mount_mm": 9,
            "prop_clearance_inch": 1.5,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 2.5,
            "standoff_height_mm": 20,
            "thingiverse_url": "https://www.thingiverse.com/search?q=acrobee75"
        }
    },
    {
        "id": "five33-switchback-pro",
        "category": "frame",
        "name": "Switchback Pro 5\"",
        "brand": "Five33",
        "price_php": 4760,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Five33+Switchback+Pro",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=five33+switchback"
        }
    },
    {
        "id": "happymodel-crux35-v2-frame",
        "category": "frame",
        "name": "Crux35 V2 3.5\" Frame",
        "brand": "Happymodel",
        "price_php": 1400,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+Crux35+V2",
        "color": "#222222",
        "specs": {
            "size_mm": 150,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 20,
            "thingiverse_url": "https://www.thingiverse.com/search?q=happymodel+crux35"
        }
    },
    {
        "id": "catalyst-chameleon-ti-7",
        "category": "frame",
        "name": "Chameleon Ti 7\" LR",
        "brand": "Catalyst Machineworks",
        "price_php": 6720,
        "weight_g": 155,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Catalyst+Machineworks+Chameleon+Ti+7",
        "color": "#2a2a2a",
        "specs": {
            "size_mm": 310,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=catalyst+chameleon+ti"
        }
    },
    {
        "id": "geprc-cinelog35-v2-frame",
        "category": "frame",
        "name": "CineLog35 V2 3.5\" Frame",
        "brand": "GEPRC",
        "price_php": 2240,
        "weight_g": 42,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+CineLog35+V2",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 155,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 3.5,
            "standoff_height_mm": 22,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+cinelog35"
        }
    },
    {
        "id": "armattan-badger-6",
        "category": "frame",
        "name": "Badger 6\" DJI Frame",
        "brand": "Armattan",
        "price_php": 5600,
        "weight_g": 120,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Armattan+Badger+6",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 260,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+badger"
        }
    },

    # ========== MOTORS ==========
    {
        "id": "tmotor-velox-v3-2207-1750kv",
        "category": "motor",
        "name": "Velox V3 2207 1750KV",
        "brand": "T-Motor",
        "price_php": 1680,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Velox+V3+2207+1750KV",
        "color": "#333333",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "tmotor-velox-v3-2207-2550kv",
        "category": "motor",
        "name": "Velox V3 2207 2550KV",
        "brand": "T-Motor",
        "price_php": 1680,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Velox+V3+2207+2550KV",
        "color": "#333333",
        "specs": {
            "kv": 2550,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "brotherhobby-avenger-2812-900kv",
        "category": "motor",
        "name": "Avenger 2812 900KV",
        "brand": "BrotherHobby",
        "price_php": 1960,
        "weight_g": 45,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2812+900KV",
        "color": "#444444",
        "specs": {
            "kv": 900,
            "stator_size": "2812",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 35
        }
    },
    {
        "id": "emax-eco-iii-2207-1900kv",
        "category": "motor",
        "name": "ECO III 2207 1900KV",
        "brand": "EMAX",
        "price_php": 896,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=EMAX+ECO+III+2207+1900KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "emax-eco-iii-2306-2400kv",
        "category": "motor",
        "name": "ECO III 2306 2400KV",
        "brand": "EMAX",
        "price_php": 896,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=EMAX+ECO+III+2306+2400KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2400,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "foxeer-wraith-2207-1850kv",
        "category": "motor",
        "name": "Wraith 2207 1850KV",
        "brand": "Foxeer",
        "price_php": 1120,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Wraith+2207+1850KV",
        "color": "#222222",
        "specs": {
            "kv": 1850,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "geprc-speedx2-2207-2150kv",
        "category": "motor",
        "name": "SpeedX2 2207 2150KV",
        "brand": "GEPRC",
        "price_php": 1344,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+SpeedX2+2207+2150KV",
        "color": "#1e1e1e",
        "specs": {
            "kv": 2150,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "sub250-1404-4600kv",
        "category": "motor",
        "name": "1404 4600KV Motor",
        "brand": "Sub250",
        "price_php": 784,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Sub250+1404+4600KV",
        "color": "#555555",
        "specs": {
            "kv": 4600,
            "stator_size": "1404",
            "motor_mount_mm": 12,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 15
        }
    },
    {
        "id": "flywoo-nin-v2-2207-1750kv",
        "category": "motor",
        "name": "NIN V2 2207 1750KV",
        "brand": "Flywoo",
        "price_php": 1400,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+NIN+V2+2207+1750KV",
        "color": "#2a2a2a",
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
        "id": "rcinpower-gts-v3-2207-1860kv",
        "category": "motor",
        "name": "GTS V3 2207 1860KV",
        "brand": "RCINPower",
        "price_php": 1568,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=RCINPower+GTS+V3+2207",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1860,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "xnova-freestyle-smooth-2207-1800kv",
        "category": "motor",
        "name": "Freestyle Smooth 2207 1800KV",
        "brand": "XNOVA",
        "price_php": 2240,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=XNOVA+Freestyle+Smooth+2207+1800KV",
        "color": "#333333",
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
        "id": "happymodel-ex1404-3500kv",
        "category": "motor",
        "name": "EX1404 3500KV",
        "brand": "Happymodel",
        "price_php": 672,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+EX1404+3500KV",
        "color": "#444444",
        "specs": {
            "kv": 3500,
            "stator_size": "1404",
            "motor_mount_mm": 12,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 12
        }
    },
    {
        "id": "speedybee-bee35-1404-3850kv",
        "category": "motor",
        "name": "Bee35 1404 3850KV",
        "brand": "SpeedyBee",
        "price_php": 728,
        "weight_g": 8.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+Bee35+1404+3850KV",
        "color": "#222222",
        "specs": {
            "kv": 3850,
            "stator_size": "1404",
            "motor_mount_mm": 12,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 14
        }
    },
    {
        "id": "lumenier-zip-2207-2050kv",
        "category": "motor",
        "name": "ZIP 2207 2050KV",
        "brand": "Lumenier",
        "price_php": 1568,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+ZIP+2207+2050KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2050,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "axisflying-2807-1300kv",
        "category": "motor",
        "name": "C2807 1300KV LR Motor",
        "brand": "AxisFlying",
        "price_php": 1792,
        "weight_g": 40,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+2807+1300KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 32
        }
    },

    # ========== ESCs ==========
    {
        "id": "speedybee-bl32-55a-4in1",
        "category": "esc",
        "name": "BL32 55A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 3360,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+BL32+55A+4-in-1",
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
        "id": "foxeer-reaper-f4-65a",
        "category": "esc",
        "name": "Reaper F4 65A 4-in-1",
        "brand": "Foxeer",
        "price_php": 4200,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Reaper+F4+65A",
        "color": "#002200",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 8,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 80
        }
    },
    {
        "id": "geprc-taker-g4-50a",
        "category": "esc",
        "name": "TAKER G4 50A 4-in-1",
        "brand": "GEPRC",
        "price_php": 3080,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+TAKER+G4+50A",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "flywoo-goku-gn745-40a",
        "category": "esc",
        "name": "Goku GN745 40A 4-in-1",
        "brand": "Flywoo",
        "price_php": 2800,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Goku+GN745+40A",
        "color": "#002200",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 50
        }
    },
    {
        "id": "tmotor-f45a-pro-v2",
        "category": "esc",
        "name": "F45A PRO V2 4-in-1",
        "brand": "T-Motor",
        "price_php": 3920,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F45A+PRO+V2+4-in-1",
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
        "id": "iflight-blitz-e80-4in1",
        "category": "esc",
        "name": "BLITZ E80 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 5040,
        "weight_g": 35,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+BLITZ+E80+4-in-1",
        "color": "#002200",
        "specs": {
            "amp_rating": 80,
            "input_voltage_s": 8,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 100
        }
    },
    {
        "id": "aikon-ak32-pro-35a",
        "category": "esc",
        "name": "AK32 Pro 35A 4-in-1",
        "brand": "AIKON",
        "price_php": 2800,
        "weight_g": 20,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AIKON+AK32+Pro+35A",
        "color": "#002200",
        "specs": {
            "amp_rating": 35,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 45
        }
    },
    {
        "id": "betafpv-toothpick-f4-2s-12a",
        "category": "esc",
        "name": "Toothpick F4 2S 12A AIO",
        "brand": "BetaFPV",
        "price_php": 2240,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+Toothpick+F4+2S+12A",
        "color": "#002200",
        "specs": {
            "amp_rating": 12,
            "input_voltage_s": 2,
            "protocol": "DSHOT600",
            "form_factor_mm": 25,
            "burst_amp": 15
        }
    },
    {
        "id": "holybro-tekko32-f4-4in1-65a",
        "category": "esc",
        "name": "Tekko32 F4 65A 4-in-1",
        "brand": "Holybro",
        "price_php": 4480,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Tekko32+F4+65A",
        "color": "#002200",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 80
        }
    },
    {
        "id": "hglrc-zeus-f4-60a",
        "category": "esc",
        "name": "Zeus F4 60A 4-in-1",
        "brand": "HGLRC",
        "price_php": 3640,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Zeus+F4+60A",
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
        "id": "diatone-mamba-f50-pro",
        "category": "esc",
        "name": "Mamba F50 Pro 4-in-1",
        "brand": "Diatone",
        "price_php": 3360,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F50+Pro",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "happymodel-x12-aio-5a",
        "category": "esc",
        "name": "X12 AIO 5A 1S ESC",
        "brand": "Happymodel",
        "price_php": 1120,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+X12+AIO+5A",
        "color": "#002200",
        "specs": {
            "amp_rating": 5,
            "input_voltage_s": 1,
            "protocol": "DSHOT600",
            "form_factor_mm": 16,
            "burst_amp": 6
        }
    },
    {
        "id": "axisflying-argus-pro-55a",
        "category": "esc",
        "name": "Argus Pro 55A 4-in-1",
        "brand": "AxisFlying",
        "price_php": 3640,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+Argus+Pro+55A",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 68
        }
    },

    # ========== FLIGHT CONTROLLERS ==========
    {
        "id": "speedybee-f405-v4-fc",
        "category": "fc",
        "name": "F405 V4 FC",
        "brand": "SpeedyBee",
        "price_php": 2240,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+F405+V4",
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
            "diagram_url": "https://www.speedybee.com/speedybee-f405-v4-bls-55a-30x30-fc-esc-stack/"
        }
    },
    {
        "id": "geprc-taker-f405-hd-v2",
        "category": "fc",
        "name": "TAKER F405 HD V2",
        "brand": "GEPRC",
        "price_php": 2520,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+TAKER+F405+HD+V2",
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
            "diagram_url": "https://geprc.com/product/gep-taker-f405-hd-v2/"
        }
    },
    {
        "id": "foxeer-f722-v4-fc",
        "category": "fc",
        "name": "F722 V4 FC",
        "brand": "Foxeer",
        "price_php": 3080,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+F722+V4",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://www.foxeer.com"
        }
    },
    {
        "id": "flywoo-goku-f405-hd",
        "category": "fc",
        "name": "Goku F405 HD FC",
        "brand": "Flywoo",
        "price_php": 2520,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Goku+F405+HD",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://flywoo.net"
        }
    },
    {
        "id": "holybro-kakute-f7-v2-hd",
        "category": "fc",
        "name": "Kakute F7 V2 HD",
        "brand": "Holybro",
        "price_php": 3920,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Kakute+F7+V2+HD",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 4,
            "curr_sensor": True,
            "diagram_url": "https://holybro.com/products/kakute-f7-v2"
        }
    },
    {
        "id": "iflight-blitz-f722-v2",
        "category": "fc",
        "name": "BLITZ F722 V2 FC",
        "brand": "iFlight",
        "price_php": 3640,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+BLITZ+F722+V2",
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
            "diagram_url": "https://shop.iflight.com"
        }
    },
    {
        "id": "axisflying-argus-f722-fc",
        "category": "fc",
        "name": "Argus F722 FC",
        "brand": "AxisFlying",
        "price_php": 3360,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+Argus+F722",
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
            "diagram_url": "https://www.axisflying.com"
        }
    },
    {
        "id": "happymodel-crazybee-x-v2",
        "category": "fc",
        "name": "CrazyBee X V2 AIO FC",
        "brand": "Happymodel",
        "price_php": 1960,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+CrazyBee+X+V2",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 25,
            "stack_mount_mm": 25,
            "barometer": False,
            "blackbox": True,
            "uart_count": 3,
            "5v_pad_count": 1,
            "curr_sensor": True,
            "diagram_url": "https://www.happymodel.cn"
        }
    },
    {
        "id": "tmotor-f7-hd-fc",
        "category": "fc",
        "name": "F7 HD Flight Controller",
        "brand": "T-Motor",
        "price_php": 4480,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F7+HD+Flight+Controller",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 4,
            "curr_sensor": True,
            "diagram_url": "https://store.tmotor.com"
        }
    },
    {
        "id": "hglrc-zeus-f722-v2",
        "category": "fc",
        "name": "Zeus F722 V2 FC",
        "brand": "HGLRC",
        "price_php": 2800,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Zeus+F722+V2",
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
            "diagram_url": "https://www.hglrc.com"
        }
    },
    {
        "id": "betafpv-f722-35a-aio-v4",
        "category": "fc",
        "name": "F722 35A AIO V4",
        "brand": "BetaFPV",
        "price_php": 3640,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+F722+35A+AIO+V4",
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
            "diagram_url": "https://betafpv.com"
        }
    },
    {
        "id": "matek-f722-wing-v3",
        "category": "fc",
        "name": "F722-Wing V3 FC",
        "brand": "Matek",
        "price_php": 3920,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F722-Wing+V3",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "INAV",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 4,
            "curr_sensor": True,
            "diagram_url": "https://www.mateksys.com/?portfolio=f722-wing-v3"
        }
    },

    # ========== PROPELLERS ==========
    {
        "id": "gemfan-hurricane-51466-v2",
        "category": "propeller",
        "name": "Hurricane 51466 V2",
        "brand": "Gemfan",
        "price_php": 224,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466+V2",
        "color": "#222222",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.66,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["clear", "blue", "green", "red", "black"]
        }
    },
    {
        "id": "hqprop-ethix-p4-candy-cane",
        "category": "propeller",
        "name": "Ethix P4 Candy Cane 5.1x3x3",
        "brand": "HQProp",
        "price_php": 280,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+P4+Candy+Cane",
        "color": "#ff3333",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["red/white"]
        }
    },
    {
        "id": "gemfan-vannystyle-5136-3",
        "category": "propeller",
        "name": "Vannystyle 5136-3",
        "brand": "Gemfan",
        "price_php": 252,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Vannystyle+5136",
        "color": "#333333",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["clear grey", "clear blue", "clear red"]
        }
    },
    {
        "id": "hqprop-dp5x4-5x3-v1s",
        "category": "propeller",
        "name": "DP5X4.5X3 V1S",
        "brand": "HQProp",
        "price_php": 196,
        "weight_g": 5.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP5X4.5X3+V1S",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "orange", "green"]
        }
    },
    {
        "id": "emax-avan-rush-2-5-tri",
        "category": "propeller",
        "name": "Avan Rush 2.5\" Tri-blade",
        "brand": "EMAX",
        "price_php": 168,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=EMAX+Avan+Rush+2.5+Tri-blade",
        "color": "#444444",
        "specs": {
            "diameter_inch": 2.5,
            "pitch": 1.9,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["clear", "red", "blue"]
        }
    },
    {
        "id": "dal-cyclone-t5047c-v3",
        "category": "propeller",
        "name": "Cyclone T5047C V3",
        "brand": "DAL",
        "price_php": 168,
        "weight_g": 5.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T5047C",
        "color": "#1e1e1e",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "orange", "green", "red"]
        }
    },
    {
        "id": "gemfan-freestyle-4s-f4s-5130",
        "category": "propeller",
        "name": "Freestyle F4S 5130-3",
        "brand": "Gemfan",
        "price_php": 224,
        "weight_g": 5.0,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+F4S+5130",
        "color": "#333333",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["clear", "blue", "red"]
        }
    },
    {
        "id": "tmotor-t5147-racing",
        "category": "propeller",
        "name": "T5147 Racing Prop",
        "brand": "T-Motor",
        "price_php": 336,
        "weight_g": 5.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+T5147+Racing",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "blue", "orange"]
        }
    },
    {
        "id": "gemfan-3520-toothpick",
        "category": "propeller",
        "name": "3520 Toothpick Prop",
        "brand": "Gemfan",
        "price_php": 140,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+3520+Toothpick",
        "color": "#444444",
        "specs": {
            "diameter_inch": 3.5,
            "pitch": 2.0,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["clear", "red", "blue", "green"]
        }
    },
    {
        "id": "hqprop-4x3x3-v1s",
        "category": "propeller",
        "name": "4x3x3 V1S Quad-blade",
        "brand": "HQProp",
        "price_php": 196,
        "weight_g": 3.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+4x3x3+V1S",
        "color": "#222222",
        "specs": {
            "diameter_inch": 4,
            "pitch": 3,
            "blade_count": 4,
            "shaft_mm": 5,
            "color_options": ["black", "orange"]
        }
    },
    {
        "id": "gemfan-hurricane-7035-2",
        "category": "propeller",
        "name": "Hurricane 7035-2 LR",
        "brand": "Gemfan",
        "price_php": 308,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+7035",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 7,
            "pitch": 3.5,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["clear", "black"]
        }
    },
    {
        "id": "hqprop-r35-3-5x3-tri",
        "category": "propeller",
        "name": "R35 3.5x3 Tri-blade",
        "brand": "HQProp",
        "price_php": 168,
        "weight_g": 2.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+R35+3.5x3",
        "color": "#333333",
        "specs": {
            "diameter_inch": 3.5,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "orange", "red"]
        }
    },

    # ========== CAMERAS ==========
    {
        "id": "caddx-ratel-pro-v4",
        "category": "camera",
        "name": "Ratel Pro V4",
        "brand": "Caddx",
        "price_php": 1960,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ratel+Pro+V4",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1500,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-predator-v6-nano",
        "category": "camera",
        "name": "Predator V6 Nano",
        "brand": "Foxeer",
        "price_php": 1680,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Predator+V6+Nano",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1300,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-phoenix-3",
        "category": "camera",
        "name": "Phoenix 3",
        "brand": "RunCam",
        "price_php": 2240,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Phoenix+3",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1500,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "walksnail-avatar-hd-mini-v3",
        "category": "camera",
        "name": "Avatar HD Mini V3",
        "brand": "Walksnail",
        "price_php": 4480,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+HD+Mini+V3",
        "color": "#222",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Walksnail",
            "tvl": 1080,
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "hdzero-nano-v3-cam",
        "category": "camera",
        "name": "Nano V3 Camera",
        "brand": "HDZero",
        "price_php": 2800,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Nano+V3+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "HDZero",
            "tvl": 720,
            "voltage_range": "5-16V"
        }
    },
    {
        "id": "dji-o4-air-unit-cam",
        "category": "camera",
        "name": "O4 Air Unit Camera",
        "brand": "DJI",
        "price_php": 7840,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+O4+Air+Unit+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.7\" CMOS",
            "fov_deg": 155,
            "format": "DJI O3",
            "tvl": 1080,
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "caddx-nebula-pro-vista-v2",
        "category": "camera",
        "name": "Nebula Pro Vista V2",
        "brand": "Caddx",
        "price_php": 4200,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Nebula+Pro+Vista+V2",
        "color": "#222",
        "specs": {
            "sensor": "1/2.7\" CMOS",
            "fov_deg": 150,
            "format": "DJI O3",
            "tvl": 1080,
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "foxeer-apollo-digital-cam",
        "category": "camera",
        "name": "Apollo Digital Camera",
        "brand": "Foxeer",
        "price_php": 2520,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Apollo+Digital+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "HDZero",
            "tvl": 720,
            "voltage_range": "5-16V"
        }
    },
    {
        "id": "runcam-wasp-link-digital",
        "category": "camera",
        "name": "Wasp Link Digital",
        "brand": "RunCam",
        "price_php": 3360,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Wasp+Link+Digital",
        "color": "#222",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Walksnail",
            "tvl": 1080,
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "betafpv-smo-4k-cam",
        "category": "camera",
        "name": "SMO 4K Camera",
        "brand": "BetaFPV",
        "price_php": 5600,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+SMO+4K+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/2.3\" CMOS",
            "fov_deg": 150,
            "format": "DJI O3",
            "tvl": 2160,
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "hdzero-micro-v3-cam",
        "category": "camera",
        "name": "Micro V3 Camera",
        "brand": "HDZero",
        "price_php": 3080,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Micro+V3+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "HDZero",
            "tvl": 720,
            "voltage_range": "5-16V"
        }
    },

    # ========== VTX ==========
    {
        "id": "rushfpv-max-solo-v2",
        "category": "vtx",
        "name": "MAX Solo V2 2.5W",
        "brand": "RushFPV",
        "price_php": 2520,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rush+MAX+Solo+V2",
        "color": "#003300",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "walksnail-avatar-hd-pro-kit-v2",
        "category": "vtx",
        "name": "Avatar HD Pro Kit V2",
        "brand": "Walksnail",
        "price_php": 11200,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+HD+Pro+Kit+V2",
        "color": "#003300",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hdzero-race-v4",
        "category": "vtx",
        "name": "Race V4 VTX",
        "brand": "HDZero",
        "price_php": 5040,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Race+V4+VTX",
        "color": "#003300",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "foxeer-reaper-extreme-vtx",
        "category": "vtx",
        "name": "Reaper Extreme VTX 2.5W",
        "brand": "Foxeer",
        "price_php": 2240,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Reaper+Extreme+VTX",
        "color": "#003300",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-36V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tbs-unify-pro32-nano-v2",
        "category": "vtx",
        "name": "Unify Pro32 Nano V2",
        "brand": "TBS",
        "price_php": 2520,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro32+Nano+V2",
        "color": "#003300",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "dji-o3-air-unit-v2",
        "category": "vtx",
        "name": "O3 Air Unit V2",
        "brand": "DJI",
        "price_php": 11760,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+O3+Air+Unit+V2",
        "color": "#003300",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "3-pin"
        }
    },
    {
        "id": "geprc-rav-vtx-1-6w",
        "category": "vtx",
        "name": "RAV VTX 1.6W",
        "brand": "GEPRC",
        "price_php": 1960,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+RAV+VTX+1.6W",
        "color": "#003300",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-zeus-nano-pro-vtx",
        "category": "vtx",
        "name": "Zeus Nano Pro VTX 800mW",
        "brand": "HGLRC",
        "price_php": 1400,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Zeus+Nano+Pro+VTX",
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
        "id": "walksnail-avatar-mini-1s-vtx",
        "category": "vtx",
        "name": "Avatar Mini 1S VTX",
        "brand": "Walksnail",
        "price_php": 5600,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+Mini+1S",
        "color": "#003300",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "3.3-5.5V",
            "connector": "MMCX"
        }
    },
    {
        "id": "speedybee-tx800-vtx",
        "category": "vtx",
        "name": "TX800 VTX 800mW",
        "brand": "SpeedyBee",
        "price_php": 1120,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+TX800+VTX",
        "color": "#003300",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "betafpv-micro-vtx-a03",
        "category": "vtx",
        "name": "Micro VTX A03 400mW",
        "brand": "BetaFPV",
        "price_php": 896,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+Micro+VTX+A03",
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
        "id": "cnhl-6s-1100mah-120c",
        "category": "battery",
        "name": "1100mAh 6S 120C",
        "brand": "CNHL",
        "price_php": 1568,
        "weight_g": 185,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=CNHL+1100mAh+6S+120C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gnb-6s-1100mah-150c",
        "category": "battery",
        "name": "1100mAh 6S 150C",
        "brand": "GNB",
        "price_php": 1960,
        "weight_g": 190,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+1100mAh+6S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-rline-v5-6s-1400",
        "category": "battery",
        "name": "R-Line V5 6S 1400mAh 150C",
        "brand": "Tattu",
        "price_php": 3360,
        "weight_g": 235,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5+6S+1400mAh",
        "color": "#004400",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "ovonic-4s-1550mah-120c",
        "category": "battery",
        "name": "1550mAh 4S 120C",
        "brand": "Ovonic",
        "price_php": 1120,
        "weight_g": 180,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ovonic+1550mAh+4S+120C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1550,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gnb-4s-650mah-100c",
        "category": "battery",
        "name": "650mAh 4S 100C",
        "brand": "GNB",
        "price_php": 784,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+650mAh+4S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 650,
            "c_rating": 100,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "cnhl-4s-850mah-100c",
        "category": "battery",
        "name": "850mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 672,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+850mAh+4S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 850,
            "c_rating": 100,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-4s-850mah-75c",
        "category": "battery",
        "name": "850mAh 4S 75C",
        "brand": "Tattu",
        "price_php": 896,
        "weight_g": 102,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+850mAh+4S+75C",
        "color": "#004400",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 850,
            "c_rating": 75,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "rdq-6s-1050mah-100c",
        "category": "battery",
        "name": "Series 1050mAh 6S 100C",
        "brand": "RDQ",
        "price_php": 1680,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=RDQ+Series+1050mAh+6S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1050,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "lumenier-6s-1300mah-120c",
        "category": "battery",
        "name": "1300mAh 6S 120C",
        "brand": "Lumenier",
        "price_php": 2800,
        "weight_g": 210,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+1300mAh+6S+120C",
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
        "id": "betafpv-bt2-450mah-1s-90c",
        "category": "battery",
        "name": "BT2.0 450mAh 1S 90C",
        "brand": "BetaFPV",
        "price_php": 336,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+BT2.0+450mAh+1S",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 1,
            "capacity_mah": 450,
            "c_rating": 90,
            "connector": "BT2.0",
            "voltage_nominal": 3.7
        }
    },
    {
        "id": "fullsend-6s-1300mah-140c",
        "category": "battery",
        "name": "1300mAh 6S 140C",
        "brand": "FullSend",
        "price_php": 2240,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=FullSend+1300mAh+6S+140C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 140,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gnb-2s-520mah-75c",
        "category": "battery",
        "name": "520mAh 2S 75C",
        "brand": "GNB",
        "price_php": 448,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+520mAh+2S+75C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 2,
            "capacity_mah": 520,
            "c_rating": 75,
            "connector": "XT30",
            "voltage_nominal": 7.4
        }
    },

    # ========== RECEIVERS ==========
    {
        "id": "radiomaster-rp4td-elrs",
        "category": "receiver",
        "name": "RP4TD ELRS 2.4GHz",
        "brand": "Radiomaster",
        "price_php": 1680,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Radiomaster+RP4TD+ELRS",
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
        "id": "happymodel-ep1-elrs-rx",
        "category": "receiver",
        "name": "EP1 ELRS 2.4GHz Nano",
        "brand": "Happymodel",
        "price_php": 784,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+EP1+ELRS+2.4GHz",
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
        "id": "betafpv-superp-14-elrs",
        "category": "receiver",
        "name": "SuperP 14 ELRS 2.4GHz",
        "brand": "BetaFPV",
        "price_php": 1120,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+SuperP+14+ELRS",
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
        "id": "tbs-crossfire-nano-se-rx",
        "category": "receiver",
        "name": "Crossfire Nano SE RX",
        "brand": "TBS",
        "price_php": 1680,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+SE",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency": "868/915MHz",
            "telemetry": True,
            "antenna_type": "T-dipole",
            "voltage_range": "5V"
        }
    },
    {
        "id": "radiomaster-rp3-elrs-900",
        "category": "receiver",
        "name": "RP3 ELRS 900MHz",
        "brand": "Radiomaster",
        "price_php": 1400,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Radiomaster+RP3+ELRS+900MHz",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency": "900MHz",
            "telemetry": True,
            "antenna_type": "T-dipole",
            "voltage_range": "5V"
        }
    },
    {
        "id": "speedybee-rx-mini-elrs",
        "category": "receiver",
        "name": "RX Mini ELRS 2.4GHz",
        "brand": "SpeedyBee",
        "price_php": 896,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+RX+Mini+ELRS",
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
        "id": "iflight-elrs-2-4g-rx-nano",
        "category": "receiver",
        "name": "ELRS 2.4G Nano Receiver",
        "brand": "iFlight",
        "price_php": 896,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+ELRS+2.4G+Nano+Receiver",
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
        "id": "frsky-r-xsr-pro",
        "category": "receiver",
        "name": "R-XSR Pro ACCESS",
        "brand": "FrSky",
        "price_php": 1960,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R-XSR+Pro+ACCESS",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "SBus",
            "frequency": "2.4GHz",
            "telemetry": True,
            "antenna_type": "IPEX",
            "voltage_range": "3.5-10V"
        }
    },
    {
        "id": "geprc-elrs-nano-rx-v2",
        "category": "receiver",
        "name": "ELRS Nano RX V2 2.4GHz",
        "brand": "GEPRC",
        "price_php": 840,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+ELRS+Nano+RX+V2",
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
        "id": "flywoo-elrs-lr-rx-868",
        "category": "receiver",
        "name": "ELRS LR RX 868MHz",
        "brand": "Flywoo",
        "price_php": 1400,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+ELRS+LR+868MHz",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "CRSF",
            "frequency": "868MHz",
            "telemetry": True,
            "antenna_type": "T-dipole",
            "voltage_range": "5V"
        }
    },

    # ========== GPS MODULES ==========
    {
        "id": "speedybee-sp-165-gps",
        "category": "gps",
        "name": "SP-165 M10 GPS",
        "brand": "SpeedyBee",
        "price_php": 1400,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+SP-165+GPS",
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
        "id": "geprc-gep-m10-nano-gps",
        "category": "gps",
        "name": "GEP-M10 Nano GPS",
        "brand": "GEPRC",
        "price_php": 1680,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+GEP-M10+Nano+GPS",
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
        "id": "flywoo-goku-gm10-nano-gps",
        "category": "gps",
        "name": "Goku GM10 Nano V3 GPS",
        "brand": "Flywoo",
        "price_php": 1568,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Goku+GM10+Nano",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "betafpv-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "BetaFPV",
        "price_php": 1344,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+M10+GPS+Module",
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
        "id": "iflight-m10-gps-v2",
        "category": "gps",
        "name": "M10 GPS Module V2",
        "brand": "iFlight",
        "price_php": 1512,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+M10+GPS+V2",
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
        "id": "hglrc-m100-gps",
        "category": "gps",
        "name": "M100 GPS Module",
        "brand": "HGLRC",
        "price_php": 1400,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+M100+GPS",
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
        "id": "axisflying-m10-mini-gps",
        "category": "gps",
        "name": "M10 Mini GPS",
        "brand": "AxisFlying",
        "price_php": 1456,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AxisFlying+M10+Mini+GPS",
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
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1792,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-5883+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "foxeer-m10q-250-gps",
        "category": "gps",
        "name": "M10Q-250 GPS Module",
        "brand": "Foxeer",
        "price_php": 1568,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+M10Q-250+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },

    # ========== ANTENNAS ==========
    {
        "id": "truerc-singularity-5-8-v2",
        "category": "antenna",
        "name": "Singularity 5.8GHz V2 RHCP",
        "brand": "TrueRC",
        "price_php": 1120,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Singularity+5.8+V2",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "foxeer-lollipop-4-plus-5-8",
        "category": "antenna",
        "name": "Lollipop 4+ 5.8GHz",
        "brand": "Foxeer",
        "price_php": 560,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Lollipop+4+Plus+5.8GHz",
        "color": "#ff0000",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "rushfpv-cherry-ultra-antenna",
        "category": "antenna",
        "name": "Cherry Ultra 5.8GHz",
        "brand": "RushFPV",
        "price_php": 672,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rush+Cherry+Ultra+5.8GHz",
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
        "id": "lumenier-axii-hd-v2-5-8",
        "category": "antenna",
        "name": "AXII HD V2 5.8GHz",
        "brand": "Lumenier",
        "price_php": 1400,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+AXII+HD+V2+5.8GHz",
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
        "id": "truerc-x2-air-5-8-patch",
        "category": "antenna",
        "name": "X2 Air 5.8GHz Patch",
        "brand": "TrueRC",
        "price_php": 2240,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+X2+Air+5.8GHz+Patch",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 10,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
        }
    },
    {
        "id": "geprc-momoda-5-8-stubby",
        "category": "antenna",
        "name": "Momoda 5.8GHz Stubby",
        "brand": "GEPRC",
        "price_php": 392,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Momoda+5.8GHz+Stubby",
        "color": "#333333",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "betafpv-air-5-8-antenna",
        "category": "antenna",
        "name": "Air 5.8GHz Antenna",
        "brand": "BetaFPV",
        "price_php": 336,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+Air+5.8GHz+Antenna",
        "color": "#444444",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "hdzero-whoop-antenna-set",
        "category": "antenna",
        "name": "Whoop Antenna Set 5.8GHz",
        "brand": "HDZero",
        "price_php": 560,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Whoop+Antenna+Set",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.5,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "walksnail-avatar-stubby-antenna",
        "category": "antenna",
        "name": "Avatar Stubby 5.8GHz",
        "brand": "Walksnail",
        "price_php": 784,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+Stubby+Antenna",
        "color": "#222222",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "vas-crosshair-xtreme-5-8",
        "category": "antenna",
        "name": "Crosshair Xtreme 5.8GHz",
        "brand": "VAS",
        "price_php": 2800,
        "weight_g": 40,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=VAS+Crosshair+Xtreme+5.8GHz",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 12,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
        }
    },
    {
        "id": "iflight-sigma-5-8-lollipop",
        "category": "antenna",
        "name": "Sigma 5.8GHz Lollipop",
        "brand": "iFlight",
        "price_php": 392,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Sigma+5.8GHz+Lollipop",
        "color": "#1e1e1e",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "menace-rc-invader-5-8",
        "category": "antenna",
        "name": "Invader 5.8GHz Patch",
        "brand": "Menace RC",
        "price_php": 1960,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Menace+RC+Invader+5.8GHz",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 9.4,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
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
