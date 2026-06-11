"""Add a new round of real FPV parts across all categories (PHP pricing, ~56 PHP/USD)."""
import json

NEW_PARTS = [

    # ─── FRAMES (3) ─────────────────────────────────────────────────────────────
    {
        "id": "armattan-rooster-5",
        "category": "frame",
        "name": "Rooster 5\"",
        "brand": "Armattan",
        "price_php": 5599,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://armattanproductions.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+5"
        }
    },
    {
        "id": "impulserc-apex",
        "category": "frame",
        "name": "Apex",
        "brand": "ImpulseRC",
        "price_php": 6159,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://impulserc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=impulserc+apex"
        }
    },
    {
        "id": "flywoo-explorer-lr4",
        "category": "frame",
        "name": "Explorer LR4 V2",
        "brand": "Flywoo",
        "price_php": 3079,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 195,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },

    # ─── MOTORS (3) ─────────────────────────────────────────────────────────────
    {
        "id": "brotherhobby-avenger-2306.5",
        "category": "motor",
        "name": "Avenger 2306.5",
        "brand": "BrotherHobby",
        "price_php": 1399,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "iflight-xing2-2207",
        "category": "motor",
        "name": "XING2 2207",
        "brand": "iFlight",
        "price_php": 1230,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "emax-eco-ii-2306",
        "category": "motor",
        "name": "ECO II 2306",
        "brand": "EMAX",
        "price_php": 895,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://emaxmodel.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2400,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },

    # ─── ESCs (3) ───────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-55a",
        "category": "esc",
        "name": "Tekko32 F4 4-in-1 55A",
        "brand": "Holybro",
        "price_php": 4199,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://holybro.com",
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
        "id": "diatone-mamba-f45-128k",
        "category": "esc",
        "name": "Mamba F45_128K 45A 4-in-1",
        "brand": "Diatone",
        "price_php": 2799,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
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
        "id": "speedybee-f405-v4-50a",
        "category": "esc",
        "name": "F405 V4 50A 4-in-1 (BLS)",
        "brand": "SpeedyBee",
        "price_php": 2999,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },

    # ─── FLIGHT CONTROLLERS (3) ──────────────────────────────────────────────────
    {
        "id": "speedybee-f405-v4-fc",
        "category": "fc",
        "name": "F405 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2799,
        "weight_g": 9,
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
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com/speedybee-f405-v4-flight-controller/"
        }
    },
    {
        "id": "holybro-kakute-h7-v2",
        "category": "fc",
        "name": "Kakute H7 V2",
        "brand": "Holybro",
        "price_php": 5599,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM20689",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://holybro.com/products/kakute-h7-v2"
        }
    },
    {
        "id": "iflight-succex-e-f4",
        "category": "fc",
        "name": "SucceX-E F4 Flight Controller",
        "brand": "iFlight",
        "price_php": 1679,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#000055",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://shop.iflight.com/succex-e-f4-flight-controller"
        }
    },

    # ─── PROPELLERS (3) ──────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-51466",
        "category": "propeller",
        "name": "Hurricane 51466",
        "brand": "Gemfan",
        "price_php": 279,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.66,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey",
                "green",
                "purple"
            ]
        }
    },
    {
        "id": "dal-cyclone-t5047c",
        "category": "propeller",
        "name": "Cyclone T5047C",
        "brand": "DAL",
        "price_php": 245,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "white",
                "orange"
            ]
        }
    },
    {
        "id": "hqprop-dp-5x4.3x3-v1s",
        "category": "propeller",
        "name": "DP 5x4.3x3 V1S",
        "brand": "HQProp",
        "price_php": 223,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "blue",
                "red"
            ]
        }
    },

    # ─── FPV CAMERAS (3) ─────────────────────────────────────────────────────────
    {
        "id": "caddx-ratel-2",
        "category": "camera",
        "name": "Ratel 2",
        "brand": "Caddx",
        "price_php": 1849,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-razer-mini",
        "category": "camera",
        "name": "Razer Mini",
        "brand": "Foxeer",
        "price_php": 1399,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-racer-nano-3",
        "category": "camera",
        "name": "Racer Nano 3",
        "brand": "RunCam",
        "price_php": 1259,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },

    # ─── VIDEO TRANSMITTERS (3) ──────────────────────────────────────────────────
    {
        "id": "hglrc-sirius-2.5w",
        "category": "vtx",
        "name": "Sirius 2.5W VTX",
        "brand": "HGLRC",
        "price_php": 2519,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-forcevtx-5.8g-2w",
        "category": "vtx",
        "name": "ForceVTX 5.8G 2W",
        "brand": "iFlight",
        "price_php": 2239,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "speedybee-tx800-vtx",
        "category": "vtx",
        "name": "TX800 VTX",
        "brand": "SpeedyBee",
        "price_php": 1959,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "6-24V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (3) ───────────────────────────────────────────────────────────
    {
        "id": "tattu-rline4-1300mah-6s",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S",
        "brand": "Tattu",
        "price_php": 2799,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.genstattu.com",
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
        "id": "cnhl-black-series-1300mah-6s",
        "category": "battery",
        "name": "Black Series 1300mAh 6S",
        "brand": "CNHL",
        "price_php": 2099,
        "weight_g": 240,
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
        "id": "gnb-850mah-4s",
        "category": "battery",
        "name": "850mAh 4S 100C",
        "brand": "GNB",
        "price_php": 839,
        "weight_g": 100,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 850,
            "c_rating": 100,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },

    # ─── RC RECEIVERS (3) ────────────────────────────────────────────────────────
    {
        "id": "betafpv-elrs-lite-rx",
        "category": "receiver",
        "name": "ELRS Lite Receiver",
        "brand": "BetaFPV",
        "price_php": 559,
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
        "id": "tbs-crossfire-nano-rx",
        "category": "receiver",
        "name": "Crossfire Nano RX",
        "brand": "TBS",
        "price_php": 1679,
        "weight_g": 1.6,
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
    {
        "id": "happymodel-ex-receiver",
        "category": "receiver",
        "name": "EP1 ELRS Receiver",
        "brand": "HappyModel",
        "price_php": 783,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },

    # ─── GPS MODULES (2) ─────────────────────────────────────────────────────────
    {
        "id": "betafpv-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "BetaFPV",
        "price_php": 1119,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 24,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "holybro-micro-m10-gps",
        "category": "gps",
        "name": "Micro M10 GPS",
        "brand": "Holybro",
        "price_php": 1399,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 23,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (3) ────────────────────────────────────────────────────────
    {
        "id": "immersionrc-axii-2",
        "category": "antenna",
        "name": "AXII 2 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 1119,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omnidirectional"
        }
    },
    {
        "id": "foxeer-lollipop-4",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz",
        "brand": "Foxeer",
        "price_php": 504,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omnidirectional"
        }
    },
    {
        "id": "rushfpv-cherry-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz Antenna",
        "brand": "Rush",
        "price_php": 448,
        "weight_g": 3,
        "in_stock": True,
        "buy_url": "https://rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "MMCX",
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
