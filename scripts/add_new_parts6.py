#!/usr/bin/env python3
"""Add a sixth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (2) ─────────────────────────────────────────────────────────────
    {
        "id": "iflight-nazgul5-v3-frame",
        "category": "frame",
        "name": "Nazgul5 V3 Frame Kit",
        "brand": "iFlight",
        "price_php": 2199,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 224,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+nazgul5"
        }
    },
    {
        "id": "flywoo-firefly-x1-frame",
        "category": "frame",
        "name": "Firefly X1 Nano Frame",
        "brand": "Flywoo",
        "price_php": 1449,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 100,
            "motor_mount_mm": 13,
            "prop_clearance_inch": 2,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2,
            "standoff_height_mm": 16,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+firefly+x1"
        }
    },

    # ─── MOTORS (2) ─────────────────────────────────────────────────────────────
    {
        "id": "tmotor-velox-vt2806-5-1300kv",
        "category": "motor",
        "name": "VELOX VT2806.5 1300KV",
        "brand": "T-Motor",
        "price_php": 1849,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2806.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 5,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-1900kv",
        "category": "motor",
        "name": "Avenger 2306.5 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1399,
        "weight_g": 32,
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
            "peak_current_a": 43
        }
    },

    # ─── ESCs (2) ───────────────────────────────────────────────────────────────
    {
        "id": "mamba-f45-128k-4in1-esc",
        "category": "esc",
        "name": "F45_128K 45A 4-in-1 ESC",
        "brand": "Mamba",
        "price_php": 2599,
        "weight_g": 24,
        "in_stock": True,
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
        "id": "speedybee-60a-4in1-esc",
        "category": "esc",
        "name": "60A BLHeli_32 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 3299,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },

    # ─── FLIGHT CONTROLLERS (2) ───────────────────────────────────────────────────
    {
        "id": "geprc-taker-g4-fc",
        "category": "fc",
        "name": "TAKER G4 Flight Controller",
        "brand": "GEPRC",
        "price_php": 1899,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://geprc.com",
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
            "curr_sensor": True,
            "diagram_url": "https://geprc.com"
        }
    },
    {
        "id": "mamba-f405-mk2-fc",
        "category": "fc",
        "name": "F405 MK2 Flight Controller",
        "brand": "Mamba",
        "price_php": 2199,
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
            "uart_count": 6,
            "5v_pad_count": 3,
            "curr_sensor": True,
            "diagram_url": "https://www.getfpv.com"
        }
    },

    # ─── PROPELLERS (2) ─────────────────────────────────────────────────────────
    {
        "id": "dalprop-cyclone-t5040c",
        "category": "propeller",
        "name": "Cyclone T5040C",
        "brand": "Dalprop",
        "price_php": 199,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "gray",
                "orange"
            ]
        }
    },
    {
        "id": "hqprop-dp-6x4.5x3",
        "category": "propeller",
        "name": "DP 6×4.5×3",
        "brand": "HQProp",
        "price_php": 249,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "blue",
                "red"
            ]
        }
    },

    # ─── FPV CAMERAS (2) ────────────────────────────────────────────────────────
    {
        "id": "runcam-racer-nano",
        "category": "camera",
        "name": "Racer Nano",
        "brand": "RunCam",
        "price_php": 999,
        "weight_g": 3.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-falkor-2-mini",
        "category": "camera",
        "name": "Falkor 2 Mini",
        "brand": "Foxeer",
        "price_php": 1399,
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

    # ─── VIDEO TRANSMITTERS (2) ───────────────────────────────────────────────────
    {
        "id": "rush-tank-solo-vtx",
        "category": "vtx",
        "name": "Tank Solo VTX",
        "brand": "Rush",
        "price_php": 1799,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-forcevtx-1g3",
        "category": "vtx",
        "name": "ForceVTX 1G3",
        "brand": "iFlight",
        "price_php": 3499,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "1.3GHz",
            "voltage_range": "7-26V",
            "connector": "SMA"
        }
    },

    # ─── BATTERIES (2) ──────────────────────────────────────────────────────────
    {
        "id": "tattu-rline-v5-1300mah-6s",
        "category": "battery",
        "name": "R-Line V5 1300mAh 6S 130C",
        "brand": "Tattu",
        "price_php": 2599,
        "weight_g": 245,
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
        "id": "cnhl-blackseries-1300mah-4s",
        "category": "battery",
        "name": "Black Series 1300mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 999,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },

    # ─── RC RECEIVERS (2) ───────────────────────────────────────────────────────
    {
        "id": "happymodel-ep2-receiver",
        "category": "receiver",
        "name": "EP2 ELRS Receiver",
        "brand": "Happymodel",
        "price_php": 699,
        "weight_g": 1.2,
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
        "id": "frsky-r9-mm2-receiver",
        "category": "receiver",
        "name": "R9 MM2 Receiver",
        "brand": "FrSky",
        "price_php": 1499,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ACCESS",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 15
        }
    },

    # ─── GPS MODULES (2) ────────────────────────────────────────────────────────
    {
        "id": "geprc-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "GEPRC",
        "price_php": 1099,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://geprc.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 22,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "betafpv-m10-lite-gps",
        "category": "gps",
        "name": "M10 Lite GPS Module",
        "brand": "BetaFPV",
        "price_php": 899,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },

    # ─── VTX ANTENNAS (2) ───────────────────────────────────────────────────────
    {
        "id": "foxeer-lollipop-4-antenna",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 599,
        "weight_g": 5,
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
        "id": "rushfpv-cherry-antenna",
        "category": "antenna",
        "name": "Cherry 5.8GHz Antenna",
        "brand": "RushFPV",
        "price_php": 699,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
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
