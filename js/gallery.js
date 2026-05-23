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
  const headerBg   = `rgba(${r},${g},${b},0.1)`;
  const borderClr  = `rgba(${r},${g},${b},0.28)`;
  const iconClr    = _isLight(r, g, b) ? `rgba(${r},${g},${b},0.7)` : color;

  const domain   = BRAND_DOMAINS[part.brand];
  const favicon  = domain
    ? `<img class="gallery-favicon" src="https://www.google.com/s2/favicons?domain=${domain}&sz=32" alt="${part.brand}" loading="lazy">`
    : `<span class="gallery-favicon-text">${(part.brand || '?')[0]}</span>`;

  const imgTag   = part.image_url
    ? `<img class="gallery-product-img" src="${part.image_url}" alt="${part.name}" loading="lazy">`
    : '';

  const spec     = _keySpec(slot, part);
  const price    = part.price_php ? `₱${part.price_php.toLocaleString()}` : '';
  const weight   = part.weight_g  ? `${part.weight_g}g` : '';

  return `<div class="gallery-card${focused_}" data-slot="${slot}"
               style="--gc:${color};--gcr:${r};--gcg:${g};--gcb:${b}">
    <a class="gallery-card-visual" href="${part.buy_url || '#'}" target="_blank"
       rel="noopener" style="background:${headerBg};" title="View on retailer site">
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
