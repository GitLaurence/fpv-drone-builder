import { getState, dispatch } from './store.js';

export function encodeBuild() {
  const { build } = getState();
  const name = document.getElementById('build-name').value.trim();
  const payload = { n: name, b: build };
  return btoa(JSON.stringify(payload));
}

export function decodeBuild(hash) {
  try {
    return JSON.parse(atob(hash));
  } catch {
    return null;
  }
}

export function applyFromHash() {
  const hash = location.hash.slice(1);
  if (!hash) return;
  const data = decodeBuild(hash);
  if (!data || !data.b) return;

  if (data.n) {
    document.getElementById('build-name').value = data.n;
  }
  dispatch('LOAD_PRESET', { parts: data.b });
}

export function copyShareLink() {
  const encoded = encodeBuild();
  const url = `${location.origin}${location.pathname}#${encoded}`;
  history.replaceState(null, '', `#${encoded}`);
  navigator.clipboard.writeText(url).catch(() => {});
  return url;
}

export function saveBuild() {
  const encoded = encodeBuild();
  const name = document.getElementById('build-name').value.trim() || 'My Build';
  const saves = JSON.parse(localStorage.getItem('fpv_builds') || '{}');
  saves[name] = encoded;
  localStorage.setItem('fpv_builds', JSON.stringify(saves));
  return name;
}
