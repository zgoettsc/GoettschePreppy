// GoettschePreppy settings page: the walkthrough shell, Save / Load, the access-key check and the
// Generate screen. Answers live in memory (state.js). See notes/workers/A2.md.

import { config } from './config.js';
import { NOTICE } from './notice.js';
import { draft, ui, toProfile, validate, loadProfile, getAt, ptr } from './state.js';
import { h, setHooks, noticeBlock, idOf } from './ui.js';
import { STEPS, env, noticeFull } from './steps.js';
import { loadRegions, loadKit, sizeEstimates } from './loaders.js';
import { checkAccessKey } from './relay.js';
import { generateBinder, loadGenerator } from './generate-adapter.js';
import { readKept, writeKept, eraseKept } from './storage.js';

const FINAL = STEPS.length; // index of the Generate screen
const main = document.getElementById('main');

const app = {
  step: 0,
  shown: new Set(),          // steps whose errors are visible (after a Next attempt)
  key: { key: '', status: 'idle', label: '' },
  keep: false,               // opt-in browser storage
  includeKeyInFile: true,
  dirty: false,
  flash: null,               // { text, kind } shown once in the Save/Load bar
  size: 'small',
  gen: { status: 'idle', fraction: 0, stage: '', error: '', url: null, bytes: 0, size: null, stub: false },
  controller: null,
};

// ---- extra checks the schema cannot make --------------------------------------------------
function extraChecks(p) {
  const out = [];
  const check = (st, county, pointer, step) => {
    const list = env.regions.available && st ? env.regions.counties[st] : null;
    if (list && county && !list.includes(county)) out.push({ pointer, step, message: 'That county is not in our list for this state. Please choose it from the list.' });
  };
  check(p.home?.state, p.home?.county, '/home/county', 1);
  (p.destinations || []).forEach((d, i) => check(d.state, d.county, `/destinations/${i}/county`, 5));
  return out;
}
function currentValidation() {
  const p = toProfile();
  return { profile: p, ...validate(p, extraChecks(p)) };
}

// ---- rendering --------------------------------------------------------------------------------
function rerender(opts = {}) {
  const active = document.activeElement;
  const focusId = opts.focus || (active && active.id && main.contains(active) ? active.id : null);
  const y = window.scrollY;
  render();
  window.scrollTo(0, y);
  if (focusId) {
    const el = document.getElementById(focusId);
    if (el) el.focus({ preventScroll: !opts.focus });
  }
}
function changed() {
  app.dirty = true;
  if (app.keep) writeKept(toProfile({ includeKey: false }), app.step);
  if (app.shown.has(app.step) || app.step === FINAL) refreshErrors();
  // the key status belongs to the key that was checked
  const k = draft.access?.access_key || '';
  if (app.key.status !== 'idle' && app.key.key !== k) { app.key = { key: '', status: 'idle', label: '' }; updateKeyStatus(); }
}
setHooks({ rerender: (o) => { changed(); rerender(o); }, changed });
env.rerender = (o) => { changed(); rerender(o); };

function goto(step, { focusHeading = true } = {}) {
  app.step = Math.max(0, Math.min(FINAL, step));
  if (app.keep) writeKept(toProfile({ includeKey: false }), app.step);
  render();
  window.scrollTo(0, 0);
  if (focusHeading) document.getElementById('step-title')?.focus();
  if (app.step >= 7) ensureKit();
}

function ensureKit() {
  if (!env.kitState.loading || env.kitState.started) return;
  env.kitState.started = true;
  loadKit().then(k => {
    Object.assign(env.kitState, { loading: false, ...k });
    if (app.step === 8 || app.step === FINAL) rerender();
  });
}

function stepNav() {
  const total = STEPS.length;
  const label = app.step === FINAL ? 'Last step' : `Step ${app.step + 1} of ${total}`;
  const pct = Math.round((Math.min(app.step, total) / total) * 100);
  return h('nav', { class: 'stepnav', 'aria-label': 'Steps' },
    h('div', { class: 'stepnav-row' },
      h('span', { class: 'stepcount' }, label),
      h('div', { class: 'bar', 'aria-hidden': 'true' }, Object.assign(h('span'), { style: `width:${pct}%` }))),
    h('details', { class: 'allsteps' },
      h('summary', {}, 'All steps'),
      h('ol', {}, [...STEPS.map((s, i) => [i, s.title]), [FINAL, 'Make your binder']].map(([i, t]) =>
        h('li', {}, h('button', { type: 'button', class: 'linklike', 'aria-current': i === app.step ? 'step' : undefined,
          onclick: () => goto(i) }, t))))));
}

function toolbar() {
  const file = h('input', { type: 'file', id: 'load-file', accept: 'application/json,.json', class: 'visually-hidden',
    onchange: (e) => { const f = e.target.files && e.target.files[0]; e.target.value = ''; if (f) loadFromFile(f); } });
  return h('div', { class: 'toolbar', role: 'group', 'aria-label': 'Your answers file' },
    h('button', { type: 'button', class: 'btn small', id: 'save-btn', onclick: saveAnswers }, 'Save my answers'),
    h('label', { class: 'btn small ghost', for: 'load-file', id: 'load-btn', tabindex: '0', role: 'button',
      onkeydown: (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); file.click(); } } }, 'Load answers'),
    file,
    h('p', { class: 'toolbar-status' + (app.flash ? ' ' + app.flash.kind : ''), id: 'toolbar-status', role: 'status', 'aria-live': 'polite' },
      app.flash ? app.flash.text : ''));
}

function errorSummary(errors) {
  if (!errors.length) return h('div', { id: 'err-summary', hidden: true });
  return h('div', { class: 'err-summary', id: 'err-summary', role: 'alert', tabindex: '-1' },
    h('p', {}, errors.length === 1 ? 'One answer on this step needs a look:' : `${errors.length} answers on this step need a look:`),
    h('ul', {}, errors.slice(0, 12).map(er => h('li', {},
      h('button', { type: 'button', class: 'linklike', onclick: () => focusPointer(er.pointer) }, describePointer(er.pointer), ': ', er.message)))));
}

function describePointer(pointer) {
  const el = fieldFor(pointer);
  const lab = el && el.querySelector('.q-label');
  let name = lab ? lab.textContent.replace(' (needed)', '').trim() : pointer.split('/').filter(Boolean).pop().replace(/_/g, ' ');
  const m = pointer.match(/^\/(members|pets|livestock|destinations)\/(\d+)/);
  if (m) name = `${{ members: 'Person', pets: 'Pet', livestock: 'Animal group', destinations: 'Destination' }[m[1]]} ${+m[2] + 1}, ${name}`;
  return name || 'An answer';
}
function fieldFor(pointer) {
  let best = null;
  for (const el of main.querySelectorAll('[data-paths]')) {
    if (el.dataset.paths.split(' ').includes(pointer)) best = el; // innermost wins (document order)
  }
  return best;
}
function focusPointer(pointer) {
  const el = fieldFor(pointer);
  if (!el) return;
  const det = el.closest('details');
  if (det) det.open = true;
  const input = el.querySelector('input:not([type=hidden]), select, textarea, button');
  el.scrollIntoView({ block: 'center' });
  (input || el).focus({ preventScroll: true });
}

function refreshErrors() {
  const { errors } = currentValidation();
  const mine = app.step === FINAL ? [] : errors.filter(e => e.step === app.step);
  const show = app.shown.has(app.step);
  for (const el of main.querySelectorAll('[data-paths]')) {
    const paths = el.dataset.paths.split(' ');
    const errEl = [...el.children].find(c => c.classList && c.classList.contains('err'));
    if (!errEl) continue;
    const hit = show ? mine.find(e => paths.includes(e.pointer)) : null;
    errEl.hidden = !hit;
    errEl.textContent = hit ? hit.message : '';
    el.classList.toggle('has-err', !!hit);
    for (const input of el.querySelectorAll(':scope > input, :scope > select, :scope > textarea, :scope > .row > input, :scope > .row > select'))
      input.toggleAttribute('aria-invalid', !!hit);
  }
  if (app.step !== FINAL) {
    const old = document.getElementById('err-summary');
    const fresh = errorSummary(show ? mine : []);
    if (old) old.replaceWith(fresh);
  } else {
    const box = document.getElementById('final-check');
    if (box) box.replaceWith(finalCheck());
  }
  return mine;
}

function render() {
  main.replaceChildren();
  const s = STEPS[app.step];
  main.append(stepNav());
  if (app.step === FINAL) { renderFinal(); return; }
  main.append(...[
    h('h1', { id: 'step-title', tabindex: '-1' }, s.title),
    config.dryRun ? h('p', { class: 'warn' }, 'Dry run (test mode): your key is checked by a stand-in and nothing is sent anywhere.') : null,
    noticeBlock(NOTICE.neverStored, { collapsedTail: app.step !== 0, cls: 'never-stored' }),
    toolbar(),
    h('p', { class: 'intro' }, s.intro),
    errorSummary([]),
    h('form', { class: 'step', novalidate: true, id: 'step-form', 'aria-labelledby': 'step-title',
      onsubmit: (e) => e.preventDefault() }, s.render()),
    h('div', { class: 'bottomnav' },
      h('button', { type: 'button', class: 'btn ghost', id: 'back-btn', disabled: app.step === 0 || undefined, onclick: () => goto(app.step - 1) }, 'Back'),
      h('button', { type: 'button', class: 'btn primary', id: 'next-btn', onclick: next },
        app.step === STEPS.length - 1 ? 'Review and finish' : 'Next'))].filter(Boolean));
  refreshErrors();
}

function next() {
  app.shown.add(app.step);
  const mine = refreshErrors();
  if (mine.length) {
    document.getElementById('err-summary')?.focus();
    return;
  }
  goto(app.step + 1);
}

// ---- access key -------------------------------------------------------------------------------
env.keyCheckUI = () => h('div', { class: 'keycheck' },
  h('button', { type: 'button', class: 'btn small', id: 'check-key-btn', onclick: runKeyCheck }, 'Check my key'),
  h('p', { id: 'key-status', class: 'key-status', role: 'status', 'aria-live': 'polite' }, keyStatusText()));

function keyStatusText() {
  switch (app.key.status) {
    case 'checking': return 'Checking your key…';
    case 'ok': return `Key accepted${app.key.label ? ` (${app.key.label})` : ''}.`;
    case 'rejected': return 'That key was not accepted. Check it for typing mistakes, or ask the person who gave it to you.';
    case 'forbidden': return 'The relay refused requests from this page\'s address. The site owner needs to add this address to the relay settings (PAGES_ORIGIN). Your answers are still here.';
    case 'unreachable': return 'Could not reach the relay to check the key. Check your connection and try again; your answers are still here.';
    default: return 'Not checked yet.';
  }
}
function updateKeyStatus() {
  for (const el of document.querySelectorAll('.key-status')) {
    el.textContent = keyStatusText();
    el.className = 'key-status ' + app.key.status;
  }
}
async function runKeyCheck() {
  const key = (draft.access?.access_key || '').trim();
  if (key.length < 8) {
    app.key = { key, status: 'rejected', label: '' };
    updateKeyStatus();
    return false;
  }
  app.key = { key: draft.access.access_key, status: 'checking', label: '' };
  updateKeyStatus();
  const r = await checkAccessKey(key);
  if ((draft.access?.access_key || '') !== app.key.key) return false; // changed while checking
  app.key = { key: draft.access.access_key, status: r.ok ? 'ok' : r.reason, label: r.label || '' };
  updateKeyStatus();
  if (app.step === FINAL) { const box = document.getElementById('final-check'); if (box) box.replaceWith(finalCheck()); }
  return r.ok;
}

// ---- keep in this browser (opt-in) ------------------------------------------------------------
env.keepToggleUI = () => h('fieldset', { class: 'q keep' },
  h('legend', { class: 'q-label' }, 'Keep my answers in this browser'),
  h('p', { class: 'why', id: 'keep-why' }, h('span', { class: 'why-tag' }, 'What it does: '),
    'Off unless you turn it on. When on, your answers (but never your access key) are kept in this browser\'s storage on this device, so closing the tab does not lose them. They are not sent anywhere. Anyone who uses this browser could read them. Turning it off erases them.'),
  h('label', { class: 'choice single', for: 'keep-toggle' },
    h('input', { type: 'checkbox', id: 'keep-toggle', checked: app.keep || undefined, 'aria-describedby': 'keep-why',
      onchange: (e) => {
        app.keep = e.target.checked;
        if (app.keep) writeKept(toProfile({ includeKey: false }), app.step); else eraseKept();
        flash(app.keep ? 'Your answers are now kept in this browser.' : 'Kept answers erased from this browser.', 'ok');
      } }),
    h('span', { class: 'choice-text' }, 'Keep my answers in this browser')));

// ---- save / load ------------------------------------------------------------------------------
function flash(text, kind = 'ok') {
  app.flash = { text, kind };
  const el = document.getElementById('toolbar-status') || document.getElementById('final-status');
  if (el) { el.textContent = text; el.className = (el.id === 'toolbar-status' ? 'toolbar-status ' : 'final-status ') + kind; }
}
function download(blob, name) {
  const url = URL.createObjectURL(blob);
  const a = h('a', { href: url, download: name, class: 'visually-hidden' });
  document.body.append(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 10000);
}
function saveAnswers() {
  const p = toProfile({ includeKey: app.includeKeyInFile });
  const { errors } = validate(toProfile(), extraChecks(p));
  download(new Blob([JSON.stringify(p, null, 2) + '\n'], { type: 'application/json' }), 'profile.json');
  app.dirty = false;
  flash(errors.length
    ? `Saved profile.json to your device. ${errors.length === 1 ? 'One answer is' : `${errors.length} answers are`} still missing or need a look; you can finish later by loading this file.`
    : 'Saved profile.json to your device. Keep it private; it holds your household\'s answers.', 'ok');
}
async function loadFromFile(file) {
  let p;
  try {
    if (file.size > 2 * 1024 * 1024) throw new Error('too-big');
    p = JSON.parse(await file.text());
  } catch {
    flash('That file could not be read as a profile.json. Nothing was changed.', 'bad');
    return;
  }
  if (!p || typeof p !== 'object' || Array.isArray(p) || (p.schema_version !== undefined && p.schema_version !== 1)) {
    flash('That file is not a GoettschePreppy profile.json (or is from a different version). Nothing was changed.', 'bad');
    return;
  }
  try { loadProfile(p); } catch {
    flash('That file could not be loaded. Nothing was changed.', 'bad');
    return;
  }
  app.key = { key: '', status: 'idle', label: '' };
  app.dirty = false;
  const { errors } = currentValidation();
  if (errors.length) for (const e of errors) app.shown.add(e.step);
  if (app.keep) writeKept(toProfile({ includeKey: false }), app.step);
  app.flash = {
    text: errors.length
      ? `Loaded your answers. ${errors.length === 1 ? 'One answer needs' : `${errors.length} answers need`} a look; they are marked in the steps.`
      : 'Loaded your answers from the file.',
    kind: errors.length ? 'warnflash' : 'ok',
  };
  render();
  document.getElementById('toolbar-status')?.focus?.();
}

// ---- final screen: check, size, generate, download --------------------------------------------
function finalCheck() {
  const { errors } = currentValidation();
  const byStep = new Map();
  for (const e of errors) { if (!byStep.has(e.step)) byStep.set(e.step, []); byStep.get(e.step).push(e); }
  const keyOk = app.key.status === 'ok' && app.key.key === (draft.access?.access_key || '');
  return h('section', { class: 'panel', id: 'final-check', 'aria-labelledby': 'check-title' },
    h('h2', { id: 'check-title' }, '1. Check your answers'),
    errors.length
      ? [h('p', { class: 'warn' }, errors.length === 1 ? 'One answer needs a look before we can make your binder:' : `${errors.length} answers need a look before we can make your binder:`),
        h('ul', { class: 'fixlist' }, [...byStep.entries()].sort((a, b) => a[0] - b[0]).map(([st, list]) =>
          h('li', {}, h('button', { type: 'button', class: 'linklike', onclick: () => { app.shown.add(st); goto(st); } },
            `${STEPS[st].title}: ${list.length === 1 ? 'one answer' : `${list.length} answers`}`))))]
      : h('p', { class: 'okline' }, 'All needed answers are filled in. Anything you skipped will print as a blank to fill in by hand.'),
    h('div', { class: 'keycheck' },
      h('p', { class: 'key-status ' + app.key.status, role: 'status', 'aria-live': 'polite' }, keyOk ? keyStatusText() : app.key.status === 'idle' ? 'Your access key is checked when you press Generate.' : keyStatusText()),
      keyOk ? null : h('button', { type: 'button', class: 'btn small', onclick: runKeyCheck }, 'Check my key now')));
}

function sizeChoice(est) {
  const fmt = (r) => (r.minMB === r.maxMB ? `about ${r.minMB} MB` : `about ${r.minMB} to ${r.maxMB} MB`);
  const opt = (value, title, mb, text) => h('label', { class: 'choice size', for: `size-${value}` },
    h('input', { type: 'radio', name: 'size', id: `size-${value}`, value, checked: app.size === value || undefined,
      disabled: app.gen.status === 'running' || undefined, onchange: () => { app.size = value; } }),
    h('span', { class: 'choice-text' }, h('strong', {}, title), h('span', { class: 'mb' }, fmt(mb)), h('span', { class: 'hint' }, text)));
  return h('fieldset', { class: 'q sizes' },
    h('legend', { class: 'q-label' }, 'Which size?'),
    h('p', { class: 'why' }, h('span', { class: 'why-tag' }, 'Why we ask: '), 'A bigger file holds more but takes longer to make and more space on your phone. You can upgrade Small to Large later by loading your saved answers file.'),
    h('div', { class: 'choices' },
      opt('small', 'Small', est.small, 'Every page, explainer, decision card, condition and gear page, the whole national region appendix and all plant pictures. Sources are listed by title, publisher and date, not included. Fast on a phone.'),
      opt('large', 'Large', est.large, 'Everything in Small, plus the full text of every cited source document bound behind the page that cites it, and topographic maps for your home, your destinations and the counties between. Fetched for your household when you generate.')));
}

function genPanel() {
  const g = app.gen;
  const box = h('section', { class: 'panel', id: 'gen-panel', 'aria-labelledby': 'gen-title' }, h('h2', { id: 'gen-title' }, '3. Make your binder'));
  if (g.stub) box.append(h('p', { class: 'warn' }, 'Test mode: the real binder generator is not installed on this site yet, so Generate makes a short placeholder file.'));
  if (config.dryRun && !g.stub) box.append(h('p', { class: 'warn', id: 'dryrun-banner' }, 'Dry run (test mode): nothing is sent to the AI service. Pages the AI would write hold filler text, and source documents are stand-ins. Do not rely on this file.'));
  box.append(h('p', { class: 'muted' }, 'A full run takes about 10 to 20 minutes. Keep this tab open and your phone awake until it finishes.'));
  if (g.status === 'running') {
    const pct = Math.round(g.fraction * 100);
    box.append(
      h('label', { for: 'gen-progress', class: 'q-label' }, 'Progress'),
      h('progress', { id: 'gen-progress', max: '100', value: String(pct) }, `${pct}%`),
      h('p', { id: 'gen-stage', role: 'status', 'aria-live': 'polite' }, `${g.stage || 'Working'}… ${pct}%`),
      h('button', { type: 'button', class: 'btn ghost', id: 'cancel-btn', onclick: () => app.controller && app.controller.abort() }, 'Cancel'));
    return box;
  }
  box.append(h('button', { type: 'button', class: 'btn primary big', id: 'generate-btn', onclick: startGenerate },
    g.status === 'done' ? 'Generate again' : 'Generate my binder'));
  if (g.status === 'cancelled') box.append(h('p', { class: 'muted', role: 'status' }, 'Cancelled. Nothing was kept; your answers are still here.'));
  if (g.status === 'error') box.append(h('p', { class: 'bad', role: 'alert' }, g.error));
  if (g.status === 'done' && g.url) {
    const name = `goettschepreppy-binder-${g.size}.html`;
    box.append(h('div', { class: 'done', role: 'status' },
      h('p', {}, h('strong', {}, 'Your binder is ready. '), `${g.size === 'large' ? 'Large' : 'Small'}, ${(g.bytes / 1048576).toFixed(1)} MB.`),
      h('a', { href: g.url, download: name, class: 'btn primary big', id: 'download-link' }, 'Download my binder'),
      h('p', { class: 'muted' }, 'Save it to your phone\'s Files app and to a laptop. It opens with no connection. Once you close this tab, the only copy is the one you downloaded.')));
  }
  return box;
}
function updateGenPanel() {
  const old = document.getElementById('gen-panel');
  if (!old) return;
  if (app.gen.status === 'running' && old.querySelector('#gen-progress')) {
    const pct = Math.round(app.gen.fraction * 100);
    const pr = old.querySelector('#gen-progress');
    pr.value = pct; pr.textContent = `${pct}%`;
    old.querySelector('#gen-stage').textContent = `${app.gen.stage || 'Working'}… ${pct}%`;
    return;
  }
  const hadFocus = old.contains(document.activeElement);
  const fresh = genPanel();
  old.replaceWith(fresh);
  for (const r of document.querySelectorAll('input[name=size]')) r.disabled = app.gen.status === 'running';
  if (hadFocus || app.gen.status !== 'running') {
    const target = fresh.querySelector('#cancel-btn, #download-link, #generate-btn');
    if (target && (hadFocus || app.gen.status === 'done')) target.focus();
  }
}

function onProgress(p) {
  let fraction = app.gen.fraction, stage = app.gen.stage;
  if (typeof p === 'number') fraction = p;
  else if (p && typeof p === 'object') {
    if (typeof p.fraction === 'number') fraction = p.fraction;
    else if (typeof p.done === 'number' && p.total) fraction = p.done / p.total;
    stage = p.stage || p.message || p.label || stage;
  }
  app.gen.fraction = Math.max(0, Math.min(1, fraction || 0));
  app.gen.stage = stage;
  updateGenPanel();
}

async function startGenerate() {
  const { profile, errors } = currentValidation();
  if (errors.length) {
    app.gen = { ...app.gen, status: 'error', error: 'Some answers still need a look (see "Check your answers" above).' };
    updateGenPanel();
    document.getElementById('final-check')?.scrollIntoView({ block: 'start' });
    return;
  }
  const keyOk = app.key.status === 'ok' && app.key.key === draft.access.access_key;
  if (!keyOk) {
    app.gen = { ...app.gen, status: 'running', fraction: 0, stage: 'Checking your access key' };
    updateGenPanel();
    const ok = await runKeyCheck();
    if (!ok) {
      app.gen = { ...app.gen, status: 'error', error: keyStatusText() };
      updateGenPanel();
      return;
    }
  }
  if (app.gen.url) URL.revokeObjectURL(app.gen.url);
  app.controller = new AbortController();
  app.gen = { ...app.gen, status: 'running', fraction: 0, stage: 'Loading the kit', error: '', url: null };
  updateGenPanel();
  try {
    ensureKit();
    const k = await loadKit();
    const blob = await generateBinder(profile, k.kit, {
      relay: config.relayBase, size: app.size, onProgress, signal: app.controller.signal,
    });
    if (!(blob instanceof Blob)) throw new Error('The generator returned no file.');
    app.gen = { ...app.gen, status: 'done', fraction: 1, url: URL.createObjectURL(blob), bytes: blob.size, size: app.size };
  } catch (err) {
    if (err && err.name === 'AbortError') app.gen = { ...app.gen, status: 'cancelled', fraction: 0 };
    else app.gen = { ...app.gen, status: 'error', error: `Something went wrong while making your binder: ${err && err.message ? err.message : err}. Your answers are still here; you can try again.` };
  } finally {
    app.controller = null;
    updateGenPanel();
  }
}

function renderFinal() {
  const est = sizeEstimates(env.kitState.kit);
  main.append(
    h('h1', { id: 'step-title', tabindex: '-1' }, 'Make your binder'),
    noticeFull(NOTICE.neverStored, 'never-stored'),
    noticeFull(NOTICE.privateCopy, 'private-copy'),
    finalCheck(),
    h('section', { class: 'panel', 'aria-labelledby': 'save-title' },
      h('h2', { id: 'save-title' }, '2. Save your answers (optional)'),
      h('p', {}, draft.access?.save_profile_locally
        ? 'You asked for a file of your answers. Save it now, before you generate; it is the only way to come back later without typing everything again.'
        : 'A file of your answers lets you rebuild or upgrade your binder later without typing everything again. It stays on your device.'),
      h('label', { class: 'choice single', for: 'include-key' },
        h('input', { type: 'checkbox', id: 'include-key', checked: app.includeKeyInFile || undefined,
          onchange: (e) => { app.includeKeyInFile = e.target.checked; } }),
        h('span', { class: 'choice-text' }, 'Include my access key in the file (so the file works on its own; keep it private)')),
      h('button', { type: 'button', class: 'btn' + (draft.access?.save_profile_locally ? ' primary' : ''), id: 'final-save-btn', onclick: saveAnswers }, 'Save my answers (profile.json)'),
      h('p', { id: 'final-status', class: 'final-status', role: 'status', 'aria-live': 'polite' }),
      env.keepToggleUI()),
    sizeChoice(est),
    genPanel(),
    h('div', { class: 'bottomnav' },
      h('button', { type: 'button', class: 'btn ghost', onclick: () => goto(FINAL - 1) }, 'Back')));
  loadGenerator().then(g => { if (g.stub !== app.gen.stub) { app.gen.stub = g.stub; updateGenPanel(); } });
}

// ---- theme ------------------------------------------------------------------------------------
const THEMES = ['auto', 'dark', 'light'];
let theme = 'auto';
function setTheme(t) {
  theme = t;
  if (t === 'auto') delete document.documentElement.dataset.theme; else document.documentElement.dataset.theme = t;
  const b = document.getElementById('theme-btn');
  if (b) b.textContent = `Theme: ${t === 'auto' ? 'Auto' : t === 'dark' ? 'Dark' : 'Light'}`;
}

// ---- start ------------------------------------------------------------------------------------
async function start() {
  document.getElementById('theme-btn')?.addEventListener('click', () => setTheme(THEMES[(THEMES.indexOf(theme) + 1) % THEMES.length]));
  setTheme('auto');
  window.addEventListener('beforeunload', (e) => {
    if (app.gen.status === 'running' || (app.dirty && !app.keep)) { e.preventDefault(); e.returnValue = ''; }
  });
  env.kitState = { loading: true, cards: [], kit: null };
  env.regions = await loadRegions();
  const kept = readKept();
  if (kept) {
    try {
      loadProfile(kept.profile);
      app.keep = true;
      app.step = Number.isInteger(kept.step) ? Math.max(0, Math.min(FINAL, kept.step)) : 0;
      app.flash = { text: 'Your answers were restored from this browser. Your access key was not kept; type it again before you generate.', kind: 'ok' };
    } catch { eraseKept(); }
  }
  render();
  if (app.step >= 7) ensureKit();
  document.documentElement.classList.add('ready');
}
start();

// for tests and debugging in the console; holds nothing that is not already on screen
window.__settings = { toProfile, validate: () => currentValidation(), goto, app, getAt, ptr, idOf };
