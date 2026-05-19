import { dispatch, on } from './store.js';
import { init as initBuilder } from './builder.js';
import { init as initCatalog } from './catalog.js';
import { init as initViewer } from './viewer.js';
import { applyFromHash, copyShareLink, saveBuild } from './share.js';

async function main() {
  const res  = await fetch('./data/parts.json');
  const data = await res.json();
  dispatch('INIT', data);

  initBuilder();
  initCatalog();
  initViewer();

  applyFromHash();

  // Header buttons
  document.getElementById('btn-share').addEventListener('click', () => {
    copyShareLink();
    showToast('Link copied!', 'success');
  });

  document.getElementById('btn-save').addEventListener('click', () => {
    const name = saveBuild();
    showToast(`"${name}" saved`, 'success');
  });

  document.getElementById('btn-reset').addEventListener('click', () => {
    if (confirm('Clear the current build?')) {
      dispatch('RESET_BUILD', {});
    }
  });
}

function showToast(message, type = '') {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.className   = `toast${type ? ' ' + type : ''} show`;
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => {
    toast.classList.remove('show');
  }, 2600);
}

main().catch(err => {
  console.error('FPV Builder init failed:', err);
});
