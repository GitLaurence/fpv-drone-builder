#!/usr/bin/env python3
"""Add a fifth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-explorer-lr4-frame",
        "category": "frame",
        "name": "Explorer LR4 Frame",
        "brand": "Flywoo",
        "price_php": 1959,
        "weight_g": 78,
        "in_stock": true,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 35,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "geprc-crocodile-baby5-frame",
        "category": "frame",
        "name": "Crocodile Baby5 Frame",
        "brand": "GEPRC",
        "price_php": 2295,
        "weight_g": 95,
        "in_stock": true,
        "buy_url": "https://geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 195,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+crocodile+baby5"
        }
    },
    {
        "id": "iflight-xing2-2207",
        "category": "motor",
        "name": "XING2 2207",
        "brand": "iFlight",
        "price_php": 1287,
        "weight_g": 32,
        "in_stock": true,
        "buy_url": "https://shop.iflight.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-v4",
        "category": "motor",
        "name": "Avenger 2306.5 V4",
        "brand": "BrotherHobby",
        "price_php": 1399,
        "weight_g": 33,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "flycolor-x-cross-50a-4in1-esc",
        "category": "esc",
        "name": "X-Cross 50A BLHeli32 4-in-1 ESC",
        "brand": "Flycolor",
        "price_php": 2519,
        "weight_g": 26,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "tmotor-f45a-v2-4in1-esc",
        "category": "esc",
        "name": "F45A V2 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 3919,
        "weight_g": 27,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "mamba-f405-mk4-fc",
        "category": "fc",
        "name": "F405 Mk4 Flight Controller",
        "brand": "Mamba",
        "price_php": 2799,
        "weight_g": 9,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": false,
            "blackbox": true,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": true,
            "diagram_url": "https://www.diatone.us/products/mamba-f405-mk4-flight-controller"
        }
    },
    {
        "id": "jhemcu-ghf411aio-v2-fc",
        "category": "fc",
        "name": "GHF411AIO V2 Flight Controller",
        "brand": "JHEMCU",
        "price_php": 1399,
        "weight_g": 8,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": true,
            "blackbox": true,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": true,
            "diagram_url": "https://www.jhemcu.com"
        }
    },
    {
        "id": "hqprop-5-1x3-1x3-durable",
        "category": "propeller",
        "name": "DT 5.1×3.1×3 Durable",
        "brand": "HQProp",
        "price_php": 251,
        "weight_g": 5.2,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.1,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey",
                "green"
            ]
        }
    },
    {
        "id": "gemfan-51433-hurricane-durable",
        "category": "propeller",
        "name": "Hurricane 51433 Durable Tri-Blade",
        "brand": "Gemfan",
        "price_php": 279,
        "weight_g": 4.8,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.33,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "white",
                "grey"
            ]
        }
    },
    {
        "id": "foxeer-falkor-2",
        "category": "camera",
        "name": "Falkor 2",
        "brand": "Foxeer",
        "price_php": 1568,
        "weight_g": 6.5,
        "in_stock": true,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-hybrid-3",
        "category": "camera",
        "name": "Hybrid 3",
        "brand": "RunCam",
        "price_php": 4199,
        "weight_g": 12,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 155,
            "format": "Analog+4K DVR",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },
    {
        "id": "iflight-translite-vtx",
        "category": "vtx",
        "name": "TransLite VTX",
        "brand": "iFlight",
        "price_php": 1119,
        "weight_g": 5,
        "in_stock": true,
        "buy_url": "https://shop.iflight.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-kit",
        "category": "vtx",
        "name": "Avatar HD V3 Kit",
        "brand": "Walksnail",
        "price_php": 8399,
        "weight_g": 27,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital",
            "bands": "5.8GHz",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "tattu-r-line-v5-1300mah-4s",
        "category": "battery",
        "name": "R-Line V5 1300mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1399,
        "weight_g": 168,
        "in_stock": true,
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
        "id": "cnhl-ministar-850mah-6s",
        "category": "battery",
        "name": "MiniStar 850mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1119,
        "weight_g": 140,
        "in_stock": true,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 850,
            "c_rating": 100,
            "connector": "XT30",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "immersionrc-ghost-atto-receiver",
        "category": "receiver",
        "name": "Ghost Atto Receiver",
        "brand": "ImmersionRC",
        "price_php": 1175,
        "weight_g": 1.2,
        "in_stock": true,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Ghost",
            "frequency_mhz": 2400,
            "telemetry": true,
            "range_km": 25
        }
    },
    {
        "id": "happymodel-ep1-elrs-receiver",
        "category": "receiver",
        "name": "EP1 ELRS Receiver",
        "brand": "Happymodel",
        "price_php": 783,
        "weight_g": 0.6,
        "in_stock": true,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": true,
            "range_km": 20
        }
    },
    {
        "id": "cuav-neo-3-gps",
        "category": "gps",
        "name": "Neo 3 GPS Module",
        "brand": "CUAV",
        "price_php": 2519,
        "weight_g": 25,
        "in_stock": true,
        "buy_url": "https://www.cuav.net",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": true,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "speedybee-m10-ultra-gps",
        "category": "gps",
        "name": "M10 Ultra GPS",
        "brand": "SpeedyBee",
        "price_php": 1679,
        "weight_g": 10,
        "in_stock": true,
        "buy_url": "https://www.speedybee.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": true,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "foxeer-lollipop-3-plus",
        "category": "antenna",
        "name": "Lollipop 3 Plus 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 559,
        "weight_g": 6,
        "in_stock": true,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omnidirectional"
        }
    },
    {
        "id": "immersionrc-spironet-5-8-antenna",
        "category": "antenna",
        "name": "SpiroNet 5.8GHz Antenna",
        "brand": "ImmersionRC",
        "price_php": 671,
        "weight_g": 8,
        "in_stock": true,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    }
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
