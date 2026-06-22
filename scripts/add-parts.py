#!/usr/bin/env python3
"""Add new real FPV parts to parts.json with accurate specs and pricing."""
import json

NEW_PARTS = [
    # ========== FRAMES ==========
    {
        "id": "ummagawd-moongoat-v2",
        "category": "frame",
        "name": "Moongoat V2 5\"",
        "brand": "Ummagawd",
        "price_php": 4480,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Ummagawd+Moongoat+V2",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=moongoat"
        }
    },
    {
        "id": "flyfishrc-volador-vx5-v2",
        "category": "frame",
        "name": "Volador VX5 V2",
        "brand": "FlyFishRC",
        "price_php": 3360,
        "weight_g": 86,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FlyFishRC+Volador+VX5+V2",
        "color": "#222222",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=volador+vx5"
        }
    },
    {
        "id": "vannystyle-pro-5",
        "category": "frame",
        "name": "Vannystyle Pro 5\"",
        "brand": "Vannystyle",
        "price_php": 3920,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Vannystyle+Pro+5",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=vannystyle+pro"
        }
    },
    {
        "id": "detroit-multirotor-apex-5",
        "category": "frame",
        "name": "Apex 5\" Frame",
        "brand": "Detroit Multirotor",
        "price_php": 4200,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Detroit+Multirotor+Apex+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=detroit+multirotor+apex"
        }
    },
    {
        "id": "xhover-stingy-v2",
        "category": "frame",
        "name": "Stingy V2 5\"",
        "brand": "XHover",
        "price_php": 3080,
        "weight_g": 75,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=XHover+Stingy+V2",
        "color": "#1e1e1e",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=xhover+stingy"
        }
    },
    {
        "id": "shen-drones-thicc-5",
        "category": "frame",
        "name": "Thicc 5\" Frame",
        "brand": "Shen Drones",
        "price_php": 3640,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Shen+Drones+Thicc",
        "color": "#1d1d1d",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=shen+drones+thicc"
        }
    },
    {
        "id": "fpvcycle-glide-5",
        "category": "frame",
        "name": "Glide 5\"",
        "brand": "FPVCycle",
        "price_php": 2520,
        "weight_g": 58,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=FPVCycle+Glide",
        "color": "#111111",
        "specs": {
            "size_mm": 210,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 20,
            "thingiverse_url": "https://www.thingiverse.com/search?q=fpvcycle+glide"
        }
    },
    {
        "id": "fpvcycle-toothfairy-2",
        "category": "frame",
        "name": "Toothfairy 2",
        "brand": "FPVCycle",
        "price_php": 2240,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=FPVCycle+Toothfairy+2",
        "color": "#0a0a0a",
        "specs": {
            "size_mm": 140,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 20,
            "thingiverse_url": "https://www.thingiverse.com/search?q=fpvcycle+toothfairy"
        }
    },
    {
        "id": "kabab-v4-5inch",
        "category": "frame",
        "name": "Kabab V4 5\"",
        "brand": "Kabab FPV",
        "price_php": 2800,
        "weight_g": 72,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Kabab+V4+frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=kabab+fpv"
        }
    },
    {
        "id": "hyperlite-evo-5",
        "category": "frame",
        "name": "Evo 5\" Freestyle",
        "brand": "HyperLite",
        "price_php": 3920,
        "weight_g": 82,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=HyperLite+Evo+5",
        "color": "#222222",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=hyperlite+evo"
        }
    },
    {
        "id": "apex-mr5-hd",
        "category": "frame",
        "name": "MR5 HD Frame",
        "brand": "Apex FPV",
        "price_php": 3360,
        "weight_g": 90,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Apex+MR5+HD",
        "color": "#1b1b1b",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28,
            "thingiverse_url": "https://www.thingiverse.com/search?q=apex+mr5"
        }
    },
    {
        "id": "squid-rc-v2-5inch",
        "category": "frame",
        "name": "Squid V2 5\"",
        "brand": "Squid RC",
        "price_php": 2520,
        "weight_g": 68,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Squid+RC+V2",
        "color": "#151515",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=squid+rc"
        }
    },
    {
        "id": "lethal-conception-bk5",
        "category": "frame",
        "name": "BK5 5\" Frame",
        "brand": "Lethal Conception",
        "price_php": 3640,
        "weight_g": 85,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Lethal+Conception+BK5",
        "color": "#1f1f1f",
        "specs": {
            "size_mm": 218,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=lethal+conception"
        }
    },
    {
        "id": "cl2-v2-frame",
        "category": "frame",
        "name": "CL2 V2 5\" Frame",
        "brand": "Rotor Riot",
        "price_php": 3920,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Rotor+Riot+CL2+V2",
        "color": "#181818",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=cl2+v2+frame"
        }
    },
    {
        "id": "skyeliner-5-hd",
        "category": "frame",
        "name": "Skyeliner 5\" HD",
        "brand": "Skyeliner",
        "price_php": 3080,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Skyeliner+5+HD+frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=skyeliner"
        }
    },

    # ========== MOTORS ==========
    {
        "id": "emax-eco3-2207-1900kv",
        "category": "motor",
        "name": "ECO3 2207 1900KV",
        "brand": "Emax",
        "price_php": 896,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Emax+ECO3+2207+1900KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "emax-eco3-2207-2400kv",
        "category": "motor",
        "name": "ECO3 2207 2400KV",
        "brand": "Emax",
        "price_php": 896,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Emax+ECO3+2207+2400KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2400,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "sub250-2306-1750kv",
        "category": "motor",
        "name": "Sub250 2306 1750KV",
        "brand": "Sub250",
        "price_php": 1120,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Sub250+2306+1750KV",
        "color": "#333333",
        "specs": {
            "kv": 1750,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "sub250-2306-2550kv",
        "category": "motor",
        "name": "Sub250 2306 2550KV",
        "brand": "Sub250",
        "price_php": 1120,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Sub250+2306+2550KV",
        "color": "#333333",
        "specs": {
            "kv": 2550,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "rcinpower-smoox-2306-1880kv",
        "category": "motor",
        "name": "SmooX 2306 1880KV",
        "brand": "RCINPower",
        "price_php": 1568,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RCINPower+SmooX+2306+1880KV",
        "color": "#252525",
        "specs": {
            "kv": 1880,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "rcinpower-smoox-2306-2580kv",
        "category": "motor",
        "name": "SmooX 2306 2580KV",
        "brand": "RCINPower",
        "price_php": 1568,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RCINPower+SmooX+2306+2580KV",
        "color": "#252525",
        "specs": {
            "kv": 2580,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "flywoo-nim-2207-1750kv",
        "category": "motor",
        "name": "NIN 2207 1750KV",
        "brand": "Flywoo",
        "price_php": 1232,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+NIN+2207+1750KV",
        "color": "#2c2c2c",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "flywoo-nim-2207-2450kv",
        "category": "motor",
        "name": "NIN 2207 2450KV",
        "brand": "Flywoo",
        "price_php": 1232,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+NIN+2207+2450KV",
        "color": "#2c2c2c",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 46
        }
    },
    {
        "id": "fpvcycle-25mm-2507-1960kv",
        "category": "motor",
        "name": "25mm 2507 1960KV",
        "brand": "FPVCycle",
        "price_php": 1400,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=FPVCycle+25mm+2507+1960KV",
        "color": "#2d2d2d",
        "specs": {
            "kv": 1960,
            "stator_size": "2507",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "geprc-speedx2-2207-1900kv",
        "category": "motor",
        "name": "SpeedX2 2207 1900KV",
        "brand": "GEPRC",
        "price_php": 1008,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+SpeedX2+2207+1900KV",
        "color": "#2b2b2b",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "geprc-speedx2-2207-2450kv",
        "category": "motor",
        "name": "SpeedX2 2207 2450KV",
        "brand": "GEPRC",
        "price_php": 1008,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+SpeedX2+2207+2450KV",
        "color": "#2b2b2b",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 47
        }
    },
    {
        "id": "tmotor-pacer-v3-2207-1950kv",
        "category": "motor",
        "name": "Pacer V3 2207 1950KV",
        "brand": "T-Motor",
        "price_php": 1344,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Pacer+V3+2207+1950KV",
        "color": "#2e2e2e",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },
    {
        "id": "tmotor-pacer-v3-2207-2550kv",
        "category": "motor",
        "name": "Pacer V3 2207 2550KV",
        "brand": "T-Motor",
        "price_php": 1344,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+Pacer+V3+2207+2550KV",
        "color": "#2e2e2e",
        "specs": {
            "kv": 2550,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "xnova-smooth-2207-1800kv",
        "category": "motor",
        "name": "Smooth 2207 1800KV",
        "brand": "XNOVA",
        "price_php": 1960,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=XNOVA+Smooth+2207+1800KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 39
        }
    },
    {
        "id": "xnova-smooth-2207-2450kv",
        "category": "motor",
        "name": "Smooth 2207 2450KV",
        "brand": "XNOVA",
        "price_php": 1960,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=XNOVA+Smooth+2207+2450KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 46
        }
    },

    # ========== ESCs ==========
    {
        "id": "speedybee-bl32-55a-4in1-v2",
        "category": "esc",
        "name": "BLS 55A 4-in-1 V2",
        "brand": "SpeedyBee",
        "price_php": 2800,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+BLS+55A+4-in-1+V2",
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
        "id": "foxeer-reaper-f4-45a-4in1-v2",
        "category": "esc",
        "name": "Reaper F4 45A 4-in-1 V2",
        "brand": "Foxeer",
        "price_php": 3080,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Reaper+F4+45A+4in1+V2",
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
        "id": "aikon-ak32-50a-6s-v3",
        "category": "esc",
        "name": "AK32 50A 6S V3 4-in-1",
        "brand": "Aikon",
        "price_php": 3920,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Aikon+AK32+50A+6S+V3+4in1",
        "color": "#001100",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "flycolor-raptor-s-tower-40a",
        "category": "esc",
        "name": "Raptor S Tower 40A 4-in-1",
        "brand": "Flycolor",
        "price_php": 2240,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+Raptor+S+Tower+40A",
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
        "id": "t-motor-f45a-pro-iii-4in1",
        "category": "esc",
        "name": "F45A PRO III 4-in-1",
        "brand": "T-Motor",
        "price_php": 3640,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F45A+PRO+III+4in1",
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
        "id": "jhemcu-blh32-45a-4in1",
        "category": "esc",
        "name": "BLH32 45A 4-in-1",
        "brand": "JHEMCU",
        "price_php": 2240,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=JHEMCU+BLH32+45A+4in1",
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
        "id": "diatone-mamba-f60a-mk2-4in1",
        "category": "esc",
        "name": "Mamba F60A MK2 4-in-1",
        "brand": "Diatone",
        "price_php": 3360,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F60A+MK2+4in1",
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
        "id": "geprc-gep-bl50a-v2-4in1",
        "category": "esc",
        "name": "GEP-BL50A V2 4-in-1",
        "brand": "GEPRC",
        "price_php": 2800,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+GEP-BL50A+V2+4in1",
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
        "id": "hobbywing-xrotor-60a-4in1-v2",
        "category": "esc",
        "name": "XRotor 60A 4-in-1 V2",
        "brand": "Hobbywing",
        "price_php": 4200,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Hobbywing+XRotor+60A+4in1+V2",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 80
        }
    },
    {
        "id": "flywoo-goku-50a-bl32-4in1",
        "category": "esc",
        "name": "Goku 50A BL32 4-in-1",
        "brand": "Flywoo",
        "price_php": 2520,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Goku+50A+BL32+4in1",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },

    # ========== FLIGHT CONTROLLERS ==========
    {
        "id": "jhemcu-ghf745-aio",
        "category": "fc",
        "name": "GHF745 AIO FC",
        "brand": "JHEMCU",
        "price_php": 2240,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=JHEMCU+GHF745+AIO",
        "color": "#000055",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },
    {
        "id": "matek-h743-slim-v3",
        "category": "fc",
        "name": "H743-SLIM V3",
        "brand": "Matek",
        "price_php": 4480,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=h743-slim-v3",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 4,
            "curr_sensor": True,
            "diagram_url": "https://www.mateksys.com/?portfolio=h743-slim-v3"
        }
    },
    {
        "id": "foxeer-f722-v4-fc",
        "category": "fc",
        "name": "F722 V4 Flight Controller",
        "brand": "Foxeer",
        "price_php": 2800,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+F722+V4+Flight+Controller",
        "color": "#000055",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },
    {
        "id": "diatone-mamba-f722-mk4",
        "category": "fc",
        "name": "Mamba F722 MK4 FC",
        "brand": "Diatone",
        "price_php": 2520,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F722+MK4",
        "color": "#000055",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },
    {
        "id": "holybro-kakute-h7-mini-v2",
        "category": "fc",
        "name": "Kakute H7 Mini V2",
        "brand": "Holybro",
        "price_php": 3360,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Kakute+H7+Mini+V2",
        "color": "#000055",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },
    {
        "id": "speedybee-f405-wing-mini",
        "category": "fc",
        "name": "F405 Wing Mini",
        "brand": "SpeedyBee",
        "price_php": 2240,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+F405+Wing+Mini",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "INAV",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },
    {
        "id": "flywoo-goku-h743-v2",
        "category": "fc",
        "name": "Goku H743 V2 FC",
        "brand": "Flywoo",
        "price_php": 3920,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Goku+H743+V2",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 4,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },
    {
        "id": "hglrc-zeusf745-v4",
        "category": "fc",
        "name": "Zeus F745 V4 FC",
        "brand": "HGLRC",
        "price_php": 2800,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Zeus+F745+V4",
        "color": "#000055",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },
    {
        "id": "microair-m745-fc",
        "category": "fc",
        "name": "M745 FC",
        "brand": "MicoAir",
        "price_php": 2520,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=MicoAir+M745+FC",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },
    {
        "id": "geprc-taker-g4-h7-45a-aio",
        "category": "fc",
        "name": "Taker G4 H7 45A AIO",
        "brand": "GEPRC",
        "price_php": 4480,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Taker+G4+H7+45A+AIO",
        "color": "#000055",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": ""
        }
    },

    # ========== PROPELLERS ==========
    {
        "id": "gemfan-hurricane-51433-v2",
        "category": "propeller",
        "name": "Hurricane 51433 V2",
        "brand": "Gemfan",
        "price_php": 168,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51433+V2",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.33,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "blue", "red", "clear"]
        }
    },
    {
        "id": "hqprop-r38-5x3-8x3",
        "category": "propeller",
        "name": "R38 5x3.8x3",
        "brand": "HQProp",
        "price_php": 224,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+R38+5x3.8x3",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 3.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "blue"]
        }
    },
    {
        "id": "ethix-p4-candy-cane",
        "category": "propeller",
        "name": "P4 Candy Cane 5.1x4x3",
        "brand": "Ethix",
        "price_php": 280,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+P4+Candy+Cane",
        "color": "#cc0000",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["red/white"]
        }
    },
    {
        "id": "dal-fold-f5-5046",
        "category": "propeller",
        "name": "Fold F5 5046",
        "brand": "DAL",
        "price_php": 196,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Fold+F5+5046",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "red", "green"]
        }
    },
    {
        "id": "gemfan-cinelifter-7035",
        "category": "propeller",
        "name": "Cinelifter 7035 Tri-Blade",
        "brand": "Gemfan",
        "price_php": 336,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+7035+Cinelifter",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 3.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "clear"]
        }
    },
    {
        "id": "hqprop-dp-3x3x3",
        "category": "propeller",
        "name": "DP 3x3x3",
        "brand": "HQProp",
        "price_php": 168,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP+3x3x3",
        "color": "#111",
        "specs": {
            "diameter_inch": 3,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "blue", "red"]
        }
    },
    {
        "id": "gemfan-hurricane-3520-v2",
        "category": "propeller",
        "name": "Hurricane 3520 V2",
        "brand": "Gemfan",
        "price_php": 140,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+3520+V2",
        "color": "#111",
        "specs": {
            "diameter_inch": 3.5,
            "pitch": 2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "clear", "green"]
        }
    },
    {
        "id": "dal-cyclone-t5045c-v3",
        "category": "propeller",
        "name": "Cyclone T5045C V3",
        "brand": "DAL",
        "price_php": 168,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T5045C+V3",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "clear", "red", "green"]
        }
    },
    {
        "id": "gemfan-hurricane-4023-2blade",
        "category": "propeller",
        "name": "Hurricane 4023 2-Blade",
        "brand": "Gemfan",
        "price_php": 140,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+4023+2-Blade",
        "color": "#111",
        "specs": {
            "diameter_inch": 4,
            "pitch": 2.3,
            "blade_count": 2,
            "shaft_mm": 5,
            "color_options": ["black", "clear"]
        }
    },
    {
        "id": "ethix-p3-peanut-butter-jelly",
        "category": "propeller",
        "name": "P3 Peanut Butter & Jelly 5.1x3x3",
        "brand": "Ethix",
        "price_php": 252,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+P3+Peanut+Butter+Jelly",
        "color": "#993399",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["purple/yellow"]
        }
    },

    # ========== CAMERAS ==========
    {
        "id": "caddx-ratel-2-pro",
        "category": "camera",
        "name": "Ratel 2 Pro",
        "brand": "Caddx",
        "price_php": 1960,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ratel+2+Pro",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-t-rex-3-micro",
        "category": "camera",
        "name": "T-Rex 3 Micro",
        "brand": "Foxeer",
        "price_php": 2240,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+T-Rex+3+Micro",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1500,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-racer-5-nano",
        "category": "camera",
        "name": "Racer 5 Nano",
        "brand": "RunCam",
        "price_php": 1680,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Racer+5+Nano",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-cam",
        "category": "camera",
        "name": "Avatar HD V3 Camera",
        "brand": "Walksnail",
        "price_php": 3360,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+HD+V3+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 170,
            "format": "Digital",
            "tvl": 1080,
            "voltage_range": "7-26V",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "hdzero-nano-lite-v3",
        "category": "camera",
        "name": "Nano Lite V3",
        "brand": "HDZero",
        "price_php": 2520,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Nano+Lite+V3",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Digital",
            "tvl": 720,
            "voltage_range": "5-16V",
            "video_system": "HDZero"
        }
    },
    {
        "id": "dji-o4-air-unit-camera",
        "category": "camera",
        "name": "O4 Air Unit Camera",
        "brand": "DJI",
        "price_php": 5600,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+O4+Air+Unit+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Digital",
            "tvl": 1080,
            "voltage_range": "7-26V",
            "video_system": "DJI"
        }
    },
    {
        "id": "foxeer-cat-4-mini",
        "category": "camera",
        "name": "Cat 4 Mini",
        "brand": "Foxeer",
        "price_php": 2800,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Cat+4+Mini",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 170,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-nebula-pro-nano-v2",
        "category": "camera",
        "name": "Nebula Pro Nano V2",
        "brand": "Caddx",
        "price_php": 3640,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Nebula+Pro+Nano+V2",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 162,
            "format": "Digital",
            "tvl": 720,
            "voltage_range": "7-26V",
            "video_system": "DJI"
        }
    },
    {
        "id": "runcam-phoenix-3",
        "category": "camera",
        "name": "Phoenix 3",
        "brand": "RunCam",
        "price_php": 2240,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Phoenix+3",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-1s-nano-cam",
        "category": "camera",
        "name": "1S Nano Camera",
        "brand": "Walksnail",
        "price_php": 2800,
        "weight_g": 2.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+1S+Nano+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/4\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "tvl": 720,
            "voltage_range": "3.3-5.5V",
            "video_system": "Walksnail"
        }
    },

    # ========== VIDEO TRANSMITTERS ==========
    {
        "id": "hdzero-race-v4-vtx",
        "category": "vtx",
        "name": "Race V4 VTX",
        "brand": "HDZero",
        "price_php": 3920,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Race+V4+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX",
            "video_system": "HDZero"
        }
    },
    {
        "id": "caddx-vista-polar-starlight",
        "category": "vtx",
        "name": "Vista Polar Starlight VTX",
        "brand": "Caddx",
        "price_php": 5040,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Vista+Polar+Starlight",
        "color": "#221100",
        "specs": {
            "power_mw_max": 700,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX",
            "video_system": "DJI"
        }
    },
    {
        "id": "rush-blade-v2-vtx",
        "category": "vtx",
        "name": "Blade V2 Race VTX",
        "brand": "Rush",
        "price_php": 1400,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rush+Blade+V2+Race+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "walksnail-avatar-hd-mini-1s",
        "category": "vtx",
        "name": "Avatar HD Mini 1S VTX",
        "brand": "Walksnail",
        "price_php": 5600,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+HD+Mini+1S+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 350,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "3.3-5.5V",
            "connector": "UFL",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "akk-x2-ultimate-vtx",
        "category": "vtx",
        "name": "X2 Ultimate VTX",
        "brand": "AKK",
        "price_php": 1120,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+X2+Ultimate+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-24V",
            "connector": "SMA"
        }
    },
    {
        "id": "tbs-unify-pro32-hv",
        "category": "vtx",
        "name": "Unify Pro32 HV VTX",
        "brand": "TBS",
        "price_php": 3080,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro32+HV",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "speedybee-tx800-vtx",
        "category": "vtx",
        "name": "TX800 VTX",
        "brand": "SpeedyBee",
        "price_php": 1680,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+TX800+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "foxeer-reaper-infinity-vtx",
        "category": "vtx",
        "name": "Reaper Infinity 5.8G VTX",
        "brand": "Foxeer",
        "price_php": 2520,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Reaper+Infinity+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },
    {
        "id": "dji-o4-air-unit-vtx",
        "category": "vtx",
        "name": "O4 Air Unit VTX",
        "brand": "DJI",
        "price_php": 7840,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+O4+Air+Unit",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX",
            "video_system": "DJI"
        }
    },
    {
        "id": "hdzero-freestyle-v3-vtx",
        "category": "vtx",
        "name": "Freestyle V3 VTX",
        "brand": "HDZero",
        "price_php": 4480,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Freestyle+V3+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX",
            "video_system": "HDZero"
        }
    },

    # ========== BATTERIES ==========
    {
        "id": "gnb-ultra-4s-1500mah-150c",
        "category": "battery",
        "name": "Ultra 1500mAh 4S 150C",
        "brand": "GNB",
        "price_php": 1400,
        "weight_g": 180,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=GNB+Ultra+1500mAh+4S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gnb-ultra-6s-1100mah-150c",
        "category": "battery",
        "name": "Ultra 1100mAh 6S 150C",
        "brand": "GNB",
        "price_php": 1680,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=GNB+Ultra+1100mAh+6S+150C",
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
        "id": "cnhl-black-series-4s-1500mah-150c",
        "category": "battery",
        "name": "Black Series 1500mAh 4S 150C",
        "brand": "CNHL",
        "price_php": 1232,
        "weight_g": 185,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=CNHL+Black+Series+1500mAh+4S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "cnhl-black-series-6s-1300mah-150c",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 150C",
        "brand": "CNHL",
        "price_php": 1568,
        "weight_g": 210,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=CNHL+Black+Series+1300mAh+6S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-r-line-v5-6s-1300mah-150c",
        "category": "battery",
        "name": "R-Line V5 1300mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2800,
        "weight_g": 205,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5+1300mAh+6S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
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
        "weight_g": 188,
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
        "id": "ovonic-6s-1300mah-120c",
        "category": "battery",
        "name": "1300mAh 6S 120C",
        "brand": "Ovonic",
        "price_php": 1400,
        "weight_g": 200,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ovonic+1300mAh+6S+120C",
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
        "id": "dogcom-4s-1500mah-150c",
        "category": "battery",
        "name": "1500mAh 4S 150C",
        "brand": "Dogcom",
        "price_php": 1344,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Dogcom+1500mAh+4S+150C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "rdq-series-4s-1500mah-100c",
        "category": "battery",
        "name": "RDQ Series 1500mAh 4S 100C",
        "brand": "RDQ",
        "price_php": 1008,
        "weight_g": 182,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=RDQ+Series+1500mAh+4S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "rdq-series-6s-1050mah-100c",
        "category": "battery",
        "name": "RDQ Series 1050mAh 6S 100C",
        "brand": "RDQ",
        "price_php": 1232,
        "weight_g": 168,
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
        "id": "lumenier-graphene-4s-1500mah-80c",
        "category": "battery",
        "name": "Graphene 1500mAh 4S 80C",
        "brand": "Lumenier",
        "price_php": 2240,
        "weight_g": 192,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+Graphene+1500mAh+4S+80C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 80,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-funfly-4s-1550mah-100c",
        "category": "battery",
        "name": "Funfly 1550mAh 4S 100C",
        "brand": "Tattu",
        "price_php": 1344,
        "weight_g": 182,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+Funfly+1550mAh+4S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1550,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "fullsend-4s-1300mah-120c",
        "category": "battery",
        "name": "FullSend 1300mAh 4S 120C",
        "brand": "FullSend",
        "price_php": 1680,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=FullSend+1300mAh+4S+120C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "fullsend-6s-1050mah-120c",
        "category": "battery",
        "name": "FullSend 1050mAh 6S 120C",
        "brand": "FullSend",
        "price_php": 1960,
        "weight_g": 162,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=FullSend+1050mAh+6S+120C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1050,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ========== RECEIVERS ==========
    {
        "id": "radiomaster-rp4td-elrs",
        "category": "receiver",
        "name": "RP4TD ELRS 2.4GHz",
        "brand": "RadioMaster",
        "price_php": 1120,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RadioMaster+RP4TD+ELRS+2.4GHz",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "happymodel-ep3-rx-elrs",
        "category": "receiver",
        "name": "EP3 RX ELRS 2.4GHz",
        "brand": "HappyModel",
        "price_php": 784,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP3+RX+ELRS",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "tbs-crossfire-nano-diversity-rx",
        "category": "receiver",
        "name": "Crossfire Nano Diversity RX",
        "brand": "TBS",
        "price_php": 2520,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+Diversity+RX",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "betafpv-elrs-nano-rx-2400",
        "category": "receiver",
        "name": "ELRS Nano RX 2.4GHz",
        "brand": "BetaFPV",
        "price_php": 896,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+ELRS+Nano+RX+2.4GHz",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "speedybee-rx-elrs-2400",
        "category": "receiver",
        "name": "RX ELRS 2.4GHz",
        "brand": "SpeedyBee",
        "price_php": 840,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+RX+ELRS+2.4GHz",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "radiomaster-er5c-elrs",
        "category": "receiver",
        "name": "ER5C ELRS 2.4GHz",
        "brand": "RadioMaster",
        "price_php": 952,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RadioMaster+ER5C+ELRS",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "iflight-elrs-2-4g-nano-rx",
        "category": "receiver",
        "name": "ELRS 2.4G Nano RX",
        "brand": "iFlight",
        "price_php": 840,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+ELRS+2.4G+Nano+RX",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "tbs-tracer-nano-rx",
        "category": "receiver",
        "name": "Tracer Nano RX",
        "brand": "TBS",
        "price_php": 2240,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Tracer+Nano+RX",
        "color": "#1a001a",
        "specs": {
            "protocol": "Tracer",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "jumper-aion-nano-pro-elrs",
        "category": "receiver",
        "name": "AION Nano Pro ELRS 2.4GHz",
        "brand": "Jumper",
        "price_php": 896,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Jumper+AION+Nano+Pro+ELRS",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "geprc-elrs-nano-rx-2400",
        "category": "receiver",
        "name": "ELRS Nano RX 2.4GHz",
        "brand": "GEPRC",
        "price_php": 784,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+ELRS+Nano+RX+2.4GHz",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },

    # ========== GPS MODULES ==========
    {
        "id": "beitian-bn880-gps-compass",
        "category": "gps",
        "name": "BN-880 GPS+Compass",
        "brand": "Beitian",
        "price_php": 840,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880+GPS+Compass",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "speedybee-nav-v2-gps",
        "category": "gps",
        "name": "NAV V2 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1400,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+NAV+V2+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 12,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "flywoo-goku-gps-m10-mini",
        "category": "gps",
        "name": "Goku GPS M10 Mini",
        "brand": "Flywoo",
        "price_php": 1120,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Goku+GPS+M10+Mini",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 15,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1680,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-5883",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 10,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-m10-nano-gps",
        "category": "gps",
        "name": "M10 Nano GPS",
        "brand": "Holybro",
        "price_php": 1344,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+M10+Nano+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 12,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "geprc-gep-m10-gps",
        "category": "gps",
        "name": "GEP-M10 GPS Module",
        "brand": "GEPRC",
        "price_php": 1232,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+GEP-M10+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 12,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "foxeer-m10q-250-gps",
        "category": "gps",
        "name": "M10Q-250 GPS+Compass",
        "brand": "Foxeer",
        "price_php": 1568,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+M10Q+250+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 10,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "betafpv-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "BetaFPV",
        "price_php": 1120,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+M10+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 15,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },

    # ========== VTX ANTENNAS ==========
    {
        "id": "truerc-singularity-5-8-stubby",
        "category": "antenna",
        "name": "Singularity 5.8GHz Stubby",
        "brand": "TrueRC",
        "price_php": 1120,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Singularity+5.8GHz+Stubby",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.1,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "foxeer-echo-2-patch",
        "category": "antenna",
        "name": "Echo 2 Patch Antenna",
        "brand": "Foxeer",
        "price_php": 1400,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Echo+2+Patch+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 9.4,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
        }
    },
    {
        "id": "lumenier-axii-2-5-8-stubby",
        "category": "antenna",
        "name": "AXII 2 5.8GHz Stubby",
        "brand": "Lumenier",
        "price_php": 1680,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Lumenier+AXII+2+5.8GHz+Stubby",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 1.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "menace-raptor-5-8-patch",
        "category": "antenna",
        "name": "Raptor 5.8GHz Patch",
        "brand": "Menace Antennas",
        "price_php": 2520,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Menace+Raptor+5.8GHz+Patch",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 11.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
        }
    },
    {
        "id": "rushfpv-cherry-2-antenna",
        "category": "antenna",
        "name": "Cherry 2 5.8GHz Antenna",
        "brand": "RushFPV",
        "price_php": 896,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RushFPV+Cherry+2+5.8GHz+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "tbs-triumph-pro-5-8",
        "category": "antenna",
        "name": "Triumph Pro 5.8GHz",
        "brand": "TBS",
        "price_php": 1400,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Triumph+Pro+5.8GHz",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "ibcrazy-pepperbox-5-8",
        "category": "antenna",
        "name": "PepperBox 5.8GHz",
        "brand": "IBCrazy",
        "price_php": 2240,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=IBCrazy+PepperBox+5.8GHz",
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
        "id": "hglrc-hammer-5-8-antenna",
        "category": "antenna",
        "name": "Hammer 5.8GHz Antenna",
        "brand": "HGLRC",
        "price_php": 672,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HGLRC+Hammer+5.8GHz+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "geprc-momoda-5-8-antenna",
        "category": "antenna",
        "name": "Momoda 5.8GHz Antenna",
        "brand": "GEPRC",
        "price_php": 560,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Momoda+5.8GHz+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "xilo-phaze-5-8-antenna",
        "category": "antenna",
        "name": "Phaze 5.8GHz Stubby",
        "brand": "XILO",
        "price_php": 784,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=XILO+Phaze+5.8GHz+Stubby",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
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
            print(f"SKIP (duplicate): {part['id']}")
            skipped += 1
        else:
            data["parts"].append(part)
            existing_ids.add(part["id"])
            added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    from collections import Counter
    cats = Counter(p["category"] for p in NEW_PARTS if p["id"] not in {pp["id"] for pp in data["parts"][:len(data["parts"]) - added]})

    print(f"\nAdded {added} new parts, skipped {skipped} duplicates")
    print(f"Total parts now: {len(data['parts'])}")

    cats2 = Counter(p["category"] for p in data["parts"])
    print("\nParts per category:")
    for cat in ["frame", "motor", "esc", "fc", "propeller", "camera", "vtx", "battery", "receiver", "gps", "antenna"]:
        print(f"  {cat}: {cats2[cat]}")


if __name__ == "__main__":
    main()
