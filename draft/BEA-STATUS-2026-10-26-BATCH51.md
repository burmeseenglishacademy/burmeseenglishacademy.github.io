# Burmese English Academy — batch51 staging editorial and CI checkpoint

**Date:** 2026-10-26 (Singapore time)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release:** **UNVERIFIED DRAFT ONLY — DO NOT MERGE OR DEPLOY**

## Actual work
- Wrote **40 original bilingual first-pass entries**: **B2 4, C1 36**. No A2 or B1 drafts were counted because the remaining visible candidate clues at those levels were predominantly non-lemma, inflected or semantically questionable. This is intentional editorial restraint, not a completed level.
- Every draft has its own English definition, original Myanmar meaning, grammatical contextual sentence, candidate-pool POS and explicit unverified/re-tier warning. The C1 group is particularly likely to contain **over-tiered common vocabulary**: a draft is **not** a C1 approval.
- Created **40 separate evidence-review packets** with unobserved Cambridge lookup leads; English sense/POS, fluent Myanmar naturalness, example grammar/collocation, graded sense-specific CEFR, and George/Emma real listening plus physical iPhone Safari are separate pending tasks. No external dictionary page is claimed observed.
- Reversibly held **34 additional candidate headwords**: A2 3, B1 3, B2 14, C1 14. These include inflected forms, named places/people, abbreviations, offensive/derogatory senses and misleading first WordNet senses. Held words are **not** counted as written drafts.
- Added a five-way **A2/B1/B2/C1/ALL** non-deploying GitHub Actions QA workflow, with recursive previous-batch checks, source-pool POS assertions, separate review-stage flags, draft/hold disjointness, unique-word accounting and a production-asset drift guard.

## Exact unique first-pass ledger

| Provisional level | Internal target | Written unique first-pass | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 534 | 0 | 166 |
| B1 | 1,000 | 778 | 0 | 222 |
| B2 | 1,300 | 931 | 0 | 369 |
| C1 | 1,500 | 735 | 0 | 765 |
| **Total** | **5,000** | **3,478** | **0** | **1,522** |

- A2–C1 **2,978 unique first-pass written**; A1 **500**. The **182 historical duplicate rows** are excluded from unique written counts.
- **1,143 reversible holds**, disjoint from all written words. All levels and dictionary senses remain provisional.
- **0/5,000 independent approvals**; no source-based English/Myanmar/sense/CEFR approval or audio listening approval in this batch.

## Commits and actually observed CI
- Content, separate review tasks, reversible holds, Python audit and workflow committed atomically as `39e718515f0d979f3338bb7bcae599c784ffb37f`.
- First run [40266383433](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40266383433) **failed** all five jobs because the structural audit compared a Python Counter without zero-count A2/B1 keys to an explicit expected dictionary containing zeros. This was a **QA code defect**, not a linguistic sign-off.
- Corrected the zero-count assertion in commit `5b9fe180d7278b2a6000689e382367167b4be43a`.
- Corrected run [40266428089](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40266428089) at exact content/QA SHA `5b9fe180d7278b2a6000689e382367167b4be43a`: **completed / success**, five actual jobs:
  - A2 job `121389741921`: success.
  - B1 job `121389741900`: success.
  - B2 job `121389741807`: success.
  - C1 job `121389741950`: success.
  - ALL job `121389741685`: success.
- Inspected decoded ALL job log: `A1=500; A1-C1 written=3478; outstanding=1522; quarantine=1143; historical duplicate rows excluded=182`; `STAGING ONLY batch51 ALL PASS: 40 drafts, 34 holds, zero approvals; no audio/deploy`; `PASS: production lesson, IELTS, George/Emma audio and privacy assets unchanged`.
- A successful **structural** workflow is not evidence of independently accurate Burmese, graded CEFR, learner dictionary sense, recorded audio quality, real-device Safari or release readiness.

## Editorial and release blockers
1. **C1 over-tiering is the largest immediate content-quality risk.** The 36 C1 first-pass words in this batch include frequent everyday words such as `graph`, `headline`, `paragraph`, `advise` and `ranch`. They must receive sense-specific graded source evidence and likely re-tiering; **do not approve C1 merely because the source pool placed them there**.
2. The original 5,000-word candidate pool is increasingly exhausted of clear A2/B1 lemmas. The remaining A2 `married` (unusual nominal sense), `anti` (informal nominal sense) and `stupid` (derogatory nominal sense), and B1 `teeth` (plural), `grace` (specialised religious sense) and `sleeping` (gerund noun) were held rather than inflated into easy drafts. Future expansion needs a cleaner learner-focused candidate list, not a WordNet-first-sense quota fill.
3. **No independent dictionary page observation or fluent Myanmar sign-off** was performed in this batch. All 40 review packets remain pending; the URL leads alone are not evidence.
4. **No new CEFR George/Emma audio** was generated or independently listened to. Full audio inventory, pronunciation approval, mobile/browser and physical iPhone Safari checks, GitHub Pages storage/bandwidth checks and live production deployment remain **not passed / not established**.
5. Production `main` was **not changed**. The GitHub Actions ALL job compared protected lesson, IELTS 1,000, George/Emma audio and privacy paths with `main`, and `cefr-vocabulary-data.js` remained empty. Staging must not publish incomplete vocabulary or audio.

**Next substantive priority:** create a clean, source-supported A2/B1 replacement-headword pipeline and audit the high-frequency C1 tier assignments before further approvals. Keep all unverified content isolated and do not notify project completion until every editorial, audio, device, hosting and live-release gate is truly satisfied.
