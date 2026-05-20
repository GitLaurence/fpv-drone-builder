import { getState, getPartById, on } from './store.js';
import { openSlot } from './builder.js';

const ICONS = {
  frame: '🛸', motor: '⚙️', esc: '⚡', fc: '💻',
  propeller: '🌀', camera: '📷', vtx: '📡', battery: '🔋', receiver: '📻',
};

let _step = 0;

export function init() {
  const { categories } = getState();

  document.getElementById('btn-step-prev')?.addEventListener('click', () => {
    if (_step > 0) goToStep(_step - 1);
  });

  document.getElementById('btn-step-next')?.addEventListener('click', () => {
    if (_step < categories.length - 1) goToStep(_step + 1);
  });

  on('slot:active', ({ slot }) => {
    if (!slot) return;
    const idx = categories.findIndex(c => c.id === slot);
    if (idx >= 0) _step = idx;
    render();
  });

  on('build:changed', () => render());

  render();
}

function goToStep(idx) {
  _step = idx;
  const { categories } = getState();
  openSlot(categories[idx].id);
}

function render() {
  const { categories, build } = getState();
  const cat = categories[_step];
  if (!cat) return;

  const partId = build[cat.id];
  const part   = partId ? getPartById(partId) : null;

  const iconEl  = document.getElementById('step-nav-icon');
  const labelEl = document.getElementById('step-nav-label');
  const subEl   = document.getElementById('step-nav-sub');
  const dotsEl  = document.getElementById('step-nav-dots');
  const prevBtn = document.getElementById('btn-step-prev');
  const nextBtn = document.getElementById('btn-step-next');

  if (iconEl)  iconEl.textContent  = ICONS[cat.id] || '•';
  if (labelEl) labelEl.textContent = cat.label;
  if (subEl) {
    subEl.textContent = part ? part.name : 'Not selected';
    subEl.classList.toggle('step-filled', !!part);
  }
  if (prevBtn) prevBtn.disabled = _step === 0;
  if (nextBtn) nextBtn.disabled = _step === categories.length - 1;

  if (dotsEl) {
    dotsEl.innerHTML = categories.map((c, i) => {
      const filled = !!build[c.id];
      const active = i === _step;
      return `<span class="step-dot${active ? ' active' : ''}${filled ? ' filled' : ''}"></span>`;
    }).join('');
  }
}
