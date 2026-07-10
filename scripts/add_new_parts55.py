"""Batch 55: adds real, currently-shipping FPV parts across all 11 categories
that were missing from the catalog, following the existing schema and
buy_url conventions (retailer/brand search URLs, never dead product links).
"""
import json

NEW_PARTS = [
    # ========== FRAME ==========
    {
        "id": "impulserc-apex-5-frame",
        "category": "frame",
        "name": "Apex 5\" Frame Kit",
        "brand": "ImpulseRC",
        "price_php": 5600,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImpulseRC+Apex+5+Frame",
        "color": "#161616",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "flywoo-explorer-lr4-v2-frame",
        "category": "frame",
        "name": "Explorer LR4 V2 7\" Frame Kit",
        "brand": "Flywoo",
        "price_php": 3360,
        "weight_g": 112,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Explorer+LR4+V2+7+Frame",
        "color": "#0e0e0e",
        "specs": {
            "size_mm": 320,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "geprc-mark5-hd-frame",
        "category": "frame",
        "name": "Mark5 HD 5\" Frame Kit",
        "brand": "GEPRC",
        "price_php": 3808,
        "weight_g": 101,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=Mark5+HD+5+Frame",
        "color": "#121212",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "armattan-marmotte-6-frame",
        "category": "frame",
        "name": "Marmotte 6\" Frame Kit",
        "brand": "Armattan",
        "price_php": 7280,
        "weight_g": 122,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Marmotte+6+Frame",
        "color": "#1a1a1a",
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
        "id": "tmotor-f80-pro-v-2408-5-1500kv",
        "category": "motor",
        "name": "F80 Pro V 2408.5 1500KV",
        "brand": "T-Motor",
        "price_php": 1400,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F80+Pro+V+2408.5+1500KV",
        "color": "#2c2c2c",
        "specs": {
            "kv": 1500,
            "stator_size": "2408.5",
            "motor_mount_mm": 25.5,
            "max_voltage_s": 6
        }
    },
    {
        "id": "iflight-xing2-2306-1700kv",
        "category": "motor",
        "name": "XING2 2306 1700KV",
        "brand": "iFlight",
        "price_php": 952,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=XING2+2306+1700KV",
        "color": "#242424",
        "specs": {
            "kv": 1700,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "max_voltage_s": 6
        }
    },
    {
        "id": "brotherhobby-avenger-v4-2207-5-2100kv",
        "category": "motor",
        "name": "Avenger V4 2207.5 2100KV",
        "brand": "BrotherHobby",
        "price_php": 1008,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=Avenger+V4+2207.5+2100KV",
        "color": "#303030",
        "specs": {
            "kv": 2100,
            "stator_size": "2207.5",
            "motor_mount_mm": 16,
            "max_voltage_s": 4
        }
    },
    {
        "id": "flywoo-nin-1404-4200kv",
        "category": "motor",
        "name": "NIN 1404 4200KV",
        "brand": "Flywoo",
        "price_php": 616,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=NIN+1404+4200KV",
        "color": "#0d0d0d",
        "specs": {
            "kv": 4200,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "max_voltage_s": 4
        }
    },

    # ========== ESC ==========
    {
        "id": "holybro-tekko32-f4-50a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 2296,
        "weight_g": 10.5,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Tekko32+F4+50A+4-in-1+ESC",
        "color": "#101010",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 25.5
        }
    },
    {
        "id": "geprc-taker-g4-35a-4in1",
        "category": "esc",
        "name": "TAKER G4 35A 4-in-1 ESC",
        "brand": "GEPRC",
        "price_php": 1568,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=TAKER+G4+35A+4-in-1+ESC",
        "color": "#0f0f0f",
        "specs": {
            "amp_rating": 35,
            "input_voltage_s": 4,
            "protocol": "DShot600",
            "form_factor_mm": 20
        }
    },
    {
        "id": "diatone-mamba-f35-35a-4in1",
        "category": "esc",
        "name": "Mamba F35 35A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 1456,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Mamba+F35+35A+4-in-1+ESC",
        "color": "#161616",
        "specs": {
            "amp_rating": 35,
            "input_voltage_s": 4,
            "protocol": "DShot600",
            "form_factor_mm": 20
        }
    },
    {
        "id": "speedybee-bls-50a-4in1",
        "category": "esc",
        "name": "BLS 50A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2072,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=BLS+50A+4-in-1+ESC",
        "color": "#0a0a0a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 30.5
        }
    },

    # ========== FLIGHT CONTROLLER ==========
    {
        "id": "geprc-taker-f411-20a-aio",
        "category": "fc",
        "name": "TAKER F411 20A AIO Flight Controller",
        "brand": "GEPRC",
        "price_php": 1848,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=TAKER+F411+20A+AIO+Flight+Controller",
        "color": "#131313",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },
    {
        "id": "flywoo-goku-gn745-v2-fc",
        "category": "fc",
        "name": "GOKU GN745 V2 Flight Controller",
        "brand": "Flywoo",
        "price_php": 2688,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=GOKU+GN745+V2+Flight+Controller",
        "color": "#0c0c0c",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5
        }
    },
    {
        "id": "holybro-kakute-f4-aio-v3",
        "category": "fc",
        "name": "Kakute F4 AIO V3 Flight Controller",
        "brand": "Holybro",
        "price_php": 2128,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Kakute+F4+AIO+V3+Flight+Controller",
        "color": "#191919",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5
        }
    },
    {
        "id": "hglrc-zeus-f435-fc",
        "category": "fc",
        "name": "Zeus F435 Flight Controller",
        "brand": "HGLRC",
        "price_php": 1736,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Zeus+F435+Flight+Controller",
        "color": "#0e0e0e",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },

    # ========== PROPELLER ==========
    {
        "id": "gemfan-hurricane-51466-prop",
        "category": "propeller",
        "name": "Hurricane 51466 Tri-Blade Prop",
        "brand": "Gemfan",
        "price_php": 168,
        "weight_g": 4.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466",
        "color": "#3a3a3a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "hqprop-dp6x4-5x3-prop",
        "category": "propeller",
        "name": "DP6X4.5X3 6-inch Tri-Blade Prop",
        "brand": "HQProp",
        "price_php": 224,
        "weight_g": 6.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP6X4.5X3",
        "color": "#414141",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "ethix-s4-lite-prop",
        "category": "propeller",
        "name": "S4 Lite 4\" Tri-Blade Prop",
        "brand": "Ethix",
        "price_php": 196,
        "weight_g": 2.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+S4+Lite+4+Propeller",
        "color": "#f2f2f2",
        "specs": {
            "diameter_inch": 4,
            "pitch": 3,
            "blade_count": 3,
            "shaft_mm": 4
        }
    },

    # ========== CAMERA ==========
    {
        "id": "foxeer-razer-nano-1200tvl-camera",
        "category": "camera",
        "name": "Razer Nano 1200TVL Camera",
        "brand": "Foxeer",
        "price_php": 1120,
        "weight_g": 3.2,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Razer+Nano+1200TVL+Camera",
        "color": "#101010",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 165,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "caddx-ratel-2-pro-camera",
        "category": "camera",
        "name": "Ratel 2 Pro FPV Camera",
        "brand": "Caddx",
        "price_php": 1680,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ratel+2+Pro+FPV+Camera",
        "color": "#141414",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "runcam-nano-4-camera",
        "category": "camera",
        "name": "Nano 4 FPV Camera",
        "brand": "RunCam",
        "price_php": 896,
        "weight_g": 2.6,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Nano+4+FPV+Camera",
        "color": "#0b0b0b",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "analog",
            "video_system": "analog"
        }
    },

    # ========== VTX ==========
    {
        "id": "tbs-unify-evo-nano-500mw-vtx",
        "category": "vtx",
        "name": "Unify Evo Nano 500mW VTX",
        "brand": "TBS",
        "price_php": 2464,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Evo+Nano+500mW+VTX",
        "color": "#0f0f0f",
        "specs": {
            "power_mw_max": 500,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },
    {
        "id": "hglrc-titan-vtx-600mw",
        "category": "vtx",
        "name": "Titan 600mW VTX",
        "brand": "HGLRC",
        "price_php": 952,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Titan+600mW+VTX",
        "color": "#0d0d0d",
        "specs": {
            "power_mw_max": 600,
            "protocol": "TrampHV",
            "video_system": "analog"
        }
    },
    {
        "id": "iflight-forcevtx-1w",
        "category": "vtx",
        "name": "ForceVTX 1W",
        "brand": "iFlight",
        "price_php": 1792,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=ForceVTX+1W",
        "color": "#131313",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },

    # ========== BATTERY ==========
    {
        "id": "cnhl-ministar-1050-4s-battery",
        "category": "battery",
        "name": "MiniStar 1050mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1288,
        "weight_g": 138,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+MiniStar+1050mAh+4S+100C",
        "color": "#282828",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1050,
            "c_rating": 100,
            "connector": "XT30"
        }
    },
    {
        "id": "tattu-rline-v5-1550-6s-battery",
        "category": "battery",
        "name": "R-Line V5.0 1550mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2744,
        "weight_g": 268,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5.0+1550mAh+6S+130C",
        "color": "#232323",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1550,
            "c_rating": 130,
            "connector": "XT60"
        }
    },
    {
        "id": "gnb-1300-4s-battery",
        "category": "battery",
        "name": "1300mAh 4S 100C",
        "brand": "GNB",
        "price_php": 1176,
        "weight_g": 142,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+1300mAh+4S+100C",
        "color": "#2d2d2d",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60"
        }
    },

    # ========== RECEIVER ==========
    {
        "id": "tbs-crossfire-nano-rx-se-v2",
        "category": "receiver",
        "name": "Crossfire Nano RX SE V2",
        "brand": "TBS",
        "price_php": 1624,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+RX+SE+V2",
        "color": "#101010",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915
        }
    },
    {
        "id": "happymodel-ep1-pro-elrs-rx",
        "category": "receiver",
        "name": "EP1 Pro ELRS 2.4GHz Receiver",
        "brand": "HappyModel",
        "price_php": 672,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP1+Pro+ELRS+2.4GHz+Receiver",
        "color": "#1e1e1e",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400
        }
    },
    {
        "id": "radiomaster-rp2-elrs-rx",
        "category": "receiver",
        "name": "RP2 ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 728,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RP2+ELRS+Receiver",
        "color": "#181818",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400
        }
    },

    # ========== GPS ==========
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS + Compass",
        "brand": "Matek",
        "price_php": 1400,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-5883+GPS+Compass",
        "color": "#0c0c0c",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 15,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m10-gps",
        "category": "gps",
        "name": "Micro M10 GPS Module",
        "brand": "Holybro",
        "price_php": 1064,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Micro+M10+GPS+Module",
        "color": "#141414",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },

    # ========== ANTENNA ==========
    {
        "id": "lumenier-axii-2-pagoda-antenna",
        "category": "antenna",
        "name": "AXII 2 Pagoda 5.8GHz RHCP SMA",
        "brand": "Lumenier",
        "price_php": 896,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com/search?q=AXII+2+Pagoda+5.8GHz+RHCP",
        "color": "#0d0d0d",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.6,
            "type": "cloverleaf"
        }
    },
    {
        "id": "truerc-xair-max-antenna",
        "category": "antenna",
        "name": "X-AIR Max 5.8GHz RHCP SMA",
        "brand": "TrueRC",
        "price_php": 1288,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+X-AIR+Max+5.8GHz+RHCP",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 5.5,
            "type": "patch"
        }
    },
    {
        "id": "rushfpv-cherry-micro-antenna",
        "category": "antenna",
        "name": "Cherry Micro 5.8GHz RHCP SMA",
        "brand": "RushFPV",
        "price_php": 504,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Cherry+Micro+5.8GHz+RHCP",
        "color": "#1a1a1a",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.1,
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
