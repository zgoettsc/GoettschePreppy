#!/usr/bin/env node
// Build the relay's source allowlist: { key: url } for every source in
// sources/index.json plus sources/additions/*.json, written to
// worker/src/source-urls.json. Only keys and URLs are kept (no titles, no
// citing pages). The relay's /api/v1/fetch fetches nothing that is not here.
//
// Usage: node scripts/build-worker-index.mjs [--check]
//   --check  exit 1 if the written file would change (for CI), write nothing.

import { readFileSync, readdirSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const indexPath = join(root, "sources", "index.json");
const additionsDir = join(root, "sources", "additions");
const outPath = join(root, "worker", "src", "source-urls.json");
const checkOnly = process.argv.includes("--check");

function entriesOf(json, file) {
  if (Array.isArray(json)) return json;
  if (json && Array.isArray(json.sources)) return json.sources;
  throw new Error(`${file}: expected an array of sources (or {sources: [...]})`);
}

const warnings = [];
function usableUrl(raw, key, file) {
  let u;
  try {
    u = new URL(raw);
  } catch {
    warnings.push(`${file}: ${key}: not a URL, skipped`);
    return null;
  }
  if (u.protocol !== "https:" && u.protocol !== "http:") {
    warnings.push(`${file}: ${key}: scheme ${u.protocol} not allowed, skipped`);
    return null;
  }
  if (u.username || u.password) {
    warnings.push(`${file}: ${key}: credentials in URL, skipped`);
    return null;
  }
  if (u.port) {
    warnings.push(`${file}: ${key}: non-default port ${u.port}, skipped (relay refuses ports)`);
    return null;
  }
  if (/^\d+\.\d+\.\d+\.\d+$/.test(u.hostname) || u.hostname.startsWith("[")) {
    warnings.push(`${file}: ${key}: IP-address host, skipped`);
    return null;
  }
  u.hash = "";
  return u.href;
}

const map = new Map();
function add(list, file, { override }) {
  for (const s of list) {
    if (!s || typeof s.key !== "string" || !s.key) continue;
    if (typeof s.url !== "string" || !s.url) continue;
    const url = usableUrl(s.url, s.key, file);
    if (!url) continue;
    if (map.has(s.key) && map.get(s.key) !== url) {
      if (!override) {
        warnings.push(`${file}: duplicate key ${s.key} with a different URL; first kept`);
        continue;
      }
      warnings.push(`${file}: key ${s.key} already in index.json with a different URL; index.json kept`);
      continue;
    }
    map.set(s.key, url);
  }
}

add(entriesOf(JSON.parse(readFileSync(indexPath, "utf8")), "sources/index.json"), "sources/index.json", {
  override: false,
});
if (existsSync(additionsDir)) {
  for (const f of readdirSync(additionsDir).filter((n) => n.endsWith(".json")).sort()) {
    const file = `sources/additions/${f}`;
    let json;
    try {
      json = JSON.parse(readFileSync(join(additionsDir, f), "utf8"));
    } catch (e) {
      warnings.push(`${file}: not valid JSON, skipped`);
      continue;
    }
    add(entriesOf(json, file), file, { override: true });
  }
}

const sorted = Object.fromEntries([...map.entries()].sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0)));
const text = JSON.stringify(sorted, null, 1) + "\n";

for (const w of warnings) console.warn("warning:", w);
if (checkOnly) {
  const current = existsSync(outPath) ? readFileSync(outPath, "utf8") : "";
  if (current !== text) {
    console.error("worker/src/source-urls.json is out of date; run node scripts/build-worker-index.mjs");
    process.exit(1);
  }
  console.log(`worker/src/source-urls.json up to date (${map.size} sources)`);
} else {
  writeFileSync(outPath, text);
  console.log(`wrote worker/src/source-urls.json (${map.size} sources)`);
}
