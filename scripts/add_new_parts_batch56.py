#!/usr/bin/env python3
"""Batch 56: real, current-production FPV parts across all 11 categories,
adding more brand/model coverage on top of batch55."""
import json

NEW_PARTS = [
    # ========== FRAME ==========
    {
        "id": "iflight-nazgul5-v2-frame",
        "category": "frame",
        "name": "Nazgul5 V2 Frame Kit",
        "brand": "iFlight",
        "price_php": 2128,
        "weight_g": 98,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=Nazgul5+V2+Frame+Kit",
        "color": "#161616",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "tbs-source-one-r2-frame",
        "category": "frame",
        "name": "Source One R2 Frame Kit",
        "brand": "TBS",
        "price_php": 1848,
        "weight_g": 92,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Source+One+R2+Frame+Kit",
        "color": "#101010",
        "specs": {
            "size_mm": 220,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    {
        "id": "geprc-mark5-hd-frame",
        "category": "frame",
        "name": "Mark5 HD Frame Kit",
        "brand": "GEPRC",
        "price_php": 2576,
        "weight_g": 108,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=Mark5+HD+Frame+Kit",
        "color": "#141414",
        "specs": {
            "size_mm": 225,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 4.5,
            "standoff_height_mm": 27
        }
    },
    {
        "id": "hglrc-sector5-v3-frame",
        "category": "frame",
        "name": "Sector 5 V3 Frame Kit",
        "brand": "HGLRC",
        "price_php": 1792,
        "weight_g": 89,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=Sector+5+V3+Frame+Kit",
        "color": "#0f0f0f",
        "specs": {
            "size_mm": 222,
            "motor_mount_mm": 25.5,
            "prop_clearance_inch": 5,
            "stack_mount_mm": 30.5,
            "material": "3K carbon fiber",
            "arm_thickness_mm": 4,
            "standoff_height_mm": 25
        }
    },
    # ========== MOTOR ==========
    {
        "id": "tmotor-f60-pro-v-2207-motor",
        "category": "motor",
        "name": "F60 Pro V 2207 1950KV",
        "brand": "T-Motor",
        "price_php": 1624,
        "weight_g": 32,
        "in_stock": True,
        "buy_url": "https://store.tmotor.com/search?q=F60+Pro+V+2207+1950KV",
        "color": "#1c1c1c",
        "specs": {
            "kv": 1950,
            "stator_size": "2207",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 42
        }
    },
    {
        "id": "brotherhobby-avenger-23065-motor",
        "category": "motor",
        "name": "Avenger 2306.5 1900KV",
        "brand": "BrotherHobby",
        "price_php": 1400,
        "weight_g": 33,
        "in_stock": True,
        "buy_url": "https://www.brotherhobby.com/search?q=Avenger+2306.5+1900KV",
        "color": "#202020",
        "specs": {
            "kv": 1900,
            "stator_size": "2306",
            "motor_mount_mm": 16,
            "min_voltage_s": 4,
            "max_voltage_s": 6,
            "shaft_mm": 5,
            "peak_current_a": 40
        }
    },
    {
        "id": "flywoo-nin-1404-4600kv-motor",
        "category": "motor",
        "name": "NIN 1404 4600KV",
        "brand": "Flywoo",
        "price_php": 728,
        "weight_g": 11.5,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=NIN+1404+4600KV",
        "color": "#0d0d0d",
        "specs": {
            "kv": 4600,
            "stator_size": "1404",
            "motor_mount_mm": 9,
            "min_voltage_s": 3,
            "max_voltage_s": 4,
            "shaft_mm": 1.5,
            "peak_current_a": 18
        }
    },
    # ========== ESC ==========
    {
        "id": "speedybee-f405-v4-55a-esc",
        "category": "esc",
        "name": "F405 V4 55A 4-in-1 ESC",
        "brand": "SpeedyBee",
        "price_php": 2912,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=F405+V4+55A+4-in-1+ESC",
        "color": "#003322",
        "specs": {
            "amp_rating": 55,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 65
        }
    },
    {
        "id": "holybro-tekko32-f4-45a-esc",
        "category": "esc",
        "name": "Tekko32 F4 45A 4-in-1 ESC",
        "brand": "Holybro",
        "price_php": 2632,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Tekko32+F4+45A+4-in-1+ESC",
        "color": "#001a33",
        "specs": {
            "amp_rating": 45,
            "input_voltage_s": 6,
            "protocol": "DSHOT600",
            "form_factor_mm": 30,
            "burst_amp": 55
        }
    },
    # ========== FC ==========
    {
        "id": "holybro-kakute-h7-v2-fc",
        "category": "fc",
        "name": "Kakute H7 V2 Flight Controller",
        "brand": "Holybro",
        "price_php": 3416,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=Kakute+H7+V2+Flight+Controller",
        "color": "#001122",
        "specs": {
            "gyro": "ICM42688P",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": True,
            "blackbox": True,
            "uart_count": 8,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    {
        "id": "speedybee-f405-v4-fc",
        "category": "fc",
        "name": "F405 V4 Flight Controller",
        "brand": "SpeedyBee",
        "price_php": 2016,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=F405+V4+Flight+Controller",
        "color": "#003322",
        "specs": {
            "gyro": "MPU6000",
            "firmware": "Betaflight",
            "form_factor_mm": 30.5,
            "stack_mount_mm": 30.5,
            "barometer": False,
            "blackbox": True,
            "uart_count": 6,
            "5v_pad_count": 2,
            "curr_sensor": True
        }
    },
    # ========== PROPELLER ==========
    {
        "id": "hqprop-r38-5x38-propeller",
        "category": "propeller",
        "name": "R38 5x3.8x3 Tri-blade",
        "brand": "HQProp",
        "price_php": 224,
        "weight_g": 4.7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HQProp+R38+5x3.8x3",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5,
            "pitch": 3.8,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey"
            ]
        }
    },
    {
        "id": "gemfan-hurricane-51466-propeller",
        "category": "propeller",
        "name": "Hurricane 51466 Tri-blade",
        "brand": "Gemfan",
        "price_php": 196,
        "weight_g": 4.3,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Gemfan+Hurricane+51466",
        "color": "#1a1a1a",
        "specs": {
            "diameter_inch": 5.1,
            "pitch": 4.66,
            "blade_count": 3,
            "shaft_mm": 5,
            "color_options": [
                "black",
                "grey",
                "orange"
            ]
        }
    },
    # ========== CAMERA ==========
    {
        "id": "foxeer-razer-mini-camera",
        "category": "camera",
        "name": "Razer Mini 1200TVL Analog",
        "brand": "Foxeer",
        "price_php": 1064,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Razer+Mini+1200TVL",
        "color": "#161616",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "runcam-phoenix2-camera",
        "category": "camera",
        "name": "Phoenix 2 1000TVL Analog",
        "brand": "RunCam",
        "price_php": 1176,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Phoenix+2+1000TVL",
        "color": "#0d0d0d",
        "specs": {
            "sensor": "1/3\" CMOS",
            "fov_deg": 155,
            "format": "Analog",
            "tvl": 1000,
            "voltage_range": "5-40V"
        }
    },
    # ========== VTX ==========
    {
        "id": "walksnail-avatar-hd-v3-vtx",
        "category": "vtx",
        "name": "Avatar HD Kit V3 VTX",
        "brand": "Walksnail",
        "price_php": 8960,
        "weight_g": 14,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Avatar+HD+Kit+V3+VTX",
        "color": "#111827",
        "specs": {
            "power_mw_max": 1200,
            "protocol": "Digital HD",
            "bands": "5.8GHz",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "iflight-tf1000-vtx",
        "category": "vtx",
        "name": "TF1000 5.8GHz 1W VTX",
        "brand": "iFlight",
        "price_php": 3080,
        "weight_g": 17,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=TF1000+5.8GHz+1W+VTX",
        "color": "#181818",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/D",
            "voltage_range": "7-27V",
            "connector": "MMCX"
        }
    },
    # ========== BATTERY ==========
    {
        "id": "cnhl-black-series-6s-1300mah-battery",
        "category": "battery",
        "name": "Black Series 1300mAh 6S 100C",
        "brand": "CNHL",
        "price_php": 2464,
        "weight_g": 226,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=CNHL+Black+Series+1300mAh+6S+100C",
        "color": "#0a0a0a",
        "specs": {
            "cell_count_s": 6,
            "capacity_mah": 1300,
            "c_rating": 100,
            "connector": "XT60",
            "voltage_nominal": 22.2
        }
    },
    {
        "id": "tattu-r-line-v5-4s-1550mah-battery",
        "category": "battery",
        "name": "R-Line V5.0 1550mAh 4S 150C",
        "brand": "Tattu",
        "price_php": 2072,
        "weight_g": 188,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Tattu+R-Line+V5.0+1550mAh+4S+150C",
        "color": "#1a1a2e",
        "specs": {
            "cell_count_s": 4,
            "capacity_mah": 1550,
            "c_rating": 150,
            "connector": "XT60",
            "voltage_nominal": 14.8
        }
    },
    # ========== RECEIVER ==========
    {
        "id": "radiomaster-bandit-nano-elrs-receiver",
        "category": "receiver",
        "name": "Bandit Nano ELRS Receiver",
        "brand": "RadioMaster",
        "price_php": 896,
        "weight_g": 1.1,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=Bandit+Nano+ELRS+Receiver",
        "color": "#222222",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "happymodel-ep2-elrs-receiver",
        "category": "receiver",
        "name": "EP2 2.4G ELRS PWM Receiver",
        "brand": "HappyModel",
        "price_php": 616,
        "weight_g": 0.9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+2.4G+ELRS+PWM+Receiver",
        "color": "#333333",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": False,
            "telemetry": True
        }
    },
    # ========== GPS ==========
    {
        "id": "holybro-m9n-gps",
        "category": "gps",
        "name": "M9N GPS Module",
        "brand": "Holybro",
        "price_php": 2744,
        "weight_g": 18,
        "in_stock": True,
        "buy_url": "https://holybro.com/search?q=M9N+GPS+Module",
        "color": "#101010",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M9N",
            "update_rate_hz": 10,
            "fix_time_s": 18,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    {
        "id": "beitian-bn-880q-gps",
        "category": "gps",
        "name": "BN-880Q GPS Module",
        "brand": "Beitian",
        "price_php": 1176,
        "weight_g": 12,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880Q+GPS+Module",
        "color": "#1c1c1c",
        "specs": {
            "constellation": "GPS+GLONASS+BeiDou",
            "chipset": "u-blox M8N",
            "update_rate_hz": 10,
            "fix_time_s": 26,
            "compass": True,
            "connector": "JST-GH 6-pin"
        }
    },
    # ========== ANTENNA ==========
    {
        "id": "foxeer-lollipop-4-rhcp-antenna",
        "category": "antenna",
        "name": "Lollipop 4 5.8GHz RHCP SMA",
        "brand": "Foxeer",
        "price_php": 616,
        "weight_g": 5,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Lollipop+4+5.8GHz+RHCP",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.3,
            "type": "cloverleaf"
        }
    },
    {
        "id": "tbs-triumph-pro-rhcp-antenna",
        "category": "antenna",
        "name": "Triumph Pro 5.8GHz RHCP SMA",
        "brand": "TBS",
        "price_php": 1120,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Triumph+Pro+5.8GHz+RHCP",
        "color": "#0f0f0f",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 3.8,
            "type": "patch"
        }
    },
]


def main():
    with open("data/parts.json", "r") as f:
        data = json.load(f)

    existing_ids = {p["id"] for p in data["parts"]}
    added = 0
    skipped = 0

    for part in NEW_PARTS:
        if part["id"] in existing_ids:
            print(f"  SKIP (duplicate): {part['id']}")
            skipped += 1
        else:
            data["parts"].append(part)
            existing_ids.add(part["id"])
            added += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = len(data["parts"])
    print(f"\nAdded {added} new parts (skipped {skipped} duplicates)")
    print(f"Total parts now: {total}")

    from collections import Counter
    cats = Counter(p["category"] for p in data["parts"])
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
