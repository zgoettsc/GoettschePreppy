// Loading the kit's data files. Each loader tolerates a missing file and a few plausible shapes,
// because app/build/* is produced by another worker (A3) and may change shape before launch.

import { config } from './config.js';

async function getJSON(url) {
  const res = await fetch(url, { cache: 'no-cache' });
  if (!res.ok) throw new Error(`${res.status}`);
  return res.json();
}

// ---- regions-lite.json: state -> counties --------------------------------------------------
let regionsPromise = null;
/** Resolves to { available: boolean, counties: { [state]: string[] } }. */
export function loadRegions() {
  regionsPromise ??= getJSON(config.regionsUrl).then(normaliseRegions).catch(() => ({ available: false, counties: {} }));
  return regionsPromise;
}
export function normaliseRegions(raw) {
  const src = raw && (raw.states || raw.counties || raw);
  const counties = {};
  if (src && typeof src === 'object') {
    for (const [st, v] of Object.entries(src)) {
      if (!/^[A-Z]{2}$/.test(st)) continue;
      const list = Array.isArray(v) ? v : (v && (v.counties || v.county_list)) || [];
      const names = list.map(c => (typeof c === 'string' ? c : c && (c.name || c.county))).filter(Boolean).map(String);
      if (names.length) counties[st] = [...new Set(names)].sort((a, b) => a.localeCompare(b));
    }
  }
  return { available: Object.keys(counties).length > 0, counties };
}

// ---- kit.json (or the cards fixture) -------------------------------------------------------
let kitPromise = null;
/** Resolves to { kit: object|null, cards: Card[], source: 'kit'|'fixture'|'none' }. */
export function loadKit() {
  kitPromise ??= (async () => {
    let kit = null;
    try { kit = await getJSON(config.kitUrl); } catch { kit = null; }
    const fromKit = kit ? cardsFromKit(kit) : [];
    if (fromKit.length) return { kit, cards: fromKit, source: 'kit' };
    try {
      const fx = await getJSON(config.cardsFixtureUrl);
      return { kit, cards: cardsFromKit(fx), source: 'fixture' };
    } catch {
      return { kit, cards: [], source: 'none' };
    }
  })();
  return kitPromise;
}

/** Card = { card: 'DC-NN', title, settings_summary, options: [{id,label,summary}] } */
export function cardsFromKit(kit) {
  const seen = new Map();
  const consider = (p) => {
    if (!p || typeof p !== 'object') return;
    const fm = p.frontmatter || p.data || p.meta || p;
    const id = fm.card || p.card;
    if (!id || !/^DC-\d{2}$/.test(id)) return;
    seen.set(id, {
      card: id,
      title: fm.title || p.title || id,
      settings_summary: fm.settings_summary || p.settings_summary || '',
      options: Array.isArray(fm.options || p.options) ? (fm.options || p.options).filter(o => o && o.id) : [],
    });
  };
  const lists = [kit.cards, kit.pages];
  for (const l of lists) {
    if (Array.isArray(l)) l.forEach(consider);
    else if (l && typeof l === 'object') Object.values(l).forEach(consider);
  }
  return [...seen.values()].sort((a, b) => a.card.localeCompare(b.card));
}

/** Size estimates for the Generate screen: kit.json may carry its own. */
export function sizeEstimates(kit) {
  const e = kit && (kit.size_estimates || kit.estimates || kit.sizes);
  const pick = (k) => {
    const v = e && e[k];
    if (v && typeof v === 'object' && (v.minMB || v.min_mb)) return { minMB: v.minMB ?? v.min_mb, maxMB: v.maxMB ?? v.max_mb ?? v.minMB ?? v.min_mb };
    if (typeof v === 'number') return { minMB: v, maxMB: v };
    return config.sizeEstimates[k];
  };
  return { small: pick('small'), large: pick('large') };
}
