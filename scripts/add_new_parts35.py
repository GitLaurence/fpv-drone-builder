"""Add 35th batch of 11 new FPV parts across all 11 categories."""
import json

NEW_PARTS = [
    {
        "id": "iflight-nazgul5-v3-frame",
        "category": "frame",
        "name": "Nazgul5 V3 Frame",
        "brand": "iFlight",
        "price_php": 2100,
        "weight_g": 120,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Nazgul5+V3+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=iflight+nazgul5"
        }
    },
    {
        "id": "tmotor-f60-pro-v-1750kv",
        "category": "motor",
        "name": "F60 Pro V 1750KV",
        "brand": "T-Motor",
        "price_php": 1700,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F60+Pro+V+1750KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1750,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "holybro-tekko32-f4-65a-4in1",
        "category": "esc",
        "name": "Tekko32 F4 65A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 2500,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Holybro+Tekko32+F4+65A+4-in-1",
        "color": "#1a1a1a",
        "specs": {
            "amp_rating": 65,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 70
        }
    },
    {
        "id": "iflight-succex-e-f4-v2-1-fc",
        "category": "fc",
        "name": "SucceX-E F4 V2.1 Flight Controller",
        "brand": "iFlight",
        "price_php": 1400,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+SucceX-E+F4+V2.1+Flight+Controller",
        "color": "#000033",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-5x4-3x3-durable",
        "category": "propeller",
        "name": "5X4.3X3 Durable Propeller",
        "brand": "HQProp",
        "price_php": 180,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+5X4.3X3+Durable",
        "color": "#333",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "gray",
                "white",
                "black"
            ]
        }
    },
    {
        "id": "walksnail-avatar-hd-v2-nano-camera",
        "category": "camera",
        "name": "Avatar HD V2 Nano Camera",
        "brand": "Walksnail",
        "price_php": 2600,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Walksnail+Avatar+HD+V2+Nano+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital",
            "tvl": 1200,
            "voltage_range": "6-28V"
        }
    },
    {
        "id": "tbs-unify-pro32-hv-vtx",
        "category": "vtx",
        "name": "Unify Pro32 HV VTX",
        "brand": "TBS",
        "price_php": 2500,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Unify+Pro32+HV",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "SmartAudio",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-1500mah-4s",
        "category": "battery",
        "name": "Black Series 1500mAh 4S",
        "brand": "CNHL",
        "price_php": 1000,
        "weight_g": 175,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1500mAh+4S",
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
        "id": "happymodel-elrs-ep2-rx",
        "category": "receiver",
        "name": "ELRS EP2 Receiver",
        "brand": "Happymodel",
        "price_php": 700,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Happymodel+ELRS+EP2+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "beitian-bn-180-gps",
        "category": "gps",
        "name": "BN-180 GPS Module",
        "brand": "Beitian",
        "price_php": 850,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-180+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 28,
            "compass": False,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "tbs-triumph-ezwide-antenna",
        "category": "antenna",
        "name": "Triumph EZ-Wide Band Antenna",
        "brand": "TBS",
        "price_php": 1100,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Triumph+EZ-Wide+Band+Antenna",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.8,
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
