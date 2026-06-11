#!/usr/bin/env python3
"""Add a seventh batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "iflight-titan-5-v2",
        "category": "frame",
        "name": "Titan 5 V2 Frame",
        "brand": "iFlight",
        "price_php": 2599,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+titan+5"
        }
    },
    {
        "id": "flywoo-firefly-hd-nano",
        "category": "frame",
        "name": "Firefly HD Nano 2.5\" Frame",
        "brand": "Flywoo",
        "price_php": 1699,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 110,
            "motor_mount_mm": 13,
            "prop_clearance_inch": 2.5,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 18,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+firefly+nano"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "emax-rsii-2306-5-1900kv",
        "category": "motor",
        "name": "RSII 2306.5 1900KV",
        "brand": "EMAX",
        "price_php": 1250,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 39
        }
    },
    {
        "id": "iflight-xinge-pro-2207-2700kv",
        "category": "motor",
        "name": "XING-E Pro 2207 2700KV",
        "brand": "iFlight",
        "price_php": 1150,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 2700,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "speedybee-bls-60a-4in1-esc",
        "category": "esc",
        "name": "BLS 60A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2599,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#1a1a1a",
        "specs": {
            "current_rating_a": 60,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "firmware": "BLHeli_S",
            "mount_pattern_mm": 30,
            "protocols": "DShot600/300/150"
        }
    },
    {
        "id": "flycolor-raptor-stower-60a-esc",
        "category": "esc",
        "name": "Raptor S-Tower 60A 4-in-1 ESC",
        "brand": "Flycolor",
        "price_php": 2750,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "current_rating_a": 60,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "firmware": "BLHeli_32",
            "mount_pattern_mm": 30,
            "protocols": "DShot1200/600/300"
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ──────────────────────────────────────────────────
    {
        "id": "betafpv-f7-v2-35a-aio-fc",
        "category": "fc",
        "name": "F7 V2 35A AIO Flight Controller",
        "brand": "BetaFPV",
        "price_php": 3399,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "mcu": "STM32F722",
            "gyro": "ICM42688P",
            "mount_pattern_mm": 25.5,
            "uart_count": 6,
            "blackbox": "16MB flash",
            "betaflight_target": "BETAFPVF7"
        }
    },
    {
        "id": "skystars-f7-hd-pro-fc",
        "category": "fc",
        "name": "F7 HD Pro Flight Controller",
        "brand": "SkyStars",
        "price_php": 3099,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "mcu": "STM32F722",
            "gyro": "ICM20689",
            "mount_pattern_mm": 30.5,
            "uart_count": 7,
            "blackbox": "32MB flash",
            "betaflight_target": "SKYSTARSF7HDPRO"
        }
    },

    # ─── PROPELLERS (2) ──────────────────────────────────────────────────────────
    {
        "id": "hqprop-christmas-tree-5x4-3x3",
        "category": "propeller",
        "name": "Christmas Tree 5X4.3X3 (4pcs)",
        "brand": "HQProp",
        "price_php": 230,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a1a1a",
        "specs": {
            "size_inch": 5,
            "pitch_inch": 4.3,
            "blade_count": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },
    {
        "id": "xoar-pjp-5045-bullnose",
        "category": "propeller",
        "name": "PJP 5045 Bullnose (4pcs)",
        "brand": "Xoar",
        "price_php": 280,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_inch": 5,
            "pitch_inch": 4.5,
            "blade_count": 3,
            "hub_bore_mm": 1.5,
            "material": "polycarbonate"
        }
    },

    # ─── FPV CAMERAS (2) ─────────────────────────────────────────────────────────
    {
        "id": "runcam-hybrid-3-camera",
        "category": "camera",
        "name": "Hybrid 3 Camera (Analog + 4K Recording)",
        "brand": "RunCam",
        "price_php": 3950,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/2\" CMOS",
            "tvl": 1000,
            "fov_deg": 165,
            "voltage_range": "5-20V",
            "format": "4K30fps recording + analog"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-camera-module",
        "category": "camera",
        "name": "Avatar HD V3 Camera Module",
        "brand": "Walksnail",
        "price_php": 3100,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "tvl": 1200,
            "fov_deg": 150,
            "voltage_range": "6.6-26V",
            "format": "Digital HD (1440x1080)"
        }
    },

    # ─── VIDEO TRANSMITTERS (2) ─────────────────────────────────────────────────
    {
        "id": "rushfpv-cicada-vtx",
        "category": "vtx",
        "name": "Cicada 5.8GHz VTX",
        "brand": "RushFPV",
        "price_php": 2250,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "6-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tbs-unify-evo-nano-vtx",
        "category": "vtx",
        "name": "Unify Evo Nano VTX",
        "brand": "TBS",
        "price_php": 2850,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "gensace-tattu-rline-4s-650mah",
        "category": "battery",
        "name": "Tattu R-Line V4.0 650mAh 4S 130C",
        "brand": "Gens Ace",
        "price_php": 850,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 650,
            "c_rating": 130,
            "connector": "XT30",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "cnhl-racing-3s-1000mah-100c",
        "category": "battery",
        "name": "Racing Series 1000mAh 3S 100C",
        "brand": "CNHL",
        "price_php": 750,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 1000,
            "c_rating": 100,
            "connector": "XT30",
            "voltage_nominal": 11.1
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────────
    {
        "id": "happymodel-rapidfire-elrs-rx",
        "category": "receiver",
        "name": "RapidFIRE 2.4GHz ELRS Receiver",
        "brand": "HappyModel",
        "price_php": 1000,
        "weight_g": 1.1,
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
        "id": "betafpv-elrs-nano-rx-900",
        "category": "receiver",
        "name": "ELRS Nano Receiver 900MHz",
        "brand": "BetaFPV",
        "price_php": 1100,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 40
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "holybro-pixhawk4-gps-m8n",
        "category": "gps",
        "name": "Pixhawk 4 GPS Module (M8N)",
        "brand": "Holybro",
        "price_php": 2550,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "iflight-m8q-5883-gps",
        "category": "gps",
        "name": "M8Q-5883 GPS+Compass Module",
        "brand": "iFlight",
        "price_php": 1400,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M8Q",
            "update_rate_hz": 10,
            "fix_time_s": 27,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────────
    {
        "id": "foxeer-night-hawk-antenna",
        "category": "antenna",
        "name": "Night Hawk 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 450,
        "weight_g": 3,
        "in_stock": True,
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
        "id": "betafpv-pagoda4-antenna",
        "category": "antenna",
        "name": "Pagoda 4 5.8GHz Antenna",
        "brand": "BetaFPV",
        "price_php": 560,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.4,
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
