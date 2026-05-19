# FPV Drone Builder

A web application where users configure custom FPV drones from real marketplace parts, with a live 3D visual that updates as they build.

---

## Table of Contents

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Core Features](#core-features)
4. [Architecture](#architecture)
5. [Data Model](#data-model)
6. [Implementation Phases](#implementation-phases)
7. [Folder Structure](#folder-structure)
8. [API Design](#api-design)
9. [Visual Renderer](#visual-renderer)
10. [Marketplace & Parts Catalog](#marketplace--parts-catalog)

---

## Overview

Users open a builder interface, browse a categorized parts catalog (frame, motors, ESC, flight controller, propellers, camera, VTX, battery, receiver), drop parts into their build, and watch a 3D drone model assemble in real time. Compatibility warnings fire when parts conflict. Completed builds can be saved, shared, and linked to purchase pages.

---

## Tech Stack

| Layer | Choice | Reason |
|---|---|---|
| Frontend framework | **Next.js 14 (App Router)** | SSR for catalog pages, RSC for performance |
| 3D rendering | **React Three Fiber + Three.js** | Declarative 3D in React, large ecosystem |
| 3D models | **GLTF/GLB assets** | Industry standard, small file size |
| UI components | **shadcn/ui + Tailwind CSS** | Accessible, unstyled primitives, fast iteration |
| State management | **Zustand** | Lightweight, no boilerplate for build state |
| Database | **PostgreSQL (Supabase)** | Relational schema for parts/builds, realtime optional |
| ORM | **Prisma** | Type-safe queries, easy migrations |
| Auth | **Supabase Auth** | OAuth (Google/GitHub) + email, free tier |
| File/image storage | **Supabase Storage** | Part images, user build screenshots |
| API | **Next.js Route Handlers** | Collocated, no separate server needed |
| Hosting | **Vercel** | Zero-config Next.js deployment |

---

## Core Features

### Phase 1 — MVP
- Parts catalog with categories, filters (size class, brand, weight, price)
- Slot-based build panel (each slot accepts one category)
- Live 3D drone viewer that updates on part selection
- Compatibility engine (motor KV vs battery voltage, frame motor mount size, prop size vs frame)
- Build summary: total weight, estimated thrust, price total
- Save build (authenticated) or share via link (anonymous)

### Phase 2 — Enhanced UX
- Part comparison side-by-side
- Recommended build presets (5" freestyle, 3" toothpick, micro whoop)
- Battery life estimator (mAh + amp draw)
- "Complete my build" suggestions when slots are empty
- Part search with instant results

### Phase 3 — Marketplace & Social
- Direct buy links (affiliate links to GetFPV, RaceDayQuads, etc.)
- Community builds feed (browse public builds, fork them)
- Build ratings and comments
- Price history and alerts
- Part review scores aggregated from external sources

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Next.js App                         │
│                                                         │
│  ┌─────────────────┐    ┌──────────────────────────┐   │
│  │  Catalog Pages  │    │     Builder Page          │   │
│  │  (SSR/RSC)      │    │  ┌────────┐ ┌─────────┐  │   │
│  │  /catalog       │    │  │ Parts  │ │  3D     │  │   │
│  │  /catalog/[id]  │    │  │ Panel  │ │ Viewer  │  │   │
│  └─────────────────┘    │  └────────┘ └─────────┘  │   │
│                         │     Zustand Build Store    │   │
│                         └──────────────────────────┘   │
│                                                         │
│  Route Handlers: /api/parts  /api/builds  /api/compat  │
└─────────────────┬───────────────────────────────────────┘
                  │
        ┌─────────▼──────────┐
        │   Supabase          │
        │  PostgreSQL  Auth   │
        │  Storage            │
        └────────────────────┘
```

---

## Data Model

### `part_categories`
```
id          uuid PK
name        text          -- "Frame", "Motor", "ESC", etc.
slot_key    text UNIQUE   -- "frame", "motor_fl", "esc", "fc", ...
sort_order  int
```

### `parts`
```
id              uuid PK
category_id     uuid FK → part_categories
name            text
brand           text
sku             text
image_url       text
price_usd       numeric
weight_g        numeric
in_stock        boolean
external_url    text      -- buy link
specs           jsonb     -- category-specific fields (see below)
created_at      timestamptz
```

**Specs JSONB shape by category**

| Category | Key fields |
|---|---|
| Frame | `size_mm`, `motor_mount_mm`, `weight_g`, `material` |
| Motor | `kv`, `stator_size`, `motor_mount_mm`, `max_voltage` |
| ESC | `amp_rating`, `input_voltage_s`, `protocol` (DSHOT300/600) |
| Flight Controller | `gyro`, `firmware` (Betaflight/INAV), `form_factor` |
| Propeller | `diameter_inch`, `pitch`, `blade_count`, `shaft_mm` |
| Camera | `sensor`, `fov_deg`, `resolution`, `weight_g` |
| VTX | `power_mw_max`, `bands`, `protocol` (Analog/DJI/HDZero) |
| Battery | `cell_count_s`, `capacity_mah`, `c_rating`, `connector` |
| Receiver | `protocol` (ELRS/FrSky/TBS), `frequency_mhz` |

### `builds`
```
id              uuid PK
user_id         uuid FK → auth.users (nullable for anonymous)
share_token     text UNIQUE
name            text
is_public       boolean DEFAULT false
parts           jsonb   -- { slot_key: part_id }
notes           text
created_at      timestamptz
updated_at      timestamptz
```

### `compatibility_rules`
```
id          uuid PK
rule_type   text   -- "require_match", "range_check", "incompatible"
slot_a      text
spec_a      text
operator    text   -- "==", "<=", ">="
slot_b      text
spec_b      text
message     text   -- shown to user on violation
```

---

## Implementation Phases

### Phase 1 — Foundation (Weeks 1–2)

**Goal:** Working builder with static parts data and basic 3D viewer.

- [ ] Scaffold Next.js 14 project with Tailwind, shadcn/ui, Prisma
- [ ] Set up Supabase project (Postgres + Auth + Storage)
- [ ] Seed parts catalog with ~20 real parts per category
- [ ] Build slot-based builder UI (left panel: slots, right panel: 3D)
- [ ] Implement Zustand build store (addPart, removePart, clearBuild)
- [ ] Integrate React Three Fiber; load a base drone GLTF model
- [ ] Wire part selection → 3D model swap for each component slot
- [ ] Display build summary (weight, price total)
- [ ] Save build to DB (authenticated) / share link (anonymous)

### Phase 2 — Catalog & Compatibility (Weeks 3–4)

**Goal:** Browsable catalog and smart compatibility checking.

- [ ] Catalog list page with filter/sort (category, price, weight, brand)
- [ ] Part detail page with full specs and buy link
- [ ] Compatibility engine: evaluate `compatibility_rules` against current build
- [ ] Show inline warnings in the slot panel when rules are violated
- [ ] Search (Postgres full-text or pg_trgm)
- [ ] Part image hosting in Supabase Storage

### Phase 3 — 3D Polish (Weeks 5–6)

**Goal:** Visually compelling drone assembly experience.

- [ ] Source or create per-category GLTF assets (frame variants, motor styles, etc.)
- [ ] Animate parts "snapping" into place on selection
- [ ] Camera orbit controls, zoom to selected part on click
- [ ] Frame size class drives the base model scale
- [ ] Color tinting: reflect user-selected color options per part
- [ ] Screenshot / export PNG of current build

### Phase 4 — Social & Marketplace (Weeks 7–8)

**Goal:** Community and purchase flow.

- [ ] Public builds feed with pagination
- [ ] Fork a build (copy to your account)
- [ ] Affiliate link tracking (UTM params on external buy links)
- [ ] Preset builds ("starter 5 inch", "micro racer")
- [ ] Part price sync job (scrape or API from suppliers)

---

## Folder Structure

```
fpv-drone-builder/
├── app/
│   ├── (marketing)/
│   │   └── page.tsx              # Landing page
│   ├── builder/
│   │   ├── page.tsx              # Main builder page
│   │   ├── BuilderLayout.tsx     # Left panel + 3D viewer split
│   │   ├── SlotPanel/
│   │   │   ├── SlotPanel.tsx
│   │   │   ├── SlotRow.tsx
│   │   │   └── PartPicker.tsx    # Popover/drawer to select a part
│   │   └── DroneViewer/
│   │       ├── DroneViewer.tsx   # R3F Canvas wrapper
│   │       ├── DroneModel.tsx    # Assembles GLTF parts
│   │       └── usePartModels.ts  # Loads GLTF assets by slot
│   ├── catalog/
│   │   ├── page.tsx              # Parts list (RSC, SSR)
│   │   └── [id]/
│   │       └── page.tsx          # Part detail
│   ├── builds/
│   │   ├── page.tsx              # Public builds feed
│   │   └── [shareToken]/
│   │       └── page.tsx          # Shared build view
│   └── api/
│       ├── parts/
│       │   └── route.ts          # GET /api/parts?category=&q=
│       ├── builds/
│       │   └── route.ts          # GET, POST /api/builds
│       └── compat/
│           └── route.ts          # POST /api/compat (validate build)
├── components/
│   ├── ui/                       # shadcn/ui primitives
│   ├── PartCard.tsx
│   ├── BuildSummary.tsx
│   └── CompatWarning.tsx
├── lib/
│   ├── store/
│   │   └── buildStore.ts         # Zustand store
│   ├── compat/
│   │   └── engine.ts             # Compatibility rule evaluator
│   ├── prisma.ts
│   └── supabase.ts
├── prisma/
│   ├── schema.prisma
│   └── seed.ts
├── public/
│   └── models/                   # GLTF drone part assets
│       ├── frame-5inch.glb
│       ├── motor-2306.glb
│       └── ...
└── types/
    ├── part.ts
    └── build.ts
```

---

## API Design

### `GET /api/parts`
Query params: `category`, `q` (search), `min_price`, `max_price`, `sort` (price|weight|name), `page`

Response:
```json
{
  "parts": [{ "id": "...", "name": "...", "brand": "...", "price_usd": 29.99, "specs": {} }],
  "total": 120,
  "page": 1
}
```

### `POST /api/builds`
Body: `{ name, parts: { frame: "uuid", motor_fl: "uuid", ... }, is_public }`
Response: `{ id, share_token }`

### `GET /api/builds/:shareToken`
Response: full build with hydrated part objects

### `POST /api/compat`
Body: `{ parts: { slot_key: part_id } }`
Response:
```json
{
  "valid": false,
  "violations": [
    { "slots": ["motor_fl", "frame"], "message": "Motor mount (16mm) doesn't fit frame (20mm)" }
  ]
}
```

---

## Visual Renderer

The 3D viewer is built with **React Three Fiber** inside a `<Canvas>` component.

**How it works:**

1. A base frame GLTF is always loaded first — it anchors the scale and motor mount positions.
2. Each slot (motor ×4, ESC, FC, camera, VTX) has a predefined attachment point (a named empty in the GLTF).
3. When a part is selected, its GLTF is loaded via `useGLTF` (with Suspense + `Drei`'s `<Preload>`), positioned at its attachment point, and scaled to match the frame class.
4. If no part is selected for a slot, a transparent placeholder mesh occupies that position.
5. Selecting a slot in the panel triggers `camera.lookAt` + zoom to that component.

**Key libraries:**
- `@react-three/fiber` — React renderer for Three.js
- `@react-three/drei` — helpers: `OrbitControls`, `useGLTF`, `Environment`, `ContactShadows`
- `three` — underlying 3D engine

**Asset pipeline:**
- Source real-world part shapes from free libraries (Sketchfab, GrabCAD) or commission low-poly originals
- Export as GLB, compress with `gltf-pipeline` or `draco`
- Host in `public/models/` (small) or Supabase Storage (larger)

---

## Marketplace & Parts Catalog

Initial parts data is seeded from:
- **GetFPV** — largest US FPV retailer (manual CSV export or public scrape)
- **RaceDayQuads** — popular motors and frames
- **Rotor Riot** — curated freestyle parts

Each part record stores `external_url` pointing to the retailer listing. Affiliate tags are appended at redirect time server-side so the token stays out of the DB.

A weekly cron job (Vercel Cron or Supabase Edge Function) re-fetches prices and stock status and updates the `parts` table.

---

## Getting Started (once scaffold is built)

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
# Fill in: DATABASE_URL, NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY

# Run migrations and seed
npx prisma migrate dev
npx prisma db seed

# Start dev server
npm run dev
```
