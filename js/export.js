import { getState, getPartById } from './store.js';

let _getRenderer = null;

export function setRendererGetter(fn) {
  _getRenderer = fn;
}

export function exportBuildCard() {
  const renderer = _getRenderer?.();
  if (!renderer) return;

  // Force a fresh render pass so preserveDrawingBuffer captures current frame
  renderer.render(renderer._scene, renderer._camera);

  const glCanvas = renderer.domElement;
  const W = 1280, H = 720;

  const card = document.createElement('canvas');
  card.width  = W;
  card.height = H;
  const ctx = card.getContext('2d');

  // 3D background
  ctx.drawImage(glCanvas, 0, 0, W, H);

  // Dark gradient overlay on the right-hand strip
  const grad = ctx.createLinearGradient(W * 0.55, 0, W, 0);
  grad.addColorStop(0,   'rgba(8,8,15,0)');
  grad.addColorStop(0.3, 'rgba(8,8,15,0.88)');
  grad.addColorStop(1,   'rgba(8,8,15,0.97)');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, W, H);

  // Bottom bar
  ctx.fillStyle = 'rgba(8,8,15,0.82)';
  ctx.fillRect(0, H - 48, W * 0.55, 48);

  const buildName = document.getElementById('build-name').value.trim() || 'FPV Build';
  const { build } = getState();

  // Build name
  ctx.fillStyle = '#e4e4f0';
  ctx.font      = 'bold 36px system-ui, sans-serif';
  ctx.fillText(buildName, W * 0.6, 72);

  // Accent underline
  ctx.fillStyle = '#00c8ff';
  ctx.fillRect(W * 0.6, 82, 180, 2);

  // Parts list
  const entries = buildEntries(build);
  ctx.font      = '15px system-ui, sans-serif';
  const colX    = [W * 0.6, W * 0.6 + (W * 0.4 * 0.5)];
  entries.forEach((entry, i) => {
    const col = Math.floor(i / 5);
    const row = i % 5;
    const x   = colX[col] ?? colX[0];
    const y   = 120 + row * 42;

    // Category label
    ctx.fillStyle = '#44445a';
    ctx.font      = 'bold 10px system-ui, sans-serif';
    ctx.fillText(entry.category.toUpperCase(), x, y);

    // Part name
    ctx.fillStyle = entry.filled ? '#e4e4f0' : '#44445a';
    ctx.font      = '15px system-ui, sans-serif';
    ctx.fillText(entry.name, x, y + 16);
  });

  // Stats row
  const stats = buildStats(build);
  ctx.fillStyle = '#7878a0';
  ctx.font      = '13px system-ui, sans-serif';
  const statsY  = H - 18;
  ctx.fillText(`Weight: ${stats.weight}`, W * 0.6, statsY);
  ctx.fillText(`Price: ${stats.price}`, W * 0.6 + 160, statsY);
  ctx.fillText(`TWR: ${stats.twr}`, W * 0.6 + 320, statsY);

  // Watermark
  ctx.fillStyle = 'rgba(120,120,160,0.5)';
  ctx.font      = '12px system-ui, sans-serif';
  ctx.fillText('fpv-drone-builder', W - 160, H - 14);

  const link = document.createElement('a');
  link.download = `${buildName.replace(/\s+/g, '-').toLowerCase()}.png`;
  link.href = card.toDataURL('image/png');
  link.click();
}

function buildEntries(build) {
  const { categories } = getState();
  return categories.map(cat => {
    const partId = build[cat.id];
    const part   = partId ? getPartById(partId) : null;
    return { category: cat.label, name: part ? part.name : 'Not selected', filled: !!part };
  });
}

function buildStats(build) {
  const parts = Object.values(build).map(id => getPartById(id)).filter(Boolean);
  const motor = getPartById(build['motor']);
  const weight = parts.reduce((s, p) => s + p.weight_g, 0) + (motor ? motor.weight_g * 3 : 0);
  const price  = parts.reduce((s, p) => s + p.price_php, 0) + (motor ? motor.price_php * 3 : 0);
  return {
    weight: weight > 0 ? `${Math.round(weight)}g` : '—',
    price:  price  > 0 ? `₱${price.toFixed(0)}`   : '—',
    twr:    '—',
  };
}
