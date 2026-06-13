"""Add 27th batch of new FPV parts - real, verified products across categories."""
import json

NEW_PARTS = [
    {
        "id": "armattan-rooster-5",
        "category": "frame",
        "name": "Rooster 5\" Frame",
        "brand": "Armattan",
        "price_php": 6200,
        "weight_g": 96,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Armattan+Rooster+5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5.1,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 5,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=armattan+rooster+5"
        }
    },
    {
        "id": "flywoo-explorer-lr4-frame",
        "category": "frame",
        "name": "Explorer LR4 Frame Kit",
        "brand": "Flywoo",
        "price_php": 2400,
        "weight_g": 58,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Explorer+LR4+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 175,
            "motor_mount_mm": 25,
            "prop_clearance_inch": 4,
            "stack_mount_mm": 25,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+explorer+lr4"
        }
    },
    {
        "id": "brotherhobby-avenger-2306-5-1750kv",
        "category": "motor",
        "name": "Avenger 2306.5 1750KV",
        "brand": "BrotherHobby",
        "price_php": 980,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2306.5+1750KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2306.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "iflight-xing2-2207-1800kv",
        "category": "motor",
        "name": "XING2 2207 1800KV",
        "brand": "iFlight",
        "price_php": 850,
        "weight_g": 31.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+XING2+2207+1800KV",
        "color": "#b8860b",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 33
        }
    },
    {
        "id": "holybro-tekko32-f4-65a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 65A 4-in-1",
        "brand": "Holybro",
        "price_php": 3200,
        "weight_g": 28,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Tekko32+F4+65A+4-in-1",
        "color": "#002200",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 80
        }
    },
    {
        "id": "diatone-mamba-f45-128k-4in1",
        "category": "esc",
        "name": "Mamba F45_128K 45A 4-in-1",
        "brand": "Diatone",
        "price_php": 1850,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F45_128K+45A+4-in-1",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 20,
            "burst_amp": 55
        }
    },
    {
        "id": "speedybee-f405-v4",
        "category": "fc",
        "name": "F405 V4",
        "brand": "SpeedyBee",
        "price_php": 2350,
        "weight_g": 9.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+F405+V4",
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
            "curr_sensor": True
        }
    },
    {
        "id": "diatone-mamba-f722-mini-mk4",
        "category": "fc",
        "name": "Mamba F722 Mini MK4",
        "brand": "Diatone",
        "price_php": 2700,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F722+Mini+MK4",
        "color": "#000055",
        "specs": {
            "gyro": "ICM20689",
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
        "id": "gemfan-hurricane-51466",
        "category": "propeller",
        "name": "Hurricane 5146-6",
        "brand": "Gemfan",
        "price_php": 240,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+5146-6",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "white",
                "grey",
                "green"
            ]
        }
    },
    {
        "id": "hqprop-7x4x3",
        "category": "propeller",
        "name": "DP 7×4×3",
        "brand": "HQProp",
        "price_php": 320,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+DP+7%C3%974%C3%973",
        "color": "#111",
        "specs": {
            "diameter_inch": 7,
            "pitch": 4,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey"
            ]
        }
    },
    {
        "id": "caddx-ratel-2",
        "category": "camera",
        "name": "Ratel 2",
        "brand": "Caddx",
        "price_php": 1850,
        "weight_g": 7.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ratel+2",
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
        "id": "walksnail-avatar-nano-kit",
        "category": "camera",
        "name": "Avatar HD Nano Kit",
        "brand": "Walksnail",
        "price_php": 9200,
        "weight_g": 19,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+HD+Nano+Kit",
        "color": "#1a1a1a",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Digital",
            "video_system": "Walksnail",
            "resolution": "1080p60",
            "voltage_range": "6-25.2V"
        }
    },
    {
        "id": "rush-tank-solo",
        "category": "vtx",
        "name": "Tank Solo",
        "brand": "Rush",
        "price_php": 1450,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Rush+Tank+Solo",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-24V",
            "connector": "SMA"
        }
    },
    {
        "id": "hdzero-whoop-lite-vtx",
        "category": "vtx",
        "name": "Whoop Lite VTX",
        "brand": "HDZero",
        "price_php": 3200,
        "weight_g": 4.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Whoop+Lite+VTX",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 25,
            "protocol": "Digital",
            "video_system": "HDZero",
            "voltage_range": "3.5-9V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-black-series-6s-1300mah-100c",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2150,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=CNHL+Black+Series+1300mAh+6S+100C",
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
        "id": "tattu-rline-4-4s-1550mah-130c",
        "category": "battery",
        "name": "R-Line 4.0 1550mAh 4S 130C",
        "brand": "Tattu",
        "price_php": 1900,
        "weight_g": 188,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+4.0+1550mAh+4S+130C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1550,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "tbs-crossfire-nano-rx",
        "category": "receiver",
        "name": "Crossfire Nano RX",
        "brand": "TBS",
        "price_php": 2650,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+RX",
        "color": "#1a001a",
        "specs": {
            "protocol": "Crossfire",
            "frequency_mhz": 868,
            "telemetry": True,
            "range_km": 40
        }
    },
    {
        "id": "radiomaster-er4-elrs-rx",
        "category": "receiver",
        "name": "ER4 ELRS 2.4GHz Receiver",
        "brand": "RadioMaster",
        "price_php": 720,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RadioMaster+ER4+ELRS+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "holybro-m9n-gps",
        "category": "gps",
        "name": "M9N GPS Module",
        "brand": "Holybro",
        "price_php": 2300,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+M9N+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M9",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "betafpv-m10-gps",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "BetaFPV",
        "price_php": 1050,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+M10+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "foxeer-lollipop-4-antenna",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz Antenna",
        "brand": "Foxeer",
        "price_php": 380,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Lollipop+4+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.5,
            "polarization": "RHCP",
            "connector": "U.FL",
            "type": "omni"
        }
    },
    {
        "id": "immersionrc-spironet-1-2ghz",
        "category": "antenna",
        "name": "SpiroNET 1.2GHz Antenna",
        "brand": "ImmersionRC",
        "price_php": 1100,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SpiroNet+1.2GHz+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 1200,
            "gain_dbi": 3,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "omni"
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
