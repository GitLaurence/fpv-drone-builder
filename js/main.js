import { dispatch } from './store.js';
import { init as initBuilder } from './builder.js';
import { init as initCatalog } from './catalog.js';
import { init as initViewer, getRenderer } from './viewer.js';
import { init as initCompare } from './compare.js';
import { init as initSaves } from './saves.js';
import { applyFromHash, copyShareLink } from './share.js';
import { setRendererGetter, exportBuildCard } from './export.js';

async function main() {
  const res  = await fetch('./data/parts.json');
  const data = await res.json();
  dispatch('INIT', data);

  initBuilder();
  initCatalog();
  initViewer();

  // Pass renderer to export module after viewer is ready
  setRendererGetter(getRenderer);

  // Compare needs a callback to refresh catalog UI
  // catalog.js manages its own update via Compare.init callback
  initCompare(() => {}); // catalog.js handles its own re-renders

  initSaves();

  applyFromHash();

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
}

export function showToast(message, type = '') {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.className   = `toast${type ? ' ' + type : ''} show`;
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => toast.classList.remove('show'), 2800);
}

main().catch(err => console.error('FPV Builder init failed:', err));
