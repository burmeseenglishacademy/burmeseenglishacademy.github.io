# CEFR 1,000 A2 fifth twelve: directly observed Oxford word/POS research — 2026-10-29

**STAGING ONLY / NO INDEPENDENT APPROVAL / NO DEPLOYMENT.** Branch: `cefr-5000-bilingual-qa-staging`. The authorised target is exactly 200 each at A1/A2/B1/B2/C1, not the superseded 5,000-word proposal. Frozen first-pass bilingual shortlist and independent-review tasks are unchanged.

## Direct publisher research
Official Oxford University Press [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) inspected on **2026-10-29**. PDF page locators below are one-based; text extraction line locators are zero-based. These are word/part-of-speech **labels only**, not publisher endorsement of the precise teaching sense or the English/Myanmar/example accuracy.

| A2 draft headword | Oxford word/POS level | PDF page | Extracted line | Verbatim short source entry | Review issue |
|---|---|---:|---:|---|---|
| history | A1 | 2 | 369 | `history n.` | HISTORY_A1_VS_A2_AND_PAST_EVENTS_VS_ACADEMIC_SUBJECT |
| university | A1 | 4 | 837 | `university n.` | UNIVERSITY_A1_VS_A2_AND_BRITISH_AT_UNIVERSITY |
| air | A1 | 1 | 23 | `air n.` | AIR_A1_VS_A2_ATMOSPHERE_VS_MANNER |
| probably | A1 | 3 | 622 | `probably adv.` | PROBABLY_A1_VS_A2_LIKELIHOOD_NOT_CERTAINTY |
| future | A1 | 2 | 322 | `future n.` | FUTURE_A1_VS_A2_NOUN_NOT_ADJECTIVE |
| police | A1 | 3 | 606 | `police n.` | POLICE_A1_VS_A2_COLLECTIVE_PLURAL_NOUN |
| reason | A1 | 3 | 643 | `reason n.` | REASON_A1_VS_A2_CAUSE_VS_EXPLANATION |
| within | B1 | 10 | 2579 | `within prep.` | WITHIN_B1_VS_A2_TIME_LIMIT_AND_SPACE |
| able | A2 | 4 | 910 | `able adj.` | ABLE_A2_MATCH_BE_ABLE_TO_CONSTRUCTION |
| single | A2 | 6 | 1618 | `single adj., n.` | SINGLE_A2_MATCH_ROOM_AMBIGUITY_AND_UNMARRIED_SENSE |
| large | A1 | 2 | 425 | `large adj.` | LARGE_A1_VS_A2_SIZE_AND_QUANTITY |
| possible | A1 | 3 | 611 | `possible adj.` | POSSIBLE_A1_VS_A2_FEASIBILITY_AND_PROBABILITY |

Nine have a **lower Oxford A1** word/POS label; `able` and `single` match A2; `within` has a **higher Oxford B1** label. The `police` shortlist's grammatical label *plural noun* versus Oxford's generic `n.` must not be treated as a substantive contradiction without checking collective/plural grammar. `single room` is potentially ambiguous (room for one guest vs one room); `within two days` expresses a deadline and must not be translated as exactly two days later. `probably` needs natural probability language in Myanmar. These are **unapplied editorial flags**, not corrections or approvals.

Each of 12 research records preserves the frozen original English definition, Myanmar meaning, example, historical source file/index/Git blob SHA, official PDF URL, observation date, page/line/excerpt, risk, and independent reviewer task. No historical WordNet/named-entity inference has been upgraded into independent CEFR evidence.

## Count checkpoint
- Written first-pass: **A1 200, A2 200, B1 200, B2 200, C1 200**. Independently approved: **0 in every level**.
- Distinct directly observed Oxford word/POS headwords: **A1 112, A2 72, B1 72, B2 70, C1 51 = 377/1,000**. No direct observation in audited packets: **623**.
- Review handoff classification: **146 publisher-lower, 11 publisher-higher, 3 unlisted (not a CEFR level), 217 matching word/POS but exact sense unverified, 623 no direct observations**.
- Source observation records: **396**, of which **377** are distinct, so repeated observations are not counted as new coverage. Historical excerpt recovery remains **36**.
- British George/Emma final headword+example real listening signoffs: **0/1,000**. Human-independent English/Myanmar/example/exact-sense CEFR signoffs, approved-corpus browser/mobile regression, real physical iPhone Safari evidence, measured GitHub Pages hosting limits and confirmed production deployment remain missing.
- Release status: **BLOCKED / STAGING ONLY**. Protected 54 lessons, separate IELTS 1,000 bank, established George/Emma production audio and privacy paths must remain unchanged.

## CI audit scope
The new source-integrity auditor pins all 12 publisher excerpts and source locations, original bilingual snapshots and historical provenance; its negative tests must reject 306 forged record/metadata variants. Six parallel CEFR-level structural jobs and the documentary no-deployment gate include this audit. Actual run IDs and job/log conclusions must be added only after they have been inspected. CI success is structural, never independent linguistic review or release permission.

## Verified CI and production protection
Verified at 2026-10-29 08:04 UTC on code commit `be36f975ba6fec218b66395bcf00cab397ecfa55`:
- [Parallel structural run 40839481745](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40839481745): **SUCCESS**, all six A1/A2/B1/B2/C1/ALL jobs completed successfully. ALL-job logs confirmed **306/306** new forged A2 publisher/bilingual/provenance/review mutations rejected, **145/145** handoff mutations rejected, 377 distinct source observations, 623 without observations, and zero approvals. Protected production paths unchanged.
- [Documentary no-deployment run 40839481736](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40839481736): **SUCCESS as report-only**. Actual job logs confirm release remains blocked for absent human approvals, final listening, physical iPhone, mobile/browser and hosting/deployment evidence; protected production paths unchanged. CI success does **not** grant launch readiness.
- Initial run IDs 40839464648 and 40839464607 failed due to an incorrectly escaped Git-blob NUL byte in the new auditor. Fixed at `be36f975ba6fec218b66395bcf00cab397ecfa55`, then both workflows were rerun successfully by branch push. No main modification, merge or publication.
