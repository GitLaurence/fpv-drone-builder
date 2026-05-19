import { getState, getPartById } from './store.js';

let _list     = [];   // array of partIds, max 3
let _category = null;
let _onUpdate = null; // callback for catalog.js to refresh UI

export function init(onUpdateCallback) {
  _onUpdate = onUpdateCallback;
  document.getElementById('btn-compare-open').addEventListener('click', openModal);
  document.getElementById('modal-compare-close').addEventListener('click', closeModal);
  document.getElementById('modal-compare').addEventListener('click', e => {
    if (e.target === e.currentTarget) closeModal();
  });
}

export function setCategory(categoryId) {
  if (categoryId !== _category) {
    _list     = [];
    _category = categoryId;
  }
}

export function toggle(partId) {
  const idx = _list.indexOf(partId);
  if (idx >= 0) {
    _list.splice(idx, 1);
  } else if (_list.length < 3) {
    _list.push(partId);
  }
  _onUpdate?.();
  return [..._list];
}

export function isComparing(partId) { return _list.includes(partId); }
export function getCount()          { return _list.length; }
export function getList()           { return [..._list]; }
export function clear()             { _list = []; _onUpdate?.(); }

function openModal() {
  if (_list.length < 2) return;
  renderTable();
  document.getElementById('modal-compare').showModal();
}

function closeModal() {
  document.getElementById('modal-compare').close();
}

function renderTable() {
  const parts = _list.map(id => getPartById(id)).filter(Boolean);
  if (!parts.length) return;

  const allSpecKeys = [...new Set(parts.flatMap(p => Object.keys(p.specs || {})))];
  const colCount = parts.length;

  const headCols = parts.map(p => `
    <th>
      <div class="ct-brand">${p.brand}</div>
      <div class="ct-name">${p.name}</div>
      <div class="ct-price">$${p.price_usd.toFixed(2)}</div>
      <div class="ct-weight">${p.weight_g}g</div>
      <span class="ct-stock ${p.in_stock ? 'in-stock' : ''}">${p.in_stock ? '● In Stock' : '○ Out of Stock'}</span>
    </th>
  `).join('');

  const specRows = allSpecKeys.map(key => {
    const vals = parts.map(p => p.specs[key]);
    const allSame = vals.every((v, _, a) => JSON.stringify(v) === JSON.stringify(a[0]));
    const cells = vals.map(v => `<td class="${allSame ? '' : 'ct-diff'}">${fmtVal(v)}</td>`).join('');
    return `<tr><td class="ct-key">${fmtKey(key)}</td>${cells}</tr>`;
  }).join('');

  document.getElementById('compare-table-container').innerHTML = `
    <table class="compare-table">
      <thead>
        <tr>
          <th class="ct-spec-col">Spec</th>
          ${headCols}
        </tr>
      </thead>
      <tbody>${specRows}</tbody>
    </table>
  `;
}

function fmtKey(k) {
  return k.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}
function fmtVal(v) {
  if (v === true)  return '✓';
  if (v === false) return '—';
  if (Array.isArray(v)) return v.join(', ');
  return v ?? '—';
}
