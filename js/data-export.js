import { getState, getPartById } from './store.js';

export function init() {
  const btn = document.getElementById('btn-export');
  const modal = document.getElementById('modal-export');
  const closeBtn = document.getElementById('modal-export-close');

  btn?.addEventListener('click', () => modal.showModal());
  closeBtn?.addEventListener('click', () => modal.close());
  modal?.addEventListener('click', e => { if (e.target === modal) modal.close(); });

  document.getElementById('btn-export-excel')?.addEventListener('click', () => {
    exportExcel();
    modal.close();
  });
  document.getElementById('btn-export-pdf')?.addEventListener('click', () => {
    exportPDF();
    modal.close();
  });
}

function gatherBuildData() {
  const { build, categories } = getState();
  const buildName = document.getElementById('build-name').value.trim() || 'FPV Build';

  const rows = categories.map(cat => {
    const partId = build[cat.id];
    const part = partId ? getPartById(partId) : null;
    const qty = cat.id === 'motor' || cat.id === 'propeller' ? 4 : 1;
    return {
      category: cat.label,
      slotId: cat.id,
      qty,
      name: part?.name || '',
      brand: part?.brand || '',
      price: part?.price_php || 0,
      weight: part?.weight_g || 0,
      inStock: part ? (part.in_stock ? 'Yes' : 'No') : '',
      buyUrl: part?.buy_url || '',
      specs: part?.specs || {},
      filled: !!part,
    };
  });

  const filledParts = rows.filter(r => r.filled);
  const totalWeight = filledParts.reduce((s, r) => s + r.weight * r.qty, 0);
  const totalPrice = filledParts.reduce((s, r) => s + r.price * r.qty, 0);

  return { buildName, rows, totalWeight, totalPrice };
}

function specSummary(slotId, specs) {
  if (!specs || Object.keys(specs).length === 0) return '';
  const s = specs;
  switch (slotId) {
    case 'frame':     return `${s.size_mm || ''}mm, ${s.material || ''}`;
    case 'motor':     return `${s.stator_size || ''} ${s.kv || ''}KV`;
    case 'esc':       return `${s.amp_rating || ''}A ${s.protocol || ''}`;
    case 'fc':        return `${s.gyro || ''} ${s.firmware || ''}`;
    case 'propeller': return `${s.diameter_inch || ''}" ${s.blade_count || ''}blade`;
    case 'camera':    return `${s.sensor || ''} ${s.video_system || ''}`;
    case 'vtx':       return `${s.power_mw_max || ''}mW ${s.video_system || ''}`;
    case 'battery':   return `${s.cell_count_s || ''}S ${s.capacity_mah || ''}mAh`;
    case 'receiver':  return `${s.protocol || ''}`;
    case 'gps':       return `${s.chipset || ''}`;
    case 'antenna':   return `${s.connector || ''}`;
    default:          return '';
  }
}

// ── Excel (CSV) Export ─────────────────────────────────

function exportExcel() {
  const { buildName, rows, totalWeight, totalPrice } = gatherBuildData();

  const headers = ['Category', 'Qty', 'Part Name', 'Brand', 'Key Specs', 'Unit Price (PHP)', 'Subtotal (PHP)', 'Weight (g)', 'In Stock', 'Buy URL'];
  const csvRows = [headers];

  for (const r of rows) {
    if (!r.filled) {
      csvRows.push([r.category, r.qty, '(not selected)', '', '', '', '', '', '', '']);
      continue;
    }
    csvRows.push([
      r.category,
      r.qty,
      r.name,
      r.brand,
      specSummary(r.slotId, r.specs),
      r.price.toFixed(2),
      (r.price * r.qty).toFixed(2),
      r.weight,
      r.inStock,
      r.buyUrl,
    ]);
  }

  csvRows.push([]);
  csvRows.push(['', '', '', '', 'TOTAL', '', totalPrice.toFixed(2), totalWeight + 'g', '', '']);

  const csv = csvRows.map(row =>
    row.map(cell => {
      const s = String(cell);
      return s.includes(',') || s.includes('"') || s.includes('\n')
        ? '"' + s.replace(/"/g, '""') + '"'
        : s;
    }).join(',')
  ).join('\n');

  const BOM = '﻿';
  download(BOM + csv, `${slugify(buildName)}-parts.csv`, 'text/csv;charset=utf-8');
}

// ── PDF Export ─────────────────────────────────────────

function exportPDF() {
  const { buildName, rows, totalWeight, totalPrice } = gatherBuildData();
  const dateStr = new Date().toLocaleDateString();

  const W = 595, H = 842;
  const M = 40;

  let stream = '';
  const esc = s => String(s)
    .replace(/\\/g, '\\\\')
    .replace(/\(/g, '\\(')
    .replace(/\)/g, '\\)')
    .replace(/[^\x20-\x7E]/g, '');

  const text = (s, x, yp, size = 9, bold = false) => {
    const font = bold ? '/F2' : '/F1';
    stream += `BT ${font} ${size} Tf ${x} ${yp} Td (${esc(s)}) Tj ET\n`;
  };

  const line = (x1, y1, x2, y2, w = 0.4) => {
    stream += `${w} w ${x1} ${y1} m ${x2} ${y2} l S\n`;
  };

  const rect = (x, y, w, h) => {
    stream += `0.95 0.97 0.99 rg ${x} ${y} ${w} ${h} re f\n`;
  };

  let y = H - M;

  text(buildName, M, y, 20, true);
  y -= 18;
  text('FPV Drone Build - Parts List', M, y, 10);
  y -= 14;
  text('Export Date: ' + dateStr, M, y, 8);
  y -= 24;

  const cols = [M, M + 90, M + 105, M + 260, M + 330, M + 395, M + 455];
  const colLabels = ['Category', 'Qty', 'Part Name', 'Brand', 'Price (PHP)', 'Subtotal', 'Weight (g)'];

  rect(M - 4, y - 4, W - 2 * M + 8, 16);
  stream += '0 0 0 rg\n';
  colLabels.forEach((label, i) => text(label, cols[i], y, 8, true));
  y -= 6;
  line(M - 4, y, W - M + 4, y, 0.6);
  y -= 14;

  for (const r of rows) {
    if (y < M + 40) break;

    text(r.category, cols[0], y, 8);
    text(String(r.qty), cols[1], y, 8);

    if (r.filled) {
      const displayName = r.name.length > 26 ? r.name.substring(0, 25) + '...' : r.name;
      text(displayName, cols[2], y, 8);
      text(r.brand, cols[3], y, 8);
      text(r.price.toFixed(2), cols[4], y, 8);
      text((r.price * r.qty).toFixed(2), cols[5], y, 8);
      text(String(r.weight), cols[6], y, 8);
    } else {
      text('(not selected)', cols[2], y, 8);
    }

    y -= 4;
    stream += '0.92 0.92 0.92 RG\n';
    line(M - 4, y, W - M + 4, y, 0.2);
    stream += '0 0 0 RG\n';
    y -= 12;
  }

  y -= 8;
  line(M - 4, y + 8, W - M + 4, y + 8, 0.8);
  y -= 6;
  text('TOTALS', cols[0], y, 9, true);
  text(totalPrice.toFixed(2), cols[5], y, 9, true);
  text(totalWeight + 'g', cols[6], y, 9, true);

  y -= 28;
  const specTitle = 'Specifications';
  text(specTitle, M, y, 12, true);
  y -= 16;

  for (const r of rows) {
    if (!r.filled || y < M + 20) continue;
    const spec = specSummary(r.slotId, r.specs);
    if (!spec) continue;
    text(r.category + ':', M, y, 8, true);
    text(spec, M + 90, y, 8);
    y -= 14;
  }

  y = M + 10;
  stream += '0.6 0.6 0.7 rg\n';
  text('Generated by FPV Drone Builder', M, y, 7);
  stream += '0 0 0 rg\n';

  const pdf = buildPDF(W, H, stream);
  download(pdf, `${slugify(buildName)}-parts.pdf`, 'application/pdf');
}

function buildPDF(W, H, contentStream) {
  const offsets = [];
  let out = '%PDF-1.4\n';

  const obj = (id, body) => {
    offsets[id] = out.length;
    out += `${id} 0 obj\n${body}\nendobj\n`;
  };

  obj(1, '<< /Type /Catalog /Pages 2 0 R >>');
  obj(2, '<< /Type /Pages /Kids [3 0 R] /Count 1 >>');
  obj(3, `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>`);
  obj(4, `<< /Length ${contentStream.length} >>\nstream\n${contentStream}endstream`);
  obj(5, '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>');
  obj(6, '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>');

  const xrefPos = out.length;
  out += 'xref\n';
  out += '0 7\n';
  out += '0000000000 65535 f \n';
  for (let i = 1; i <= 6; i++) {
    out += String(offsets[i]).padStart(10, '0') + ' 00000 n \n';
  }
  out += 'trailer\n<< /Size 7 /Root 1 0 R >>\nstartxref\n' + xrefPos + '\n%%EOF';
  return out;
}

// ── Helpers ────────────────────────────────────────────

function slugify(s) {
  return s.replace(/\s+/g, '-').replace(/[^a-zA-Z0-9-]/g, '').toLowerCase() || 'build';
}

function download(content, filename, mimeType) {
  const blob = typeof content === 'string'
    ? new Blob([content], { type: mimeType })
    : content;
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 5000);
}
