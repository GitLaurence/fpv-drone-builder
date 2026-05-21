import { getState, getPartById, dispatch, on } from './store.js';
import { showCatalog, hideCatalog } from './catalog.js';
import { update as updateSummary } from './summary.js';

const SLOT_ICONS = {
  frame:     '🛸',
  motor:     '⚙️',
  esc:       '⚡',
  fc:        '💻',
  propeller: '🌀',
  camera:    '📷',
  vtx:       '📡',
  battery:   '🔋',
  receiver:  '📻',
};

export function init() {
  renderSlotList();
  bindPresets();

  on('build:changed', () => {
    renderSlotList();
    updateSummary();
  });

  on('slot:active', ({ slot }) => {
    document.querySelectorAll('.slot-item').forEach(el => {
      el.classList.toggle('active', el.dataset.slot === slot);
    });
  });
}

function renderSlotList() {
  const { categories, build } = getState();
  const list = document.getElementById('slot-list');
  list.innerHTML = '';

  categories.forEach(cat => {
    const partId = build[cat.id];
    const part = partId ? getPartById(partId) : null;
    const li = document.createElement('li');
    li.className = 'slot-item' + (part ? ' slot-filled' : ' slot-empty');
    li.dataset.slot = cat.id;
    li.setAttribute('role', 'button');
    li.setAttribute('tabindex', '0');
    li.setAttribute('aria-label', `${cat.label}: ${part ? part.name : 'empty'}`);

    li.innerHTML = `
      <div class="slot-icon">${SLOT_ICONS[cat.id] || '•'}</div>
      <div class="slot-info">
        <div class="slot-category">${cat.label}</div>
        <div class="slot-part-name">${part ? part.name : 'Click to select…'}</div>
        ${part ? `<div class="slot-meta">${partMeta(cat.id, part)}</div>` : ''}
      </div>
      <div class="slot-actions">
        ${part ? `<button class="slot-clear-btn" data-slot="${cat.id}" aria-label="Remove ${cat.label}" title="Remove">✕</button>` : ''}
        <svg class="slot-arrow" viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 4l4 4-4 4"/></svg>
      </div>
    `;

    li.addEventListener('click', e => {
      if (e.target.closest('.slot-clear-btn')) return;
      openSlot(cat.id);
    });
    li.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openSlot(cat.id); }
    });

    const clearBtn = li.querySelector('.slot-clear-btn');
    if (clearBtn) {
      clearBtn.addEventListener('click', e => {
        e.stopPropagation();
        dispatch('SELECT_PART', { slot: cat.id, partId: null });
      });
    }

    list.appendChild(li);
  });
}

function partMeta(categoryId, part) {
  const s = part.specs;
  switch (categoryId) {
    case 'frame':     return `${s.size_mm}mm · ${s.standoff_height_mm ? s.standoff_height_mm + 'mm standoffs · ' : ''}${s.material || ''}`;
    case 'motor':     return `${s.kv}KV · ${s.stator_size} · ${s.min_voltage_s ? s.min_voltage_s + '–' : ''}${s.max_voltage_s}S`;
    case 'esc':       return `${s.amp_rating}A · ${s.protocol}`;
    case 'fc':        return `${s.gyro} · ${s.uart_count ? s.uart_count + ' UARTs' : s.firmware}`;
    case 'propeller': return `${s.diameter_inch}" · ${s.blade_count}-blade`;
    case 'camera':    return `${s.fov_deg}° · ${s.format}`;
    case 'vtx':       return `${s.power_mw_max}mW · ${s.protocol}`;
    case 'battery':   return `${s.cell_count_s}S · ${s.capacity_mah}mAh`;
    case 'receiver':  return `${s.protocol} · ${s.frequency_mhz}MHz`;
    default:          return '';
  }
}

export function openSlot(slotId) {
  dispatch('SET_ACTIVE_SLOT', { slot: slotId });
  showCatalog(slotId);
}

export function closeSlot() {
  dispatch('SET_ACTIVE_SLOT', { slot: null });
  hideCatalog();
}

function bindPresets() {
  document.querySelectorAll('.btn-preset').forEach(btn => {
    btn.addEventListener('click', () => {
      const { presets } = getState();
      const key = btn.dataset.preset;
      const preset = presets[key];
      if (!preset) return;
      dispatch('LOAD_PRESET', { parts: preset.parts });
      document.getElementById('build-name').value = preset.name;
    });
  });
}
