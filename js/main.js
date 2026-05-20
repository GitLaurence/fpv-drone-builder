import { dispatch, on, getState } from './store.js';
import { init as initBuilder } from './builder.js';
import { init as initCatalog } from './catalog.js';
import { init as initBlueprint } from './blueprint.js';
import { init as initCompare } from './compare.js';
import { init as initSaves } from './saves.js';
import { applyFromHash, copyShareLink } from './share.js';

const TOTAL_SLOTS = 9;

async function main() {
  const res  = await fetch('./data/parts.json');
  const data = await res.json();
  dispatch('INIT', data);

  initBuilder();
  initCatalog();
  initBlueprint();
  initCompare(() => {});
  initSaves();
  applyFromHash();
  initMobileDrawer();

  // Header actions
  document.getElementById('btn-share').addEventListener('click', () => {
    copyShareLink();
    showToast('Share link copied!', 'success');
  });

  document.getElementById('btn-reset')?.addEventListener('click', () => {
    if (confirm('Clear the current build?')) dispatch('RESET_BUILD', {});
  });

  // Update progress + hint on build changes
  on('build:changed', ({ build }) => {
    updateProgress(build);
    updateHint(build);
  });

  on('slot:active', ({ slot }) => {
    updateBlueprintHint(slot);
  });

  updateProgress(getState().build);
  updateHint(getState().build);
}

// ── Progress bars ────────────────────────────────────

function updateProgress(build) {
  const count = Object.keys(build).length;
  const pct   = (count / TOTAL_SLOTS) * 100;

  const fill  = document.getElementById('build-progress-fill');
  const label = document.getElementById('build-progress-count');
  if (fill)  fill.style.width  = `${pct}%`;
  if (label) label.textContent = `${count} / ${TOTAL_SLOTS}`;

  const dfill  = document.getElementById('drawer-progress-fill');
  const dlabel = document.getElementById('drawer-progress-count');
  const dtext  = document.getElementById('drawer-status-text');
  if (dfill)  dfill.style.width  = `${pct}%`;
  if (dlabel) dlabel.textContent = `${count} / ${TOTAL_SLOTS}`;
  if (dtext) {
    if      (count === 0)          dtext.textContent = 'Tap to configure';
    else if (count === TOTAL_SLOTS) dtext.textContent = '✓ Build complete';
    else                            dtext.textContent = `${count} of ${TOTAL_SLOTS} selected`;
  }
}

// ── Blueprint HUD hint ───────────────────────────────

function updateHint(build) {
  const hint  = document.getElementById('blueprint-hint');
  if (!hint) return;
  const count = Object.keys(build).length;
  if      (count === 0)           hint.textContent = 'Click a component to select parts';
  else if (count === TOTAL_SLOTS) hint.textContent = '✓ Build complete';
  else                            hint.textContent = `${count} / ${TOTAL_SLOTS} components selected`;
}

function updateBlueprintHint(slot) {
  const hint = document.getElementById('blueprint-hint');
  if (!hint) return;
  if (slot) {
    const { categories } = getState();
    const cat = categories.find(c => c.id === slot);
    hint.textContent = cat ? `Selecting: ${cat.label}` : 'Selecting part…';
  } else {
    updateHint(getState().build);
  }
}

// ── Mobile drawer (left panel) ───────────────────────

function initMobileDrawer() {
  const panel   = document.getElementById('left-panel');
  const overlay = document.getElementById('mobile-overlay');
  const handle  = document.getElementById('drawer-handle');
  const rightPanel = document.getElementById('right-panel');

  function isMobile() { return window.innerWidth <= 900; }

  function openDrawer() {
    panel.classList.add('drawer-open');
    if (!rightPanel.classList.contains('panel-open')) {
      overlay.classList.add('visible');
    }
  }

  function closeDrawer() {
    panel.classList.remove('drawer-open');
    if (!rightPanel.classList.contains('panel-open')) {
      overlay.classList.remove('visible');
    }
  }

  handle?.addEventListener('click', () => {
    if (!isMobile()) return;
    panel.classList.contains('drawer-open') ? closeDrawer() : openDrawer();
  });

  // Overlay closes whichever panel is open
  overlay?.addEventListener('click', () => {
    rightPanel.classList.remove('panel-open');
    panel.classList.remove('drawer-open');
    overlay.classList.remove('visible');
    dispatch('SET_ACTIVE_SLOT', { slot: null });
  });

  // Auto-open left drawer when slot activated on mobile
  on('slot:active', ({ slot }) => {
    if (!isMobile()) return;
    if (slot) {
      // Right panel opens (handled by catalog.js showCatalog)
      // Keep left panel open behind it
      openDrawer();
    }
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && isMobile()) {
      rightPanel.classList.remove('panel-open');
      panel.classList.remove('drawer-open');
      overlay.classList.remove('visible');
    }
  });
}

// ── Toast ────────────────────────────────────────────

export function showToast(message, type = '') {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.className   = `toast${type ? ' ' + type : ''} show`;
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => toast.classList.remove('show'), 2800);
}

main().catch(err => console.error('FPV Builder init failed:', err));
