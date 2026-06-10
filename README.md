# FPV Drone Builder

A browser-native app for configuring custom FPV drones from a catalog of real parts. Select components across all 9 slots, see a live blueprint diagram update in real time, catch compatibility problems before you buy, and share your build with a link.

No frameworks. No build step. No install required.

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Running Locally](#running-locally)
4. [Architecture](#architecture)
5. [Data Model](#data-model)
6. [Folder Structure](#folder-structure)
7. [Blueprint Diagram](#blueprint-diagram)
8. [Parts Gallery](#parts-gallery)
9. [Compatibility Engine](#compatibility-engine)
10. [Scripts](#scripts)

---

## Features

- **2980 real parts** across 11 categories (frame, motor, ESC, FC, propeller, FPV camera, VTX, battery, receiver, GPS, antenna)
- **Live SVG blueprint** — top-down drone diagram updates in real time as you select parts; each component takes the part's actual color and shows the brand name, key spec, and a gallery shortcut icon
- **Parts gallery modal** — click the Gallery button or the camera icon on any blueprint component to see all selected parts as a visual card grid with product photos, specs, and retailer links
- **Compatibility checker** — 9 rules covering motor mount sizing, voltage limits, prop clearance, ESC current, digital video system pairing (DJI O3, Walksnail, HDZero) and cross-system mismatches; violations shown inline and highlighted amber on the diagram
- **Part catalog** — search, filter by brand / in-stock, sort by price/weight/name, view full specs, compare up to 4 parts side by side
- **5 preset builds** — 5" freestyle, 5" race, 3" toothpick, long-range 5", micro 3.5"
- **Saved builds** — multiple named builds in `localStorage`, load/delete anytime
- **Share link** — full build state encoded in URL hash, shareable and bookmark-able
- **Build stats** — total weight, estimated thrust-to-weight ratio, total price (PHP)

---

## Tech Stack

| Concern | Choice |
|---|---|
| Markup | HTML5 — `<dialog>`, semantic elements, SVG |
| Styling | Vanilla CSS — custom properties, Grid, Flexbox, transitions |
| Logic | Vanilla JS (ES Modules) — native `import/export`, no transpiler |
| Diagram | Hand-crafted SVG generated in JS — no canvas, no Three.js |
| Persistence | `localStorage` — save/restore builds client-side |
| Dev server | None required — `python3 -m http.server` or `npx serve .` |
| Hosting | Any static host — GitHub Pages, Netlify, Cloudflare Pages |

No npm install. No build step. No framework. Runs in Chrome 105+, Firefox 110+, Safari 16+.

---

## Running Locally

```bash
# Python (built into macOS/Linux)
python3 -m http.server 8080

# Node
npx serve .
```

Open `http://localhost:8080`. A real HTTP server is required (not `file://`) because ES module imports are subject to CORS.

---

## Architecture

```
index.html
│
├── css/
│   ├── reset.css          ← base reset + CSS custom properties
│   ├── layout.css         ← three-column split: left panel | blueprint | right panel
│   ├── catalog.css        ← part cards, filters, search, comparison modal
│   ├── blueprint.css      ← SVG diagram states (empty / filled / active / violation)
│   ├── components.css     ← modals, buttons, toasts, gallery cards
│   └── viewer.css         ← mobile drawer animations
│
└── js/
    ├── main.js            ← app entry — wires all modules, mobile drawer
    ├── store.js           ← plain-object state + pub/sub event bus
    ├── builder.js         ← slot panel, preset loader, active-slot management
    ├── catalog.js         ← part cards, search/filter/sort, detail view, brand logos
    ├── blueprint.js       ← SVG diagram — draws and updates all 9 components
    ├── gallery.js         ← parts gallery modal (card grid with product photos + specs)
    ├── compat.js          ← compatibility rule evaluator
    ├── summary.js         ← weight / price / TWR calc + violation badge count
    ├── compare.js         ← side-by-side part comparison modal
    ├── saves.js           ← multiple saved builds in localStorage
    ├── stepper.js         ← guided build flow (step through slots in order)
    ├── share.js           ← encode/decode build state in URL hash
    └── export.js          ← build card PNG generator
```

### State flow

```
User clicks part card
        │
        ▼
store.dispatch('SELECT_PART', { slot, partId })
        │
        ├──► builder.js   updates slot panel, triggers compat.evaluate()
        ├──► blueprint.js redraws component with part color + name + spec
        ├──► gallery.js   updates card grid if modal is open
        └──► summary.js   recalculates weight / price / TWR
```

All inter-module communication goes through the store's pub/sub bus (`on` / `dispatch`). Modules never import each other directly — this keeps the dependency graph flat.

---

## Data Model

Everything lives in `data/parts.json`. No database, no server.

### Top-level shape

```json
{
  "categories": [...],
  "parts": [...],
  "compatibility_rules": [...],
  "presets": {}
}
```

### Part object

```json
{
  "id": "iflight-nazgul-evoque-f5",
  "category": "frame",
  "name": "iFlight Nazgul Evoque F5 V2",
  "brand": "iFlight",
  "price_php": 3800,
  "weight_g": 68,
  "color": "#1a1a1a",
  "buy_url": "https://iflight.com/...",
  "image_url": "https://cdn.shopify.com/...",
  "in_stock": true,
  "specs": {
    "size_mm": 225,
    "motor_mount_mm": 30,
    "prop_clearance_inch": 5,
    "material": "carbon fiber",
    "stack_mount_mm": 30
  }
}
```

`image_url` is populated by the GitHub Actions workflow (see [Scripts](#scripts)). The gallery shows a color-matched SVG illustration when the field is absent.

### Spec fields by category

| Category | Key spec fields |
|---|---|
| Frame | `size_mm`, `motor_mount_mm`, `prop_clearance_inch`, `stack_mount_mm`, `material` |
| Motor | `kv`, `stator_size`, `motor_mount_mm`, `max_voltage_s` |
| ESC | `amp_rating`, `input_voltage_s`, `protocol`, `form_factor_mm` |
| Flight Controller | `gyro`, `firmware`, `form_factor_mm`, `stack_mount_mm` |
| Propeller | `diameter_inch`, `pitch`, `blade_count`, `shaft_mm` |
| Camera | `sensor`, `fov_deg`, `format`, `video_system` |
| VTX | `power_mw_max`, `protocol`, `video_system` |
| Battery | `cell_count_s`, `capacity_mah`, `c_rating`, `connector` |
| Receiver | `protocol`, `frequency_mhz` |

### Compatibility rule object

Two rule types are supported:

```json
{ "type": "spec_match", "slot_a": "frame", "spec_a": "motor_mount_mm",
  "slot_b": "motor", "spec_b": "motor_mount_mm",
  "message": "Motor mount ({b}mm) doesn't match frame ({a}mm)" }

{ "type": "range", "operator": ">=",
  "slot_a": "motor", "spec_a": "max_voltage_s",
  "slot_b": "battery", "spec_b": "cell_count_s",
  "message": "Motor max voltage ({a}S) is less than battery ({b}S)" }
```

---

## Folder Structure

```
fpv-drone-builder/
├── index.html
├── package.json
├── css/
│   ├── reset.css
│   ├── layout.css
│   ├── catalog.css
│   ├── blueprint.css
│   ├── components.css
│   └── viewer.css
├── js/
│   ├── main.js
│   ├── store.js
│   ├── builder.js
│   ├── catalog.js
│   ├── blueprint.js
│   ├── gallery.js
│   ├── compat.js
│   ├── summary.js
│   ├── compare.js
│   ├── saves.js
│   ├── stepper.js
│   ├── share.js
│   └── export.js
├── data/
│   └── parts.json
├── scripts/
│   └── fetch-product-images.js
└── .github/
    └── workflows/
        └── fetch-images.yml
```

---

## Blueprint Diagram

The SVG diagram in `js/blueprint.js` is fully dynamic — no static SVG file. The entire diagram is built programmatically on page load via `document.createElementNS`.

**Per-part color** is applied through CSS custom properties set on each component's `<g>` element:

```js
el.style.setProperty('--pc', part.color);                 // stroke / accent
el.style.setProperty('--pf', hexAlpha(part.color, 0.18)); // fill
```

CSS uses `var(--pc)` and `var(--pf)` for all strokes and fills. Violation state overrides both via `.bp-group.bp-violation`.

**Component states:**

| Class | Appearance |
|---|---|
| `.bp-empty` | Light gray outlines |
| `.bp-filled` | Part's color via `--pc` / `--pf`, drop shadow |
| `.bp-active` | Brighter stroke, glow filter, bolder labels |
| `.bp-violation` | Amber override — ignores `--pc` / `--pf` |

**Dynamic features:**
- Propeller blade count and sweep radius scale from `specs.diameter_inch` and `specs.blade_count`
- Battery cell dividers match `specs.cell_count_s`
- Brand favicon loads from Google's favicon service per brand domain
- Camera icon pill appears on each filled component — click it to open the gallery focused on that slot

---

## Parts Gallery

The gallery modal (`js/gallery.js`) shows all 9 build slots as cards. Each filled card displays:

- Product photo (`image_url`) filling the card header, or a color-matched SVG illustration if no photo is available
- Brand favicon (top-right corner)
- "View product ↗" overlay on hover — links directly to the retailer
- Part name, brand, key spec, price, and weight

**Open the gallery by:**
- Clicking the **Gallery** button in the blueprint toolbar (shows a count badge of selected parts)
- Clicking the **📷 icon** on any selected component in the blueprint diagram

---

## Compatibility Engine

`js/compat.js` evaluates rules from `data/parts.json` against the current build on every change. Rules are only evaluated when both referenced slots have a part selected.

| Rule | Type | What it checks |
|---|---|---|
| `motor-mount-match` | spec_match | Frame and motor mounting hole size |
| `prop-frame-clearance` | range | Prop diameter fits inside frame |
| `battery-voltage-motor` | range | Motor max voltage ≥ battery cell count |
| `esc-current-motor` | range | ESC amp rating ≥ motor current draw |
| `esc-battery-voltage` | range | ESC input voltage ≥ battery cell count |
| `fc-esc-stack-size` | spec_match | FC and ESC stack mounting pattern |
| `prop-motor-shaft` | spec_match | Prop shaft hole matches motor shaft |
| `camera-vtx-format` | spec_match | Camera and VTX both analog or both digital |
| `camera-vtx-digital-system` | spec_match | Digital camera and VTX use the same ecosystem |

---

## Scripts

### `scripts/fetch-product-images.js`

Populates `image_url` for all 369 parts by querying brand official sites and major FPV retailers. No API keys. No npm install. Requires Node 18+.

**Strategy per part (tried in order):**
1. **Brand Shopify predictive search** — `/search/suggest.json` on the brand's own site; fastest and most accurate for Shopify brands (iFlight, BetaFPV, GEPRC, Holybro…)
2. **Brand Shopify catalog match** — `/products.json` full catalog with Jaccard fuzzy matching
3. **FPV retailer search** — searches GetFPV and RaceDayQuads, which stock virtually every brand including non-Shopify ones (Gemfan, HQProp, RunCam, Foxeer, Matek, T-Motor, CNHL…)
4. **HTML search fallback** — fetches `/search?q=<name>` and extracts a product image from JSON-LD schema or Shopify CDN URLs

All strategies filter out logo, banner, and social images via URL keyword matching. Parts whose `image_url` looks like a logo are automatically re-fetched on the next run.

```bash
node scripts/fetch-product-images.js            # fetch missing + fix logos
node scripts/fetch-product-images.js --dry-run  # list brands + part counts, no fetches
node scripts/fetch-product-images.js --force    # re-fetch everything
```

### GitHub Actions workflow

`.github/workflows/fetch-images.yml` runs the script in a GitHub Actions environment (full internet access) and commits the updated `data/parts.json` back to the repo.

**Trigger:** Actions tab → **Fetch Product Images** → **Run workflow**. Check "force" to re-fetch all parts regardless of cache.
