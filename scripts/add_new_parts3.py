#!/usr/bin/env python3
"""Add a third batch of 33 new FPV parts (3 per category) to parts.json"""
import json

NEW_PARTS = [
    # ─── FRAMES (3) ─────────────────────────────────────────────────────────────
    {
        "id": "flywoo-explorer-lr7",
        "category": "frame",
        "name": "Explorer LR7 V2 7\" Long Range Frame",
        "brand": "Flywoo",
        "price_php": 4060,
        "weight_g": 145,
        "in_stock": True,
        "buy_url": "https://flywoo.net",
        "color": "#0d0d0d",
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
        "id": "arris-x220-frame",
        "category": "frame",
        "name": "X220 V2 5\" Racing Frame",
        "brand": "ARRIS",
        "price_php": 2030,
        "weight_g": 120,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "jb-hobby-strafe-5",
        "category": "frame",
        "name": "Strafe 5\" Freestyle Frame",
        "brand": "JB Hobby",
        "price_php": 2610,
        "weight_g": 68,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#141414",
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

    # ─── MOTORS (3) ─────────────────────────────────────────────────────────────
    {
        "id": "tmotor-velox-2207-5",
        "category": "motor",
        "name": "Velox 2207.5 1900KV",
        "brand": "T-Motor",
        "price_php": 1334,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 44
        }
    },
    {
        "id": "xnova-freestylerexx-2306",
        "category": "motor",
        "name": "Freestylerexx 2306 1900KV",
        "brand": "Xnova",
        "price_php": 1566,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.xnovamotor.com",
        "color": "#0a0a0a",
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
        "id": "rcinpower-gts-v3-2306",
        "category": "motor",
        "name": "GTS V3 2306 1850KV",
        "brand": "RCinPower",
        "price_php": 1450,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1850,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },

    # ─── ESC (3) ────────────────────────────────────────────────────────────────
    {
        "id": "holybro-tekko32-f4-50a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 50A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 3190,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "aikon-aks35-bit-50a",
        "category": "esc",
        "name": "AK32BITX 35A 4-in-1 ESC",
        "brand": "Aikon",
        "price_php": 2320,
        "weight_g": 22,
        "in_stock": True,
        "buy_url": "https://www.aikonrc.com",
        "color": "#0a0a0a",
        "specs": {
            "amp_rating": 35,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 45
        }
    },
    {
        "id": "spedix-es35-50a",
        "category": "esc",
        "name": "ES35 50A 4-in-1 ESC",
        "brand": "Spedix",
        "price_php": 2784,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },

    # ─── FLIGHT CONTROLLERS (3) ─────────────────────────────────────────────────
    {
        "id": "mamba-f405-mk2-stack-fc",
        "category": "fc",
        "name": "F405 MK2 Flight Controller",
        "brand": "Diatone",
        "price_php": 2030,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#1c1c1c",
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
        "id": "foxeer-f722-v4",
        "category": "fc",
        "name": "F722 V4 Mini Flight Controller",
        "brand": "Foxeer",
        "price_php": 2320,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/foxeer-f722-v4-dual-bec-5v-10v-hv-8s-mini-flight-controller-g-455",
        "color": "#111",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "airbot-f7-mini",
        "category": "fc",
        "name": "F7 Mini Flight Controller",
        "brand": "Airbot",
        "price_php": 2610,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#0a0a0a",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 4,
            "5v_pad_count": 1,
            "curr_sensor": False
        }
    },

    # ─── PROPELLERS (3) ─────────────────────────────────────────────────────────
    {
        "id": "gemfan-hurricane-durable-51466",
        "category": "propeller",
        "name": "Hurricane Durable 51466 3-Blade",
        "brand": "Gemfan",
        "price_php": 174,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.66,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "tmotor-t5147-tri-blade",
        "category": "propeller",
        "name": "T5147 5\" Tri-Blade Props",
        "brand": "T-Motor",
        "price_php": 290,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.7,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "grey"]
        }
    },
    {
        "id": "azure-power-lambo-5040",
        "category": "propeller",
        "name": "Lambo 5040 3-Blade",
        "brand": "Azure Power",
        "price_php": 174,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.0,
            "pitch": 4.0,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "white", "purple"]
        }
    },

    # ─── CAMERAS (3) ────────────────────────────────────────────────────────────
    {
        "id": "runcam-racer-3-nano",
        "category": "camera",
        "name": "Racer 3 Nano FPV Camera",
        "brand": "RunCam",
        "price_php": 1450,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.runcam.com",
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
        "id": "eachine-rapidfire-cam",
        "category": "camera",
        "name": "RapidFire Mini FPV Camera",
        "brand": "Eachine",
        "price_php": 1160,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 150,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-rush-nano-pro",
        "category": "camera",
        "name": "Rush Nano Pro FPV Camera",
        "brand": "Foxeer",
        "price_php": 1276,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },

    # ─── VTX (3) ────────────────────────────────────────────────────────────────
    {
        "id": "hglrc-zeus-vtx-5-8",
        "category": "vtx",
        "name": "Zeus 5.8GHz VTX 800mW",
        "brand": "HGLRC",
        "price_php": 1450,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/products/hglrc-zeus-vtx",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "MMCX"
        }
    },
    {
        "id": "foxeer-tm25-plus",
        "category": "vtx",
        "name": "TM25 Plus 25/200/500mW VTX",
        "brand": "Foxeer",
        "price_php": 870,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/foxeer-tm25-5-8g-25-200-500mw-switchable-vtx",
        "color": "#111",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-22V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-twr-vtx-v2",
        "category": "vtx",
        "name": "TWR-VTX V2 5.8GHz",
        "brand": "iFlight",
        "price_php": 1740,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#0a0a0a",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },

    # ─── BATTERIES (3) ──────────────────────────────────────────────────────────
    {
        "id": "tattu-rline-4s-1800",
        "category": "battery",
        "name": "R-Line V5 4S 1800mAh 150C",
        "brand": "Tattu",
        "price_php": 1856,
        "weight_g": 220,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1800,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "gnb-4s-1500-95c",
        "category": "battery",
        "name": "4S 1500mAh 95C LiPo",
        "brand": "GNB",
        "price_php": 1276,
        "weight_g": 190,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1500,
            "c_rating": 95,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "ovonic-6s-1300-100c",
        "category": "battery",
        "name": "6S 1300mAh 100C LiPo",
        "brand": "Ovonic",
        "price_php": 1972,
        "weight_g": 250,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/ovonic-1300mah-6s-100c-lipo-battery-xt60.html",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },

    # ─── RECEIVERS (3) ──────────────────────────────────────────────────────────
    {
        "id": "frsky-r9-mm-rx",
        "category": "receiver",
        "name": "R9 MM 900MHz Long Range RX",
        "brand": "FrSky",
        "price_php": 1450,
        "weight_g": 1.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/frsky-r9mm-900mhz-long-range-receiver.html",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "FrSky ACCST",
            "frequency_mhz": 900,
            "diversity": False,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "jumper-r1-elrs-rx",
        "category": "receiver",
        "name": "R1 Nano ELRS RX",
        "brand": "Jumper",
        "price_php": 754,
        "weight_g": 1,
        "in_stock": True,
        "buy_url": "https://www.jumper-rc.com/products/r1-nano-elrs-receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "radiomaster-rp1-elrs-rx",
        "category": "receiver",
        "name": "RP1 2.4GHz ELRS Nano RX",
        "brand": "RadioMaster",
        "price_php": 580,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#001a00",
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
        "id": "beitian-bn-220-gps",
        "category": "gps",
        "name": "BN-220 GPS+GLONASS Module",
        "brand": "Beitian",
        "price_php": 870,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/beitian-bn-220-gps-glonass-module.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 32,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "holybro-m8n-gps-v2",
        "category": "gps",
        "name": "M8N GPS Module",
        "brand": "Holybro",
        "price_php": 1740,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://holybro.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "readytosky-gps-m8n",
        "category": "gps",
        "name": "GPS M8N w/ Compass",
        "brand": "Readytosky",
        "price_php": 1044,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },

    # ─── ANTENNAS (3) ───────────────────────────────────────────────────────────
    {
        "id": "lumenier-axii2-rhcp",
        "category": "antenna",
        "name": "AXII 2 5.8GHz RHCP",
        "brand": "Lumenier",
        "price_php": 870,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "foxeer-lollipop-4-rhcp",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP",
        "brand": "Foxeer",
        "price_php": 696,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/foxeer-lollipop-4-5-8g-fpv-antenna-g-304.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "stubby"
        }
    },
    {
        "id": "realacc-cloverleaf-rhcp",
        "category": "antenna",
        "name": "5.8GHz Cloverleaf RHCP",
        "brand": "RealAcc",
        "price_php": 464,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.0,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "cloverleaf"
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
