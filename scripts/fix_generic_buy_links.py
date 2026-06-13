"""Replace generic root-domain buy_url links with retailer search URLs
pointing at the specific product, using brand + name as the query.
"""
import json
import re
from urllib.parse import quote_plus

MAGENTO_SEARCH = {
    "https://www.getfpv.com": "https://www.getfpv.com/catalogsearch/result/?q={q}",
}

KEYWORDS_SEARCH = {
    "https://www.foxeer.com": "https://www.foxeer.com/search?keywords={q}",
}

# Domain rewrites applied before the generic shopify search template
DOMAIN_REWRITE = {
    "https://www.walksnail.com": "https://store.walksnail.com",
}

SHOPIFY_SEARCH_DOMAINS = {
    "https://www.racedayquads.com",
    "https://betafpv.com",
    "https://shop.iflight.com",
    "https://flywoo.net",
    "https://www.hglrc.com",
    "https://geprc.com",
    "https://geprc.com/",
    "https://holybro.com",
    "https://www.diatone.us",
    "https://www.radiomasterrc.com",
    "https://www.rushfpv.com",
    "https://www.axisflying.com",
    "https://www.lumenier.com",
    "https://chinahobbyline.com",
    "https://caddxfpv.com",
    "https://www.brotherhobby.com",
    "https://www.walksnail.com",
}

SHOPIFY_TEMPLATE = "{domain}/search?q={q}"

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

        if url in MAGENTO_SEARCH:
            part["buy_url"] = MAGENTO_SEARCH[url].format(q=query)
            fixed += 1
        elif url in KEYWORDS_SEARCH:
            part["buy_url"] = KEYWORDS_SEARCH[url].format(q=query)
            fixed += 1
        elif url in SHOPIFY_SEARCH_DOMAINS:
            domain = DOMAIN_REWRITE.get(url, url).rstrip("/")
            part["buy_url"] = SHOPIFY_TEMPLATE.format(domain=domain, q=query)
            fixed += 1

    with open("data/parts.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Fixed {fixed} generic buy_url links")


if __name__ == "__main__":
    main()
