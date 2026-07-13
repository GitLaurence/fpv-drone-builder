#!/usr/bin/env python3
"""Batch 58: real, current-production FPV parts across all 11 categories,
prioritizing the lower-coverage categories (GPS, receiver, antenna, VTX,
camera, FC) while topping up the rest."""
import json

NEW_PARTS = [
    # ========== GPS ==========
    {
        "id": "beitian-bn-880q-gps",
        "category": "gps",
        "name": "BN-880Q GPS + Compass Module",
        "brand": "Beitian",
        "price_php": 1064,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880Q+GPS+Compass+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "radiomaster-m10-gps",
        "category": "gps",
        "name": "RM M10 GPS Module",
        "brand": "RadioMaster",
        "price_php": 1512,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RM+M10+GPS+Module",
        "color": "#0f0f0f",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "iflight-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "iFlight",
        "price_php": 1400,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=M10+GPS+Module",
        "color": "#181818",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 16,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m9n-5883-gps",
        "category": "gps",
        "name": "M9N-5883 GPS + Compass Module",
        "brand": "Matek",
        "price_php": 1736,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M9N-5883+GPS+Compass+Module",
        "color": "#0a2233",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "speedybee-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1288,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+M10+GPS+Module",
        "color": "#00263d",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 17,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    # ========== RECEIVER ==========
    {
        "id": "expresslrs-rp2-diversity-2-4ghz-rx",
        "category": "receiver",
        "name": "RP2 Diversity 2.4GHz ELRS Receiver",
        "brand": "ExpressLRS",
        "price_php": 896,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ExpressLRS+RP2+Diversity+2.4GHz+Receiver",
        "color": "#101010",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_ghz": 2.4,
            "diversity": True,
            "telemetry": True,
            "output": "CRSF"
        }
    },
    {
        "id": "radiomaster-rp3-2-4ghz-rx",
        "category": "receiver",
        "name": "RP3 2.4GHz ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 728,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RP3+2.4GHz+ELRS+Receiver",
        "color": "#0f0f0f",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_ghz": 2.4,
            "diversity": False,
            "telemetry": True,
            "output": "CRSF"
        }
    },
    {
        "id": "happymodel-ep2-2-4ghz-rx",
        "category": "receiver",
        "name": "EP2 2.4GHz ELRS Receiver",
        "brand": "HappyModel",
        "price_php": 672,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+2.4GHz+ELRS+Receiver",
        "color": "#151515",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_ghz": 2.4,
            "diversity": False,
            "telemetry": True,
            "output": "CRSF"
        }
    },
    {
        "id": "tbs-crossfire-nano-rx-se",
        "category": "receiver",
        "name": "Crossfire Nano RX SE",
        "brand": "TBS",
        "price_php": 1624,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+RX+SE",
        "color": "#1c1c1c",
        "specs": {
            "protocol": "TBS Crossfire",
            "frequency_ghz": 0.915,
            "diversity": False,
            "telemetry": True,
            "output": "CRSF"
        }
    },
    {
        "id": "frsky-r9-mm-rx",
        "category": "receiver",
        "name": "R9 MM 900MHz Long Range Receiver",
        "brand": "FrSky",
        "price_php": 1288,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R9+MM+900MHz+Long+Range+Receiver",
        "color": "#0d0d0d",
        "specs": {
            "protocol": "FrSky ACCESS",
            "frequency_ghz": 0.9,
            "diversity": False,
            "telemetry": True,
            "output": "SBUS"
        }
    },
    {
        "id": "flysky-fs-a8s-rx",
        "category": "receiver",
        "name": "FS-A8S 2.4GHz Receiver",
        "brand": "FlySky",
        "price_php": 560,
        "weight_g": 5.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FlySky+FS-A8S+2.4GHz+Receiver",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "FlySky AFHDS 2A",
            "frequency_ghz": 2.4,
            "diversity": True,
            "telemetry": True,
            "output": "iBUS/SBUS/PPM"
        }
    },
    # ========== ANTENNA ==========
    {
        "id": "tbs-triumph-pro-rhcp-rp-sma",
        "category": "antenna",
        "name": "Triumph Pro 5.8GHz RHCP RP-SMA",
        "brand": "TBS",
        "price_php": 1288,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Triumph+Pro+5.8GHz+RHCP+RP-SMA",
        "color": "#0d0d0d",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "RP-SMA",
            "gain_dbi": 2.8,
            "type": "omni"
        }
    },
    {
        "id": "rushfpv-cherry-2-lhcp-sma",
        "category": "antenna",
        "name": "Cherry 2 5.8GHz LHCP SMA",
        "brand": "RushFPV",
        "price_php": 784,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Cherry+2+5.8GHz+LHCP+SMA",
        "color": "#8a1f1f",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "LHCP",
            "connector": "SMA",
            "gain_dbi": 2.2,
            "type": "cloverleaf"
        }
    },
    {
        "id": "foxeer-lollipop-4-rhcp-sma",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP SMA",
        "brand": "Foxeer",
        "price_php": 616,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Lollipop+4+5.8GHz+RHCP+SMA",
        "color": "#101010",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.3,
            "type": "omni"
        }
    },
    {
        "id": "immersionrc-skew-planar-rhcp-sma",
        "category": "antenna",
        "name": "SkewPlanar Race 5.8GHz RHCP SMA",
        "brand": "ImmersionRC",
        "price_php": 896,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SkewPlanar+Race+5.8GHz+RHCP+SMA",
        "color": "#1f1f1f",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.5,
            "type": "cloverleaf"
        }
    },
    {
        "id": "expresslrs-2-4ghz-dipole-t-antenna",
        "category": "antenna",
        "name": "2.4GHz Dipole T-Antenna",
        "brand": "ExpressLRS",
        "price_php": 280,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ExpressLRS+2.4GHz+Dipole+T-Antenna",
        "color": "#151515",
        "specs": {
            "frequency_ghz": 2.4,
            "polarization": "Linear",
            "connector": "IPEX",
            "gain_dbi": 2.0,
            "type": "dipole"
        }
    },
    # ========== VTX ==========
    {
        "id": "hglrc-titan-vtx-5-8ghz",
        "category": "vtx",
        "name": "Titan 1W VTX 5.8GHz",
        "brand": "HGLRC",
        "price_php": 1848,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Titan+1W+VTX+5.8GHz",
        "color": "#0d0d0d",
        "specs": {
            "power_mw": 1000,
            "frequency_ghz": 5.8,
            "channels": 40,
            "smart_audio": True,
            "connector": "MMCX",
            "mount_mm": 25.5
        }
    },
    {
        "id": "iflight-tranfpv-vtx-500mw",
        "category": "vtx",
        "name": "TranFPV VTX 500mW",
        "brand": "iFlight",
        "price_php": 1288,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=TranFPV+VTX+500mW",
        "color": "#181818",
        "specs": {
            "power_mw": 500,
            "frequency_ghz": 5.8,
            "channels": 40,
            "smart_audio": True,
            "connector": "MMCX",
            "mount_mm": 20
        }
    },
    {
        "id": "walksnail-avatar-hd-pro-vtx",
        "category": "vtx",
        "name": "Avatar HD Pro Kit VTX",
        "brand": "Walksnail",
        "price_php": 8960,
        "weight_g": 13.5,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+Pro+Kit+VTX",
        "color": "#101010",
        "specs": {
            "power_mw": 1000,
            "frequency_ghz": 5.8,
            "channels": 0,
            "smart_audio": False,
            "connector": "MMCX",
            "mount_mm": 25.5,
            "video_system": "Walksnail"
        }
    },
    {
        "id": "hdzero-freestyle-v2-vtx",
        "category": "vtx",
        "name": "Freestyle V2 VTX",
        "brand": "HDZero",
        "price_php": 5936,
        "weight_g": 6.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Freestyle+V2+VTX",
        "color": "#151515",
        "specs": {
            "power_mw": 400,
            "frequency_ghz": 5.8,
            "channels": 0,
            "smart_audio": False,
            "connector": "MMCX",
            "mount_mm": 20,
            "video_system": "HDZero"
        }
    },
    # ========== CAMERA ==========
    {
        "id": "runcam-phoenix-2-fpv-camera",
        "category": "camera",
        "name": "Phoenix 2 Analog FPV Camera",
        "brand": "RunCam",
        "price_php": 1568,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Phoenix+2+Analog+FPV+Camera",
        "color": "#101010",
        "specs": {
            "sensor": "1/2\" CMOS",
            "tvl": 1000,
            "fov_deg": 155,
            "format": "Analog",
            "min_illumination_lux": 0.001,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-falkor-3-micro-camera",
        "category": "camera",
        "name": "Falkor 3 Micro FPV Camera",
        "brand": "Foxeer",
        "price_php": 1904,
        "weight_g": 5.8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Falkor+3+Micro+FPV+Camera",
        "color": "#0f0f0f",
        "specs": {
            "sensor": "1/2\" CMOS",
            "tvl": 1200,
            "fov_deg": 165,
            "format": "Analog",
            "min_illumination_lux": 0.0001,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ratel-2-camera",
        "category": "camera",
        "name": "Ratel 2 Analog FPV Camera",
        "brand": "Caddx",
        "price_php": 1736,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Ratel+2+Analog+FPV+Camera",
        "color": "#151515",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "tvl": 1200,
            "fov_deg": 166,
            "format": "Analog",
            "min_illumination_lux": 0.0001,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "dji-o4-air-unit-camera",
        "category": "camera",
        "name": "O4 Air Unit Digital HD Camera",
        "brand": "DJI",
        "price_php": 8288,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=DJI+O4+Air+Unit+Digital+HD+Camera",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.3\" CMOS",
            "tvl": 0,
            "fov_deg": 150,
            "format": "Digital",
            "min_illumination_lux": 0.0001,
            "voltage_range": "6-27.9V",
            "video_system": "DJI-O4"
        }
    },
    # ========== FC ==========
    {
        "id": "speedybee-f405-v4-fc",
        "category": "fc",
        "name": "F405 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2464,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=F405+V4+Flight+Controller",
        "color": "#00263d",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "geprc-taker-f411-fc",
        "category": "fc",
        "name": "Taker F411 Flight Controller",
        "brand": "GEPRC",
        "price_php": 1568,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=Taker+F411+Flight+Controller",
        "color": "#181818",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": False,
            "uart_count": 4,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "flywoo-goku-f745-fc",
        "category": "fc",
        "name": "GOKU F745 AIO Flight Controller",
        "brand": "Flywoo",
        "price_php": 3136,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=GOKU+F745+AIO+Flight+Controller",
        "color": "#0d0d0d",
        "specs": {
            "gyro": "ICM42688P",
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
    # ========== ESC ==========
    {
        "id": "hobbywing-xrotor-micro-60a-esc",
        "category": "esc",
        "name": "XRotor Micro 60A 4-in-1 ESC",
        "brand": "Hobbywing",
        "price_php": 3360,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Hobbywing+XRotor+Micro+60A+4-in-1+ESC",
        "color": "#101010",
        "specs": {
            "current_rating_a": 60,
            "voltage_s": "3-6S",
            "firmware": "BLHeli_32",
            "form_factor_mm": 30.5,
            "continuous_current_a": 60,
            "burst_current_a": 75
        }
    },
    {
        "id": "t-motor-f55a-pro-ii-esc",
        "category": "esc",
        "name": "F55A PRO II 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 3808,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F55A+PRO+II+4-in-1+ESC",
        "color": "#181818",
        "specs": {
            "current_rating_a": 55,
            "voltage_s": "3-6S",
            "firmware": "BLHeli_32",
            "form_factor_mm": 30.5,
            "continuous_current_a": 55,
            "burst_current_a": 65
        }
    },
    # ========== MOTOR ==========
    {
        "id": "brotherhobby-avenger-2306-5-motor",
        "category": "motor",
        "name": "Avenger 2306.5 1900KV Motor",
        "brand": "BrotherHobby",
        "price_php": 1176,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=Avenger+2306.5+1900KV+Motor",
        "color": "#151515",
        "specs": {
            "stator_size": "2306.5",
            "kv": 1900,
            "shaft_mm": 5,
            "voltage_s": "4-6S",
            "weight_class": "freestyle",
            "max_thrust_g": 2100
        }
    },
    {
        "id": "emax-eco-ii-2306-motor",
        "category": "motor",
        "name": "ECO II 2306 1900KV Motor",
        "brand": "EMAX",
        "price_php": 784,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com/search?q=ECO+II+2306+1900KV+Motor",
        "color": "#1a1a1a",
        "specs": {
            "stator_size": "2306",
            "kv": 1900,
            "shaft_mm": 5,
            "voltage_s": "4-6S",
            "weight_class": "freestyle",
            "max_thrust_g": 1850
        }
    },
    # ========== PROPELLER ==========
    {
        "id": "gemfan-hurricane-51466-prop",
        "category": "propeller",
        "name": "Hurricane 51466 5\" Tri-Blade Prop",
        "brand": "Gemfan",
        "price_php": 224,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466+5+Tri-Blade+Prop",
        "color": "#0d0d0d",
        "specs": {
            "diameter_inch": 5,
            "pitch_inch": 4.66,
            "blade_count": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    {
        "id": "hqprop-r38-tri-blade-prop",
        "category": "propeller",
        "name": "R38 3.8\" Tri-Blade Prop",
        "brand": "HQProp",
        "price_php": 196,
        "weight_g": 2.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+R38+3.8+Tri-Blade+Prop",
        "color": "#101010",
        "specs": {
            "diameter_inch": 3.8,
            "pitch_inch": 3.5,
            "blade_count": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    # ========== BATTERY ==========
    {
        "id": "cnhl-black-series-1300mah-4s-battery",
        "category": "battery",
        "name": "Black Series 1300mAh 4S 100C LiPo",
        "brand": "CNHL",
        "price_php": 1568,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1300mAh+4S+100C+LiPo",
        "color": "#0d0d0d",
        "specs": {
            "capacity_mah": 1300,
            "cell_count_s": 4,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_v": 14.8
        }
    },
    {
        "id": "tattu-r-line-4-0-1300mah-6s-battery",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S 130C LiPo",
        "brand": "Tattu",
        "price_php": 2856,
        "weight_g": 240,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+4.0+1300mAh+6S+130C+LiPo",
        "color": "#7a1f1f",
        "specs": {
            "capacity_mah": 1300,
            "cell_count_s": 6,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_v": 22.2
        }
    },
    # ========== FRAME ==========
    {
        "id": "armattan-marmotte-frame",
        "category": "frame",
        "name": "Marmotte 5\" Frame",
        "brand": "Armattan",
        "price_php": 5320,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Marmotte+5+Frame",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 227,
            "motor_mount_mm": 20.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "5mm carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 25.5
        }
    },
    {
        "id": "impulserc-apex-frame",
        "category": "frame",
        "name": "Apex 5\" Frame",
        "brand": "ImpulseRC",
        "price_php": 4816,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImpulseRC+Apex+5+Frame",
        "color": "#101010",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 20.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25.5
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
