# Coordinator follow-ups

Collected from worker reports; resolved in the integration pass.

- [ ] L4: two source additions (FDA Drug Facts, USDA food dating) listed without the page being read; verify or replace in the source-trace pass.
- [ ] L4: fuel shelf life has no federal or manufacturer number; EX-01 says "months, not years". Make sure no other page states the household's 6-month / 2-5-year figures as fact.
- [ ] L4: EX-10 hazard 1-3 rating wording must match D1's NRI mapping.
- [ ] L4: check current NWS naming of cold and heat products (Extreme Cold Warning / Cold Weather Advisory, 2024-25 consolidation).
- [ ] L4: appliance wattages (EX-02) and radio ranges (EX-09) labelled "typical", unsourced; acceptable as labelled.
- [ ] C01: confirm template filtering workarounds can switch to the new filtered lists (children, adults, agreed_destinations, refrigerated_meds).
- [ ] Figures requested across workers: collect from notes/workers/*.md for the figures worker.
- [ ] Section 17: seven national hazard pages added to the plan (17-12..17-18); assign with C12.
- [x] C03 requested: destinations water_source/sewer, dwelling.roof_area_sqft (+ derived.rain_gal_per_inch), gear.generator_volts — added to profile and context; A2/A3 notified. C03 pages print blanks for these until updated in the integration pass.
- [ ] C03 asked whether handwashing with untreated water (13-02) should be a card; left neutral with a household blank. No card unless the owner wants one.
- [ ] C09: AAP children's acetaminophen/ibuprofen chart only partly transcribed (12-47 lb rows checked); transcribe the full published chart in the integration pass.
- [ ] C09: removed the AHA aspirin-for-suspected-heart-attack amount. That is a published AHA recommendation, not a derived dose; consider restoring as published.
- [ ] C09: two household sources without index entries (2025 AHA/Red Cross first-aid guidelines; wilderness first-responder curriculum).
- [ ] C09: seven owner questions in notes/workers/C09.md (tourniquet "the limb is the price" wording; WHO 75 mL/kg ORS figure) — put to the owner.
- [x] C09 requested meds where_kept, expiry (days_on_hand already added); added to profile and context.
- [x] C08: backfeed floor wording corrected in docs/05 (cord-and-plug is not a connection to house wiring; interlock needs main off). L3 told. Re-check 09-04 and 30-01/30-08 wording in integration.
- [x] C08 slots added: station pv_input_max_v/w, panel voc/isc, region.home.latitude, derived.solar_wh_dec/jun, has.hybrid. Medicine-cooler Wh/day left as a fill-in.
- [ ] C08: photo slot ids reused across pages (station-ports): renderer should share one photo per slot id across the binder. Tell A3.
- [ ] C08: kettle numbers on 07-06 must match 09-xx.
- [x] L3: DC-07 row in docs/05 fixed (risk is the DIY wiring, not backfeed). Flag has.adult_over_40 added; DC-22 (30-23) should switch from has.elder to it in integration.
- [x] L3: household 08-09 propane volume error (1,700 cu ft) fixed in the SHTF binder to ~170 cu ft with LFL arithmetic; C07 warned. Check 28-04 when written.
- [ ] L3: camp stoves indoors are covered in floor 1's explanation; check 07-05 agrees.
- [ ] L3: DC-10 humane-end option needs a method section on 20-09 (tell C13). DC-16 last-resort names a published adult antibiotic table not yet printed anywhere: either source one (e.g. CDC/IDSA tables are prescriber-facing) or reword DC-16.
- [ ] A3: Large binds PDFs as embedded files with an "Open the document" button; print shows a note, not the pages, and opening an embedded PDF offline on iOS is unreliable. Owner wants sources inside and printable: render PDF pages to images or text in the browser (vendored pdf.js) at Large build time.
- [ ] A3: model review runs only on household-variable pages. Frozen core text needs a one-time kit-level review pass at build (integration phase: source-trace + consistency over all core pages).
- [ ] A3: topo maps can push Large past 400 MB; cap to home county + destinations, route counties optional with size shown.
- [ ] A3: kit build should include only sources cited by kit pages (household-only sources such as the AAPS docs trip the owner-token check otherwise).
- [ ] A3: refusal fallback written but disabled per G19.
- [ ] A2: saved profile.json includes the access key by default. Change: never write the key into the saved file (schema: make access optional in saved files, required only at generate time); user re-enters the key when regenerating.
- [ ] A2/A3: Large estimate 347-753 MB, over G11's 200-400 MB; driven by topo maps. Cap maps (home county + destinations by default; route counties opt-in) and render PDFs as compressed page images.
- [ ] A2: DC-05 hidden without an attached garage (recorded undecided) — fine; check the card page prints "not applicable" rather than "not decided" in that case.
- [ ] Owner deploy action: set relayBase in app/settings/config.js to the Worker address (docs/10-deploy.md).
