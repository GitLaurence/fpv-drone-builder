import { dispatch, getState } from './store.js';
import { encodeBuild } from './share.js';

const STORAGE_KEY = 'fpv_builds';

export function init() {
  document.getElementById('btn-my-builds').addEventListener('click', open);
  document.getElementById('modal-saves-close').addEventListener('click', close);
  document.getElementById('modal-saves').addEventListener('click', e => {
    if (e.target === e.currentTarget) close();
  });
  document.getElementById('btn-save').addEventListener('click', saveCurrentBuild);
}

function open() {
  renderList();
  document.getElementById('modal-saves').showModal();
}

function close() {
  document.getElementById('modal-saves').close();
}

function saveCurrentBuild() {
  const name    = document.getElementById('build-name').value.trim() || 'My Build';
  const encoded = encodeBuild();
  const saves   = load();
  saves[name]   = { encoded, date: new Date().toISOString() };
  persist(saves);
  return name;
}

export function getSaveCount() {
  return Object.keys(load()).length;
}

function renderList() {
  const saves  = load();
  const keys   = Object.keys(saves).sort((a, b) =>
    new Date(saves[b].date) - new Date(saves[a].date)
  );
  const container = document.getElementById('saves-list');

  if (keys.length === 0) {
    container.innerHTML = `<p class="saves-empty">No saved builds yet.<br>Use the <strong>Save</strong> button in the header to save your build.</p>`;
    return;
  }

  container.innerHTML = keys.map(name => {
    const { date } = saves[name];
    const d = new Date(date);
    const ago = timeAgo(d);
    return `
      <div class="save-item" data-name="${escAttr(name)}">
        <div class="save-item-info">
          <div class="save-item-name">${esc(name)}</div>
          <div class="save-item-date">${ago}</div>
        </div>
        <div class="save-item-actions">
          <button class="btn btn-ghost save-load-btn">Load</button>
          <button class="btn btn-ghost save-del-btn" title="Delete">✕</button>
        </div>
      </div>
    `;
  }).join('');

  container.querySelectorAll('.save-load-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const name = btn.closest('.save-item').dataset.name;
      loadBuild(name);
      close();
    });
  });

  container.querySelectorAll('.save-del-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const name = btn.closest('.save-item').dataset.name;
      if (confirm(`Delete "${name}"?`)) {
        deleteBuild(name);
        renderList();
      }
    });
  });
}

function loadBuild(name) {
  const saves = load();
  const entry = saves[name];
  if (!entry) return;
  try {
    const data = JSON.parse(atob(entry.encoded));
    if (data.n) document.getElementById('build-name').value = data.n;
    if (data.b) dispatch('LOAD_PRESET', { parts: data.b });
  } catch {}
}

function deleteBuild(name) {
  const saves = load();
  delete saves[name];
  persist(saves);
}

function load() {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); }
  catch { return {}; }
}

function persist(saves) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(saves));
}

function timeAgo(date) {
  const sec = Math.floor((Date.now() - date) / 1000);
  if (sec < 60)   return 'just now';
  if (sec < 3600) return `${Math.floor(sec / 60)}m ago`;
  if (sec < 86400) return `${Math.floor(sec / 3600)}h ago`;
  return date.toLocaleDateString();
}

function esc(s)     { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function escAttr(s) { return s.replace(/"/g, '&quot;'); }
