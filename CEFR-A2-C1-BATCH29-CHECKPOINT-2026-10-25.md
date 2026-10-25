# Burmese English Academy — Batch29 staging checkpoint (2026-10-25)
**UNVERIFIED FIRST-PASS DRAFTS ONLY. NEVER MERGE OR PUBLISH.**

## This iteration
- 52 original bilingual drafts: A2 12, B1 14, B2 14, C1 12. English definitions, Myanmar meanings and original examples remain distinct DRAFT fields.
- 52 independent-review packets; English POS/sense, Myanmar naturalness, examples, sense-specific CEFR and George/Emma real listening remain separately pending.
- 16 reversible quarantines: A2 4, B1 4, B2 4, C1 4; named entities, WordNet mismatches, rare POS and inappropriate senses.
- Provisional CEFR tiers are **not** independently verified. Several obvious tier mismatches are explicitly flagged; the pool must be re-tiered or quarantined before publication.

## Exact unique written inventory (not approved)
| Level | Target | Written | Independently checked | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 498 | 0 | 202 |
| B1 | 1,000 | 511 | 0 | 489 |
| B2 | 1,300 | 509 | 0 | 791 |
| C1 | 1,500 | 362 | 0 | 1,138 |
| **Total** | **5,000** | **2,380** | **0** | **2,620** |

A2–C1 unique drafted: **1,880**. Quarantined candidates: **456** (440 prior + 16 new). Prior 182 identical legacy duplicate draft rows excluded from unique totals.

## Structural checks and evidence
- Five parallel GitHub Actions jobs for A2, B1, B2, C1 and ALL are configured to check draft structure, original examples, duplicate prevention, candidate pool POS/tier consistency, quarantine disjointness and unpublished status. **CI results are pending at initial checkpoint creation**; only actual completed job objects and logs can establish pass/fail.
- No independent dictionary page observations, Myanmar reviewer sign-off, grammatical example review, sense-specific CEFR confirmation or listening.
- No complete CEFR George/Emma audio generation or human listening, physical iPhone Safari, hosting limits approval, or live CEFR deployment.
- Production 54 lessons, IELTS 1,000 bank, existing audio, privacy and live main are untouched by this staging-only commit. Staging `cefr-vocabulary-data.js` must remain `entries:[]`.

## Publication gate
Do not merge, publish, count these as independently checked or claim audio validation until all independent reviews, listening, real-device and hosting checks are evidenced. Structural QA success is not linguistic validation.
