"""
Adds a new batch of real, current FPV parts to data/parts.json.
Run with: python3 scripts/add_new_parts7.py
"""
import json

NEW_PARTS = [
    # ─── FRAMES (3) ─────────────────────────────────────────────────────────
    {
        "id": "iflight-chimera7-pro-frame",
        "category": "frame",
        "name": "Chimera7 Pro Frame Kit",
        "brand": "iFlight",
        "price_php": 6800,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.iflight-rc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 35
        }
    },
    {
        "id": "impulserc-apex-frame",
        "category": "frame",
        "name": "Apex 5\" Frame Kit",
        "brand": "ImpulseRC",
        "price_php": 5200,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://impulserc.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "flywoo-mr-croc-frame",
        "category": "frame",
        "name": "Mr. Croc 7\" Frame Kit",
        "brand": "Flywoo",
        "price_php": 3200,
        "weight_g": 125,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2d3a1a",
        "specs": {
            "size_mm": 295,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 35
        }
    },

    # ─── MOTORS (3) ─────────────────────────────────────────────────────────
    {
        "id": "tmotor-velox-v2807.5",
        "category": "motor",
        "name": "Velox V2807.5",
        "brand": "T-Motor",
        "price_php": 2400,
        "weight_g": 42,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "rcinpower-gts-v25-2306",
        "category": "motor",
        "name": "GTS V2.5 2306",
        "brand": "RCINPOWER",
        "price_php": 1450,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.rcinpower.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "flywoo-nin-1404-motor",
        "category": "motor",
        "name": "NIN 1404",
        "brand": "Flywoo",
        "price_php": 850,
        "weight_g": 11.5,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#2a2a2a",
        "specs": {
            "kv": 4600,
            "stator_size": "1404",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 3,
            "peak_current_a": 20
        }
    },

    # ─── ESCs (3) ───────────────────────────────────────────────────────────
    {
        "id": "mamba-f45-128k-mk2-4in1",
        "category": "esc",
        "name": "F45 128K MK2 4-in-1 (30x30)",
        "brand": "Mamba",
        "price_php": 2800,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#001a1a",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "tekko32-f4-50a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 (30x30)",
        "brand": "T-Motor",
        "price_php": 3100,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#001a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "flycolor-x-cross-60a-4in1",
        "category": "esc",
        "name": "X-Cross 60A 4-in-1 (30x30)",
        "brand": "FlyColor",
        "price_php": 2600,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.flycolor-tech.com",
        "color": "#001a1a",
        "specs": {
            "amp_rating": 60,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },

    # ─── FLIGHT CONTROLLERS (3) ────────────────────────────────────────────
    {
        "id": "speedybee-f405-wing-v3",
        "category": "fc",
        "name": "F405 Wing V3",
        "brand": "SpeedyBee",
        "price_php": 2700,
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
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "mamba-h743-v3",
        "category": "fc",
        "name": "H743 V3 Processor",
        "brand": "Mamba",
        "price_php": 4500,
        "weight_g": 11,
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
            "uart_count": 8,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "holybro-kakuteh7-v2-fc",
        "category": "fc",
        "name": "Kakute H7 V2",
        "brand": "Holybro",
        "price_php": 4200,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#000044",
        "specs": {
            "gyro": "ICM20689",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },

    # ─── PROPELLERS (3) ─────────────────────────────────────────────────────
    {
        "id": "hqprop-ethix-s5-v2",
        "category": "propeller",
        "name": "Ethix S5 V2",
        "brand": "HQProp",
        "price_php": 280,
        "weight_g": 4.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "black"]
        }
    },
    {
        "id": "gemfan-hurricane-durable-51499",
        "category": "propeller",
        "name": "Hurricane Durable 5149",
        "brand": "Gemfan",
        "price_php": 240,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.9,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "dalprop-cyclone-t5047c",
        "category": "propeller",
        "name": "Cyclone T5047C",
        "brand": "DALProp",
        "price_php": 220,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.dalprop.com",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.0,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "orange"]
        }
    },

    # ─── CAMERAS (3) ────────────────────────────────────────────────────────
    {
        "id": "runcam-phoenix-2-vision",
        "category": "camera",
        "name": "Phoenix 2 Vision",
        "brand": "RunCam",
        "price_php": 1850,
        "weight_g": 7.2,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "video_system": "Analog",
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-camera",
        "category": "camera",
        "name": "Avatar HD V3 Camera",
        "brand": "Walksnail",
        "price_php": 4200,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "video_system": "Walksnail",
            "voltage_range": "6-25V"
        }
    },
    {
        "id": "runcam-nano-3-camera",
        "category": "camera",
        "name": "Nano 3",
        "brand": "RunCam",
        "price_php": 950,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "video_system": "Analog",
            "voltage_range": "5-40V"
        }
    },

    # ─── VTX (3) ────────────────────────────────────────────────────────────
    {
        "id": "hglrc-titan-vtx-5w",
        "category": "vtx",
        "name": "Titan VTX 5W",
        "brand": "HGLRC",
        "price_php": 2200,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 5000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "walksnail-avatar-hd-v3-vtx",
        "category": "vtx",
        "name": "Avatar HD V3 VTX",
        "brand": "Walksnail",
        "price_php": 5400,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.walksnail.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital",
            "video_system": "Walksnail",
            "voltage_range": "6-25V",
            "connector": "U.FL"
        }
    },
    {
        "id": "rush-tank-max-solo",
        "category": "vtx",
        "name": "Tank Max Solo",
        "brand": "Rush",
        "price_php": 2900,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://rushfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-25V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (3) ──────────────────────────────────────────────────────
    {
        "id": "cnhl-black-series-1300-6s",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2300,
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
        "id": "tattu-r-line-version4-1300mah",
        "category": "battery",
        "name": "R-Line V4.0 1300mAh 6S 150C",
        "brand": "Tattu",
        "price_php": 2950,
        "weight_g": 250,
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
        "id": "gnb-30c-1500mah-4s",
        "category": "battery",
        "name": "30C 1500mAh 4S",
        "brand": "GNB",
        "price_php": 1100,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 30,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },

    # ─── RECEIVERS (3) ──────────────────────────────────────────────────────
    {
        "id": "radiomaster-er6-elrs-receiver",
        "category": "receiver",
        "name": "ER6 ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 1300,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a1a00",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "immersionrc-ghost-atto-rx",
        "category": "receiver",
        "name": "Ghost Atto RX",
        "brand": "ImmersionRC",
        "price_php": 1900,
        "weight_g": 1.0,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a00",
        "specs": {
            "protocol": "Ghost",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "happymodel-ep1-elrs-rx",
        "category": "receiver",
        "name": "EP1 ELRS Receiver",
        "brand": "Happymodel",
        "price_php": 750,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a1a00",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 10
        }
    },

    # ─── GPS (3) ────────────────────────────────────────────────────────────
    {
        "id": "holybro-st01-gps",
        "category": "gps",
        "name": "ST01 GPS+Compass",
        "brand": "Holybro",
        "price_php": 1750,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com",
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
        "id": "beitian-bn-880q-gps",
        "category": "gps",
        "name": "BN-880Q GPS+Compass",
        "brand": "Beitian",
        "price_php": 950,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.beitian.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "matek-m10-3100-gps-v2",
        "category": "gps",
        "name": "M10-3100 V2 GPS+Compass",
        "brand": "Matek",
        "price_php": 1599,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 16,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── ANTENNAS (3) ───────────────────────────────────────────────────────
    {
        "id": "tbs-axii2-stubby-antenna",
        "category": "antenna",
        "name": "Triumph Axii 2 Stubby 5.8GHz",
        "brand": "TBS",
        "price_php": 750,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
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
        "id": "foxeer-lollipop4-stubby-antenna",
        "category": "antenna",
        "name": "Lollipop 4 Stubby 5.8GHz",
        "brand": "Foxeer",
        "price_php": 399,
        "weight_g": 2.5,
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
        "price_php": 550,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://rushfpv.com",
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
