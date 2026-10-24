# Burmese English Academy — staging batch11 — 2026-10-24

**STAGING ONLY. UNVERIFIED. NEVER DEPLOY.**

## Substantive new drafting
- 62 original bilingual drafts: A2 20, B1 20, B2 20, C1 2.
- Separate labelled stages for English definition/POS, natural Myanmar meaning, original grammatical usage example, independent source-evidence review tasks and later audio listening.
- 17 additional likely lower-level candidate headwords quarantined from provisional C1; do not count these as written. Existing 119 quarantined; new total 136.
- Only 2 C1 drafts were considered plausible enough for first-pass drafting, but both remain **high-risk provisional levels**, not independently supported C1 assignments. Avoided padding the count with obvious A1–B2 words.
- All source fields are empty; Cambridge URLs are unvisited lookup leads, not evidence.
- No independent linguistic review, CEFR confirmation, native Burmese review, audio generation, listening, browser or iPhone checks were performed as part of drafting.

| Provisional level | Target | Written drafts | Independently approved | Still unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 236 | 0 | 464 |
| B1 | 1000 | 236 | 0 | 764 |
| B2 | 1300 | 236 | 0 | 1064 |
| C1 | 1500 | 218 | 0 | 1282 |
| **TOTAL** | **5000** | **1426** | **0** | **3574** |

## Release blockers and controls
- Source-based review of exact English senses, CEFR, Burmese meanings, example grammar/collocation and lexical POS is incomplete.
- All George/Emma collection generation and actual human listening validation for the full 5000-word bank are incomplete.
- Browser/mobile and physical iPhone Safari, hosting/bandwidth, and final production deployment remain unverified.
- The existing 54 lessons, IELTS 1000 bank, production George/Emma audio and privacy code were not modified. Unapproved CEFR content remains unpublished via `cefr-vocabulary-data.js` with empty entries.
- The new five-way matrix checks **structure and quarantine only**; a green Actions job is never editorial approval.

## Commits and tests
- This report is created in the same atomic staging commit as batch11; inspect GitHub branch commit and actual Actions run/job logs after commit. No job is claimed passed before GitHub reports success.
- If a check fails, record the failure and repair on staging only. Do not merge unverified content.

## Actual initial QA failures and repairs
- Initial content commit `1cfdfe177b4e24ff1788c2250d88aa08bb066234` produced batch11 five-job run `40095304427`: **FAILURE** due an incorrectly escaped regex in the new test script. The script was corrected in `4e294f5b06738172c3aaa0dbb0472a32bd8d33ea`; a rerun was queued.
- Existing quarantine audit run `40095304229`: **FAILURE** because its allowlist did not yet recognise the newly documented unsupported-provisional-C1 hold category; this commit adds a constrained category and C1 assertion.
- Existing bilingual structural run `40095304209`: **FAILURE** because batch11 provenance text started with 'Original editorial' instead of the required 'Original draft'; this commit aligns the note while preserving the explicit unverified warning.
- No green job or editorial approval is inferred from a source-code repair. Inspect the corrected push's GitHub Actions statuses and logs separately.

## Corrected GitHub Actions evidence (actual completed runs)
- Repair commit: `a2f07c7656c5076fc8e9f0dce8a7676adba7675a`. No production branch, 54 lessons, IELTS 1000, George/Emma audio or privacy files changed.
- Batch11 five-way matrix run [40095390429](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40095390429): **COMPLETED / SUCCESS**. Individual A2, B1, B2, C1, ALL jobs each passed; ALL job `120876427716` reports 62 unverified drafts, 0 independent approvals, no deployment.
- Quarantine run [40095390441](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40095390441): **COMPLETED / SUCCESS**. Job `120876427537` reports 136 held headwords, none drafted or approved.
- Existing bilingual/source-evidence audit run [40095390452](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40095390452): **COMPLETED / SUCCESS**. Job `120876427635` reports 926 A2–C1 drafts, A2=236 B1=236 B2=236 C1=218; 21 previous source observations and 8 previously flagged conflicts; 0 independent approvals.
- All 14 observed workflows triggered by the repair commit `a2f07c7` finished **COMPLETED / SUCCESS**, including prior batch05–10, candidate triage, previews and parallel four-level structural checks. These are not linguistic approvals or audio listening tests.
- Initial failed jobs are retained in history, not hidden or called successes. They resulted from new QA regex escaping, unrecognised quarantine risk enum, and provenance text mismatch; fixes were made and rechecked.
- Production release remains **BLOCKED**; live website deployment was not performed.
