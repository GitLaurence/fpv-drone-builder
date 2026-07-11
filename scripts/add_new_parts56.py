"""Batch 56: adds real, currently-shipping FPV parts across all 11 categories
that were missing from the catalog, following the existing schema and
buy_url conventions (retailer/brand search URLs, never dead product links).
"""
import json

NEW_PARTS = [
    # ========== FRAME ==========
    {
        "id": "geprc-crocodile-baby5-frame",
        "category": "frame",
        "name": "Crocodile Baby5 5\" Frame Kit",
        "brand": "GEPRC",
        "price_php": 3024,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=Crocodile+Baby5+5+Frame",
        "color": "#141414",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "flywoo-hex-nano-baby-quad-frame",
        "category": "frame",
        "name": "Hex-Nano Baby Quad 2.5\" Frame Kit",
        "brand": "Flywoo",
        "price_php": 1288,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Hex-Nano+Baby+Quad+2.5+Frame",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 110,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber"
        }
    },
    {
        "id": "iflight-chimera7-pro-frame",
        "category": "frame",
        "name": "Chimera7 Pro 7\" Frame Kit",
        "brand": "iFlight",
        "price_php": 3696,
        "weight_g": 118,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=Chimera7+Pro+7+Frame",
        "color": "#111111",
        "specs": {
            "size_mm": 320,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },

    # ========== MOTOR ==========
    {
        "id": "tmotor-velox-v2306-v3-1900kv",
        "category": "motor",
        "name": "Velox V2306 V3 1900KV",
        "brand": "T-Motor",
        "price_php": 1064,
        "weight_g": 29.5,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=Velox+V2306+V3+1900KV",
        "color": "#292929",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "max_voltage_s": 6
        }
    },
    {
        "id": "brotherhobby-avenger-2807-5-1300kv",
        "category": "motor",
        "name": "Avenger 2807.5 1300KV",
        "brand": "BrotherHobby",
        "price_php": 1288,
        "weight_g": 42,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=Avenger+2807.5+1300KV",
        "color": "#333333",
        "specs": {
            "kv": 1300,
            "stator_size": "2807.5",
            "motor_mount_mm": 25.5,
            "max_voltage_s": 6
        }
    },
    {
        "id": "hglrc-speed-2207-5-1900kv",
        "category": "motor",
        "name": "SPEED 2207.5 1900KV",
        "brand": "HGLRC",
        "price_php": 896,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=SPEED+2207.5+1900KV",
        "color": "#1f1f1f",
        "specs": {
            "kv": 1900,
            "stator_size": "2207.5",
            "motor_mount_mm": 16,
            "max_voltage_s": 6
        }
    },

    # ========== ESC ==========
    {
        "id": "tmotor-f55a-pro-ii-4in1",
        "category": "esc",
        "name": "F55A PRO II 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 2408,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F55A+PRO+II+4-in-1+ESC",
        "color": "#141414",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 30.5
        }
    },
    {
        "id": "iflight-succex-e-45a-4in1",
        "category": "esc",
        "name": "SucceX-E 45A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 1680,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=SucceX-E+45A+4-in-1+ESC",
        "color": "#0f0f0f",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 25.5
        }
    },

    # ========== FLIGHT CONTROLLER ==========
    {
        "id": "speedybee-f405-wing-mini-fc",
        "category": "fc",
        "name": "F405 Wing Mini Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 1512,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=F405+Wing+Mini+Flight+Controller",
        "color": "#131313",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },
    {
        "id": "matek-f722-wing-fc",
        "category": "fc",
        "name": "F722-WING Flight Controller",
        "brand": "Matek",
        "price_php": 2296,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F722-WING+Flight+Controller",
        "color": "#0a0a0a",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5
        }
    },

    # ========== PROPELLER ==========
    {
        "id": "gemfan-hurricane-3018-prop",
        "category": "propeller",
        "name": "Hurricane 3018 Tri-Blade Prop",
        "brand": "Gemfan",
        "price_php": 140,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+3018",
        "color": "#383838",
        "specs": {
            "diameter_inch": 3,
            "pitch": 1.8,
            "blade_count": 3,
            "shaft_mm": 1.5
        }
    },
    {
        "id": "hqprop-r38-5x2-5x3-prop",
        "category": "propeller",
        "name": "R38.5X2.5X3 Race Tri-Blade Prop",
        "brand": "HQProp",
        "price_php": 196,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+R38.5X2.5X3",
        "color": "#454545",
        "specs": {
            "diameter_inch": 5,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },

    # ========== CAMERA ==========
    {
        "id": "runcam-phoenix-2-nano-camera",
        "category": "camera",
        "name": "Phoenix 2 Nano FPV Camera",
        "brand": "RunCam",
        "price_php": 1064,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Phoenix+2+Nano+FPV+Camera",
        "color": "#0e0e0e",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "foxeer-toothless-3-nano-camera",
        "category": "camera",
        "name": "Toothless 3 Nano FPV Camera",
        "brand": "Foxeer",
        "price_php": 1176,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Toothless+3+Nano+FPV+Camera",
        "color": "#151515",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "analog",
            "video_system": "analog"
        }
    },

    # ========== VTX ==========
    {
        "id": "iflight-forcevtx-2-1w",
        "category": "vtx",
        "name": "ForceVTX 2 1W",
        "brand": "iFlight",
        "price_php": 1848,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=ForceVTX+2+1W",
        "color": "#101010",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },
    {
        "id": "speedybee-tx800-vtx",
        "category": "vtx",
        "name": "TX800 800mW VTX",
        "brand": "SpeedyBee",
        "price_php": 1400,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=TX800+800mW+VTX",
        "color": "#0c0c0c",
        "specs": {
            "power_mw_max": 800,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },

    # ========== BATTERY ==========
    {
        "id": "cnhl-black-series-1300-6s-battery",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1904,
        "weight_g": 232,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1300mAh+6S+100C",
        "color": "#262626",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60"
        }
    },
    {
        "id": "tattu-rline-v5-850-4s-battery",
        "category": "battery",
        "name": "R-Line V5.0 850mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1568,
        "weight_g": 108,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5.0+850mAh+4S+130C",
        "color": "#212121",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 850,
            "c_rating": 130,
            "connector": "XT30"
        }
    },

    # ========== RECEIVER ==========
    {
        "id": "happymodel-ep2-elrs-rx",
        "category": "receiver",
        "name": "EP2 ELRS 2.4GHz Receiver",
        "brand": "HappyModel",
        "price_php": 784,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ELRS+2.4GHz+Receiver",
        "color": "#181818",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400
        }
    },
    {
        "id": "tbs-crossfire-diversity-nano-rx",
        "category": "receiver",
        "name": "Crossfire Diversity Nano RX",
        "brand": "TBS",
        "price_php": 1904,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Diversity+Nano+RX",
        "color": "#0d0d0d",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915
        }
    },

    # ========== GPS ==========
    {
        "id": "holybro-m9n-gps",
        "category": "gps",
        "name": "M9N GPS Module",
        "brand": "Holybro",
        "price_php": 1568,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=M9N+GPS+Module",
        "color": "#111111",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-gps",
        "category": "gps",
        "name": "M10Q GPS Module",
        "brand": "Matek",
        "price_php": 1064,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q+GPS+Module",
        "color": "#0e0e0e",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 15,
            "compass": False,
            "connector": "JST-SH 6-pin"
        }
    },

    # ========== ANTENNA ==========
    {
        "id": "truerc-abomination-antenna",
        "category": "antenna",
        "name": "Abomination 5.8GHz RHCP SMA",
        "brand": "TrueRC",
        "price_php": 1120,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Abomination+5.8GHz+RHCP",
        "color": "#101010",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 3.3,
            "type": "cloverleaf"
        }
    },
    {
        "id": "foxeer-lollipop-4-antenna",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP SMA",
        "brand": "Foxeer",
        "price_php": 476,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Lollipop+4+5.8GHz+RHCP",
        "color": "#1c1c1c",
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
