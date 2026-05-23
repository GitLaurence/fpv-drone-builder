#!/usr/bin/env node
/**
 * Fetch product images for all parts in data/parts.json.
 *
 * Uses Bing Image Search (no API key needed) via a headless Playwright browser.
 * Results are cached to scripts/image-cache.json so the script is safe to
 * re-run — it skips parts that already have an image_url or a cached result.
 *
 * Usage:
 *   node scripts/fetch-product-images.js            # fetch all missing images
 *   node scripts/fetch-product-images.js --dry-run  # show queries, no writes
 *   node scripts/fetch-product-images.js --force    # re-fetch even if cached
 *
 * Requirements:
 *   npm install playwright   (or: npx playwright install chromium)
 */

import { chromium } from 'playwright';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';

const __dir     = dirname(fileURLToPath(import.meta.url));
const PARTS_PATH = resolve(__dir, '../data/parts.json');
const CACHE_PATH = resolve(__dir, 'image-cache.json');

const DRY_RUN = process.argv.includes('--dry-run');
const FORCE   = process.argv.includes('--force');
const DELAY_MS = 1200; // be polite to Bing

// ── Load data ──────────────────────────────────────────
const data  = JSON.parse(readFileSync(PARTS_PATH, 'utf8'));
const cache = existsSync(CACHE_PATH)
  ? JSON.parse(readFileSync(CACHE_PATH, 'utf8'))
  : {};

const parts = data.parts.filter(p => FORCE || (!p.image_url && !cache[p.id]));
console.log(`Parts to fetch: ${parts.length} of ${data.parts.length} total`);

if (DRY_RUN) {
  parts.forEach(p => console.log(`  [dry] ${p.id}: "${p.brand} ${p.name}"`));
  process.exit(0);
}

if (parts.length === 0) {
  console.log('Nothing to do — all parts already have images.');
  process.exit(0);
}

// ── Bing Image Search ──────────────────────────────────
async function searchBing(page, query) {
  const url = `https://www.bing.com/images/search?q=${encodeURIComponent(query)}&form=HDRSC2&first=1`;
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });

  const imgUrl = await page.evaluate(() => {
    // Bing encodes the media URL in JSON inside each result anchor's `m` attribute
    const anchors = document.querySelectorAll('a.iusc');
    for (const a of anchors) {
      try {
        const m = JSON.parse(a.getAttribute('m') || '{}');
        if (m.murl && /\.(jpe?g|png|webp)/i.test(m.murl)) return m.murl;
      } catch {}
    }
    // Fallback: grab first <img> inside results
    const img = document.querySelector('.iuscp img, .mimg');
    return img?.src || img?.getAttribute('data-src') || null;
  });

  return imgUrl || null;
}

// ── Google Images fallback ─────────────────────────────
async function searchGoogle(page, query) {
  const url = `https://www.google.com/search?tbm=isch&q=${encodeURIComponent(query)}`;
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });

  return await page.evaluate(() => {
    const imgs = document.querySelectorAll('img[data-src], img[src]');
    for (const img of imgs) {
      const src = img.getAttribute('data-src') || img.src;
      if (src && src.startsWith('http') && !src.includes('google.com') &&
          /\.(jpe?g|png|webp)/i.test(src)) {
        return src;
      }
    }
    return null;
  });
}

// ── Build search query ─────────────────────────────────
function buildQuery(part) {
  // Trim long model names to avoid over-specific queries
  const name = part.name.replace(/\s+v\d+(\.\d+)?$/i, '').trim();
  return `${part.brand} ${name} fpv product`;
}

// ── Main ───────────────────────────────────────────────
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page    = await browser.newPage();

  // Look like a real browser
  await page.setExtraHTTPHeaders({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  });

  let found = 0, failed = 0;

  for (let i = 0; i < parts.length; i++) {
    const part  = parts[i];
    const query = buildQuery(part);
    process.stdout.write(`[${i + 1}/${parts.length}] ${part.id} ... `);

    let url = null;
    try {
      url = await searchBing(page, query);
      if (!url) url = await searchGoogle(page, query);
    } catch (e) {
      process.stdout.write(`ERROR: ${e.message.slice(0, 60)}\n`);
    }

    if (url) {
      cache[part.id] = url;
      process.stdout.write(`✓ ${url.slice(0, 80)}\n`);
      found++;
    } else {
      cache[part.id] = null; // mark as attempted
      process.stdout.write(`✗ not found\n`);
      failed++;
    }

    // Save cache after every part so progress isn't lost on interrupt
    writeFileSync(CACHE_PATH, JSON.stringify(cache, null, 2));

    if (i < parts.length - 1) {
      await new Promise(r => setTimeout(r, DELAY_MS));
    }
  }

  await browser.close();

  // ── Write results back into parts.json ────────────────
  let updated = 0;
  data.parts.forEach(p => {
    if (cache[p.id]) {
      p.image_url = cache[p.id];
      updated++;
    }
  });

  writeFileSync(PARTS_PATH, JSON.stringify(data, null, 2));
  console.log(`\nDone. Found: ${found}, Failed: ${failed}, Updated parts.json: ${updated} parts.`);
  console.log(`Cache saved to ${CACHE_PATH} — re-run to retry failed parts.`);
})();
