import { on, getState, getPartById, dispatch } from './store.js';

const NS  = 'http://www.w3.org/2000/svg';
const VW  = 500;
const VH  = 500;
const CX  = 250;  // drone center x
const CY  = 252;  // drone center y (slightly below mid for camera clearance)

const MOTOR_POS = [
  { x: 142, y: 142 }, // FL
  { x: 358, y: 142 }, // FR
  { x: 142, y: 358 }, // RL
  { x: 358, y: 358 }, // RR
];
const MOTOR_R  = 18;
const PROP_R   = 52;
const PLATE_HW = 36; // half-width of center plate

let _svg    = null;
let _els    = {};   // named element handles for state updates
let _active = null;

// ── Public API ───────────────────────────────────────

export function init() {
  const wrap = document.getElementById('blueprint-wrap');
  if (!wrap) return;

  _svg = _el('svg', {
    viewBox: `0 0 ${VW} ${VH}`,
    class: 'blueprint-svg',
    role: 'img',
    'aria-label': 'FPV drone component blueprint — top view',
  });
  wrap.appendChild(_svg);

  _buildStatic();
  _buildComponents();
  _refresh();

  on('build:changed', () => _refresh());
  on('slot:active',   ({ slot }) => { _active = slot; _refresh(); });
}

// ── Static elements (bg, grid, labels) ──────────────

function _buildStatic() {
  // Defs
  const defs = _el('defs');

  // Glow filter
  const glow = _el('filter', { id: 'bp-glow', x: '-60%', y: '-60%', width: '220%', height: '220%' });
  glow.appendChild(_el('feGaussianBlur', { in: 'SourceGraphic', stdDeviation: '5', result: 'blur' }));
  const merge = _el('feMerge');
  merge.appendChild(_el('feMergeNode', { in: 'blur' }));
  merge.appendChild(_el('feMergeNode', { in: 'SourceGraphic' }));
  glow.appendChild(merge);
  defs.appendChild(glow);

  // Dot grid
  const pat = _el('pattern', { id: 'dotgrid', width: 24, height: 24, patternUnits: 'userSpaceOnUse' });
  pat.appendChild(_el('circle', { cx: 12, cy: 12, r: 0.85, fill: '#0b1c2c' }));
  defs.appendChild(pat);

  _svg.appendChild(defs);

  // Background
  _svg.appendChild(_el('rect', { width: VW, height: VH, fill: '#040c16' }));
  _svg.appendChild(_el('rect', { width: VW, height: VH, fill: 'url(#dotgrid)' }));

  // Border
  _svg.appendChild(_el('rect', {
    x: 6, y: 6, width: VW - 12, height: VH - 12,
    fill: 'none', stroke: '#091a28', 'stroke-width': 1,
  }));

  // FRONT / REAR compass labels
  _svg.appendChild(_txt('▲  FRONT', { x: CX, y: 24, class: 'bp-compass', 'text-anchor': 'middle' }));
  _svg.appendChild(_txt('▼  REAR',  { x: CX, y: 493, class: 'bp-compass', 'text-anchor': 'middle' }));
}

// ── Interactive components ───────────────────────────

function _buildComponents() {
  // Draw order: back → front (props → arms → body layers → periphery)
  _drawProps();
  _drawFrame();
  _drawBattery();
  _drawESC();
  _drawFC();
  _drawCamera();
  _drawVTX();
  _drawReceiver();
  _drawMotors();
}

function _drawProps() {
  const g = _group('propeller', 'propeller');

  MOTOR_POS.forEach(mp => {
    g.appendChild(_el('circle', {
      cx: mp.x, cy: mp.y, r: PROP_R,
      class: 'bp-prop-sweep',
      fill: 'none',
      'stroke-dasharray': '5 4',
    }));
    // Blade cross marks
    [0, 90].forEach(deg => {
      const rad = deg * Math.PI / 180;
      const dx = Math.cos(rad) * PROP_R * 0.72;
      const dy = Math.sin(rad) * PROP_R * 0.72;
      g.appendChild(_el('line', {
        x1: mp.x - dx * 0.3, y1: mp.y - dy * 0.3,
        x2: mp.x + dx, y2: mp.y + dy,
        class: 'bp-blade', 'stroke-width': 2.5, 'stroke-linecap': 'round',
      }));
      g.appendChild(_el('line', {
        x1: mp.x + dx * 0.3, y1: mp.y + dy * 0.3,
        x2: mp.x - dx, y2: mp.y - dy,
        class: 'bp-blade', 'stroke-width': 2.5, 'stroke-linecap': 'round',
      }));
    });
  });

  // Label near top-right prop
  g.appendChild(_txt('PROP ×4', {
    x: MOTOR_POS[1].x + PROP_R + 6, y: MOTOR_POS[1].y,
    class: 'bp-code', 'text-anchor': 'start', 'font-size': 9,
  }));

  _svg.appendChild(g);
}

function _drawFrame() {
  const g = _group('frame', 'frame');

  // Arms
  MOTOR_POS.forEach(mp => {
    g.appendChild(_el('line', {
      x1: CX, y1: CY, x2: mp.x, y2: mp.y,
      class: 'bp-arm', 'stroke-width': 10, 'stroke-linecap': 'round',
    }));
  });

  // Center plate
  g.appendChild(_el('rect', {
    x: CX - PLATE_HW, y: CY - PLATE_HW,
    width: PLATE_HW * 2, height: PLATE_HW * 2,
    rx: 4, class: 'bp-plate',
  }));

  // Plate corner holes
  [[-1,-1],[1,-1],[-1,1],[1,1]].forEach(([sx,sy]) => {
    g.appendChild(_el('circle', {
      cx: CX + sx * 28, cy: CY + sy * 28, r: 2.5,
      class: 'bp-mount-hole', fill: 'none',
    }));
  });

  // FRAME label on a diagonal arm
  g.appendChild(_txt('FRAME', {
    x: 192, y: 200,
    class: 'bp-code', 'font-size': 9,
    transform: 'rotate(-45, 192, 200)',
    'text-anchor': 'middle',
  }));

  _svg.appendChild(g);
}

function _drawBattery() {
  const g = _group('battery', 'battery');

  const W = 90, H = 28;
  const bx = CX - W / 2;
  const by = CY + 22;

  g.appendChild(_el('rect', { x: bx, y: by, width: W, height: H, rx: 4, class: 'bp-shape' }));

  // Cell lines
  for (let i = 1; i < 4; i++) {
    g.appendChild(_el('line', {
      x1: bx + W * i / 4, y1: by + 3,
      x2: bx + W * i / 4, y2: by + H - 3,
      class: 'bp-cell-line', 'stroke-width': 1,
    }));
  }

  // XT60 nub at left
  g.appendChild(_el('rect', { x: bx - 6, y: by + H / 2 - 5, width: 7, height: 10, rx: 1, class: 'bp-connector' }));

  g.appendChild(_txt('BATTERY', {
    x: CX, y: by + H / 2 + 4,
    class: 'bp-code', 'text-anchor': 'middle', 'font-size': 8,
  }));

  _svg.appendChild(g);
}

function _drawESC() {
  const g = _group('esc', 'esc');
  const S = 52;

  g.appendChild(_el('rect', {
    x: CX - S / 2, y: CY - S / 2, width: S, height: S,
    rx: 3, class: 'bp-shape',
  }));

  // PCB trace lines
  [[-12,-12],[12,-12],[-12,12],[12,12]].forEach(([dx,dy]) => {
    g.appendChild(_el('circle', { cx: CX + dx, cy: CY + dy, r: 4, class: 'bp-mosfet' }));
  });

  g.appendChild(_txt('ESC', {
    x: CX - S / 2 - 4, y: CY - S / 2 + 8,
    class: 'bp-code', 'text-anchor': 'end', 'font-size': 9,
  }));

  _svg.appendChild(g);
}

function _drawFC() {
  const g = _group('fc', 'fc');
  const S = 28;

  g.appendChild(_el('rect', {
    x: CX - S / 2, y: CY - S / 2, width: S, height: S,
    rx: 2, class: 'bp-shape',
  }));

  // Gyro crosshair
  g.appendChild(_el('line', { x1: CX - 7, y1: CY, x2: CX + 7, y2: CY, class: 'bp-cross', 'stroke-width': 1.2 }));
  g.appendChild(_el('line', { x1: CX, y1: CY - 7, x2: CX, y2: CY + 7, class: 'bp-cross', 'stroke-width': 1.2 }));
  g.appendChild(_el('circle', { cx: CX, cy: CY, r: 3.5, class: 'bp-cross', fill: 'none', 'stroke-width': 1 }));

  g.appendChild(_txt('FC', {
    x: CX + S / 2 + 4, y: CY + S / 2 - 4,
    class: 'bp-code', 'text-anchor': 'start', 'font-size': 9,
  }));

  _svg.appendChild(g);
}

function _drawCamera() {
  const g = _group('camera', 'camera');
  const CAM_Y = 80;

  // Mount line to body
  g.appendChild(_el('line', {
    x1: CX, y1: 96, x2: CX, y2: CY - PLATE_HW,
    class: 'bp-mount-line',
  }));

  // Housing
  g.appendChild(_el('rect', { x: CX - 19, y: CAM_Y - 14, width: 38, height: 28, rx: 3, class: 'bp-shape' }));

  // Lens barrel
  g.appendChild(_el('circle', { cx: CX, cy: CAM_Y, r: 10, class: 'bp-shape' }));
  g.appendChild(_el('circle', { cx: CX, cy: CAM_Y, r: 6, class: 'bp-lens' }));
  g.appendChild(_el('circle', { cx: CX, cy: CAM_Y, r: 2.5, class: 'bp-lens-inner' }));

  // Tilt mount arms
  g.appendChild(_el('line', { x1: CX - 18, y1: CAM_Y - 5, x2: CX - 24, y2: CAM_Y + 8, class: 'bp-arm-thin', 'stroke-width': 2 }));
  g.appendChild(_el('line', { x1: CX + 18, y1: CAM_Y - 5, x2: CX + 24, y2: CAM_Y + 8, class: 'bp-arm-thin', 'stroke-width': 2 }));

  g.appendChild(_txt('FPV CAM', { x: CX, y: 51, class: 'bp-code', 'text-anchor': 'middle', 'font-size': 9 }));

  _svg.appendChild(g);
}

function _drawVTX() {
  const g = _group('vtx', 'vtx');
  const VTX_Y = 426;

  // Mount line
  g.appendChild(_el('line', {
    x1: CX, y1: VTX_Y - 1, x2: CX, y2: CY + PLATE_HW,
    class: 'bp-mount-line',
  }));

  // Body
  g.appendChild(_el('rect', { x: CX - 17, y: VTX_Y, width: 34, height: 20, rx: 3, class: 'bp-shape' }));

  // Antenna stem + mushroom tip
  g.appendChild(_el('line', { x1: CX - 6, y1: VTX_Y, x2: CX - 14, y2: VTX_Y - 22, class: 'bp-antenna', 'stroke-width': 2 }));
  g.appendChild(_el('circle', { cx: CX - 14, cy: VTX_Y - 25, r: 5, class: 'bp-antenna-tip' }));

  g.appendChild(_txt('VTX', { x: CX, y: VTX_Y + 34, class: 'bp-code', 'text-anchor': 'middle', 'font-size': 9 }));

  _svg.appendChild(g);
}

function _drawReceiver() {
  const g = _group('receiver', 'receiver');
  const RX = 162, RY = CY - 9;

  // Body
  g.appendChild(_el('rect', { x: RX, y: RY, width: 26, height: 18, rx: 2, class: 'bp-shape' }));

  // Dipole antennas
  g.appendChild(_el('line', { x1: RX + 7, y1: RY, x2: RX + 3, y2: RY - 22, class: 'bp-antenna', 'stroke-width': 1.8 }));
  g.appendChild(_el('line', { x1: RX + 18, y1: RY, x2: RX + 22, y2: RY - 22, class: 'bp-antenna', 'stroke-width': 1.8 }));
  g.appendChild(_el('circle', { cx: RX + 3,  cy: RY - 25, r: 2.5, class: 'bp-antenna-tip' }));
  g.appendChild(_el('circle', { cx: RX + 22, cy: RY - 25, r: 2.5, class: 'bp-antenna-tip' }));

  g.appendChild(_txt('RX', { x: RX + 13, y: RY + 30, class: 'bp-code', 'text-anchor': 'middle', 'font-size': 9 }));

  _svg.appendChild(g);
}

function _drawMotors() {
  const g = _group('motor', 'motor');

  MOTOR_POS.forEach((mp, i) => {
    // Outer ring
    g.appendChild(_el('circle', { cx: mp.x, cy: mp.y, r: MOTOR_R, class: 'bp-shape' }));
    // Inner shaft
    g.appendChild(_el('circle', { cx: mp.x, cy: mp.y, r: 5, class: 'bp-shaft' }));
    // Mount screw holes
    [0, 90, 180, 270].forEach(deg => {
      const rad = deg * Math.PI / 180;
      g.appendChild(_el('circle', {
        cx: mp.x + Math.cos(rad) * 12, cy: mp.y + Math.sin(rad) * 12,
        r: 2, class: 'bp-mount-hole', fill: 'none',
      }));
    });
  });

  // Single label near top-left motor
  g.appendChild(_txt('MTR ×4', {
    x: MOTOR_POS[0].x - MOTOR_R - 6, y: MOTOR_POS[0].y,
    class: 'bp-code', 'text-anchor': 'end', 'font-size': 9,
  }));

  _svg.appendChild(g);
}

// ── State refresh ────────────────────────────────────

function _refresh() {
  const { build, violations = [] } = getState();
  const badSlots = new Set(violations.flatMap(v => v.slots));

  Object.entries(_els).forEach(([slot, el]) => {
    if (!el || !el.getAttribute) return;
    const state = _slotState(slot, build, badSlots, _active);
    el.setAttribute('class', `bp-group bp-${state}`);
    if (state === 'active') el.setAttribute('filter', 'url(#bp-glow)');
    else el.removeAttribute('filter');
  });
}

function _slotState(slot, build, badSlots, active) {
  if (slot === active)           return 'active';
  if (badSlots.has(slot))       return 'violation';
  if (build[slot])               return 'filled';
  return 'empty';
}

// ── SVG helpers ──────────────────────────────────────

function _el(tag, attrs = {}) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, String(v));
  return e;
}

function _txt(text, attrs = {}) {
  const e = _el('text', attrs);
  e.textContent = text;
  return e;
}

function _group(id, slot) {
  const g = _el('g', { class: 'bp-group bp-empty', 'data-slot': slot || '' });
  if (slot) {
    g.style.cursor = 'pointer';
    g.setAttribute('role', 'button');
    g.setAttribute('aria-label', `Select ${slot}`);
    g.addEventListener('click', () => dispatch('SET_ACTIVE_SLOT', { slot }));
  }
  if (id) _els[id] = g;
  return g;
}
