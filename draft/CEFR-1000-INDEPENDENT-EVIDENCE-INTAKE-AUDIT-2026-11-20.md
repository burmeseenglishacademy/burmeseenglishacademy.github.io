# CEFR-1000 independent evidence intake completeness audit — 2026-11-20

**Scope:** user-approved 1,000 entries only, not the historical 5,000-word plan. **Status:** staging / NOT RELEASE READY. This is an author-run mechanical audit, **not** independent linguistic, pronunciation, listening or CEFR review.

## Audited source snapshots
- Provisional shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Independent-review task intake: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- Observed 2026-11-20 via authenticated GitHub connector on `cefr-5000-bilingual-qa-staging`. Repository source: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/tree/cefr-5000-bilingual-qa-staging/draft

## Exact per-level intake audit

| Level | Provisional written entries | Review tasks | Tasks with evidence URL | Tasks with observation date | Assigned reviewer | Signed reviewer | Independently approved |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 0 | 0 | 0 | 0 | 0 |
| A2 | 200 | 200 | 0 | 0 | 0 | 0 | 0 |
| B1 | 200 | 200 | 0 | 0 | 0 | 0 | 0 |
| B2 | 200 | 200 | 0 | 0 | 0 | 0 | 0 |
| C1 | 200 | 200 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **1,000** | **1,000** | **0** | **0** | **0** | **0** | **0** |

All 1,000 shortlist records have empty `source_english`, `source_burmese`, and `source_level` fields, and zero true `reviewed_english`, `reviewed_burmese`, `reviewed_example`, `reviewed_level`, `reviewed_pronunciation`, or `release_approved` flags. These counts refer specifically to the two machine-readable manifests: earlier separate author-researched markdown evidence notes do **not** populate independent review tasks and must not be counted as reviewer evidence or signoff.

## Concrete next implementation: fail-closed evidence intake

1. Maintain author-researched source notes separately from reviewer decisions. Each review must bind to immutable shortlist blob SHA, task ID, level, headword, part of speech, **exact sense**, example and source index; reject stale task-to-shortlist mappings.
2. Require reviewer identity distinct from the author, reviewer timestamp, independently examined English definition, fluent Myanmar meaning, original example grammar, source URL, date accessed, and a documented explicit CEFR judgment **for the same sense**. A dictionary URL alone does not prove a level; missing or conflicting sense-level labels must remain unresolved.
3. Reject placeholder URLs, author-only evidence, generic headword-level CEFR citations used for a different sense, unverifiable reviewer identities, empty rationale, and inconsistent review timestamps. Never auto-set reviewed or approved booleans from validator success.
4. Track evidence completeness per level in a machine-readable report, but count **independent approval** only after separately attested English, Myanmar, example and CEFR reviews. Re-check cross-level headword/sense duplication and exactly 200 accepted entries at each level before constructing any approved manifest.
5. Separate lexical review from audio evidence: require George and Emma **headword and example** files for every approved entry, hashes and actual human listening signoffs. File existence, generated waveforms or synthetic checks are not listening approval.
6. Keep release gate closed until independent review, audio listening, browser/mobile regression, physical iPhone Safari evidence, GitHub Pages constraints, production preservation checks and confirmed live deployment all have genuine evidence. Existing 54 lessons, separate IELTS bank, production audio and privacy must remain untouched.

## Priority independent sense-resolution queue
Review the existing author-researched source notes for `signature` (C1 provisional vs Cambridge B1 handwritten-name sense), `retail` (B2 provisional vs Cambridge C1 commercial noun sense), `independent` (B1 vs autonomy-sense concern), `trigger`, `through`, `while`, and `relief`. These are **open editorial questions**, not level changes or approvals. Source URLs and observed dates in the respective earlier markdown notes must be revisited and independently checked before entering a signed review record.

**Current blockers:** 0/1,000 independent approvals; no verified completed final-list George/Emma listening signoffs; no physical iPhone Safari evidence; no verified hosting clearance or production deployment. This audit did not execute GitHub Actions and makes no current-commit CI conclusion.
