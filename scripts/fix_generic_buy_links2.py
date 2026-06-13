"""Replace remaining generic root-domain buy_url links (brand homepages with
no product path) with a GetFPV search URL for the specific part, since GetFPV
carries nearly all of these brands and a search results page is far more
useful to a buyer than a bare homepage.
"""
import json
import re
from urllib.parse import quote_plus

GENERIC_RE = re.compile(r"^https?://[^/]+/?$")


def main():
    with open("data/parts.json") as f:
        data = json.load(f)

    fixed = 0
    for part in data["parts"]:
        url = part.get("buy_url", "")
        if not GENERIC_RE.match(url):
            continue

        query = quote_plus(f"{part['brand']} {part['name']}")
        part["buy_url"] = f"https://www.getfpv.com/catalogsearch/result/?q={query}"
        fixed += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Fixed {fixed} generic buy_url links")


if __name__ == "__main__":
    main()
