# CEFR-1000 staging CI log verification — 2026-11-11

Scope: **approved 1,000-total** CEFR A1–C1 project, not the superseded 5,000 plan. Staging branch only; no publishing authorization inferred from a successful structural test.

## Verified GitHub Actions evidence

- Run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/43014720921
- Run ID: `43014720921`; associated staging commit: `3e70d8f594390579443ede252b0b06fd4436f359` (from the prior staging commit record; verify commit association separately if needed).
- Jobs API inspected 2026-11-11: **all five** level-specific jobs completed with conclusion `success`, including their `Python provisional audit and adversarial regression` and `Ensure release validator rejects provisional inventory` steps.
- A1 job `130502798125`, A2 job `130502798080`, B1 job `130502798192`, B2 job `130502797784`, C1 job `130502798177`.
- Raw logs successfully retrieved for **A1, A2 and C1** on 2026-11-11. Each includes `PASS: release remains blocked`. Logs explicitly identify missing independent signoffs, missing CEFR evidence, missing `sense_id`, and missing George/Emma audio artifacts in the intentionally rejected provisional inventory. These messages are **expected rejection evidence**, not CI failures or proof of complete review.
- Raw logs for B1 and B2 were **not** retrieved in this inspection; their jobs and steps are confirmed successful by the jobs API.
- Runner warnings about Node.js 20 deprecation for `actions/checkout@v4` and `actions/setup-node@v4` appeared in inspected logs. Plan an independently tested actions version upgrade on staging, without changing production.

## Exact inventory and release blockers

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Inventory counts and zero approvals are from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` metadata inspected 2026-11-11, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. All entries remain editorial hold. Counts mean provisional first-pass entries, **not independently verified CEFR words**.

Unresolved release gates: independent exact-sense English, fluent Myanmar, original example and publisher-supported CEFR review for all entries; normalized sense-level deduplication and cross-level adjudication; 4,000 final British George/Emma headword/example artifacts and genuine listening signoff; browser/mobile regression; physical iPhone Safari review evidence; GitHub Pages hosting/asset limits; and confirmed production deployment plus preservation verification for 54 lessons, separate IELTS 1,000 bank, existing George/Emma audio and privacy guarantees.

**Decision: FAIL CLOSED / STAGING ONLY.** No independent approval, listening, iPhone QA or deployment is asserted by this report.
