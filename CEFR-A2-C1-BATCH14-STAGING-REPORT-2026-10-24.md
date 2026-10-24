# Burmese English Academy — Batch14 staging editorial checkpoint
Date: 24 October 2026, Singapore. Branch: `cefr-5000-bilingual-qa-staging`.

**NOT RELEASE READY. DO NOT MERGE INTO MAIN.**
Batch14 adds **42** original first-pass bilingual vocabulary drafts: A2 12, B1 10, B2 12, C1 8. All definitions, Myanmar glosses and examples are **drafts**, not independently reviewed. The separate review-task file contains **42** English-sense, Burmese, example, CEFR and George/Emma listening review tasks; all remain pending. No source URL was opened as evidence for these new drafts.

Batch14 also holds **14** other risky candidate headwords for sense-specific CEFR and polysemy review (6 provisional A2, 8 provisional C1). These are **provisional quarantines, not independently proven rejections**.

## Exact inventory (unique headwords, excluding identical repeat rows)
| Level | Curriculum target | Written first-pass drafts | Independently approved |
|---|---:|---:|---:|
| A1 | 500 | 500 | 0 |
| A2 | 700 | 283 | 0 |
| B1 | 1,000 | 281 | 0 |
| B2 | 1,300 | 283 | 0 |
| C1 | 1,500 | 261 | 0 |
| **Total** | **5,000** | **1,608** | **0** |

The A2–C1 source files contain 1,290 raw draft rows but only **1,108 unique headwords**; **182** identical legacy repeats are deliberately **not counted twice**. The new batch14 headwords are not repeated in earlier draft files. **3,392** unique first-pass drafts remain unwritten. All 5,000 entries still require independent sense/CEFR/Myanmar/example approval.

## QA and release blockers
A new five-way level-specific GitHub Actions workflow and structural audit check candidate alignment, original text presence, example headwords, false approval flags, quarantine separation, duplicate reconciliation and production data isolation. **CI executed and inspected:** [GitHub Actions run 40105003949](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40105003949) completed **success** at 23:00 SGT, 24 October 2026. Five jobs (A2, B1, B2, C1 and ALL) each completed **success**. The ALL job log explicitly reports `UNIQUE A2-C1 WRITTEN: A2=283 B1=281 B2=283 C1=261 total=1108; independent approvals=0`, `Legacy identical duplicate rows= 182 not counted twice`, and `STAGING ONLY: batch14 ALL structure PASS; 42 new drafts, 14 holds, 0 independent approvals, no audio/deploy`. This verifies structural consistency only, not meanings, pronunciation or CEFR suitability.

Outstanding: authoritative word-specific source review, Burmese language specialist approval, corrected CEFR assignments, full George/Emma recording and actual listening validation, browser/mobile and physical iPhone Safari regression, measured GitHub Pages hosting limits and live deployment acceptance. No new audio, published data or production changes are authorised.

## Actual GitHub commit and production isolation
- Batch14 implementation commit: [`1b9a79a1cc38d989387a6f48065b6b72aa5fd8c6`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/1b9a79a1cc38d989387a6f48065b6b72aa5fd8c6).
- GitHub Actions run: [40105003949](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40105003949), five successful jobs, logs inspected.
- Production `main` independently checked at `dca0db7aa30118ecc18350db8dc406e6cac91554`; the 54 existing lessons, IELTS 1,000-word bank, existing George/Emma audio and privacy features were not modified by this staging commit.
- This checkpoint is **not** a 5,000-word completion notice and is not permission to deploy.
