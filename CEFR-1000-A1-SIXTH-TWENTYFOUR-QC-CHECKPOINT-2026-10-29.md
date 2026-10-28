# CEFR 1,000 — A1 sixth Oxford 24-source observation checkpoint (29 October 2026)

**BLOCKED / STAGING ONLY.** Approved scope is **1,000 total** (A1/A2/B1/B2/C1 **200 each**), not the superseded 5,000. All 1,000 remain on editorial hold; **0 independent human approvals**. This is an evidence-research and structural-integrity checkpoint, **not** independently reviewed language content, real listening, physical iPhone QA or publication.

## Direct publisher observations — 24 additional A1 headwords

Directly inspected [Oxford University Press, The Oxford 3000 by CEFR level (official PDF)](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-29**. The following 24 **new distinct provisional A1** words are listed in the Oxford **A1 word/POS section**. One-based PDF pages and zero-based extracted web lines are recorded in [the machine-readable evidence packet](draft/CEFR-1000-OXFORD-A1-SIXTH-TWENTYFOUR-2026-10-29.json), together with original English definitions, Myanmar meanings, example snapshots, upstream source path/index/Git blob, explicit review tasks and editorial risk codes.

| Draft word | Draft POS | Oxford PDF page:line | Editorial exact-sense risk |
|---|---|---|---|
| friend | noun | 2:314 | FRIEND_PERSON_VS_FRIENDLY_ADJECTIVE |
| name | noun | 2:509 | NAME_PEOPLE_VS_OBJECT_OR_PLACE_AND_VERB |
| red | adjective | 3:644 | RED_COLOUR_ADJECTIVE_VS_NOUN |
| blue | adjective | 1:93 | BLUE_COLOUR_ADJECTIVE_VS_MOOD |
| green | adjective | 2:338 | GREEN_COLOUR_VS_ENVIRONMENTAL_SENSE |
| black | adjective | 1:90 | BLACK_COLOUR_VS_NOUN |
| white | adjective | 4:877 | WHITE_COLOUR_VS_NOUN |
| girl | noun | 2:327 | GIRL_CHILD_VS_ADULT_INFORMAL_USE |
| boy | noun | 1:104 | BOY_CHILD_VS_ADULT_INFORMAL_USE |
| woman | noun | 4:888 | WOMAN_ADULT_VS_GIRL_CHILD |
| child | noun | 1:145 | CHILD_PERSON_VS_CHILD_OF_PARENT |
| car | noun | 1:129 | CAR_ROAD_VEHICLE_VS_RAILWAY_CARRIAGE |
| bus | noun | 1:114 | BUS_PASSENGER_VEHICLE_VS_VERB |
| train | noun | 4:817 | TRAIN_RAIL_VEHICLE_VS_TRAIN_VERB |
| city | noun | 1:149 | CITY_VS_TOWN_CONTEXT |
| country | noun | 1:177 | COUNTRY_NATION_VS_RURAL_AREA |
| street | noun | 3:743 | STREET_ROAD_VS_ADDRESS_NAME |
| table | noun | 3:760 | TABLE_FURNITURE_VS_DATA_TABLE |
| chair | noun | 1:138 | CHAIR_SEAT_VS_MEETING_CHAIRPERSON |
| door | noun | 1:220 | DOOR_PANEL_VS_ENTRANCE |
| window | noun | 4:883 | WINDOW_BUILDING_VS_COMPUTER_INTERFACE |
| pen | noun | 3:580 | PEN_WRITING_INSTRUMENT_VS_ANIMAL_ENCLOSURE |
| apple | noun | 1:39 | APPLE_FRUIT_VS_BRAND_NAMED_ENTITY |
| and | conjunction | 1:30 | AND_COORDINATING_CONJUNCTION_VS_SEQUENCE |

**Coverage accounting:** five previous A1 packets cover **76 distinct** provisional A1 words. This sixth batch adds **24 non-overlapping** headwords, reaching **100/200 (50%) A1 word/POS research observations**. This is **NOT 100 independently approved words**, and Oxford's word/POS list does not verify exact senses, Myanmar fluency, original sentence grammar or British pronunciation. A1 remains **200 first-pass written / 0 independently approved**.

## Substantive bilingual editorial triage (unreviewed, not applied)

Six original editorial rewrite proposals address: **name** (person-only gloss omits places/things), **red** (clearer colour gloss), **woman** (adult versus child), **city** (city/town classification depends on context), **train** (rail noun versus training verb) and **and** (coordination of words, phrases and clauses). Proposed English definitions, fluent-Myanmar candidates and original examples are stored in the packet with `UNREVIEWED_UNAPPLIED_PROPOSAL` and `human_independent_approval=false`. No shortlist text or review flag was changed.

Special independent-review risks: **apple** as ordinary fruit versus proper-noun technology brand, **country** as nation versus rural area, **table** as furniture versus tabular data, **chair** as furniture versus meeting chairperson, and **window** as physical window versus software window. These are **sense disambiguation tasks**, not claims of a publisher's sense-specific CEFR classification.

## Fail-closed structural safeguard

[New auditor](tools/audit_cefr_1000_oxford_a1_sixth_twentyfour.py) binds all 24 exact PDF word/POS locators and excerpts, original English/Myanmar/example snapshots, shortlist blob, upstream original-source Git blobs and indices, all human-review holds, and six unapproved rewrites. It rejects duplicate previously observed A1 headwords and requires exactly **100 unique observed A1** across all six packets. The negative-test suite attempts **212 deliberate mutations** of source locators, publisher excerpts, Myanmar meanings, examples, historical provenance, review receipts, false approvals and held proposals. Passing mechanical tests cannot substitute for independent linguistic signoff.

The auditor is integrated into **six parallel A1/A2/B1/B2/C1/ALL GitHub Actions structural jobs** and the **documentary no-deployment release gate**. Actual job conclusions and log counts must be verified before describing CI as passing. Initial CI attempts [40779210457](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40779210457) and [40779215971](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40779215971) failed due to a new auditor using `myanmar_meaning` as a shortlist field; the shortlist actually stores `burmese_meaning`. This was corrected in staging commit `39ec52e1d3471ee51133a2ade4a624ecea5d7e08`; post-fix CI verification is required.

## Release gate and production protection

| Level | First-pass written | Independently approved | Final both-voice listening signed off |
|---|---:|---:|---:|
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

Final British George/Emma headword and example audio creation plus real listening signoff, independent English/Myanmar/example/exact-sense CEFR approval, full desktop/mobile browser regression on the final approved corpus, **real physical iPhone Safari** QA, measured GitHub Pages hosting limits, production asset preservation and confirmed live deployment all remain **unverified or incomplete**. Existing 54 lessons, separate IELTS 1,000 bank, production audio and privacy are protected; no changes to `main`, merge, publication or launch authorisation occurred. **BLOCKED / STAGING ONLY.**
