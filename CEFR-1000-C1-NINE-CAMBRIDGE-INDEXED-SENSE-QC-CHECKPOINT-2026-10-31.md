# CEFR 1,000 — nine C1 indexed Cambridge sense/POS research leads (31 October 2026)

**Scope:** user-approved 1,000 TOTAL (A1 200, A2 200, B1 200, B2 200, C1 200), never the superseded 5,000. **Branch:** `cefr-5000-bilingual-qa-staging`. **Release:** BLOCKED / STAGING ONLY. No changes to frozen shortlist, independent-review task receipts, main, existing 54 lessons, separate IELTS 1,000, production George/Emma audio, or privacy controls.

## What was actually researched

Nine provisional C1 entries without prior direct Oxford word/POS observation were cross-checked against **public search-index/cached Cambridge Dictionary results observed on 2026-10-31**. Direct Cambridge page fetch attempts returned **HTTP 403**; do **not** describe these as direct publisher-page inspection, authoritative independent exact-sense verification, or human approval. The source-bound [nine-record packet](draft/CEFR-1000-CAMBRIDGE-C1-NINE-INDEXED-SENSE-AND-POS-TRIAGE-2026-10-31.json) retains URLs, date, frozen original English/Myanmar/examples, historical source path/index/blob, publisher badge where actually visible, editorial risk, and nine unapproved bilingual/example proposals.

| Provisional C1 | Indexed publisher observation | Human reviewer priority |
|---|---|---|
| naval (adjective) | [Cambridge C2 adjective](https://dictionary.cambridge.org/dictionary/english/naval) | Same navy-related sense appears C2; do not assume C1 |
| noble (adjective) | [Cambridge C1 moral sense](https://dictionary.cambridge.org/dictionary/english/noble) | Moral goodness versus noble rank and unlabelled appearance |
| treasury (noun) | [Cambridge the Treasury, no CEFR badge seen](https://dictionary.cambridge.org/dictionary/english/treasury) | Government institution; British article/capitalization; no invented C1 label |
| ethics (noun) | [Cambridge C2 study-of-morality sense](https://dictionary.cambridge.org/dictionary/english/ethics) | Draft means principles; do not transfer the study-sense C2 badge automatically |
| manufacturer (noun) | [Cambridge B2 producer-company sense](https://dictionary.cambridge.org/us/dictionary/english/manufacturer) | Same intended producer-company sense is indexed B2 |
| veteran (adjective in draft) | [Cambridge C2 **noun**](https://dictionary.cambridge.org/fr/dictionnaire/anglais/veteran) | **POS mismatch**: noun label cannot justify adjective C1 |
| legally (adverb) | [Cambridge B2 law-compliance sense](https://dictionary.cambridge.org/dictionary/english/legally) | Verify legally binding collocation and fluent Myanmar |
| destiny (noun) | [Cambridge C1 countable future and uncountable fate](https://dictionary.cambridge.org/dictionary/english/destiny) | Distinguish events versus controlling force and countability |
| census (noun) | [Cambridge official count, no CEFR badge seen](https://dictionary.cambridge.org/dictionary/english/census) | Countable population census; absence of badge is not C1 proof |

These are **nine additional Cambridge indexed leads**, **zero additional direct Oxford PDF observations**. The previously CI-reconciled direct Oxford word/POS count remains **A1 195/200, A2 168/200, B1 200/200, B2 166/200, C1 111/200 = 840/1,000**, with 160 lacking those direct Oxford observations. Cambridge indexed levels are C1 two, B2 two, C2 three, and unlabelled two; veteran's C2 noun badge is explicitly **not** a draft-adjective level.

## Staging safeguard and real release blockers

Added [source-bound fail-closed auditor](tools/audit_cefr_1000_cambridge_c1_nine_indexed.py) to the six parallel A1/A2/B1/B2/C1/ALL structural lanes and the documentary no-deployment workflow. It binds all nine original bilingual/example snapshots and Git provenance to the frozen 1,000 shortlist, pins indexed-source access limitations and the source packet Git blob, rejects forged CEFR/POS/source, edits, fake human review or listening, and exercises **149 adversarial mutations**. **This tests documentary integrity, not publisher authentication or real-world listening.**

| Level | First-pass written | Independently checked/approved | Real final George+Emma listening signoffs |
|---|---:|---:|---:|
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |

**Required before any launch:** independent English/fluent Myanmar/example/exact-sense source and CEFR signoff; 200 deduplicated approved headwords/senses per level; complete George and Emma headword/example audio generation and real listening receipts; approved-corpus browser/mobile regression; real physical iPhone Safari QA evidence; measured GitHub Pages hosting constraints; confirmed deployment and unchanged protected production assets. Do not set reviewer flags or merge/publish based on assistant research. **Release remains blocked and staging only.**

CI workflows triggered by staging changes: [structural run 41177473607](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41177473607) and [documentary run 41177473617](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41177473617), both on code SHA `2df05a7930e1505827db252bb69fea56d11fec2a`. **ACTUAL CI VERIFIED:** structural run **SUCCESS across A1/A2/B1/B2/C1/ALL** (all six job conclusions checked); documentary no-deploy run **SUCCESS, report-only**. Actual ALL and documentary logs confirm **149/149 adversarial mutations rejected**, zero independent approvals, no real listening receipts, and protected production assets unchanged. Structural ALL artifact **13033832726**; documentary blocker artifact **13033816676**. The prior intermediate SHA `f3c782d3474ee22dc046f51cb836715c9a9f84c6` failed due to packet Git-blob rebind after the ethics example correction; repaired and verified at `2df05a7930e1505827db252bb69fea56d11fec2a`. These checks are structural/documentary only, not human or device testing.
