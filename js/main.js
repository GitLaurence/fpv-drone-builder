import { dispatch, on, getState } from './store.js';
import { init as initBuilder, closeSlot } from './builder.js';
import { init as initStepper } from './stepper.js';
import { init as initCatalog } from './catalog.js';
import { init as initBlueprint } from './blueprint.js';
import { init as initCompare } from './compare.js';
import { init as initSaves } from './saves.js';
import { applyFromHash, copyShareLink } from './share.js';
import { init as initGallery } from './gallery.js';

const TOTAL_SLOTS = 9;

async function main() {
  const res  = await fetch('./data/parts.json');
  const data = await res.json();
  dispatch('INIT', data);

  initBuilder();
  initCatalog();
  initBlueprint();
  initGallery();
  initCompare(() => {});
  initSaves();
  initStepper();
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

  const helpModal = document.getElementById('modal-help');
  document.getElementById('btn-help').addEventListener('click', () => helpModal.showModal());
  document.getElementById('modal-help-close').addEventListener('click', () => helpModal.close());
  helpModal.addEventListener('click', e => { if (e.target === helpModal) helpModal.close(); });

  const statsModal = document.getElementById('modal-stats');
  document.getElementById('btn-stats')?.addEventListener('click', e => {
    e.stopPropagation(); // don't toggle the drawer
    statsModal.showModal();
  });
  document.getElementById('modal-stats-close')?.addEventListener('click', () => statsModal.close());
  statsModal?.addEventListener('click', e => { if (e.target === statsModal) statsModal.close(); });

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

  const mfill  = document.getElementById('modal-build-progress-fill');
  const mlabel = document.getElementById('modal-build-progress-count');
  const mcount = document.getElementById('modal-stats-count');
  if (mfill)  mfill.style.width  = `${pct}%`;
  if (mlabel) mlabel.textContent = `${count} / ${TOTAL_SLOTS}`;
  if (mcount) mcount.textContent = count > 0 ? `${count} / ${TOTAL_SLOTS}` : '';

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
  const panel       = document.getElementById('left-panel');
  const overlay     = document.getElementById('mobile-overlay');
  const handle      = document.getElementById('drawer-handle');
  const rightPanel  = document.getElementById('right-panel');
  const rightHandle = document.getElementById('right-drawer-handle');
  const closeBtn    = document.getElementById('btn-right-close');

  function isMobile() { return window.innerWidth <= 900; }

  function openDrawer() {
    panel.classList.add('drawer-open');
    // Overlay is managed by catalog.js — don't interfere here
  }

  function closeDrawer() {
    panel.classList.remove('drawer-open');
  }

  // ── Left drawer swipe gesture ─────────────────────
  let _swipeStartY = 0;
  let _didSwipe    = false;

  handle?.addEventListener('touchstart', e => {
    if (!isMobile()) return;
    _swipeStartY = e.touches[0].clientY;
    _didSwipe    = false;
  }, { passive: true });

  handle?.addEventListener('touchend', e => {
    if (!isMobile()) return;
    const dy = e.changedTouches[0].clientY - _swipeStartY;
    if (Math.abs(dy) > 30) {
      _didSwipe = true;
      if (dy > 0) closeDrawer();
      else openDrawer();
    }
  }, { passive: true });

  handle?.addEventListener('click', () => {
    if (!isMobile()) return;
    if (_didSwipe) { _didSwipe = false; return; }
    panel.classList.contains('drawer-open') ? closeDrawer() : openDrawer();
  });

  // ── Right panel (catalog) swipe-down to dismiss ───
  let _rightSwipeStart = 0;

  rightHandle?.addEventListener('touchstart', e => {
    if (!isMobile()) return;
    _rightSwipeStart = e.touches[0].clientY;
  }, { passive: true });

  rightHandle?.addEventListener('touchend', e => {
    if (!isMobile()) return;
    const dy = e.changedTouches[0].clientY - _rightSwipeStart;
    if (dy > 50) closeSlot();
  }, { passive: true });

  // Right panel close button
  closeBtn?.addEventListener('click', () => {
    if (!isMobile()) return;
    closeSlot();
  });

  // Overlay tap — close the catalog popup
  overlay?.addEventListener('click', () => {
    closeSlot();
    overlay.classList.remove('visible');
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && isMobile()) {
      closeSlot();
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
