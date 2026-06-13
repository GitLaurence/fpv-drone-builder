#!/usr/bin/env python3
"""Add a twentieth batch of 11 new FPV parts (1 per category) to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "armattan-marmotte-5-5-frame",
        "category": "frame",
        "name": "Marmotte 5.5\" Frame - Classic Carbon Fiber",
        "brand": "Armattan",
        "price_php": 5320,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/armattan-marmotte-5-5-frame.html",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 234,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5.5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+marmotte"
        }
    },
    {
        "id": "brotherhobby-avenger-se-2004-1700kv",
        "category": "motor",
        "name": "Avenger SE 2004 Motor 1700KV",
        "brand": "BrotherHobby",
        "price_php": 895,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/brotherhobby-avenger-se-2004-motor-1700kv.html",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2004",
            "motor_mount_mm": 12,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 1.5,
            "peak_current_a": 14
        }
    },
    {
        "id": "spedix-gs25-25a-4in1",
        "category": "esc",
        "name": "GS25 25A 4-in-1 ESC",
        "brand": "Spedix",
        "price_php": 1959,
        "weight_g": 11.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/spedix-gs25-25a-4-in-1-2-4s-blheli-32-dshot-esc.html",
        "color": "#002200",
        "specs": {
            "amp_rating": 25,
            "input_voltage_s": 4,
            "protocol": "BLHeli_32",
            "form_factor_mm": 20,
            "burst_amp": 30
        }
    },
    {
        "id": "jhemcu-ghf13aio-f4-13a",
        "category": "fc",
        "name": "GHF13AIO F4 13A 4-in-1 AIO",
        "brand": "JHEMCU",
        "price_php": 1847,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/jhemcu-ghf13aio-f4-13a-2-4s-bl-s-4-in-1-brushless-flight-controller.html",
        "color": "#000055",
        "specs": {
            "gyro": "BMI270",
            "firmware": "Betaflight",
            "form_factor_mm": 16,
            "stack_mount_mm": 16,
            "barometer": False,
            "blackbox": False,
            "uart_count": 2,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-dps-5x4x3-white",
        "category": "propeller",
        "name": "DPS 5x4x3 White",
        "brand": "HQProp",
        "price_php": 195,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/hqprop-dps-5x4x3-propeller-3-blade-set-of-4-white.html",
        "color": "#eeeeee",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["white"]
        }
    },
    {
        "id": "foxeer-cleartx-2-vtx",
        "category": "vtx",
        "name": "ClearTX 2 5.8GHz VTX",
        "brand": "Foxeer",
        "price_php": 1455,
        "weight_g": 6.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/foxeer-cleartx-2-5-8g-25-200-500-800mw-video-transmitter-w-remote-control.html",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race",
            "voltage_range": "7-25V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-1300mah-6s-100c",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1399,
        "weight_g": 230,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/cnhl-black-series-100c-6s-lipo-battery-1300mah.html",
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
        "id": "radiomaster-xr2-nano-elrs",
        "category": "receiver",
        "name": "XR2 Nano ELRS 2.4GHz Receiver",
        "brand": "RadioMaster",
        "price_php": 727,
        "weight_g": 0.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/radiomaster-xr2-nano-elrs-2-4ghz-receiver.html",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "holybro-micro-m10-gps-w-case",
        "category": "gps",
        "name": "Micro M10 GPS w/ Case",
        "brand": "Holybro",
        "price_php": 1567,
        "weight_g": 16,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/holybro-micro-m10-gps-w-case.html",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 30,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "truerc-vulcan-mk-ii-5-8",
        "category": "antenna",
        "name": "Vulcan MK II 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 3079,
        "weight_g": 50,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/truerc-vulcan-mk-ii-5-8ghz-antenna-rhcp.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 18,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
        }
    },
    {
        "id": "foxeer-cat-super-starlight",
        "category": "camera",
        "name": "Cat Super Starlight Low Light FPV Camera",
        "brand": "Foxeer",
        "price_php": 2514,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/foxeer-cat-super-starlight-low-light-fpv-camera.html",
        "color": "#111111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 145,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
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
