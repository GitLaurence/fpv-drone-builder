import { dispatch, on, getState } from './store.js';
import { init as initBuilder } from './builder.js';
import { init as initCatalog } from './catalog.js';
import { init as initViewer, getRenderer } from './viewer.js';
import { init as initCompare } from './compare.js';
import { init as initSaves } from './saves.js';
import { applyFromHash, copyShareLink } from './share.js';
import { setRendererGetter, exportBuildCard } from './export.js';

const TOTAL_SLOTS = 9;

async function main() {
  const res  = await fetch('./data/parts.json');
  const data = await res.json();
  dispatch('INIT', data);

  initBuilder();
  initCatalog();
  initViewer();

  setRendererGetter(getRenderer);
  initCompare(() => {});
  initSaves();
  applyFromHash();
  initMobileDrawer();

  // Header actions
  document.getElementById('btn-share').addEventListener('click', () => {
    copyShareLink();
    showToast('Share link copied!', 'success');
  });

  document.getElementById('btn-reset').addEventListener('click', () => {
    if (confirm('Clear the current build?')) dispatch('RESET_BUILD', {});
  });

  document.getElementById('btn-export').addEventListener('click', () => {
    exportBuildCard();
    showToast('Build card exported!', 'success');
  });

  // Update progress bar whenever build changes
  on('build:changed', ({ build }) => updateProgress(build));

  // Trigger an initial progress update
  updateProgress(getState().build);
}

// ── Progress bar ────────────────────────────────────

function updateProgress(build) {
  const count = Object.keys(build).length;
  const pct   = (count / TOTAL_SLOTS) * 100;

  // Desktop bar
  const fill  = document.getElementById('build-progress-fill');
  const label = document.getElementById('build-progress-count');
  if (fill)  fill.style.width  = `${pct}%`;
  if (label) label.textContent = `${count} / ${TOTAL_SLOTS}`;

  // Mobile drawer bar
  const dfill  = document.getElementById('drawer-progress-fill');
  const dlabel = document.getElementById('drawer-progress-count');
  const dtext  = document.getElementById('drawer-status-text');
  if (dfill)  dfill.style.width  = `${pct}%`;
  if (dlabel) dlabel.textContent = `${count} / ${TOTAL_SLOTS}`;
  if (dtext) {
    if (count === 0)               dtext.textContent = 'Tap to configure build';
    else if (count === TOTAL_SLOTS) dtext.textContent = '✓ Build complete';
    else                            dtext.textContent = `${count} of ${TOTAL_SLOTS} parts selected`;
  }
}

// ── Mobile drawer ───────────────────────────────────

function initMobileDrawer() {
  const panel   = document.getElementById('side-panel');
  const overlay = document.getElementById('mobile-overlay');
  const handle  = document.getElementById('drawer-handle');

  function isMobile() { return window.innerWidth <= 767; }

  function openDrawer() {
    panel.classList.add('drawer-open');
    overlay.classList.add('visible');
    overlay.setAttribute('aria-hidden', 'false');
  }

  function closeDrawer() {
    panel.classList.remove('drawer-open');
    overlay.classList.remove('visible');
    overlay.setAttribute('aria-hidden', 'true');
  }

  function toggleDrawer() {
    if (panel.classList.contains('drawer-open')) closeDrawer();
    else openDrawer();
  }

  handle?.addEventListener('click', () => {
    if (isMobile()) toggleDrawer();
  });

  overlay?.addEventListener('click', closeDrawer);

  // Auto-open drawer when a slot becomes active on mobile
  on('slot:active', ({ slot }) => {
    if (slot && isMobile()) openDrawer();
  });

  // Close drawer (but stay in slot-list view) after selecting a part on mobile
  on('build:changed', () => {
    // Keep drawer open after part selection so user can pick next slot
  });

  // Keyboard: Escape to close
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && isMobile()) closeDrawer();
  });
}

// ── Toast ───────────────────────────────────────────

export function showToast(message, type = '') {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.className   = `toast${type ? ' ' + type : ''} show`;
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => toast.classList.remove('show'), 2800);
}

main().catch(err => console.error('FPV Builder init failed:', err));
