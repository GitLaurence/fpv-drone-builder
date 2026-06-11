"""Add a new batch of current-generation FPV parts across all categories."""
import json

NEW_PARTS = [
    {
        "id": "iflight-xl5-v2",
        "category": "frame",
        "name": "XL5 V2",
        "brand": "iFlight",
        "price_php": 3579,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 230,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+xl5+v2"
        }
    },
    {
        "id": "flywoo-explorer-lr5-v3",
        "category": "frame",
        "name": "Explorer LR5 V3",
        "brand": "Flywoo",
        "price_php": 5849,
        "weight_g": 128,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2a2a2a",
        "specs": {
            "size_mm": 248,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr5+v3"
        }
    },
    {
        "id": "tmotor-velox-v2807.5-v2",
        "category": "motor",
        "name": "Velox V2807.5 V2",
        "brand": "T-Motor",
        "price_php": 1754,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2807.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "brotherhobby-avenger-2812-v3",
        "category": "motor",
        "name": "Avenger 2812 V3",
        "brand": "BrotherHobby",
        "price_php": 1624,
        "weight_g": 36,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2812",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 55
        }
    },
    {
        "id": "flywoo-goku-70a-aio",
        "category": "esc",
        "name": "GOKU 70A AIO 4-in-1",
        "brand": "Flywoo",
        "price_php": 3899,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#002200",
        "specs": {
            "amp_rating": 70,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 80
        }
    },
    {
        "id": "mamba-f45-mini-45a",
        "category": "esc",
        "name": "F45_Mini 45A 4-in-1",
        "brand": "Mamba",
        "price_php": 2274,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "iflight-blitz-mini-f745-aio",
        "category": "fc",
        "name": "BLITZ Mini F745 AIO",
        "brand": "iFlight",
        "price_php": 3574,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "iflight-succex-e-f722",
        "category": "fc",
        "name": "SucceX-E F722",
        "brand": "iFlight",
        "price_php": 2924,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-hurricane-5128",
        "category": "propeller",
        "name": "Hurricane 5128",
        "brand": "Gemfan",
        "price_php": 228,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "green"]
        }
    },
    {
        "id": "hqprop-dp-5x4x3-v1s",
        "category": "propeller",
        "name": "DP 5x4x3 V1S",
        "brand": "HQProp",
        "price_php": 208,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "grey"]
        }
    },
    {
        "id": "foxeer-razer-pro-mini",
        "category": "camera",
        "name": "Razer Pro Mini",
        "brand": "Foxeer",
        "price_php": 1624,
        "weight_g": 5.5,
        "in_stock": True,
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
        "id": "runcam-phoenix-2-vision",
        "category": "camera",
        "name": "Phoenix 2 Vision",
        "brand": "RunCam",
        "price_php": 2274,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2.8\" CMOS",
            "fov_deg": 160,
            "format": "Switchable",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "hdzero-race-vtx-v2",
        "category": "vtx",
        "name": "Race VTX V2",
        "brand": "HDZero",
        "price_php": 3899,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.hd-zero.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Digital HD",
            "bands": "5.8GHz",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "foxeer-tower-pro-vtx",
        "category": "vtx",
        "name": "Tower Pro VTX",
        "brand": "Foxeer",
        "price_php": 1949,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-24V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-6s-1800mah",
        "category": "battery",
        "name": "Black Series 1800mAh 6S",
        "brand": "CNHL",
        "price_php": 1624,
        "weight_g": 248,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1800,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-r-line-4-1300mah-6s-150c",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2274,
        "weight_g": 222,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "radiomaster-rp1a-elrs",
        "category": "receiver",
        "name": "RP1A ELRS RX",
        "brand": "RadioMaster",
        "price_php": 649,
        "weight_g": 1,
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
        "id": "betafpv-elrs-lite-rx-spi",
        "category": "receiver",
        "name": "ELRS Lite RX SPI",
        "brand": "BetaFPV",
        "price_php": 844,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "cubepilot-here4-gps",
        "category": "gps",
        "name": "Here4 RTK GPS",
        "brand": "CubePilot",
        "price_php": 8999,
        "weight_g": 41,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou+Galileo",
            "chipset": "u-blox ZED-F9P RTK",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-gnss",
        "category": "gps",
        "name": "M10Q GNSS",
        "brand": "Matek",
        "price_php": 1299,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 22,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "rushfpv-cherry-pro-antenna",
        "category": "antenna",
        "name": "Cherry Pro 5.8GHz Antenna",
        "brand": "Rush",
        "price_php": 649,
        "weight_g": 8,
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
    {
        "id": "axisflying-cobra-antenna",
        "category": "antenna",
        "name": "Cobra 5.8GHz Antenna",
        "brand": "AxisFlying",
        "price_php": 519,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
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
