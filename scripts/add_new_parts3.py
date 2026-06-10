#!/usr/bin/env python3
"""Add a third batch of 33 new FPV parts (3 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (3) ─────────────────────────────────────────────────────────────
    {
        "id": "iflight-nazgul-evoque-f5-v2-frame",
        "category": "frame",
        "name": "Nazgul Evoque F5 V2 5\" Frame",
        "brand": "iFlight",
        "price_php": 3800,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30
        }
    },
    {
        "id": "tbs-source-one-v4-frame",
        "category": "frame",
        "name": "Source One V4 5\" Frame",
        "brand": "TBS",
        "price_php": 1254,
        "weight_g": 75,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#0d0d0d",
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
        "id": "axisflying-cinegoo-7-frame",
        "category": "frame",
        "name": "Cinegoo 7\" Cinelifter Frame",
        "brand": "Axisflying",
        "price_php": 5700,
        "weight_g": 220,
        "in_stock": True,
        "buy_url": "https://axisflying.com",
        "color": "#0a0a0a",
        "specs": {
            "size_mm": 320,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 7,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 35
        }
    },

    # ─── MOTORS (3) ─────────────────────────────────────────────────────────────
    {
        "id": "tmotor-f1404-v3-4600kv",
        "category": "motor",
        "name": "F1404 V3 4600KV",
        "brand": "T-Motor",
        "price_php": 798,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 4600,
            "stator_size": "1404",
            "motor_mount_mm": 16,
            "min_voltage_s": 2,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 15
        }
    },
    {
        "id": "brotherhobby-avenger-2208-1300kv",
        "category": "motor",
        "name": "Avenger V4 2208.5 1300KV",
        "brand": "BrotherHobby",
        "price_php": 1083,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1300,
            "stator_size": "2208",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "flywoo-nin-2207-1900kv",
        "category": "motor",
        "name": "NIN 2207 1900KV",
        "brand": "Flywoo",
        "price_php": 912,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 43
        }
    },

    # ─── ESC (3) ────────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-50a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 2622,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "flywoo-goku-gn-745-50a",
        "category": "esc",
        "name": "GOKU GN 745 50A 4-in-1 ESC",
        "brand": "Flywoo",
        "price_php": 2280,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 60
        }
    },
    {
        "id": "mamba-f45-mini-45a-4in1",
        "category": "esc",
        "name": "F45 Mini 4-in-1 45A ESC",
        "brand": "Diatone",
        "price_php": 1995,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },

    # ─── FLIGHT CONTROLLERS (3) ─────────────────────────────────────────────────
    {
        "id": "speedybee-tcmm-h743",
        "category": "fc",
        "name": "TCMM H743 Bullet Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 5700,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#002244",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "flywoo-goku-f405-hd-aio",
        "category": "fc",
        "name": "GOKU F405 HD AIO V2",
        "brand": "Flywoo",
        "price_php": 2850,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
        "specs": {
            "gyro": "MPU6000",
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
        "id": "diatone-mamba-f722-mk2",
        "category": "fc",
        "name": "Mamba F722 Mk2 Flight Controller",
        "brand": "Diatone",
        "price_php": 2394,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM20689",
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

    # ─── PROPELLERS (3) ─────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-5125-3blade",
        "category": "propeller",
        "name": "Hurricane 5125 3-Blade",
        "brand": "Gemfan",
        "price_php": 171,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "gemfan-windancer-5126-3blade",
        "category": "propeller",
        "name": "Windancer 5126 3-Blade",
        "brand": "Gemfan",
        "price_php": 178,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "ethix-s5-prop",
        "category": "propeller",
        "name": "S5 5\" 3-Blade Prop",
        "brand": "Ethix",
        "price_php": 256,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 3.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["purple", "white"]
        }
    },

    # ─── CAMERAS (3) ────────────────────────────────────────────────────────────
    {
        "id": "runcam-link-wasp",
        "category": "camera",
        "name": "Link Wasp HD Digital Camera",
        "brand": "RunCam",
        "price_php": 4845,
        "weight_g": 7.6,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Digital",
            "video_system": "RunCam Link",
            "resolution": "1080p60fps",
            "voltage_range": "6-28V"
        }
    },
    {
        "id": "foxeer-toothless-2-mini",
        "category": "camera",
        "name": "Toothless V2 Mini Camera",
        "brand": "Foxeer",
        "price_php": 1140,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS Super HAD II",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-ratel-pro-nano",
        "category": "camera",
        "name": "Ratel Pro Nano Camera",
        "brand": "Caddx",
        "price_php": 1653,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" Starlight CMOS",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },

    # ─── VTX (3) ────────────────────────────────────────────────────────────────
    {
        "id": "hglrc-sirius-1w-vtx",
        "category": "vtx",
        "name": "Sirius 5.8GHz 1W VTX",
        "brand": "HGLRC",
        "price_php": 1995,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "caddx-vista-hd-vtx",
        "category": "vtx",
        "name": "Vista HD Digital VTX",
        "brand": "Caddx",
        "price_php": 5130,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com",
        "color": "#111111",
        "specs": {
            "power_mw_max": 700,
            "protocol": "Digital",
            "video_system": "DJI O3",
            "voltage_range": "7-25.2V",
            "connector": "U.FL"
        }
    },
    {
        "id": "iflight-blackbird-vtx",
        "category": "vtx",
        "name": "Blackbird 5.8GHz VTX",
        "brand": "iFlight",
        "price_php": 1710,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "6-24V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (3) ──────────────────────────────────────────────────────────
    {
        "id": "cnhl-mini-tank-4s-1500-100c",
        "category": "battery",
        "name": "MiniTank 4S 1500mAh 100C",
        "brand": "CNHL",
        "price_php": 1311,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://chinahobbyline.com",
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
        "id": "tattu-rline-v5-6s-1300-150c",
        "category": "battery",
        "name": "R-Line V5 6S 1300mAh 150C",
        "brand": "Tattu",
        "price_php": 2964,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "betafpv-2s-300mah-75c",
        "category": "battery",
        "name": "2S 300mAh 75C LiPo",
        "brand": "BetaFPV",
        "price_php": 285,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a1a2e",
        "specs": {
            "cell_count_s": 2,
            "capacity_mah": 300,
            "c_rating": 75,
            "connector": "PH2.0",
            "voltage_nominal": 7.4
        }
    },

    # ─── RECEIVERS (3) ──────────────────────────────────────────────────────────
    {
        "id": "radiomaster-rp4-elrs",
        "category": "receiver",
        "name": "RP4TD 2.4GHz ELRS Diversity RX",
        "brand": "RadioMaster",
        "price_php": 798,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "tbs-crossfire-diversity-nano-v2",
        "category": "receiver",
        "name": "Crossfire Diversity Nano RX V2",
        "brand": "TBS",
        "price_php": 2052,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com",
        "color": "#220000",
        "specs": {
            "protocol": "TBS Crossfire",
            "frequency_mhz": 900,
            "diversity": True,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "happymodel-ex2-elrs",
        "category": "receiver",
        "name": "EX2 2.4GHz ELRS RX",
        "brand": "Happymodel",
        "price_php": 570,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.happymodel.cn",
        "color": "#1a0011",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 25
        }
    },

    # ─── GPS MODULES (3) ────────────────────────────────────────────────────────
    {
        "id": "hglrc-m100-5883-gps",
        "category": "gps",
        "name": "M100-5883 GPS+Compass",
        "brand": "HGLRC",
        "price_php": 1368,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "radiomaster-r88-gps",
        "category": "gps",
        "name": "R88 GPS Module",
        "brand": "RadioMaster",
        "price_php": 1197,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
        "specs": {
            "constellation": "GPS+GLONASS+BDS",
            "chipset": "u-blox M8",
            "update_rate_hz": 18,
            "fix_time_s": 29,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "iflight-gps-m8",
        "category": "gps",
        "name": "iFlight M8 GPS Module",
        "brand": "iFlight",
        "price_php": 912,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-SH 4-pin"
        }
    },

    # ─── ANTENNAS (3) ───────────────────────────────────────────────────────────
    {
        "id": "truerc-singularity-58",
        "category": "antenna",
        "name": "Singularity 5.8GHz RHCP",
        "brand": "TrueRC",
        "price_php": 1140,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://truerc.ca",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "foxeer-lollipop-4-58",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP",
        "brand": "Foxeer",
        "price_php": 513,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "stubby"
        }
    },
    {
        "id": "rushfpv-cherry-58",
        "category": "antenna",
        "name": "Cherry 5.8GHz RHCP",
        "brand": "RushFPV",
        "price_php": 855,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
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
