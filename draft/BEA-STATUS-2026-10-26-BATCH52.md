# BEA batch52 — staging-only 40 bilingual re-tier drafts (2026-10-26)

**Branch:** `cefr-5000-bilingual-qa-staging`. **UNVERIFIED; DO NOT MERGE/DEPLOY.**

## Actual work and boundaries

40 original first-pass English definitions, Myanmar meanings and grammatical usage examples have been written in a **separate re-tier proposal file**. Their original candidate-pool CEFR label is **C1 for all 40**; proposed teaching levels are **A2 12, B1 12, B2 12, C1 4**. These are NOT evidence-based CEFR assignments and are NOT automatically added to the canonical 5,000-bank ledger. Each has a separate evidence packet with unvisited dictionary leads and pending independent English, Myanmar, example, level and George/Emma listening/device tasks. Fourteen additional candidate words are reversibly quarantined for named-entity, abbreviation, register and misleading WordNet-sense issues. No holds count as drafts.

## Exact first-pass inventory (zero independent approvals)

| Level | Previous canonical first-pass | New provisional re-tier first-pass | Combined cross-stage first-pass | Independently checked/approved |
|---|---:|---:|---:|---:|
| A1 | 500 | 0 | 500 | 0 |
| A2 | 534 | 12 | 546 | 0 |
| B1 | 778 | 12 | 790 | 0 |
| B2 | 931 | 12 | 943 | 0 |
| C1 | 735 | 4 | 739 | 0 |
| **Total** | **3,478** | **40** | **3,518** | **0** |

**Caution:** Cross-stage totals use proposed teaching tiers, not the original pool's C1 classification. The **canonical** ledger is still 3,478 unique first-pass, 1,522 unwritten, zero approved until independent evidence permits re-tiering. 182 historical duplicate rows are excluded. Existing 1,143 holds plus 14 new = 1,157 distinct reversible holds **subject to CI collision check**.

## QA and release blockers

Initial workflow run 40276058485 failed all five jobs on a real prior-draft/hold collision, not a linguistic failure. Diagnostic run 40276101988 identified ten colliding words (nine previously drafted and one previously held); these have been replaced with ten fresh candidate drafts without changing the 40-entry count. A new CI run must verify the corrected set. Do not describe either failed run as passed.


The nondeploying five-job A2/B1/B2/C1/ALL workflow checks source-pool POS and source-tier, unique words, prior draft/hold collisions, original examples, separate review flags, zero approvals and production drift. It recursively runs batch51's existing structural audit. **Job success must be confirmed from actual GitHub Actions run/job status and logs; no success is asserted here.** Batch51 prior verified structural run 40266428089 completed success; that did not verify any linguistic claims.

The 40 words have **no observed learner-dictionary pages, no independent fluent Myanmar signoff, no sense-specific CEFR grading, no generated or listened-to new George/Emma audio, and no real-device Safari test**. Specialist C1 noun senses `dental`, `hull` and `spectacular` require special teaching-utility checks. The production 54 lessons, IELTS 1000 bank, audio and privacy remain protected, and the CEFR production data file stays empty. The 5,000 approvals, full audio generation/listening, mobile/iPhone Safari, hosting limits and confirmed live deployment are all outstanding.

## Verified GitHub Actions execution (actual run/job/log inspection)

- Initial batch52 content/QA commit `7ea5e91535325f6a13641f60b59a34bad561dce0`; run **40276058485**, **completed/failure** in all five jobs. Actual ALL log showed a collision with earlier drafts/holds. Diagnostic commit `8c6b1aabf40c4635afd29bdc860590d330057406`; run **40276101988**, **completed/failure**, identified ten exact collisions. They were replaced without inflating the 40-entry count.
- Replacement commit `3587a71d117ae7e465cea3661c19376ff73c3dc8`; run **40276195814**, **completed/success** in five jobs. A further original-example collocation improvement to `spectacular` was committed as `9cd69e8f633dc5ada5566ae96ec57a5c19512e0d`.
- **Latest actual run [40276264636](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40276264636)** at exact draft SHA `9cd69e8f633dc5ada5566ae96ec57a5c19512e0d`: **completed/success**. Jobs **A2 121419556094**, **B1 121419556147**, **B2 121419556113**, **C1 121419555979**, **ALL 121419556111** all **completed/success**.
- Inspected decoded ALL job log: `PRIOR canonical first-pass 3478; new separate retier first-pass 40; combined unique 3518; independent approved 0; holds 1157`; `STAGING batch52 ALL STRUCTURAL PASS; proposed 40; 14 holds; NO CEFR/audio approval`; `PASS: production lessons, IELTS 1000, George/Emma audio and privacy assets unchanged`.
- **Scope:** structural checks only. No independent bilingual, graded CEFR, real audio listening, physical iPhone Safari, hosting or production-release validation was performed or passed.
