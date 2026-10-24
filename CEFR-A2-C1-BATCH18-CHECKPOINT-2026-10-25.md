# Burmese English Academy — batch18 staging checkpoint (25 October 2026 SGT)

**Status: STAGING ONLY / UNVERIFIED / DO NOT MERGE OR PUBLISH.**

## Substantive editorial work completed

- Created **40 original first-pass bilingual draft entries** in `draft/A2-C1-EDITORIAL-BATCH18.json`: **A2 12, B1 12, B2 12, C1 4**. Each contains a selected POS, original learner English definition, first-pass Myanmar meaning and original contextual sentence. These are **NOT independently reviewed**.
- Created **40 separate five-stage review packets** in `draft/A2-C1-REVIEW-TASKS-BATCH18.json`: English sense/POS, Myanmar idiom/sense, original example grammar, sense-specific CEFR evidence, and actual George/Emma listening. **All review flags remain false.** Cambridge dictionary URLs are **unvisited leads**, not observed evidence.
- Added **20 provisional candidate quarantine records** in `draft/A2-C1-QUARANTINE-BATCH18.json`, including WordNet first-sense mismatches, inflected forms, proper names, homographs, and register-sensitive material. These are **holds**, not permanent editorial rejections.
- Updated `tools/list_cefr_next_candidates.py` to exclude **all** previous batch drafts and all quarantine files rather than only the starter, with a clue-based warning filter. It is a candidate preview, **not a CEFR validator**.
- Added `tools/audit_cefr_batch18_review_tasks.py` and `.github/workflows/cefr-batch18-review-qa.yml` with five parallel staging-only checks for A2/B1/B2/C1/ALL. Checked pool membership, prior unique-headword exclusion, quarantine isolation, separate review task matching, empty approval/source fields, draft structure, exact per-level totals and empty release dataset.
- Improved three example sentences after the first passing workflow to make `society`, cytoplasmic `streaming` and `customs duties` more natural and sense-specific. Re-ran checks against the corrected head commit.

## Exact staging inventory

| Provisional CEFR | Target | Unique first-pass written | Independently approved | Not yet drafted |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 338 | 0 | 362 |
| B1 | 1,000 | 340 | 0 | 660 |
| B2 | 1,300 | 338 | 0 | 962 |
| C1 | 1,500 | 292 | 0 | 1,208 |
| **Total** | **5,000** | **1,808** | **0** | **3,192** |

A2–C1 total is **1,308** distinct first-pass headwords, excluding **182 identical legacy duplicate rows**. Prior checkpoint reported 219 unique quarantines; new 20 holds are disjoint from existing holds per the ALL structural audit, giving **239 total distinct holds**. Holds are not counted as drafted words or approvals.

## Real GitHub commits and test evidence

- Candidate preview correction commit: [`0a1281c404e3ddaed113fe7a2b631398db112cdf`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/0a1281c404e3ddaed113fe7a2b631398db112cdf).
- Batch18 initial multi-file commit: [`d0e964b5b43d2c2969a00e05c0db5c2db4c317e5`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/d0e964b5b43d2c2969a00e05c0db5c2db4c317e5).
- Example-quality revision commit: [`7fbc0033787a6c0adfb043b69353bbb0b3bba009`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/7fbc0033787a6c0adfb043b69353bbb0b3bba009).
- [Candidate-preview GitHub Actions run 40124724780](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40124724780): **completed / success**, actual preview job logs inspected.
- [Initial batch18 run 40124921531](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40124921531): **completed / success**, all A2/B1/B2/C1/ALL jobs inspected.
- [Final revised batch18 run 40124959012](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40124959012): **completed / success**, all **five** level jobs inspected; ALL job `120964297160` log read directly. Log prints: `A2=338 B1=340 B2=338 C1=292 total=1308; independent approvals=0`, `A1-C1 written=1808; first drafts outstanding=3192`, `40 drafts, 20 holds, zero approvals; no audio/deploy`.
- **These checks establish only staging data/structural integrity.** They do not certify the correctness of English or Myanmar meanings, real CEFR classifications, grammar naturalness, audio pronunciation, physical iPhone Safari behavior or live deployment.

## Production protection and blockers

- Confirmed production `main` commit remains `dca0db7aa30118ecc18350db8dc406e6cac91554`; the staging branch after example fixes was `7fbc0033787a6c0adfb043b69353bbb0b3bba009` before this report commit.
- `cefr-vocabulary-data.js` remains `entries:[]`; **no unverified CEFR vocabulary is released**. The 54 existing lessons, separate IELTS 1,000-word bank, existing George/Emma audio and privacy features were not changed by these staging commits.
- **No new CEFR audio** was generated or listening-validated in this run. No independent Myanmar language reviewer, CEFR evidence reviewer or pronunciation listener signed off.
- Provisional candidate tiers are frequency-derived and WordNet first senses can be misleading. The flagged entries, particularly `marine`, `quarters`, `reserves`, `streaming`, `customs`, `bush`, `parking`, `awful` and `silent`, require **sense-specific source verification and possible reclassification**.
- Outstanding: **3,192** first drafts, independent approvals for **all 5,000**, all George/Emma recordings and real listening, browser/mobile regressions, **physical iPhone Safari**, hosting/bandwidth verification, and actual production deployment confirmation.

**No completion notification or merge is justified.**
