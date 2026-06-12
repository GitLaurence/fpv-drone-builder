#!/usr/bin/env python3
"""Add a sixteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-chimera7-pro",
        "category": "frame",
        "name": "Chimera7 Pro",
        "brand": "iFlight",
        "price_php": 4500,
        "weight_g": 196,
        "in_stock": True,
        "buy_url": "https://shop.iflight-rc.com/Chimera7-Pro-Frame-Kit-Pro1893",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+chimera7"
        }
    },
    {
        "id": "geprc-smart35-frame",
        "category": "frame",
        "name": "Smart35 Frame",
        "brand": "GEPRC",
        "price_php": 1450,
        "weight_g": 47,
        "in_stock": True,
        "buy_url": "https://geprc.com/product/geprc-smart35-frame/",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 150,
            "motor_mount_mm": 12,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+smart35"
        }
    },
    {
        "id": "flywoo-nin-v2-2306-5",
        "category": "motor",
        "name": "NIN V2 2306.5",
        "brand": "Flywoo",
        "price_php": 1450,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://flywoo.net/products/nin-v2-2306-5-motor",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1950,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "tmotor-f60-pro-iv",
        "category": "motor",
        "name": "F60 Pro IV",
        "brand": "T-Motor",
        "price_php": 1500,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/product/f60provicompetitionversion.html",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "flywoo-goku-60a-aio",
        "category": "esc",
        "name": "GOKU 60A 4-in-1 ESC",
        "brand": "Flywoo",
        "price_php": 2800,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://flywoo.net/products/goku-g60a-4in1-esc",
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
        "id": "tbs-tornado-esc",
        "category": "esc",
        "name": "Tornado 4-in-1 ESC",
        "brand": "TBS",
        "price_php": 3200,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/prod:tbs_tornado_esc",
        "color": "#001a00",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "mamba-f405-mk2-fc",
        "category": "fc",
        "name": "Mamba F405 MK2 FC",
        "brand": "Diatone",
        "price_php": 1800,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/products/mamba-f405-mk2-flight-controller",
        "color": "#000044",
        "specs": {
            "gyro": "MPU6000",
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
        "id": "iflight-succex-e-f4",
        "category": "fc",
        "name": "SucceX-E F4 FC",
        "brand": "iFlight",
        "price_php": 1200,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://shop.iflight-rc.com/SucceX-E-F4-Flight-Controller-Pro777",
        "color": "#000044",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-hurricane-5125",
        "category": "propeller",
        "name": "Hurricane 5125",
        "brand": "Gemfan",
        "price_php": 280,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/gemfan-hurricane-5125-3-blade-propeller-set-of-4.html",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray"
            ]
        }
    },
    {
        "id": "dal-t5046-tri",
        "category": "propeller",
        "name": "T5046 Tri-Blade",
        "brand": "DAL",
        "price_php": 240,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/dal-t5046c-cyclone-5-prop.html",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "white",
                "gray"
            ]
        }
    },
    {
        "id": "runcam-racer-nano",
        "category": "camera",
        "name": "Racer Nano",
        "brand": "RunCam",
        "price_php": 1400,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/store/index.php?id_product=180",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 170,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-20V"
        }
    },
    {
        "id": "eachine-rapidfire-cam",
        "category": "camera",
        "name": "RapidFire Mini Camera",
        "brand": "Eachine",
        "price_php": 480,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/eachine-rapidfire-mini-fpv-camera.html",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 700,
            "voltage_range": "5-22V"
        }
    },
    {
        "id": "flywoo-eagle-mini-vtx",
        "category": "vtx",
        "name": "Eagle Mini VTX",
        "brand": "Flywoo",
        "price_php": 1500,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://flywoo.net/products/eagle-mini-vtx",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Smart Audio",
            "video_system": "Analog",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rush-cherry-vtx",
        "category": "vtx",
        "name": "Cherry Micro VTX",
        "brand": "Rush",
        "price_php": 1300,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Smart Audio",
            "video_system": "Analog",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-black-series-1500mah-4s-100c",
        "category": "battery",
        "name": "Black Series 1500mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1100,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.cnhlbattery.com/products/cnhl-black-series-4s-1500mah",
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
        "id": "tattu-r-line-4-1300mah-6s",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S 120C",
        "brand": "Tattu",
        "price_php": 1850,
        "weight_g": 235,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com/tattu-r-line-version-4-0-1300mah-22-2v-120c-6s1p-lipo-battery-pack.html",
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
        "id": "happymodel-elrs-pp-rx",
        "category": "receiver",
        "name": "ExpressLRS PP Receiver",
        "brand": "HappyModel",
        "price_php": 400,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn/index.php/product/ep2-receiver/",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "betafpv-elrs-superd-rx",
        "category": "receiver",
        "name": "ELRS SuperD Nano RX",
        "brand": "BetaFPV",
        "price_php": 900,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://betafpv.com/products/elrs-superd-2-4ghz-diversity-receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "holybro-microm10-gps",
        "category": "gps",
        "name": "Micro M10 GPS",
        "brand": "Holybro",
        "price_php": 1300,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://holybro.com/products/micro-m10-gps",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-5883l-gps",
        "category": "gps",
        "name": "M10Q-5883L GPS",
        "brand": "Matek",
        "price_php": 1250,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-5883l",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M10Q",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "tbs-triumph-pro-antenna",
        "category": "antenna",
        "name": "Triumph Pro Antenna",
        "brand": "TBS",
        "price_php": 1900,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/prod:triumph_pro",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 8,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional patch"
        }
    },
    {
        "id": "axii2-stubby-antenna",
        "category": "antenna",
        "name": "AXII 2 Stubby 5.8GHz",
        "brand": "Lumenier",
        "price_php": 700,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "omni"
        }
    },
]


def main():
    with open("data/parts.json") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    added = 0
    skipped = 0

    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"SKIP (exists): {part['id']}")
            skipped += 1
        else:
            data["parts"].append(part)
            existing_ids.add(part["id"])
            added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone: added {added} parts, skipped {skipped} duplicates")
    print(f"Total parts now: {len(data['parts'])}")


if __name__ == "__main__":
    main()
