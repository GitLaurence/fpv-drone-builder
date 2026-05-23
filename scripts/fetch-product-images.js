#!/usr/bin/env node
/**
 * Fetch product images from each brand's official website using fetch().
 *
 * Strategy per brand (tried in order):
 *   1. Shopify /products.json  — most FPV brands run Shopify; returns structured
 *      JSON with product titles + image URLs, no API key required.
 *   2. HTML search fallback    — fetch /search?q=<name>, extract the first
 *      product image from the response HTML (Shopify CDN pattern, og:image,
 *      or JSON-LD structured data).
 *
 * Brand product catalogs are cached in scripts/brand-catalog.json so each
 * brand's site is only hit once per run, even if they have many parts.
 * Per-part results are cached in scripts/image-cache.json so the script is
 * safe to interrupt and resume.
 *
 * Requirements: Node 18+ (built-in fetch). No npm install needed.
 *
 * Usage:
 *   node scripts/fetch-product-images.js            # fetch all missing images
 *   node scripts/fetch-product-images.js --dry-run  # show queries, no writes
 *   node scripts/fetch-product-images.js --force    # re-fetch even if cached
 */

import { readFileSync, writeFileSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';

const __dir       = dirname(fileURLToPath(import.meta.url));
const PARTS_PATH  = resolve(__dir, '../data/parts.json');
const CACHE_PATH  = resolve(__dir, 'image-cache.json');
const CATALOG_PATH = resolve(__dir, 'brand-catalog.json');

const DRY_RUN  = process.argv.includes('--dry-run');
const FORCE    = process.argv.includes('--force');
const TIMEOUT  = 12000;
const DELAY_MS = 800;

// Brand → official shop domain (overrides the favicon domain where they differ)
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

const todo = data.parts.filter(p => FORCE || (!p.image_url && cache[p.id] === undefined));
console.log(`Parts to fetch: ${todo.length} of ${data.parts.length}`);

if (DRY_RUN) {
  const byBrand = {};
  todo.forEach(p => (byBrand[p.brand] = (byBrand[p.brand] || 0) + 1));
  Object.entries(byBrand).forEach(([b, n]) => console.log(`  ${b} (${BRAND_DOMAINS[b] || '?'}): ${n} parts`));
  process.exit(0);
}

if (todo.length === 0) {
  console.log('Nothing to do — all parts already have images.');
  process.exit(0);
}

// ── Helpers ────────────────────────────────────────────

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

// Jaccard similarity on word tokens — used to match part name to product title
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

// Extract image URL from raw HTML using multiple patterns
function extractImageFromHTML(html) {
  if (!html) return null;

  // 1. Shopify CDN image in <img> or <source> tags
  const shopifyCDN = html.match(/https:\/\/cdn\.shopify\.com\/s\/files\/[^"'\s]+\.(?:jpe?g|png|webp)/i);
  if (shopifyCDN) return cleanImgUrl(shopifyCDN[0]);

  // 2. og:image meta tag (both attribute orders)
  const og = html.match(/<meta[^>]+property=["']og:image["'][^>]+content=["']([^"']+)["']/i)
          || html.match(/<meta[^>]+content=["']([^"']+)["'][^>]+property=["']og:image["']/i);
  if (og?.[1]) return og[1];

  // 3. JSON-LD Product schema
  const jsonld = html.match(/"@type"\s*:\s*"Product"[\s\S]{0,500}?"image"\s*:\s*"([^"]+)"/);
  if (jsonld?.[1]) return jsonld[1];

  // 4. Any https image URL near "product" keyword
  const near = html.match(/product[^"'<>]{0,80}(https?:\/\/[^"'\s]+\.(?:jpe?g|png|webp))/i)
            || html.match(/(https?:\/\/[^"'\s]+\.(?:jpe?g|png|webp))[^"'<>]{0,80}product/i);
  if (near?.[1]) return near[1];

  return null;
}

// Strip Shopify size suffixes like _1024x1024 to get full-size image
function cleanImgUrl(url) {
  return url.replace(/_\d+x\d+(\.\w+)$/, '$1');
}

// ── Strategy 1: Shopify products.json ─────────────────

async function fetchShopifyCatalog(domain) {
  if (catalog[domain]) return catalog[domain]; // cached

  const products = [];
  let page = 1;
  while (true) {
    const data = await fetchJSON(`https://${domain}/products.json?limit=250&page=${page}`);
    if (!data?.products?.length) break;
    data.products.forEach(p => {
      const img = p.images?.[0]?.src;
      if (img) products.push({ title: p.title, image: cleanImgUrl(img) });
    });
    if (data.products.length < 250) break;
    page++;
    await delay(300);
  }

  if (products.length > 0) {
    catalog[domain] = products;
    writeFileSync(CATALOG_PATH, JSON.stringify(catalog, null, 2));
    console.log(`    Shopify catalog: ${products.length} products from ${domain}`);
  }
  return products;
}

// ── Strategy 2: HTML search fallback ──────────────────

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
  if (!domain) return null;

  // Strategy 1: Shopify catalog
  const shopify = await fetchShopifyCatalog(domain);
  if (shopify.length > 0) {
    const match = bestMatch(shopify, part.name);
    if (match) return match.image;
  }

  // Strategy 2: HTML search
  return await searchHTML(domain, part.name);
}

// ── Utilities ──────────────────────────────────────────

const delay = ms => new Promise(r => setTimeout(r, ms));

function saveCache() {
  writeFileSync(CACHE_PATH, JSON.stringify(cache, null, 2));
}

// ── Main ───────────────────────────────────────────────

let found = 0, failed = 0;

// Group by brand so we only fetch Shopify catalogs once per brand
const byBrand = {};
todo.forEach(p => (byBrand[p.brand] = [...(byBrand[p.brand] || []), p]));
const brands = Object.keys(byBrand);
console.log(`Brands to query: ${brands.join(', ')}\n`);

let idx = 0;
for (const brand of brands) {
  const parts = byBrand[brand];
  const domain = BRAND_DOMAINS[brand];
  console.log(`\n── ${brand} (${domain || 'no domain'}) — ${parts.length} parts`);

  if (!domain) {
    parts.forEach(p => { cache[p.id] = null; });
    saveCache();
    continue;
  }

  // Warm up Shopify catalog for this brand (shared across all its parts)
  await fetchShopifyCatalog(domain).catch(() => []);

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

// Write image URLs back into parts.json
let updated = 0;
data.parts.forEach(p => {
  if (cache[p.id]) { p.image_url = cache[p.id]; updated++; }
});
writeFileSync(PARTS_PATH, JSON.stringify(data, null, 2));

console.log(`\n────────────────────────────────────────────`);
console.log(`Found:   ${found}`);
console.log(`Failed:  ${failed}`);
console.log(`Updated: ${updated} parts in data/parts.json`);
console.log(`Brand catalogs cached in scripts/brand-catalog.json`);
console.log(`Re-run to retry any failed parts.`);
