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

A new nondeploying five-job A2/B1/B2/C1/ALL workflow checks source-pool POS and source-tier, unique words, prior draft/hold collisions, original examples, separate review flags, zero approvals and production drift. It recursively runs batch51's existing structural audit. **Job success must be confirmed from actual GitHub Actions run/job status and logs; no success is asserted here.** Batch51 prior verified structural run 40266428089 completed success; that did not verify any linguistic claims.

The 40 words have **no observed learner-dictionary pages, no independent fluent Myanmar signoff, no sense-specific CEFR grading, no generated or listened-to new George/Emma audio, and no real-device Safari test**. Specialist C1 noun senses `dental` and `intensive` require special teaching-utility checks. The production 54 lessons, IELTS 1000 bank, audio and privacy remain protected, and the CEFR production data file stays empty. The 5,000 approvals, full audio generation/listening, mobile/iPhone Safari, hosting limits and confirmed live deployment are all outstanding.
