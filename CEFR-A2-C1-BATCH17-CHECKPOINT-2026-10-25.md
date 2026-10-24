# Burmese English Academy — batch17 staging checkpoint (25 October 2026 SGT)

**Status: STAGING ONLY — NOT RELEASE READY. Do not merge or publish unverified data/audio.**

## Substantive changes and exact inventory
- Added **50 original first-pass bilingual entries** in `draft/A2-C1-EDITORIAL-BATCH17.json`: A2 **14**, B1 **14**, B2 **14**, C1 **8**. Every entry has an original English learner definition, Myanmar first-pass meaning, part of speech and original contextual example. These are **drafts**, not verified vocabulary.
- Added **50 separate source and editorial review tasks** in `draft/A2-C1-REVIEW-TASKS-BATCH17.json`. English sense/POS, Burmese meaning, example grammar, CEFR sense-level and George/Emma listening are five distinct **pending** stages. Source URLs are *suggested consultation links*, not proof that source pages were read. All independent approvals remain false.
- Added **21 new candidate quarantine holds** in `draft/A2-C1-QUARANTINE-BATCH17.json`: names, places, register-sensitive profanity, inflected forms, wrong WordNet first senses and suspicious CEFR tier. Holds are provisional editorial triage, not permanently rejected words.
- Four additional **drafted** entries (`spend`, `survey`, `dramatic`, `accordance`) have explicit WordNet first-sense mismatch review tasks. Six entries (`agree`, `seem`, `deep`, `create`, `delay`, `visible`) have possible lower-tier CEFR review warnings. None of these warnings is a verified source finding.
- Fixed `minimum` to use the noun sense in its example; expanded `visible` definition after a structural QA failure.

| Level | Drafted unique headwords | Target | Independently approved |
|---|---:|---:|---:|
| A1 | 500 | 500 | 0 |
| A2 | 326 | 700 | 0 |
| B1 | 328 | 1,000 | 0 |
| B2 | 326 | 1,300 | 0 |
| C1 | 288 | 1,500 | 0 |
| **Total** | **1,768** | **5,000** | **0** |

A2–C1 total **1,268/4,500**; **3,232** A2–C1 entries still lack original first drafts. This is a unique-headword count: **182 legacy identical duplicate rows were excluded**, as printed by the ALL job. Across existing quarantine records and batch17 there are **219 unique holds**, which are not counted as new drafts.

## Actual GitHub test evidence
- Final corrected staging content commit: [`586ae106d6b9a90dc284079721aa886dcf9e6660`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/586ae106d6b9a90dc284079721aa886dcf9e6660).
- [GitHub Actions batch17 run 40121971469](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40121971469): **completed / success**. Inspected real jobs: A2 **success**, B1 **success**, B2 **success**, C1 **success**, ALL **success**.
- ALL job log explicitly printed `A2=326 B1=328 B2=326 C1=288 total=1268; independent approvals=0` and `50 new drafts, 21 holds, zero approvals, no audio/deploy`.
- Earlier batch17 runs [40121920311](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40121920311), [40121941640](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40121941640) and [40121954119](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40121954119) **failed** during iteration, including a B2 `visible` definition shorter than the audit's minimum; the final run passed after correction. These failed runs are not described as successes.
- Structural checks are NOT a source-based English/Myanmar semantic review, a verified CEFR classification, a native-speaker sign-off or actual audio listening.

## Production and release blockers
- Verified `main` at `dca0db7aa30118ecc18350db8dc406e6cac91554`; the new staging work did **not** alter production.
- `cefr-vocabulary-data.js` still has `entries:[]` and the unverified release marker. The 54 production lessons, 1,000 IELTS words, previously published George/Emma recordings and privacy architecture were not changed by this batch.
- No new CEFR audio was generated, independently listened to, or deployed in this batch.
- Outstanding: 3,232 more A2–C1 original bilingual drafts; independent sense/POS, Myanmar, CEFR and example approvals for **all 5,000**; complete George/Emma word/example audio, listening validation, actual iPhone Safari checks, browser/mobile accessibility, hosting size/bandwidth validation and verified live production deployment.
- **Never merge into `main` or claim 100% completion until all gates are evidenced.**
