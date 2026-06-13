#!/usr/bin/env python3
"""Add a seventeenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "armattan-marmotte-6",
        "category": "frame",
        "name": "Marmotte 6\"",
        "brand": "Armattan",
        "price_php": 4200,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://www.armattanquads.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 254,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+marmotte"
        }
    },
    {
        "id": "lumenier-qav-s5-v2",
        "category": "frame",
        "name": "QAV-S 5\" V2",
        "brand": "Lumenier",
        "price_php": 2650,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=lumenier+qav-s5"
        }
    },
    {
        "id": "emax-eco-ii-2807-1700kv",
        "category": "motor",
        "name": "ECO II 2807 1700KV",
        "brand": "Emax",
        "price_php": 1250,
        "weight_g": 36,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com/products/emax-eco-ii-series-2807-motor",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 6,
            "max_voltage_s": 8,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "flywoo-nin-v2-2207-1900kv",
        "category": "motor",
        "name": "NIN V2 2207 1900KV",
        "brand": "Flywoo",
        "price_php": 1400,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://flywoo.net/products/nin-v2-2207-motor",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "flycolor-x-cross-80a",
        "category": "esc",
        "name": "X-Cross HV 80A 4-in-1 ESC",
        "brand": "Flycolor",
        "price_php": 3400,
        "weight_g": 35,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/product:4557",
        "color": "#001a00",
        "specs": {
            "amp_rating": 80,
            "input_voltage_s": 12,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 95
        }
    },
    {
        "id": "diatone-mamba-f50-45a-4in1",
        "category": "esc",
        "name": "Mamba F50 45A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 2500,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/products/mamba-f50-45a-4in1-esc",
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
        "id": "speedybee-f405-v3-bls-50a",
        "category": "fc",
        "name": "F405 V3 BLS 50A Stack",
        "brand": "SpeedyBee",
        "price_php": 2900,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://speedybee.com",
        "color": "#000044",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "iflight-blitz-mini-f7-g3",
        "category": "fc",
        "name": "BLITZ Mini F7 G3 FC",
        "brand": "iFlight",
        "price_php": 1700,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight-rc.com",
        "color": "#000044",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-windancer-5125-3",
        "category": "propeller",
        "name": "Windancer 5125-3",
        "brand": "Gemfan",
        "price_php": 270,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "black",
                "white"
            ]
        }
    },
    {
        "id": "dal-cyclone-t5040-3",
        "category": "propeller",
        "name": "Cyclone T5040 Tri-Blade",
        "brand": "DAL",
        "price_php": 230,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com/collections/dal-props",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray",
                "white"
            ]
        }
    },
    {
        "id": "runcam-night-eagle-3-pro",
        "category": "camera",
        "name": "Night Eagle 3 Pro",
        "brand": "RunCam",
        "price_php": 1850,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-22V"
        }
    },
    {
        "id": "caddx-nebula-pro-v2",
        "category": "camera",
        "name": "Nebula Pro V2",
        "brand": "Caddx",
        "price_php": 2400,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 155,
            "format": "Digital",
            "tvl": 1200,
            "voltage_range": "6-25V"
        }
    },
    {
        "id": "hglrc-titan-vtx-1w",
        "category": "vtx",
        "name": "Titan 1W VTX",
        "brand": "HGLRC",
        "price_php": 1900,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Smart Audio",
            "video_system": "Analog",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-chimera-vtx-5w",
        "category": "vtx",
        "name": "Chimera 5W VTX",
        "brand": "iFlight",
        "price_php": 2300,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://shop.iflight-rc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 5000,
            "protocol": "Smart Audio",
            "video_system": "Analog",
            "voltage_range": "7-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-r-line-5-1400mah-6s",
        "category": "battery",
        "name": "R-Line 5.0 1400mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2000,
        "weight_g": 250,
        "in_stock": True,
        "buy_url": "https://genstattu.com/tattu-batteries/",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1400,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "cnhl-ministar-1100mah-6s",
        "category": "battery",
        "name": "MiniStar 1100mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1500,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.cnhlbattery.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-ep2-pro-rx",
        "category": "receiver",
        "name": "EP2 PRO ELRS Receiver",
        "brand": "HappyModel",
        "price_php": 550,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 22
        }
    },
    {
        "id": "betafpv-elrs-nano-rx-v2",
        "category": "receiver",
        "name": "ELRS Nano RX V2",
        "brand": "BetaFPV",
        "price_php": 850,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 28
        }
    },
    {
        "id": "iflight-m9n-gps-v2",
        "category": "gps",
        "name": "M9N GPS V2",
        "brand": "iFlight",
        "price_php": 1350,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://shop.iflight-rc.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 24,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "radiomaster-m9n-gps",
        "category": "gps",
        "name": "M9N GPS Module",
        "brand": "RadioMaster",
        "price_php": 1300,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "akk-x2-5-8-stubby",
        "category": "antenna",
        "name": "X2 5.8GHz Stubby Antenna",
        "brand": "AKK",
        "price_php": 450,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.akktek.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "foxeer-pagoda-pro-3",
        "category": "antenna",
        "name": "Pagoda Pro 3",
        "brand": "Foxeer",
        "price_php": 750,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
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
