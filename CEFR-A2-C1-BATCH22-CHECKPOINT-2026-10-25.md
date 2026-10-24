# Burmese English Academy — batch22 staging report (25 October 2026 SGT)

**UNVERIFIED EDITORIAL DRAFTS — STAGING ONLY — DO NOT MERGE, PUBLISH OR GENERATE RELEASE AUDIO**

## Substantive editorial work completed
- Authored **52 original English-definition / Myanmar-meaning / grammatical-example first-pass drafts** in `draft/A2-C1-EDITORIAL-BATCH22.json`: **A2 16, B1 16, B2 16, C1 4**. The English definitions, natural-first-pass Myanmar meanings and original examples are stored as separate fields. All sense and tier decisions remain provisional.
- Created **52 separate five-stage independent review packets** in `draft/A2-C1-REVIEW-TASKS-BATCH22.json`: dictionary English POS/sense, native Myanmar translation, sentence grammar/collocation, sense-specific CEFR evidence, and real George/Emma listening/physical iPhone Safari review. Cambridge dictionary URLs are **unvisited reference leads**, not observed source evidence.
- **Quarantined 40 additional distinct candidates** in `draft/A2-C1-QUARANTINE-BATCH22.json`: 10 each provisional A2/B1/B2/C1. Reasons include named entities, demonym capitalization, inflected/gerund forms and WordNet sense collisions. These are reversible holds, not independently adjudicated rejections.
- Expanded the staging-only candidate preview to **200 words per provisional tier**, enabling selection beyond weak high-frequency WordNet senses; observed the resulting real preview run.
- Added **five-way parallel GitHub Actions structural QA** for A2, B1, B2, C1 and ALL, with no deployment steps.

## Exact unique first-pass written inventory (not independently approved)

| Provisional level | Target | Unique written drafts | Independently approved | Still unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 398 | 0 | 302 |
| B1 | 1,000 | 398 | 0 | 602 |
| B2 | 1,300 | 394 | 0 | 906 |
| C1 | 1,500 | 308 | 0 | 1,192 |
| **Total** | **5,000** | **1,998** | **0** | **3,002** |

The unique A2–C1 first-pass written total is **1,498**. The older source files also contain **182 identical legacy duplicate rows**, excluded from all unique counts. Total disjoint quarantined A2–C1 candidate headwords: **339**. None of these holds is counted as written or approved.

## Actual GitHub commits
- [`c15bd55ecae361beb695128746d9d2af759f1741`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/c15bd55ecae361beb695128746d9d2af759f1741): expand candidate preview.
- [`9ec59d1a171467bfa49fa5e6757fffa06298db21`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/9ec59d1a171467bfa49fa5e6757fffa06298db21): 52 bilingual drafts.
- [`37b8e4951e1b347db01903cc8442b43fe236a3e1`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/37b8e4951e1b347db01903cc8442b43fe236a3e1): 52 independent review task packets.
- [`e902f08358c3ea1f2573af82ddea015ec71c3f03`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/e902f08358c3ea1f2573af82ddea015ec71c3f03): 40 quarantined candidates.
- [`a937757881cb099e56a0532362aaa149e33f1412`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/a937757881cb099e56a0532362aaa149e33f1412): fail-closed structural auditor and cumulative inventory checks.
- [`d799fc85c61571043c99b68cccc25c4ca1d0fe39`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/d799fc85c61571043c99b68cccc25c4ca1d0fe39): parallel staging-only GitHub Actions workflow.

## Observed real GitHub Actions evidence
- [Expanded preview run **40143781686**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40143781686): **completed / success**. The actual job log was read and contained 200 provisional candidate clues per level; WordNet clues are not dictionary or CEFR approvals.
- [Batch22 five-way QA run **40144025989**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40144025989) at commit `d799fc85`: all five jobs **completed / success**, and each actual decoded job log was inspected:
  - A2 job `121021465502`: structural PASS.
  - B1 job `121021465630`: structural PASS.
  - B2 job `121021465507`: structural PASS.
  - C1 job `121021465479`: structural PASS.
  - ALL job `121021465488`: structural PASS; log states `A2=398 B1=398 B2=394 C1=308 total=1498; independent approvals=0`; `A1-C1 written=1998; first drafts outstanding=3002; legacy duplicate rows=182`; `52 drafts, 40 holds, zero approvals; no audio/deploy`.
- GitHub compare `c15bd55..d799fc85` was inspected: **exactly five newly added staging files** (drafts, review packets, quarantine, auditor, workflow), no existing site, lessons, IELTS bank, MP3 or privacy files changed in these five commits.
- Direct staging read of `cefr-vocabulary-data.js` still shows **`entries:[]`**. Direct production `main` branch read shows head `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged in this iteration.

## Remaining hard release blockers
1. **0 / 5,000 independently approved** for sense, POS, natural Myanmar, grammatical example and sense-specific CEFR. Several provisional tiers may be wrong (especially C1; some A2/B2 terms are likely mislevelled). Structural QA cannot adjudicate these.
2. **3,002** first-pass entries not yet written. The provisional 5,000-word candidate pool is not a verified CEFR headword list; held or mislevelled candidates may need replacement.
3. No batch22 George/Emma CEFR recordings were generated or listened to. The **4,652 existing production lesson/IELTS MP3s** are separate from the new CEFR bank; their existence does not prove new CEFR audio coverage or subjective pronunciation correctness.
4. Real physical iPhone Safari, end-to-end mobile/browser release QA, hosting bandwidth/storage budget for the expanded CEFR collection, and production deployment **have not passed**.
5. Never mark a word or recording independently reviewed based on an AI draft, a WordNet clue, an unvisited Cambridge URL, a synthetic file check or a structural CI success.

**Release decision:** HOLD. No merge, no live production change, no completion notification.
