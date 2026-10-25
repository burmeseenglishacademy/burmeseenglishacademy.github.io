# Burmese English Academy — CEFR 5,000 batch35 staging checkpoint
**Date:** 25 October 2026 (Singapore time)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release decision:** **UNVERIFIED — NO MERGE, NO PUBLICATION, NO COMPLETION NOTIFICATION**

## Substantive changes in this iteration
- Wrote **45 new original bilingual first-pass entries** with distinct English definitions, Myanmar glosses and grammatical original English examples: **A2 2, B1 22, B2 19, C1 2**. These are **drafts, not independently verified or approved**.
- Added **45 separate independent source-evidence and editorial review packets** for exact English sense/POS, natural Myanmar meaning, sentence grammar/collocation, sense-specific CEFR and later George/Emma listening/real iPhone Safari. Cambridge dictionary URLs are **unvisited lookup destinations**, not evidence observed.
- Reversibly quarantined **85 additional weak candidate headwords**: **A2 3, B1 15, B2 20, C1 47**. Holds identify dubious WordNet senses, wrong part of speech, inflected or plural lemmas, named entities, offensive register and unsupported provisional CEFR levels. The C1 candidate pool contains many common lower-level meanings; **only two C1 drafts** were defensible as tentative specialised/figurative senses, and both remain high-risk.
- Kept all source evidence fields empty, independent approval flags false and pronunciation flags false. No new CEFR audio was generated. No production files were edited.

## Exact unique first-draft inventory, confirmed by the batch35 ALL GitHub Actions job
| Level | Target | Written first drafts | Independently checked and approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 521 | 0 | 179 |
| B1 | 1,000 | 638 | 0 | 362 |
| B2 | 1,300 | 631 | 0 | 669 |
| C1 | 1,500 | 416 | 0 | 1,084 |
| **Total** | **5,000** | **2,706** | **0** | **2,294** |

A2–C1 unique first drafts: **2,206**. Unique quarantined candidate headwords: **676** (not counted as written or approved). Historical duplicate draft rows excluded: **182**. All level assignments are provisional pending sense-specific source review.

## Actual staging commits
1. 45 bilingual draft entries: `54f53ae1f3a3c43c29927f359b40ac64996d7b6d`.
2. 45 separate independent review packets: `208576b1eb33b27e345b613066faa3081469ab44`.
3. 85 reversible quarantine records: `f8557cb9e7c348668c7b7877f420f160d8e05db7`.
4. Fail-closed cumulative and per-level auditor: `82f4d2507bbe62d39fa060ac09e8104736c5771e`.
5. Five-way no-deploy GitHub Actions workflow: `052cb41d4167da42797d71a959eb5fd259427e08`.

## Real GitHub Actions statuses and inspected job logs
[Batch35 workflow run 40193662855](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40193662855) tested commit `052cb41d4167da42797d71a959eb5fd259427e08` and finished **completed / success**. The five individual job records and decoded logs were inspected:

| Matrix job | GitHub job ID | Actual result | Decoded log evidence |
|---|---:|---|---|
| A2 | `121169794576` | completed / success | `STAGING ONLY batch35 A2 PASS: 45 drafts, 85 held, zero approvals; no audio/deploy` |
| B1 | `121169794464` | completed / success | `STAGING ONLY batch35 B1 PASS: 45 drafts, 85 held, zero approvals; no audio/deploy` |
| B2 | `121169794395` | completed / success | `STAGING ONLY batch35 B2 PASS: 45 drafts, 85 held, zero approvals; no audio/deploy` |
| C1 | `121169794255` | completed / success | `STAGING ONLY batch35 C1 PASS: 45 drafts, 85 held, zero approvals; no audio/deploy` |
| ALL | `121169794483` | completed / success | `UNIQUE A2-C1 A2=521 B1=638 B2=631 C1=416 total=2206; independently approved=0`; `A1=500; A1-C1 written=2706; outstanding=2294; quarantine=676; legacy duplicate rows=182` |

These jobs check structure, candidate-pool POS/level alignment, deduplication, example headword, Myanmar script presence, quarantine separation, pending review flags, prior batch34 baseline and the empty unpublished CEFR loader. **They do not prove linguistic correctness, independently observed source evidence, real listening, physical-device testing or hosting capacity.**

## Specific editorial blockers
1. **0/5,000** entries independently approved for exact English sense/POS, natural Myanmar meaning, grammatical examples and sense-specific CEFR. All 45 new source-evidence packets remain pending. Dictionary links were not treated as observed evidence.
2. **2,294** first drafts remain unwritten. **676** quarantined candidate words require independent re-tiering, substitution or documented rejection; 182 historical duplicate rows remain excluded from unique counts.
3. Recheck high-risk batch35 words before approval: A2 `western`, `female`; B1 `quiet`, `cream`, `kingdom`, `split`, `papers`, `talks`; B2 `gaming` (gambling sense, not video games), `fancy`, `josh`, `cop`; C1 `torture` (figurative mental distress), `blowing` (industrial gas-process noun). Their provisional tier may be wrong even when the draft sentence is grammatical.
4. **No complete new CEFR George/Emma pronunciation collection**, no per-file listening approval, no complete final audio manifest and no verified physical iPhone Safari acceptance.
5. No final browser/mobile corpus test, GitHub Pages storage/bandwidth clearance or verified CEFR live deployment.

## Production safety
Production `main` was read at `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged from the previous checkpoint. The staging audit confirmed the public CEFR loader `cefr-vocabulary-data.js` still contains `entries:[]`. The new commits touch only staging draft JSON, review JSON, quarantine JSON, auditor, workflow and this report. The 54 production lessons, IELTS 1,000 bank, existing George/Emma recordings and privacy features were not modified. No merge or deployment was performed.

**Outcome:** 45 useful new bilingual drafts plus 85 reversible evidence-based-risk holds, with real five-way structural CI success and a strict editorial/audio/device/hosting release hold.
