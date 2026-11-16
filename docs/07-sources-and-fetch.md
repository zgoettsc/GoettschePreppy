# Sources: inline, no links, fetched per user

Owner decisions G8 and G9.

## Rules

1. **No URL is ever printed or shown in a binder.** Not in prose, not in a citation, not in a
   bibliography. The reader has no internet. A citation reads: title, publisher, edition or date.
   Example: "USDA Complete Guide to Home Canning, Guide 1, revised 2015."
2. **Every cited document is bound inside the binder**, behind the page that cites it, the way the
   household binder's volumes now bind sources behind each tab. In the app that is a "Sources for
   this page" drawer; in the PDF export it is the pages after the tab.
3. **The kit itself ships only what may be redistributed**: the project's own text, public-domain
   federal works (Air Force survival handbook, Army field manuals, USDA guides and plant
   photographs, NWS, FEMA, CDC and NIH public-domain pages, FDA labels), and openly licensed works
   with the licence carried along.
4. **Everything else is fetched for the individual household at download time**, through the
   stateless relay, into their private copy only. The relay does not store what it fetches.
5. **The household is told, three times, that the copy is private and sharing it breaks
   copyright**: in settings, at download, and on page two of the binder (`NOTICE-TO-USERS.md`).

## The source index

`sources/index.json` is the only place a URL lives. It carries, per source: key, title, publisher,
date or edition, licence class, the citing page ids, the fetch URL, the capture method that
worked for the household binder (direct, cached, manual), and the checksum of the last good
capture. Licence classes:

| Class | Shipped in the kit | Fetched per user |
|---|---|---|
| `public-domain` | yes | no need |
| `open` (CC BY, CC BY-SA, AGPL docs, government open licences) | yes, with licence text | no need |
| `restricted` (manuals, standards, societies, Extension where not open, journals, news) | no | yes |
| `blocked` (host refuses automated fetch) | no | attempted; on failure the page's own summary stands and the source is listed on the "not captured" page |

From the household binder's 391 sources: 144 public domain, 192 restricted, 55 marked for personal
reference (to be re-classified as restricted or open per document), 88 hosts blocked at last run.

## Fetch at download, step by step

1. The browser has the generated page set and the list of cited source keys.
2. For each key not in the shipped archive, the browser asks the relay to fetch it. The relay
   allows only hosts present in the index, fetches, and streams the bytes back. It keeps nothing.
3. The browser renders PDFs to page images (or extracts text where the PDF is text) and binds them
   behind the citing page. HTML sources are captured to a readable article view.
4. Blocked or failed sources go on the "sources not captured" page with the kit's own summary
   paragraph for that source, so the binder is still complete in substance.
5. This step runs for **Large** (sources cited by the life-safety sections 02, 03, 04, 06, 08, 09, 12,
   17, 20, 27 and 30) and **Everything** (every cited source), decision G25. **Small** skips it: citations
   show title, publisher and date, and the page text stands on its own. The download screen shows
   both sizes before fetching; Small can be upgraded to Large later from the saved profile file.

Manual captures (the household binder has 88 blocked hosts, mostly manufacturer sites and
paywalled standards) cannot be automated. The "not captured" page tells the household which
documents to download themselves while the internet is up, and the app has an "add a document to
this page" button that stores the file inside their copy, locally.

## What the household binder has that cannot go into the kit

- Section 30 reproductions. The Juggluco guide author forbids redistribution; the AndroidAPS docs
  are AGPL and may be fetched per user with the licence. Neither ships.
- The manufacturer manuals in the archive (heaters, power stations, CGM, pods): fetched per user.
- Red Cross, NFPA, AHA, AAP, ADA, AAAAI, WHO, ARRL, SAAMI, NSSF pages: fetched per user.
- University Extension PDFs: classified per document; many are open with credit and can ship.

## Posture

The project redistributes nothing it does not have the right to. Each household fetches, for its
own use, documents that are publicly available to it anyway, and is told plainly not to pass the
file on. That is the limit of what the project can do; what a household does with its file after
that is the household's responsibility, and the notice says so.
