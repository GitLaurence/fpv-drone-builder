#!/usr/bin/env python3
"""Add an eleventh batch of new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "axisflying-cinevolution-c229-v2",
        "category": "frame",
        "name": "Cinevolution C229 V2",
        "brand": "Axisflying",
        "price_php": 3199,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 229,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+cinevolution+c229"
        }
    },
    {
        "id": "iflight-marc4-v3",
        "category": "frame",
        "name": "Marc4 V3",
        "brand": "iFlight",
        "price_php": 1799,
        "weight_g": 64,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 178,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 3.5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+marc4"
        }
    },
    {
        "id": "tmotor-f90-pro-v",
        "category": "motor",
        "name": "F90 PRO V 2207",
        "brand": "T-Motor",
        "price_php": 1649,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "brotherhobby-avenger-2306.5-v2",
        "category": "motor",
        "name": "Avenger 2306.5 V2",
        "brand": "BrotherHobby",
        "price_php": 1399,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1850,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "tmotor-f45a-mini",
        "category": "esc",
        "name": "F45A Mini 4-in-1",
        "brand": "T-Motor",
        "price_php": 2599,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
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
        "id": "flycolor-x-cross-50a-4in1",
        "category": "esc",
        "name": "X-Cross 50A 4-in-1",
        "brand": "Flycolor",
        "price_php": 1850,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.flycolor.cn",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 60
        }
    },
    {
        "id": "iflight-succex-e-f722",
        "category": "fc",
        "name": "SucceX-E F722",
        "brand": "iFlight",
        "price_php": 2599,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://shop.iflight.com"
        }
    },
    {
        "id": "speedybee-f405-v4-50a-aio",
        "category": "fc",
        "name": "F405 V4 50A AIO",
        "brand": "SpeedyBee",
        "price_php": 3999,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com"
        }
    },
    {
        "id": "azure-power-freestyle-5x4.3",
        "category": "propeller",
        "name": "Freestyle 5x4.3x3",
        "brand": "Azure Power",
        "price_php": 219,
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
        "id": "dal-cyclone-t5045-3",
        "category": "propeller",
        "name": "Cyclone T5045 3-Blade",
        "brand": "DAL",
        "price_php": 199,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.dalprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "orange"]
        }
    },
    {
        "id": "runcam-hybrid-3",
        "category": "camera",
        "name": "Hybrid 3",
        "brand": "RunCam",
        "price_php": 3399,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "6-22V",
            "video_system": "Analog + HD"
        }
    },
    {
        "id": "caddx-nebula-pro-2",
        "category": "camera",
        "name": "Nebula Pro 2",
        "brand": "Caddx",
        "price_php": 4299,
        "weight_g": 7.7,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "resolution": "1080p60",
            "voltage_range": "6.6-25.2V",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-vtx-pro",
        "category": "vtx",
        "name": "Avatar HD V3 VTX Pro",
        "brand": "Walksnail",
        "price_php": 5599,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1500,
            "protocol": "Digital",
            "bands": "Walksnail Avatar",
            "voltage_range": "6.6-25.2V",
            "connector": "MMCX",
            "video_system": "Walksnail"
        }
    },
    {
        "id": "rush-tank-max-solo-vtx",
        "category": "vtx",
        "name": "Tank Max Solo VTX",
        "brand": "Rush",
        "price_php": 2799,
        "weight_g": 12,
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
        "price_php": 1899,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
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
        "id": "tattu-rline-5-4s-1300",
        "category": "battery",
        "name": "R-Line V5.0 1300mAh 4S 150C",
        "brand": "Tattu",
        "price_php": 1599,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "betafpv-elrs-nano-rx",
        "category": "receiver",
        "name": "ELRS Nano RX",
        "brand": "BetaFPV",
        "price_php": 799,
        "weight_g": 0.6,
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
        "id": "immersionrc-ghost-atto-rx",
        "category": "receiver",
        "name": "Ghost Atto RX",
        "brand": "ImmersionRC",
        "price_php": 1299,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Ghost",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "cuav-neo-3-pro",
        "category": "gps",
        "name": "NEO 3 Pro GPS",
        "brand": "CUAV",
        "price_php": 3199,
        "weight_g": 24,
        "in_stock": True,
        "buy_url": "https://www.cuav.net",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-5883-pro",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1550,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-5883",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "immersionrc-spironet",
        "category": "antenna",
        "name": "SpiroNet 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 799,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    },
    {
        "id": "lumenier-axii-2",
        "category": "antenna",
        "name": "AXII 2 5.8GHz",
        "brand": "Lumenier",
        "price_php": 899,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
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
