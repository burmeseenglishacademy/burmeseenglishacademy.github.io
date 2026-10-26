# Burmese English Academy CEFR 5,000 — Batch54 staging QA checkpoint

**Date:** 26 October 2026 (Singapore). **Branch:** `cefr-5000-bilingual-qa-staging`. **Release:** UNVERIFIED — DO NOT MERGE, PUBLISH OR DEPLOY.

## Substantive work actually committed

- Created **48 original bilingual first-pass drafts** from as-yet-unused source-pool C1 headwords, with **proposed teaching tiers A2 12, B1 16, B2 18, C1 2**. Original source-pool tier C1 is **not** sense-specific graded CEFR evidence. These 48 are separate re-tier proposals, not canonical approvals.
- Each word has its own original English definition, natural first-pass Myanmar meaning and contextual grammatical example, and **a separate five-stage evidence task packet**. All English sense/POS, Myanmar naturalness, example grammar/collocation, CEFR and George/Emma listening flags remain **false**; dictionary URLs are **unvisited lookup leads**, not observed evidence.
- Added **13 reversible holds** (short ambiguous abbreviations and proper names, plus `lighter` for WordNet-first-sense conflict). A first-pass `lighter` device meaning was removed when the candidate-pool WordNet clue pointed to a lighting *substance*; `disk` with matching noun clue replaced it without increasing the draft count. Holds are never counted as drafted or approved.
- Repaired remaining-candidate triage so it subtracts batch52/batch53 (and subsequent) separate re-tier drafts/holds rather than offering already-used candidates again.
- Added five-way non-deploying **A2 / B1 / B2 / C1 / ALL** GitHub Actions checks for exact draft/hold counts, source-pool POS, cross-batch collisions, Unicode Myanmar, original example shape, unapproved source flags, empty public CEFR bank and protected production-asset drift. ALL runs the earlier regression chain.

## Exact per-level ledger — FIRST PASS, not independently verified

| Proposed teaching tier | Target | Canonical first-pass through batch51 | Separate re-tier batches52–53 | New batch54 | Cross-stage unique written | Independently checked/approved | Unwritten |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 | **500** | **0** | 0 |
| A2 | 700 | 534 | 22 | 12 | **568** | **0** | 132 |
| B1 | 1,000 | 778 | 24 | 16 | **818** | **0** | 182 |
| B2 | 1,300 | 931 | 24 | 18 | **973** | **0** | 327 |
| C1 | 1,500 | 735 | 10 | 2 | **747** | **0** | 753 |
| **Total** | **5,000** | **3,478** | **80** | **48** | **3,606** | **0** | **1,394** |

**Accounting:** 3,478 canonical first-pass + 128 separately stored, unique unapproved re-tier proposals = 3,606 first-pass written. Canonical ledger remains 3,478 until editorial evidence permits formal incorporation. Historical duplicate rows excluded: 182. Reversible holds: 1,167 before batch54 + 13 = **1,180**. Holds and duplicates do not count as written. **Independent English sense approvals 0, independent Myanmar approvals 0, independent example approvals 0, sense-specific CEFR approvals 0, George/Emma listening approvals 0.**

### Source-candidate bottleneck

The corrected live CI triage on commit `17105bf092ca3a8c553740f61e2d1252b558db0c` logged **3,058 A2–C1 drafted**, **1,167 held**, and remaining unheld by *original source tier*: A2 **22**, B1 **13**, B2 **27**, C1 **213**. Most remaining A2/B1/B2 source entries are abbreviations, possessive forms or suspect WordNet senses, **not 62 safe ready-to-write entries**. Batch54 used 48 C1-source entries and held 13 C1-source entries, so the inferred remaining unheld source pool is A2 22 / B1 13 / B2 27 / C1 152 = **214**. This is candidate availability, not learner-dictionary validation. A new, clean, independently graded candidate source is needed to fill the remaining 1,394 without quota filler.

## Actual commits, workflow runs and logs

- Candidate triage fix: `17105bf092ca3a8c553740f61e2d1252b558db0c`. Four parallel triage jobs in run [40284981335](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40284981335) **completed/success**; real C1 and B1 logs were inspected to select eligible headwords and identify suspicious senses.
- Initial batch54 atomic content/workflow commit: `5d7a2c72f2529ecbe275e6014a34e5e1dc69d522`. Initial run [40285253431](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40285253431) **completed/failure** because the new audit retained the old 40-example assertion despite 48 drafts.
- QA count fix: `0d4c3c58a5dd94da328cc4a45226615b88a3ac11`; recursive regression fix: `4a25343522f78a84c1fb6e53698330983021116e`. Intermediate runs **40285287813** and **40285297894** **completed/failure**: a real `lamb` definition was shorter than the audit's minimum 25-character informative-definition rule.
- Definition improvement: `0daa7c841c945d3ed4b3ae85a5fb630c09dbc02d`; run [40285329901](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40285329901) **completed/success**, five jobs.
- WordNet sense-conflict quarantine and `disk` replacement: final content/QA commit **`e7543b5821a8dc1e1c6ddce7eed85998c03f27f4`**.
- **Latest exact-content run [40285412642](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40285412642): completed/success at `e7543b5821a8dc1e1c6ddce7eed85998c03f27f4`. Actual jobs: C1 `121447788546`, B2 `121447788770`, A2 `121447788817`, B1 `121447788870`, ALL `121447788872` — all **completed/success**.
- The decoded ALL job log was inspected and explicitly said: `BATCH54 ALL structural pass; canonical prior=3478; separate retier=128; combined first-pass=3606; independent approvals=0; new holds=13; cumulative holds=1180`. The separate production drift step logged `PASS: protected production lessons, IELTS, George/Emma audio and privacy unchanged`.
- **Scope of CI:** machine-checked structure, collisions, regression and protected-file diff only. Successful jobs **do not** independently certify any English meaning, Burmese translation, CEFR level, example quality, audio or browser compatibility. This documentation-only commit follows the tested content SHA and is not represented as another CI execution.

## Unresolved release gates — no completion notification

**1,394 unwritten first-pass entries, 1,180 held candidates and 0/5,000 independently approved entries.** Graded learner-dictionary sense/POS/CEFR evidence, fluent Myanmar sign-off and sentence/collocation review remain pending. All new George/Emma audio generation and real listening validation remain pending; no batch54 audio was produced or listened to. Browser/mobile, **physical iPhone Safari**, hosting storage/bandwidth and final live deployment are **not passed**. Production 54 lessons, IELTS 1,000 bank, George/Emma audio and privacy assets were left unchanged. Public CEFR data remains empty. **Do not merge or publish unverified data; do not claim 100% completion.**
