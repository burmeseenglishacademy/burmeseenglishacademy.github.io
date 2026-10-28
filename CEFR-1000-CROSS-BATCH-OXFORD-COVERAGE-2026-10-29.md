# CEFR 1,000 Oxford evidence consolidation — 29 October 2026 (staging only)

**Scope:** USER-APPROVED 1,000 TOTAL (A1/A2/B1/B2/C1 = 200 each), not the superseded 5,000-word plan. Source of truth remains `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; all 1,000 first-pass entries are editorial holds, with **0 human-independent approvals**. The branch is `cefr-5000-bilingual-qa-staging` and no production publication is authorised until all gates actually pass.

## Why this consolidation matters

Prior publisher observations used **two distinct schemas**: newer `publisher_source.source_cefr_level` records and older flat `source_cefr` records. Treating a missing nested field as an Oxford non-listing would falsely label **36 legacy records** as unlisted. The new `tools/audit_cefr_1000_oxford_coverage.py` normalises both formats and requires genuine, dated Oxford URLs and PDF locators. It distinguishes **36 historical locator-only records with no quoted source excerpt** from three explicitly documented non-matches in the two inspected core lists. These 36 need a fresh direct-publisher excerpt check before claiming excerpt-level traceability; do not fabricate quotations.

Across **21 source packets**, there are **324 observations covering 305 distinct provisional headwords**, with **19 repeat observations** (8 A1, 2 B2 and 9 C1). Repeats are not additional review coverage. The normalised publisher word/POS classifications, counted **once per distinct headword**, are:

| Provisional level | First-pass written | Distinct Oxford-observed | Matching word/POS | Lower Oxford label | Higher Oxford label | Not listed in inspected core PDFs | Independently approved |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A1 | 200 | 100 | 100 | 0 | 0 | 0 | 0 |
| A2 | 200 | 48 | 12 | 36 | 0 | 0 | 0 |
| B1 | 200 | 60 | 20 | 36 | 4 | 0 | 0 |
| B2 | 200 | 58 | 28 | 26 | 3 | 1 | 0 |
| C1 | 200 | 39 | 16 | 21 | 0 | 2 | 0 |
| **Total** | **1,000** | **305** | **176** | **119** | **7** | **3** | **0** |

**129 distinct observed entries** require explicit editorial resolution because the proposed level differs from the Oxford word/POS label or the word was absent from the two inspected PDFs. The **three absent-core-list words** are `officially` (B2), `premises` and `divine` (C1). An absent word is **not** evidence of a CEFR level. **695** provisional words do not yet have an observation in these 21 consolidated packets; other separate evidence sources may exist, but are not counted here.

## Release and editorial consequences

- This is **publisher word/part-of-speech research**, not exact-sense CEFR evidence, a fluent Myanmar translation verdict, example-grammar verification, or human-independent signoff. All 305 observed words remain unapproved.
- Prioritise independent exact-sense review for **119 lower-level discrepancies**, **7 higher-level discrepancies**, and **3 core-list non-matches**, before treating a proposed teaching level as substantiated. A distinct sense and pedagogical rationale must be evidenced, not inferred from word-list membership.
- Preserve both the source URL and date, the original English/Myanmar/example snapshot, and the historical Git provenance. For the 36 legacy locator-only observations, collect a real publisher excerpt with its locator rather than silently filling the missing field.
- The new cross-batch auditor checks frozen shortlist binding, 200-per-level scope, deduplicated coverage, both historical schemas, publisher URLs/locators, original bilingual/example snapshots, source provenance, repeated-observation consistency, zero approvals and false-signoff rejection. It is wired into all **six parallel A1/A2/B1/B2/C1/ALL structural lanes** and the **staging-only documentary release gate**.
- Final George/Emma headword+example audio real-listening signoffs remain **0/1,000**. Independent English/Myanmar/example/CEFR approvals, complete final audio, browser/mobile regression, real physical iPhone Safari evidence, GitHub Pages measured hosting limits, privacy/protected-asset verification and confirmed production deployment are still required.

Publisher PDFs inspected in the underlying dated source packets: [Oxford 3000](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf). These are pre-existing direct-source observations from 28–29 October 2026; this consolidation does **not** claim a new independent publisher inspection or human verification.

**Verified CI (code/workflow head `53e82e59932914d09cc24c5939ae41e059970cbe`):** [parallel structural run 40786416169](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40786416169) completed **SUCCESS** across **A1/A2/B1/B2/C1/ALL**, including actual ALL-job log **16/16 forged-source, bilingual, locator and false-review mutations rejected**, and protected production diff **PASS**. [Documentary no-deploy run 40786416334](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40786416334) completed **SUCCESS as report-only**; actual logs independently reproduced **305 distinct / 324 observations / 129 flagged / 36 locator-only**, rejected **16/16** mutations, explicitly recorded missing human review, and passed protected production diff. Initial runs 40786231689/40786238704 and 40786345097/40786345074 **failed** due overly strict handling of historical excerpt-less packets and differing genuine publisher no-match schemas; both defects were corrected and the two cited final runs succeeded. The final report update is documentation-only after the verified CI commit. No merge, main change, deployment or release approval. **BLOCKED / STAGING ONLY.**
