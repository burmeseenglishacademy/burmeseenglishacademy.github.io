# BEA CEFR 1000 — B1 mixed Oxford word/POS evidence checkpoint (2026-10-28)

**Scope:** The user-approved **1,000 TOTAL** CEFR A1–C1 vocabulary entries (200 per level), NOT the superseded 5,000-word plan. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED / STAGING ONLY. No merge, production deployment, independent human approval or device/audio signoff.

## Direct primary-source observations

Directly inspected Oxford University Press's official [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-28**. PDF pages below are 1-based; extracted-text lines are 0-based. These are **publisher word/part-of-speech level observations only**, not exact-sense CEFR proof or independent human review.

| B1 draft word | Oxford word/POS level | PDF page / text line | Editorial triage |
|---|---|---|---|
| independent | A2 adj. | 5 / 1301 | Lower than draft; ordinary independence sense |
| impact | B1 n., v. | 8 / 2136 | Word/POS aligns; verify strong-effect noun |
| cancer | B2 n. | 10 / 2679 | Higher than draft; medical-definition accuracy |
| civil | B2 adj. | 10 / 2695 | Higher than draft; civil-rights example may differ from military/civilian definition |
| organization | A2 n. | 6 / 1439 | Lower than draft; check British *organisation* spelling |
| multiple | B2 adj. | 11 / 3016 | Higher than draft; ordinary more-than-one sense |
| operation | B1 n. | 9 / 2252 | Word/POS aligns; distinguish warehouse and surgical senses |
| disease | A2 n. | 5 / 1136 | Lower than draft; ordinary illness sense |
| notice | A2 v., n. | 6 / 1426 | Lower than draft; written-announcement noun |
| basic | B1 adj. | 7 / 1844 | Word/POS aligns; original example still requires review |
| effective | B1 adj. | 8 / 2006 | Word/POS aligns; distinguish effective from efficient |
| highly | B1 adv. | 8 / 2119 | Word/POS aligns; intensifier/collocation review |

**Breakdown:** 4 Oxford A2 versus provisional B1, 5 Oxford B1 matches, 3 Oxford B2 versus provisional B1. **7 word/POS level discrepancies** need explicit independently reviewed sense reconciliation or replacement/retiering. None is automatically reclassified. Original English definitions, fluent-Myanmar first-pass meanings, example sentences, upstream source paths/indexes/blob hashes, direct publisher URL, observation date, and per-word independent-review instructions are preserved in [the 12-record evidence packet](draft/CEFR-1000-OXFORD-B1-MIXED-TWELVE-2026-10-28.json).

## Safeguards and actual verification

- Created [fail-closed provenance auditor](tools/audit_cefr_1000_oxford_b1_mixed_twelve.py) that binds the packet to the unchanged canonical shortlist, exact publisher word/POS observations, PDF locators, bilingual/example snapshots, editorial risks and held flags; it rejects **28/28** forged or corrupted cases in the observed ALL-job log.
- Added the auditor to the existing **six parallel A1/A2/B1/B2/C1/ALL** structural GitHub Actions jobs and to the no-deployment documentary gate.
- Added an **empty** `oxford_b1_mixed_twelve_review_receipts` ledger collection. The release gate requires genuine independently signed, content-hash-bound exact-sense B1 evidence for every retained entry and explicit rationales/changed content for mismatched levels. Unknown, duplicate, forged or malformed receipts are rejected; a negative test was added.
- [Structural run 40668288398](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40668288398), code head `1f61cdf75bf38556ba120f753024b275f5a4317c`: actual six job conclusions **success**; ALL job `122748311263` logged **28/28 negative mutations rejected** and protected production paths unchanged.
- [Documentary run 40668328425](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40668328425), head `bc94ff58812f659c98eddd83b6456d2c8aef35bc`: actual documentary job `122748447187` **success as report-only**, not a release pass. Log confirms zero independent approvals, zero final both-voice listening receipts, missing real physical iPhone Safari and measured hosting evidence, and protected production paths unchanged.
- Latest unknown-receipt negative-test commit [`6657180fe7385923b00559558452ce30dd858fe6`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/6657180fe7385923b00559558452ce30dd858fe6) was verified by [post-commit documentary run 40668387486](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40668387486), job `122748644449`: actual **success**. Log explicitly confirms **28/28** negative provenance mutations rejected, unknown forged B1 receipt rejected, zero source-reviewed words, zero both-voice listening signoffs and protected production paths unchanged.

## Exact release-blocking counts

| Level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Final George/Emma headword+example recordings have **0/1,000 completed independent both-voice listening receipts**. This is **not** a claim that all audio files are absent. Full real desktop/mobile browser regression, physical iPhone Safari, measured GitHub Pages site/repository/bandwidth limits, human-independent bilingual/example/CEFR signoff, preserved full production audio inventory and confirmed public deployment remain outstanding. CI path-diff checks protect the existing 54 lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy code, but do not substitute for final full production-asset verification.

**Decision:** STAGING ONLY / NOT RELEASE READY. Public launch remains conditional on every specified real QC gate, not on documentary or structural CI success.
