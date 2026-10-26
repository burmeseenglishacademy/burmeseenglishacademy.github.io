# BEA CEFR 5,000 — Batch48 staging editorial and CI checkpoint
**26 October 2026 (Singapore) — unpublished first-pass drafts, not independently verified vocabulary.**

## Work completed in this iteration
- Created **66 original bilingual draft entries** with distinct English definitions, natural first-pass Myanmar meanings and original grammatical example sentences: **A2 8, B1 18, B2 20, C1 20**.
- Created **66 separate pending evidence/review packets**. English dictionary sense/POS, native Myanmar language, grammar/collocation, sense-specific CEFR and George/Emma listening are distinct fields. No dictionary URL is represented as an observed source page.
- Added **49 reversible candidate holds**: A2 3, B1 6, B2 22, C1 18. Examples: place/person names (Washington, Rome, Singapore, Harvey), branded OS WordNet sense (windows), and misleading rare senses/POS (longer, ancient, hardware, generic, intensive, rational, provincial, cope, rebel).
- Added a full-pool unheld candidate triage script and four-way non-deploying GitHub Actions matrix. The actual triage run was **40253820372**, all A2/B1/B2/C1 jobs completed successfully and their decoded logs were inspected. Before batch48 the script found 51 A2, 61 B1, 115 B2, 456 C1 unheld candidates; most carry substantial first-WordNet-sense, proper-name or tier concerns. Heuristic risk is not linguistic approval.
- Corrected a **real CI-detected POS error**: `convert` is a noun in the candidate pool, not the verb first drafted. Replaced the misleading noun senses `cope` and `rebel` with `stance` and `namely`, and quarantined the two rejected words. Improved the `ruin` example to use natural “financial ruin”.

## Exact staging ledger (verified from ALL job log)
| Provisional level | Internal target | Unique first-pass written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 529 | 0 | 171 |
| B1 | 1,000 | 765 | 0 | 235 |
| B2 | 1,300 | 906 | 0 | 394 |
| C1 | 1,500 | 653 | 0 | 847 |
| **Total** | **5,000** | **3,353** | **0** | **1,647** |

- A2–C1 **2,853 unique written drafts**. **182 historical duplicate rows excluded** from written totals.
- **1,079 reversible held candidates**, disjoint from written entries.
- These are *provisional candidate level* counts, not official CEFR allocations or independent dictionary/sense-level approvals. In particular, several frequent B2/C1 candidates may require lower-tier reclassification; do not equate their first-pass existence with level correctness.

## Independent editorial stages
1. **English definition and sense/POS:** 66 newly written; 0 independent source-based approvals.
2. **Myanmar natural meaning:** 66 newly written; 0 independent native-speaker approvals.
3. **Original example grammar/collocation:** 66 newly written; 0 independent reviewer approvals.
4. **Independent source and graded CEFR evidence:** 66 separate pending review tasks; no dictionary pages consulted/observed as part of batch48, no source-based tier sign-offs.
5. **George/Emma audio:** no new recordings generated or listened to for batch48. Full new CEFR pronunciation generation and independent listening remain pending.
6. **Browser/mobile/physical iPhone Safari and hosting:** not newly tested for batch48; cannot be claimed passed.
7. **Production:** no merge, no new CEFR data published, no audio published. Protected production 54-lesson content, IELTS 1,000 bank, existing George/Emma audio and privacy assets unchanged according to the exact-head GitHub diff check.

## Commits and observed GitHub Actions evidence
- Remaining-candidate triage script: `9029bf1dff7ff7ede928c90c61e3e0df28fa6f71`; four-way workflow: `b44baa797ef057ffc44dce76338501ac08848467`.
- 66 draft entries: `5ba40ec52a63ef355d052986ada3e062f36cc325`.
- Separate review packets: `9386031d9b3c554bf3c3d686dc6348011e41653a`.
- Candidate holds: `2b9ff60fe827661da44bf16bbe59fef125bb18bd`.
- Batch48 structural audit: `360a931e1cebf93058e47336aa8ea501d2271c24`; five-way non-deploying workflow: `625785d605b63fcb8d2c8014a3a1e848368f8804`.
- Editorial correction commits: `82a10bab8cf70b640ddf8ffb3b0b46afbd6f30aa`, `e41ffb71852c3d726a084ff08f975190fae7109b`, `1312f6d4a514ab0d9b490a53c7da3146066d58df`; final audit correction: `b6f75d5c330e42cd1ce7d1032d3eb8388ebe4007`.
- Initial [batch48 run 40254057192](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40254057192) **failed** C1 and ALL on a real `AssertionError: convert` POS mismatch. It was fixed, not ignored.
- Final [batch48 run 40254142860](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40254142860) on exact content/QA SHA `b6f75d5c330e42cd1ce7d1032d3eb8388ebe4007`: all five jobs **completed successfully**, decoded logs actually inspected:
  - A2 `121352248420` success; B1 `121352248385` success; B2 `121352248182` success; C1 `121352248355` success; ALL `121352248358` success.
  - ALL log independently computed **A2 529 / B1 765 / B2 906 / C1 653 = 2,853 A2–C1**, plus A1 500 = **3,353 written**, **1,647 unwritten**, **1,079 held**, **182 duplicate rows excluded**, **zero independent approvals**.
  - ALL log also printed `PASS: production lesson, IELTS, George/Emma audio and privacy assets unchanged` after comparing protected assets with `main`. The public CEFR bank remains empty by structural assertion.
- The final report itself is a subsequent staging-only documentation commit; it does not change the content/QA SHA or constitute another CI run.

## Release blockers / next editorial priorities
- **1,647 unwritten**, **1,079 held**, and **0/5,000 independently approved**.
- Prioritise **A2/B1 replacement headwords with real learner-dictionary sense/CEFR evidence**: the remaining original candidate pool is heavily polluted by acronyms, names and bad WordNet senses. Do not fill quotas with these.
- Audit potentially over-tiered high-frequency B2/C1 drafts and replace/re-tier only on graded evidence. Native Myanmar, example and sense-specific CEFR review remain required for every entry.
- Full George/Emma generation, independent real listening, browser/mobile and physical iPhone Safari checks, hosting limits and live production deployment are all pending. **Never merge or notify completion until every gate is truly met.**
