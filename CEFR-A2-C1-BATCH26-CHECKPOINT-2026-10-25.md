# Burmese English Academy — Batch26 staging checkpoint (25 October 2026, Singapore)

**HOLD — UNVERIFIED DRAFTS ONLY. DO NOT MERGE, PUBLISH, CLAIM CEFR ACCURACY OR NOTIFY COMPLETION.**

## Substantive changes

1. Wrote **50 original English–Myanmar vocabulary drafts** in `draft/A2-C1-EDITORIAL-BATCH26.json`: **A2 16, B1 16, B2 15, C1 3**. Each has a selected sense/POS, original English learner definition, Myanmar meaning and original English usage example. The levels are inherited from an unverified candidate pool, NOT independently established CEFR levels. Entries are drafts, not reviewed educational content.
2. Added **50 separate independent review packets** in `draft/A2-C1-REVIEW-TASKS-BATCH26.json`. Five separate pending stages: (a) exact English sense/POS and dictionary evidence, (b) natural Myanmar translation, (c) grammatical/collocational example, (d) independently observed sense-specific CEFR source, and (e) George/Emma pronunciation generation, actual listening and physical iPhone Safari acceptance. All flags remain false, all observed evidence/reviewer fields null, and all approvals zero. Cambridge dictionary URLs are **unvisited research leads**, not source citations.
3. Quarantined **22 additional reversible candidate headwords** in `draft/A2-C1-QUARANTINE-BATCH26.json`: A2 5 (india, paul, despite, specific, chinese); B1 5 (dick, wearing, younger, domestic, launch); B2 6 (iraq, judges, syria, atlantic, mum, stops); C1 6 (thai, gentle, chuck, crush, acres, piss). Reasons include named entities, wrong WordNet POS/sense, archaic or obscure senses, plural-only headwords and register concerns. Holds are provisional editorial decisions, **not** independently source-adjudicated.
4. Added `tools/audit_cefr_batch26_review_tasks.py` and `.github/workflows/cefr-batch26-review-qa.yml`: parallel, read-only A2/B1/B2/C1/ALL structural checks. Checks enforce pool POS/level consistency (without claiming those labels are right), unique draft headwords, quarantine separation, exact pending review flags, zero source observations, unchanged empty CEFR publication data, and accurate cumulative unique counts. Workflow contains **no build, publish, deployment or audio steps**.
5. Adjusted the staging-only next-candidate preview to print 90 candidates per level. Its real job log was examined; poor WordNet clues and implausible tier assignments were rejected/held rather than copied blindly.

## Exact inventory (unique first-pass written, NOT independently approved)

| Provisional level | Target | Unique written | Independently approved | Still unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 462 | 0 | 238 |
| B1 | 1,000 | 462 | 0 | 538 |
| B2 | 1,300 | 456 | 0 | 844 |
| C1 | 1,500 | 335 | 0 | 1,165 |
| **TOTAL** | **5,000** | **2,215** | **0** | **2,785** |

A2–C1 unique written = **1,715**; A1 = **500**. **182** identical legacy duplicate A2–C1 rows are excluded from unique counts. Cumulative distinct A2–C1 quarantines = **409** (previous 387 + batch26 22). These figures were asserted in the actual ALL GitHub Actions job log. **Structural CI success is not a linguistic or CEFR approval.**

## Actual commits, GitHub Actions and logs

- Candidate preview workflow improvement: `de96af4c2651f98ba64733bce14c518cf120ed2b`.
- 50 bilingual drafts: `71a72ead2dbaf5365d1f29ae6a4b5f251a3e8e71`.
- 22 quarantines: `f3216325b8c3b49df90cb539679b69b67f0b5992`.
- 50 independent review packets: `0dfa9dbee9ea89a778056b1768ec6b840d4bf16b`.
- Fail-closed structural auditor: `ee43efac462ab50fe2199512032fdb581daba537`.
- Five-way staging workflow: `cda1d3f0d1d83b448411485ecc245b0d73865639`.
- **Candidate preview run [40156585250](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40156585250): completed/success**, real job `121059164515` log inspected.
- **Batch26 QA run [40156742506](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40156742506): completed/success** at `cda1d3f0d1d83b448411485ecc245b0d73865639`. All five actual jobs and decoded logs inspected: B2 `121059624274`, B1 `121059624408`, ALL `121059624411`, A2 `121059624423`, C1 `121059624542` — **each completed/success**.
- ALL log explicitly printed: `UNIQUE A2-C1 A2=462 B1=462 B2=456 C1=335 total=1715; independent approvals=0`; `A1=500; A1-C1 written=2215; first drafts outstanding=2785; legacy duplicate rows=182`; `STAGING ONLY batch26 ALL PASS: 50 drafts, 22 held, zero approvals; no audio/deploy`.
- Compared staging baseline `56a4917cb7952676018835843e03ae959b46bab1` to `cda1d3f0d1d83b448411485ecc245b0d73865639`: six commits, changes limited to three `draft/` JSON files, one `tools/` Python auditor and two `.github/workflows/` files. No lesson, IELTS, production audio, UI or privacy file was changed by these six commits.
- Independently read `main` at `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged from the previous checkpoint. Staging `cefr-vocabulary-data.js` still has `entries:[]`.

## Editorial risks and release blockers

- The candidate list is contaminated by wrong WordNet senses, inflected forms, proper names, everyday words labelled C1, and some unlikely A2/B2 assignments. Batch26 C1 **suite, grammar, proceed** need explicit sense-level evidence; **proceed** and **grammar** may be lower-level. A2 **justice** and B2 **odd, woods, lab** likewise require re-tiering review. This is why all 50 remain unverified.
- **No** independent dictionary-based exact-sense sign-off, Myanmar linguistic review, example sign-off, or CEFR-level confirmation was performed in this batch.
- **No** new CEFR George/Emma audio was generated or actually listened to. Existing production George/Emma assets remain untouched.
- **No** browser/mobile final corpus QA, real-device iPhone Safari check, hosting/storage/bandwidth approval, or live CEFR deployment was performed.
- **2,785** unique first-pass drafts still unwritten and **0/5,000** independently approved. Do not promote draft data or audio to the 54-lesson / IELTS-1000 live site. Completion notification remains prohibited.
