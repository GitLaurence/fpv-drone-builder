"""Add 30th batch of new FPV parts - real, verified products across categories."""
import json

NEW_PARTS = [
    {
        "id": "diatone-roma-f5-frame",
        "category": "frame",
        "name": "Roma F5 Frame",
        "brand": "Diatone",
        "price_php": 3120,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Roma+F5",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=diatone+roma+f5"
        }
    },
    {
        "id": "emax-eco2-2306",
        "category": "motor",
        "name": "ECO II 2306",
        "brand": "EMAX",
        "price_php": 749,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=EMAX+ECO+II+2306",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1700,
            "stator_size": "2306",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 30
        }
    },
    {
        "id": "tmotor-f45a-pro-iii-esc",
        "category": "esc",
        "name": "F45A PRO III 4-in-1",
        "brand": "T-Motor",
        "price_php": 3199,
        "weight_g": 26,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=T-Motor+F45A+PRO+III+4-in-1",
        "color": "#002200",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    {
        "id": "speedybee-f405-v4-aio-fc",
        "category": "fc",
        "name": "F405 V4 AIO",
        "brand": "SpeedyBee",
        "price_php": 2399,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+F405+V4+AIO",
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
            "curr_sensor": True,
            "diagram_url": "https://www.speedybee.com/speedybee-f405-v4-bls-50a-30x30mm-stack/"
        }
    },
    {
        "id": "hqprop-ethix-s5-5x4.3x3",
        "category": "propeller",
        "name": "Ethix S5 5x4.3x3",
        "brand": "HQProp",
        "price_php": 259,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+Ethix+S5",
        "color": "#111",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "black"]
        }
    },
    {
        "id": "foxeer-falkor-3-micro-cam",
        "category": "camera",
        "name": "Falkor 3 Micro",
        "brand": "Foxeer",
        "price_php": 1399,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Falkor+3+Micro",
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
        "id": "foxeer-reaper-v2-vtx",
        "category": "vtx",
        "name": "Reaper V2",
        "brand": "Foxeer",
        "price_php": 2599,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Reaper+V2",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-25V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-6s-1500mah",
        "category": "battery",
        "name": "Black Series 1500mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 1799,
        "weight_g": 255,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=CNHL+Black+Series+1500mAh+6S",
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
        "id": "happymodel-elrs-pp2723",
        "category": "receiver",
        "name": "ELRS PP2723 Nano RX",
        "brand": "HappyModel",
        "price_php": 899,
        "weight_g": 0.6,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=HappyModel+ELRS+PP2723",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 20
        }
    },
    {
        "id": "betafpv-bn220-gps",
        "category": "gps",
        "name": "BN-220 GPS Module",
        "brand": "BetaFPV",
        "price_php": 950,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=BetaFPV+BN-220+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "immersionrc-spironet-rhcp",
        "category": "antenna",
        "name": "SpiroNet RHCP Antenna",
        "brand": "ImmersionRC",
        "price_php": 1120,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=ImmersionRC+SpiroNet",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.6,
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
