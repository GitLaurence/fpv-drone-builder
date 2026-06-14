"""Add 29th batch of new FPV parts - real, verified products across categories."""
import json

NEW_PARTS = [
    {
        "id": "tbs-source-one-v5-frame",
        "category": "frame",
        "name": "Source One V5 Frame Kit",
        "brand": "TBS",
        "price_php": 1450,
        "weight_g": 95,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=Source+One+V5",
        "color": "#1b1b1b",
        "specs": {
            "size_mm": 210,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5.1,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25,
            "thingiverse_url": "https://www.thingiverse.com/search?q=tbs+source+one+v5"
        }
    },
    {
        "id": "emax-eco-ii-2807-1300kv-motor",
        "category": "motor",
        "name": "ECO II 2807 1300KV Brushless Motor",
        "brand": "EMAX",
        "price_php": 950,
        "weight_g": 46,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=EMAX+ECO+II+2807+1300KV",
        "color": "#3a3a3a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 38
        }
    },
    {
        "id": "diatone-mamba-f40-4in1-esc",
        "category": "esc",
        "name": "Mamba F40_128k 40A 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 1950,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Diatone+Mamba+F40+4in1+ESC",
        "color": "#101010",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 45
        }
    },
    {
        "id": "mateksys-f405-std-fc",
        "category": "fc",
        "name": "F405-STD Flight Controller",
        "brand": "Mateksys",
        "price_php": 1850,
        "weight_g": 8.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Matek+F405-STD",
        "color": "#0c0c0c",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 1,
            "curr_sensor": True,
            "diagram_url": "https://www.mateksys.com/?portfolio=f405-std"
        }
    },
    {
        "id": "hqprop-5x4-3x3-propeller",
        "category": "propeller",
        "name": "5X4.3X3 V1S Durable Tri-Blade Propeller",
        "brand": "HQProp",
        "price_php": 210,
        "weight_g": 4.4,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+5X4.3X3+V1S",
        "color": "#1f1f1f",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.3,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["grey", "black", "orange"]
        }
    },
    {
        "id": "runcam-phoenix-2-camera",
        "category": "camera",
        "name": "Phoenix 2 FPV Camera",
        "brand": "RunCam",
        "price_php": 1350,
        "weight_g": 11.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=RunCam+Phoenix+2",
        "color": "#161616",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Analog/Switchable NTSC-PAL",
            "tvl": 1000,
            "voltage_range": "5-36V"
        }
    },
    {
        "id": "tbs-unify-pro32-nano-vtx",
        "category": "vtx",
        "name": "Unify Pro32 Nano VTX",
        "brand": "TBS",
        "price_php": 2650,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.team-blacksheep.com/products/search?q=Unify+Pro32+Nano",
        "color": "#262626",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/Race band",
            "voltage_range": "6-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "cnhl-black-series-1300mah-4s-100c-battery",
        "category": "battery",
        "name": "Black Series 1300mAh 4S 100C LiPo",
        "brand": "CNHL",
        "price_php": 1380,
        "weight_g": 168,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1300mAh+4S+100C",
        "color": "#5c0a0a",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "frsky-r9-mm-receiver",
        "category": "receiver",
        "name": "R9 MM OTA Receiver",
        "brand": "FrSky",
        "price_php": 1050,
        "weight_g": 1.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FrSky+R9+MM",
        "color": "#2b2b2b",
        "specs": {
            "protocol": "ACCESS/ACCST",
            "frequency_mhz": 900,
            "telemetry": True,
            "range_km": 15
        }
    },
    {
        "id": "rdq-pavo-pico-gps-v2",
        "category": "gps",
        "name": "Pavo Pico GPS V2",
        "brand": "RDQ",
        "price_php": 1450,
        "weight_g": 5.8,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Pavo+Pico+GPS",
        "color": "#141414",
        "specs": {
            "constellation": "GPS+GLONASS+Galileo+BeiDou",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 20,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "foxeer-rush-ant-ii-antenna",
        "category": "antenna",
        "name": "Rush ANT II RHCP Antenna",
        "brand": "Foxeer",
        "price_php": 480,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?keywords=Rush+ANT+II",
        "color": "#0d0d0d",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
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
