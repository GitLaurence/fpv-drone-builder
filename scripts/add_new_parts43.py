#!/usr/bin/env python3
"""Add 43rd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "diatone-roma-f5-v2-frame",
        "category": "frame",
        "name": "Roma F5 V2 Freestyle Frame",
        "brand": "Diatone",
        "price_php": 3300,
        "weight_g": 85,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Roma+F5+V2",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 30.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=diatone+roma+f5"
        }
    },
    {
        "id": "brotherhobby-avenger-2807.5",
        "category": "motor",
        "name": "Avenger 2807.5",
        "brand": "BrotherHobby",
        "price_php": 1700,
        "weight_g": 56,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BrotherHobby+Avenger+2807.5",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807.5",
            "motor_mount_mm": 30.5,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 45
        }
    },
    {
        "id": "tmotor-f55a-pro-ii-esc",
        "category": "esc",
        "name": "F55A Pro II 4-in-1 ESC",
        "brand": "T-Motor",
        "price_php": 3900,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F55A+Pro+II+4-in-1+ESC",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "iflight-succex-e-f4-fc",
        "category": "fc",
        "name": "SucceX-E F4 Flight Controller",
        "brand": "iFlight",
        "price_php": 1400,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+SucceX-E+F4+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True,
            "diagram_url": "https://shop.iflight-rc.com/index.php?route=product/product&product_id=1199"
        }
    },
    {
        "id": "hqprop-ethix-s5-propeller",
        "category": "propeller",
        "name": "Ethix S5 Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 170,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S5",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 3.1,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "white",
                "orange"
            ]
        }
    },
    {
        "id": "caddx-ratel-2-pro-camera",
        "category": "camera",
        "name": "Ratel 2 Pro FPV Camera",
        "brand": "Caddx",
        "price_php": 1700,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Caddx+Ratel+2+Pro+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 150,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "tbs-unify-pro32-hv-vtx",
        "category": "vtx",
        "name": "Unify Pro32 HV VTX",
        "brand": "TBS",
        "price_php": 2500,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=TBS+Unify+Pro32+HV",
        "color": "#222222",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog/SmartAudio",
            "bands": "5.8GHz 48CH",
            "voltage_range": "7-36V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-black-series-1800mah-6s",
        "category": "battery",
        "name": "Black Series 1800mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1950,
        "weight_g": 245,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=CNHL+Black+Series+1800mAh+6S+100C",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1800,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "happymodel-elrs-pp-m3-nano-rx",
        "category": "receiver",
        "name": "ELRS PP M3 Nano Receiver",
        "brand": "HappyModel",
        "price_php": 840,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=HappyModel+ELRS+PP+M3+Nano+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "matek-m10q-l1l5-gps",
        "category": "gps",
        "name": "M10Q-L1L5 GPS Module",
        "brand": "Matek",
        "price_php": 1560,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+M10Q-L1L5+GPS+Module",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou+QZSS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "truerc-xair-58ghz-antenna",
        "category": "antenna",
        "name": "X-AIR 5.8GHz Antenna",
        "brand": "TrueRC",
        "price_php": 720,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+X-AIR+5.8GHz+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omnidirectional"
        }
    }
]


def main():
    path = "data/parts.json"
    with open(path) as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            raise ValueError(f"Duplicate id: {part['id']}")

    data["parts"].extend(NEW_PARTS)

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added {len(NEW_PARTS)} parts. Total parts: {len(data['parts'])}")


if __name__ == "__main__":
    main()
