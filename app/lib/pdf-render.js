// pdf-render.js — a bound PDF source → page images, so a Large binder shows and prints the whole
// document on any device with no PDF viewer and no network (owner request, docs/07 step 3).
//
//   const r = await renderPdfPages(bytes, { width, quality, maxPages, signal, onPage })
//   → { pages: [{ bytes: Uint8Array (JPEG), width, height }], total, truncated }
//
// Uses the vendored pdf.js (app/lib/vendor/pdfjs/, Apache-2.0, pdfjs-dist 4.10.38) at generation
// time in the browser. pdf.js never goes into the binder; only the JPEG pages do. Needs a canvas
// (OffscreenCanvas or a DOM canvas): in node it throws and generate.js falls back to embedding the
// PDF with an "Open the document" button.

const VENDOR = new URL('./vendor/pdfjs/', import.meta.url);

export const canRenderPdf = () => typeof OffscreenCanvas !== 'undefined' || (typeof document !== 'undefined' && !!document.createElement);

function makeCanvas(w, h) {
  if (typeof OffscreenCanvas !== 'undefined') return new OffscreenCanvas(w, h);
  const c = document.createElement('canvas'); c.width = w; c.height = h; return c;
}

async function toJpeg(canvas, quality) {
  const blob = canvas.convertToBlob
    ? await canvas.convertToBlob({ type: 'image/jpeg', quality })
    : await new Promise((ok, no) => canvas.toBlob(b => (b ? ok(b) : no(new Error('canvas toBlob failed'))), 'image/jpeg', quality));
  return new Uint8Array(await blob.arrayBuffer());
}

let libPromise = null;
async function lib() {
  libPromise ??= import(new URL('pdf.min.mjs', VENDOR).href).then(m => {
    m.GlobalWorkerOptions.workerSrc = new URL('pdf.worker.min.mjs', VENDOR).href;
    return m;
  });
  return libPromise;
}

export async function renderPdfPages(bytes, { width = 1100, quality = 0.6, maxPages = 600, signal, onPage } = {}) {
  if (!canRenderPdf()) throw new Error('no canvas in this environment');
  const pdfjs = await lib();
  const doc = await pdfjs.getDocument({
    data: bytes.slice(), // pdf.js transfers the buffer to its worker; keep ours
    standardFontDataUrl: new URL('standard_fonts/', VENDOR).href,
    isEvalSupported: false, enableXfa: false,
  }).promise;
  try {
    const total = doc.numPages;
    if (!total) throw new Error('the PDF has no pages');
    const n = Math.min(total, maxPages);
    const pages = [];
    for (let i = 1; i <= n; i++) {
      signal?.throwIfAborted?.();
      const page = await doc.getPage(i);
      const base = page.getViewport({ scale: 1 });
      const vp = page.getViewport({ scale: width / base.width });
      const w = Math.ceil(vp.width), h = Math.ceil(vp.height);
      const canvas = makeCanvas(w, h);
      const ctx = canvas.getContext('2d');
      ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, w, h);
      await page.render({ canvasContext: ctx, viewport: vp, annotationMode: 0 }).promise;
      pages.push({ bytes: await toJpeg(canvas, quality), width: w, height: h });
      page.cleanup();
      onPage?.(i, n);
    }
    return { pages, total, truncated: total > n };
  } finally { await doc.destroy(); }
}
