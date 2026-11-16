# Deploying GoettschePreppy (owner guide)

This guide assumes you have never used Cloudflare. It puts two things on the internet, both on
Cloudflare's free `pages.dev` / `workers.dev` addresses (decision G12):

| Piece | What it is | Where it comes from |
|---|---|---|
| **Settings site** (Cloudflare Pages) | The static pages friends open to fill in their profile and download their binder. | The `app/` folder. |
| **Relay** (Cloudflare Worker) | A small program that holds your Anthropic API key, checks each friend's access key, passes generation requests to Claude, and fetches source documents and USGS maps for Large binders. It stores nothing except a monthly request count per friend. | `worker/` and `wrangler.toml`. |

You type every command below in a terminal, in the repository folder (`goettschepreppy`).
`npx wrangler@4 ...` downloads Cloudflare's command-line tool the first time; nothing to install
by hand except Node.js.

Time needed: about 45 minutes the first time.

---

## 0. What you need first

1. **Node.js 20 or newer.** Check with `node --version`. If it is missing or older, install the
   "LTS" version from nodejs.org.
2. **Your Anthropic API key** (decision G14). In the Claude Console (platform.claude.com), go to
   **API keys**, create a key named `goettschepreppy-relay`, and copy it somewhere safe for the next
   few minutes. It starts with `sk-ant-`.
3. **A spending limit** on that Anthropic account (Console, **Settings**, **Limits**). A binder costs
   roughly $15 to $25 to generate (`docs/01-architecture.md` section 6); set a monthly limit you are
   comfortable with for the number of friends you plan to invite.

## 1. Create a Cloudflare account

1. Go to dash.cloudflare.com/sign-up, enter an email and password, and confirm the email Cloudflare
   sends you. No credit card is needed for the free plan.
2. You do not need to add a website or domain. Skip any "add a site" prompts.

## 2. Log the command-line tool in

```sh
npx wrangler@4 --version      # first run downloads it; answer "y" if asked to install
npx wrangler@4 login          # opens a browser page; click "Allow"
npx wrangler@4 whoami         # should print your email and account
```

If the browser does not open (for example over SSH), copy the address the command prints into a
browser on the same machine.

## 3. Create the counter store (Workers KV)

The relay keeps one number per friend per month, in a Cloudflare KV namespace called `COUNTS`.

```sh
npx wrangler@4 kv namespace create COUNTS
```

It prints a block that contains an `id = "..."` (a long hexadecimal string). Open `wrangler.toml`
and replace `REPLACE-WITH-KV-NAMESPACE-ID` with that id. If wrangler offers to update the file for
you, you may say yes instead; check afterwards that `wrangler.toml` has exactly one
`[[kv_namespaces]]` block with `binding = "COUNTS"`.

## 4. Create the Pages project (to learn the settings site's address)

```sh
npx wrangler@4 pages project create goettschepreppy --production-branch main
```

Your site's address will be `https://goettschepreppy.pages.dev`. If the name is taken, pick
another (for example `goettschepreppy-binders`) and use that name everywhere below.

Open `wrangler.toml` and set:

```toml
PAGES_ORIGIN = "https://goettschepreppy.pages.dev"
```

Exactly the address, `https://` included, no trailing slash, no path. The relay refuses browser
requests from any other address.

## 5. Build and test the relay

```sh
npm install                   # once, for the repository's own tools
npm run test:worker           # builds worker/src/source-urls.json, runs the relay tests
```

You should see `# fail 0`. The tests use a fake Anthropic server and a fake key; nothing is sent
anywhere.

`worker/src/source-urls.json` is the list of the only documents the relay will fetch: every source
key and URL from `sources/index.json` and `sources/additions/*.json`. **Whenever the source index
changes, run `npm run test:worker` again and redeploy the relay (step 6)**, or the relay will not
fetch the new sources.

## 6. Deploy the relay

```sh
npx wrangler@4 deploy
```

The first time, wrangler may ask you to choose a `workers.dev` subdomain (for example your name).
Pick one; it is part of the relay's address. When it finishes it prints an address like:

```
https://goettschepreppy-relay.YOUR-SUBDOMAIN.workers.dev
```

Write it down. That is the relay.

## 7. Give the relay its secrets

Secrets are stored encrypted by Cloudflare. They never go in a file in this repository.

**Your Anthropic API key:**

```sh
npx wrangler@4 secret put ANTHROPIC_API_KEY
```

Paste the `sk-ant-...` key when asked and press Enter. Then delete the copy you made in step 0.

**The first access key (for yourself, to test):**

```sh
node scripts/make-access-key.mjs "Owner"
npx wrangler@4 secret put ACCESS_KEYS < access-keys.local.json
```

The first command prints a key that starts with `gpk_`. Keep it: that is your own access key. The
file `access-keys.local.json` holds only the hashes (labels plus SHA-256), never the keys; keep it
on your computer, because you re-upload it every time you add or remove a friend. Do not commit it.

**Check the relay.** Open this address in a browser:

```
https://goettschepreppy-relay.YOUR-SUBDOMAIN.workers.dev/api/v1/health
```

You should see `"anthropic_api_key":true`, `"access_keys":1`, `"counts":true`,
`"pages_origin":true` and a `sources` count. If one is `false` or `0`, redo that step. (Secrets take
effect within a few seconds; no redeploy is needed.)

## 8. Point the settings site at the relay

Open `app/settings/config.js` and set `relayBase` to the relay address from step 6, no trailing
slash:

```js
relayBase: relayOverride() ?? 'https://goettschepreppy-relay.YOUR-SUBDOMAIN.workers.dev',
```

## 9. Build and deploy the settings site

Build the app's data files, then upload the `app/` folder:

```sh
node scripts/build-kit.mjs          # kit.json and regions-lite.json into app/build/
npm run build:settings              # the settings page's profile validator
npx wrangler@4 pages deploy app --project-name goettschepreppy --branch main
```

(If `notes/workers/A2.md` or `notes/workers/A3.md` names further build steps, run those before the
upload.) Wrangler may print a warning that `wrangler.toml` is "missing pages_build_output_dir" and
that it is ignoring it. That is expected: that file is for the relay, not for Pages.

Pages limits each file to 25 MiB. If the upload refuses a file for size, tell whoever maintains the
build; very large documents must be fetched through the relay instead of shipped as site files.

When it finishes, open `https://goettschepreppy.pages.dev/settings/` and try your own access key on
the access step. It should say the key is accepted.

## 10. Add a friend

```sh
node scripts/make-access-key.mjs "Aunt May"
npx wrangler@4 secret put ACCESS_KEYS < access-keys.local.json
```

Send the printed `gpk_...` key to that friend privately (in person, a text message, or a phone
call), with the settings site address. The key is printed once and not saved anywhere; if it is
lost, revoke it and make a new one. Labels are for you only (1 to 40 letters, digits, spaces,
`. - _ '`); each friend needs a different label.

To see who has a key: `node scripts/make-access-key.mjs --list`.

## 11. Revoke a friend

```sh
node scripts/make-access-key.mjs --remove "Aunt May"
npx wrangler@4 secret put ACCESS_KEYS < access-keys.local.json
```

The relay refuses that key within a few seconds. A generation already running for that friend
stops at its next request.

To revoke everyone at once (for example if the file leaked), delete `access-keys.local.json`, make
new keys for the friends you still want, upload, and send them the new keys.

## 12. Rotate your Anthropic API key

Do this if the key may have leaked, or once a year as a habit.

1. In the Claude Console, create a new API key.
2. `npx wrangler@4 secret put ANTHROPIC_API_KEY` and paste the new key.
3. Open `/api/v1/health` on the relay and confirm `"anthropic_api_key":true`. Generate one test
   page from the settings site with your own access key, or simply wait a minute.
4. In the Console, delete the old key.

Generations running at the moment of the switch may fail and need to be restarted.

## 13. Check the request counts

The relay counts requests per friend per month (generation, source fetch and map fetch requests;
access checks are not counted). The counter key looks like
`count:2026-11:Aunt_May:208cc5ae` (month, label, first 8 characters of the key's hash).

```sh
npx wrangler@4 kv key list --binding COUNTS --remote --prefix "count:2026-11:"
npx wrangler@4 kv key get --binding COUNTS --remote "count:2026-11:Aunt_May:208cc5ae"
```

Leave out `--prefix` to list every month. A full Large binder is a few hundred requests. The counts
are approximate (Workers KV is eventually consistent, and two requests at the same instant can
count as one). For money, the Claude Console's usage page is the exact figure; the relay's count
tells you who used it.

To reset a count: `npx wrangler@4 kv key delete --binding COUNTS --remote "<key>"`.

## 14. Updating later

| What changed | What to run |
|---|---|
| Pages, cards, regions, settings code | Steps 9 (build and `pages deploy`). |
| `sources/index.json` or `sources/additions/` | `npm run test:worker`, then `npx wrangler@4 deploy` (step 6), then step 9. |
| Relay code (`worker/`) or `wrangler.toml` | `npm run test:worker`, then `npx wrangler@4 deploy`. |
| Friends | Steps 10 and 11. |

`npx wrangler@4 deploy` keeps the secrets; you do not need to set them again.

---

## Limits and costs

- **Cloudflare free plan:** 100,000 Worker requests a day (plenty), but **10 ms of CPU time per
  request** and **1,000 KV writes a day**. The relay does almost no work per request, except that a
  generation request has to be read and checked; a request carrying about 1 MB of template text uses
  roughly 5 ms. If friends see errors that mention "exceeded resource limits" (Cloudflare error
  1102), or if the counts stop rising after about two binders in a day, switch to **Workers Paid**
  ($5 a month: dashboard, **Workers & Pages**, **Plans**). Nothing else changes. When the counter
  hits the free write limit the relay keeps working; it only stops counting until the next day.
- **Size caps** (in `wrangler.toml`, `[vars]`): `MAX_TOKENS` (largest answer length a request may
  ask for, default 32000; larger asks are lowered to it), `MAX_BODY_MB` (largest generation request,
  default 8), `FETCH_MAX_MB` (largest source document, default 60), `MAP_MAX_MB` (largest USGS map,
  default 100). Change, then `npx wrangler@4 deploy`.
- **What the relay refuses** so a key cannot be used to run up your bill on other things: any model
  but `claude-opus-5-5` (decision G19), fast mode (set `ALLOW_FAST_MODE = "1"` in `[vars]` to allow
  it; it costs twice as much), refusal fallbacks to models other than `claude-opus-5` and
  `claude-opus-4-8` (change with `FALLBACK_MODELS = "model-a,model-b"`), server-side conversation
  threads (they keep the conversation on the provider's side), MCP servers and code containers.
- **Anthropic API version:** the relay sends `anthropic-version: 2026-10-21`. To pin another, add
  `ANTHROPIC_VERSION = "..."` under `[vars]`.

## Map hosts (Large binders, decision G16)

`/api/v1/fetch-map` fetches only from these USGS hosts, over https, and only under these paths
(also checked for every redirect). Checked on 2026-11-16 against The National Map's Access API,
whose `downloadURL` for current US Topo maps points at the first host.

| Host | Paths | What is there |
|---|---|---|
| `prd-tnm.s3.amazonaws.com` | `/StagedProducts/` | The National Map's staged products bucket: US Topo GeoPDFs (`/StagedProducts/Maps/USTopo/PDF/<state>/...`, about 20 to 60 MB each), historical topos (`/StagedProducts/Maps/HistoricalTopo/...`), and the full product list (`/StagedProducts/Maps/Metadata/topomaps_all.zip`). |
| `prd-tnm.s3.us-west-2.amazonaws.com` | `/StagedProducts/` | The same bucket under its regional name. |
| `tnmaccess.nationalmap.gov` | `/api/v1/` | The TNM Access API, used to find which maps cover a county (`/api/v1/products?datasets=US%20Topo%20Current&bbox=...`). |
| `rockyweb.usgs.gov` | `/vdelivery/` | The older staged-products mirror. |

To add a host, edit `MAP_HOSTS` in `worker/src/relay.js`, add a test in
`worker/test/fetch.test.mjs`, run `npm run test:worker`, and redeploy.

## What Cloudflare sees (privacy)

- The relay's code never logs and never writes anything except the counter. `wrangler.toml` turns
  Workers Logs off (`[observability] enabled = false`); leave it off, and do not add Logpush.
- `npx wrangler@4 tail` shows live request lines (time, address, status) while it runs. It does not
  show bodies, because the relay never prints them. You do not need to use it.
- Cloudflare, like any host, sees the network traffic and keeps its own aggregate request metrics
  (counts, status codes, countries) in the dashboard. It does not see inside requests unless code
  logs them, and this code does not.
- Requests go on to Anthropic's API under its data terms; the notice to users says so.

## Troubleshooting

| What you see | What it means | Fix |
|---|---|---|
| Settings page: key rejected, but you just made it | `ACCESS_KEYS` not uploaded, or uploaded from another folder | Rerun the `secret put ACCESS_KEYS < access-keys.local.json` line from the repository folder. |
| Settings page: relay unreachable | `relayBase` wrong, or `PAGES_ORIGIN` does not match the site address | Compare `app/settings/config.js` with the address from step 6, and `PAGES_ORIGIN` with the address bar of the settings site (no trailing slash). Redeploy whichever you changed. |
| `/api/v1/health` shows `"counts":false` | KV id still the placeholder | Step 3, then `npx wrangler@4 deploy`. |
| Generation fails with "The relay's API key was refused. Tell the owner." | Anthropic key wrong, deleted, or out of credit | Step 12, and check billing in the Claude Console. |
| Generation fails with `rate_limit_error` or `overloaded_error` | Anthropic is busy or your account's rate limit is reached | Wait and retry; the generator retries on its own. |
| `wrangler deploy` says the KV namespace does not exist | id typed wrong | `npx wrangler@4 kv namespace list` shows the right id. |
