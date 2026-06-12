#!/usr/bin/env python3
"""Add a sixteenth batch of 22 new FPV parts (2 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-explorer-lr4-frame-kit-v2",
        "category": "frame",
        "name": "Explorer LR4 Frame Kit V2",
        "brand": "Flywoo",
        "price_php": 2320,
        "weight_g": 35,
        "in_stock": True,
        "buy_url": "https://flywoo.net/products/explorer-lr-4-frame-kit-v2-hd-analog-version",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 159,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 16,
            "material": "carbon fiber + 7075 aluminum",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "geprc-tern-lr40-frame",
        "category": "frame",
        "name": "GEP-Tern-LR40 Frame",
        "brand": "GEPRC",
        "price_php": 2030,
        "weight_g": 59,
        "in_stock": True,
        "buy_url": "https://geprc.com/product/gep-tern-lr40-frame/",
        "color": "#0d0d0d",
        "specs": {
            "size_mm": 180,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 20,
            "material": "7075 aluminum + carbon fiber",
            "arm_thickness_mm": 3.5,
            "standoff_height_mm": 20,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+tern+lr40"
        }
    },
    {
        "id": "t-motor-f60-pro-v-1950kv",
        "category": "motor",
        "name": "F60 PRO V 2207.5 1950KV",
        "brand": "T-Motor",
        "price_php": 1914,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/product/f60prov-fpv-motor.html",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1950,
            "stator_size": "2207.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 4,
            "peak_current_a": 49
        }
    },
    {
        "id": "brotherhobby-avenger-2407-1700kv",
        "category": "motor",
        "name": "Avenger 2407 1700KV",
        "brand": "BrotherHobby",
        "price_php": 1508,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2407",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 47
        }
    },
    {
        "id": "t-motor-f55a-pro-3-4in1",
        "category": "esc",
        "name": "F55A PRO III 55A 4-in-1",
        "brand": "T-Motor",
        "price_php": 3770,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 8,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "diatone-mamba-f40-pro-4in1",
        "category": "esc",
        "name": "Mamba F40_Pro 40A 4-in-1",
        "brand": "Diatone",
        "price_php": 1856,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.diatone.us",
        "color": "#002200",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 50
        }
    },
    {
        "id": "diatone-mamba-mk4-f405-mini",
        "category": "fc",
        "name": "Mamba MK4 F405 Mini",
        "brand": "Diatone",
        "price_php": 1740,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/products/mb-mk4-f405-mini-fc",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.diatone.us/products/mb-mk4-f405-mini-fc"
        }
    },
    {
        "id": "speedybee-f405-wing-mini",
        "category": "fc",
        "name": "F405 WING Mini",
        "brand": "SpeedyBee",
        "price_php": 2030,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "INAV/ArduPilot/Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com"
        }
    },
    {
        "id": "hqprop-5-1x3-1x3",
        "category": "propeller",
        "name": "5.1X3.1X3",
        "brand": "HQProp",
        "price_php": 174,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.hqprop.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.1,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "green"]
        }
    },
    {
        "id": "gemfan-hurricane-5125-3",
        "category": "propeller",
        "name": "Hurricane 5125-3",
        "brand": "Gemfan",
        "price_php": 203,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["gray", "black", "white"]
        }
    },
    {
        "id": "runcam-racer-3-nano",
        "category": "camera",
        "name": "Racer 3 Nano",
        "brand": "RunCam",
        "price_php": 1276,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://shop.runcam.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-nightwolf-v3",
        "category": "camera",
        "name": "Nightwolf V3",
        "brand": "Foxeer",
        "price_php": 1624,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" STARVIS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-reaper-extreme-v3",
        "category": "vtx",
        "name": "Reaper Extreme V3 2.5W VTX",
        "brand": "Foxeer",
        "price_php": 3480,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://pyrodrone.com/products/foxeer-reaper-extreme-2-5w-5-8ghz-37ch-adjustable-analog-vtx",
        "color": "#221100",
        "specs": {
            "power_mw_max": 2500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-36V",
            "connector": "MMCX"
        }
    },
    {
        "id": "hglrc-sky-v3-vtx",
        "category": "vtx",
        "name": "Sky V3 VTX",
        "brand": "HGLRC",
        "price_php": 1276,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-24V",
            "connector": "MMCX"
        }
    },
    {
        "id": "geprc-m10-gps",
        "category": "gps",
        "name": "GEP-M10 GPS Module",
        "brand": "GEPRC",
        "price_php": 1160,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://geprc.com/product/gep-m10-series-gps-module/",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+BDS+Galileo+QZSS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "matek-m10-l4-3100",
        "category": "gps",
        "name": "AP Periph GNSS M10-L4-3100",
        "brand": "Matek",
        "price_php": 1276,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.mateksys.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "truerc-x-air-mk2",
        "category": "antenna",
        "name": "X-AIR MK II 5.8GHz",
        "brand": "TrueRC",
        "price_php": 870,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://truerc.com",
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
        "id": "immersionrc-skew-planar-v3",
        "category": "antenna",
        "name": "Skew Planar V3 5.8GHz",
        "brand": "ImmersionRC",
        "price_php": 696,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.immersionrc.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
        }
    },
    {
        "id": "cnhl-black-series-1500-6s",
        "category": "battery",
        "name": "Black Series 1500mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1740,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.cnhlbattery.com",
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
        "id": "tattu-r-line-v5-1100-6s",
        "category": "battery",
        "name": "R-Line V5 1100mAh 6S",
        "brand": "Tattu",
        "price_php": 1856,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.gensace.de",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1100,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "radiomaster-bandit-br1",
        "category": "receiver",
        "name": "Bandit BR1 ELRS 915MHz Receiver",
        "brand": "RadioMaster",
        "price_php": 2376,
        "weight_g": 2,
        "in_stock": True,
        "buy_url": "https://radiomasterrc.com/products/bandit-br1-expresslrs-receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 915,
            "telemetry": True,
            "range_km": 50
        }
    },
    {
        "id": "happymodel-ep2-rx",
        "category": "receiver",
        "name": "EP2 ELRS 2.4GHz Receiver",
        "brand": "HappyModel",
        "price_php": 985,
        "weight_g": 0.44,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/happymodel-expresslrs-nano-2-4ghz-ep2-rx.html",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 15
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
