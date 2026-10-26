# BEA CEFR 5,000 — Batch61 verified staging checkpoint
**26 October 2026, 22:49 SGT. STAGING ONLY. NOT RELEASE-APPROVED. DO NOT MERGE OR PUBLISH.**

## Work actually completed in this iteration
- **80 original bilingual first-pass proposals**: A2 **18**, B1 **20**, B2 **22**, C1 **20**. Each has a separate English definition, Myanmar meaning, part of speech and original grammatical example. These are **unverified editorial drafts**, not approved teaching content.
- **80 independent review task packets** were prepared. English exact sense/POS/register, Myanmar naturalness, grammatical example/collocation, graded CEFR sense evidence, and George/Emma listening/device review remain **separate incomplete stages**. Source URLs in packets are suggested reference pages, **not consulted or independently checked sources**.
- **11 explicit reversible editorial holds** for uncertain CEFR tier or specialist register, plus automated duplicate cross-corpus quarantine. No WordNet senses or named entities were promoted from unreviewed data. All newly written records retain approval flags **false**.
- Structural CI identified **43 new unique nonheld first-pass records** and **37 quarantined proposals**. Of the 37 held, **31** collide with the original 5,000 candidate pool or prior drafts, **11** have explicit tier/register holds, and **5** have both reasons (37 unique holds). Quarantine is reversible after source-based review; none of the held records is counted as eligible.

## Exact level ledger (structural first-pass eligibility, NOT linguistic approval)
| Level | Target | Before batch61 eligible | Batch61 raw proposals | Batch61 new eligible | Current written eligible | Independently approved | Remaining unwritten |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 | **500** | **0** | 0 |
| A2 | 700 | 590 | 18 | 10 | **600** | **0** | 100 |
| B1 | 1,000 | 859 | 20 | 16 | **875** | **0** | 125 |
| B2 | 1,300 | 1,044 | 22 | 11 | **1,055** | **0** | 245 |
| C1 | 1,500 | 877 | 20 | 6 | **883** | **0** | 617 |
| **Total** | **5,000** | **3,870** | **80** | **43** | **3,913** | **0** | **1,087** |

**Stage accounting for batch61:** English definitions 80 first-pass / 0 independently checked; Myanmar meanings 80 first-pass / 0 independently checked; original examples 80 first-pass / 0 independently checked; provisional CEFR labels 80 / 0 independently source-approved; separate source review tasks 80 / 0 actual dictionary pages consulted / 0 independently completed; new CEFR George/Emma audio generated **0**, real listening **0**, real-device Safari checks **0**. Cross-corpus duplicates and held entries are excluded from eligible written counts.

## Actual GitHub commits and real CI evidence
- **Staging commit** `0cfcbb54b318c50af25e14ce433e4a591c96693d`: 80 bilingual proposals, 80 review packets, new batch61 structural audit, five-way parallel nondeploy workflow and initial report.
- **Audit fix** `21953e9b17f9a9199639d1e71cc69e0debfb5be8`: corrected public-bank empty-array regex and newline handling in the batch61 script.
- First workflow run [40343086767](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40343086767) **completed / failed** on an overescaped audit regex, not on linguistic content; failure retained in history.
- Corrected workflow run [40343129353](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40343129353), head `21953e9b17f9a9199639d1e71cc69e0debfb5be8`, **completed / success** at 14:48:57 UTC on 26 October 2026.
- Five individually inspected job outcomes: A2 **121642852289 success**, B1 **121642851990 success**, B2 **121642852257 success**, C1 **121642852002 success**, ALL **121642851631 success**.
- Decoded ALL log: **80 proposals, 43 eligible, 37 held, 31 duplicate collisions, 11 explicit holds, 0 source pages observed, 0 independently approved**. The ALL job also ran batch60 regression successfully and printed **PASS: protected production assets unchanged**. Reversible quarantine artifact **12659601762** uploaded.
- This workflow has **no deployment job**. The protected production **54 lessons, IELTS 1,000 vocabulary bank, existing George/Emma audio, and privacy scripts** were not changed. GitHub Pages settings, hosting limits, mobile browser functionality and physical iPhone Safari were not independently tested in this run.

## Release blockers and next work
**1,087 first-pass eligible curriculum slots remain unwritten**, and **all 5,000 require independent English/Myanmar/example/sense-specific CEFR approvals**. All new CEFR George/Emma audio generation and real listening checks remain outstanding, as do physical iPhone Safari, mobile/browser regression, hosting/bandwidth verification and confirmed live deployment. Quarantined headwords require graded source-based sense review, not automatic retiering. Never interpret green structural CI as dictionary, Myanmar, CEFR or pronunciation approval. Keep all unverified drafts isolated from the public CEFR bank.
