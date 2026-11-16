// Settings page configuration. The owner edits this file before deploying (docs/10-deploy.md).
//
// relayBase: the Cloudflare Worker relay's address, with no trailing slash, for example
//   'https://goettschepreppy-relay.YOUR-ACCOUNT.workers.dev'.
//   Empty string means "same address as this page" (useful when a route sends /api/* to the Worker).
//   A page address with ?relay=<url> overrides it for testing (only https:// or same-origin paths).
//   A page address with ?dryrun=1 uses the built-in fake relay instead (no network, filler text).
//
// The other entries are paths relative to this file; they rarely need changing.
const here = (p) => new URL(p, import.meta.url).href;

function relayOverride() {
  try {
    const v = new URLSearchParams(location.search).get('relay');
    if (v && (/^https:\/\//.test(v) || v.startsWith('/'))) return v.replace(/\/+$/, '');
  } catch { /* no location (tests) */ }
  return null;
}

function flag(name) {
  try { return new URLSearchParams(location.search).get(name) === '1'; } catch { return false; }
}

export const config = {
  relayBase: relayOverride() ?? '',
  // ?dryrun=1 : test mode. The key check and generation talk to A3's fake relay
  // (app/lib/relay-dryrun.js) inside this tab; nothing is sent anywhere and AI-written text is filler.
  dryRun: flag('dryrun'),
  dryRunUrl: here('../lib/relay-dryrun.js'),
  kitUrl: here('../build/kit.json'),
  regionsUrl: here('../build/regions-lite.json'),
  cardsFixtureUrl: here('./fixtures/cards.json'),
  generatorUrl: here('../lib/generate.js'),
  // Shown on the Generate screen when kit.json does not carry its own estimates (decision G11).
  sizeEstimates: {
    small: { minMB: 30, maxMB: 60 },
    large: { minMB: 200, maxMB: 400 },
  },
};
