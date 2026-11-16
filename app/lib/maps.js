// maps.js — USGS topo maps for the Large download (decision G16).
//
// Which maps: the home county and each destination county; with opts.routeMaps also every county
// the straight line from home to a destination crosses (docs/02 step 5: no driving route).
// Where from: the county's own `topo_maps` list in the region data when D1 supplies one; otherwise a
// search of the USGS National Map (TNM Access API, "US Topo" GeoPDF) for the quad at the county's
// centroid, all through the relay's /fetch-map (A1 allows tnmaccess.nationalmap.gov/api/v1/ and the
// USGS download hosts). A US Topo GeoPDF is 20 to 60 MB, so the number of maps is capped
// (opts.maxMaps, default 12: home and destinations first, then route counties nearest home); the
// rest are listed on "Sources not captured" by title so the household can fetch them while it can.
//
// County fields used (notes/workers/A3.md §1.1): centroid [lat, lon], bbox [west, south, east, north].

import { findCounty } from './context.js';

const TNM = 'https://tnmaccess.nationalmap.gov/api/v1/products';

export function countyGeo(kit, state, county) {
  const hit = findCounty(kit?.regions?.[state], county);
  if (!hit) return null;
  return { state, county: hit.name, centroid: hit.data.centroid || null, bbox: hit.data.bbox || null, topo_maps: kit?.maps?.[state]?.[hit.name] || [] };
}

// Counties whose bbox contains a point on the straight line between two centroids.
export function routeCounties(kit, from, to, stepMiles = 5) {
  if (!from?.centroid || !to?.centroid) return [];
  const [lat1, lon1] = from.centroid, [lat2, lon2] = to.centroid;
  const miles = Math.hypot((lat2 - lat1) * 69, (lon2 - lon1) * 69 * Math.cos(((lat1 + lat2) / 2) * Math.PI / 180));
  const n = Math.max(2, Math.ceil(miles / stepMiles));
  const all = [];
  for (const [st, obj] of Object.entries(kit?.regions || {})) for (const [name, c] of Object.entries(obj.counties || {})) if (Array.isArray(c.bbox)) all.push({ st, name, bbox: c.bbox });
  const seen = new Map();
  for (let i = 1; i < n; i++) {
    const lat = lat1 + (lat2 - lat1) * i / n, lon = lon1 + (lon2 - lon1) * i / n;
    for (const c of all) {
      const [w, s, e, no] = c.bbox;
      if (lon >= w && lon <= e && lat >= s && lat <= no) { const k = `${c.st}|${c.name}`; if (!seen.has(k)) seen.set(k, { order: i, st: c.st, name: c.name }); }
    }
  }
  return [...seen.values()].sort((a, b) => a.order - b.order)
    .filter(c => !(c.st === from.state && c.name === from.county) && !(c.st === to.state && c.name === to.county))
    .map(c => countyGeo(kit, c.st, c.name));
}

// Route counties are opt-in (opts.route): each is another 20 to 60 MB map. mapPlan() gives the
// settings page the counts and a size range to show before the household decides.
export const MAP_MB = { min: 20, max: 60 };
export function mapTargets(kit, ctx, { route = false } = {}) {
  const home = countyGeo(kit, ctx.home.state, ctx.region.home.county);
  const targets = [];
  const add = (g, why) => { if (g && !targets.some(t => t.state === g.state && t.county === g.county)) targets.push({ ...g, why }); };
  add(home, 'home county');
  const dests = ctx.destinations.map(d => countyGeo(kit, d.region?.state, d.region?.county));
  dests.forEach((g, i) => add(g, `destination: ${ctx.destinations[i].name}`));
  if (route) dests.forEach((g, i) => { for (const r of routeCounties(kit, home, g)) add(r, `on the way to ${ctx.destinations[i].name}`); });
  return targets;
}

export function mapPlan(kit, ctx) {
  const base = mapTargets(kit, ctx);
  const all = mapTargets(kit, ctx, { route: true });
  const mb = n => ({ min_mb: n * MAP_MB.min, max_mb: n * MAP_MB.max });
  return { base: { count: base.length, ...mb(base.length), counties: base.map(t => `${t.county}, ${t.state}`) },
    route: { count: all.length - base.length, ...mb(all.length - base.length), counties: all.slice(base.length).map(t => `${t.county}, ${t.state}`) } };
}

async function searchTopo(relay, t, signal) {
  if (!t.centroid) return [];
  const [lat, lon] = t.centroid, d = 0.01;
  const q = `${TNM}?datasets=${encodeURIComponent('US Topo')}&prodFormats=GeoPDF&max=1&bbox=${lon - d},${lat - d},${lon + d},${lat + d}`;
  const r = await relay.fetchMap(q, { signal });
  if (!r.ok) return [];
  try {
    const j = JSON.parse(new TextDecoder().decode(r.bytes));
    return (j.items || []).filter(x => x.downloadURL).slice(0, 1).map(x => ({ title: `${x.title || 'USGS US Topo map'} (${t.county}, ${t.state})`, url: x.downloadURL, date: x.publicationDate || '' }));
  } catch { return []; }
}

// → [{ title, why, ok, bytes, contentType, reason }]
export async function fetchTopoMaps(relay, targets, { maxMaps = 12, signal } = {}) {
  const out = [];
  for (const t of targets) {
    signal?.throwIfAborted?.();
    if (!relay) { out.push({ title: `Topo map, ${t.county}, ${t.state}`, why: t.why, ok: false, reason: 'no relay' }); continue; }
    if (out.filter(x => x.ok).length >= maxMaps) { out.push({ title: `USGS US Topo map, ${t.county}, ${t.state}`, why: t.why, ok: false, reason: `left out to keep the file size down (${maxMaps} maps bound)` }); continue; }
    let list = t.topo_maps?.length ? t.topo_maps : [];
    try { if (!list.length) list = await searchTopo(relay, t, signal); } catch (e) { if (e.name === 'AbortError') throw e; }
    if (!list.length) { out.push({ title: `USGS US Topo map, ${t.county}, ${t.state}`, why: t.why, ok: false, reason: t.centroid ? 'no map found or the map service did not answer' : 'no county location in the region data' }); continue; }
    for (const m of list.slice(0, 1)) {
      try {
        const r = await relay.fetchMap(m.url, { signal });
        out.push(r.ok ? { title: m.title, date: m.date, why: t.why, ok: true, bytes: r.bytes, contentType: r.contentType || 'application/pdf' }
          : { title: m.title, why: t.why, ok: false, reason: `map download failed (HTTP ${r.status})` });
      } catch (e) { if (e.name === 'AbortError') throw e; out.push({ title: m.title, why: t.why, ok: false, reason: 'map download failed' }); }
    }
  }
  return out;
}
