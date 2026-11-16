// Small DOM helpers and the question widgets. Every question shows its "why we ask" line.

import { getAt, setAt, ptr } from './state.js';

const hooks = { rerender: () => {}, changed: () => {} };
export function setHooks(h) { Object.assign(hooks, h); }

export function h(tag, attrs = {}, ...kids) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === undefined || v === null || v === false) continue;
    if (k === 'class') el.className = v;
    else if (k === 'html') el.innerHTML = v;
    else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
    else if (k === 'dataset') Object.assign(el.dataset, v);
    else el.setAttribute(k, v === true ? '' : v);
  }
  for (const kid of kids.flat(Infinity)) {
    if (kid === undefined || kid === null || kid === false) continue;
    el.append(kid instanceof Node ? kid : document.createTextNode(String(kid)));
  }
  return el;
}

export const idOf = (path, extra) => 'f-' + path.join('-') + (extra !== undefined ? '-' + String(extra).replace(/[^a-z0-9-]/gi, '_') : '');
const opts = (list) => list.map(o => (Array.isArray(o) ? { value: o[0], label: o[1] } : o));

function parseNum(raw, integer) {
  const t = String(raw).trim();
  if (t === '') return undefined;
  const n = Number(t.replace(/,/g, ''));
  if (!Number.isFinite(n)) return t; // keep the text; validation will say "type a number"
  return integer ? n : n;
}

function wrap(o, control, { group = false } = {}) {
  const paths = [ptr(o.path), ...(o.alsoPaths || []).map(ptr)].join(' ');
  const whyId = idOf(o.path, 'why');
  const errId = idOf(o.path, 'err');
  const label = group
    ? h('legend', { class: 'q-label' }, o.label, o.required ? h('span', { class: 'req' }, ' (needed)') : null)
    : h('label', { class: 'q-label', for: idOf(o.path) }, o.label, o.required ? h('span', { class: 'req' }, ' (needed)') : null);
  const why = o.why ? h('p', { class: 'why', id: whyId }, h('span', { class: 'why-tag' }, 'Why we ask: '), o.why) : null;
  const err = h('p', { class: 'err', id: errId, hidden: true });
  const box = h(group ? 'fieldset' : 'div', { class: 'q' + (o.class ? ' ' + o.class : ''), dataset: { paths } },
    label, why, control, err);
  return box;
}
const describedBy = (o) => [o.why ? idOf(o.path, 'why') : null, idOf(o.path, 'err')].filter(Boolean).join(' ');

function after(o) { if (o.then) o.then(getAt(o.path)); if (o.rerender) hooks.rerender(); else hooks.changed(); }

/** A question. o = { path, label, why, kind, options, required, ... } */
export function q(o) {
  const v = getAt(o.path);
  const common = { id: idOf(o.path), 'aria-describedby': describedBy(o), required: o.required || undefined };
  switch (o.kind || 'text') {
    case 'text': case 'password': case 'tel': {
      const input = h('input', {
        ...common, type: o.kind === 'password' && !o.reveal ? 'password' : o.kind === 'tel' ? 'tel' : 'text',
        value: v ?? '', maxlength: o.maxlength, placeholder: o.placeholder, autocomplete: o.autocomplete || 'off',
        spellcheck: o.kind === 'password' ? 'false' : undefined, autocapitalize: o.autocapitalize,
        oninput: (e) => { setAt(o.path, e.target.value === '' ? undefined : e.target.value); hooks.changed(); },
        onchange: () => { if (o.then) o.then(getAt(o.path)); if (o.rerender) hooks.rerender(); },
      });
      return wrap(o, o.after ? h('div', { class: 'row' }, input, o.after) : input);
    }
    case 'textarea': {
      const ta = h('textarea', {
        ...common, rows: o.rows || 3, maxlength: o.maxlength, placeholder: o.placeholder,
        oninput: (e) => { setAt(o.path, e.target.value === '' ? undefined : e.target.value); hooks.changed(); },
      });
      ta.value = v ?? '';
      return wrap(o, ta);
    }
    case 'int': case 'number': {
      const input = h('input', {
        ...common, type: 'text', inputmode: o.kind === 'int' ? 'numeric' : 'decimal', class: 'num',
        value: v ?? '', placeholder: o.placeholder, autocomplete: 'off',
        oninput: (e) => { setAt(o.path, parseNum(e.target.value, o.kind === 'int')); hooks.changed(); },
      });
      return wrap(o, o.unit ? h('div', { class: 'row' }, input, h('span', { class: 'unit' }, o.unit)) : input);
    }
    case 'select': {
      const sel = h('select', {
        ...common,
        onchange: (e) => { setAt(o.path, e.target.value === '' ? undefined : e.target.value); after(o); },
      }, o.noEmpty ? null : h('option', { value: '' }, o.emptyLabel || 'Choose…'),
      opts(o.options).map(x => h('option', { value: x.value, selected: v === x.value || undefined }, x.label)));
      return wrap(o, sel);
    }
    case 'radio': case 'yesno': {
      const choices = o.kind === 'yesno'
        ? [{ value: true, label: o.yes || 'Yes' }, { value: false, label: o.no || 'No' }, { value: '', label: o.skip || 'Not sure, skip' }]
        : opts(o.options).concat(o.skip ? [{ value: '', label: o.skip }] : []);
      const name = idOf(o.path);
      const items = choices.map((c, i) => {
        const checked = c.value === '' ? (v === undefined || v === null || v === '') : v === c.value;
        const id = i === 0 ? idOf(o.path) : idOf(o.path, String(c.value) || 'skip');
        return h('label', { class: 'choice', for: id },
          h('input', {
            type: 'radio', name, id, value: String(c.value), checked: checked || undefined,
            'aria-describedby': i === 0 ? describedBy(o) : undefined,
            onchange: () => { setAt(o.path, c.value === '' ? undefined : c.value); after(o); },
          }),
          h('span', { class: 'choice-text' }, c.label, c.hint ? h('span', { class: 'hint' }, c.hint) : null));
      });
      return wrap(o, h('div', { class: 'choices' + (o.inline ? ' inline' : ''), role: o.kind === 'yesno' ? undefined : undefined }, items), { group: true });
    }
    case 'multi': {
      const cur = Array.isArray(v) ? v : [];
      const items = opts(o.options).map((c, i) => {
        const id = i === 0 ? idOf(o.path) : idOf(o.path, c.value);
        return h('label', { class: 'choice', for: id },
          h('input', {
            type: 'checkbox', id, value: c.value, checked: cur.includes(c.value) || undefined,
            'aria-describedby': i === 0 ? describedBy(o) : undefined,
            onchange: (e) => {
              let next = (Array.isArray(getAt(o.path)) ? getAt(o.path) : []).filter(x => x !== c.value);
              if (e.target.checked) {
                if (o.exclusive && c.value === o.exclusive) next = [];
                else if (o.exclusive) next = next.filter(x => x !== o.exclusive);
                next.push(c.value);
              }
              setAt(o.path, next.length ? next : undefined);
              if (o.exclusive || o.rerender) hooks.rerender(); else hooks.changed();
            },
          }),
          h('span', { class: 'choice-text' }, c.label, c.hint ? h('span', { class: 'hint' }, c.hint) : null));
      });
      return wrap(o, h('div', { class: 'choices' + (o.columns ? ' cols' : '') }, items), { group: true });
    }
    case 'check': {
      const id = idOf(o.path);
      const box = h('label', { class: 'choice single', for: id },
        h('input', {
          type: 'checkbox', id, checked: v === true || undefined, 'aria-describedby': describedBy(o), required: o.required || undefined,
          onchange: (e) => { setAt(o.path, e.target.checked ? true : (o.falseWhenOff ? false : undefined)); after(o); },
        }),
        h('span', { class: 'choice-text' }, o.text || o.label));
      return wrap({ ...o, label: o.text ? o.label : o.groupLabel || '' }, box, { group: true });
    }
    default: throw new Error('unknown kind ' + o.kind);
  }
}

/** A group of related questions (fieldset). */
export function group(title, why, ...kids) {
  return h('fieldset', { class: 'group' }, h('legend', { class: 'group-title' }, title),
    why ? h('p', { class: 'why' }, h('span', { class: 'why-tag' }, 'Why we ask: '), why) : null, kids);
}

/**
 * An add-and-remove list.
 * o = { path, title, why, itemName, max, min, make(), item(path, i) -> nodes, addLabel, empty }
 */
export function list(o) {
  let arr = getAt(o.path);
  if (!Array.isArray(arr)) { arr = []; }
  const min = o.min || 0;
  const items = arr.map((_, i) => {
    const ip = [...o.path, i];
    const headId = idOf(ip, 'head');
    return h('section', { class: 'item', 'aria-labelledby': headId },
      h('div', { class: 'item-head' },
        h('h4', { id: headId, tabindex: '-1' }, `${o.itemName} ${i + 1}`, o.itemTitle ? h('span', { class: 'item-sub' }, o.itemTitle(arr[i] || {})) : null),
        h('button', {
          type: 'button', class: 'btn small ghost', disabled: arr.length <= min || undefined,
          'aria-label': `Remove ${o.itemName.toLowerCase()} ${i + 1}`,
          onclick: () => {
            const a = getAt(o.path); a.splice(i, 1);
            hooks.rerender({ focus: a.length ? idOf([...o.path, Math.max(0, i - 1)], 'head') : idOf(o.path, 'add') });
          },
        }, 'Remove')),
      o.item(ip, i));
  });
  const full = o.max !== undefined && arr.length >= o.max;
  const add = h('button', {
    type: 'button', class: 'btn add', id: idOf(o.path, 'add'), disabled: full || undefined,
    onclick: () => {
      const a = Array.isArray(getAt(o.path)) ? getAt(o.path) : (setAt(o.path, []), getAt(o.path));
      a.push(o.make ? o.make() : {});
      hooks.rerender({ focus: idOf([...o.path, a.length - 1], 'head') });
    },
  }, '+ ', o.addLabel || `Add ${o.itemName.toLowerCase()}`);
  const paths = ptr(o.path);
  return h('fieldset', { class: 'q list', dataset: { paths } },
    h('legend', { class: 'q-label' }, o.title, o.required ? h('span', { class: 'req' }, ' (needed)') : null),
    o.why ? h('p', { class: 'why' }, h('span', { class: 'why-tag' }, 'Why we ask: '), o.why) : null,
    items.length ? items : h('p', { class: 'muted' }, o.empty || 'None added.'),
    h('p', { class: 'err', id: idOf(o.path, 'err'), hidden: true }),
    add, full ? h('p', { class: 'muted small' }, `That is the most this list takes (${o.max}).`) : null);
}

export function noticeBlock(n, { collapsedTail = false, cls = '' } = {}) {
  const [first, ...rest] = n.paragraphs;
  return h('section', { class: 'notice ' + cls, 'aria-label': n.title },
    h('h2', { class: 'notice-title' }, n.title),
    h('p', { html: first }),
    collapsedTail && rest.length
      ? h('details', { class: 'notice-more' }, h('summary', {}, 'And when you press Generate…'), rest.map(p => h('p', { html: p })))
      : rest.map(p => h('p', { html: p })));
}
