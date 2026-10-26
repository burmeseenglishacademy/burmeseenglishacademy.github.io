# BEA CEFR 5,000 — Batch64 staging checkpoint
**27 October 2026, 01:20 SGT. STAGING ONLY — NOT RELEASE-APPROVED. DO NOT MERGE OR PUBLISH.**

## Actual substantive editorial work
- Created **64 original bilingual first-pass proposals**, evenly split A2 **16**, B1 **16**, B2 **16**, C1 **16**. Every proposal includes an original English sense definition, a Myanmar meaning, an original grammatical example, and a provisional CEFR level. **All 64 are unverified drafts.**
- Created **64 independent review packets** with distinct English sense/register, fluent Myanmar meaning, original example, graded sense-specific CEFR evidence, and George/Emma pronunciation/listening/device stages. Every independent approval flag remains false.
- **13 proactive editorial risk holds** (regional variants, compounds, specialist registers and unsupported CEFR). Cross-corpus structural triage detected **14 wordform collisions** with the original candidate pool or earlier drafts. Some collisions overlap explicit holds.
- Actual five-way structural CI: **41 eligible provisional first-pass drafts** (A2 **9**, B1 **9**, B2 **14**, C1 **9**) and **23 reversibly quarantined** (A2 **7**, B1 **7**, B2 **2**, C1 **7**). Eligible does **not** mean linguistically approved. Quarantined proposals are not added to the eligible-written ledger.
- Additional exploratory dictionary observations for **doorbell, streamline, coerce** are stored separately in `draft/A2-C1-SOURCE-OBSERVATIONS-BATCH64.json`. These were real retrieved dictionary snippets, **not independent editorial sign-offs**, and **no graded sense-specific CEFR evidence was observed**. Streamline remains quarantined as a duplicate.

## Exact eligible-written ledger after batch64
| Level | Target | Previous eligible | Batch64 eligible | Eligible written now | Independently approved | Remaining unwritten |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | **500** | **0** | 0 |
| A2 | 700 | 624 | 9 | **633** | **0** | 67 |
| B1 | 1,000 | 907 | 9 | **916** | **0** | 84 |
| B2 | 1,300 | 1,096 | 14 | **1,110** | **0** | 190 |
| C1 | 1,500 | 913 | 9 | **922** | **0** | 578 |
| **Total** | **5,000** | **4,040** | **41** | **4,081** | **0** | **919** |

This is a provisional **unique structurally eligible first-pass written** count, not an approved vocabulary count. The 23 holds are excluded. Do not infer graded CEFR accuracy or linguistic approval from passing structural checks.

## Separate editorial, evidence, audio and device stages
1. **English definition/POS/register:** 64 first-pass drafts; **0 independent source-checked approvals**.
2. **Natural Myanmar meanings:** 64 first-pass drafts; **0 independent fluent-editor approvals**.
3. **Original usage examples:** 64 first-pass drafts; **0 independent grammar/collocation approvals**.
4. **Source-evidence and CEFR:** 64 separate review tasks remain unapproved; **3 exploratory dictionary snippets actually observed**, **0 sense-specific graded CEFR approvals**.
5. **George/Emma audio:** **0 new batch64 recordings generated, 0 real listening approvals**. Existing audio assets not changed.
6. **Browser/mobile, physical iPhone Safari, hosting limits:** no new real-device or storage/bandwidth pass claimed.
7. **Production:** no merge/deployment. Protected existing 54 lessons, IELTS 1,000 bank, George/Emma audio, and privacy assets unchanged per exact-head ALL-job diff guard.

## Commits, real CI statuses and logs
- [Initial 64-proposal staging commit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/c5a44111b08d60ba1610e8d35cafa67bbc5a9158) — draft/review packets, auditor, nondeploy workflow. Run **40367371692 failed** because a copied unique-word assertion incorrectly expected 80.
- [First correction](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/7bfc27a2d6e0988a40f51bfdfc0d32a7814e031a) — corrected 64-count and a short example. Run **40367482263 failed** because `mismanaged` was inflected while the auditor required the exact headword `mismanage`.
- [Final QA-head correction](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/ac408e79767e0c791453538bd5dfb50b47ed02e2) — rewrote the mismanage example with its exact headword.
- [Actual final workflow run 40367553099](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40367553099) at exact QA head `ac408e79767e0c791453538bd5dfb50b47ed02e2`: **completed / success**, all five matrix jobs individually inspected. Decoded logs:
  - A2 job **121729256298** — success: 16 proposed / **9 eligible** / 7 held.
  - B1 job **121729255763** — success: 16 proposed / **9 eligible** / 7 held.
  - B2 job **121729256357** — success: 16 proposed / **14 eligible** / 2 held.
  - C1 job **121729256232** — success: 16 proposed / **9 eligible** / 7 held.
  - ALL job **121729256226** — success: 64 proposed / **41 eligible** / **23 quarantined** / **14 collisions** / 0 independent approvals. Prior batch63 regression succeeded, protected-production diff guard logged `PASS: protected production assets unchanged`. Quarantine artifact **12671028117** uploaded.
- All CI passes here are **structural**, never linguistic/audio/listening/device certification. Workflow has no deploy job.

## Release blockers
**919 structurally eligible word slots remain unwritten and 0/5,000 entries have independent English/Myanmar/CEFR/example approvals.** Reassess or replace quarantined candidates only with genuine distinct words and graded sense-specific evidence. Independent fluent Myanmar/editorial review, complete George/Emma generation and real listening, browser/mobile and physical iPhone Safari QA, hosting checks and safe confirmed production deployment all remain required. No release notification or merge.
