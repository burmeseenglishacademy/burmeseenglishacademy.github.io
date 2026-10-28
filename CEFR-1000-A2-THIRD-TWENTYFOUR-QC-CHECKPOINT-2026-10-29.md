# CEFR 1,000 — third A2 Oxford source / exact-sense triage (29 October 2026)

**Status: BLOCKED / STAGING ONLY.** Approved project scope: A1/A2/B1/B2/C1 **200 each, 1,000 total**. Branch: `cefr-5000-bilingual-qa-staging`. This is source observation and automated provenance integrity work, **not** independent English/Myanmar/CEFR approval, audio listening, iPhone testing or production deployment.

## Primary source and provenance

Opened the official [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) directly on **2026-10-29**. Recorded **24 further provisional A2** headword/POS entries from the frozen shortlist, with Oxford PDF page (one-based), extracted web text line (zero-based), short publisher entry, source URL, observation date, original English definition, Myanmar meaning, example, original source path/index/blob SHA, and explicit reviewer tasks. Packet: [dated 24-word evidence](draft/CEFR-1000-OXFORD-A2-THIRD-TWENTYFOUR-2026-10-29.json). Source shortlist Git blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Oxford is a **word/POS-level CEFR list**; no publisher exact-sense CEFR conclusion is inferred.

**Publisher word/POS comparison:** **16 Oxford A1 vs provisional A2**, **8 Oxford A2 matches**. These are conflicts to investigate, not automatic evidence that a specific A2 sense is wrong. The 24 entries remain editorial-held with zero independent approvals.

| Draft headword | Draft POS | Oxford word/POS CEFR | PDF page:line | Priority review issue |
|---|---|---|---|---|
| public | noun | A2 | 6:1512 | PUBLIC_NOUN_VS_ADJECTIVE_AND_COMMUNITY_SCOPE |
| system | noun | A2 | 7:1687 | SYSTEM_CONNECTED_PARTS_VS_DIGITAL_ORDER_TRACKING |
| support | verb | A2 | 7:1678 | SUPPORT_VERB_HELP_VS_NOUN |
| power | noun | A2 | 6:1491 | POWER_AUTHORITY_VS_GENERAL_CONTROL_AND_ENERGY |
| side | noun | A2 | 6:1612 | SIDE_SURFACE_VS_EDGE |
| business | noun | A1 | 1:115 | A1_BUSINESS_VS_A2_DRAFT |
| however | adverb | A1 | 2:382 | A1_HOWEVER_CONTRAST_VS_A2_DRAFT |
| nothing | pronoun | A1 | 3:533 | A1_NOTHING_VS_A2_DRAFT |
| actually | adverb | A2 | 4:918 | ACTUALLY_CORRECTION_VS_FACTUALITY |
| less | determiner | A2 | 5:1356 | LESS_DETERMINER_UNCOUNTABLE_VS_ADVERB |
| party | noun | A1 | 3:576 | A1_SOCIAL_EVENT_VS_A2_DRAFT |
| whole | adjective | A2 | 7:1763 | WHOLE_COMPLETE_VS_TIME_DURATION |
| maybe | adverb | A1 | 2:469 | A1_MAYBE_VS_A2_DRAFT |
| story | noun | A1 | 3:742 | A1_NARRATIVE_VS_A2_DRAFT |
| health | noun | A1 | 2:357 | A1_HEALTH_VS_A2_DRAFT |
| hope | verb | A1 | 2:374 | A1_HOPE_VS_A2_DRAFT |
| important | adjective | A1 | 2:392 | A1_IMPORTANT_VS_A2_DRAFT |
| information | noun | A1 | 2:396 | A1_INFORMATION_UNCOUNTABLE_VS_A2_DRAFT |
| local | adjective | A1 | 2:450 | A1_LOCAL_VS_A2_DRAFT |
| course | noun | A1 | 1:178 | A1_COURSE_STUDY_VS_OTHER_SENSES |
| video | noun | A1 | 4:848 | A1_VIDEO_VS_A2_DRAFT |
| ago | adverb | A1 | 1:21 | A1_AGO_VS_A2_DRAFT |
| fact | noun | A1 | 2:265 | A1_FACT_VS_A2_DRAFT |
| half | noun | A1 | 2:346 | HALF_NOUN_VS_QUANTIFIER_AND_A1_DRAFT_CONFLICT |

## Exact-sense cross-publisher leads, not direct verification

Cambridge Dictionary publisher-indexed [power](https://dictionary.cambridge.org/dictionary/english/power) shows **CONTROL** at **B2**, while Oxford lists the noun at A2 word/POS. The draft example *“The manager has the power to approve requests.”* is closer to an **official right/authority** sense, which Cambridge's indexed entry does not visibly assign a CEFR label. Do **not** automatically treat the B2 CONTROL label as proof of the draft example's level; independent exact-sense reconciliation is required.

Cambridge publisher-indexed [less](https://dictionary.cambridge.org/dictionary/english/less) shows the smaller-amount sense at **A2**. The draft *“Please add less sugar to my tea.”* uses `less` with an uncountable noun and needs a real grammar/translation review. Direct Cambridge page requests returned **HTTP 403** on 2026-10-29; these are explicitly **search-index leads**, not directly inspected dictionary-page evidence and never a signoff.

Editorial priorities: natural Myanmar phrasing for `nothing`, `whole`, `less` and `half`; `side` as paper face vs edge; `power` authority vs general control; `fact` example naturalness; `course` educational sense vs other senses; `public` noun vs adjective; `support` verb vs noun. No original example, Myanmar meaning, draft tier or approval flag was altered.

## Original English/Myanmar rewrite proposals (not reviewed)

Added [12 bilingual/editorial rewrite candidates](draft/CEFR-1000-A2-THIRD-BILINGUAL-REWRITE-CANDIDATES-2026-10-29.json) for `power`, `side`, `nothing`, `whole`, `less`, `business`, `however`, `public`, `fact`, `half`, `course` and `information`. Each preserves the original definition/Myanmar/example snapshot and source provenance, offers an original alternative English definition, Myanmar meaning and example sentence, and explains the sense/grammar issue. **These are suggestions for human review, not changes to the canonical shortlist or independently validated translations.** A separate structural auditor rejects forged source snapshots, missing headwords in example sentences, absent Myanmar script and false signoffs.

## GitHub Pages policy cross-check

[Official GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits), viewed 2026-10-29, state a **1 GB published-site maximum**, **1 GB recommended source-repository size**, **10-minute deployment timeout**, **100 GB/month soft bandwidth limit**, and **10 builds/hour soft limit** (custom Actions publishing exception). Repository metadata currently reports **122,762 KB** of repository size, which is **not** a measurement of the final published site or the planned George/Emma audio assets. Hosting QA remains **unverified** pending actual artifact, audio, forecast and delivery measurements.

## Release and CI integrity

A new [fail-closed A2 packet auditor](tools/audit_cefr_1000_oxford_a2_third_twentyfour.py) binds the observations to the exact shortlist Git blob, snapshots, source locators, risk IDs and zero-approval status. It contains **48 authored negative mutation cases** (24 forged source excerpts plus 24 false approval/provenance/translation changes). Both the six-way A1/A2/B1/B2/C1/ALL structural workflow and the documentary no-deploy workflow invoke it. Actual latest run conclusions/logs must be inspected before claiming any pass.

The launch gate now requires separate, genuine, content-hash-bound **human-independent exact-sense A2** receipts for retained entries. All 16 lower Oxford word/POS labels need explicit reconciliation; retained `power` additionally requires cross-publisher authority/control sense resolution. The independent receipt array was created **empty**; no approvals were manufactured.

| CEFR level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**Final George/Emma audio listening receipts:** 0/1,000. **Missing:** real independent bilingual/example/exact-sense signoff, full British George/Emma headword and example audio with real listening, desktop/mobile regression, physical iPhone Safari QA, measured GitHub Pages hosting capacity, final approved manifest, confirmed production deployment and complete protected production asset verification. Existing 54 lessons, separate IELTS 1,000 bank, established production audio and privacy are protected; no `main` change, merge or publish is authorised before all gates pass.
