// ADAPTER between the settings page and the generator owned by worker A3.
//
// The real call is generateBinder(profile, kit, { relay, size, onProgress, signal }) -> Blob,
// exported by app/lib/generate.js. This file imports it at run time. If that module does not
// exist yet (or fails to load), a clearly marked STUB stands in so the page can be built and
// tested end to end. The stub makes no network request and its output says it is a placeholder.
//
// What the settings page passes:
//   profile     the validated profile (schema/profile.schema.json), access key included
//   kit         the parsed app/build/kit.json, or null when it is not built yet
//   relay       the relay base URL string from config.js ('' = same origin)
//   size        'small' | 'large'
//   onProgress  called with a number 0..1, or an object such as
//               { fraction, done, total, stage, message } (any of these keys may be missing)
//   signal      an AbortSignal; Cancel aborts it
// What it expects back: a Blob (text/html) for the binder file.

import { config } from './config.js';

let modPromise = null;
export function loadGenerator() {
  modPromise ??= import(config.generatorUrl)
    .then(m => {
      const fn = m.generateBinder || (m.default && m.default.generateBinder) || (typeof m.default === 'function' ? m.default : null);
      if (typeof fn !== 'function') throw new Error('generateBinder missing');
      return { generateBinder: fn, stub: false };
    })
    .catch(() => ({ generateBinder: stubGenerateBinder, stub: true }));
  return modPromise;
}

export async function generateBinder(profile, kit, opts) {
  const { generateBinder: fn } = await loadGenerator();
  return fn(profile, kit, opts);
}

// ---- STUB: used ONLY when app/lib/generate.js is absent or fails to load -----------------
const STEPS = ['Reading your answers', 'Filling the pages', 'Writing your household pages', 'Checking every page', 'Putting the file together'];
async function stubGenerateBinder(profile, kit, { size = 'small', onProgress = () => {}, signal } = {}) {
  const total = 20;
  for (let i = 0; i <= total; i++) {
    if (signal && signal.aborted) throw new DOMException('Cancelled', 'AbortError');
    onProgress({ fraction: i / total, done: i, total, stage: STEPS[Math.min(STEPS.length - 1, Math.floor((i / total) * STEPS.length))] });
    await new Promise(r => setTimeout(r, 60));
  }
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Placeholder binder</title></head><body style="font:16px/1.5 system-ui;padding:1rem;background:#111;color:#eee"><h1>Placeholder, not a binder</h1><p>This file was made by the settings page's test stub because the real generator (app/lib/generate.js) is not installed yet. It contains no survival information.</p><p>Size chosen: ${esc(size)}. Household members: ${esc((profile.members || []).length)}.</p></body></html>`;
  return new Blob([html], { type: 'text/html' });
}
