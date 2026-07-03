#!/usr/bin/env python3
"""Second follow-up batch of real, current-production FPV parts, focused on
categories under-filled by batch50 (GPS, VTX, camera, receiver, antenna)."""
import json

NEW_PARTS = [
    # ========== GPS ==========
    {
        "id": "beitian-bn-880q-gps",
        "category": "gps",
        "name": "BN-880Q GPS + Compass",
        "brand": "Beitian",
        "price_php": 896,
        "weight_g": 11,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=Beitian+BN-880Q+GPS+Compass",
        "color": "#0a0a0a",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M8",
            "update_rate_hz": 10,
            "fix_time_s": 15,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "radiomaster-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "RadioMaster",
        "price_php": 1288,
        "weight_g": 8.5,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=M10+GPS+Module",
        "color": "#222266",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 11,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "flywoo-m10-nano-gps",
        "category": "gps",
        "name": "M10 Nano GPS Module",
        "brand": "Flywoo",
        "price_php": 1120,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://flywoo.net/search?q=M10+Nano+GPS+Module",
        "color": "#111111",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 13,
            "compass": False,
            "connector": "JST-SH 4-pin"
        }
    },
    {
        "id": "iflight-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "iFlight",
        "price_php": 1176,
        "weight_g": 9,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=M10+GPS+Module",
        "color": "#0d0d0d",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 12,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "hglrc-m100-5883-gps",
        "category": "gps",
        "name": "M100-5883 GPS + Compass",
        "brand": "HGLRC",
        "price_php": 1512,
        "weight_g": 8,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=M100-5883+GPS+Compass",
        "color": "#111122",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS+Galileo",
            "chipset": "u-blox M10",
            "update_rate_hz": 25,
            "fix_time_s": 9,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    {
        "id": "geprc-m10-gps-module",
        "category": "gps",
        "name": "M10 GPS Module",
        "brand": "GEPRC",
        "price_php": 1064,
        "weight_g": 8.2,
        "in_stock": True,
        "buy_url": "https://geprc.com/search?q=M10+GPS+Module",
        "color": "#0f0f0f",
        "specs": {
            "constellation": "GPS+BeiDou+GLONASS",
            "chipset": "u-blox M10",
            "update_rate_hz": 10,
            "fix_time_s": 12,
            "compass": True,
            "connector": "JST-SH 6-pin"
        }
    },
    # ========== VTX ==========
    {
        "id": "hdzero-ultimate-1w-vtx",
        "category": "vtx",
        "name": "Ultimate 1W VTX",
        "brand": "HDZero",
        "price_php": 6216,
        "weight_g": 10.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Ultimate+1W+VTX",
        "color": "#101010",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Digital HD",
            "bands": "N/A",
            "voltage_range": "7-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "walksnail-moonlight-vtx",
        "category": "vtx",
        "name": "Moonlight HD VTX",
        "brand": "Walksnail",
        "price_php": 5544,
        "weight_g": 9.8,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Moonlight+HD+VTX",
        "color": "#0a0a0a",
        "specs": {
            "power_mw_max": 600,
            "protocol": "Digital HD",
            "bands": "N/A",
            "voltage_range": "6-27V",
            "connector": "U.FL"
        }
    },
    {
        "id": "foxeer-echo-vtx",
        "category": "vtx",
        "name": "Echo 5.8GHz 1W VTX",
        "brand": "Foxeer",
        "price_php": 2072,
        "weight_g": 7.2,
        "in_stock": True,
        "buy_url": "https://www.foxeer.com/search?q=Echo+5.8GHz+1W+VTX",
        "color": "#151515",
        "specs": {
            "power_mw_max": 1000,
            "protocol": "Analog",
            "bands": "A/B/E/F/R/L",
            "voltage_range": "7-26V",
            "connector": "MMCX"
        }
    },
    {
        "id": "iflight-blitz-hd-vtx",
        "category": "vtx",
        "name": "BLITZ HD Whoop VTX",
        "brand": "iFlight",
        "price_php": 3416,
        "weight_g": 5.2,
        "in_stock": True,
        "buy_url": "https://shop.iflight.com/search?q=BLITZ+HD+Whoop+VTX",
        "color": "#111133",
        "specs": {
            "power_mw_max": 400,
            "protocol": "Digital HD",
            "bands": "N/A",
            "voltage_range": "6-17V",
            "connector": "U.FL"
        }
    },
    {
        "id": "speedybee-tx800-vtx",
        "category": "vtx",
        "name": "TX800 5.8GHz VTX",
        "brand": "SpeedyBee",
        "price_php": 1680,
        "weight_g": 6.8,
        "in_stock": True,
        "buy_url": "https://www.speedybee.com/search?q=TX800+5.8GHz+VTX",
        "color": "#001133",
        "specs": {
            "power_mw_max": 800,
            "protocol": "Analog",
            "bands": "A/B/E/F/R",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    {
        "id": "caddx-vista-2-vtx",
        "category": "vtx",
        "name": "Vista 2 Digital VTX",
        "brand": "Caddx",
        "price_php": 5152,
        "weight_g": 8.8,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Vista+2+Digital+VTX",
        "color": "#121212",
        "specs": {
            "power_mw_max": 700,
            "protocol": "Digital HD",
            "bands": "N/A",
            "voltage_range": "7-26V",
            "connector": "U.FL"
        }
    },
    # ========== CAMERAS ==========
    {
        "id": "walksnail-moonlight-cam",
        "category": "camera",
        "name": "Moonlight HD Nano Camera",
        "brand": "Walksnail",
        "price_php": 3696,
        "weight_g": 5.8,
        "in_stock": True,
        "buy_url": "https://store.walksnail.com/search?q=Moonlight+HD+Nano+Camera",
        "color": "#0a0a0a",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital HD",
            "tvl": 1100,
            "voltage_range": "6-27V"
        }
    },
    {
        "id": "hdzero-ultimate-cam",
        "category": "camera",
        "name": "Ultimate HD Camera",
        "brand": "HDZero",
        "price_php": 4816,
        "weight_g": 7.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HDZero+Ultimate+HD+Camera",
        "color": "#101010",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 155,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "7-27V"
        }
    },
    {
        "id": "runcam-master-cam",
        "category": "camera",
        "name": "Master Nano Camera",
        "brand": "RunCam",
        "price_php": 1904,
        "weight_g": 5.5,
        "in_stock": True,
        "buy_url": "https://www.runcam.com/search?q=Master+Nano+Camera",
        "color": "#101010",
        "specs": {
            "sensor": "1/1.8\" CMOS",
            "fov_deg": 160,
            "format": "Analog",
            "tvl": 1200,
            "voltage_range": "5-40V"
        }
    },
    {
        "id": "caddx-nebula-pro-nova-cam",
        "category": "camera",
        "name": "Nebula Pro Nova Digital Camera",
        "brand": "Caddx",
        "price_php": 4592,
        "weight_g": 7.9,
        "in_stock": True,
        "buy_url": "https://caddxfpv.com/search?q=Nebula+Pro+Nova+Digital+Camera",
        "color": "#121212",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 155,
            "format": "Digital HD",
            "tvl": 1200,
            "voltage_range": "6-25V"
        }
    },
    {
        "id": "betafpv-nebula-pro-cam",
        "category": "camera",
        "name": "Nebula Pro Digital Camera",
        "brand": "BetaFPV",
        "price_php": 3920,
        "weight_g": 4.6,
        "in_stock": True,
        "buy_url": "https://betafpv.com/search?q=Nebula+Pro+Digital+Camera",
        "color": "#111",
        "specs": {
            "sensor": "1/2\" CMOS",
            "fov_deg": 150,
            "format": "Digital HD",
            "tvl": 1100,
            "voltage_range": "6-25V"
        }
    },
    # ========== RECEIVERS ==========
    {
        "id": "radiomaster-rp4td-elrs-receiver",
        "category": "receiver",
        "name": "RP4TD 2.4GHz ExpressLRS Diversity Receiver",
        "brand": "RadioMaster",
        "price_php": 1064,
        "weight_g": 2.0,
        "in_stock": True,
        "buy_url": "https://www.radiomasterrc.com/search?q=RP4TD+ExpressLRS+Diversity+Receiver",
        "color": "#222266",
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
        "name": "EP2 ExpressLRS 2.4GHz Receiver",
        "brand": "HappyModel",
        "price_php": 728,
        "weight_g": 1.2,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=HappyModel+EP2+ExpressLRS+2.4GHz+Receiver",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "ExpressLRS",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    {
        "id": "tbs-nano-rx-long-range",
        "category": "receiver",
        "name": "Crossfire Nano RX Long Range",
        "brand": "TBS",
        "price_php": 1400,
        "weight_g": 1.6,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TBS+Crossfire+Nano+RX+Long+Range",
        "color": "#151515",
        "specs": {
            "protocol": "TBS Crossfire",
            "frequency_mhz": 915,
            "diversity": False,
            "telemetry": True
        }
    },
    {
        "id": "flysky-fs-x8b-receiver",
        "category": "receiver",
        "name": "FS-X8B 2.4GHz Receiver",
        "brand": "FlySky",
        "price_php": 616,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=FlySky+FS-X8B+2.4GHz+Receiver",
        "color": "#1a1a1a",
        "specs": {
            "protocol": "FlySky AFHDS 2A",
            "frequency_mhz": 2400,
            "diversity": True,
            "telemetry": True
        }
    },
    # ========== ANTENNAS ==========
    {
        "id": "truerc-abomination-sma",
        "category": "antenna",
        "name": "Abomination 5.8GHz SMA Antenna",
        "brand": "TrueRC",
        "price_php": 1120,
        "weight_g": 7,
        "in_stock": True,
        "buy_url": "https://www.getfpv.com/catalogsearch/result/?q=TrueRC+Abomination+5.8GHz+SMA+Antenna",
        "color": "#111111",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 5.8,
            "type": "patch"
        }
    },
    {
        "id": "rushfpv-cherry-sma-v2",
        "category": "antenna",
        "name": "Cherry V2 5.8GHz SMA Antenna",
        "brand": "Rush",
        "price_php": 616,
        "weight_g": 4.5,
        "in_stock": True,
        "buy_url": "https://www.rushfpv.com/search?q=Cherry+V2+5.8GHz+SMA+Antenna",
        "color": "#121212",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "RHCP",
            "connector": "SMA",
            "gain_dbi": 2.5,
            "type": "cloverleaf"
        }
    },
    {
        "id": "hglrc-5-8ghz-mushroom-sma",
        "category": "antenna",
        "name": "5.8GHz Mushroom Antenna SMA",
        "brand": "HGLRC",
        "price_php": 336,
        "weight_g": 3.5,
        "in_stock": True,
        "buy_url": "https://www.hglrc.com/search?q=5.8GHz+Mushroom+Antenna+SMA",
        "color": "#111122",
        "specs": {
            "frequency_ghz": 5.8,
            "polarization": "LHCP",
            "connector": "SMA",
            "gain_dbi": 1.5,
            "type": "omnidirectional"
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
