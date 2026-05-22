import { on, getState, getPartById, dispatch } from './store.js';

const NS  = 'http://www.w3.org/2000/svg';
const VW  = 500;
const VH  = 500;
const CX  = 250;
const CY  = 252;

const MOTOR_POS = [
  { x: 142, y: 142 }, // FL
  { x: 358, y: 142 }, // FR
  { x: 142, y: 358 }, // RL
  { x: 358, y: 358 }, // RR
];
const MOTOR_R  = 18;
const PROP_R   = 52;
const PLATE_HW = 36;

const BRAND_DOMAINS = {
  'AKK': 'akktek.com', 'Aikon': 'aikonfpv.com', 'Armattan': 'armattanquads.com',
  'BetaFPV': 'betafpv.com', 'Caddx': 'caddxfpv.com', 'CNHL': 'chinahobbyline.com',
  'DAL': 'dalprops.com', 'Diatone': 'diatone.us', 'DJI': 'dji.com',
  'EMAX': 'emaxmodel.com', 'Ethix': 'ethix.cc', 'ExpressLRS': 'expresslrs.org',
  'FlyFishRC': 'flyfish-rc.com', 'FlySky': 'flysky.com', 'Flywoo': 'flywoo.net',
  'Foxeer': 'foxeer.com', 'FrSky': 'frsky-rc.com', 'Gemfan': 'gemfanhobby.com',
  'GEPRC': 'geprc.com', 'GNB': 'gaonengmodels.com', 'HappyModel': 'happymodel.cn',
  'HDZero': 'hd-zero.com', 'HGLRC': 'hglrc.com', 'Hobbywing': 'hobbywing.com',
  'Holybro': 'holybro.com', 'HQProp': 'hqprop.com', 'Hypetrain': 'hypetrain.io',
  'iFlight': 'iflight.com', 'ImmersionRC': 'immersionrc.com', 'ImpulseRC': 'impulserc.com',
  'JHEMCU': 'jhemcu.com', 'Jumper': 'jumper-rc.com', 'Lumenier': 'lumenier.com',
  'Matek': 'mateksys.com', 'MEPS': 'mepsrc.com', 'Ovonic': 'ovonicshop.com',
  'Racerstar': 'racerstar.com', 'RadioMaster': 'radiomasterrc.com', 'RunCam': 'runcam.com',
  'Rush': 'rushfpv.net', 'ShenDrones': 'shendrones.com', 'Spektrum': 'spektrumrc.com',
  'SpeedyBee': 'speedybee.com', 'Tattu': 'genstattu.com', 'TBS': 'team-blacksheep.com',
  'T-Motor': 'tmotor.com', 'Walksnail': 'caddxfpv.com',
};

let _svg    = null;
let _els    = {};
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

// ── Static elements ──────────────────────────────────

function _buildStatic() {
  const defs = _el('defs');

  // Glow filter
  const glow = _el('filter', { id: 'bp-glow', x: '-60%', y: '-60%', width: '220%', height: '220%' });
  glow.appendChild(_el('feGaussianBlur', { in: 'SourceGraphic', stdDeviation: '5', result: 'blur' }));
  const merge = _el('feMerge');
  merge.appendChild(_el('feMergeNode', { in: 'blur' }));
  merge.appendChild(_el('feMergeNode', { in: 'SourceGraphic' }));
  glow.appendChild(merge);
  defs.appendChild(glow);

  // Drop shadow filter for filled components
  const shadow = _el('filter', { id: 'bp-shadow', x: '-20%', y: '-20%', width: '140%', height: '140%' });
  shadow.appendChild(_el('feDropShadow', { dx: '0', dy: '2', stdDeviation: '3', 'flood-color': '#00000020' }));
  defs.appendChild(shadow);

  // Radial gradient for motor highlight
  const motorGrad = _el('radialGradient', { id: 'bp-motor-grad', cx: '38%', cy: '32%', r: '70%' });
  const mg1 = _el('stop', { offset: '0%' });
  mg1.style.stopColor = '#ffffff';
  mg1.style.stopOpacity = '0.28';
  const mg2 = _el('stop', { offset: '100%' });
  mg2.style.stopColor = '#000000';
  mg2.style.stopOpacity = '0.38';
  motorGrad.appendChild(mg1);
  motorGrad.appendChild(mg2);
  defs.appendChild(motorGrad);

  // Favicon clip circle
  const clip = _el('clipPath', { id: 'bp-fav-clip' });
  clip.appendChild(_el('circle', { cx: 8, cy: 8, r: 8 }));
  defs.appendChild(clip);

  // Light dot grid
  const pat = _el('pattern', { id: 'dotgrid', width: 24, height: 24, patternUnits: 'userSpaceOnUse' });
  pat.appendChild(_el('circle', { cx: 12, cy: 12, r: 0.7, fill: '#dde4ed' }));
  defs.appendChild(pat);

  _svg.appendChild(defs);

  // Light background
  _svg.appendChild(_el('rect', { width: VW, height: VH, fill: '#f8fafc' }));
  _svg.appendChild(_el('rect', { width: VW, height: VH, fill: 'url(#dotgrid)' }));

  // Border
  _svg.appendChild(_el('rect', {
    x: 6, y: 6, width: VW - 12, height: VH - 12,
    fill: 'none', stroke: '#e2e8f0', 'stroke-width': 1,
  }));

  _svg.appendChild(_txt('▲  FRONT', { x: CX, y: 24, class: 'bp-compass', 'text-anchor': 'middle' }));
  _svg.appendChild(_txt('▼  REAR',  { x: CX, y: 493, class: 'bp-compass', 'text-anchor': 'middle' }));
}

// ── Interactive components ───────────────────────────

function _buildComponents() {
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
    // Curved blade pair (2 bezier paths, will be replaced dynamically)
    _appendBlades(g, mp.x, mp.y, PROP_R, 2);
  });

  g.appendChild(_txt('PROP ×4', {
    x: MOTOR_POS[1].x + PROP_R + 6, y: MOTOR_POS[1].y - 6,
    class: 'bp-code', 'text-anchor': 'start', 'font-size': 9,
  }));
  // Part name + spec labels
  const nameT = _txt('', { class: 'bp-part-name', 'text-anchor': 'start',
    x: MOTOR_POS[1].x + PROP_R + 6, y: MOTOR_POS[1].y + 8 });
  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'start',
    x: MOTOR_POS[1].x + PROP_R + 6, y: MOTOR_POS[1].y + 19 });
  g.appendChild(nameT);
  g.appendChild(specT);

  _svg.appendChild(g);
}

function _appendBlades(parent, mx, my, pr, bladeCount) {
  const angles = bladeCount === 2
    ? [0, 180]
    : bladeCount === 3
    ? [0, 120, 240]
    : [0, 90, 180, 270];

  angles.forEach(deg => {
    const rad = deg * Math.PI / 180;
    const cos = Math.cos(rad), sin = Math.sin(rad);
    const tipX = mx + cos * pr * 0.88;
    const tipY = my + sin * pr * 0.88;
    const ctlX = mx + cos * pr * 0.5 - sin * pr * 0.38;
    const ctlY = my + sin * pr * 0.5 + cos * pr * 0.38;
    const d = `M ${mx + cos * 5} ${my + sin * 5} Q ${ctlX} ${ctlY} ${tipX} ${tipY}`;
    const blade = _el('path', { d, class: 'bp-blade', 'stroke-width': 2.5, 'stroke-linecap': 'round', fill: 'none' });
    blade.setAttribute('data-blade', '1');
    parent.appendChild(blade);
  });
}

function _drawFrame() {
  const g = _group('frame', 'frame');

  // Tapered arm shadow + main arm
  MOTOR_POS.forEach(mp => {
    g.appendChild(_el('line', {
      x1: CX, y1: CY, x2: mp.x, y2: mp.y,
      class: 'bp-arm-shadow', 'stroke-width': 16, 'stroke-linecap': 'round',
    }));
    g.appendChild(_el('line', {
      x1: CX, y1: CY, x2: mp.x, y2: mp.y,
      class: 'bp-arm', 'stroke-width': 10, 'stroke-linecap': 'round',
    }));
  });

  // Center plate
  g.appendChild(_el('rect', {
    x: CX - PLATE_HW, y: CY - PLATE_HW,
    width: PLATE_HW * 2, height: PLATE_HW * 2,
    rx: 5, class: 'bp-plate',
  }));

  // Corner holes
  [[-1,-1],[1,-1],[-1,1],[1,1]].forEach(([sx,sy]) => {
    g.appendChild(_el('circle', {
      cx: CX + sx * 28, cy: CY + sy * 28, r: 2.5,
      class: 'bp-mount-hole', fill: 'none',
    }));
  });

  // Brand favicon (top-left of plate)
  const fav = _el('image', {
    x: CX - PLATE_HW + 4, y: CY - PLATE_HW + 4,
    width: 14, height: 14,
    class: 'bp-brand-img',
    display: 'none',
    'clip-path': 'url(#bp-fav-clip)',
  });
  g.appendChild(fav);

  g.appendChild(_txt('FRAME', {
    x: 192, y: 200,
    class: 'bp-code', 'font-size': 9,
    transform: 'rotate(-45, 192, 200)',
    'text-anchor': 'middle',
  }));

  const nameT = _txt('', { class: 'bp-part-name', 'text-anchor': 'middle',
    x: CX, y: CY - PLATE_HW - 10 });
  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'middle',
    x: CX, y: CY - PLATE_HW - 1 });
  g.appendChild(nameT);
  g.appendChild(specT);

  _svg.appendChild(g);
}

function _drawBattery() {
  const g = _group('battery', 'battery');

  const W = 90, H = 28;
  const bx = CX - W / 2;
  const by = CY + 22;

  g.appendChild(_el('rect', { x: bx, y: by, width: W, height: H, rx: 5, class: 'bp-shape' }));

  // Default 4 cell lines — tagged for dynamic replacement
  for (let i = 1; i < 4; i++) {
    const line = _el('line', {
      x1: bx + W * i / 4, y1: by + 4,
      x2: bx + W * i / 4, y2: by + H - 4,
      class: 'bp-cell-line', 'stroke-width': 1,
    });
    line.setAttribute('data-cell', '1');
    g.appendChild(line);
  }

  // XT60 connector nub
  g.appendChild(_el('rect', { x: bx - 7, y: by + H / 2 - 5, width: 8, height: 10, rx: 2, class: 'bp-connector' }));

  // Brand favicon
  const fav = _el('image', {
    x: bx + 5, y: by + H / 2 - 7,
    width: 14, height: 14,
    class: 'bp-brand-img',
    display: 'none',
    'clip-path': 'url(#bp-fav-clip)',
  });
  g.appendChild(fav);

  g.appendChild(_txt('BATTERY', {
    x: CX + 8, y: by + H / 2 + 4,
    class: 'bp-code', 'text-anchor': 'middle', 'font-size': 8,
  }));

  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'middle', x: CX, y: by + H + 12 });
  g.appendChild(specT);

  _svg.appendChild(g);
}

function _drawESC() {
  const g = _group('esc', 'esc');
  const S = 52;

  g.appendChild(_el('rect', {
    x: CX - S / 2, y: CY - S / 2, width: S, height: S,
    rx: 4, class: 'bp-shape',
  }));

  // Chip pads
  [[-12,-12],[12,-12],[-12,12],[12,12]].forEach(([dx,dy]) => {
    g.appendChild(_el('rect', {
      x: CX + dx - 4, y: CY + dy - 3.5, width: 8, height: 7, rx: 1.5,
      class: 'bp-mosfet',
    }));
  });

  // Brand favicon
  const fav = _el('image', {
    x: CX - 7, y: CY - 7,
    width: 14, height: 14,
    class: 'bp-brand-img',
    display: 'none',
    'clip-path': 'url(#bp-fav-clip)',
  });
  g.appendChild(fav);

  g.appendChild(_txt('ESC', {
    x: CX - S / 2 - 4, y: CY - S / 2 + 8,
    class: 'bp-code', 'text-anchor': 'end', 'font-size': 9,
  }));

  const nameT = _txt('', { class: 'bp-part-name', 'text-anchor': 'end',
    x: CX - S / 2 - 4, y: CY - S / 2 + 20 });
  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'end',
    x: CX - S / 2 - 4, y: CY - S / 2 + 31 });
  g.appendChild(nameT);
  g.appendChild(specT);

  _svg.appendChild(g);
}

function _drawFC() {
  const g = _group('fc', 'fc');
  const S = 28;

  g.appendChild(_el('rect', {
    x: CX - S / 2, y: CY - S / 2, width: S, height: S,
    rx: 3, class: 'bp-shape',
  }));

  // PCB chip package outline
  g.appendChild(_el('rect', {
    x: CX - 5, y: CY - 5, width: 10, height: 10, rx: 1,
    class: 'bp-cross', fill: 'none', 'stroke-width': 1,
  }));

  // Gyro crosshair
  g.appendChild(_el('line', { x1: CX - 8, y1: CY, x2: CX + 8, y2: CY, class: 'bp-cross', 'stroke-width': 1.2 }));
  g.appendChild(_el('line', { x1: CX, y1: CY - 8, x2: CX, y2: CY + 8, class: 'bp-cross', 'stroke-width': 1.2 }));
  g.appendChild(_el('circle', { cx: CX, cy: CY, r: 3.5, class: 'bp-cross', fill: 'none', 'stroke-width': 1 }));

  // Brand favicon
  const fav = _el('image', {
    x: CX - S / 2 + 1, y: CY - S / 2 + 1,
    width: 10, height: 10,
    class: 'bp-brand-img',
    display: 'none',
    'clip-path': 'url(#bp-fav-clip)',
  });
  g.appendChild(fav);

  g.appendChild(_txt('FC', {
    x: CX + S / 2 + 4, y: CY + S / 2 - 4,
    class: 'bp-code', 'text-anchor': 'start', 'font-size': 9,
  }));

  const nameT = _txt('', { class: 'bp-part-name', 'text-anchor': 'start',
    x: CX + S / 2 + 4, y: CY + S / 2 + 6 });
  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'start',
    x: CX + S / 2 + 4, y: CY + S / 2 + 17 });
  g.appendChild(nameT);
  g.appendChild(specT);

  _svg.appendChild(g);
}

function _drawCamera() {
  const g = _group('camera', 'camera');
  const CAM_Y = 80;

  g.appendChild(_el('line', {
    x1: CX, y1: 96, x2: CX, y2: CY - PLATE_HW,
    class: 'bp-mount-line',
  }));

  // Housing
  g.appendChild(_el('rect', { x: CX - 19, y: CAM_Y - 14, width: 38, height: 28, rx: 3, class: 'bp-shape' }));

  // Lens layers
  g.appendChild(_el('circle', { cx: CX, cy: CAM_Y, r: 10, class: 'bp-shape' }));
  g.appendChild(_el('circle', { cx: CX, cy: CAM_Y, r: 6, class: 'bp-lens' }));
  g.appendChild(_el('circle', { cx: CX, cy: CAM_Y, r: 2.5, class: 'bp-lens-inner' }));
  // Specular highlight
  g.appendChild(_el('ellipse', {
    cx: CX - 3, cy: CAM_Y - 3.5, rx: 2, ry: 1.3,
    class: 'bp-lens-highlight',
  }));

  // Tilt arms
  g.appendChild(_el('line', { x1: CX - 18, y1: CAM_Y - 5, x2: CX - 24, y2: CAM_Y + 8, class: 'bp-arm-thin', 'stroke-width': 2 }));
  g.appendChild(_el('line', { x1: CX + 18, y1: CAM_Y - 5, x2: CX + 24, y2: CAM_Y + 8, class: 'bp-arm-thin', 'stroke-width': 2 }));

  // Brand favicon inside lens area
  const fav = _el('image', {
    x: CX - 7, y: CAM_Y - 7,
    width: 14, height: 14,
    class: 'bp-brand-img',
    display: 'none',
    opacity: '0.7',
    'clip-path': 'url(#bp-fav-clip)',
  });
  g.appendChild(fav);

  g.appendChild(_txt('FPV CAM', { x: CX, y: 51, class: 'bp-code', 'text-anchor': 'middle', 'font-size': 9 }));

  const nameT = _txt('', { class: 'bp-part-name', 'text-anchor': 'middle', x: CX, y: 41 });
  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'middle', x: CX, y: 32 });
  g.appendChild(nameT);
  g.appendChild(specT);

  _svg.appendChild(g);
}

function _drawVTX() {
  const g = _group('vtx', 'vtx');
  const VTX_Y = 426;

  g.appendChild(_el('line', {
    x1: CX, y1: VTX_Y - 1, x2: CX, y2: CY + PLATE_HW,
    class: 'bp-mount-line',
  }));

  g.appendChild(_el('rect', { x: CX - 17, y: VTX_Y, width: 34, height: 20, rx: 3, class: 'bp-shape' }));

  // Antenna
  g.appendChild(_el('line', { x1: CX - 6, y1: VTX_Y, x2: CX - 14, y2: VTX_Y - 22, class: 'bp-antenna', 'stroke-width': 2 }));
  g.appendChild(_el('circle', { cx: CX - 14, cy: VTX_Y - 25, r: 5, class: 'bp-antenna-tip' }));

  // Brand favicon
  const fav = _el('image', {
    x: CX - 6, y: VTX_Y + 3,
    width: 12, height: 12,
    class: 'bp-brand-img',
    display: 'none',
    'clip-path': 'url(#bp-fav-clip)',
  });
  g.appendChild(fav);

  g.appendChild(_txt('VTX', { x: CX, y: VTX_Y + 34, class: 'bp-code', 'text-anchor': 'middle', 'font-size': 9 }));

  const nameT = _txt('', { class: 'bp-part-name', 'text-anchor': 'middle', x: CX, y: VTX_Y + 44 });
  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'middle', x: CX, y: VTX_Y + 54 });
  g.appendChild(nameT);
  g.appendChild(specT);

  _svg.appendChild(g);
}

function _drawReceiver() {
  const g = _group('receiver', 'receiver');
  const RX = 162, RY = CY - 9;

  g.appendChild(_el('rect', { x: RX, y: RY, width: 26, height: 18, rx: 2, class: 'bp-shape' }));

  // Dipole antennas
  g.appendChild(_el('line', { x1: RX + 7, y1: RY, x2: RX + 3, y2: RY - 22, class: 'bp-antenna', 'stroke-width': 1.8 }));
  g.appendChild(_el('line', { x1: RX + 18, y1: RY, x2: RX + 22, y2: RY - 22, class: 'bp-antenna', 'stroke-width': 1.8 }));
  g.appendChild(_el('circle', { cx: RX + 3,  cy: RY - 25, r: 2.5, class: 'bp-antenna-tip' }));
  g.appendChild(_el('circle', { cx: RX + 22, cy: RY - 25, r: 2.5, class: 'bp-antenna-tip' }));

  // Brand favicon
  const fav = _el('image', {
    x: RX + 7, y: RY + 2,
    width: 12, height: 12,
    class: 'bp-brand-img',
    display: 'none',
    'clip-path': 'url(#bp-fav-clip)',
  });
  g.appendChild(fav);

  g.appendChild(_txt('RX', { x: RX + 13, y: RY + 30, class: 'bp-code', 'text-anchor': 'middle', 'font-size': 9 }));

  const nameT = _txt('', { class: 'bp-part-name', 'text-anchor': 'middle', x: RX + 13, y: RY + 40 });
  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'middle', x: RX + 13, y: RY + 50 });
  g.appendChild(nameT);
  g.appendChild(specT);

  _svg.appendChild(g);
}

function _drawMotors() {
  const g = _group('motor', 'motor');

  MOTOR_POS.forEach(mp => {
    // Outer ring with radial gradient overlay
    g.appendChild(_el('circle', { cx: mp.x, cy: mp.y, r: MOTOR_R, class: 'bp-shape' }));
    // Gradient highlight layer
    g.appendChild(_el('circle', {
      cx: mp.x, cy: mp.y, r: MOTOR_R,
      fill: 'url(#bp-motor-grad)',
      'pointer-events': 'none',
      class: 'bp-motor-grad-layer',
    }));
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
    // Stator winding lines
    for (let w = 0; w < 6; w++) {
      const wRad = (w * 60) * Math.PI / 180;
      g.appendChild(_el('line', {
        x1: mp.x + Math.cos(wRad) * 7,  y1: mp.y + Math.sin(wRad) * 7,
        x2: mp.x + Math.cos(wRad) * 14, y2: mp.y + Math.sin(wRad) * 14,
        class: 'bp-winding', 'stroke-width': 1.5,
      }));
    }
  });

  // Brand favicon near FL motor
  const fav = _el('image', {
    x: MOTOR_POS[0].x - 8, y: MOTOR_POS[0].y - MOTOR_R - 20,
    width: 14, height: 14,
    class: 'bp-brand-img',
    display: 'none',
    'clip-path': 'url(#bp-fav-clip)',
  });
  g.appendChild(fav);

  g.appendChild(_txt('MTR ×4', {
    x: MOTOR_POS[0].x - MOTOR_R - 6, y: MOTOR_POS[0].y,
    class: 'bp-code', 'text-anchor': 'end', 'font-size': 9,
  }));

  const nameT = _txt('', { class: 'bp-part-name', 'text-anchor': 'end',
    x: MOTOR_POS[0].x - MOTOR_R - 6, y: MOTOR_POS[0].y + 12 });
  const specT = _txt('', { class: 'bp-part-spec', 'text-anchor': 'end',
    x: MOTOR_POS[0].x - MOTOR_R - 6, y: MOTOR_POS[0].y + 23 });
  g.appendChild(nameT);
  g.appendChild(specT);

  _svg.appendChild(g);
}

// ── State refresh ────────────────────────────────────

function _refresh() {
  const { build, violations = [] } = getState();
  const badSlots = new Set(violations.flatMap(v => v.slots));

  Object.entries(_els).forEach(([slot, el]) => {
    if (!el || !el.getAttribute) return;
    const partId = build[slot];
    const part   = partId ? getPartById(partId) : null;
    const state  = _slotState(slot, build, badSlots, _active);

    el.setAttribute('class', `bp-group bp-${state}`);

    if (state === 'active') {
      el.setAttribute('filter', 'url(#bp-glow)');
    } else if (state === 'filled') {
      el.setAttribute('filter', 'url(#bp-shadow)');
    } else {
      el.removeAttribute('filter');
    }

    if (part && state !== 'violation') {
      el.style.setProperty('--pc', part.color);
      el.style.setProperty('--pf', _hexAlpha(part.color, 0.15));
    } else {
      el.style.removeProperty('--pc');
      el.style.removeProperty('--pf');
    }

    _updatePartInfo(slot, el, part, state);
    if (slot === 'propeller') _updatePropBlades(el, part);
    if (slot === 'battery')   _updateBatteryCells(el, part);
  });
}

function _updatePartInfo(slot, el, part, state) {
  const nameEl = el.querySelector('.bp-part-name');
  const specEl = el.querySelector('.bp-part-spec');
  const imgEl  = el.querySelector('.bp-brand-img');
  const filled = !!part && state !== 'empty';

  if (nameEl) nameEl.textContent = filled ? _truncate(part.name, 18) : '';
  if (specEl) specEl.textContent = filled ? _partSpec(slot, part) : '';

  if (imgEl) {
    const domain = BRAND_DOMAINS[part?.brand];
    if (filled && domain) {
      imgEl.setAttribute('href', `https://www.google.com/s2/favicons?domain=${domain}&sz=64`);
      imgEl.removeAttribute('display');
    } else {
      imgEl.setAttribute('display', 'none');
    }
  }
}

function _updatePropBlades(el, part) {
  // Remove existing blade paths
  el.querySelectorAll('[data-blade]').forEach(n => n.remove());
  const bladeCount = part?.specs?.blade_count ?? 2;
  const propR = part?.specs?.diameter_inch
    ? Math.min(58, Math.max(36, part.specs.diameter_inch * 9.5))
    : PROP_R;

  // Update sweep circle radii
  const sweeps = el.querySelectorAll('.bp-prop-sweep');
  sweeps.forEach((sw, i) => {
    sw.setAttribute('r', propR);
  });

  // Re-draw blades at each motor position
  MOTOR_POS.forEach(mp => {
    _appendBlades(el, mp.x, mp.y, propR, bladeCount);
  });
}

function _updateBatteryCells(el, part) {
  el.querySelectorAll('[data-cell]').forEach(n => n.remove());
  const cells = part?.specs?.cell_count_s ?? 4;
  const W = 90;
  const bx = CX - W / 2;
  const by = CY + 22;
  const H  = 28;

  for (let i = 1; i < cells; i++) {
    const line = _el('line', {
      x1: bx + W * i / cells, y1: by + 4,
      x2: bx + W * i / cells, y2: by + H - 4,
      class: 'bp-cell-line', 'stroke-width': 1,
    });
    line.setAttribute('data-cell', '1');
    el.appendChild(line);
  }
}

function _slotState(slot, build, badSlots, active) {
  if (slot === active)     return 'active';
  if (badSlots.has(slot)) return 'violation';
  if (build[slot])         return 'filled';
  return 'empty';
}

// ── Helpers ──────────────────────────────────────────

function _partSpec(slot, part) {
  const s = part.specs || {};
  switch (slot) {
    case 'motor':     return s.kv ? `${s.kv}KV` : '';
    case 'propeller': return (s.diameter_inch && s.blade_count) ? `${s.diameter_inch}" ${s.blade_count}B` : '';
    case 'battery':   return (s.cell_count_s && s.capacity_mah) ? `${s.cell_count_s}S ${s.capacity_mah}mAh` : '';
    case 'frame':     return s.size_mm ? `${s.size_mm}mm` : '';
    case 'esc':       return s.amp_rating ? `${s.amp_rating}A` : '';
    case 'fc':        return s.gyro || '';
    case 'camera':    return s.fov_deg ? `${s.fov_deg}° FOV` : '';
    case 'vtx':       return s.power_mw_max ? `${s.power_mw_max}mW` : '';
    case 'receiver':  return s.protocol || '';
    default:          return '';
  }
}

function _truncate(str, n) {
  return str && str.length > n ? str.slice(0, n - 1) + '…' : str;
}

function _hexAlpha(hex, a) {
  const h = (hex || '#888888').replace(/^#/, '');
  const full = h.length === 3
    ? h[0]+h[0]+h[1]+h[1]+h[2]+h[2]
    : h.padEnd(6, '0').slice(0, 6);
  const r = parseInt(full.slice(0, 2), 16) || 0;
  const g = parseInt(full.slice(2, 4), 16) || 0;
  const b = parseInt(full.slice(4, 6), 16) || 0;
  return `rgba(${r},${g},${b},${a})`;
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
