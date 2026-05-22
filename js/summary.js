import { getState, getPartById } from './store.js';
import { evaluate, slotsWithViolations } from './compat.js';

const $ = id => document.getElementById(id);

function setVal(id, value) {
  const main  = $(id);
  const modal = $('modal-' + id);
  if (main)  main.textContent  = value;
  if (modal) modal.textContent = value;
}

export function update() {
  const { build, categories } = getState();
  const selectedParts = Object.values(build)
    .map(id => getPartById(id))
    .filter(Boolean);

  const weight = selectedParts.reduce((sum, p) => sum + (p.weight_g || 0), 0);
  // ×4 motors
  const motor = getPartById(build['motor']);
  const totalWeight = weight + (motor ? motor.weight_g * 3 : 0);

  const price = selectedParts.reduce((sum, p) => sum + (p.price_php || 0), 0);
  const totalPrice = price + (motor ? motor.price_php * 3 : 0);

  setVal('summary-weight',  totalWeight > 0 ? `${Math.round(totalWeight)}g` : '—');
  setVal('summary-price',   totalPrice  > 0 ? `₱${totalPrice.toFixed(2)}` : '—');

  const battery = getPartById(build['battery']);
  setVal('summary-battery', battery
    ? `${battery.specs.cell_count_s}S / ${battery.specs.capacity_mah}mAh`
    : '—');

  const twr = estimateTWR(build);
  setVal('summary-twr', twr ? `${twr.toFixed(1)}:1` : '—');

  const violations = evaluate();
  renderViolations(violations);
  renderSlotViolationBadges();
}

function estimateTWR(build) {
  const motor  = getPartById(build['motor']);
  const battery = getPartById(build['battery']);
  if (!motor || !battery) return null;

  const kv = motor.specs.kv;
  const voltage = battery.specs.voltage_nominal || battery.specs.cell_count_s * 3.7;
  const rpm = kv * voltage;
  // rough thrust: 4 motors, ~1g thrust per 1000 rpm (very approximate)
  const thrustG = (rpm / 1000) * 4 * 1.2;

  const { build: b } = getState();
  const parts = Object.values(b).map(id => getPartById(id)).filter(Boolean);
  const totalW = parts.reduce((s, p) => s + p.weight_g, 0) + motor.weight_g * 3;
  if (totalW === 0) return null;

  return thrustG / totalW;
}

function renderViolations(violations) {
  ['compat-violations', 'modal-compat-violations'].forEach(id => {
    const el = $(id);
    if (!el) return;
    if (violations.length === 0) {
      el.hidden = true;
      el.innerHTML = '';
    } else {
      el.hidden = false;
      el.innerHTML = violations.map(v =>
        `<div class="violation-item">⚠ ${v.message}</div>`
      ).join('');
    }
  });
}

function renderSlotViolationBadges() {
  const bad = slotsWithViolations();
  document.querySelectorAll('.slot-item').forEach(el => {
    el.classList.toggle('has-violation', bad.has(el.dataset.slot));
  });
}
