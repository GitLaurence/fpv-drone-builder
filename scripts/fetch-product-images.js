#!/usr/bin/env node
/**
 * Fetch product images using fetch(). No npm install needed.
 *
 * Strategy per part (tried in order):
 *   1. Brand Shopify predictive search  — /search/suggest.json on the
 *      brand's own site (works for Shopify brands like iFlight, BetaFPV…)
 *   2. Brand Shopify catalog match      — /products.json fuzzy match
 *   3. Retailer predictive search       — searches GetFPV and RaceDayQuads,
 *      which carry essentially every FPV brand including non-Shopify ones
 *      (Gemfan, HQProp, RunCam, Foxeer, Matek, T-Motor, CNHL, FlySky…)
 *   4. HTML search on brand site        — last resort; extracts structured
 *      product image from the response HTML
 *
 * All strategies filter out logo/banner/social images via isProductImage().
 * Parts whose current image_url looks like a logo are automatically
 * re-fetched on a normal run (no --force needed).
 *
 * Requirements: Node 18+ (built-in fetch). No npm install needed.
 *
 * Usage:
 *   node scripts/fetch-product-images.js            # fetch missing + fix logos
 *   node scripts/fetch-product-images.js --dry-run  # show queries, no writes
 *   node scripts/fetch-product-images.js --force    # re-fetch everything
 */

import { readFileSync, writeFileSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';

const __dir        = dirname(fileURLToPath(import.meta.url));
const PARTS_PATH   = resolve(__dir, '../data/parts.json');
const CACHE_PATH   = resolve(__dir, 'image-cache.json');
const CATALOG_PATH = resolve(__dir, 'brand-catalog.json');

const DRY_RUN  = process.argv.includes('--dry-run');
const FORCE    = process.argv.includes('--force');
const TIMEOUT  = 12000;
const DELAY_MS = 600;

const BRAND_DOMAINS = {
  'AKK':        'www.akktek.com',
  'Aikon':      'aikonfpv.com',
  'Armattan':   'armattanquads.com',
  'BetaFPV':    'betafpv.com',
  'Caddx':      'caddxfpv.com',
  'CNHL':       'www.chinahobbyline.com',
  'DAL':        'dalprops.com',
  'Diatone':    'www.diatone.us',
  'DJI':        'store.dji.com',
  'EMAX':       'emaxmodel.com',
  'Ethix':      'ethix.cc',
  'ExpressLRS': 'expresslrs.org',
  'FlyFishRC':  'www.flyfish-rc.com',
  'FlySky':     'www.flysky-cn.com',
  'Flywoo':     'flywoo.net',
  'Foxeer':     'www.foxeer.com',
  'FrSky':      'www.frsky-rc.com',
  'Gemfan':     'www.gemfanhobby.com',
  'GEPRC':      'geprc.com',
  'GNB':        'www.gaonengmodels.com',
  'HappyModel': 'www.happymodel.cn',
  'HDZero':     'www.hd-zero.com',
  'HGLRC':      'www.hglrc.com',
  'Hobbywing':  'www.hobbywing.com',
  'Holybro':    'holybro.com',
  'HQProp':     'www.hqprop.com',
  'Hypetrain':  'hypetrain.io',
  'iFlight':    'iflight-rc.com',
  'ImmersionRC':'www.immersionrc.com',
  'ImpulseRC':  'www.impulserc.com',
  'JHEMCU':     'jhemcu.com',
  'Jumper':     'www.jumper-rc.com',
  'Lumenier':   'www.lumenier.com',
  'Matek':      'www.mateksys.com',
  'MEPS':       'www.mepsrc.com',
  'Ovonic':     'www.ovonicshop.com',
  'Racerstar':  'www.racerstar.com',
  'RadioMaster':'www.radiomasterrc.com',
  'RunCam':     'www.runcam.com',
  'Rush':       'rushfpv.net',
  'ShenDrones': 'shendrones.com',
  'Spektrum':   'www.spektrumrc.com',
  'SpeedyBee':  'www.speedybee.com',
  'Tattu':      'www.genstattu.com',
  'TBS':        'www.team-blacksheep.com',
  'T-Motor':    'store.tmotor.com',
  'Walksnail':  'www.walksnail.com',
};

const HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/json,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.9',
};

// ── Load data ──────────────────────────────────────────

const data    = JSON.parse(readFileSync(PARTS_PATH, 'utf8'));
const cache   = existsSync(CACHE_PATH)   ? JSON.parse(readFileSync(CACHE_PATH, 'utf8'))   : {};
const catalog = existsSync(CATALOG_PATH) ? JSON.parse(readFileSync(CATALOG_PATH, 'utf8')) : {};

// Re-fetch if: no image, never tried, or current image looks like a logo
const todo = data.parts.filter(p =>
  FORCE ||
  (!p.image_url && cache[p.id] === undefined) ||
  (p.image_url && !isProductImage(p.image_url))
);
console.log(`Parts to fetch: ${todo.length} of ${data.parts.length}`);

if (DRY_RUN) {
  const byBrand = {};
  todo.forEach(p => (byBrand[p.brand] = (byBrand[p.brand] || 0) + 1));
  Object.entries(byBrand).forEach(([b, n]) => console.log(`  ${b} (${BRAND_DOMAINS[b] || '?'}): ${n} parts`));
  process.exit(0);
}

if (todo.length === 0) {
  console.log('Nothing to do — all parts already have good images.');
  process.exit(0);
}

// ── Image quality filter ───────────────────────────────
// Returns false for URLs that look like logos, banners, or store assets
// rather than actual product photos.

const LOGO_KEYWORDS = [
  'logo', 'social', 'banner', 'icon', 'flag', 'header', 'footer',
  'placeholder', 'badge', 'avatar', 'favicon', 'sprite', 'loading',
  'no-image', 'noimage', 'default', 'blank', 'bg-', '-bg.', 'background',
];

function isProductImage(url) {
  if (!url) return false;
  const u = url.toLowerCase();
  return !LOGO_KEYWORDS.some(k => u.includes(k));
}

// ── HTTP helpers ───────────────────────────────────────

async function fetchText(url) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), TIMEOUT);
  try {
    const res = await fetch(url, { headers: HEADERS, signal: ctrl.signal, redirect: 'follow' });
    if (!res.ok) return null;
    return await res.text();
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}

async function fetchJSON(url) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), TIMEOUT);
  try {
    const res = await fetch(url, { headers: { ...HEADERS, Accept: 'application/json' }, signal: ctrl.signal, redirect: 'follow' });
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}

// ── Similarity / matching ──────────────────────────────

function similarity(a, b) {
  const tok = s => new Set(s.toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/).filter(Boolean));
  const A = tok(a), B = tok(b);
  let inter = 0;
  A.forEach(t => { if (B.has(t)) inter++; });
  return inter / (A.size + B.size - inter);
}

function bestMatch(products, partName) {
  let best = null, bestScore = 0;
  for (const p of products) {
    const s = similarity(partName, p.title);
    if (s > bestScore) { bestScore = s; best = p; }
  }
  return bestScore >= 0.35 ? best : null;
}

// ── Image extraction from HTML ─────────────────────────
// Priority: JSON-LD Product schema > Shopify /products/ CDN path >
//           filtered Shopify /files/ CDN > og:image (last resort)

function extractImageFromHTML(html) {
  if (!html) return null;

  // 1. JSON-LD Product schema — structured data is the most reliable signal
  const jsonld = html.match(/"@type"\s*:\s*"Product"[\s\S]{0,800}?"image"\s*:\s*"([^"]+)"/);
  if (jsonld?.[1] && isProductImage(jsonld[1])) return jsonld[1];

  // 2. Shopify CDN /products/ path (product images, not store assets)
  const shopifyProduct = html.match(/https:\/\/cdn\.shopify\.com\/s\/files\/[^"'\s]+\/products\/[^"'\s]+\.(?:jpe?g|png|webp)/i);
  if (shopifyProduct) return cleanImgUrl(shopifyProduct[0]);

  // 3. Any Shopify CDN image that passes the logo filter
  const allShopify = [...html.matchAll(/https:\/\/cdn\.shopify\.com\/s\/files\/[^"'\s]+\.(?:jpe?g|png|webp)/gi)];
  for (const m of allShopify) {
    if (isProductImage(m[0])) return cleanImgUrl(m[0]);
  }

  // 4. og:image — last resort; often a brand logo but worth trying if nothing else worked
  const og = html.match(/<meta[^>]+property=["']og:image["'][^>]+content=["']([^"']+)["']/i)
          || html.match(/<meta[^>]+content=["']([^"']+)["'][^>]+property=["']og:image["']/i);
  if (og?.[1] && isProductImage(og[1])) return og[1];

  return null;
}

function cleanImgUrl(url) {
  return url.replace(/_\d+x\d+(\.\w+)$/, '$1');
}

// ── Strategy 1: Shopify predictive search ─────────────
// /search/suggest.json returns direct product matches with images —
// more accurate than fuzzy-matching the full catalog.

async function searchShopifyPredictive(domain, partName) {
  const url = `https://${domain}/search/suggest.json?q=${encodeURIComponent(partName)}&resources[type]=product&resources[limit]=6`;
  const json = await fetchJSON(url);
  const products = json?.resources?.results?.products;
  if (!products?.length) return null;

  let best = null, bestScore = 0;
  for (const p of products) {
    const s = similarity(partName, p.title);
    if (s > bestScore) { bestScore = s; best = p; }
  }
  if (bestScore < 0.25 || !best) return null;

  const img = best.image;
  return (img && isProductImage(img)) ? img : null;
}

// ── Strategy 2: Shopify products.json catalog ─────────

async function fetchShopifyCatalog(domain) {
  if (catalog[domain]) return catalog[domain];

  const products = [];
  let page = 1;
  while (true) {
    const json = await fetchJSON(`https://${domain}/products.json?limit=250&page=${page}`);
    if (!json?.products?.length) break;
    json.products.forEach(p => {
      // Prefer images from /products/ path; fall back to any image that passes the filter
      const img = p.images?.find(i => i.src?.includes('/products/'))?.src
               || p.images?.find(i => isProductImage(i.src))?.src;
      if (img) products.push({ title: p.title, image: cleanImgUrl(img) });
    });
    if (json.products.length < 250) break;
    page++;
    await delay(300);
  }

  if (products.length > 0) {
    catalog[domain] = products;
    writeFileSync(CATALOG_PATH, JSON.stringify(catalog, null, 2));
    console.log(`    catalog: ${products.length} products from ${domain}`);
  }
  return products;
}

// ── Strategy 3: FPV retailer search ───────────────────
// GetFPV and RaceDayQuads carry essentially every FPV brand, including
// ones whose own sites are not on Shopify (Gemfan, HQProp, RunCam,
// Foxeer, Matek, T-Motor, CNHL, FlySky, DJI, Hobbywing…).
// Query includes the brand name to disambiguate generic part names.

const FPV_RETAILERS = [
  'www.getfpv.com',
  'www.racedayquads.com',
];

async function searchRetailers(brand, partName) {
  const query = `${brand} ${partName}`;
  for (const domain of FPV_RETAILERS) {
    const img = await searchShopifyPredictive(domain, query);
    if (img) return img;
    await delay(300);
  }
  return null;
}

// ── Strategy 4: HTML search on brand site (last resort) ──

async function searchHTML(domain, partName) {
  const queries = [
    `https://${domain}/search?type=product&q=${encodeURIComponent(partName)}`,
    `https://${domain}/search?q=${encodeURIComponent(partName)}`,
    `https://${domain}/catalogsearch/result/?q=${encodeURIComponent(partName)}`,
  ];
  for (const url of queries) {
    const html = await fetchText(url);
    const img  = extractImageFromHTML(html);
    if (img) return img;
    await delay(300);
  }
  return null;
}

// ── Per-part lookup ────────────────────────────────────

async function findImage(part) {
  const domain = BRAND_DOMAINS[part.brand];

  if (domain) {
    // Strategy 1: Brand Shopify predictive search
    const predictive = await searchShopifyPredictive(domain, part.name);
    if (predictive) return predictive;
    await delay(200);

    // Strategy 2: Brand Shopify catalog match
    const products = await fetchShopifyCatalog(domain);
    if (products.length > 0) {
      const match = bestMatch(products, part.name);
      if (match && isProductImage(match.image)) return match.image;
    }
  }

  // Strategy 3: FPV retailer search (covers non-Shopify brands)
  const retailer = await searchRetailers(part.brand, part.name);
  if (retailer) return retailer;

  // Strategy 4: HTML search on brand site
  if (domain) return await searchHTML(domain, part.name);

  return null;
}

// ── Utilities ──────────────────────────────────────────

const delay = ms => new Promise(r => setTimeout(r, ms));

function saveCache() {
  writeFileSync(CACHE_PATH, JSON.stringify(cache, null, 2));
}

// ── Main ───────────────────────────────────────────────

let found = 0, failed = 0;

const byBrand = {};
todo.forEach(p => (byBrand[p.brand] = [...(byBrand[p.brand] || []), p]));
const brands = Object.keys(byBrand);
console.log(`Brands to query: ${brands.join(', ')}\n`);

let idx = 0;
for (const brand of brands) {
  const parts  = byBrand[brand];
  const domain = BRAND_DOMAINS[brand];
  console.log(`\n── ${brand} (${domain || 'no domain'}) — ${parts.length} parts`);

  // Warm brand Shopify catalog once (skipped for non-Shopify sites — returns [] quickly)
  if (domain) await fetchShopifyCatalog(domain).catch(() => []);

  for (const part of parts) {
    idx++;
    process.stdout.write(`  [${idx}/${todo.length}] ${part.name} ... `);

    let url = null;
    try {
      url = await findImage(part);
    } catch (e) {
      process.stdout.write(`ERROR: ${e.message.slice(0, 60)}\n`);
    }

    cache[part.id] = url || null;
    saveCache();

    if (url) {
      process.stdout.write(`✓ ${url.slice(0, 90)}\n`);
      found++;
    } else {
      process.stdout.write(`✗\n`);
      failed++;
    }

    await delay(DELAY_MS);
  }
}

// Write image URLs back into parts.json (only set non-null results)
let updated = 0;
data.parts.forEach(p => {
  if (cache[p.id]) {
    p.image_url = cache[p.id];
    updated++;
  } else if (cache[p.id] === null && p.image_url && !isProductImage(p.image_url)) {
    // Clear logo images that we couldn't replace with a real photo
    delete p.image_url;
  }
});
writeFileSync(PARTS_PATH, JSON.stringify(data, null, 2));

console.log(`\n────────────────────────────────────────────`);
console.log(`Found:   ${found}`);
console.log(`Failed:  ${failed}`);
console.log(`Updated: ${updated} parts in data/parts.json`);
console.log(`Brand catalogs cached in scripts/brand-catalog.json`);
console.log(`Re-run to retry failed parts.`);
