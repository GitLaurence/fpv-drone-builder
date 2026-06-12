#!/usr/bin/env python3
"""Add a fifteenth batch of 33 new FPV parts (3 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-mark5-hd5",
        "category": "frame",
        "name": "Mark5 HD5",
        "brand": "GEPRC",
        "price_php": 2520,
        "weight_g": 85,
        "in_stock": True,
        "buy_url": "https://www.geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5"
        }
    },
    {
        "id": "flywoo-hex-vampire-hd",
        "category": "frame",
        "name": "Hex Vampire HD",
        "brand": "Flywoo",
        "price_php": 2800,
        "weight_g": 78,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+hex+vampire"
        }
    },
    {
        "id": "tbs-source-one-v4",
        "category": "frame",
        "name": "Source One V4",
        "brand": "TBS",
        "price_php": 1680,
        "weight_g": 70,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+v4"
        }
    },
    {
        "id": "t-motor-velox-v2306",
        "category": "motor",
        "name": "VELOX V2306 V2",
        "brand": "T-Motor",
        "price_php": 1512,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "brotherhobby-avenger-2306",
        "category": "motor",
        "name": "Avenger 2306",
        "brand": "BrotherHobby",
        "price_php": 1400,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1850,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "ethix-mr-steele-v4-2306",
        "category": "motor",
        "name": "Mr Steele V4 2306",
        "brand": "Ethix",
        "price_php": 1850,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "aikon-af45-4in1",
        "category": "esc",
        "name": "AF45 4-in-1",
        "brand": "Aikon",
        "price_php": 2520,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.aikonfpv.com",
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
        "id": "hobbywing-xrotor-60a",
        "category": "esc",
        "name": "XRotor 60A 4-in-1",
        "brand": "Hobbywing",
        "price_php": 3080,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.hobbywing.com",
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
        "id": "diatone-mamba-f50-45a",
        "category": "esc",
        "name": "Mamba F50 45A 4-in-1",
        "brand": "Diatone",
        "price_php": 2240,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
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
        "id": "diatone-mamba-h743-v3",
        "category": "fc",
        "name": "Mamba F405 H743 V3",
        "brand": "Diatone",
        "price_php": 3640,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us"
        }
    },
    {
        "id": "mateksys-f405-te",
        "category": "fc",
        "name": "F405-TE",
        "brand": "Matek",
        "price_php": 2240,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.mateksys.com/?portfolio=f405-te"
        }
    },
    {
        "id": "holybro-kakuteh7-mini",
        "category": "fc",
        "name": "Kakute H7 Mini",
        "brand": "Holybro",
        "price_php": 3920,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.holybro.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.holybro.com"
        }
    },
    {
        "id": "dalprop-t5045c",
        "category": "propeller",
        "name": "T5045C Cyclone",
        "brand": "DAL",
        "price_php": 168,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.dalprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "purple"]
        }
    },
    {
        "id": "hqprop-5x4x3",
        "category": "propeller",
        "name": "5X4X3 Durable",
        "brand": "HQProp",
        "price_php": 224,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "orange"]
        }
    },
    {
        "id": "gemfan-floppy-5055",
        "category": "propeller",
        "name": "Floppy Proppy 5055",
        "brand": "Gemfan",
        "price_php": 196,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 5.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "black"]
        }
    },
    {
        "id": "runcam-racer-3",
        "category": "camera",
        "name": "Racer 3",
        "brand": "RunCam",
        "price_php": 1400,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-mix-2",
        "category": "camera",
        "name": "Mix 2",
        "brand": "Foxeer",
        "price_php": 1680,
        "weight_g": 5.4,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog/Digital",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },
    {
        "id": "foxeer-night-cat-3",
        "category": "camera",
        "name": "Night Cat 3",
        "brand": "Foxeer",
        "price_php": 1568,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" STARVIS",
            "fov_deg": 150,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "hdzero-freestyle-v2",
        "category": "vtx",
        "name": "Freestyle V2 VTX",
        "brand": "HDZero",
        "price_php": 3920,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "HDZero",
            "bands": "Race/F",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3",
        "category": "vtx",
        "name": "Avatar HD V3 VTX",
        "brand": "Walksnail",
        "price_php": 4200,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Walksnail",
            "bands": "Digital",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "rush-tank-max",
        "category": "vtx",
        "name": "Tank Max",
        "brand": "Rush",
        "price_php": 2520,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
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
        "id": "cnhl-black-series-6s-1300",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1680,
        "weight_g": 230,
        "in_stock": True,
        "buy_url": "https://www.cnhlbattery.com",
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
        "id": "gnb-4s-1300",
        "category": "battery",
        "name": "1300mAh 4S 100C",
        "brand": "GNB",
        "price_php": 1008,
        "weight_g": 155,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-r-line-v5-4s",
        "category": "battery",
        "name": "R-Line V5 1300mAh 4S",
        "brand": "Tattu",
        "price_php": 1568,
        "weight_g": 160,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "radiomaster-er8",
        "category": "receiver",
        "name": "ER8 ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 840,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "tbs-crossfire-deluxe-rx",
        "category": "receiver",
        "name": "Crossfire Deluxe RX",
        "brand": "TBS",
        "price_php": 1680,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "siyi-fm30",
        "category": "receiver",
        "name": "FM30 Receiver",
        "brand": "SIYI",
        "price_php": 1120,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://shop.siyi.biz",
        "color": "#1a001a",
        "specs": {
            "protocol": "SIYI FM",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "matek-m10q-1125",
        "category": "gps",
        "name": "M10Q-1125 GPS",
        "brand": "Matek",
        "price_php": 1232,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": False,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "beitian-bn-880t",
        "category": "gps",
        "name": "BN-880T GPS+Compass",
        "brand": "Beitian",
        "price_php": 1008,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.beitian.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-st-m9n",
        "category": "gps",
        "name": "ST-M9N GPS",
        "brand": "Holybro",
        "price_php": 1680,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "tbs-triumph-plus",
        "category": "antenna",
        "name": "Triumph Plus 5.8GHz",
        "brand": "TBS",
        "price_php": 1120,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "rushfpv-cherry-pepper",
        "category": "antenna",
        "name": "Cherry Pepper 5.8GHz",
        "brand": "RushFPV",
        "price_php": 560,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "foxeer-lollipop-3-plus",
        "category": "antenna",
        "name": "Lollipop 3 Plus 5.8GHz",
        "brand": "Foxeer",
        "price_php": 448,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "MMCX",
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
