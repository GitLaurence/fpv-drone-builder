#!/usr/bin/env python3
"""Add a fifth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "flywoo-explorer-lr4-frame",
        "category": "frame",
        "name": "Explorer LR4 Frame",
        "brand": "Flywoo",
        "price_php": 1899,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 178,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "axisflying-cinerace-frame",
        "category": "frame",
        "name": "CineRace 4K Frame",
        "brand": "Axisflying",
        "price_php": 2349,
        "weight_g": 82,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 185,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+cinerace"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "tmotor-f60pro4-2207-1950kv",
        "category": "motor",
        "name": "F60 Pro IV 2207 1950KV",
        "brand": "T-Motor",
        "price_php": 1549,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },
    {
        "id": "flywoo-nin-2207-1950kv",
        "category": "motor",
        "name": "NIN 2207 1950KV Motor",
        "brand": "Flywoo",
        "price_php": 1199,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 39
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "tmotor-f55a-pro2-4in1",
        "category": "esc",
        "name": "F55A PRO II 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 3349,
        "weight_g": 29,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "aikon-aks55-4in1",
        "category": "esc",
        "name": "AK32 55A 4-in-1 ESC",
        "brand": "Aikon",
        "price_php": 2649,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://aikon-electronics.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ─────────────────────────────────────────────────
    {
        "id": "flywoo-goku-f405-fc",
        "category": "fc",
        "name": "GOKU F405 Pro Flight Controller",
        "brand": "Flywoo",
        "price_php": 2099,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "geprc-takerf722-fc",
        "category": "fc",
        "name": "TAKER F722 Flight Controller",
        "brand": "GEPRC",
        "price_php": 2549,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 7,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "hqprop-ethix-s5",
        "category": "propeller",
        "name": "Ethix S5 Propeller",
        "brand": "HQProp",
        "price_php": 299,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "white"]
        }
    },
    {
        "id": "hqprop-dp5x4x3",
        "category": "propeller",
        "name": "DP 5x4x3 Durable Propeller",
        "brand": "HQProp",
        "price_php": 219,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "orange"]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────────
    {
        "id": "foxeer-toothless-v2",
        "category": "camera",
        "name": "Toothless V2 Camera",
        "brand": "Foxeer",
        "price_php": 1599,
        "weight_g": 6,
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
        "id": "runcam-phoenix2",
        "category": "camera",
        "name": "Phoenix 2 Camera",
        "brand": "RunCam",
        "price_php": 1349,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },

    # ─── VIDEO TRANSMITTERS (2) ─────────────────────────────────────────────────
    {
        "id": "tbs-unify-evo-pro-vtx",
        "category": "vtx",
        "name": "Unify EVO Pro VTX",
        "brand": "TBS",
        "price_php": 4699,
        "weight_g": 5.6,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6.5-28V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-tranporter-vtx",
        "category": "vtx",
        "name": "Transporter V2 VTX",
        "brand": "iFlight",
        "price_php": 1699,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "tattu-rline4-6s-1300mah",
        "category": "battery",
        "name": "R-Line V4.0 1300mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2399,
        "weight_g": 247,
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
        "id": "cnhl-rline-6s-1500mah",
        "category": "battery",
        "name": "R-Line 1500mAh 6S 150C",
        "brand": "CNHL",
        "price_php": 2299,
        "weight_g": 280,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1500,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────────
    {
        "id": "radiomaster-er6-elrs-rx",
        "category": "receiver",
        "name": "ER6 2.4GHz ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 999,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "tbs-crossfire-diversity-nano",
        "category": "receiver",
        "name": "Crossfire Diversity Nano RX",
        "brand": "TBS",
        "price_php": 1599,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 915,
            "telemetry": True,
            "range_km": 40
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "matek-m10q-5883-gps",
        "category": "gps",
        "name": "M10Q-5883 GPS+Compass",
        "brand": "Matek",
        "price_php": 1699,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "foxeer-gps-2",
        "category": "gps",
        "name": "GPS-2 Module",
        "brand": "Foxeer",
        "price_php": 1199,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────────
    {
        "id": "truerc-xair",
        "category": "antenna",
        "name": "X-Air 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 899,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omnidirectional"
        }
    },
    {
        "id": "immersionrc-skew-planar",
        "category": "antenna",
        "name": "Skew Planar 5.8GHz Antenna",
        "brand": "ImmersionRC",
        "price_php": 599,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
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
