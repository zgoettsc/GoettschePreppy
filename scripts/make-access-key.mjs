#!/usr/bin/env node
// Make, list and revoke relay access keys (decision G18: one key per friend).
//
// The relay stores only SHA-256 hashes, in the Worker secret ACCESS_KEYS
// (a JSON array of {label, sha256}). This script keeps that array in a local
// file (default access-keys.local.json, hashes only, never the keys) so you can
// re-upload the whole list after each change:
//
//   node scripts/make-access-key.mjs "Aunt May"           new key for a friend; adds the hash to the file
//   node scripts/make-access-key.mjs --list               show labels in the file
//   node scripts/make-access-key.mjs --remove "Aunt May"  revoke: drop that label from the file
//   node scripts/make-access-key.mjs --hash <key>         print the hash of an existing key
//   options: --file <path>   use another list file
//            --print-only    make a key and print it with its entry; do not touch the file
//
// After any change, upload the list:
//   npx wrangler@4 secret put ACCESS_KEYS < access-keys.local.json
//
// The key itself is printed once. Give it to the friend privately; it is not
// saved anywhere by this script.

import { randomBytes, createHash } from "node:crypto";
import { readFileSync, writeFileSync, existsSync } from "node:fs";

const args = process.argv.slice(2);
function opt(name) {
  const i = args.indexOf(name);
  if (i === -1) return undefined;
  const v = args[i + 1];
  args.splice(i, 2);
  return v;
}
function flag(name) {
  const i = args.indexOf(name);
  if (i === -1) return false;
  args.splice(i, 1);
  return true;
}

const file = opt("--file") || "access-keys.local.json";
const removeLabel = opt("--remove");
const hashKey = opt("--hash");
const list = flag("--list");
const printOnly = flag("--print-only");
const label = args.join(" ").trim();

const sha256 = (s) => createHash("sha256").update(s, "utf8").digest("hex");
const LABEL_RE = /^[A-Za-z0-9 _.'-]{1,40}$/;

function die(msg) {
  console.error(msg);
  process.exit(1);
}

function load() {
  if (!existsSync(file)) return [];
  let j;
  try {
    j = JSON.parse(readFileSync(file, "utf8"));
  } catch {
    die(`${file} is not valid JSON. Fix or delete it.`);
  }
  if (!Array.isArray(j)) die(`${file} must hold a JSON array.`);
  return j;
}

function save(entries) {
  writeFileSync(file, JSON.stringify(entries, null, 2) + "\n");
}

const UPLOAD = `npx wrangler@4 secret put ACCESS_KEYS < ${file}`;

if (hashKey !== undefined) {
  console.log(sha256(hashKey));
  process.exit(0);
}

if (list) {
  const entries = load();
  if (!entries.length) console.log(`${file}: no keys yet.`);
  for (const e of entries) console.log(`${e.label}\t${String(e.sha256).slice(0, 8)}…`);
  process.exit(0);
}

if (removeLabel !== undefined) {
  const entries = load();
  const kept = entries.filter((e) => e.label !== removeLabel);
  if (kept.length === entries.length) die(`No key labelled "${removeLabel}" in ${file}.`);
  save(kept);
  console.log(`Removed "${removeLabel}" from ${file} (${kept.length} keys left).`);
  console.log(`Now upload the list so the relay forgets that key:\n  ${UPLOAD}`);
  if (kept.length === 0) console.log("Note: with no keys left the relay refuses everyone.");
  process.exit(0);
}

if (!label) {
  die('Give the friend a label, e.g.: node scripts/make-access-key.mjs "Aunt May"');
}
if (!LABEL_RE.test(label)) die("Label: 1 to 40 letters, digits, spaces, dot, dash, underscore or apostrophe.");

// 32 random bytes = 256 bits, base64url, with a short prefix so it is
// recognisable when pasted.
const key = "gpk_" + randomBytes(32).toString("base64url");
const entry = { label, sha256: sha256(key) };

if (!printOnly) {
  const entries = load();
  if (entries.some((e) => e.label === label)) {
    die(`"${label}" already has a key in ${file}. Remove it first or pick another label.`);
  }
  entries.push(entry);
  save(entries);
}

console.log(`Access key for ${label} (give this to them privately; it is shown only once):\n`);
console.log(`  ${key}\n`);
console.log("Entry for ACCESS_KEYS:\n");
console.log(`  ${JSON.stringify(entry)}\n`);
if (!printOnly) console.log(`Added to ${file}. Now upload the list:\n  ${UPLOAD}`);
