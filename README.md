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
| 3D geometry | **Procedural Three.js** | All parts built from Three.js primitives — no `.glb` files required |
| Persistence | **`localStorage`** | Save and restore builds client-side |
| Dev server | **none required** | Open `index.html` directly, or use `npx serve .` |
| Hosting | **any static host** | GitHub Pages, Netlify, Cloudflare Pages |

No npm install required. No build step. No framework. All features use APIs available natively in modern browsers (Chrome 105+, Firefox 110+, Safari 16+).

---

## Core Features

### Phase 1 — MVP
- Parts catalog JSON file with real parts per category
- Slot-based builder UI: each category has exactly one active slot
- Live 3D drone viewer powered by Three.js — renders procedural part geometry on selection
- Compatibility checker: evaluates rules against the current build, shows inline warnings
- Build summary panel: total weight, estimated thrust-to-weight, total price
- Save build to `localStorage`; share via URL hash (base64-encoded build state)

### Phase 2 — Enhanced UX
- Part search with instant client-side filtering
- Filter pills: in-stock toggle; sort by price, weight, or name
- Part detail panel (slide-in view): full specs, buy link
- Part comparison: pin up to 3 parts, see specs side by side in a modal table
- Preset builds (5" freestyle, 5" race, 3" toothpick): populate all slots from one click

### Phase 3 — 3D Polish
- Per-part procedural geometry with accurate visual detail per category
- Pop-in animation on part select (scale 0 → 1 with cubic easing)
- Emissive highlight on the active slot's model (cyan tint)
- Camera auto-orbit to selected component on slot click
- Frame size drives overall model scale across all attached parts
- Export PNG: `renderer.domElement.toDataURL()` → instant download

### Phase 4 — Share & Extras
- Build card exporter: Canvas 2D overlay (1280×720) with 3D snapshot + part list + stats
- Multiple saved builds in `localStorage`, keyed by build name with timestamps
- Affiliate UTM params appended to buy links at click time

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
    ├── summary.js                 ← weight / price / TWR calc + violation badges
    ├── compare.js                 ← part comparison modal (up to 3 parts)
    ├── saves.js                   ← multiple saved builds in localStorage
    ├── export.js                  ← build card PNG generator (Canvas 2D)
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
      ├──► viewer.js   rebuilds procedural mesh for that slot
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
  "compatibility_rules": [...],
  "presets": {}
}
```

### Category object

```json
{
  "id": "frame",
  "label": "Frame",
  "slot_count": 1,
  "required": true,
  "icon": "🛸"
}
```

### Part object

```json
{
  "id": "iflight-titan-dc5",
  "category": "frame",
  "name": "iFlight Titan DC5 V3",
  "brand": "iFlight",
  "price_usd": 52.99,
  "weight_g": 68,
  "color": "#1a1a1a",
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

### Phase 1 — Foundation ✅

- [x] `index.html` shell: split layout, import map, slot panel, canvas placeholder
- [x] `css/` base styles: CSS custom properties (colors, spacing, radius), layout grid
- [x] `data/parts.json`: ~10 real parts per category with full specs
- [x] `js/store.js`: minimal pub/sub state store (no external lib)
- [x] `js/catalog.js`: render part cards from JSON, filter by category
- [x] `js/builder.js`: slot rows, open part picker, select a part, clear a slot
- [x] `js/viewer.js`: Three.js scene with OrbitControls, ambient + directional lights
- [x] Procedural 3D part geometry per category — no `.glb` files required
- [x] `js/compat.js`: evaluate rules, return violations array
- [x] Compatibility violation badges inline in slot panel
- [x] Build summary: weight, price, thrust-to-weight estimate
- [x] `js/share.js`: encode build → URL hash; decode on load

### Phase 2 — Catalog & Filtering ✅

- [x] Live search input (filters `parts.json` client-side as user types)
- [x] Filter pills: in-stock toggle
- [x] Sort: price ↑↓, weight ↑↓, name A–Z
- [x] Part detail view: full specs table, add-to-build button, buy link with UTM
- [x] Part comparison: pin up to 3 parts, specs highlighted side by side in modal
- [x] Preset builds: populate all slots from a preset JSON object

### Phase 3 — 3D Polish ✅

- [x] Procedural per-category geometry (frame, motors, ESC, FC, props, camera, VTX, battery, receiver)
- [x] Pop-in animation on part select (scale 0 → 1 with cubic easing)
- [x] Emissive highlight on active slot's model (cyan tint)
- [x] Camera auto-lerp to selected component on slot click
- [x] Frame size drives overall model scale for all attached parts
- [x] Propeller spin animation when motor is selected
- [x] Export PNG: `renderer.domElement.toDataURL()` → download via screenshot button

### Phase 4 — Share & Extras ✅ / 🔲

- [x] Build card generator: Canvas 2D overlay (1280×720) with 3D snapshot + part list + stats
- [x] Multiple saved builds (`localStorage`, keyed by build name with timestamps, load/delete)
- [x] Affiliate UTM param injection on buy links at click time
- [ ] Print/PDF-friendly build summary view

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
│   ├── catalog.js           ← part cards, filters, search, detail view
│   ├── builder.js           ← slot panel, preset loader
│   ├── viewer.js            ← Three.js scene, procedural part meshes
│   ├── compat.js            ← rule evaluator
│   ├── summary.js           ← weight / price / TWR calc + violation badges
│   ├── compare.js           ← part comparison modal (up to 3 parts)
│   ├── saves.js             ← multiple saved builds in localStorage
│   ├── export.js            ← build card PNG generator (Canvas 2D)
│   └── share.js             ← URL hash encode/decode
└── data/
    └── parts.json           ← all parts + categories + compat rules + presets
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
```

**How part rendering works:**

All parts are built from Three.js primitives (`BoxGeometry`, `CylinderGeometry`, `ExtrudeGeometry`, etc.) — no external `.glb` assets are required. Each part category has a dedicated mesh builder:

| Function | Output |
|---|---|
| `addFrameMesh` | Center plate, top plate, 4 arms, standoffs, motor-mount rings |
| `addMotorMeshes` | 4× motor groups (stator, bell, cap, shaft, screws) at arm endpoints |
| `addPropMeshes` | 4× prop groups (tapered extruded blades, hub) with live spin animation |
| `addESCMesh` | PCB, corner MOSFETs, capacitor |
| `addFCMesh` | PCB, gyro chip, USB port, emissive LEDs |
| `addCameraMesh` | Body, lens barrel, glass disc, reflection ring |
| `addVTXMesh` | PCB, heatsink fins, antenna wire + mushroom tip, status LED |
| `addBatteryMesh` | Cell-sized body, label strip, XT60 plug, cell separation lines |
| `addReceiverMesh` | PCB, RF chip, dipole antennas (UHF or 2.4 GHz variant) |

**Attachment points** are hardcoded `THREE.Vector3` offsets in the `ATTACH` map. When a slot is active, `highlightSlot()` adds a cyan emissive tint to that part's mesh group. On slot click, `startCamAnim()` smoothly lerps the camera to a preset position focused on that component.

---

## Marketplace & Parts Catalog

`data/parts.json` is seeded manually from:
- **GetFPV** product pages
- **RaceDayQuads** — motors and frames
- **Rotor Riot** — curated freestyle parts

Each part has a `buy_url` field. Affiliate tags (`?ref=fpvbuilder&utm_source=fpvbuilder&utm_medium=referral`) are appended in `js/catalog.js` at render time so they stay out of the data file.

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

> Note: Three.js requires a real HTTP server (not `file://`) due to CORS restrictions on ES module imports.
