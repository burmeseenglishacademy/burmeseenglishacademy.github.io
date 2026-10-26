# BEA CEFR 5,000 — Batch60 staging editorial and CI report
**26 October 2026, approximately 21:06 SGT. STAGING ONLY. NOT RELEASE-APPROVED. DO NOT MERGE OR PUBLISH.**

## Original work and evidence stages
- **54 new original bilingual first-pass proposals**: A2 **5**, B1 **9**, B2 **14**, C1 **26**. Each contains a separate English sense definition, Myanmar meaning, part of speech and an original grammatical usage example. These are **drafts**, not validated CEFR placements or translations.
- **54 separate independent review task packets** require exact dictionary sense/POS/register, fluent Myanmar editorial review, original example grammar/collocation, sense-specific graded CEFR source evidence and later George/Emma real listening and physical iPhone Safari testing. Every independent approval flag remains **false**.
- **3 actually consulted Cambridge Dictionary pages** are logged separately in `draft/A2-C1-SOURCE-OBSERVATIONS-BATCH60.json`: `footpath` (noun; mainly UK), `reprimand` (verb; formal), and `recalibrate` (verb with separate instrument-calibration and strategy-adjustment senses). These are source **observations**, not independent linguistic approval. No graded CEFR evidence or Myanmar reviewer evidence was observed.
- The `recalibrate` draft incorrectly combines two distinguishable dictionary senses and was put on **reversible editorial hold** pending a sense split or editorial decision. The `footpath` and `reprimand` drafts have register notes for further review. The source observations are paraphrases, not copied dictionary definitions.
- Additional explicit reversible holds: **6** C1/C2 tier-uncertain proposals. Cross-corpus audit found **15** duplicate headword collisions against the original candidate pool and historical A1/A2–C1 drafts. Some of these reasons overlap; **18 distinct records are held**. No named-entity or WordNet-derived senses were promoted; the structural script guards against obvious named-entity and unreviewed WordNet provenance but is not a semantic review.

## Exact first-pass curriculum ledger — independently approved still zero
| Level | Target | Before batch60 | New unique nonheld first-pass | Current written first-pass | Independently approved | Unwritten |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | **500** | **0** | 0 |
| A2 | 700 | 585 | 5 | **590** | **0** | 110 |
| B1 | 1,000 | 850 | 9 | **859** | **0** | 141 |
| B2 | 1,300 | 1,034 | 10 | **1,044** | **0** | 256 |
| C1 | 1,500 | 865 | 12 | **877** | **0** | 623 |
| **TOTAL** | **5,000** | **3,834** | **36** | **3,870** | **0** | **1,130** |

**Stage accounting:** 54 English definitions written / 0 independently approved; 54 Myanmar meanings written / 0 independently approved; 54 original example sentences written / 0 independently approved; 54 review task packets / 3 dictionary pages observed / 0 completed independent source-based reviews; 54 provisional CEFR labels / 0 sense-specific graded CEFR approvals; 0 new CEFR George/Emma audio generated / 0 real listening checks / 0 physical iPhone Safari checks. The 18 held records are retained as drafts but excluded from the written-eligible ledger.

## Real commits, CI and blockers
- First-pass editorial draft `c446bbb92e7fc2f1458a679a551e2bf53ec58d2c`; review tasks `9b3208b4c835588e0fcdf5e7f980bbe6d237557c`.
- Initial five-way structural QA script `698cf83996cec43463c9c041e4edddfc2d39e7e3`; nondeploy workflow `40bc3316dd6962c155c3c9b271da24419d2a8f95`. Regex/newline fix `8401d516f5a3d4fcd9a8f20d86d617e156c11926`; expanded A1 and named-entity/WordNet provenance gate `ff0c6e6b0ff2de049c1773bdbf7a29eb68526b85`.
- Historical batch59 audit forward-compatibility corrected in `745be634b246d567852ba334d52417cba32d1021` and `2f3f78f1f84d9b90918c4a93eb6fe64fb2c1a5fe` so newer source-recovery batches do not retroactively invalidate old counts.
- Source observation file `7e9a3a8e907372bdca9fab5e8d12ed0ba973d32e`; explicit sense hold `a8af5ed0d2b7f76ba1789066ce34a4964345c954`; updated review tasks `62fd8026d9855908d1bc9d96e4dcf96fd2047e68`; observation gate `672901e4540d82e18f6138113ab544dd2f4a5609`; workflow source trigger `b953986a69e5157b6aba06e24825b75532dfa421`; observation shape correction `a6a0fed0ee00fff9266fe790ffb3eba8a9508d94`.
- Earlier workflow runs [40327117840](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40327117840), [40327162319](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40327162319), [40327589319](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40327589319) and intermediate source-observation runs **failed** on specific audit implementation or observation-shape assertions. These were corrected; they are not presented as passes.
- **Final checked run [40327623445](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40327623445), head `a6a0fed0ee00fff9266fe790ffb3eba8a9508d94`: completed / success**, five observed independent matrix jobs: B2 `121588317863`, A2 `121588318223`, C1 `121588318322`, ALL `121588318584`, B1 `121588318603`.
- Decoded ALL job log reports **54 proposals / 36 eligible unapproved / 18 reversibly held / 15 duplicate collisions / 6 tier-risk holds / 3 actual dictionary pages observed / 0 independently approved**. Counts reflect overlaps between hold reasons. Earlier batch59 regression passed. The protected production asset diff guard printed **PASS: protected production assets unchanged**. Quarantine artifact **12652365638** was uploaded.
- Workflow has **no deploy job**. No production branch merge, no CEFR public bank publication, no new audio deployment. The existing production **54 lessons, IELTS 1,000 bank, George/Emma recordings and privacy code** were not edited. GitHub Pages source/hosting settings and physical-device behaviour were **not independently checked**.

## Release blockers
**1,130 first-pass curriculum slots remain unwritten**, and **all 5,000 entries still lack complete independent approval**. All new CEFR George/Emma pronunciation audio remains ungenerated and unlistened; physical iPhone Safari, browser/mobile regression, full hosting/bandwidth checks and confirmed live deployment are outstanding. Existing original-source holds remain separate from these 18 new batch60 holds. No stage should be marked complete based on a structural CI success. Keep unverified drafts quarantined from publication and continue real source-based editorial review and nondeploy QA.
