"""Add 22nd batch of new FPV parts across all 11 categories."""
import json

NEW_PARTS = [
    {
        "id": "lumenier-qav-s-3",
        "category": "frame",
        "name": "QAV-S 3\" Micro Freestyle Frame",
        "brand": "Lumenier",
        "price_php": 1450,
        "weight_g": 35,
        "in_stock": True,
        "buy_url": "https://www.lumenier.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 132,
            "motor_mount_mm": 16,
            "prop_clearance_inch": 3,
            "stack_mount_mm": 20,
            "material": "carbon fiber",
            "arm_thickness_mm": 2.5,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=lumenier+qav-s+3"
        }
    },
    {
        "id": "tmotor-velox-v2207-v3-2450kv",
        "category": "motor",
        "name": "Velox V2207 V3 2450KV",
        "brand": "T-Motor",
        "price_php": 1850,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2450,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "diatone-mamba-f40-45a-4in1",
        "category": "esc",
        "name": "Mamba F40 45A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 2350,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.diatone.us/products/mamba-f40-esc",
        "color": "#0a0a0a",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "iflight-blitz-f7-mini-v2",
        "category": "fc",
        "name": "BLITZ F7 Mini V2 Flight Controller",
        "brand": "iFlight",
        "price_php": 3100,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "gyro": "ICM20689",
            "firmware": "Betaflight",
            "form_factor_mm": 20,
            "stack_mount_mm": 20,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True,
            "diagram_url": "https://shop.iflight.com/Blitz-F7-Mini-Flight-Controller"
        }
    },
    {
        "id": "gemfan-hurricane-5125-3",
        "category": "propeller",
        "name": "Hurricane 5125-3 Propeller",
        "brand": "Gemfan",
        "price_php": 245,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.gemfanhobby.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 2.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey"
            ]
        }
    },
    {
        "id": "runcam-phoenix-3-vision-mini",
        "category": "camera",
        "name": "Phoenix 3 Vision Mini",
        "brand": "RunCam",
        "price_php": 1850,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
        "id": "iflight-ts5828x-pro",
        "category": "vtx",
        "name": "TS5828X Pro VTX",
        "brand": "iFlight",
        "price_php": 1250,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/Raceband",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-ministar-1800mah-4s",
        "category": "battery",
        "name": "MiniStar 1800mAh 4S 100C",
        "brand": "CNHL",
        "price_php": 1180,
        "weight_g": 195,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1800,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "betafpv-elrs-nano-rx",
        "category": "receiver",
        "name": "ELRS Nano Receiver",
        "brand": "BetaFPV",
        "price_php": 720,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "iflight-m10q-gps",
        "category": "gps",
        "name": "M10Q GPS Module",
        "brand": "iFlight",
        "price_php": 1550,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "rushfpv-cherry-5.8-v4",
        "category": "antenna",
        "name": "Cherry 5.8GHz V4 Antenna",
        "brand": "RushFPV",
        "price_php": 620,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.2,
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
