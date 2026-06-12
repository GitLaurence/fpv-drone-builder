#!/usr/bin/env python3
"""Add a sixteenth batch of 33 new FPV parts (3 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-cidora-sl5",
        "category": "frame",
        "name": "Cidora SL5",
        "brand": "iFlight",
        "price_php": 2240,
        "weight_g": 76,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+cidora+sl5"
        }
    },
    {
        "id": "lumenier-qav-x",
        "category": "frame",
        "name": "QAV-X 5\" Freestyle",
        "brand": "Lumenier",
        "price_php": 3360,
        "weight_g": 90,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=lumenier+qav-x"
        }
    },
    {
        "id": "geprc-mark5-vector",
        "category": "frame",
        "name": "Mark5 Vector",
        "brand": "GEPRC",
        "price_php": 2632,
        "weight_g": 82,
        "in_stock": True,
        "buy_url": "https://www.geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 223,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark5+vector"
        }
    },
    {
        "id": "t-motor-f60-pro-v",
        "category": "motor",
        "name": "F60 PRO V 2207",
        "brand": "T-Motor",
        "price_php": 1736,
        "weight_g": 33,
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
            "peak_current_a": 52
        }
    },
    {
        "id": "rcinpower-gts-v2-2207",
        "category": "motor",
        "name": "GTS V2 2207",
        "brand": "RCINPOWER",
        "price_php": 1456,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.rcinpower.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "emax-eco-ii-2807",
        "category": "motor",
        "name": "ECO II 2807",
        "brand": "EMAX",
        "price_php": 1288,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://emax-usa.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "iflight-succex-e-mini-40a",
        "category": "esc",
        "name": "SucceX-E Mini 40A 4-in-1",
        "brand": "iFlight",
        "price_php": 1736,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 50
        }
    },
    {
        "id": "t-motor-f55a-pro-ii",
        "category": "esc",
        "name": "F55A PRO II 4-in-1",
        "brand": "T-Motor",
        "price_php": 2912,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "flywoo-goku-gn-745",
        "category": "esc",
        "name": "GOKU GN 745 45A 4-in-1",
        "brand": "Flywoo",
        "price_php": 2128,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
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
        "id": "iflight-succex-e-f7-v2",
        "category": "fc",
        "name": "SucceX-E F7 V2.1",
        "brand": "iFlight",
        "price_php": 2912,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
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
            "diagram_url": "https://shop.iflight.com"
        }
    },
    {
        "id": "speedybee-f405-wing-mini",
        "category": "fc",
        "name": "F405 Wing Mini",
        "brand": "SpeedyBee",
        "price_php": 2576,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://speedybee.com"
        }
    },
    {
        "id": "flywoo-goku-f405-aio-v2",
        "category": "fc",
        "name": "GOKU F405 AIO V2",
        "brand": "Flywoo",
        "price_php": 2240,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
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
            "diagram_url": "https://flywoo.net"
        }
    },
    {
        "id": "hqprop-5x43x3-v1s",
        "category": "propeller",
        "name": "5X4.3X3 V1S",
        "brand": "HQProp",
        "price_php": 196,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "white"]
        }
    },
    {
        "id": "gemfan-hurricane-5042",
        "category": "propeller",
        "name": "Hurricane 5042",
        "brand": "Gemfan",
        "price_php": 168,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.2,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "dalprop-t5046c",
        "category": "propeller",
        "name": "T5046C Cyclone",
        "brand": "DAL",
        "price_php": 168,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.dalprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "purple"]
        }
    },
    {
        "id": "caddx-nebula-pro-2",
        "category": "camera",
        "name": "Nebula Pro 2",
        "brand": "Caddx",
        "price_php": 3920,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" STARVIS 2",
            "fov_deg": 155,
            "format": "Digital HD",
            "tvl": 1300,
            "voltage_range": "6-25V"
        }
    },
    {
        "id": "walksnail-avatar-hd-3-camera",
        "category": "camera",
        "name": "Avatar HD V3 Camera",
        "brand": "Walksnail",
        "price_php": 3360,
        "weight_g": 7.6,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 150,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "7-25.2V"
        }
    },
    {
        "id": "runcam-hybrid-3",
        "category": "camera",
        "name": "Hybrid 3",
        "brand": "RunCam",
        "price_php": 3640,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog + 4K DVR",
            "tvl": 1200,
            "voltage_range": "6-22V"
        }
    },
    {
        "id": "diatone-mamba-vtx-mr1",
        "category": "vtx",
        "name": "Mamba VTX MR1",
        "brand": "Diatone",
        "price_php": 1568,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "immersionrc-tramp-m-plus",
        "category": "vtx",
        "name": "Tramp M Plus VTX",
        "brand": "ImmersionRC",
        "price_php": 2520,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "foxeer-cabin-tx",
        "category": "vtx",
        "name": "Cabin TX 1W",
        "brand": "Foxeer",
        "price_php": 2800,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-racing-6s-1500",
        "category": "battery",
        "name": "Racing Series 1500mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1960,
        "weight_g": 260,
        "in_stock": True,
        "buy_url": "https://www.cnhlrc.com",
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
        "id": "tattu-r-line-v5-6s-1100",
        "category": "battery",
        "name": "R-Line V5 1100mAh 6S",
        "brand": "Tattu",
        "price_php": 1848,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gnb-4s-1500",
        "category": "battery",
        "name": "1500mAh 4S 100C",
        "brand": "GNB",
        "price_php": 1120,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
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
        "id": "happymodel-elrs-ep2",
        "category": "receiver",
        "name": "EP2 ELRS Receiver",
        "brand": "Happymodel",
        "price_php": 672,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "betafpv-elrs3-nano-rx",
        "category": "receiver",
        "name": "ELRS3 Nano Receiver",
        "brand": "BetaFPV",
        "price_php": 896,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "frsky-archer-rs-rx",
        "category": "receiver",
        "name": "Archer RS Receiver",
        "brand": "FrSky",
        "price_php": 1008,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.frsky-rc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "betafpv-m10-nano-gps",
        "category": "gps",
        "name": "M10 Nano GPS",
        "brand": "BetaFPV",
        "price_php": 896,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 22,
            "compass": False,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m9-gps",
        "category": "gps",
        "name": "Micro M9N GPS",
        "brand": "Holybro",
        "price_php": 1456,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-1233",
        "category": "gps",
        "name": "M10Q-1233 GPS",
        "brand": "Matek",
        "price_php": 1176,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 24,
            "compass": False,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "immersionrc-spironet",
        "category": "antenna",
        "name": "SpiroNET 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 672,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "axisflying-sailing-antenna",
        "category": "antenna",
        "name": "Sailing 5.8GHz",
        "brand": "AxisFlying",
        "price_php": 504,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.4,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "betafpv-pagoda-4",
        "category": "antenna",
        "name": "Pagoda 4 5.8GHz",
        "brand": "BetaFPV",
        "price_php": 560,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
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
