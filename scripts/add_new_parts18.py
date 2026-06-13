#!/usr/bin/env python3
"""Add an eighteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "iflight-nazgul-evoque-f5-v2",
        "category": "frame",
        "name": "Nazgul Evoque F5 V2 Frame Kit",
        "brand": "iFlight",
        "price_php": 2850,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 223,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+nazgul+evoque+f5"
        }
    },
    {
        "id": "tbs-source-one-v5-1-5in",
        "category": "frame",
        "name": "Source One V5.1 5\"",
        "brand": "TBS",
        "price_php": 1350,
        "weight_g": 90,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 210,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+v5"
        }
    },
    {
        "id": "tmotor-f60-pro-iv-v2-1950kv",
        "category": "motor",
        "name": "F60 PRO IV V2 2207.5 1950KV",
        "brand": "T-Motor",
        "price_php": 1750,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "brotherhobby-avenger-2806-5-1700kv",
        "category": "motor",
        "name": "Avenger 2806.5 1700KV",
        "brand": "BrotherHobby",
        "price_php": 1400,
        "weight_g": 42,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2806.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "iflight-blitz-e55-4in1-55a",
        "category": "esc",
        "name": "BLITZ E55 4-in-1 55A ESC",
        "brand": "iFlight",
        "price_php": 2500,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#001a00",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "holybro-tekko32-f4-4in1-60a",
        "category": "esc",
        "name": "Tekko32 F4 4-in-1 60A ESC",
        "brand": "Holybro",
        "price_php": 4000,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "holybro-kakute-f722",
        "category": "fc",
        "name": "Kakute F722",
        "brand": "Holybro",
        "price_php": 2750,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://docs.holybro.com/flight-controller/kakute-f7-series"
        }
    },
    {
        "id": "speedybee-f405-v4",
        "category": "fc",
        "name": "F405 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 1850,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com/speedybee-f405-v4-flight-controller/"
        }
    },
    {
        "id": "gemfan-hurricane-51433",
        "category": "propeller",
        "name": "Hurricane 51433",
        "brand": "Gemfan",
        "price_php": 180,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.33,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "grey", "purple"]
        }
    },
    {
        "id": "hqprop-5x4.3x3-v1s",
        "category": "propeller",
        "name": "5x4.3x3 V1S",
        "brand": "HQProp",
        "price_php": 150,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey", "green", "orange"]
        }
    },
    {
        "id": "runcam-phoenix-2",
        "category": "camera",
        "name": "Phoenix 2",
        "brand": "RunCam",
        "price_php": 1500,
        "weight_g": 7.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-22V"
        }
    },
    {
        "id": "foxeer-razer-mini-v2",
        "category": "camera",
        "name": "Razer Mini V2",
        "brand": "Foxeer",
        "price_php": 1250,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 125,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "rushfpv-tank-solo",
        "category": "vtx",
        "name": "Tank Solo",
        "brand": "RushFPV",
        "price_php": 2300,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "6-20V",
            "connector": "MMCX"
        }
    },
    {
        "id": "foxeer-reaper-nano",
        "category": "vtx",
        "name": "Reaper Nano",
        "brand": "Foxeer",
        "price_php": 1750,
        "weight_g": 5.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 350,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-25V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-6s-1500mah",
        "category": "battery",
        "name": "Black Series 1500mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1700,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "tattu-rline-v4-6s-1300mah",
        "category": "battery",
        "name": "R-Line V4.0 1300mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2450,
        "weight_g": 192,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tbs-crossfire-nano-rx-pro",
        "category": "receiver",
        "name": "Crossfire Nano RX Pro",
        "brand": "TBS",
        "price_php": 1750,
        "weight_g": 1.6,
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
        "id": "betafpv-elrs-nano-receiver",
        "category": "receiver",
        "name": "ELRS Nano Receiver",
        "brand": "BetaFPV",
        "price_php": 850,
        "weight_g": 1,
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
        "id": "holybro-m9n-gps",
        "category": "gps",
        "name": "M9N GPS",
        "brand": "Holybro",
        "price_php": 2750,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 25,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10q-5883",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1300,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com/?portfolio=m10q-5883",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 15,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "rushfpv-cherry2-antenna",
        "category": "antenna",
        "name": "Cherry2 Antenna II",
        "brand": "RushFPV",
        "price_php": 450,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "foxeer-lollipop-3",
        "category": "antenna",
        "name": "Lollipop 3",
        "brand": "Foxeer",
        "price_php": 500,
        "weight_g": 5,
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
