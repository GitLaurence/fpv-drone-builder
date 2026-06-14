#!/usr/bin/env python3
"""Add 34th batch of 14 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "flywoo-explorer-lr4-v2-frame",
        "category": "frame",
        "name": "Explorer LR4 V2 Frame",
        "brand": "Flywoo",
        "price_php": 3200,
        "weight_g": 105,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Explorer+LR4+V2",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 25.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 3,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "brotherhobby-avenger-2812-1300kv",
        "category": "motor",
        "name": "Avenger 2812 1300KV",
        "brand": "BrotherHobby",
        "price_php": 1450,
        "weight_g": 38,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2812+1300KV",
        "color": "#3a3a3a",
        "specs": {
            "kv": 1300,
            "stator_size": "2812",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "axisflying-c2207-2-1900kv",
        "category": "motor",
        "name": "C2207.2 1900KV",
        "brand": "Axisflying",
        "price_php": 1550,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Axisflying+C2207.2+1900KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1900,
            "stator_size": "2207.5",
            "motor_mount_mm": 25.5,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "tmotor-f60-pro-v-60a-4in1",
        "category": "esc",
        "name": "F60 PRO V 60A 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 5200,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F60+PRO+V+60A+4-in-1",
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
        "id": "speedybee-bls-50a-32x32",
        "category": "esc",
        "name": "BLS 50A 32x32 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 1900,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+BLS+50A+32x32",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 32,
            "burst_amp": 55
        }
    },
    {
        "id": "geprc-f411-12a-aio",
        "category": "fc",
        "name": "F411 12A AIO Flight Controller",
        "brand": "GEPRC",
        "price_php": 1500,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+F411+12A+AIO",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": False,
            "uart_count": 4,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-hurricane-51466-5blade",
        "category": "propeller",
        "name": "Hurricane 51466 5\" 5-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 210,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.66,
            "blade_count": 5,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-hurricane-2015-3blade",
        "category": "propeller",
        "name": "Hurricane 2015 2\" Tri-Blade Propeller",
        "brand": "Gemfan",
        "price_php": 130,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+2015",
        "color": "#333",
        "specs": {
            "diameter_inch": 2,
            "pitch": 1.5,
            "blade_count": 3,
            "shaft_mm": 1.5,
            "color_options": ["gray", "pink"]
        }
    },
    {
        "id": "foxeer-razer-nano-2",
        "category": "camera",
        "name": "Razer Nano 2",
        "brand": "Foxeer",
        "price_php": 1450,
        "weight_g": 4.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Razer+Nano+2",
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
        "id": "rush-tank-nano-vtx",
        "category": "vtx",
        "name": "Tank Nano VTX",
        "brand": "Rush",
        "price_php": 1700,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rush+Tank+Nano+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 500,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-rline-4-1300mah-6s",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 6S",
        "brand": "Tattu",
        "price_php": 2100,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+4.0+1300mAh+6S",
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
        "id": "radiomaster-rp3-elrs-rx",
        "category": "receiver",
        "name": "RP3 ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 950,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RadioMaster+RP3+ELRS",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "beitian-bn-880q-gps",
        "category": "gps",
        "name": "BN-880Q GPS+Compass",
        "brand": "Beitian",
        "price_php": 1050,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880Q",
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
        "id": "immersionrc-skew-planar-antenna",
        "category": "antenna",
        "name": "Skew Planar Antenna",
        "brand": "ImmersionRC",
        "price_php": 1300,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+Skew+Planar",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.5,
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
