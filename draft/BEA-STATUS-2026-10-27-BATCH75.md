# BEA CEFR 5,000 — Batch75 staging evidence report
**27 October 2026, Singapore. STAGING ONLY. NOT INDEPENDENTLY APPROVED, MERGED, DEPLOYED OR RELEASED.**

## Substantive new bilingual drafting
- Wrote **72 original first-pass bilingual entries**: **A2 15, B1 17, B2 20, C1 20**. Each has an original English definition, Myanmar meaning and grammatical intended-sense English example, plus a proposed part of speech. These are original *drafts*, not independently verified text.
- Created **72 separate independent-review task records** for dictionary sense and POS, fluent Myanmar sense, example grammar and collocation, independent sense-specific CEFR evidence, and George/Emma pronunciation and listening. No task is marked completed, and no source URL or review evidence is fabricated.
- Created **72 reversible editorial quarantine records**, plus **34 targeted risk flags** for technical/legal meanings, polysemy, formal register, spelling variants, and potentially unsuitable level placement. All 72 are held and excluded from eligible/approved counts.
- Selected only candidate-level pairs marked **CLEAR_ONLY_NOT_APPROVED** in actual successful Batch74 candidate preflight [40440285272](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40440285272), which mechanically screened 549 rows (261 clear-only, 288 flagged). Excluded all 60 Batch74 drafted headwords and nine candidate cross-level conflicts. The Batch75 structural audit additionally checked the earlier authored corpus and unverified seed-tier/sense clues. Mechanical screening is not source-backed CEFR approval.

## Observed GitHub Actions QA, including repaired warning
- First Batch75 workflow [40444318389](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40444318389) **completed successfully in all five A2/B1/B2/C1/ALL jobs**, but ALL-job log **121991826626** warned that the expected JSON report artifact was absent. This was a **report filename bug** (the auditor wrote the prior batch's filename), not a linguistic issue. The warning is preserved in this report.
- Fixed the artifact filename and reran through a staging commit. Final workflow [40444361749](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40444361749) **completed successfully in all five A2/B1/B2/C1/ALL jobs**. Actual ALL-job log **121991965521**: `BATCH75 ALL checked 72 risk flags 34 problems []`; `PASS: STRUCTURAL ONLY. Zero independent approvals. No audio, merge or publication.`; `PASS: protected production assets unchanged`. The JSON hold report was actually uploaded: [artifact 12707751648](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40444361749/artifacts/12707751648).
- The structural audit checks non-empty text, original examples containing the target word, per-level totals, review and quarantine parity, absence of previous authored collisions, candidate-preflight status, flagged WordNet/seed clues, historical cross-level holds, and an empty CEFR publication placeholder. These are **structural** checks; they do not establish natural Myanmar usage or verified CEFR classification.
- Workflow has **no deployment step**. The ALL job compared protected production assets with `main` and passed; existing 54 lessons, IELTS 1,000-word bank, George/Emma production audio/player and privacy assets were not edited.

## Exact eligible-written and independently checked ledger
| Level | Target | Structurally eligible first-pass written | Independently checked and approved | New Batch75 held drafts |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 654 | 0 | 15 |
| B1 | 1,000 | 947 | 0 | 17 |
| B2 | 1,300 | 1,133 | 0 | 20 |
| C1 | 1,500 | 956 | 0 | 20 |
| **Total** | **5,000** | **4,190** | **0** | **72** |

**810 structurally eligible slots remain.** The historical derived distinct authored staging inventory is now **4,790 wordforms** (4,718 before Batch75 + 72 checked noncolliding first-pass drafts), including unapproved material. This is not a count of approved entries. Proposed distinct authored counts, including held entries: A1 500, A2 789, B1 1,076, B2 1,272, C1 1,177. Historical **24 cross-level wordforms** remain quarantined; nine additional Batch74 candidate-only conflicts remain held separately. Historical duplicate occurrences require reconciliation.

## Staging commit trail
- 72 bilingual draft entries: `ea2a40aa7fe735987601918c27eeb94f0ab1387c`
- 72 independent-review task records: `d5e6bb8d53f5b222458b2083525e9304a895c8a3`
- 72 reversible quarantine records: `c001e3593a1c1fe5934c627e01484a9a77f723a7`
- Five-level structural auditor: `a87ce7a4a0ce4d6bfd191129e459addc162562c4`
- Parallel nondeploying workflow: `8ee0c3c653f3c22d8610bb3a3d34f15a2d15c7e5`
- Corrected audit artifact filename: `d6d1e8e005db7b98d9cc76a4671c6760c182c6df`

## Outstanding editorial and release blockers
**Zero entries have independent English dictionary, fluent Myanmar, grammatical example, and sense-specific CEFR approval.** No new George/Emma recordings were generated or actually listened to. Browser/mobile and physical iPhone Safari validation, full audio coverage, hosting quota verification, and production deployment are not complete. All new drafts remain unpublished and under reversible hold. Do not merge or release until the full 5,000-word bilingual, CEFR, audio, real-device and hosting gates have evidence and pass.
