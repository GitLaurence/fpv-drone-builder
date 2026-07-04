"""Batch 52 — adds real, currently-available FPV parts across all 11 categories.

Prices are in PHP, converted at the same ~56 PHP/USD rate used by prior
batches. buy_url values point to each brand's own storefront search (or
getfpv.com as a general retailer) using the same query-string convention as
the rest of the catalog.
"""
import json

NEW_PARTS = [
    # ========== FRAMES ==========
    {
        "id": "armattan-skitzo-5-frame",
        "category": "frame",
        "name": "Skitzo 5\" Freestyle Frame",
        "brand": "Armattan",
        "price_php": 6160,
        "weight_g": 96,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Skitzo+5+Freestyle+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 227,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28
        }
    },
    {
        "id": "geprc-cinebot30-frame",
        "category": "frame",
        "name": "Cinebot30 3\" Cinewhoop Frame",
        "brand": "GEPRC",
        "price_php": 2464,
        "weight_g": 65,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+Cinebot30+Frame",
        "color": "#0f0f0f",
        "specs": {
            "size_mm": 149,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 20,
            "material": "carbon fiber + duct",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 20
        }
    },
    {
        "id": "geprc-cinelog35-v2-frame",
        "category": "frame",
        "name": "Cinelog35 V2 Cinewhoop Frame",
        "brand": "GEPRC",
        "price_php": 3080,
        "weight_g": 108,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+Cinelog35+V2+Frame",
        "color": "#101010",
        "specs": {
            "size_mm": 178,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber + duct",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "hglrc-sector-5-v5-frame",
        "category": "frame",
        "name": "Sector 5 V5 Freestyle Frame",
        "brand": "HGLRC",
        "price_php": 3696,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Sector+5+V5+Frame",
        "color": "#111827",
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
        "id": "diatone-roma-l6-frame",
        "category": "frame",
        "name": "Roma L6 Long Range Frame",
        "brand": "Diatone",
        "price_php": 4480,
        "weight_g": 118,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Diatone+Roma+L6+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 275,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "iflight-ix5-v3-frame",
        "category": "frame",
        "name": "iX5 V3 Freestyle Frame",
        "brand": "iFlight",
        "price_php": 3920,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+iX5+V3+Frame",
        "color": "#151515",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 28
        }
    },
    {
        "id": "flywoo-explorer-lr4-v3-frame",
        "category": "frame",
        "name": "Explorer LR4 V3 Long Range Frame",
        "brand": "Flywoo",
        "price_php": 3360,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+Explorer+LR4+V3+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 197,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "impulserc-reverb-4-frame",
        "category": "frame",
        "name": "Reverb 4\" Freestyle Frame",
        "brand": "ImpulseRC",
        "price_php": 5320,
        "weight_g": 74,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImpulseRC+Reverb+4+Frame",
        "color": "#111111",
        "specs": {
            "size_mm": 178,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "lumenier-qav-s-jb2-frame",
        "category": "frame",
        "name": "QAV-S JB2 Racing Frame",
        "brand": "Lumenier",
        "price_php": 4760,
        "weight_g": 68,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com/search?q=Lumenier+QAV-S+JB2+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 24
        }
    },
    {
        "id": "flywoo-hexplorer-lr-7-frame",
        "category": "frame",
        "name": "Hexplorer LR 7\" Long Range Frame",
        "brand": "Flywoo",
        "price_php": 5824,
        "weight_g": 152,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+Hexplorer+LR+7+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 305,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 32
        }
    },
    {
        "id": "emax-babyhawk-r-pro-frame",
        "category": "frame",
        "name": "Babyhawk R Pro 3\" Frame",
        "brand": "EMAX",
        "price_php": 1512,
        "weight_g": 48,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=EMAX+Babyhawk+R+Pro+3+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 138,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 18
        }
    },
    {
        "id": "axisflying-manta5-v3-frame",
        "category": "frame",
        "name": "Manta5 V3 Freestyle Frame",
        "brand": "Axisflying",
        "price_php": 4144,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/search?q=Axisflying+Manta5+V3+Frame",
        "color": "#101820",
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
        "id": "shendrones-squirt-v4-frame",
        "category": "frame",
        "name": "Squirt V4 5\" Freestyle Frame",
        "brand": "ShenDrones",
        "price_php": 6440,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ShenDrones+Squirt+V4+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 227,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 28
        }
    },
    {
        "id": "geprc-crocodile-baby8-v2-frame",
        "category": "frame",
        "name": "Crocodile Baby8 V2 Long Range Frame",
        "brand": "GEPRC",
        "price_php": 5040,
        "weight_g": 135,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+Crocodile+Baby8+V2+Frame",
        "color": "#0f0f0f",
        "specs": {
            "size_mm": 330,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 8,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 32
        }
    },
    # ========== MOTORS ==========
    {
        "id": "iflight-xing-e-pro-2207-1800kv",
        "category": "motor",
        "name": "XING-E Pro 2207 1800KV",
        "brand": "iFlight",
        "price_php": 1064,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+XING-E+Pro+2207+1800KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "tmotor-velox-v2207-v2-1750kv",
        "category": "motor",
        "name": "Velox V2207 V2 1750KV",
        "brand": "T-Motor",
        "price_php": 1400,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=T-Motor+Velox+V2207+V2+1750KV",
        "color": "#202020",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "brotherhobby-avenger-4-2306-1900kv",
        "category": "motor",
        "name": "Avenger 4 2306 1900KV",
        "brand": "BrotherHobby",
        "price_php": 952,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=BrotherHobby+Avenger+4+2306+1900KV",
        "color": "#0d0d0d",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "xnova-freestyle-v3-2306-1800kv",
        "category": "motor",
        "name": "Freestyle V3 2306 1800KV",
        "brand": "Xnova",
        "price_php": 1176,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Xnova+Freestyle+V3+2306+1800KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1800,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },
    {
        "id": "rcinpower-gts-v3-2306-1900kv",
        "category": "motor",
        "name": "GTS V3 2306 1900KV",
        "brand": "RCinPower",
        "price_php": 1064,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RCinPower+GTS+V3+2306+1900KV",
        "color": "#151515",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "flywoo-nin-2306.5-1800kv",
        "category": "motor",
        "name": "NIN 2306.5 1800KV",
        "brand": "Flywoo",
        "price_php": 896,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+NIN+2306.5+1800KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1800,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 39
        }
    },
    {
        "id": "geprc-speedx-2207.5-1800kv",
        "category": "motor",
        "name": "SPEEDX 2207.5 1800KV",
        "brand": "GEPRC",
        "price_php": 840,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+SPEEDX+2207.5+1800KV",
        "color": "#0f0f0f",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "hglrc-driver-2306.5-1900kv",
        "category": "motor",
        "name": "Driver 2306.5 1900KV",
        "brand": "HGLRC",
        "price_php": 868,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Driver+2306.5+1900KV",
        "color": "#111827",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "emax-eco-ii-2306-1700kv",
        "category": "motor",
        "name": "ECO II 2306 1700KV",
        "brand": "EMAX",
        "price_php": 616,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=EMAX+ECO+II+2306+1700KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1700,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "iflight-xing2-1608-3800kv",
        "category": "motor",
        "name": "XING2 1608 3800KV",
        "brand": "iFlight",
        "price_php": 616,
        "weight_g": 10.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+XING2+1608+3800KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 3800,
            "stator_size": "1608",
            "motor_mount_mm": 9,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 18
        }
    },
    {
        "id": "betafpv-1404-3800kv",
        "category": "motor",
        "name": "1404 3800KV Motor",
        "brand": "BetaFPV",
        "price_php": 448,
        "weight_g": 6.4,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=BetaFPV+1404+3800KV+Motor",
        "color": "#00aaff",
        "specs": {
            "kv": 3800,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 14
        }
    },
    {
        "id": "tmotor-f60-pro-v-2306-1950kv",
        "category": "motor",
        "name": "F60 Pro V 2306 1950KV",
        "brand": "T-Motor",
        "price_php": 1288,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=T-Motor+F60+Pro+V+2306+1950KV",
        "color": "#202020",
        "specs": {
            "kv": 1950,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },
    {
        "id": "sunnysky-r2207-v2-2450kv",
        "category": "motor",
        "name": "R2207 V2 2450KV",
        "brand": "SunnySky",
        "price_php": 728,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SunnySky+R2207+V2+2450KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 39
        }
    },
    # ========== ESCs ==========
    {
        "id": "iflight-blitz-e55-55a-4in1",
        "category": "esc",
        "name": "BLITZ E55 55A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 3080,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+BLITZ+E55+55A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "holybro-tekko32-f4-70a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 70A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 4368,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+Tekko32+F4+70A+4-in-1+ESC",
        "color": "#0a4d8f",
        "specs": {
            "amp_rating": 70,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 85
        }
    },
    {
        "id": "speedybee-bls-60a-v3-4in1",
        "category": "esc",
        "name": "BLS 60A V3 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 3416,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+BLS+60A+V3+4-in-1+ESC",
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
        "id": "diatone-mamba-f55-mk5-55a",
        "category": "esc",
        "name": "Mamba F55 MK5 55A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 3024,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Diatone+Mamba+F55+MK5+55A+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "geprc-taker-45a-4in1-esc",
        "category": "esc",
        "name": "TAKER 45A 4-in-1 ESC",
        "brand": "GEPRC",
        "price_php": 1904,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+TAKER+45A+4-in-1+ESC",
        "color": "#0f0f0f",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "hglrc-zeus-60a-v2-4in1",
        "category": "esc",
        "name": "ZEUS 60A V2 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 2856,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+ZEUS+60A+V2+4-in-1+ESC",
        "color": "#111827",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "flywoo-goku-gn-745-50a-4in1",
        "category": "esc",
        "name": "GOKU GN745 50A 4-in-1 ESC",
        "brand": "Flywoo",
        "price_php": 2352,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+GOKU+GN745+50A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 60
        }
    },
    {
        "id": "aikon-ak32h-45a-4in1",
        "category": "esc",
        "name": "AK32H 45A 4-in-1 ESC",
        "brand": "AIKON",
        "price_php": 2128,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AIKON+AK32H+45A+4-in-1+ESC",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "hobbywing-xrotor-70a-v2-4in1",
        "category": "esc",
        "name": "XRotor 70A V2 4-in-1 ESC",
        "brand": "Hobbywing",
        "price_php": 3752,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Hobbywing+XRotor+70A+V2+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 70,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 85
        }
    },
    {
        "id": "jhemcu-gh40-40a-4in1",
        "category": "esc",
        "name": "GH40 40A 4-in-1 ESC",
        "brand": "JHEMCU",
        "price_php": 1568,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=JHEMCU+GH40+40A+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 50
        }
    },
    # ========== FLIGHT CONTROLLERS ==========
    {
        "id": "speedybee-f745-v4-aio-fc",
        "category": "fc",
        "name": "F745 V4 AIO Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 3808,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+F745+V4+AIO+Flight+Controller",
        "color": "#111111",
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
        "id": "holybro-kakute-h7-mini-v2-fc",
        "category": "fc",
        "name": "Kakute H7 Mini V2 Flight Controller",
        "brand": "Holybro",
        "price_php": 3696,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+Kakute+H7+Mini+V2+Flight+Controller",
        "color": "#0a4d8f",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "iflight-blitz-mini-f722-fc",
        "category": "fc",
        "name": "BLITZ Mini F722 Flight Controller",
        "brand": "iFlight",
        "price_php": 2856,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+BLITZ+Mini+F722+Flight+Controller",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "geprc-taker-f745-v2-fc",
        "category": "fc",
        "name": "TAKER F745 V2 Flight Controller",
        "brand": "GEPRC",
        "price_php": 2464,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+TAKER+F745+V2+Flight+Controller",
        "color": "#0f0f0f",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": False
        }
    },
    {
        "id": "hglrc-zeus-f745-v2-fc",
        "category": "fc",
        "name": "ZEUS F745 V2 Flight Controller",
        "brand": "HGLRC",
        "price_php": 2632,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+ZEUS+F745+V2+Flight+Controller",
        "color": "#111827",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": False
        }
    },
    {
        "id": "flywoo-goku-gn745-fc",
        "category": "fc",
        "name": "GOKU GN745 Flight Controller",
        "brand": "Flywoo",
        "price_php": 2296,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+GOKU+GN745+Flight+Controller",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "foxeer-f722-v5-fc",
        "category": "fc",
        "name": "F722 V5 Flight Controller",
        "brand": "Foxeer",
        "price_php": 2072,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+F722+V5+Flight+Controller",
        "color": "#1a1a1a",
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
    {
        "id": "matek-f765-wing-se-fc",
        "category": "fc",
        "name": "F765-WING SE Flight Controller",
        "brand": "Matek",
        "price_php": 4144,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F765-WING+SE+Flight+Controller",
        "color": "#1a1a1a",
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
        "id": "axisflying-argus-f745-fc",
        "category": "fc",
        "name": "ARGUS F745 Flight Controller",
        "brand": "Axisflying",
        "price_php": 2744,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/search?q=Axisflying+ARGUS+F745+Flight+Controller",
        "color": "#101820",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": False
        }
    },
    # ========== PROPELLERS ==========
    {
        "id": "hqprop-dp5x4.3x3-v2",
        "category": "propeller",
        "name": "DP5x4.3x3 V2 Durable Prop",
        "brand": "HQProp",
        "price_php": 224,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP5x4.3x3+V2",
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
        "id": "gemfan-hurricane-51477-v3",
        "category": "propeller",
        "name": "Hurricane 51477 V3",
        "brand": "Gemfan",
        "price_php": 252,
        "weight_g": 5.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51477+V3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    {
        "id": "dal-cyclone-t5045c-v4",
        "category": "propeller",
        "name": "Cyclone T5045C V4",
        "brand": "DAL",
        "price_php": 210,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DAL+Cyclone+T5045C+V4",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "orange"]
        }
    },
    {
        "id": "azure-power-switchblade-5-v2",
        "category": "propeller",
        "name": "Switchblade 5 V2",
        "brand": "Azure",
        "price_php": 266,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Azure+Switchblade+5+V2",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    {
        "id": "ethix-s5-lite-v2",
        "category": "propeller",
        "name": "S5 Lite V2",
        "brand": "Ethix",
        "price_php": 280,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+S5+Lite+V2",
        "color": "#f5f5f5",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "white"]
        }
    },
    {
        "id": "iflight-cine-tri-blade-3-prop",
        "category": "propeller",
        "name": "Cinewhoop Tri-Blade 3\" Prop",
        "brand": "iFlight",
        "price_php": 168,
        "weight_g": 2.9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+Cinewhoop+Tri-Blade+3+Prop",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 3,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["black"]
        }
    },
    {
        "id": "gemfan-windancer-5140-v2",
        "category": "propeller",
        "name": "WinDancer 5140 V2",
        "brand": "Gemfan",
        "price_php": 238,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+WinDancer+5140+V2",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "green"]
        }
    },
    {
        "id": "dalprop-t7056c-7in-prop",
        "category": "propeller",
        "name": "T7056C 7\" Long Range Prop",
        "brand": "DALProp",
        "price_php": 336,
        "weight_g": 8.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DALProp+T7056C+7in+Prop",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 7,
            "pitch": 5.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black"]
        }
    },
    # ========== FPV CAMERAS ==========
    {
        "id": "walksnail-avatar-hd-v2-nano-cam",
        "category": "camera",
        "name": "Avatar HD V2 Nano Digital Camera",
        "brand": "Walksnail",
        "price_php": 3696,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Walksnail+Avatar+HD+V2+Nano+Camera",
        "color": "#111111",
        "specs": {
            "sensor": "1/1.8\" STARVIS",
            "fov_deg": 150,
            "format": "4:3",
            "video_system": "Walksnail",
            "resolution": "1080p60",
            "latency_ms": 18
        }
    },
    {
        "id": "hdzero-freestyle-v7-cam",
        "category": "camera",
        "name": "Freestyle V7 Digital Camera",
        "brand": "HDZero",
        "price_php": 3360,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Freestyle+V7+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 150,
            "format": "4:3",
            "video_system": "HDZero",
            "resolution": "720p60",
            "latency_ms": 10
        }
    },
    {
        "id": "caddx-ratel-air-nano-cam",
        "category": "camera",
        "name": "Ratel Air Nano Analog Camera",
        "brand": "Caddx",
        "price_php": 1064,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Caddx+Ratel+Air+Nano+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "video_system": "analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-hybrid-3-cam",
        "category": "camera",
        "name": "Hybrid 3 Analog/4K Camera",
        "brand": "RunCam",
        "price_php": 4816,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=RunCam+Hybrid+3+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/2.3\" CMOS",
            "fov_deg": 155,
            "format": "4K/Analog",
            "tvl": 1200,
            "voltage_range": "6-21V"
        }
    },
    {
        "id": "foxeer-razer-nano-4-cam",
        "category": "camera",
        "name": "Razer Nano 4 Analog Camera",
        "brand": "Foxeer",
        "price_php": 1176,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Razer+Nano+4+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "video_system": "analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "dji-o4-lite-air-unit-cam",
        "category": "camera",
        "name": "O4 Lite Air Unit Camera",
        "brand": "DJI",
        "price_php": 8960,
        "weight_g": 19,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+O4+Lite+Air+Unit+Camera",
        "color": "#e0e0e0",
        "specs": {
            "sensor": "1/1.3\" CMOS",
            "fov_deg": 155,
            "format": "4:3",
            "video_system": "DJI O4",
            "resolution": "1080p60",
            "latency_ms": 20
        }
    },
    # ========== VIDEO TRANSMITTERS ==========
    {
        "id": "walksnail-avatar-hd-v2-vtx",
        "category": "vtx",
        "name": "Avatar HD V2 VTX",
        "brand": "Walksnail",
        "price_php": 6720,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Walksnail+Avatar+HD+V2+VTX",
        "color": "#111111",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Walksnail",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "U.FL",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "hdzero-freestyle-v7-vtx",
        "category": "vtx",
        "name": "Freestyle V7 VTX",
        "brand": "HDZero",
        "price_php": 5600,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Freestyle+V7+VTX",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 400,
            "protocol": "HDZero",
            "bands": "5.8GHz",
            "voltage_range": "6-26V",
            "connector": "U.FL",
            "video_system": "HDZero"
        }
    },
    {
        "id": "dji-o4-lite-air-unit-vtx",
        "category": "vtx",
        "name": "O4 Lite Air Unit VTX",
        "brand": "DJI",
        "price_php": 8960,
        "weight_g": 19,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+O4+Lite+Air+Unit+VTX",
        "color": "#e0e0e0",
        "specs": {
            "power_mw_max": 900,
            "protocol": "DJI O4",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "U.FL",
            "video_system": "DJI O4"
        }
    },
    {
        "id": "akk-fx3-ultimate-1600mw-vtx",
        "category": "vtx",
        "name": "FX3 Ultimate 1600mW VTX",
        "brand": "AKK",
        "price_php": 1064,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=AKK+FX3+Ultimate+1600mW+VTX",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },
    {
        "id": "tbs-unify-evo-hv-vtx",
        "category": "vtx",
        "name": "Unify EVO HV VTX",
        "brand": "TBS",
        "price_php": 4032,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/search?q=TBS+Unify+EVO+HV+VTX",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 800,
            "protocol": "SmartAudio",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "speedybee-tx800-v2-vtx",
        "category": "vtx",
        "name": "TX800 V2 VTX",
        "brand": "SpeedyBee",
        "price_php": 1512,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+TX800+V2+VTX",
        "color": "#111111",
        "specs": {
            "power_mw_max": 800,
            "protocol": "SmartAudio",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },
    # ========== BATTERIES ==========
    {
        "id": "cnhl-black-series-v2-1400mah-6s",
        "category": "battery",
        "name": "Black Series V2 1400mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1848,
        "weight_g": 246,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+V2+1400mAh+6S",
        "color": "#111111",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-r-line-v6-1300mah-6s",
        "category": "battery",
        "name": "R-Line V6 1300mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2296,
        "weight_g": 235,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V6+1300mAh+6S",
        "color": "#000033",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gaoneng-gnb-4s-1300mah-120c-v2",
        "category": "battery",
        "name": "GNB 1300mAh 4S 120C V2",
        "brand": "Gaoneng",
        "price_php": 1176,
        "weight_g": 160,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gaoneng+GNB+1300mAh+4S+120C+V2",
        "color": "#1a1a1a",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 120,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "rdq-series-4s-1500mah-100c",
        "category": "battery",
        "name": "RDQ Series 1500mAh 4S 100C",
        "brand": "RDQ",
        "price_php": 952,
        "weight_g": 172,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=RDQ+Series+1500mAh+4S+100C",
        "color": "#1a1a1a",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "cnhl-mini-black-series-6s-1300mah-v2",
        "category": "battery",
        "name": "Mini Black Series V2 1300mAh 6S",
        "brand": "CNHL",
        "price_php": 1736,
        "weight_g": 225,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Mini+Black+Series+V2+1300mAh+6S",
        "color": "#111111",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "ovonic-4s-1500mah-100c-v2",
        "category": "battery",
        "name": "Ovonic 1500mAh 4S 100C V2",
        "brand": "Ovonic",
        "price_php": 896,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ovonic+1500mAh+4S+100C+V2",
        "color": "#1a1a1a",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gensace-tattu-6s-1550mah-130c",
        "category": "battery",
        "name": "Gens Ace Tattu 1550mAh 6S 130C",
        "brand": "Gens Ace",
        "price_php": 2072,
        "weight_g": 250,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gens+Ace+Tattu+1550mAh+6S+130C",
        "color": "#000033",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1550,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    # ========== RC RECEIVERS ==========
    {
        "id": "radiomaster-rp3-v2-elrs-nano-rx",
        "category": "receiver",
        "name": "RP3 V2 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 896,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RadioMaster+RP3+V2+ELRS+Nano+Receiver",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-ep2-v2-elrs-rx",
        "category": "receiver",
        "name": "EP2 V2 ELRS Receiver",
        "brand": "Happymodel",
        "price_php": 728,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+EP2+V2+ELRS+Receiver",
        "color": "#1a1a1a",
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
        "price_php": 1288,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/search?q=TBS+Crossfire+Nano+RX+V6",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 900,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "betafpv-elrs-2.4g-super-d-rx",
        "category": "receiver",
        "name": "ELRS 2.4G Super D Receiver",
        "brand": "BetaFPV",
        "price_php": 952,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=BetaFPV+ELRS+2.4G+Super+D+Receiver",
        "color": "#00aaff",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "iflight-elrs-2.4g-pro-rx",
        "category": "receiver",
        "name": "ELRS 2.4G Pro Receiver",
        "brand": "iFlight",
        "price_php": 840,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+ELRS+2.4G+Pro+Receiver",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "radiomaster-rp1-v3-900-elrs-rx",
        "category": "receiver",
        "name": "RP1 V3 900MHz ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 1064,
        "weight_g": 2.1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RadioMaster+RP1+V3+900MHz+ELRS+Receiver",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 900,
            "diversity": True,
            "telemetry": True
        }
    },
    # ========== GPS MODULES ==========
    {
        "id": "matek-m10q-5883-v6-gps",
        "category": "gps",
        "name": "M10Q-5883 V6 GPS",
        "brand": "Matek",
        "price_php": 1568,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-5883+V6+GPS",
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
        "id": "holybro-m10-gps-module-v2",
        "category": "gps",
        "name": "M10 GPS Module V2",
        "brand": "Holybro",
        "price_php": 1848,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+M10+GPS+Module+V2",
        "color": "#0a4d8f",
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
        "id": "beitian-bn-880q-v2-gps",
        "category": "gps",
        "name": "BN-880Q V2 GPS + Compass",
        "brand": "Beitian",
        "price_php": 896,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880Q+V2+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 5,
            "fix_time_s": 8,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "hglrc-m100-5883-gps",
        "category": "gps",
        "name": "M100 5883 GPS Module",
        "brand": "HGLRC",
        "price_php": 1120,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+M100+5883+GPS+Module",
        "color": "#111827",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 6,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "radiolink-se100-gps",
        "category": "gps",
        "name": "SE100 GPS Module",
        "brand": "Radiolink",
        "price_php": 1008,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Radiolink+SE100+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 7,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    # ========== ANTENNAS ==========
    {
        "id": "truerc-abomination-v3-sma",
        "category": "antenna",
        "name": "Abomination V3 5.8GHz SMA Antenna",
        "brand": "TrueRC",
        "price_php": 1176,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Abomination+V3+5.8GHz+SMA+Antenna",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 6,
            "type": "patch"
        }
    },
    {
        "id": "foxeer-lollipop-4-plus-v5-sma",
        "category": "antenna",
        "name": "Lollipop 4 Plus V5 SMA Antenna",
        "brand": "Foxeer",
        "price_php": 392,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Lollipop+4+Plus+V5+SMA+Antenna",
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
        "id": "rushfpv-cherry-v3-sma",
        "category": "antenna",
        "name": "Cherry V3 5.8GHz SMA Antenna",
        "brand": "Rush",
        "price_php": 644,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Rush+Cherry+V3+5.8GHz+SMA+Antenna",
        "color": "#121212",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.6,
            "type": "cloverleaf"
        }
    },
    {
        "id": "immersionrc-spironet-v2-sma",
        "category": "antenna",
        "name": "SpiroNET V2 5.8GHz SMA Antenna",
        "brand": "ImmersionRC",
        "price_php": 728,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SpiroNET+V2+5.8GHz+SMA+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.2,
            "type": "cloverleaf"
        }
    },
    {
        "id": "hglrc-mushroom-v3-sma",
        "category": "antenna",
        "name": "5.8GHz Mushroom V3 Antenna SMA",
        "brand": "HGLRC",
        "price_php": 350,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+5.8GHz+Mushroom+V3+Antenna+SMA",
        "color": "#111122",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "LHCP",
            "connector": "SMA",
            "gain_dbi": 1.6,
            "type": "omnidirectional"
        }
    },
    {
        "id": "menace-rc-havoc-sma",
        "category": "antenna",
        "name": "Havoc 5.8GHz SMA Antenna",
        "brand": "Menace RC",
        "price_php": 560,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Menace+RC+Havoc+5.8GHz+SMA+Antenna",
        "color": "#1a1a1a",
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
