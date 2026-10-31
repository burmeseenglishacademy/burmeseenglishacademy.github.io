# CEFR 1,000 — C1 thirteenth twelve Oxford publisher observations (1 November 2026 SGT)

**STAGING ONLY. No independent approvals, real audio listening, physical iPhone testing, production merge or deployment.**

## Source-supported observations

Directly inspected Oxford University Press's official [Oxford 3000](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) by CEFR level PDFs on **2026-11-01**. Twelve previously unobserved C1-draft headwords were checked: naval, noble, treasury, ethics, manufacturer, veteran, legally, census, destiny, mitigate, disproportionate, perpetuate.

- **mitigate v.** appears under Oxford 5000 **C1**, PDF page **6**, extracted line **1488**. This is **word/POS** evidence only; it does not independently verify the intended exact sense or CEFR pedagogy.
- **Eleven other draft word/POS combinations were not found** in either inspected core list. **Not found is NOT a CEFR level.** Oxford 5000 does contain **veteran n.** under C1 (page 8, extracted line **1976**), but the draft is **veteran adjective**. Oxford 5000 also contains **ethic n.** under B2 (page 1, extracted line **220**), which must not be automatically assigned to plural **ethics**. Related words **manufacture v.** and **manufacturing n.** do not classify **manufacturer n.**

Five official Oxford dictionary pages were directly accessed as **sense/grammar research leads**, not independently attested CEFR evidence:

- [naval adjective](https://www.oxfordlearnersdictionaries.com/definition/english/naval), page text lines 88–110: navy-related adjective; **War and conflict c1** is a topic label, not a wordlist CEFR signoff.
- [ethic noun](https://www.oxfordlearnersdictionaries.com/definition/english/ethic), lines 88–125: plural **ethics** for moral principles, and uncountable **ethics** for the philosophical field; do not conflate senses.
- [manufacturer noun](https://www.oxfordlearnersdictionaries.com/definition/english/manufacturer), lines 88–115: a person **or company** producing goods in quantity; **Business b2** is a topic label, not an exact-sense CEFR label.
- [census noun](https://www.oxfordlearnersdictionaries.com/definition/english/census), lines 88–132: official counting and recording, especially population; **Word of the Day C1** in the page footer is unrelated to census.
- [mitigate verb](https://www.oxfordlearnersdictionaries.com/definition/english/mitigate), lines 88–122: formal transitive usage **mitigate something** (harm, effects, problems); the unrelated Word of the Day B2 footer must not override the actual PDF C1 word/POS evidence.

Original English definitions, Myanmar meanings, examples, historical source indices and Git blob provenance are preserved in [the immutable twelve-record packet](draft/CEFR-1000-OXFORD-C1-THIRTEENTH-TWELVE-AND-FIVE-DIRECT-SENSE-LEADS-2026-11-01.json). Five **unapproved** Myanmar/example alternatives were prepared for ethics, manufacturer, veteran, census and mitigate. None was copied into the frozen shortlist or marked reviewed.

## Structural checks and reviewer handoff

The [new fail-closed auditor](tools/audit_cefr_1000_oxford_c1_thirteenth_twelve.py) verifies frozen shortlist snapshots, three actual historical source blobs and indices, exact Oxford PDF locators, five publisher dictionary leads, and rejection of fabricated human approval. It defines **188 adversarial mutations** (12 × 14 source/bilingual/approval mutations, 5 × 2 dictionary mutations, 5 proposal mutations and 5 packet mutations). Wired into all **six parallel A1/A2/B1/B2/C1/ALL structural lanes** and documentary no-deployment QC.

**Actual GitHub Actions verified:** [parallel structural run 41222601714](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41222601714) completed **SUCCESS** for A1/A2/B1/B2/C1/ALL on code SHA `764063176a170178dbcb669c94d87595bff14d4b`. [Documentary no-deployment run 41222605950](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41222605950) completed **SUCCESS (report-only)** on code SHA `60c953fa034220d0632394fd83cd3f3b81d5231a`. Actual ALL and documentary job logs each confirmed **188/188** forged publisher, bilingual, historical-source and approval mutations rejected. ALL logs verified **930 distinct Oxford research observations, 949 source observations, 70 unobserved**, and the precise review priority counts below. Protected production assets unchanged in both CI jobs. Structural ALL artifact ID `13050622641`; documentary blocker artifact ID `13049874132`. **CI success is structural and documentary only, not independent linguistic approval or launch permission.**

Expected after reconciliation: Oxford research **A1 195/200, A2 200/200, B1 200/200, B2 200/200, C1 135/200 = 930/1,000 distinct** across **949 observations**; 70 still without audited Oxford core-list observations. Reviewer priority expected: **46 unlisted**, **61 publisher-higher**, **352 publisher-lower**, **471 matching word/POS but exact sense unverified**, and **70 unobserved**. These are structural research classifications, not independently approved vocabulary.

First-pass written / independently approved remains **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Final George/Emma actual listening signoffs **0/1,000**. Independent English, fluent Myanmar, original example and source-backed exact-sense CEFR review; approved-manifest deduplication; complete George/Emma headword and example audio with actual listening; browser/mobile and physical iPhone Safari testing; GitHub Pages deployment-artifact measurement; preserved production assets and confirmed production launch remain missing. **Release BLOCKED / STAGING ONLY.**
