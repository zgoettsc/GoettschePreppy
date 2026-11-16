// template.js — the page template language of docs/09-authoring-spec.md §4, nothing more.
//
//   {{ path }}                         value from the context; missing/empty → fill-in blank
//   {{#if flag}} … {{else}} … {{/if}}  flag from the context; `!flag` negates; nesting allowed
//   {{#each list as x}} … {{x.field}} … {{else}} … {{/each}}
//   {{choice DC-NN}}  {{card DC-NN}}  {{photo slot-id}}  {{figure fig-id}}  {{plates}}  {{ai block-id}}
//
// Runs in the browser and in node (no imports). Rendering happens before Markdown, so values are
// escaped for both HTML and Markdown. The special forms ({{choice}}, {{photo}} …) are delegated to
// hooks supplied by the caller (generate.js); without a hook they render a plain placeholder.
//
// Block tags that stand alone on a line remove that whole line, so `{{#if}}` lines inside lists and
// tables leave no blank lines behind.

export const BLANK_HTML = '<span class="blank">__________<small> (fill in)</small></span>';

export class TemplateError extends Error {
  constructor(message, pos) { super(message); this.name = 'TemplateError'; this.pos = pos; }
}

const TAG_RE = /\{\{\s*([\s\S]*?)\s*\}\}/g;
const BLOCK = /^(#if\s|#each\s|else$|\/if$|\/each$)/;

// ---- tokenizer ---------------------------------------------------------------------------------
export function tokenize(src) {
  const toks = [];
  let last = 0;
  src = String(src ?? '');
  for (const m of src.matchAll(TAG_RE)) {
    let start = m.index, end = m.index + m[0].length;
    const tag = m[1].trim();
    if (BLOCK.test(tag)) {
      // standalone line: only whitespace between the previous newline and the tag, and between
      // the tag and the next newline (or end of text) → swallow the line.
      const ls = src.lastIndexOf('\n', start - 1) + 1;
      let le = src.indexOf('\n', end); if (le < 0) le = src.length;
      if (ls >= last && /^[ \t]*$/.test(src.slice(ls, start)) && /^[ \t]*$/.test(src.slice(end, le))) {
        start = ls; end = le < src.length ? le + 1 : le;
      }
    }
    if (start > last) toks.push({ type: 'text', text: src.slice(last, start) });
    toks.push({ type: 'tag', tag, pos: m.index });
    last = end;
  }
  if (last < src.length) toks.push({ type: 'text', text: src.slice(last) });
  return toks;
}

// ---- parser → tree -----------------------------------------------------------------------------
export function parse(src) {
  const root = { type: 'root', children: [] };
  const stack = [root];
  const top = () => stack[stack.length - 1];
  const push = n => { const t = top(); (t.inElse ? t.elseChildren : t.children).push(n); };
  for (const t of tokenize(src)) {
    if (t.type === 'text') { push(t); continue; }
    const tag = t.tag;
    let m;
    if ((m = /^#if\s+(!?)([A-Za-z0-9_.\-]+)$/.exec(tag))) {
      const n = { type: 'if', neg: !!m[1], path: m[2], children: [], elseChildren: [], inElse: false, pos: t.pos };
      push(n); stack.push(n);
    } else if ((m = /^#each\s+([A-Za-z0-9_.\-]+)\s+as\s+([A-Za-z_][A-Za-z0-9_]*)$/.exec(tag))) {
      const n = { type: 'each', path: m[1], as: m[2], children: [], elseChildren: [], inElse: false, pos: t.pos };
      push(n); stack.push(n);
    } else if (tag === 'else') {
      const n = top();
      if (n.type === 'root' || n.inElse) throw new TemplateError('{{else}} without an open {{#if}} or {{#each}}', t.pos);
      n.inElse = true;
    } else if (tag === '/if' || tag === '/each') {
      const n = top();
      if (n.type !== tag.slice(1)) throw new TemplateError(`{{${tag}}} does not close ${n.type === 'root' ? 'anything' : '{{#' + n.type + '}}'}`, t.pos);
      stack.pop();
    } else if ((m = /^(choice|card)\s+(DC-\d{2})$/.exec(tag))) push({ type: m[1], id: m[2] });
    else if ((m = /^photo\s+([a-z0-9-]+)$/.exec(tag))) push({ type: 'photo', id: m[1] });
    else if ((m = /^figure\s+(fig-[a-z0-9-]+)$/.exec(tag))) push({ type: 'figure', id: m[1] });
    else if (tag === 'plates') push({ type: 'plates' });
    else if ((m = /^ai\s+([a-z0-9-]+)$/.exec(tag))) push({ type: 'ai', id: m[1] });
    else if (/^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z0-9_\-]+)*$/.test(tag)) push({ type: 'value', path: tag, pos: t.pos });
    else throw new TemplateError(`unrecognised template tag {{${tag}}}`, t.pos);
  }
  if (stack.length > 1) throw new TemplateError(`{{#${top().type}}} is never closed`, top().pos);
  return root;
}

// ---- values ------------------------------------------------------------------------------------
export function lookup(path, scopes) {
  const parts = path.split('.');
  for (let i = scopes.length - 1; i >= 0; i--) {
    const s = scopes[i];
    if (s && Object.prototype.hasOwnProperty.call(s, parts[0])) return walk(s[parts[0]], parts.slice(1));
  }
  return undefined;
}
function walk(v, parts) {
  for (let i = 0; i < parts.length; i++) {
    if (v == null) return undefined;
    // keys may themselves contain dots-free hyphens (has.condition.CL-01) — plain property access
    v = v[parts[i]];
  }
  return v;
}

export function isEmpty(v) {
  return v === undefined || v === null || v === '' || (typeof v === 'number' && !Number.isFinite(v)) ||
    (Array.isArray(v) && v.length === 0);
}

export function truthy(v) {
  if (Array.isArray(v)) return v.length > 0;
  return !!v;
}

// Escape household text for HTML and for Markdown (so a typed "*" or "|" cannot break a table).
export function escapeValue(s) {
  return String(s).replace(/[&<>"'*_`[\]|\\#~]/g, c => '&#' + c.charCodeAt(0) + ';')
    .replace(/\r?\n/g, ' ');
}

export function formatValue(v) {
  if (isEmpty(v)) return null;
  if (typeof v === 'boolean') return v ? 'yes' : 'no';
  // schema/context.json "formatting": numbers with thousands separators, arrays as "a, b and c"
  if (typeof v === 'number') return v.toLocaleString('en-US', { maximumFractionDigits: 2 });
  if (Array.isArray(v)) {
    const parts = v.map(formatValue).filter(x => x !== null);
    if (!parts.length) return null;
    return parts.length === 1 ? parts[0] : parts.slice(0, -1).join(', ') + ' and ' + parts[parts.length - 1];
  }
  if (typeof v === 'object') return v.text != null ? formatValue(v.text) : (v.name != null ? formatValue(v.name) : null);
  return String(v);
}

// ---- render ------------------------------------------------------------------------------------
// hooks: { choice(id, scopes), card(id, scopes), photo(id), figure(id), plates(), ai(id, scopes),
//          onBlank(path), blank: string }
export function render(src, context, hooks = {}) {
  const tree = typeof src === 'string' ? parse(src) : src;
  const blank = hooks.blank ?? BLANK_HTML;
  const out = [];
  const run = (nodes, scopes) => {
    for (const n of nodes) {
      switch (n.type) {
        case 'text': out.push(n.text); break;
        case 'value': {
          const v = formatValue(lookup(n.path, scopes));
          if (v === null) { hooks.onBlank?.(n.path); out.push(blank); }
          else out.push(escapeValue(v));
          break;
        }
        case 'if': {
          const v = truthy(lookup(n.path, scopes));
          run((v !== n.neg) ? n.children : n.elseChildren, scopes);
          break;
        }
        case 'each': {
          const list = lookup(n.path, scopes);
          if (Array.isArray(list) && list.length) {
            for (const item of list) run(n.children, [...scopes, { [n.as]: item }]);
          } else run(n.elseChildren, scopes);
          break;
        }
        case 'choice': out.push(hooks.choice ? hooks.choice(n.id, scopes) : `(choice ${n.id})`); break;
        case 'card': out.push(hooks.card ? hooks.card(n.id, scopes) : `(card ${n.id})`); break;
        case 'photo': out.push(hooks.photo ? hooks.photo(n.id, scopes) : `(photo ${n.id})`); break;
        case 'figure': out.push(hooks.figure ? hooks.figure(n.id, scopes) : `(figure ${n.id})`); break;
        case 'plates': out.push(hooks.plates ? hooks.plates(scopes) : ''); break;
        case 'ai': out.push(hooks.ai ? hooks.ai(n.id, scopes) : blank); break;
      }
    }
  };
  run(tree.children, [context]);
  return out.join('');
}

// Every tag a template uses (for checks and for collecting ai blocks without rendering).
export function listTags(src) {
  return tokenize(src).filter(t => t.type === 'tag').map(t => t.tag);
}
