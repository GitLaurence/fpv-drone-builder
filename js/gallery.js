import { on, getState, getPartById } from './store.js';

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

const CATEGORY_META = {
  frame:     { icon: '🛸', label: 'Frame' },
  motor:     { icon: '⚙️', label: 'Motors' },
  esc:       { icon: '⚡', label: 'ESC' },
  fc:        { icon: '💻', label: 'Flight Controller' },
  propeller: { icon: '🌀', label: 'Propellers' },
  camera:    { icon: '📷', label: 'FPV Camera' },
  vtx:       { icon: '📡', label: 'VTX' },
  battery:   { icon: '🔋', label: 'Battery' },
  receiver:  { icon: '📻', label: 'Receiver' },
};

const SLOTS_ORDER = ['frame', 'motor', 'esc', 'fc', 'propeller', 'camera', 'vtx', 'battery', 'receiver'];

// ── Public API ───────────────────────────────────────

export function init() {
  const modal   = document.getElementById('modal-gallery');
  const btn     = document.getElementById('btn-gallery');
  const closeBtn = document.getElementById('modal-gallery-close');

  if (!modal || !btn) return;

  btn.addEventListener('click', () => openGallery());
  closeBtn?.addEventListener('click', () => modal.close());
  modal.addEventListener('click', e => { if (e.target === modal) modal.close(); });

  on('build:changed', ({ build }) => _updateBtn(build));

  // Handle gallery open requests from blueprint diagram
  document.addEventListener('gallery:open', e => {
    openGallery(e.detail?.slot);
  });
}

export function openGallery(focusSlot = null) {
  const modal = document.getElementById('modal-gallery');
  if (!modal) return;
  _renderGrid(focusSlot);
  modal.showModal();
  if (focusSlot) {
    requestAnimationFrame(() => {
      const card = modal.querySelector(`[data-slot="${focusSlot}"]`);
      card?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      card?.classList.add('gallery-card-focus');
      setTimeout(() => card?.classList.remove('gallery-card-focus'), 1600);
    });
  }
}

// ── Internal ─────────────────────────────────────────

function _updateBtn(build) {
  const btn   = document.getElementById('btn-gallery');
  const count = document.getElementById('gallery-btn-count');
  if (!btn) return;
  const filled = Object.values(build).filter(Boolean).length;
  btn.classList.toggle('gallery-btn-active', filled > 0);
  if (count) count.textContent = filled > 0 ? filled : '';
}

function _renderGrid(focusSlot) {
  const { build } = getState();
  const grid    = document.getElementById('gallery-grid');
  const countEl = document.getElementById('gallery-modal-count');
  if (!grid) return;

  const filled = SLOTS_ORDER.filter(s => build[s]).length;
  if (countEl) countEl.textContent = filled > 0 ? `${filled} / 9 selected` : '';

  grid.innerHTML = SLOTS_ORDER.map(slot => {
    const partId = build[slot];
    const part   = partId ? getPartById(partId) : null;
    const focused = slot === focusSlot;
    return _cardHTML(slot, part, focused);
  }).join('');
}

function _cardHTML(slot, part, focused) {
  const meta    = CATEGORY_META[slot] || { icon: '📦', label: slot };
  const focused_ = focused ? ' gallery-card-focus' : '';

  if (!part) {
    return `<div class="gallery-card gallery-card-empty${focused_}" data-slot="${slot}">
      <div class="gallery-card-visual gallery-card-visual-empty">
        <span class="gallery-card-icon">${meta.icon}</span>
      </div>
      <div class="gallery-card-info">
        <div class="gallery-card-category">${meta.label}</div>
        <div class="gallery-card-name gallery-card-unset">Not selected</div>
      </div>
    </div>`;
  }

  const color  = _expandHex(part.color || '#3b82f6');
  const [r, g, b] = _hexToRgb(color);
  const borderClr  = `rgba(${r},${g},${b},0.28)`;
  const iconClr    = _isLight(r, g, b) ? `rgba(${r},${g},${b},0.7)` : color;

  const domain   = BRAND_DOMAINS[part.brand];
  const favicon  = domain
    ? `<img class="gallery-favicon" src="https://www.google.com/s2/favicons?domain=${domain}&sz=32" alt="${part.brand}" loading="lazy" onerror="this.replaceWith(Object.assign(document.createElement('span'),{className:'gallery-favicon-text',textContent:'${(part.brand||'?')[0]}'}));">`
    : `<span class="gallery-favicon-text">${(part.brand || '?')[0]}</span>`;

  // Use real product photo if available, otherwise an inline SVG placeholder
  const imgSrc = part.image_url || _placeholderImg(slot, r, g, b, meta.icon, part);
  const imgTag = `<img class="gallery-product-img${part.image_url ? '' : ' gallery-product-placeholder'}" src="${imgSrc}" alt="${part.name}" loading="lazy">`;

  const spec     = _keySpec(slot, part);
  const price    = part.price_php ? `₱${part.price_php.toLocaleString()}` : '';
  const weight   = part.weight_g  ? `${part.weight_g}g` : '';

  return `<div class="gallery-card${focused_}" data-slot="${slot}"
               style="--gc:${color};--gcr:${r};--gcg:${g};--gcb:${b}">
    <a class="gallery-card-visual" href="${part.buy_url || '#'}" target="_blank"
       rel="noopener" title="View on retailer site">
      ${imgTag}
      <span class="gallery-card-icon" style="color:${iconClr}">${meta.icon}</span>
      <div class="gallery-favicon-wrap">${favicon}</div>
      <span class="gallery-card-view-label">View product ↗</span>
    </a>
    <div class="gallery-card-info" style="--card-border:${borderClr}">
      <div class="gallery-card-category">${meta.label}</div>
      <div class="gallery-card-brand">${part.brand}</div>
      <div class="gallery-card-name" title="${part.name}">${part.name}</div>
      ${spec ? `<div class="gallery-card-spec">${spec}</div>` : ''}
      <div class="gallery-card-meta">
        ${price  ? `<span class="gallery-card-price">${price}</span>` : ''}
        ${weight ? `<span class="gallery-card-weight">${weight}</span>` : ''}
      </div>
    </div>
  </div>`;
}

function _keySpec(slot, part) {
  const s = part.specs || {};
  switch (slot) {
    case 'motor':     return s.kv ? `${s.kv} KV` : '';
    case 'propeller': return (s.diameter_inch && s.blade_count) ? `${s.diameter_inch}" ${s.blade_count}-blade` : '';
    case 'battery':   return (s.cell_count_s && s.capacity_mah) ? `${s.cell_count_s}S ${s.capacity_mah}mAh` : '';
    case 'frame':     return s.size_mm ? `${s.size_mm}mm · ${(s.material || '').slice(0,2).toUpperCase() || ''}` : '';
    case 'esc':       return s.amp_rating ? `${s.amp_rating}A` : '';
    case 'fc':        return s.gyro || '';
    case 'camera':    return s.fov_deg ? `${s.fov_deg}° FOV` : '';
    case 'vtx':       return s.power_mw_max ? `${s.power_mw_max}mW` : '';
    case 'receiver':  return s.protocol || '';
    default:          return '';
  }
}

// ── Per-category SVG illustrations ──────────────────────
// Returns a data URI SVG illustration styled in the part's color.
// Used as the img src when no product photo is available.

function _placeholderImg(slot, r, g, b, _icon, part) {
  const pc  = `rgb(${r},${g},${b})`;           // primary color
  const pf  = `rgba(${r},${g},${b},0.13)`;     // fill
  const pm  = `rgba(${r},${g},${b},0.22)`;     // mid fill
  const bg1 = `rgba(${r},${g},${b},0.05)`;
  const bg2 = `rgba(${r},${g},${b},0.15)`;
  const s   = part?.specs || {};

  const drawings = {
    frame() {
      const arms = [[120,48,42,14],[120,48,198,14],[120,48,42,82],[120,48,198,82]];
      return arms.map(([x1,y1,x2,y2]) =>
        `<line x1='${x1}' y1='${y1}' x2='${x2}' y2='${y2}' stroke='${pc}' stroke-width='9' stroke-linecap='round' opacity='.75'/>
         <line x1='${x1}' y1='${y1}' x2='${x2}' y2='${y2}' stroke='${pc}' stroke-width='5' stroke-linecap='round'/>`
      ).join('') +
        `<rect x='98' y='26' width='44' height='44' rx='5' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        [[42,14],[198,14],[42,82],[198,82]].map(([cx,cy]) =>
          `<circle cx='${cx}' cy='${cy}' r='10' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>
           <circle cx='${cx}' cy='${cy}' r='4' fill='${pc}' opacity='.4'/>`
        ).join('') +
        `<circle cx='120' cy='48' r='6' fill='${pc}' opacity='.35'/>`;
    },

    motor() {
      const rings = [38, 27, 17, 7];
      const windings = Array.from({length:6},(_,i)=>{
        const a=i*60*Math.PI/180;
        return `<line x1='${120+Math.cos(a)*18}' y1='${48+Math.sin(a)*18}' x2='${120+Math.cos(a)*28}' y2='${48+Math.sin(a)*28}' stroke='${pc}' stroke-width='1.5' opacity='.55'/>`;
      }).join('');
      return rings.map((r,i) =>
        `<circle cx='120' cy='48' r='${r}' fill='${i===0?pf:i===1?pm:"none"}' stroke='${pc}' stroke-width='${i===0?1.5:1}' opacity='${i===3?.4:1}'/>`
      ).join('') + windings +
        `<circle cx='120' cy='48' r='5' fill='${pc}' opacity='.6'/>` +
        `<circle cx='108' cy='38' r='4' fill='rgba(255,255,255,.22)'/>`;
    },

    esc() {
      const chips = [[32,20,176,12],[32,64,176,12],[136,20,30,56],[100,20,30,56]];
      const [px,py,pw,ph] = chips[2];
      return `<rect x='18' y='16' width='204' height='64' rx='5' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        [[24,22,26,16],[190,22,26,16],[24,58,26,16],[190,58,26,16]].map(([x,y,w,h]) =>
          `<rect x='${x}' y='${y}' width='${w}' height='${h}' rx='2' fill='${pm}' stroke='${pc}' stroke-width='1'/>`
        ).join('') +
        `<rect x='88' y='26' width='64' height='44' rx='3' fill='${pm}' stroke='${pc}' stroke-width='1'/>` +
        `<line x1='120' y1='30' x2='120' y2='66' stroke='${pc}' stroke-width='.8' opacity='.4'/>` +
        `<line x1='92' y1='48' x2='148' y2='48' stroke='${pc}' stroke-width='.8' opacity='.4'/>`;
    },

    fc() {
      const sz = 58;
      return `<rect x='${120-sz/2}' y='${48-sz/2}' width='${sz}' height='${sz}' rx='5' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        `<rect x='107' y='35' width='26' height='26' rx='2' fill='${pm}' stroke='${pc}' stroke-width='1'/>` +
        `<line x1='91' y1='48' x2='149' y2='48' stroke='${pc}' stroke-width='1.2' opacity='.7'/>` +
        `<line x1='120' y1='19' x2='120' y2='77' stroke='${pc}' stroke-width='1.2' opacity='.7'/>` +
        `<circle cx='120' cy='48' r='8' fill='none' stroke='${pc}' stroke-width='1' opacity='.8'/>` +
        `<circle cx='120' cy='48' r='3' fill='${pc}' opacity='.5'/>` +
        [[91,19],[149,19],[91,77],[149,77]].map(([cx,cy]) =>
          `<circle cx='${cx}' cy='${cy}' r='3' fill='none' stroke='${pc}' stroke-width='1' opacity='.55'/>`
        ).join('');
    },

    propeller() {
      const blades = (count) => Array.from({length:count},(_,i)=>{
        const a  = (i*360/count)*Math.PI/180;
        const mx=80, my=48, pr=30;
        const tx=mx+Math.cos(a)*pr*.88, ty=my+Math.sin(a)*pr*.88;
        const cx=mx+Math.cos(a)*pr*.5-Math.sin(a)*pr*.35, cy=my+Math.sin(a)*pr*.5+Math.cos(a)*pr*.35;
        return `<path d='M${mx+Math.cos(a)*5} ${my+Math.sin(a)*5} Q${cx} ${cy} ${tx} ${ty}' stroke='${pc}' stroke-width='2.5' stroke-linecap='round' fill='none'/>`;
      }).join('');
      const n = s.blade_count || 3;
      return `<circle cx='80' cy='48' r='32' fill='none' stroke='${pc}' stroke-width='1' stroke-dasharray='5 4' opacity='.5'/>
              <circle cx='160' cy='48' r='32' fill='none' stroke='${pc}' stroke-width='1' stroke-dasharray='5 4' opacity='.5'/>` +
        blades(n) +
        Array.from({length:n},(_,i)=>{
          const a=(i*360/n)*Math.PI/180;
          const mx=160,my=48,pr=30;
          const tx=mx+Math.cos(a)*pr*.88, ty=my+Math.sin(a)*pr*.88;
          const cx=mx+Math.cos(a)*pr*.5-Math.sin(a)*pr*.35, cy2=my+Math.sin(a)*pr*.5+Math.cos(a)*pr*.35;
          return `<path d='M${mx+Math.cos(a)*5} ${my+Math.sin(a)*5} Q${cx} ${cy2} ${tx} ${ty}' stroke='${pc}' stroke-width='2.5' stroke-linecap='round' fill='none'/>`;
        }).join('') +
        `<circle cx='80' cy='48' r='5' fill='${pf}' stroke='${pc}' stroke-width='1.2'/>
         <circle cx='160' cy='48' r='5' fill='${pf}' stroke='${pc}' stroke-width='1.2'/>`;
    },

    camera() {
      return `<rect x='50' y='22' width='140' height='52' rx='5' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        `<circle cx='120' cy='48' r='26' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        `<circle cx='120' cy='48' r='17' fill='${pm}' stroke='${pc}' stroke-width='1'/>` +
        `<circle cx='120' cy='48' r='8'  fill='${pc}' opacity='.45'/>` +
        `<ellipse cx='113' cy='41' rx='4' ry='2.5' fill='rgba(255,255,255,.5)'/>` +
        `<line x1='50' y1='38' x2='38' y2='52' stroke='${pc}' stroke-width='2' stroke-linecap='round'/>` +
        `<line x1='190' y1='38' x2='202' y2='52' stroke='${pc}' stroke-width='2' stroke-linecap='round'/>`;
    },

    vtx() {
      const fins = [92,100,108,116,124,132,140,148].map(x =>
        `<rect x='${x}' y='32' width='5' height='32' rx='1' fill='${pm}' stroke='${pc}' stroke-width='.8' opacity='.7'/>`
      ).join('');
      return `<rect x='84' y='28' width='72' height='42' rx='4' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        fins +
        `<line x1='110' y1='28' x2='100' y2='10' stroke='${pc}' stroke-width='2' stroke-linecap='round'/>` +
        `<circle cx='100' cy='7' r='5' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        `<circle cx='157' cy='44' r='5' fill='${pc}' opacity='.5'/>` +
        `<circle cx='157' cy='44' r='2.5' fill='rgba(255,255,255,.6)'/>`;
    },

    battery() {
      const cells = s.cell_count_s || 4;
      const W = 180, x0 = 30, y0 = 24, H = 48;
      const dividers = Array.from({length:cells-1},(_,i)=>{
        const x = x0 + W*(i+1)/cells;
        return `<line x1='${x}' y1='${y0+5}' x2='${x}' y2='${y0+H-5}' stroke='${pc}' stroke-width='1' opacity='.5'/>`;
      }).join('');
      return `<rect x='${x0}' y='${y0}' width='${W}' height='${H}' rx='6' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        dividers +
        `<rect x='${x0-10}' y='${y0+H/2-8}' width='12' height='16' rx='3' fill='${pm}' stroke='${pc}' stroke-width='1.2'/>` +
        `<rect x='${x0+4}' y='${y0+6}' width='40' height='14' rx='2' fill='${pm}' opacity='.6'/>` +
        `<text x='${x0+W/2}' y='${y0+H/2+5}' font-size='10' text-anchor='middle' fill='${pc}' font-family='monospace' opacity='.7' font-weight='700'>${cells}S</text>`;
    },

    receiver() {
      return `<rect x='88' y='28' width='64' height='40' rx='3' fill='${pf}' stroke='${pc}' stroke-width='1.5'/>` +
        `<line x1='100' y1='28' x2='92' y2='8'  stroke='${pc}' stroke-width='1.8' stroke-linecap='round'/>` +
        `<line x1='140' y1='28' x2='148' y2='8' stroke='${pc}' stroke-width='1.8' stroke-linecap='round'/>` +
        `<circle cx='92'  cy='5' r='4' fill='${pf}' stroke='${pc}' stroke-width='1.2'/>` +
        `<circle cx='148' cy='5' r='4' fill='${pf}' stroke='${pc}' stroke-width='1.2'/>` +
        `<rect x='96' y='36' width='48' height='16' rx='2' fill='${pm}' stroke='${pc}' stroke-width='.8'/>` +
        `<circle cx='120' cy='44' r='5' fill='${pc}' opacity='.4'/>`;
    },
  };

  const draw = drawings[slot]?.() || '';
  const svg = `<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 240 96' width='240' height='96'>
    <defs>
      <linearGradient id='bg' x1='0' y1='0' x2='0' y2='1'>
        <stop offset='0%' stop-color='${bg1}'/>
        <stop offset='100%' stop-color='${bg2}'/>
      </linearGradient>
    </defs>
    <rect width='240' height='96' fill='url(%23bg)'/>
    ${draw}
  </svg>`;
  return `data:image/svg+xml,${encodeURIComponent(svg)}`;
}

function _expandHex(hex) {
  const h = hex.replace(/^#/, '');
  if (h.length === 3) return '#' + h[0]+h[0]+h[1]+h[1]+h[2]+h[2];
  return '#' + h.padEnd(6, '0').slice(0, 6);
}

function _hexToRgb(hex) {
  const h = hex.replace('#', '');
  return [
    parseInt(h.slice(0, 2), 16) || 0,
    parseInt(h.slice(2, 4), 16) || 0,
    parseInt(h.slice(4, 6), 16) || 0,
  ];
}

function _isLight(r, g, b) {
  return (0.299 * r + 0.587 * g + 0.114 * b) > 160;
}
