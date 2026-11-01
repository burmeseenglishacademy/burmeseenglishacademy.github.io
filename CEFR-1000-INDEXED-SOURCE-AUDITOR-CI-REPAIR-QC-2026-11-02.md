# CEFR-1000 indexed-source auditor CI repair — 2026-11-02

**Scope:** user-approved 1,000 total, exactly 200 provisional cards each for A1, A2, B1, B2, C1. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED; research is not independent human approval.

## Observed failure (actual GitHub Actions evidence)

- Structural run [41339973190](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41339973190), push SHA `783be54126f148554bd7f355aa8c8e88886a8ed7`, concluded **failure** on all six lanes (A1/A2/B1/B2/C1/ALL).
- Actual ALL job `124947710875` log: `FAIL: missing source-access limitation`, at `tools/audit_cefr_1000_crosslevel_connectors_degree_eight.py --level ALL`. The five other lanes failed the same audit step. Earlier audit steps in that ALL log completed before this failure; that does **not** mean the overall run passed.
- Root cause: the auditor searched for the literal words `not independently` in the packet's top-level `source_limitations`. The authentic frozen packet instead states `never as independent exact-sense human signoff`, correctly identifying public search indexing, HTTP 403 direct-page restrictions, and the absence of a CEFR label for *quite*. The literal-string requirement caused a false failure despite an accurate limitation disclosure.

## Staging-only correction

Commit [`fa302048c82da8d5f2c93cee1941000c4d73c6b2`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/fa302048c82da8d5f2c93cee1941000c4d73c6b2) changes only the eight-card auditor. The auditor now checks the **exact pinned, truthful source-limitation statement** rather than a misleading substring. Two new synthetic negative cases reject replacement with a forged independent-access claim or an empty limitation. The original research JSON, its pinned blob SHA, frozen shortlist, review flags, and all production assets are unchanged by that repair.

**Verification boundary:** the auditor source was read back before editing and the GitHub update returned the commit SHA. New six-lane job conclusions/logs for the repair were not yet retrieved when this checkpoint was written; do not claim a pass until those jobs are observed. If any lane still fails, inspect its actual failing step and fix only staging code/data without weakening a legitimate gate.

## Exact current approval ledger

| CEFR | Provisional first-pass written | Independently approved |
| --- | ---: | ---: |
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**Unmet gates:** independent English/Myanmar/example/exact-sense CEFR review; signed 200-per-level deduplicated release manifest; both George and Emma headword/example audio plus genuine listening signoffs; browser/mobile and real physical iPhone Safari evidence; measured GitHub Pages hosting compliance; verified production deployment and preserved 54 lessons, separate IELTS 1,000-word bank, existing George/Emma audio and privacy. Do not merge or publish while any gate is absent.


## Verified post-repair CI — 2 November 2026 SGT

- [Structural run 41347371667](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41347371667), tested **`fa302048c82da8d5f2c93cee1941000c4d73c6b2`**, completed **SUCCESS** for all six independently reported A1/A2/B1/B2/C1/ALL GitHub Actions jobs.
- Actual ALL job **`124969979895`** log confirms the previously failing eight-card indexed-source auditor now passes and its synthetic negative test rejects **166/166** forged-evidence mutations. The same ALL log confirms the six Oxford replacement-candidate audit passes **150/150** synthetic mutation tests; neither is a human-independent review.
- Structural ALL artifact **`13100171246`**. This run did **not** deploy. The documentation commit below postdates the tested SHA and only changes this report.
- Frozen first-pass shortlist: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0** (written/independently approved). Real final George/Emma listening signoffs **0**. All other release blockers above remain.
