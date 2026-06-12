#!/usr/bin/env python3
"""Add a fourteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-crocodile-baby5-frame",
        "category": "frame",
        "name": "Crocodile Baby5 V2 Frame",
        "brand": "GEPRC",
        "price_php": 3080,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 210,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+crocodile+baby5"
        }
    },
    {
        "id": "lumenier-qav-s3-v3",
        "category": "frame",
        "name": "QAV-S 3 V3 Frame",
        "brand": "Lumenier",
        "price_php": 1680,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 140,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=lumenier+qav-s3"
        }
    },
    {
        "id": "tmotor-f60-pro-v-plus-2207",
        "category": "motor",
        "name": "F60 PRO V PLUS 2207",
        "brand": "T-Motor",
        "price_php": 1568,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 38
        }
    },
    {
        "id": "flywoo-nin1404-4500kv",
        "category": "motor",
        "name": "NIN1404 4500KV",
        "brand": "Flywoo",
        "price_php": 616,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2a2a2a",
        "specs": {
            "kv": 4500,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 14
        }
    },
    {
        "id": "tmotor-f45a-pro-ii-4in1",
        "category": "esc",
        "name": "F45A PRO II 4-in-1",
        "brand": "T-Motor",
        "price_php": 3248,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
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
        "id": "hglrc-zeus-50a-4in1",
        "category": "esc",
        "name": "Zeus 50A 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 2352,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
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
        "id": "foxeer-f722-v4-aio",
        "category": "fc",
        "name": "F722 V4 AIO Flight Controller",
        "brand": "Foxeer",
        "price_php": 3248,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#000055",
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
        "id": "iflight-succex-d-f405-v2-1",
        "category": "fc",
        "name": "SucceX-D F405 V2.1",
        "brand": "iFlight",
        "price_php": 2240,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
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
        "id": "hqprop-5x4x3-light",
        "category": "propeller",
        "name": "5X4X3 Light",
        "brand": "HQProp",
        "price_php": 168,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
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
        "id": "gemfan-2015-2-toothpick",
        "category": "propeller",
        "name": "2015-2 Toothpick Prop",
        "brand": "Gemfan",
        "price_php": 140,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 2,
            "pitch": 1.5,
            "blade_count": 2,
            "shaft_mm": 1.5,
            "color_options": [
                "gray",
                "transparent"
            ]
        }
    },
    {
        "id": "caddx-polar-vista",
        "category": "camera",
        "name": "Polar Vista",
        "brand": "Caddx",
        "price_php": 2800,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "resolution": "720p60",
            "voltage_range": "6-22V",
            "video_system": "HDZero"
        }
    },
    {
        "id": "runcam-hybrid-3",
        "category": "camera",
        "name": "Hybrid 3",
        "brand": "RunCam",
        "price_php": 3920,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog/Digital",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },
    {
        "id": "foxeer-pulse-pro-vtx",
        "category": "vtx",
        "name": "Pulse Pro VTX",
        "brand": "Foxeer",
        "price_php": 1960,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Raceband",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tbs-unify-evo-pro32",
        "category": "vtx",
        "name": "Unify Evo Pro32",
        "brand": "TBS",
        "price_php": 3640,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "Full 48ch",
            "voltage_range": "6-23V",
            "connector": "U.FL"
        }
    },
    {
        "id": "tattu-rline3-1300mah-4s-95c",
        "category": "battery",
        "name": "R-Line 3.0 1300mAh 4S 95C",
        "brand": "Tattu",
        "price_php": 1512,
        "weight_g": 158,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
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
        "id": "cnhl-black-series-1500mah-6s",
        "category": "battery",
        "name": "Black Series 1500mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1960,
        "weight_g": 230,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1500,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "betafpv-elrs-nano-rx",
        "category": "receiver",
        "name": "ELRS Nano Receiver",
        "brand": "BetaFPV",
        "price_php": 728,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "radiomaster-rp4td-elrs-rx",
        "category": "receiver",
        "name": "RP4TD ELRS Diversity Receiver",
        "brand": "RadioMaster",
        "price_php": 1400,
        "weight_g": 2.5,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "matek-m10q-pro-gps",
        "category": "gps",
        "name": "M10Q-Pro GPS+Compass",
        "brand": "Matek",
        "price_php": 1680,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "betafpv-m10-gps-pro",
        "category": "gps",
        "name": "M10 GPS Pro",
        "brand": "BetaFPV",
        "price_php": 1232,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "immersionrc-spironet",
        "category": "antenna",
        "name": "SpiroNet 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 728,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
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
        "id": "rushfpv-cherry-pagoda",
        "category": "antenna",
        "name": "Cherry Pagoda Antenna",
        "brand": "RushFPV",
        "price_php": 728,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
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
