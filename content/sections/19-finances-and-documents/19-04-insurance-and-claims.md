---
id: 19-04-insurance-and-claims
section: 19-finances-and-documents
title: "Insurance and claims"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, C]
tags: [insurance, homeowners, renters, flood insurance, hail, wind, deductible, replacement cost, claims, adjuster, home inventory, life insurance, disability insurance]
derived_from: [19-04-insurance-and-claims]
sources:
  - consumer-financial-protection-bureau-disasters-and-e-44eaa3
  - usa-gov-find-disaster-financial-help-fbcd9e
  - internal-revenue-service-reconstructing-records-afte-28669f
  - cdc-preparing-for-floods-safety-cleanup-and-hygiene-d00a5d
  - fema-nfip-floodsmart-buy-a-policy
  - fema-nri-counties
related: [19-01-document-grab-kit, 19-02-cash-and-value, 19-03-records-and-backups, 19-07-access-continuity, 19-08-income-continuity, 22-04-household-inventory, 25-03-regional-contacts, 25-05-blank-logs, 25-10-annual-review, 16-12-grid-down-house-repairs, 17-01-blizzards-and-ice, 17-02-tornadoes, 17-03-floods, 17-08-power-grid-failure, 17-12-earthquakes, 17-13-hurricanes-and-tropical-storms, 17-14-wildfire-smoke-and-evacuation, 17-18-hail-and-damaging-wind, 04-17-food-safety-power-outage, 14-04-caliber-roles-and-inventory, 18-01-mutual-aid, 01-05-choosing-a-destination]
cards: []
explainers: []
promote_when: [is.flood_region, is.hurricane_region, is.tornado_region, is.wildfire_region, is.earthquake_region]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "NFIP 30-day wait and exceptions verified (FEMA FloodSmart, read live); basement-contents wording corrected; NRI rating caveat added." }
---

# Insurance and claims

**What this page is for.** Understanding what your insurance covers before the disaster, and making a
claim work after it. Insurance is the main financial protection against the disasters that actually
happen to most households: fire, wind, hail, storms, freezing damage and flood. It is also the thing
most households have never read.

**Your home county's main hazards:**
{{#each region.home.hazards as h}}- {{h.name}}: {{h.rating_text}}
{{/each}}
These ratings come from FEMA's National Risk Index (FEMA, National Risk Index). They weigh how much
there is to damage as well as how often a hazard strikes, so "low" is not a promise that it will
not happen to you. Your state page in Section 32 explains them.

> **CAUTION. Two things that surprise people, both worth knowing now.**
> 1. **Standard homeowner's and renter's policies usually do not cover flood.** Flood coverage is a
>    separate policy, and **it does not start the day you buy it**: you cannot buy it when the water
>    is rising (→ 17-03).{{#if is.flood_region}} **Your county's flood rating is high: ask about it
>    this week.**{{/if}}
> 2. **Limits, deductibles and exclusions vary enormously**, especially for wind and hail, which
>    sometimes carry a separate, higher deductible{{#if is.hurricane_region}}, and for hurricanes,
>    which often have their own deductible{{/if}}{{#if is.earthquake_region}}; earthquake damage is
>    usually excluded unless you add it{{/if}}.
>
> **This page cannot tell you what your policy covers. Read it, and call your agent.**

> **Before the collapse:** a National Flood Insurance Program policy takes effect 30 days after
> you buy it. The exceptions are narrow, such as buying it while making, increasing, extending or
> renewing a mortgage (FEMA FloodSmart, Buy a Policy). A private flood policy has its own terms;
> ask. NFIP policies do not cover personal property kept in a basement, temporary housing while
> the home is repaired, or sewer backup unless it is caused directly by flooding (FEMA FloodSmart).
> FEMA's flood maps show whether an address is in a mapped flood zone; your agent can look it up.

## Do this now

1. **Read your actual policy:** coverage limits, deductibles, exclusions, and whether wind and hail
   have their own deductible. One afternoon, once.
2. **Ask your agent three questions:** Am I covered for flood? Is my dwelling coverage enough to
   rebuild at today's costs? What is my wind and hail deductible?
3. **Ask two more if you have a basement:** what a flood policy pays for in the basement, and
   whether you can add **sewer and sump-pump backup** coverage (→ 17-08). That is the water event many
   houses actually have.
4. **Do the photo inventory** (→ 19-01, → 22-04), an hour with a phone, stored away from home. This is
   what makes a claim work.
5. **Put policies, policy numbers and agents' phone numbers in the grab folder** (→ 19-01).

## Coverage worth checking

| Hazard | Typical situation. **Check your own policy** |
|---|---|
| Hail | Often a separate, higher deductible; older roofs may be paid at depreciated value, not replacement cost |
| Wind and tornado | Usually covered; check the deductible |
| Hurricane | Often its own deductible; storm surge counts as flood |
| Fire and wildfire | Usually covered |
| Ice and winter storm | Often covered; burst-pipe damage may depend on whether the home was heated and maintained |
| **Flood** | **Usually NOT covered.** Separate policy with a waiting period; NFIP policies do not cover personal property kept in a basement. Seepage and sump failure are not "flood" without wider flooding |
| **Sewer and drain backup** | **Often excluded unless added.** A real risk when power fails and a sump pump stops |
| Earthquake | Usually excluded unless added |
| Food spoiled in an outage | Sometimes covered, with limits (→ 04-17) |
| Additional living expenses | Pays for somewhere to stay if the home cannot be lived in. Check the limit |
| Personal property | **Replacement cost versus "actual cash value" (depreciated) is the big difference** |
| Special limits | Firearms, jewelry, cash and electronics often have low limits. Check, and list valuable items separately if needed |

## Is the house itself insured for enough?

**The most common serious gap is too little coverage on the building.** Building costs rise, and a
policy written years ago may not pay to rebuild today.
- Ask whether your dwelling limit reflects current rebuilding costs.
- Ask about "extended" or "guaranteed" replacement cost if offered.
- It matters most in exactly the case where you need it: a total loss.

## Insuring the people, not just the house

Property policies protect things. These protect the plan:
- **Life insurance on every adult whose income or work the household depends on.** A chronic
  condition often raises the price; it does not always rule coverage out. Get quotes; do not assume
  the answer.
- **Disability insurance** for anyone whose income depends on their ability to do their job,
  especially if self-employed (→ 19-08).
- **Beneficiaries checked on every policy**, and matching your will and other documents (→ 19-07).

**Adults in your household:** {{#each adults as a}}{{a.label}}; {{/each}}

**Coverage worksheet: fill in by hand from the actual documents.** No policy numbers in the app; the
filled copy goes in the grab folder (→ 19-01).

```
ON PAPER
Policy               Company         Policy no.     Amount / benefit   Beneficiary   Reviewed
Life: __________     ____________    ___________    $__________        ___________   ________
Life: __________     ____________    ___________    $__________        ___________   ________
Disability: _______  ____________    ___________    $______/month      n/a           ________
Home or renters      ____________    ___________    $__________        n/a           ________
Auto                 ____________    ___________    $__________        n/a           ________
Umbrella             ____________    ___________    $__________        n/a           ________
Flood                ____________    ___________    $__________        n/a           ________
Business (19-08)     ____________    ___________    $__________        n/a           ________
```

## The inventory decides whether a claim works

The most useful hour you can spend on insurance (→ 22-04, → 19-03):
- **Video every room**, talking as you go. Open closets, cabinets and drawers.
- **Photograph serial numbers** on major items.
- **Photograph storage areas:** food, tools, equipment and your preparedness supplies. They are real
  money, and people routinely forget to claim them.
- **Keep receipts** for significant purchases where you can.
- **Store it away from home** (→ 19-03). An inventory that burns with the house is no inventory.
- **Update it every year** (→ 25-10).

**Without it you rebuild a list from memory under stress, and you will under-claim badly.**

```
PHOTO / VIDEO INVENTORY
Done? ____  Date: __________  By: __________
Stored away from home where (19-03): ____________________
Second copy: ____________________
Supplies and storage areas included? ____  Serial numbers? ____
Refreshed at yearly review (25-10): __________
```

## Making a claim

From the CFPB's disaster guidance (CFPB, Disasters and Emergencies) and common practice:
1. **Safety first** (→ 17-02, → 17-03). The claim can wait.
2. **Contact the insurer as soon as practical.** Many have 24-hour claim lines. Write down the claim
   number and the adjuster's name.
3. **Document the damage before cleaning up:** many photos and video. **Do not throw out damaged
   property until it is documented or the adjuster has seen it**, unless it is a health hazard, such
   as flood-soaked food or moldy materials (CDC, Preparing for Floods).
4. **Make reasonable temporary repairs** to stop more damage: tarp the roof, board the window
   (→ 16-12). Keep receipts; this is usually covered. **No permanent repairs before the adjuster
   sees it.**
5. **Keep a log** of every call: date, name, what was said (→ 25-05).
6. **Keep every receipt** for lodging, meals and supplies if you are displaced. Additional living
   expenses are often covered.
7. **Read what you are asked to sign.**
8. **If you disagree with the settlement**, ask about the appraisal process in your policy. The
   regulator to contact is the {{ home.state_name }} state insurance department. Phone:
   ______________ (also on → 25-03).

## Help beyond insurance

Federal and state disaster assistance exists, separate from insurance (USA.gov, Find Disaster
Financial Help).
- It usually requires a declared disaster and adds to insurance rather than replacing it.
- It requires documents (→ 19-01, → 19-03).
- The IRS has disaster guidance on records and on casualty losses (IRS, Reconstructing Records After
  a Disaster).
- Write down where to find help now (→ 25-03).

## The honest limit

**Insurance works in a working society.** It covers the fire, the tornado, the hailstorm: bounded
disasters, which are also the most likely ones. **In a long collapse, insurance is not a plan**:
claims will not be paid and money may not buy anything (→ 19-02). That is fine; it is not what
insurance is for. Most bad things that actually happen to a household are the bounded kind, and for
those, a policy you have read and an inventory you have made are worth more than almost anything else
in this binder.

## Gear

| Item | Why | Notes |
|---|---|---|
| **Your policy, read** | Almost nobody has | An afternoon, once |
| **Photo and video inventory, stored away from home** | What makes a claim work | → 22-04 |
| Policies, numbers and agent contacts in the grab folder | You will need them when the house is gone | → 19-01 |
| Flood coverage, if it applies | Not in standard policies; waiting period | → 17-03 |
| Sewer and sump backup coverage | Real risk in an outage | → 17-08 |
| Valuable items listed separately on the policy | Above the low sub-limits | |
| Receipts for significant purchases | Support the claim | Photograph them |
| A claim log notebook | Every call, date, name | → 25-05 |
| Tarps, plastic sheeting, boards | Temporary repairs | → 16-12 |

**Substitutes:** the inventory can be done today with a phone. Photos of anything you cannot document
formally. Neighbors as witnesses to damage and to what you had (→ 18-01). **What you cannot
substitute is coverage not bought before the event, or the flood waiting period.**

## When it runs out

- **Coverage lapses if premiums are not paid**, a real risk in a financial disruption (→ 19-02).
  Insurers and lenders are often accommodating if you contact them early (CFPB).
- **Review every year:** coverage against rebuilding costs, the inventory, and changes in your life.
- **Substitutes:** the emergency fund (→ 19-02), disaster assistance, and your neighbors, who are
  the help that actually arrives first (→ 18-01).

## By phase

- **A, at home:** read the policy, close the gaps, do the inventory, store it away from home. All of
  this only works before the event.
- **B, on the move:** the grab folder holds the policy details; the away-from-home inventory supports
  a claim if the house is lost while you are gone.
- **C, settled:** redo it all for the new place. Rural properties raise different questions:
  outbuildings, wells, livestock, distance from a fire station. Ask before you commit (→ 01-05).
