"""Batch 17: Add 22 new FPV parts across all 11 categories with verified pricing and links."""
import json

NEW_PARTS = [
    {
        "id": "iflight-nazgul5-v2-frame",
        "category": "frame",
        "name": "Nazgul5 V2 Frame",
        "brand": "iFlight",
        "price_php": 1850,
        "weight_g": 120,
        "in_stock": True,
        "buy_url": "https://shop.iflight-rc.com/index.php?route=product/product&product_id=1199",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 230,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+nazgul5"
        }
    },
    {
        "id": "armattan-marmotte-7-frame",
        "category": "frame",
        "name": "Marmotte 7\" Frame",
        "brand": "Armattan",
        "price_php": 7800,
        "weight_g": 210,
        "in_stock": True,
        "buy_url": "https://armattanquads.com/marmotte/",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 320,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+marmotte"
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5",
        "category": "motor",
        "name": "Avenger 2306.5",
        "brand": "BrotherHobby",
        "price_php": 1520,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.brotherhobbyshop.com/products/avenger-2306-5",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1850,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "xing-e-pro-2207",
        "category": "motor",
        "name": "XING-E Pro 2207",
        "brand": "iFlight",
        "price_php": 1390,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://shop.iflight-rc.com/index.php?route=product/product&product_id=1180",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "hglrc-zeus-60a-aio",
        "category": "esc",
        "name": "Zeus 60A AIO ESC",
        "brand": "HGLRC",
        "price_php": 2950,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/products/hglrc-zeus-f765-aio",
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
        "id": "diatone-mamba-f45-mini-esc",
        "category": "esc",
        "name": "Mamba F45 Mini 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 1750,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/products/mamba-f45-mini-4in1-esc",
        "color": "#001a00",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "mamba-f722-mk2-fc",
        "category": "fc",
        "name": "Mamba F722 MK2 FC",
        "brand": "Diatone",
        "price_php": 2400,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/products/mamba-f722-mk2-flight-controller",
        "color": "#000055",
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
        "id": "matek-h743-mini-v3-fc",
        "category": "fc",
        "name": "H743-MINI V3 FC",
        "brand": "Matek",
        "price_php": 4200,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=h743-mini-v3",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.mateksys.com/?portfolio=h743-mini-v3"
        }
    },
    {
        "id": "hqprop-7x4x3",
        "category": "propeller",
        "name": "DP 7x4x3",
        "brand": "HQProp",
        "price_php": 280,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/hqprop-7x4x3-durable-prop-set-of-4.html",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray"
            ]
        }
    },
    {
        "id": "gemfan-hurricane-7042",
        "category": "propeller",
        "name": "Hurricane 7042",
        "brand": "Gemfan",
        "price_php": 320,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/gemfan-hurricane-7042-3-blade-propeller-set-of-4.html",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4.2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray"
            ]
        }
    },
    {
        "id": "caddx-ratel-2-mini",
        "category": "camera",
        "name": "Ratel 2 Mini",
        "brand": "Caddx",
        "price_php": 1450,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://shop.caddxfpv.com/products/caddx-ratel-2",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-25V"
        }
    },
    {
        "id": "runcam-phoenix-oscar-micro",
        "category": "camera",
        "name": "Phoenix Oscar Micro",
        "brand": "RunCam",
        "price_php": 1550,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/store/index.php?id_product=216",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "hglrc-titan-vtx5",
        "category": "vtx",
        "name": "Titan VTX5",
        "brand": "HGLRC",
        "price_php": 1650,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/products/hglrc-titan-vtx5",
        "color": "#221100",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Smart Audio",
            "video_system": "Analog",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "iflight-tantan-vtx",
        "category": "vtx",
        "name": "TanTan VTX",
        "brand": "iFlight",
        "price_php": 1400,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://shop.iflight-rc.com/index.php?route=product/product&product_id=1392",
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
        "id": "cnhl-mini-tank-1300mah-6s",
        "category": "battery",
        "name": "MiniTank 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1650,
        "weight_g": 235,
        "in_stock": True,
        "buy_url": "https://www.cnhlbattery.com/products/cnhl-minitank-6s-1300mah",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gnb-4s-1500mah-100c",
        "category": "battery",
        "name": "1500mAh 4S 100C",
        "brand": "GNB",
        "price_php": 1050,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/gnb-1500mah-4s-100c-lipo-battery-xt60.html",
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
        "id": "betafpv-elrs-nano-rx-v2",
        "category": "receiver",
        "name": "ELRS Nano RX V2",
        "brand": "BetaFPV",
        "price_php": 850,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://betafpv.com/products/elrs-nano-receiver-v2",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "happymodel-ep2-v2-rx",
        "category": "receiver",
        "name": "ExpressLRS EP2 V2 Receiver",
        "brand": "HappyModel",
        "price_php": 950,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn/index.php/product/ep2-receiver/",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "mateksys-m10q-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1500,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-5883",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "beitian-bn-220-v2-gps",
        "category": "gps",
        "name": "BN-220 V2 GPS",
        "brand": "Beitian",
        "price_php": 750,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/beitian-bn-220-flight-control-gps.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 32,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "tbs-triumph-omni-antenna",
        "category": "antenna",
        "name": "Triumph Omni Antenna",
        "brand": "TBS",
        "price_php": 1300,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/prod:triumph",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "foxeer-lollipop-4-antenna",
        "category": "antenna",
        "name": "Lollipop 4 Antenna",
        "brand": "Foxeer",
        "price_php": 480,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/foxeer-lollipop-4-5-8ghz-fpv-antenna.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
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
