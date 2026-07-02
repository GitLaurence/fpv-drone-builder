#!/usr/bin/env python3
"""Add new real FPV parts to parts.json - Batch 49: new parts across all 11 categories."""
import json

NEW_PARTS = [
    # ========== FRAMES ==========
    {
        "id": "impulserc-apex-frame-2023",
        "category": "frame",
        "name": "Apex 5\" Frame 2023 Edition",
        "brand": "ImpulseRC",
        "price_php": 5600,
        "weight_g": 96,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImpulseRC+Apex+2023",
        "color": "#111111",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 26,
            "thingiverse_url": "https://www.thingiverse.com/search?q=impulserc+apex+2023"
        }
    },
    {
        "id": "axisflying-cinemental-v3-4inch",
        "category": "frame",
        "name": "Cinemental V3 4\" Frame",
        "brand": "Axisflying",
        "price_php": 2940,
        "weight_g": 62,
        "in_stock": True,
        "buy_url": "https://www.axisflying.com/search?q=Axisflying+Cinemental+V3+4inch",
        "color": "#151515",
        "specs": {
            "size_mm": 190,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 22,
            "thingiverse_url": "https://www.thingiverse.com/search?q=axisflying+cinemental+v3"
        }
    },
    {
        "id": "flywoo-explorer-lr6-hd-frame",
        "category": "frame",
        "name": "Explorer LR6 6\" HD Long Range Frame",
        "brand": "Flywoo",
        "price_php": 3080,
        "weight_g": 88,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+Explorer+LR6+6inch+HD",
        "color": "#1c1c1c",
        "specs": {
            "size_mm": 260,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr6"
        }
    },
    {
        "id": "hglrc-sector-cx10-10inch-frame",
        "category": "frame",
        "name": "Sector CX10 10\" Long Range Frame",
        "brand": "HGLRC",
        "price_php": 4760,
        "weight_g": 210,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Sector+CX10+10inch",
        "color": "#111111",
        "specs": {
            "size_mm": 460,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 10,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 6,
            "standoff_height_mm": 40,
            "thingiverse_url": "https://www.thingiverse.com/search?q=hglrc+sector+cx10"
        }
    },
    {
        "id": "geprc-crocodile6-hd-frame",
        "category": "frame",
        "name": "Crocodile6 HD 6\" Frame",
        "brand": "GEPRC",
        "price_php": 3360,
        "weight_g": 112,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+Crocodile6+HD",
        "color": "#151515",
        "specs": {
            "size_mm": 260,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 6,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+crocodile6"
        }
    },
    # ========== MOTORS ==========
    {
        "id": "tmotor-velox-2807-5-1300kv",
        "category": "motor",
        "name": "Velox 2807.5 1300KV",
        "brand": "T-Motor",
        "price_php": 1400,
        "weight_g": 48,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=T-Motor+Velox+2807.5+1300KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 8,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "iflight-xing-e-pro-2306-1700kv",
        "category": "motor",
        "name": "XING-E Pro 2306 1700KV",
        "brand": "iFlight",
        "price_php": 868,
        "weight_g": 31,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+XING-E+Pro+2306+1700KV",
        "color": "#1c1c1c",
        "specs": {
            "kv": 1700,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 36
        }
    },
    {
        "id": "flywoo-nin-2004-3800kv",
        "category": "motor",
        "name": "NIN 2004 3800KV",
        "brand": "Flywoo",
        "price_php": 700,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+NIN+2004+3800KV",
        "color": "#111111",
        "specs": {
            "kv": 3800,
            "stator_size": "2004",
            "motor_mount_mm": 12,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 22
        }
    },
    {
        "id": "hglrc-speed-2207-5-2650kv",
        "category": "motor",
        "name": "Speed 2207.5 2650KV",
        "brand": "HGLRC",
        "price_php": 812,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Speed+2207.5+2650KV",
        "color": "#151515",
        "specs": {
            "kv": 2650,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 39
        }
    },
    {
        "id": "geprc-speedx-2306-5-1800kv",
        "category": "motor",
        "name": "SPEEDX 2306.5 1800KV",
        "brand": "GEPRC",
        "price_php": 924,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+SPEEDX+2306.5+1800KV",
        "color": "#1a1a1a",
        "specs": {
            "kv": 1800,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 37
        }
    },
    # ========== ESCs ==========
    {
        "id": "diatone-mamba-f80-80a-4in1",
        "category": "esc",
        "name": "Mamba F80 80A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 3640,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/search?q=Diatone+Mamba+F80+80A+4in1",
        "color": "#151515",
        "specs": {
            "amp_rating": 80,
            "input_voltage_s": 8,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 95
        }
    },
    {
        "id": "hglrc-zeus-40a-mini-4in1",
        "category": "esc",
        "name": "Zeus 40A Mini 4-in-1 ESC",
        "brand": "HGLRC",
        "price_php": 1568,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Zeus+40A+Mini+4in1",
        "color": "#111111",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 50
        }
    },
    {
        "id": "iflight-succex-e-55a-4in1",
        "category": "esc",
        "name": "SucceX-E 55A 4-in-1 ESC",
        "brand": "iFlight",
        "price_php": 2184,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+SucceX-E+55A+4in1",
        "color": "#1c1c1c",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "speedybee-bls-55a-30x30-4in1",
        "category": "esc",
        "name": "BLS 55A 30x30 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2408,
        "weight_g": 11.5,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=SpeedyBee+BLS+55A+30x30+4in1",
        "color": "#151515",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    # ========== FLIGHT CONTROLLERS ==========
    {
        "id": "holybro-kakute-h7-mini-fc",
        "category": "fc",
        "name": "Kakute H7 Mini Flight Controller",
        "brand": "Holybro",
        "price_php": 3080,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Holybro+Kakute+H7+Mini",
        "color": "#111111",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "geprc-f722-bt-hd-fc",
        "category": "fc",
        "name": "F722-BT HD Flight Controller",
        "brand": "GEPRC",
        "price_php": 2632,
        "weight_g": 9.5,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=GEPRC+F722-BT+HD",
        "color": "#151515",
        "specs": {
            "gyro": "ICM42688",
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
        "id": "hglrc-zeus-f722-fc",
        "category": "fc",
        "name": "Zeus F722 Flight Controller",
        "brand": "HGLRC",
        "price_php": 2296,
        "weight_g": 8.2,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=HGLRC+Zeus+F722",
        "color": "#1a1a1a",
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
    # ========== PROPELLERS ==========
    {
        "id": "hqprop-6x4-5x3-v1s",
        "category": "propeller",
        "name": "6X4.5X3 V1S Propeller (4pc)",
        "brand": "HQProp",
        "price_php": 224,
        "weight_g": 6.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+6X4.5X3+V1S",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-3018-3inch-tri-blade",
        "category": "propeller",
        "name": "3018 3\" Tri-Blade Propeller (4pc)",
        "brand": "Gemfan",
        "price_php": 140,
        "weight_g": 2.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+3018",
        "color": "#111111",
        "specs": {
            "diameter_inch": 3,
            "pitch": 1.8,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["black", "gray"]
        }
    },
    # ========== FPV CAMERAS ==========
    {
        "id": "runcam-racer-nano-3-camera",
        "category": "camera",
        "name": "Racer Nano 3 FPV Camera",
        "brand": "RunCam",
        "price_php": 1120,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=RunCam+Racer+Nano+3",
        "color": "#111111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-toothless-3-camera",
        "category": "camera",
        "name": "Toothless 3 Micro FPV Camera",
        "brand": "Foxeer",
        "price_php": 1008,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Toothless+3",
        "color": "#151515",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    # ========== VIDEO TRANSMITTERS ==========
    {
        "id": "flywoo-vp906-vtx",
        "category": "vtx",
        "name": "VP906 5.8GHz VTX",
        "brand": "Flywoo",
        "price_php": 1064,
        "weight_g": 3.4,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=Flywoo+VP906+5.8GHz",
        "color": "#111111",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "iflight-jesc-vtx-1w",
        "category": "vtx",
        "name": "JESC 5.8GHz 1W VTX",
        "brand": "iFlight",
        "price_php": 1792,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=iFlight+JESC+VTX+1W",
        "color": "#1c1c1c",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    # ========== BATTERIES ==========
    {
        "id": "cnhl-black-series-1100mah-6s",
        "category": "battery",
        "name": "Black Series 1100mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1624,
        "weight_g": 198,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1100mAh+6S+100C",
        "color": "#111111",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "gnb-1300mah-3s-95c",
        "category": "battery",
        "name": "1300mAh 3S 95C LiPo",
        "brand": "GNB",
        "price_php": 728,
        "weight_g": 132,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GNB+1300mAh+3S+95C",
        "color": "#151515",
        "specs": {
            "cell_count_s": 3,
            "capacity_mah": 1300,
            "c_rating": 95,
            "connector": "XT30",
            "voltage_nominal": 11.1
        }
    },
    # ========== RC RECEIVERS ==========
    {
        "id": "radiomaster-er4-exlrs-rx",
        "category": "receiver",
        "name": "ER4 ExpressLRS Receiver",
        "brand": "RadioMaster",
        "price_php": 784,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RadioMaster+ER4+ExpressLRS",
        "color": "#111111",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-ep1-exlrs-rx",
        "category": "receiver",
        "name": "EP1 ExpressLRS Receiver",
        "brand": "HappyModel",
        "price_php": 644,
        "weight_g": 0.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP1+ExpressLRS",
        "color": "#151515",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    # ========== GPS MODULES ==========
    {
        "id": "matek-m10q-oled-gps",
        "category": "gps",
        "name": "M10Q-OLED GPS + Compass + Display",
        "brand": "Matek",
        "price_php": 2016,
        "weight_g": 10.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-OLED",
        "color": "#111111",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 12,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    # ========== VTX ANTENNAS ==========
    {
        "id": "truerc-immortal-t-sma-antenna",
        "category": "antenna",
        "name": "Immortal T 5.8GHz SMA Antenna",
        "brand": "TrueRC",
        "price_php": 812,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Immortal+T",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.8,
            "type": "cloverleaf"
        }
    },
    {
        "id": "foxeer-lollipop-3-plus-rp-sma-antenna",
        "category": "antenna",
        "name": "Lollipop 3 Plus 5.8GHz RP-SMA Antenna",
        "brand": "Foxeer",
        "price_php": 504,
        "weight_g": 4,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Foxeer+Lollipop+3+Plus+RP-SMA",
        "color": "#151515",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "RP-SMA",
            "gain_dbi": 2.2,
            "type": "cloverleaf"
        }
    },
]


def main():
    with open("data/parts.json", "r") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    added = 0
    skipped = 0

    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"  SKIP (duplicate): {part['id']}")
            skipped += 1
        else:
            data["parts"].append(part)
            existing_ids.add(part["id"])
            added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = len(data["parts"])
    print(f"\nAdded {added} new parts (skipped {skipped} duplicates)")
    print(f"Total parts now: {total}")

    from collections import Counter
    cats = Counter(p["category"] for p in data["parts"])
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
