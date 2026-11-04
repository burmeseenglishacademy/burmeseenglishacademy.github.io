# CEFR-1000: real CI log verification and release-gate scope (2026-11-04)

**Status:** STAGING ONLY — NOT independently reviewed, not audio-approved, not ready to release. Scope is **1,000 total** (A1/A2/B1/B2/C1: 200 each), not the superseded 5,000 proposal.

## Directly inspected evidence
- GitHub Actions run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41801157929
- Run's five jobs returned `completed / success`: A1 `126476956545`, A2 `126476956833`, B1 `126476956739`, B2 `126476956787`, C1 `126476956858`. These are job conclusions, **not linguistic signoffs**.
- Retrieved the **actual A1 raw job log** (`126476956545`) on **2026-11-04**. It explicitly shows `Ran 14 tests ... OK` for `test_cefr1000_release_gate.py` and `Ran 10 tests ... OK` for `test_cefr1000_level_lane.py`; it also shows the job's explicit structural-only/no-deploy disclaimer. A1 log review does **not** substitute for retrieving all four other job logs. Source: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41801157929/job/126476956545
- Actual frozen shortlist file `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, inspected on **2026-11-04**. Parsed `entries` length = 1,000 and level counts = 200 each. `independently_approved_by_level` is 0 for every level; its release status explicitly says `DO_NOT_PUBLISH`. First-pass text exists, but is unverified.
- Independent-review tasks file path: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, blob `88f472e4c79e5e9b6ae5957f5244f9cb60dc0ef2`; connector returned no decoded text for this file on this run, so its contents were **not** audited.

## What the A1 log proves and does not prove
The shared tests exercise adversarial cases including absent independent review, missing listening, missing physical iPhone evidence, malformed sources, and provisional hold. The level-lane suite exercises count corruption, cross-level duplicate sense, hold, missing George headword listening, missing Emma example clip, missing Myanmar review and CEFR observation. These are synthetic structural tests; passing does **not** establish genuine reviews, audio existence, real listening, device QA, Pages readiness or deployment. No claim is made that the latest staging commit passed CI.

## Editorial evidence still requiring external confirmation
- `civil` (B1 adjective, source index 51) defines non-military/ordinary-citizen sense, but its `civil rights` example uses a different collocation; resolve sense and source-backed level before publication. Earlier Cambridge research flagged a C1-vs-B1 conflict; the publisher page was **not** re-fetched during this run.
- `fine` (A2 adjective, source index 864) defines acceptability, while `The weather was fine for our picnic.` may demonstrate pleasant weather instead. Independent sense alignment required.
- `permit` (C1 noun, source index 569) needs a publisher-backed CEFR label for the *document* sense, not a generic headword label. Verify British noun pronunciation separately.
- `training` (A2 noun, source index 603) and `conduct` (B2 verb, source index 250) likewise require exact-sense publisher evidence and independent fluent Myanmar/example review.

These are **editorial risk observations**, not independent approvals, not verified publisher claims, and not changes to the frozen shortlist.

## Release blockers and non-actions
| Level | First-pass entries | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

All 1,000 remain on editorial hold. No final George/Emma per-headword/per-example inventory or real listening signoff was verified; no mobile/browser regression or physical iPhone Safari evidence was verified; no GitHub Pages hosting clearance or production deployment was verified. Preserve the 54 lessons, separate IELTS 1,000-word bank, existing George/Emma production audio, and privacy protections. **No main-branch write, merge, release, flag change or publication authorised by this report.**

**Next substantive work:** retrieve remaining four job logs; add precise source-backed CEFR sense observations with dated publisher URLs; arrange genuinely independent bilingual review; prepare fail-closed audio/listening and physical-device evidence manifests. Keep staging blocked until every gate has independently verifiable evidence.
