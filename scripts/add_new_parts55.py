"""Batch 55: adds real, currently-shipping FPV parts across all 11 categories
that were missing from the catalog, following the existing schema and
buy_url conventions (retailer/brand search URLs, never dead product links).
"""
import json

NEW_PARTS = [
    # ========== FRAME ==========
    {
        "id": "geprc-mark5-hd-frame",
        "category": "frame",
        "name": "Mark5 HD Frame Kit",
        "brand": "GEPRC",
        "price_php": 3360,
        "weight_g": 108,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Mark5+HD+Frame",
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
        "id": "armattan-marmotte-6-frame",
        "category": "frame",
        "name": "Marmotte 6\" Frame Kit",
        "brand": "Armattan",
        "price_php": 6944,
        "weight_g": 122,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Marmotte+6+Frame",
        "color": "#1b1b1b",
        "specs": {
            "size_mm": 265,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "flywoo-firefly-baby-quad-1s-frame",
        "category": "frame",
        "name": "Firefly Baby Quad 1S Frame",
        "brand": "Flywoo",
        "price_php": 728,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Firefly+Baby+Quad+1S+Frame",
        "color": "#0f0f0f",
        "specs": {
            "size_mm": 65,
            "motor_mount_mm": 9,
            "prop_clearance_inch": 1.6,
            "stack_mount_mm": 16,
            "material": "carbon fiber"
        }
    },
    {
        "id": "iflight-nazgul5-v3-frame",
        "category": "frame",
        "name": "Nazgul5 V3 Frame Kit",
        "brand": "iFlight",
        "price_php": 2856,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=Nazgul5+V3+Frame",
        "color": "#131313",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },
    {
        "id": "diatone-roma-f5-frame",
        "category": "frame",
        "name": "Roma F5 Frame Kit",
        "brand": "Diatone",
        "price_php": 3808,
        "weight_g": 96,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Roma+F5+Frame",
        "color": "#191919",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber"
        }
    },

    # ========== MOTOR ==========
    {
        "id": "iflight-xing2-1806-4200kv",
        "category": "motor",
        "name": "XING2 1806 4200KV",
        "brand": "iFlight",
        "price_php": 728,
        "weight_g": 14.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=XING2+1806+4200KV",
        "color": "#232323",
        "specs": {
            "kv": 4200,
            "stator_size": "1806",
            "motor_mount_mm": 12,
            "max_voltage_s": 4
        }
    },
    {
        "id": "tmotor-f60-pro-iv-2500kv",
        "category": "motor",
        "name": "F60 PRO IV 2500KV",
        "brand": "T-Motor",
        "price_php": 896,
        "weight_g": 12.8,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F60+PRO+IV+2500KV",
        "color": "#2d2d2d",
        "specs": {
            "kv": 2500,
            "stator_size": "1408",
            "motor_mount_mm": 9,
            "max_voltage_s": 4
        }
    },
    {
        "id": "brotherhobby-avenger-2812-800kv",
        "category": "motor",
        "name": "Avenger 2812 800KV",
        "brand": "BrotherHobby",
        "price_php": 1512,
        "weight_g": 52,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=Avenger+2812+800KV",
        "color": "#303030",
        "specs": {
            "kv": 800,
            "stator_size": "2812",
            "motor_mount_mm": 25.5,
            "max_voltage_s": 8
        }
    },
    {
        "id": "flywoo-nin-1404-4200kv",
        "category": "motor",
        "name": "NIN 1404 4200KV",
        "brand": "Flywoo",
        "price_php": 616,
        "weight_g": 11.2,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=NIN+1404+4200KV",
        "color": "#111111",
        "specs": {
            "kv": 4200,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "max_voltage_s": 4
        }
    },
    {
        "id": "emax-rsii-2306-1900kv",
        "category": "motor",
        "name": "RSII 2306 1900KV",
        "brand": "EMAX",
        "price_php": 1008,
        "weight_g": 33.5,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com/search?q=RSII+2306+1900KV",
        "color": "#1c1c1c",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
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
        "price_php": 2632,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F55A+PRO+II+4-in-1+ESC",
        "color": "#0e0e0e",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 30.5
        }
    },
    {
        "id": "iflight-blitz-e55-4in1-esc",
        "category": "esc",
        "name": "BLITZ E55 55A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 2408,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=BLITZ+E55+55A+4-in-1+ESC",
        "color": "#181818",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DShot600",
            "form_factor_mm": 30.5
        }
    },
    {
        "id": "speedybee-bls-50a-4in1-esc",
        "category": "esc",
        "name": "BLS 50A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2128,
        "weight_g": 10,
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
    {
        "id": "geprc-taker-45a-4in1-esc",
        "category": "esc",
        "name": "Taker F4 45A 4-in-1 ESC",
        "brand": "GEPRC",
        "price_php": 1792,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Taker+F4+45A+4-in-1+ESC",
        "color": "#141414",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 4,
            "protocol": "DShot600",
            "form_factor_mm": 20
        }
    },
    {
        "id": "hglrc-zeus-40a-4in1-esc",
        "category": "esc",
        "name": "Zeus 40A F4 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 1624,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Zeus+40A+F4+4-in-1+ESC",
        "color": "#0d0d0d",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 4,
            "protocol": "DShot600",
            "form_factor_mm": 20
        }
    },

    # ========== FLIGHT CONTROLLER ==========
    {
        "id": "geprc-taker-g4-f411-fc",
        "category": "fc",
        "name": "Taker G4 F411 AIO Flight Controller",
        "brand": "GEPRC",
        "price_php": 1736,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Taker+G4+F411+Flight+Controller",
        "color": "#101010",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },
    {
        "id": "diatone-mamba-f405-mk4-fc",
        "category": "fc",
        "name": "Mamba F405 Mk4 Flight Controller",
        "brand": "Diatone",
        "price_php": 2296,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Mamba+F405+Mk4+Flight+Controller",
        "color": "#151515",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5
        }
    },
    {
        "id": "betafpv-f4-1s-brushless-fc",
        "category": "fc",
        "name": "F4 1S 12A AIO Brushless FC",
        "brand": "BetaFPV",
        "price_php": 1400,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=F4+1S+12A+AIO+Brushless+Flight+Controller",
        "color": "#202020",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 16,
            "stack_mount_mm": 16
        }
    },
    {
        "id": "jhemcu-ghf411aio-fc",
        "category": "fc",
        "name": "GHF411AIO Flight Controller",
        "brand": "JHEMCU",
        "price_php": 1288,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=JHEMCU+GHF411AIO+Flight+Controller",
        "color": "#121212",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20
        }
    },

    # ========== PROPELLER ==========
    {
        "id": "gemfan-hurricane-51433-prop",
        "category": "propeller",
        "name": "Hurricane 51433 Tri-Blade Prop",
        "brand": "Gemfan",
        "price_php": 210,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51433",
        "color": "#3a3a3a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.33,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "hqprop-t3x2x3-micro-prop",
        "category": "propeller",
        "name": "T3X2X3 Micro Tri-Blade Prop",
        "brand": "HQProp",
        "price_php": 140,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+T3X2X3",
        "color": "#414141",
        "specs": {
            "diameter_inch": 3,
            "pitch": 2,
            "blade_count": 3,
            "shaft_mm": 1.5
        }
    },
    {
        "id": "ethix-s5-wave-prop",
        "category": "propeller",
        "name": "S5 Wave 5\" Tri-Blade Prop",
        "brand": "Ethix",
        "price_php": 280,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Ethix+S5+Wave+Prop",
        "color": "#4d4d4d",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.9,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "dalprop-cyclone-t5040c",
        "category": "propeller",
        "name": "Cyclone T5040C Tri-Blade Prop",
        "brand": "DALPROP",
        "price_php": 168,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DALPROP+Cyclone+T5040C",
        "color": "#474747",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },

    # ========== CAMERA ==========
    {
        "id": "runcam-phoenix-2-camera",
        "category": "camera",
        "name": "Phoenix 2 FPV Camera",
        "brand": "RunCam",
        "price_php": 1400,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Phoenix+2+FPV+Camera",
        "color": "#0f0f0f",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "foxeer-micro-razer-2-camera",
        "category": "camera",
        "name": "Micro Razer 2 Camera",
        "brand": "Foxeer",
        "price_php": 1064,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Micro+Razer+2+Camera",
        "color": "#101010",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "analog",
            "video_system": "analog"
        }
    },
    {
        "id": "caddx-nebula-pro-nano-camera",
        "category": "camera",
        "name": "Nebula Pro Nano Digital Camera",
        "brand": "Caddx",
        "price_php": 3248,
        "weight_g": 5.7,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Nebula+Pro+Nano+Digital+Camera",
        "color": "#181818",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "digital",
            "video_system": "hdzero"
        }
    },
    {
        "id": "walksnail-avatar-hd-nano-camera",
        "category": "camera",
        "name": "Avatar HD Nano Kit Camera",
        "brand": "Walksnail",
        "price_php": 3696,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+Nano+Kit+Camera",
        "color": "#0c0c0c",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 145,
            "format": "digital",
            "video_system": "walksnail"
        }
    },

    # ========== VTX ==========
    {
        "id": "rushfpv-cherry-2-5w-vtx",
        "category": "vtx",
        "name": "Cherry 2.5W VTX",
        "brand": "RushFPV",
        "price_php": 3416,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Cherry+2.5W+VTX",
        "color": "#1e1e1e",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },
    {
        "id": "tbs-unify-pro32-hv-vtx",
        "category": "vtx",
        "name": "Unify Pro32 HV VTX",
        "brand": "TBS",
        "price_php": 4032,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro32+HV+VTX",
        "color": "#101010",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },
    {
        "id": "foxeer-whoopa-0-5w-vtx",
        "category": "vtx",
        "name": "Whoopa 0.5W VTX",
        "brand": "Foxeer",
        "price_php": 728,
        "weight_g": 2.4,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Whoopa+0.5W+VTX",
        "color": "#131313",
        "specs": {
            "power_mw_max": 500,
            "protocol": "SmartAudio",
            "video_system": "analog"
        }
    },

    # ========== BATTERY ==========
    {
        "id": "cnhl-black-series-1300-4s-battery",
        "category": "battery",
        "name": "Black Series 1300mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1568,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1300mAh+4S+100C",
        "color": "#282828",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60"
        }
    },
    {
        "id": "tattu-rline-v4-1550-6s-battery",
        "category": "battery",
        "name": "R-Line V4.0 1550mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2632,
        "weight_g": 265,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V4.0+1550mAh+6S+130C",
        "color": "#232323",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1550,
            "c_rating": 130,
            "connector": "XT60"
        }
    },
    {
        "id": "gnb-450-3s-battery",
        "category": "battery",
        "name": "450mAh 3S 80C",
        "brand": "GNB",
        "price_php": 448,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+450mAh+3S+80C",
        "color": "#2c2c2c",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 450,
            "c_rating": 80,
            "connector": "XT30"
        }
    },

    # ========== RECEIVER ==========
    {
        "id": "happymodel-elrs-ep1-rx",
        "category": "receiver",
        "name": "EP1 ExpressLRS Receiver",
        "brand": "HappyModel",
        "price_php": 588,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP1+ExpressLRS+Receiver",
        "color": "#1f1f1f",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400
        }
    },
    {
        "id": "radiomaster-rp1-elrs-nano-rx",
        "category": "receiver",
        "name": "RP1 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 728,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RP1+ELRS+Nano+Receiver",
        "color": "#191919",
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
        "price_php": 1736,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Diversity+Nano+RX",
        "color": "#0f0f0f",
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
        "price_php": 2464,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=M9N+GPS+Module",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 15,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "betafpv-m8-gps",
        "category": "gps",
        "name": "M8 GPS Module",
        "brand": "BetaFPV",
        "price_php": 728,
        "weight_g": 3.8,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=M8+GPS+Module",
        "color": "#151515",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 22,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },

    # ========== ANTENNA ==========
    {
        "id": "rushfpv-cherry-sma-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz RHCP SMA",
        "brand": "RushFPV",
        "price_php": 672,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Cherry+5.8GHz+RHCP+Antenna",
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
        "id": "immersionrc-spironet-antenna",
        "category": "antenna",
        "name": "SpiroNET 5.8GHz RHCP SMA",
        "brand": "ImmersionRC",
        "price_php": 896,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SpiroNET+5.8GHz+RHCP",
        "color": "#0d0d0d",
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
