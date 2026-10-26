# BEA CEFR 5,000 — Batch66 staging editorial and CI checkpoint
**27 October 2026, approximately 03:31 Singapore time. STAGING ONLY. NOT APPROVED. DO NOT MERGE OR DEPLOY.**

## Substantive draft output and quarantines
- Authored **80 original bilingual first-pass vocabulary proposals**: A2 **20**, B1 **20**, B2 **20**, C1 **20**. Each has a distinct English sense definition/POS, Myanmar first-pass meaning and original grammatical example. These are **unverified** drafts, not approved learning entries.
- Authored **80 separate independent review packets**. The stages for dictionary-based English sense/register, fluent Myanmar meaning, grammar/collocation, graded sense-specific CEFR, and George/Emma audio/listening/real-device checks are separately tracked and all remain pending.
- Proactively held **30** proposals for questionable tier, spelling/regional usage, register, specialist senses or rare terms. The cross-corpus auditor detected **43 duplicate wordforms** against the original candidate pool or prior draft batches. Overlapping reasons are possible. In total **56 reversibly quarantined** and **24 unique structurally eligible but linguistically unapproved** proposals remained.
- Structural eligibility by level: A2 **1/20** (19 held); B1 **9/20** (11 held); B2 **4/20** (16 held); C1 **10/20** (10 held). The high A2 collision rate is a genuine limitation; do not inflate the count by treating repeated candidates as new words.
- No WordNet definition or synset was imported into these authored records. Named entities and unreviewed WordNet sense fields are guarded by the auditor, but structural checks are not proof of lexicographic accuracy.

## Exact provisional written ledger (eligible unique first-pass, not approved)
| Level | Target | Prior eligible written | New eligible written | Current eligible written | Independently approved | Still unwritten |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | **500** | **0** | 0 |
| A2 | 700 | 645 | 1 | **646** | **0** | 54 |
| B1 | 1,000 | 929 | 9 | **938** | **0** | 62 |
| B2 | 1,300 | 1,121 | 4 | **1,125** | **0** | 175 |
| C1 | 1,500 | 933 | 10 | **943** | **0** | 557 |
| **Total** | **5,000** | **4,128** | **24** | **4,152** | **0** | **848** |

The cumulative counts above follow the batch65 recorded ledger plus actual batch66 cross-corpus CI results. They count unique structurally eligible *drafts*, not independently checked/approved words. Quarantined words are excluded.

## Independent editorial and release stages (truthful status)
1. **English definitions and POS/register:** 80 first-pass proposals; **0 independently verified** in this batch.
2. **Myanmar meaning:** 80 first-pass proposals; **0 independent fluent-editor sign-offs**.
3. **Original example grammar/collocation:** 80 first-pass sentences; **0 independent linguistic sign-offs**.
4. **Dictionary and graded CEFR source evidence:** 80 pending review packets with URLs to consult; **0 actually observed graded CEFR source approvals**. Merely listing a dictionary URL does not count as checking it.
5. **Audio:** **0 new George/Emma recordings** generated for batch66; **0 real listening validations**.
6. **Browser/mobile, real-device iPhone Safari and hosting:** no new physical-device or hosting/bandwidth pass performed in this batch.
7. **Release:** no production merge or deployment; no completion notification.

## Actual commits, parallel GitHub Actions statuses and log evidence
- [Draft commit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/750c8db6c5c3a65e9c25044584565860b123c902) — 80 bilingual entries.
- [Separate review-packet commit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/9b6517ac90d422e6d8688330ee71b55fee99cc9a) — 80 review tasks.
- [Structural auditor commit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/99d6b5dd2e7f3d5f6350bf7af7e3516f02c8e17f) — per-level and cross-corpus triage, batch65 regression and unapproved bank guard.
- [Parallel nondeploy workflow commit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/8ce4e662e59979546205c939d73b9a9ac0529718) — five matrix jobs; no deploy job.
- [Actual workflow run **40387411912**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40387411912) on exact QA head **8ce4e662e59979546205c939d73b9a9ac0529718**: **completed / success**, all five job statuses individually inspected and decoded logs read:
  - A2 job **121799240851**: completed/success; `BATCH66 A2 proposals 20 eligible 1 held 19`.
  - B1 job **121799240863**: completed/success; `BATCH66 B1 proposals 20 eligible 9 held 11`.
  - B2 job **121799240331**: completed/success; `BATCH66 B2 proposals 20 eligible 4 held 16`.
  - C1 job **121799240820**: completed/success; `BATCH66 C1 proposals 20 eligible 10 held 10`.
  - ALL job **121799240937**: completed/success; `80 proposals / 24 eligible / 56 quarantined / 43 duplicate collisions / 0 independently approved`. Prior batch65 structural regression succeeded. Exact-head production guard logged `PASS: protected production assets unchanged`.
- Real GitHub Actions quarantine artifact **12681926744**, `batch66-reversible-quarantine`, uploaded and observed (retention 30 days). **These are structural QA successes only**, not independent linguistic/audio/device validation.
- This status report is added after the exact QA head; it changes documentation only, not vocabulary/audio/production content.

## Next meaningful work and release blockers
**848 unique eligible written slots remain**, with **0/5,000 independently approved**. The original 5,000-word candidate pool and prior 66 batches now cause many wordform collisions, particularly at A2. Future batches should pre-screen candidate uniqueness before drafting, use graded sense-specific CEFR evidence, and prioritise resolving existing reversible holds rather than inventing rare words solely to increase counts. Independent Myanmar/editorial review, full George/Emma audio generation plus real listening, browser/mobile and physical iPhone Safari testing, hosting/storage/bandwidth checks, and confirmed live deployment are still blocking release. **Do not merge, publish or send a completion notification.**
