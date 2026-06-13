#!/usr/bin/env python3
"""Add an eighteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "axisflying-cinerace35-v3-frame",
        "category": "frame",
        "name": "Cinerace35 V3",
        "brand": "Axisflying",
        "price_php": 3200,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 178,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 3.5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+cinerace35"
        }
    },
    {
        "id": "iflight-titan-e-frame",
        "category": "frame",
        "name": "Titan E 5\"",
        "brand": "iFlight",
        "price_php": 2750,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+titan+e"
        }
    },
    {
        "id": "tmotor-velox-v2306-v2-1900kv",
        "category": "motor",
        "name": "Velox V2306 V2 1900KV",
        "brand": "T-Motor",
        "price_php": 1550,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "brotherhobby-avenger-2306.5-1900kv",
        "category": "motor",
        "name": "Avenger 2306.5 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1400,
        "weight_g": 31.5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 43
        }
    },
    {
        "id": "speedybee-f405-v4-55a-aio",
        "category": "esc",
        "name": "F405 V4 55A AIO",
        "brand": "SpeedyBee",
        "price_php": 4200,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "hglrc-zeus-f745-60a-aio",
        "category": "esc",
        "name": "Zeus F745 60A AIO",
        "brand": "HGLRC",
        "price_php": 5200,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 80
        }
    },
    {
        "id": "holybro-kakute-f7-hdx",
        "category": "fc",
        "name": "Kakute F7 HDX",
        "brand": "Holybro",
        "price_php": 4800,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
            "diagram_url": "https://docs.holybro.com/flight-controller/kakute-f7-hdx"
        }
    },
    {
        "id": "speedybee-f405-wing-mini",
        "category": "fc",
        "name": "F405 Wing Mini",
        "brand": "SpeedyBee",
        "price_php": 2600,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-5x4.3x3-v1s",
        "category": "propeller",
        "name": "5X4.3X3 V1S",
        "brand": "HQProp",
        "price_php": 210,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-banshee-5126-3blade",
        "category": "propeller",
        "name": "Banshee 5126 3-Blade",
        "brand": "Gemfan",
        "price_php": 240,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "white"]
        }
    },
    {
        "id": "caddx-walter-2",
        "category": "camera",
        "name": "Walter 2",
        "brand": "Caddx",
        "price_php": 4500,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "tvl": 1300,
            "voltage_range": "7-26V"
        }
    },
    {
        "id": "runcam-hybrid-3",
        "category": "camera",
        "name": "Hybrid 3",
        "brand": "RunCam",
        "price_php": 6500,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 145,
            "format": "Digital/Analog combo",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },
    {
        "id": "iflight-ts5828l",
        "category": "vtx",
        "name": "TS5828L",
        "brand": "iFlight",
        "price_php": 800,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-sirius-1-2w",
        "category": "vtx",
        "name": "Sirius 1.2W VTX",
        "brand": "HGLRC",
        "price_php": 2900,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-r-line-1300mah-4s",
        "category": "battery",
        "name": "R-Line 1300mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1850,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "gnb-1300mah-4s-100c",
        "category": "battery",
        "name": "1300mAh 4S 100C",
        "brand": "GNB",
        "price_php": 1100,
        "weight_g": 158,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
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
        "id": "happymodel-ep2-rx",
        "category": "receiver",
        "name": "EP2 ELRS Receiver",
        "brand": "HappyModel",
        "price_php": 750,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "tbs-nano-rx-elrs",
        "category": "receiver",
        "name": "Nano RX ELRS",
        "brand": "TBS",
        "price_php": 900,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "beitian-bn-280",
        "category": "gps",
        "name": "BN-280 GPS+Compass",
        "brand": "Beitian",
        "price_php": 950,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8030",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "hglrc-m100-5883",
        "category": "gps",
        "name": "M100 5883 GPS+Compass",
        "brand": "HGLRC",
        "price_php": 1250,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 24,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "rush-cherry-pro-5-8",
        "category": "antenna",
        "name": "Cherry Pro 5.8GHz",
        "brand": "Rush",
        "price_php": 650,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "aomway-3dbi-stubby",
        "category": "antenna",
        "name": "3dBi Stubby Antenna",
        "brand": "Aomway",
        "price_php": 380,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://www.aomway.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.0,
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
