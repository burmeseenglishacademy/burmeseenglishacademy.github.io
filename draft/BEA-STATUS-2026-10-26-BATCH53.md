# BEA CEFR 5,000 — Batch53 staging QA checkpoint (26 October 2026)

**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release:** UNVERIFIED; **DO NOT MERGE OR DEPLOY**.  
**This report distinguishes original first-pass drafts from independently checked content.**

## Substantive staging work
- Added **40 original English-definition + natural first-pass Myanmar-meaning + grammatical example DRAFTS**, separate from the canonical bank. Source pool labels all 40 as C1, but **proposed (not source-verified) teaching tiers** are A2 10, B1 12, B2 12, C1 6.
- Added **40 distinct evidence-review task packets**. Each word has separate English sense/POS, fluent Myanmar, example grammar/collocation, graded CEFR and George/Emma audio/device tasks. Dictionary links are **unvisited leads**, not observed evidence.
- Added **10 reversible candidate holds**: `shanghai`, `arkansas`, `amsterdam`, `nato`, `guinea`, `orlando`, `taiwan`, `leeds`, `lebanon`, `hampshire`. Proper names, acronym and sense ambiguity must not become filler vocabulary.
- Implemented a non-deploying five-way GitHub Actions QA workflow that checks exact counts, source-pool membership/POS, uniqueness against all prior drafts/holds including batch52, Myanmar Unicode presence, nonempty original examples, all false editorial approval flags, the empty public CEFR bank and no protected production asset drift.
- Draft examples include `fridge` (A2), `instructor` (B1), `kidney` (B2), `cannon` (C1). These **are not approved CEFR levels**. Some C1-source headwords likely belong lower; grading requires learner-dictionary evidence.

## Exact first-pass ledger, no independent sign-off

| Proposed teaching level | Academy target | Canonical first-pass before separate re-tier | Batch52 separate draft | Batch53 separate draft | Total cross-stage first-pass | Independently checked/approved | Remaining unwritten |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 | 500 | 0 | 0 |
| A2 | 700 | 534 | 12 | 10 | 556 | 0 | 144 |
| B1 | 1,000 | 778 | 12 | 12 | 802 | 0 | 198 |
| B2 | 1,300 | 931 | 12 | 12 | 955 | 0 | 345 |
| C1 | 1,500 | 735 | 4 | 6 | 745 | 0 | 755 |
| **Total** | **5,000** | **3,478** | **40** | **40** | **3,558** | **0** | **1,442** |

The canonical ledger remains **3,478** pending actual sense-specific CEFR evidence and formal incorporation of 80 separate re-tier proposals. Cross-stage first-pass totals **3,558** count those 80 *unapproved proposals* exactly once; they are **not a verified CEFR bank**. **182 historical duplicate rows** remain excluded from canonical counts. Reversible holds: **1,157 before batch53 + 10 new = 1,167**. Holds are not written drafts or approvals.

## Editorial stage accounting (batch53 only)
1. **English definition:** 40 original first-pass drafts; 0 independent sense/POS approvals.
2. **Myanmar meaning:** 40 first-pass bilingual glosses; 0 independent fluent-language approvals.
3. **Usage example:** 40 original grammatical first-pass sentences; 0 independent collocation/sense approvals.
4. **Source/CEFR evidence:** 40 separate pending packets; 0 observed dictionary pages, 0 sense-specific CEFR sign-offs. Source-pool WordNet first senses are only screening clues.
5. **George/Emma audio:** 0 newly generated or listened-to batch53 recordings; 0 pronunciation approvals.
6. **Browser/mobile/real iPhone Safari/hosting:** no new tests executed or passed this batch.
7. **Live deployment:** no merge or release. Existing 54 lessons, IELTS 1,000 bank, George/Emma production audio and privacy assets preserved.

## Actual commits, CI runs and job logs
- **Initial batch53 content/workflow commit:** `aac655a9b2bfccb2a25b779a3d703634e8905c66`.
- **Initial run:** [40280657419](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40280657419), **completed/failure**. All five jobs failed on a **real regex escaping error in the empty-bank assertion**, not a vocabulary-review failure. The ALL job's decoded log and traceback were inspected; no success was claimed.
- **Corrective commit:** `f71e49e40fbdeee0283f876ea316e56fe3bf3443` fixed the regex.
- **Latest exact-content run:** [40280680620](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40280680620), **completed/success**, SHA `f71e49e40fbdeee0283f876ea316e56fe3bf3443`. Actual job status and step summaries inspected:
  - A2 job `121433065241` completed/success.
  - B1 job `121433065057` completed/success.
  - B2 job `121433064786` completed/success.
  - C1 job `121433064898` completed/success.
  - ALL job `121433064994` completed/success.
- Decoded ALL log actually inspected: `PRIOR canonical first-pass 3478; new separate retier first-pass 40; combined unique 3518; independent approved 0; holds 1157` (batch52 regression); then `BATCH53 ALL structural pass; canonical prior=3478; separate retier=80; combined first-pass=3558; independent approvals=0; new holds=10; cumulative holds=1167`.
- The ALL job separately logged `PASS: protected production lessons, IELTS, George/Emma audio and privacy unchanged` after checking `main` against the batch53 commit.
- This documentation-only report commit is later than the exact content/QA SHA. It does not alter draft data, audit code or the workflow and is **not** represented as another CI run.

## Release blockers
**1,442 unwritten (cross-stage), 1,167 reversible holds, and 0/5,000 independent editorial approvals.** Current word-list source tiers are provisional; several frequent headwords need evidence-led re-tiering or replacement. All independently reviewed English senses, native Myanmar meanings, example/collocation checks and graded CEFR citations are outstanding. Full George/Emma pronunciation generation and actual listening, browser/mobile and physical iPhone Safari tests, hosting limits and confirmed live deployment are also outstanding.

**Do not notify completion, publish incomplete text/audio, or merge into production.**
