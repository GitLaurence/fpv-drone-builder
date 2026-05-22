import { dispatch, getState } from './store.js';
import { encodeBuild } from './share.js';

const STORAGE_KEY = 'fpv_builds';

export function init() {
  document.getElementById('btn-my-builds').addEventListener('click', open);
  document.getElementById('modal-saves-close').addEventListener('click', close);
  document.getElementById('modal-saves').addEventListener('click', e => {
    if (e.target === e.currentTarget) close();
  });
  document.getElementById('btn-save').addEventListener('click', () => {
    saveCurrentBuild();
    toast('Build saved!', 'success');
  });
  document.getElementById('btn-save-in-modal').addEventListener('click', () => {
    saveCurrentBuild();
    renderList();
    toast('Build saved!', 'success');
  });
}

function open() {
  renderList();
  updateCountChip();
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
    container.innerHTML = `
      <div class="saves-empty">
        <span class="saves-empty-icon">🛸</span>
        No saved builds yet.<br>
        Hit <strong>+ Save Current</strong> above to save your first build.
      </div>`;
    return;
  }

  container.innerHTML = keys.map(name => {
    const { date, encoded } = saves[name];
    const d = new Date(date);
    const ago = timeAgo(d);
    const partCount = countParts(encoded);
    const partBadge = partCount > 0
      ? `<span class="save-parts-badge">⚙ ${partCount} part${partCount !== 1 ? 's' : ''}</span>`
      : '';
    return `
      <div class="save-item" data-name="${escAttr(name)}">
        <div class="save-item-icon">🛸</div>
        <div class="save-item-info">
          <div class="save-item-name">${esc(name)}</div>
          <div class="save-item-meta">
            ${partBadge}
            ${partCount > 0 ? '<span class="save-item-meta-sep">·</span>' : ''}
            <span>${ago}</span>
          </div>
        </div>
        <div class="save-item-actions">
          <button class="btn btn-ghost save-load-btn">Load</button>
          <button class="btn btn-ghost save-del-btn" title="Delete">✕</button>
        </div>
      </div>
    `;
  }).join('');
  updateCountChip();

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

function toast(msg, type = '') {
  const el = document.getElementById('toast');
  if (!el) return;
  el.textContent = msg;
  el.className   = `toast${type ? ' ' + type : ''} show`;
  clearTimeout(el._timer);
  el._timer = setTimeout(() => el.classList.remove('show'), 2800);
}

function countParts(encoded) {
  try {
    const data = JSON.parse(atob(encoded));
    if (!data.b) return 0;
    return Object.values(data.b).filter(Boolean).length;
  } catch { return 0; }
}

function updateCountChip() {
  const count = Object.keys(load()).length;
  const chip  = document.getElementById('modal-saves-count');
  if (!chip) return;
  chip.textContent  = count > 0 ? `${count} saved` : '';
  chip.style.display = count > 0 ? '' : 'none';
}
