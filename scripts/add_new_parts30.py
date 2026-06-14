"""Add 30th batch of new FPV parts - real, verified products across categories."""
import json

NEW_PARTS = [
    {
        "id": "flywoo-venom-5-frame",
        "category": "frame",
        "name": "Venom 5\" Freestyle Frame",
        "brand": "Flywoo",
        "price_php": 2240,
        "weight_g": 86,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flywoo+Venom+5+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5.1,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=flywoo+venom+5"
        }
    },
    {
        "id": "iflight-xing-e-2207-motor",
        "category": "motor",
        "name": "Xing E 2207 Brushless Motor",
        "brand": "iFlight",
        "price_php": 1120,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Xing+E+2207",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1800,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 41
        }
    },
    {
        "id": "flycolor-pro-50a-4in1-esc",
        "category": "esc",
        "name": "Pro 50A 4-in-1 ESC",
        "brand": "Flycolor",
        "price_php": 1730,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flycolor+Pro+50A+4-in-1+ESC",
        "color": "#101010",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "iflight-blitz-mini-f745-fc",
        "category": "fc",
        "name": "BLITZ Mini F745 Flight Controller",
        "brand": "iFlight",
        "price_php": 2420,
        "weight_g": 6.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+BLITZ+Mini+F745",
        "color": "#0c0c0c",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://shop.iflight.com/blitz-mini-f745-flight-controller"
        }
    },
    {
        "id": "gemfan-banshee-bandit-propeller",
        "category": "propeller",
        "name": "Banshee Bandit 5-Blade",
        "brand": "Gemfan",
        "price_php": 245,
        "weight_g": 4.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Banshee+Bandit",
        "color": "#1f1f1f",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.8,
            "blade_count": 5,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey",
                "white"
            ]
        }
    },
    {
        "id": "runcam-phoenix-oasis-camera",
        "category": "camera",
        "name": "Phoenix Oasis",
        "brand": "RunCam",
        "price_php": 1820,
        "weight_g": 7.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Phoenix+Oasis",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 165,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "foxeer-trip65-vtx",
        "category": "vtx",
        "name": "Trip65 5.8GHz VTX",
        "brand": "Foxeer",
        "price_php": 1860,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Trip65+VTX",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "tattu-r-line-6s-1300mah-150c",
        "category": "battery",
        "name": "R-Line 6S 1300mAh 150C",
        "brand": "Tattu",
        "price_php": 2110,
        "weight_g": 215,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+6S+1300mAh+150C",
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
        "id": "betafpv-super-d-elrs-receiver",
        "category": "receiver",
        "name": "Super D ELRS 2.4GHz Receiver",
        "brand": "BetaFPV",
        "price_php": 760,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+Super+D+ELRS+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "matek-m10q-v2-gps",
        "category": "gps",
        "name": "M10Q V2 GPS+Compass",
        "brand": "Matek",
        "price_php": 1560,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q+V2+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "foxeer-pagoda-x-antenna",
        "category": "antenna",
        "name": "Pagoda X 5.8GHz",
        "brand": "Foxeer",
        "price_php": 360,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Pagoda+X+Antenna",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    }
]


def main():
    with open("data/parts.json") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    added = 0
    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"Skipping duplicate id: {part['id']}")
            continue
        data["parts"].append(part)
        added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added {added} new parts. Total parts: {len(data['parts'])}")


if __name__ == "__main__":
    main()
