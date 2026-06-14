"""Replace remaining generic root-domain buy_url links (brand homepages with
no product path) with a GetFPV catalog search for the part, since GetFPV
carries essentially every FPV brand and its search URLs always resolve.
"""
import json
import re
from urllib.parse import quote_plus

GENERIC_RE = re.compile(r"^https?://[^/]+/?$")
GETFPV_SEARCH = "https://www.getfpv.com/catalogsearch/result/?q={q}"


def main():
    with open("data/parts.json") as f:
        data = json.load(f)

    fixed = 0
    for part in data["parts"]:
        url = part.get("buy_url", "")
        if not GENERIC_RE.match(url):
            continue

        query = quote_plus(f"{part['brand']} {part['name']}")
        part["buy_url"] = GETFPV_SEARCH.format(q=query)
        fixed += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Fixed {fixed} generic buy_url links")


if __name__ == "__main__":
    main()
