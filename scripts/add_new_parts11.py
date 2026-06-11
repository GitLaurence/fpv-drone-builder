#!/usr/bin/env python3
"""Add an eleventh batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-nazgul5-v2",
        "category": "frame",
        "name": "Nazgul5 V2 Frame",
        "brand": "iFlight",
        "price_php": 3199,
        "weight_g": 106,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 226,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+nazgul5+v2"
        }
    },
    {
        "id": "gepro-cinelog35",
        "category": "frame",
        "name": "Cinelog35 Frame",
        "brand": "GEPRC",
        "price_php": 2399,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 150,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+cinelog35"
        }
    },
    {
        "id": "brother-hobby-avenger-2807-5",
        "category": "motor",
        "name": "Avenger 2807.5",
        "brand": "BrotherHobby",
        "price_php": 1449,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 52
        }
    },
    {
        "id": "iflight-xing-x2806-5",
        "category": "motor",
        "name": "XING X2806.5",
        "brand": "iFlight",
        "price_php": 1099,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2806.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "holybro-tekko32-f4-50a",
        "category": "esc",
        "name": "Tekko32 F4 4-in-1 50A",
        "brand": "Holybro",
        "price_php": 3199,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#001a00",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "spedix-ls45-v3",
        "category": "esc",
        "name": "LS45 V3 4-in-1 45A",
        "brand": "Spedix",
        "price_php": 2599,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "mamba-f722-mini-mk2",
        "category": "fc",
        "name": "F722 Mini MK2",
        "brand": "Mamba",
        "price_php": 2799,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "airbot-f7-mini",
        "category": "fc",
        "name": "F7 Mini Flight Controller",
        "brand": "Airbot",
        "price_php": 2399,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000044",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 1,
            "curr_sensor": False
        }
    },
    {
        "id": "gemfan-hurricane-5152-3",
        "category": "propeller",
        "name": "Hurricane 5152 3-Blade",
        "brand": "Gemfan",
        "price_php": 250,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 5.2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray",
                "green"
            ]
        }
    },
    {
        "id": "hqprop-5x4.3x3-durable",
        "category": "propeller",
        "name": "Durable 5X4.3X3",
        "brand": "HQProp",
        "price_php": 232,
        "weight_g": 5.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray"
            ]
        }
    },
    {
        "id": "runcam-hybrid3",
        "category": "camera",
        "name": "Hybrid 3",
        "brand": "RunCam",
        "price_php": 3199,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 145,
            "format": "Analog + 4K Digital DVR",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },
    {
        "id": "foxeer-toothless2-nano",
        "category": "camera",
        "name": "Toothless 2 Nano",
        "brand": "Foxeer",
        "price_php": 1499,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "dji-o3-air-unit",
        "category": "vtx",
        "name": "O3 Air Unit",
        "brand": "DJI",
        "price_php": 9499,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 700,
            "protocol": "Digital (DJI O3)",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "Onboard"
        }
    },
    {
        "id": "rushfpv-tank-max-solo",
        "category": "vtx",
        "name": "Tank Max Solo",
        "brand": "Rush",
        "price_php": 2799,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "gnb-2s-650mah",
        "category": "battery",
        "name": "650mAh 2S 80C",
        "brand": "GNB",
        "price_php": 449,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 2,
            "capacity_mah": 650,
            "c_rating": 80,
            "connector": "PH2.0",
            "voltage_nominal": 7.4
        }
    },
    {
        "id": "tattu-4s-1300mah-95c",
        "category": "battery",
        "name": "R-Line V5 4S 1300mAh 95C",
        "brand": "Tattu",
        "price_php": 1449,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 95,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "frsky-r9-mm",
        "category": "receiver",
        "name": "R9 MM Long Range Receiver",
        "brand": "FrSky",
        "price_php": 1899,
        "weight_g": 1.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "radiomaster-er6",
        "category": "receiver",
        "name": "ER6 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 699,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "cubepilot-here3-pro-gps",
        "category": "gps",
        "name": "Here3+ GPS/RTK Module",
        "brand": "CubePilot",
        "price_php": 6499,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou+Galileo",
            "chipset": "u-blox M8P",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m8n",
        "category": "gps",
        "name": "Micro M8N GPS",
        "brand": "Holybro",
        "price_php": 1199,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "rushfpv-cherry-vtx-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz VTX Antenna",
        "brand": "Rush",
        "price_php": 649,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "aomway-rd-cloverleaf",
        "category": "antenna",
        "name": "RD Cloverleaf Antenna",
        "brand": "Aomway",
        "price_php": 449,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "SMA",
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
