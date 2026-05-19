import { getState, getPartsByCategory, getPartById, dispatch } from './store.js';
import { closeSlot } from './builder.js';

let _currentCategory = null;
let _searchQuery     = '';
let _sortMode        = 'name';
let _filterStock     = false;

const $ = id => document.getElementById(id);

export function init() {
  $('btn-back').addEventListener('click', closeSlot);
  $('catalog-search').addEventListener('input', e => {
    _searchQuery = e.target.value.toLowerCase();
    renderParts();
  });
  $('catalog-sort').addEventListener('change', e => {
    _sortMode = e.target.value;
    renderParts();
  });
  $('filter-pills').addEventListener('click', e => {
    const pill = e.target.closest('.pill');
    if (!pill) return;
    _filterStock = pill.dataset.filter === 'in_stock';
    document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    renderParts();
  });
}

export function showCatalog(categoryId) {
  _currentCategory = categoryId;
  _searchQuery = '';
  _filterStock = false;
  _sortMode = 'name';

  $('catalog-search').value = '';
  $('catalog-sort').value = 'name';
  document.querySelectorAll('.pill').forEach(p => {
    p.classList.toggle('active', p.dataset.filter === 'all');
  });

  const { categories } = getState();
  const cat = categories.find(c => c.id === categoryId);
  $('catalog-slot-label').textContent = cat ? `Select ${cat.label}` : 'Select Part';

  $('view-slots').hidden   = true;
  $('view-catalog').hidden = false;

  renderParts();
}

export function hideCatalog() {
  $('view-slots').hidden   = false;
  $('view-catalog').hidden = true;
  _currentCategory = null;
}

function renderParts() {
  if (!_currentCategory) return;

  let parts = getPartsByCategory(_currentCategory);

  if (_filterStock) parts = parts.filter(p => p.in_stock);

  if (_searchQuery) {
    parts = parts.filter(p =>
      p.name.toLowerCase().includes(_searchQuery) ||
      p.brand.toLowerCase().includes(_searchQuery)
    );
  }

  parts = [...parts].sort((a, b) => {
    switch (_sortMode) {
      case 'price_asc':  return a.price_usd - b.price_usd;
      case 'price_desc': return b.price_usd - a.price_usd;
      case 'weight_asc': return a.weight_g  - b.weight_g;
      default:           return a.name.localeCompare(b.name);
    }
  });

  const selectedId = getState().build[_currentCategory] || null;
  const list = $('part-list');

  if (parts.length === 0) {
    list.innerHTML = `<li style="color:var(--text-muted);font-size:0.85rem;padding:1rem 0;text-align:center;">No parts found</li>`;
    return;
  }

  list.innerHTML = '';
  parts.forEach(part => {
    const li = document.createElement('li');
    li.className = 'part-card' +
      (part.id === selectedId ? ' selected' : '') +
      (!part.in_stock ? ' out-of-stock' : '');
    li.setAttribute('role', 'button');
    li.setAttribute('tabindex', '0');

    li.innerHTML = `
      <div class="part-card-thumb">${categoryEmoji(_currentCategory)}</div>
      <div class="part-card-info">
        <div class="part-card-brand">${part.brand}</div>
        <div class="part-card-name">${part.name}</div>
        <div class="part-card-specs">${specLine(_currentCategory, part)}</div>
      </div>
      <div class="part-card-right">
        <div class="part-card-price">$${part.price_usd.toFixed(2)}</div>
        <div class="part-card-weight">${part.weight_g}g</div>
        <div class="part-card-stock ${part.in_stock ? 'in-stock' : 'out-of-stock-label'}">
          ${part.in_stock ? '● In Stock' : '○ Out of Stock'}
        </div>
      </div>
      ${part.id === selectedId
        ? '<div class="part-card-selected-check">✓</div>'
        : ''}
    `;

    li.addEventListener('click', () => selectPart(part.id));
    li.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); selectPart(part.id); }
    });

    list.appendChild(li);
  });
}

function selectPart(partId) {
  if (!_currentCategory) return;
  const alreadySelected = getState().build[_currentCategory] === partId;
  dispatch('SELECT_PART', {
    slot: _currentCategory,
    partId: alreadySelected ? null : partId,
  });
}

function categoryEmoji(cat) {
  const map = {
    frame:'🛸', motor:'⚙️', esc:'⚡', fc:'💻',
    propeller:'🌀', camera:'📷', vtx:'📡', battery:'🔋', receiver:'📻'
  };
  return map[cat] || '•';
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
