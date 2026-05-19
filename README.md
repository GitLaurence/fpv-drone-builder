# FPV Drone Builder

A browser-native app where users configure custom FPV drones from real marketplace parts, with a live 3D visual that updates as they build. Built entirely with modern HTML, CSS, and JavaScript — no frameworks, no build step.

---

## Table of Contents

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Core Features](#core-features)
4. [Architecture](#architecture)
5. [Data Model](#data-model)
6. [Implementation Phases](#implementation-phases)
7. [Folder Structure](#folder-structure)
8. [Visual Renderer](#visual-renderer)
9. [Marketplace & Parts Catalog](#marketplace--parts-catalog)

---

## Overview

Users open a single-page builder, browse a categorized parts catalog, select parts for each slot (frame, motors, ESC, flight controller, propellers, camera, VTX, battery, receiver), and watch a 3D drone assemble in real time inside a Three.js canvas. Compatibility warnings fire when parts conflict. Finished builds are saved to `localStorage` and shareable via a URL hash.

---

## Tech Stack

| Concern | Choice | Notes |
|---|---|---|
| Markup | **HTML5** | Semantic elements, `<dialog>`, `<details>`, `<template>` |
| Styling | **Modern CSS** | Custom properties, Grid, Flexbox, `@layer`, `@container`, transitions |
| Logic | **Vanilla JS (ES Modules)** | Native `import/export`, no transpiler |
| 3D rendering | **Three.js** (ESM build) | Loaded via import map, no bundler needed |
| GLTF loading | **Three.js GLTFLoader** | Loads `.glb` part models |
| Persistence | **`localStorage`** | Save and restore builds client-side |
| Dev server | **none required** | Open `index.html` directly, or use `npx serve .` |
| Hosting | **any static host** | GitHub Pages, Netlify, Cloudflare Pages |

No npm install required. No build step. No framework. All features use APIs available natively in modern browsers (Chrome 105+, Firefox 110+, Safari 16+).

---

## Core Features

### Phase 1 — MVP
- Parts catalog JSON file with real parts per category
- Slot-based builder UI: each category has exactly one active slot
- Live 3D drone viewer powered by Three.js — swaps part models on selection
- Compatibility checker: evaluates rules against the current build, shows inline warnings
- Build summary panel: total weight, estimated thrust-to-weight, total price
- Save build to `localStorage`; share via URL hash (base64-encoded build state)

### Phase 2 — Enhanced UX
- Part search with instant client-side filtering
- Part comparison drawer (select up to 3, see specs side by side)
- Recommended presets (5" freestyle, 3" toothpick, micro whoop)
- Battery life estimator based on capacity + estimated amp draw
- "Suggest missing parts" when slots are empty

### Phase 3 — Marketplace & Social
- Direct buy links (affiliate UTM links to GetFPV, RaceDayQuads)
- Export build as PNG (Three.js renderer snapshot)
- Export build as shareable card (HTML Canvas → PNG)
- Community builds via a lightweight JSON API or static JSON gallery

---

## Architecture

Everything runs in the browser. There is no server-side code.

```
index.html
│
├── <script type="importmap">      ← maps "three" to ESM CDN URL
│
├── css/
│   ├── reset.css
│   ├── layout.css                 ← grid split: catalog panel | 3D viewer
│   ├── catalog.css                ← part cards, slot rows, filters
│   ├── viewer.css                 ← canvas wrapper, HUD overlay
│   └── components.css             ← dialogs, tooltips, badges
│
└── js/
    ├── main.js                    ← app entry point, wires everything together
    ├── store.js                   ← plain-object state + pub/sub event bus
    ├── catalog.js                 ← loads parts.json, renders part cards
    ├── builder.js                 ← slot panel logic, compatibility checks
    ├── viewer.js                  ← Three.js scene, camera, lighting, part swap
    ├── compat.js                  ← rule evaluator (reads rules from parts.json)
    └── share.js                   ← encode/decode build state in URL hash
```

### State flow

```
User clicks part
      │
      ▼
store.dispatch('SELECT_PART', { slot, partId })
      │
      ├──► builder.js  re-renders slot panel, triggers compat check
      ├──► viewer.js   swaps GLTF model for that slot
      └──► summary.js  recalculates weight / price / TWR
```

---

## Data Model

All data lives in `data/parts.json`. No database. No server.

### Top-level shape

```json
{
  "categories": [...],
  "parts": [...],
  "compatibility_rules": [...]
}
```

### Category object

```json
{
  "id": "frame",
  "label": "Frame",
  "slot_count": 1,
  "required": true,
  "icon": "icons/frame.svg"
}
```

### Part object

```json
{
  "id": "iflight-titan-dc5",
  "category": "frame",
  "name": "iFlight Titan DC5 V2",
  "brand": "iFlight",
  "price_usd": 49.99,
  "weight_g": 68,
  "image": "images/parts/iflight-titan-dc5.webp",
  "buy_url": "https://www.getfpv.com/...",
  "in_stock": true,
  "specs": {
    "size_mm": 215,
    "motor_mount_mm": 30,
    "prop_clearance_inch": 5,
    "material": "carbon fiber",
    "stack_mount_mm": 30
  }
}
```

**Specs shape by category:**

| Category | Key spec fields |
|---|---|
| Frame | `size_mm`, `motor_mount_mm`, `prop_clearance_inch`, `stack_mount_mm` |
| Motor | `kv`, `stator_size`, `motor_mount_mm`, `max_voltage_s`, `weight_g` |
| ESC | `amp_rating`, `input_voltage_s`, `protocol`, `form_factor_mm` |
| Flight Controller | `gyro`, `firmware`, `form_factor_mm`, `stack_mount_mm` |
| Propeller | `diameter_inch`, `pitch`, `blade_count`, `shaft_mm` |
| Camera | `sensor`, `fov_deg`, `format`, `weight_g` |
| VTX | `power_mw_max`, `protocol`, `connector` |
| Battery | `cell_count_s`, `capacity_mah`, `c_rating`, `connector`, `weight_g` |
| Receiver | `protocol`, `frequency_mhz`, `weight_g` |

### Compatibility rule object

```json
{
  "id": "motor-mount-match",
  "type": "spec_match",
  "slot_a": "frame",
  "spec_a": "motor_mount_mm",
  "slot_b": "motor",
  "spec_b": "motor_mount_mm",
  "message": "Motor mount ({b}mm) doesn't match frame ({a}mm)"
},
{
  "id": "battery-voltage-range",
  "type": "range",
  "slot_a": "motor",
  "spec_a": "max_voltage_s",
  "operator": ">=",
  "slot_b": "battery",
  "spec_b": "cell_count_s",
  "message": "Motor max voltage ({a}S) is less than battery ({b}S)"
}
```

---

## Implementation Phases

### Phase 1 — Foundation (Weeks 1–2)

- [ ] `index.html` shell: split layout, import map, slot panel, canvas placeholder
- [ ] `css/` base styles: CSS custom properties (colors, spacing, radius), layout grid
- [ ] `data/parts.json`: seed ~10 real parts per category with full specs
- [ ] `js/store.js`: minimal pub/sub state store (no external lib)
- [ ] `js/catalog.js`: render part cards from JSON, filter by category
- [ ] `js/builder.js`: slot rows, open part picker dialog, select a part
- [ ] `js/viewer.js`: Three.js scene with OrbitControls, ambient + directional lights
- [ ] Load a base drone GLTF; swap per-slot GLTF on part select
- [ ] `js/compat.js`: evaluate rules, return violations array
- [ ] Display compatibility badges inline in slot panel
- [ ] Build summary: weight, price, basic thrust estimate
- [ ] `js/share.js`: encode build → URL hash; decode on load

### Phase 2 — Catalog & Filtering (Weeks 3–4)

- [ ] Live search input (filters `parts.json` client-side as user types)
- [ ] Filter pills: brand, price range, in-stock toggle
- [ ] Sort: price ↑↓, weight ↑↓, name A–Z
- [ ] Part detail panel (slide-in drawer): full specs, buy link, image gallery
- [ ] Part comparison: pin up to 3 parts, see specs in a table
- [ ] Preset builds: populate all slots from a preset JSON object

### Phase 3 — 3D Polish (Weeks 5–6)

- [ ] Per-category GLTF assets (source from Sketchfab / GrabCAD, optimize with `gltf-transform`)
- [ ] Animate part snap-in on select (scale from 0 → 1 with easing)
- [ ] Highlight selected slot's model in the viewer (emissive tint)
- [ ] Camera auto-orbit to selected component on slot click
- [ ] Frame size class drives overall model scale
- [ ] Export PNG: `renderer.domElement.toDataURL()` → download link

### Phase 4 — Share & Extras (Weeks 7–8)

- [ ] Build card generator: Canvas 2D overlay with part list + 3D screenshot
- [ ] Multiple saved builds (localStorage, keyed by build ID)
- [ ] Print/PDF-friendly build summary view
- [ ] Affiliate UTM param injection on buy links at click time

---

## Folder Structure

```
fpv-drone-builder/
├── index.html               ← single HTML file, import map, app shell
├── css/
│   ├── reset.css
│   ├── layout.css
│   ├── catalog.css
│   ├── viewer.css
│   └── components.css
├── js/
│   ├── main.js              ← entry: imports all modules, init()
│   ├── store.js             ← state + event bus
│   ├── catalog.js           ← part cards, filters, search
│   ├── builder.js           ← slot panel, part picker dialog
│   ├── viewer.js            ← Three.js scene
│   ├── compat.js            ← rule evaluator
│   ├── summary.js           ← weight / price / TWR calc
│   └── share.js             ← URL hash encode/decode
├── data/
│   └── parts.json           ← all parts + categories + compat rules
├── models/
│   ├── frame-5inch.glb
│   ├── motor-2306.glb
│   ├── esc-4in1.glb
│   ├── fc.glb
│   ├── camera.glb
│   └── ...
└── images/
    ├── parts/               ← part product photos (.webp)
    └── icons/               ← category SVG icons
```

---

## Visual Renderer

The 3D viewer lives in `js/viewer.js` and uses Three.js loaded as an ES module via an import map — no bundler needed.

```html
<!-- in index.html -->
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.164.1/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.164.1/examples/jsm/"
  }
}
</script>
```

```js
// js/viewer.js
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
```

**How part swapping works:**

1. The scene keeps a `Map<slotKey, THREE.Object3D>` of currently loaded part meshes.
2. On `SELECT_PART` event: remove the old mesh, load the new part's `.glb`, position it at the slot's attachment point, add to scene.
3. Attachment points are named empties baked into the frame model (e.g. `motor_fl`, `motor_fr`, `motor_rl`, `motor_rr`, `stack`, `camera_mount`).
4. If a slot is cleared, a wireframe placeholder sphere occupies the attachment point.

---

## Marketplace & Parts Catalog

`data/parts.json` is seeded manually from:
- **GetFPV** product pages (copy specs by hand or from their CSV export)
- **RaceDayQuads** — motors and frames
- **Rotor Riot** — curated freestyle parts

Each part has a `buy_url` field. Affiliate tags (`?ref=fpvbuilder`) are appended in `js/share.js` at click time so they stay out of the data file.

To update prices: edit `data/parts.json` directly, or write a small Node script (`scripts/sync-prices.js`) that fetches from supplier APIs and rewrites the file.

---

## Running Locally

No install required. Just serve the folder as static files:

```bash
# Option 1: Python (built into macOS/Linux)
python3 -m http.server 8080

# Option 2: Node
npx serve .

# Option 3: VS Code Live Server extension
# Right-click index.html → "Open with Live Server"
```

Then open `http://localhost:8080` in a modern browser.

> Note: Three.js GLTF loading requires a real HTTP server (not `file://`) due to CORS.
