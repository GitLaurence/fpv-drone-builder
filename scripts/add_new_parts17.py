#!/usr/bin/env python3
"""Add a new batch of real FPV parts across all 11 categories."""
import json

NEW_PARTS = [
    {
        "id": "iflight-cidora-sl5c",
        "category": "frame",
        "name": "Cidora SL5C 5\" Semi-LR Frame",
        "brand": "iFlight",
        "price_php": 3200,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 235,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+cidora+sl5c"
        }
    },
    {
        "id": "axisflying-c229-v2",
        "category": "frame",
        "name": "C229 V2 5\" Frame",
        "brand": "AxisFlying",
        "price_php": 3450,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 229,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+c229"
        }
    },
    {
        "id": "tmotor-velox-v3-1404",
        "category": "motor",
        "name": "Velox V3 1404 4500KV",
        "brand": "T-Motor",
        "price_php": 950,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 4500,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 20
        }
    },
    {
        "id": "brotherhobby-returner-r7-2306",
        "category": "motor",
        "name": "Returner R7 2306 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1450,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "speedybee-f405-v4-bls-60a-esc",
        "category": "esc",
        "name": "F405 V4 BLS 60A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2300,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
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
        "id": "flywoo-goku-60a-4in1-pro",
        "category": "esc",
        "name": "GOKU 60A 4-in-1 ESC Pro",
        "brand": "Flywoo",
        "price_php": 2650,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
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
        "id": "speedybee-f745-v4-aio-fc",
        "category": "fc",
        "name": "F745 V4 AIO FC",
        "brand": "SpeedyBee",
        "price_php": 2900,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000044",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "diatone-mamba-f722-mk4",
        "category": "fc",
        "name": "Mamba F722 MK4 FC",
        "brand": "Diatone",
        "price_php": 2100,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#000044",
        "specs": {
            "gyro": "ICM42688P",
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
        "id": "hqprop-light-5x4x3",
        "category": "propeller",
        "name": "Light 5x4x3",
        "brand": "HQProp",
        "price_php": 195,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "orange"]
        }
    },
    {
        "id": "gemfan-hurricane-dc-51466",
        "category": "propeller",
        "name": "Hurricane DC 51466",
        "brand": "Gemfan",
        "price_php": 290,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.gemfan.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.66,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "foxeer-nightwolf-2-v2",
        "category": "camera",
        "name": "Nightwolf 2 V2",
        "brand": "Foxeer",
        "price_php": 2150,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "6-28V"
        }
    },
    {
        "id": "runcam-phoenix-2-vision",
        "category": "camera",
        "name": "Phoenix 2 Vision",
        "brand": "RunCam",
        "price_php": 1850,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 160,
            "format": "Analog/Digital",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "iflight-tws-1-5w-vtx",
        "category": "vtx",
        "name": "TWS 1.5W VTX",
        "brand": "iFlight",
        "price_php": 2600,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "rush-tank-solo-v5",
        "category": "vtx",
        "name": "Tank Solo V5 1000mW",
        "brand": "RushFPV",
        "price_php": 1750,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "gnb-4s-1300mah-80c",
        "category": "battery",
        "name": "1300mAh 4S 80C",
        "brand": "GNB",
        "price_php": 850,
        "weight_g": 158,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 80,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tattu-rline-3-1550mah-4s",
        "category": "battery",
        "name": "R-Line 3.0 1550mAh 4S",
        "brand": "Tattu",
        "price_php": 1150,
        "weight_g": 178,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1550,
            "c_rating": 95,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "diatone-mamba-elrs-rx",
        "category": "receiver",
        "name": "Mamba ELRS Nano RX 2.4GHz",
        "brand": "Diatone",
        "price_php": 920,
        "weight_g": 1.5,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "iflight-elrs-nano-rx-v3",
        "category": "receiver",
        "name": "ELRS Nano RX V3",
        "brand": "iFlight",
        "price_php": 980,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "betafpv-m9n-nano-gps",
        "category": "gps",
        "name": "M9N Nano GPS",
        "brand": "BetaFPV",
        "price_php": 1350,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "speedybee-m8n-gps",
        "category": "gps",
        "name": "M8N GPS",
        "brand": "SpeedyBee",
        "price_php": 1200,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "immersionrc-spironet-v4",
        "category": "antenna",
        "name": "SpiroNet V4 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 1100,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
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
        "id": "menace-atlas-5-8",
        "category": "antenna",
        "name": "Atlas 5.8GHz Antenna",
        "brand": "Menace Antennas",
        "price_php": 1250,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 7.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
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
