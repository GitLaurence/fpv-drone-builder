#!/usr/bin/env python3
"""Add 32nd batch of 11 new FPV parts across all 11 categories to parts.json"""
import json

NEW_PARTS = [
    {
        "id": "geprc-gep-mark2-5-frame",
        "category": "frame",
        "name": "Mark2 5\" Freestyle Frame",
        "brand": "GEPRC",
        "price_php": 2200,
        "weight_g": 117,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+Mark2+5+Frame",
        "color": "#1a1a1a",
        "specs": {
            "size_mm": 215,
            "motor_mount_mm": 30,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30,
            "material": "carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 30,
            "thingiverse_url": "https://www.thingiverse.com/search?q=geprc+mark2+5"
        }
    },
    {
        "id": "iflight-tachyon-2207-2650kv",
        "category": "motor",
        "name": "Tachyon 2207 2650KV",
        "brand": "iFlight",
        "price_php": 950,
        "weight_g": 34,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=iFlight+Tachyon+2207+2650KV",
        "color": "#2a2a2a",
        "specs": {
            "kv": 2650,
            "stator_size": "2207",
            "motor_mount_mm": 30,
            "min_voltage_s": 3,
            "max_voltage_s": 5,
            "shaft_mm": 4,
            "peak_current_a": 40
        }
    },
    {
        "id": "diatone-mamba-f40-bls-40a-4in1",
        "category": "esc",
        "name": "Mamba F40_BLS 40A 6S 4-in-1 ESC",
        "brand": "Diatone",
        "price_php": 2128,
        "weight_g": 25,
        "in_stock": True,
        "buy_url": "https://www.racedayquads.com/search?q=Diatone+Mamba+F40_BLS+40A+4-in-1",
        "color": "#002200",
        "specs": {
            "amp_rating": 40,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 50
        }
    },
    {
        "id": "geprc-gep-f722-45a-aio-v2",
        "category": "fc",
        "name": "GEP-F722-45A AIO V2 Flight Controller",
        "brand": "GEPRC",
        "price_php": 4423,
        "weight_g": 8.8,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=GEPRC+GEP-F722-45A+AIO+V2",
        "color": "#000033",
        "specs": {
            "gyro": "ICM42688-P",
            "firmware": "Betaflight",
            "form_factor_mm": 32,
            "stack_mount_mm": 25.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 5,
            "5v_pad_count": 1,
            "curr_sensor": True
        }
    },
    {
        "id": "gemfan-master-3d-5146",
        "category": "propeller",
        "name": "Master 3D 5146",
        "brand": "Gemfan",
        "price_php": 250,
        "weight_g": 4.85,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Master+3D+5146",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 4.6,
            "blade_count": 3,
            "shaft_mm": 5
        }
    },
    {
        "id": "foxeer-predator-nano-v4",
        "category": "camera",
        "name": "Predator Nano V4 1000TVL",
        "brand": "Foxeer",
        "price_php": 750,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Foxeer+Predator+Nano+V4+1000TVL",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-22V"
        }
    },
    {
        "id": "hglrc-gtx585-vtx",
        "category": "vtx",
        "name": "GTX585 5.8GHz VTX",
        "brand": "HGLRC",
        "price_php": 1679,
        "weight_g": 10,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/hglrc-gtx585-5-8ghz-25-100-200-400-600mw-bf-control-vtx-mmcx.html",
        "color": "#1a1a1a",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "thunderpower-adrenaline-1300mah-4s-100c",
        "category": "battery",
        "name": "Adrenaline 1300mAh 4S 100C LiPo",
        "brand": "Thunder Power",
        "price_php": 1850,
        "weight_g": 165,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/thunder-power-adrenaline-1300mah-4s-100c-lipo-battery.html",
        "color": "#1a0000",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    {
        "id": "flysky-fgr4s-receiver",
        "category": "receiver",
        "name": "FGr4S AFHDS 3 Receiver",
        "brand": "Flysky",
        "price_php": 1900,
        "weight_g": 5.1,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Flysky+FGr4S+Receiver",
        "color": "#1a001a",
        "specs": {
            "protocol": "AFHDS 3",
            "frequency_mhz": 2400,
            "telemetry": True,
            "range_km": 0.2
        }
    },
    {
        "id": "speedybee-bz-181-gps",
        "category": "gps",
        "name": "BZGNSS BZ-181 GPS Module",
        "brand": "SpeedyBee",
        "price_php": 1119,
        "weight_g": 6.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=SpeedyBee+BZGNSS+BZ-181+GPS",
        "color": "#1a1a1a",
        "specs": {
            "constellation": "GPS+GLONASS+BDS+GALILEO",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 25,
            "compass": False,
            "connector": "SH1.0 4-pin"
        }
    },
    {
        "id": "truerc-sniper-ii-5-8",
        "category": "antenna",
        "name": "Sniper II 5.8GHz RHCP",
        "brand": "TrueRC",
        "price_php": 3300,
        "weight_g": 15,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/truerc-sniper-ii-5-8ghz-antenna-rhcp.html",
        "color": "#1a1a1a",
        "specs": {
            "frequency_mhz": 5800,
            "gain_dbi": 13.5,
            "polarization": "RHCP",
            "connector": "SMA",
            "type": "directional"
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
