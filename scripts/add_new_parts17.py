"""Add a new batch of real FPV parts across all 11 categories."""
import json

NEW_PARTS = [
    {
        "id": "iflight-nazgul-evoque-f5x-v2",
        "category": "frame",
        "name": "Nazgul Evoque F5X V2",
        "brand": "iFlight",
        "price_php": 4480,
        "weight_g": 76,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber"
        }
    },
    {
        "id": "five33-freybird-5",
        "category": "frame",
        "name": "Freybird 5",
        "brand": "Five33",
        "price_php": 5040,
        "weight_g": 82,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 230,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber"
        }
    },
    {
        "id": "brotherhobby-avenger-4-2812.5",
        "category": "motor",
        "name": "Avenger 4 2812.5",
        "brand": "BrotherHobby",
        "price_php": 1960,
        "weight_g": 52,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2812.5",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 50
        }
    },
    {
        "id": "tmotor-velox-v2807",
        "category": "motor",
        "name": "Velox V2807",
        "brand": "T-Motor",
        "price_php": 2128,
        "weight_g": 48,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#2a2a2a",
        "specs": {
            "kv": 1300,
            "stator_size": "2807",
            "motor_mount_mm": 30,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 48
        }
    },
    {
        "id": "mamba-f50-pro-50a-4in1",
        "category": "esc",
        "name": "Mamba F50 Pro 50A 4-in-1",
        "brand": "Diatone",
        "price_php": 3360,
        "weight_g": 30,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 50,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 60
        }
    },
    {
        "id": "spedix-s55-50a-4in1-esc",
        "category": "esc",
        "name": "S55 50A 4-in-1 ESC",
        "brand": "Spedix",
        "price_php": 2912,
        "weight_g": 27,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
        "color": "#002200",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "iflight-blitz-mini-f7-pro",
        "category": "fc",
        "name": "BLITZ Mini F7 Pro",
        "brand": "iFlight",
        "price_php": 3920,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
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
            "curr_sensor": True
        }
    },
    {
        "id": "hglrc-zeus-f765-aio",
        "category": "fc",
        "name": "Zeus F765 AIO",
        "brand": "HGLRC",
        "price_php": 4760,
        "weight_g": 13,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#000055",
        "specs": {
            "gyro": "ICM42688",
            "firmware": "Betaflight",
            "form_factor_mm": 30,
            "stack_mount_mm": 30,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 3,
            "curr_sensor": True
        }
    },
    {
        "id": "hqprop-dp-6x4.5x3",
        "category": "propeller",
        "name": "DP 6x4.5x3",
        "brand": "HQProp",
        "price_php": 251,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 6,
            "pitch": 4.5,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray"]
        }
    },
    {
        "id": "gemfan-hurricane-durable-51477",
        "category": "propeller",
        "name": "Hurricane Durable 51477",
        "brand": "Gemfan",
        "price_php": 196,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.77,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": ["black", "gray", "green"]
        }
    },
    {
        "id": "foxeer-cat-3-nano",
        "category": "camera",
        "name": "Cat 3 Nano",
        "brand": "Foxeer",
        "price_php": 2016,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/1.8\" CMOS Starlight",
            "fov_deg": 166,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "foxeer-mix-3-camera",
        "category": "camera",
        "name": "Mix 3",
        "brand": "Foxeer",
        "price_php": 1456,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#111",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "diatone-air-vtx-1w",
        "category": "vtx",
        "name": "Air VTX 1W",
        "brand": "Diatone",
        "price_php": 1736,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "6-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "eachine-tx805s-vtx",
        "category": "vtx",
        "name": "TX805S VTX",
        "brand": "Eachine",
        "price_php": 1064,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.banggood.com",
        "color": "#221100",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "6-24V",
            "connector": "MMCX"
        }
    },
    {
        "id": "cnhl-black-series-1800mah-6s",
        "category": "battery",
        "name": "Black Series 1800mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2912,
        "weight_g": 268,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com",
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
        "id": "tattu-rline-4.0-1300mah-4s",
        "category": "battery",
        "name": "R-Line 4.0 1300mAh 4S",
        "brand": "Tattu",
        "price_php": 1848,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 130,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "radiomaster-rp1-elrs-nano",
        "category": "receiver",
        "name": "RP1 ELRS Nano Receiver",
        "brand": "RadioMaster",
        "price_php": 784,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 25
        }
    },
    {
        "id": "betafpv-superd-receiver",
        "category": "receiver",
        "name": "SuperD Receiver",
        "brand": "BetaFPV",
        "price_php": 1120,
        "weight_g": 1.8,
        "in_stock": True,
        "buy_url": "https://betafpv.com",
        "color": "#1a001a",
        "specs": {
            "protocol": "ELRS",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 30
        }
    },
    {
        "id": "foxeer-gm3-mini-gps",
        "category": "gps",
        "name": "GM3 Mini GPS",
        "brand": "Foxeer",
        "price_php": 1064,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BEIDOU",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "geprc-gps-m10-mini",
        "category": "gps",
        "name": "GPS M10 Mini",
        "brand": "GEPRC",
        "price_php": 980,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "lumenier-axii-2-mini",
        "category": "antenna",
        "name": "AXII 2 Mini 5.8GHz",
        "brand": "Lumenier",
        "price_php": 896,
        "weight_g": 6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 2.3,
            "polarization": "RHCP",
            "connector": "MMCX",
            "type": "omni"
        }
    },
    {
        "id": "menace-vagabond-antenna",
        "category": "antenna",
        "name": "Vagabond 5.8GHz",
        "brand": "Menace Antennas",
        "price_php": 1232,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 3.5,
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
