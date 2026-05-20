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

  $('catalog-idle').hidden = true;
  $('view-catalog').hidden = false;

  if (window.innerWidth <= 900) {
    $('right-panel').classList.add('panel-open');
    $('mobile-overlay').classList.add('visible');
  }

  updateCompareBar();
  renderParts();
}

export function hideCatalog() {
  $('catalog-idle').hidden = false;
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
    if (_sort === 'price_asc')  return a.price_usd - b.price_usd;
    if (_sort === 'price_desc') return b.price_usd - a.price_usd;
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

    li.innerHTML = `
      <div class="part-card-thumb">${catEmoji(_category)}</div>
      <div class="part-card-info">
        <div class="part-card-brand">${part.brand}</div>
        <div class="part-card-name">${part.name}</div>
        <div class="part-card-specs">${specLine(_category, part)}</div>
      </div>
      <div class="part-card-right">
        <div class="part-card-price">$${part.price_usd.toFixed(2)}</div>
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

    li.addEventListener('click', () => {
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

function catEmoji(cat) {
  return { frame:'🛸',motor:'⚙️',esc:'⚡',fc:'💻',propeller:'🌀',camera:'📷',vtx:'📡',battery:'🔋',receiver:'📻' }[cat] || '•';
}

function specLine(cat, part) {
  const s = part.specs;
  switch (cat) {
    case 'frame':     return `${s.size_mm}mm · ${s.motor_mount_mm}mm mounts · ${s.material}`;
    case 'motor':     return `${s.kv}KV · ${s.stator_size} · max ${s.max_voltage_s}S`;
    case 'esc':       return `${s.amp_rating}A · ${s.protocol} · max ${s.input_voltage_s}S`;
    case 'fc':        return `${s.gyro} · ${s.firmware}`;
    case 'propeller': return `${s.diameter_inch}" · pitch ${s.pitch} · ${s.blade_count}-blade`;
    case 'camera':    return `${s.fov_deg}° FOV · ${s.format}`;
    case 'vtx':       return `${s.power_mw_max}mW · ${s.protocol}`;
    case 'battery':   return `${s.cell_count_s}S · ${s.capacity_mah}mAh · ${s.c_rating}C`;
    case 'receiver':  return `${s.protocol} · ${s.frequency_mhz}MHz`;
    default:          return '';
  }
}
