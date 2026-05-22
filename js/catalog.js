import { getState, getPartsByCategory, getPartById, dispatch } from './store.js';
import { closeSlot } from './builder.js';
import * as Compare from './compare.js';

const UTM = '?ref=fpvbuilder&utm_source=fpvbuilder&utm_medium=referral';

let _category      = null;
let _search        = '';
let _sort          = 'name';
let _filterStock   = false;
let _compareMode   = false;

const $ = id => document.getElementById(id);

export function init() {
  $('btn-back').addEventListener('click', closeSlot);
  $('catalog-search').addEventListener('input', e => { _search = e.target.value.toLowerCase(); renderParts(); });
  $('catalog-sort').addEventListener('change', e => { _sort = e.target.value; renderParts(); });

  $('filter-pills').addEventListener('click', e => {
    const pill = e.target.closest('.pill[data-filter]');
    if (!pill) return;
    _filterStock = pill.dataset.filter === 'in_stock';
    document.querySelectorAll('.pill[data-filter]').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    renderParts();
  });

  $('btn-compare-toggle').addEventListener('click', () => {
    _compareMode = !_compareMode;
    $('btn-compare-toggle').classList.toggle('active', _compareMode);
    $('btn-compare-toggle').textContent = _compareMode ? 'Done' : 'Compare';
    if (!_compareMode) Compare.clear();
    renderParts();
    updateCompareBar();
  });
}

export function showCatalog(categoryId) {
  _category    = categoryId;
  _search      = '';
  _filterStock = false;
  _sort        = 'name';
  _compareMode = false;

  $('catalog-search').value = '';
  $('catalog-sort').value   = 'name';
  $('btn-compare-toggle').classList.remove('active');
  $('btn-compare-toggle').textContent = 'Compare';
  Compare.setCategory(categoryId);
  Compare.clear();

  document.querySelectorAll('.pill[data-filter]').forEach(p =>
    p.classList.toggle('active', p.dataset.filter === 'all')
  );

  const cat = getState().categories.find(c => c.id === categoryId);
  $('catalog-slot-label').textContent = cat ? `Select ${cat.label}` : 'Select Part';

  $('view-catalog').hidden = false;

  if (window.innerWidth <= 900) {
    $('right-panel').classList.add('panel-open');
    $('mobile-overlay').classList.add('visible');
  }

  updateCompareBar();
  renderParts();
}

export function hideCatalog() {
  $('view-catalog').hidden = true;
  _category    = null;
  _compareMode = false;
  Compare.clear();

  if (window.innerWidth <= 900) {
    $('right-panel').classList.remove('panel-open');
    $('mobile-overlay').classList.remove('visible');
  }
}

// ── Part list rendering ───────────────────────────────

function renderParts() {
  if (!_category) return;

  let parts = getPartsByCategory(_category);
  if (_filterStock) parts = parts.filter(p => p.in_stock);
  if (_search) {
    parts = parts.filter(p =>
      p.name.toLowerCase().includes(_search) ||
      p.brand.toLowerCase().includes(_search)
    );
  }

  parts = [...parts].sort((a, b) => {
    if (_sort === 'price_asc')  return a.price_php - b.price_php;
    if (_sort === 'price_desc') return b.price_php - a.price_php;
    if (_sort === 'weight_asc') return a.weight_g - b.weight_g;
    return a.name.localeCompare(b.name);
  });

  const selectedId = getState().build[_category] || null;
  const list = $('part-list');

  if (!parts.length) {
    list.innerHTML = `<li class="parts-empty">No parts match your filters</li>`;
    return;
  }

  list.innerHTML = '';
  parts.forEach(part => {
    const isSelected  = part.id === selectedId;
    const isComparing = Compare.isComparing(part.id);
    const li = document.createElement('li');

    li.className = [
      'part-card',
      isSelected  ? 'selected'   : '',
      isComparing ? 'in-compare' : '',
      !part.in_stock ? 'out-of-stock' : '',
    ].filter(Boolean).join(' ');
    li.setAttribute('role', 'button');
    li.setAttribute('tabindex', '0');

    const extraLinks = _category === 'frame' ? thingiLink(part) : '';
    const detailHtml = _category === 'fc' ? fcDetailSection(part) : '';

    li.innerHTML = `
      <div class="part-card-thumb">${catEmoji(_category)}</div>
      <div class="part-card-info">
        <div class="part-card-brand">${part.brand}</div>
        <div class="part-card-name">${part.name}</div>
        <div class="part-card-specs">${specLine(_category, part)}</div>
        ${detailHtml}
        <div class="part-card-buy">${buyLinks(part)}${extraLinks}</div>
      </div>
      <div class="part-card-right">
        <div class="part-card-price">₱${part.price_php.toFixed(2)}</div>
        <div class="part-card-weight">${part.weight_g}g</div>
        <div class="part-card-stock ${part.in_stock ? 'in-stock' : 'out-of-stock-label'}">
          ${part.in_stock ? '● In Stock' : '○ Out of Stock'}
        </div>
      </div>
      ${isSelected && !_compareMode
        ? '<div class="part-card-selected-check">✓</div>'
        : ''}
      ${_compareMode
        ? `<div class="compare-check ${isComparing ? 'active' : ''}">${isComparing ? '✓' : '+'}</div>`
        : ''}
    `;

    li.addEventListener('click', e => {
      if (e.target.closest('.part-buy-link')) return;
      if (_compareMode) {
        Compare.toggle(part.id);
        renderParts();
        updateCompareBar();
      } else {
        selectPart(part.id);
      }
    });
    li.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        _compareMode ? Compare.toggle(part.id) : selectPart(part.id);
      }
    });

    list.appendChild(li);
  });
}

function selectPart(partId) {
  if (!_category) return;
  const already = getState().build[_category] === partId;
  dispatch('SELECT_PART', { slot: _category, partId: already ? null : partId });
}

// ── Compare bar ───────────────────────────────────────

function updateCompareBar() {
  const bar = $('compare-bar');
  const count = Compare.getCount();

  if (!_compareMode) { bar.hidden = true; return; }

  bar.hidden = false;
  const partsEl = $('compare-bar-parts');
  const list    = Compare.getList();
  partsEl.innerHTML = list.map(id => {
    const p = getPartById(id);
    return p ? `<span class="compare-chip">${p.name} <button class="compare-chip-remove" data-id="${id}">✕</button></span>` : '';
  }).join('');

  partsEl.querySelectorAll('.compare-chip-remove').forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      Compare.toggle(btn.dataset.id);
      renderParts();
      updateCompareBar();
    });
  });

  const openBtn = $('btn-compare-open');
  openBtn.textContent = `Compare (${count})`;
  openBtn.disabled    = count < 2;
}

// ── Helpers ───────────────────────────────────────────

const STORES = [
  { name: 'GetFPV',  search: q => `https://www.getfpv.com/catalogsearch/result/?q=${q}` },
  { name: 'RDQ',     search: q => `https://www.racedayquads.com/search?type=product&q=${q}` },
  { name: 'Rotor Riot', search: q => `https://rotorriot.com/search?q=${q}` },
];

function buyLinks(part) {
  const q = encodeURIComponent(`${part.brand} ${part.name}`);
  return STORES.map(s =>
    `<a class="part-buy-link" href="${s.search(q)}" target="_blank" rel="noopener noreferrer">${s.name} ↗</a>`
  ).join('');
}

function catEmoji(cat) {
  return { frame:'🛸',motor:'⚙️',esc:'⚡',fc:'💻',propeller:'🌀',camera:'📷',vtx:'📡',battery:'🔋',receiver:'📻' }[cat] || '•';
}

function specLine(cat, part) {
  const s = part.specs;
  switch (cat) {
    case 'frame':     return `${s.size_mm}mm · ${s.motor_mount_mm}mm mounts · ${s.standoff_height_mm ? s.standoff_height_mm + 'mm standoffs · ' : ''}${s.material}`;
    case 'motor':     return `${s.kv}KV · ${s.stator_size} · ${s.min_voltage_s ? s.min_voltage_s + '–' : ''}${s.max_voltage_s}S`;
    case 'esc':       return `${s.amp_rating}A · ${s.protocol} · max ${s.input_voltage_s}S`;
    case 'fc':        return `${s.gyro} · ${s.firmware} · ${s.uart_count ? s.uart_count + ' UARTs' : ''}`;
    case 'propeller': return `${s.diameter_inch}" · pitch ${s.pitch} · ${s.blade_count}-blade`;
    case 'camera':    return `${s.fov_deg}° FOV · ${s.format}`;
    case 'vtx':       return `${s.power_mw_max}mW · ${s.protocol}`;
    case 'battery':   return `${s.cell_count_s}S · ${s.capacity_mah}mAh · ${s.c_rating}C`;
    case 'receiver':  return `${s.protocol} · ${s.frequency_mhz}MHz`;
    default:          return '';
  }
}

function fcDetailSection(part) {
  const s = part.specs;
  const diagLink = s.diagram_url
    ? `<a class="part-card-diagram-link part-buy-link" href="${s.diagram_url}" target="_blank" rel="noopener noreferrer">📋 Wiring Diagram ↗</a>`
    : '';
  return `
    <div class="part-card-detail">
      <div class="part-card-detail-row">
        <span class="fc-badge">UARTs&nbsp;<strong>${s.uart_count ?? '–'}</strong></span>
        <span class="fc-badge">5V&nbsp;pads&nbsp;<strong>${s['5v_pad_count'] ?? '–'}</strong></span>
        <span class="fc-badge">${s.curr_sensor ? '✓ Curr' : '✗ Curr'}</span>
        <span class="fc-badge">${s.barometer ? '✓ Baro' : '✗ Baro'}</span>
        ${diagLink}
      </div>
    </div>
  `;
}

function thingiLink(part) {
  const url = part.specs.thingiverse_url;
  if (!url) return '';
  return `<a class="part-buy-link part-thingi-link" href="${url}" target="_blank" rel="noopener noreferrer">🖨 3D Prints ↗</a>`;
}
