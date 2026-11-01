# CEFR 1000 — twelve source-bound noun countability and agreement cases (1 November 2026)

**STAGING ONLY / RELEASE BLOCKED.** User-approved scope is **1,000 total**, exactly 200 first-pass entries at each of A1, A2, B1, B2 and C1; not the superseded 5,000-word plan. Work confined to `cefr-5000-bilingual-qa-staging`. The frozen shortlist and independent review tasks remain unchanged.

## Evidence-backed findings

A fresh scan of the 1,000 frozen bilingual entries selected **12 teaching-sensitive noun cases**: **A1 1, A2 5, B1 5, B2 0, C1 1**. The [12-record research packet](draft/CEFR-1000-NOUN-COUNTABILITY-AND-AGREEMENT-TWELVE-2026-11-01.json) preserves each exact original English definition, Myanmar meaning, original example, historical source path/index/blob SHA, publisher or educational-grammar URL, observation date, source locator, grammar risk, and an **UNAPPROVED** example plus Myanmar teaching note. All original examples remain held; the scan did **not** establish a grammatical error in any of these twelve.

| Draft level | Word | Specific source-supported review issue |
| --- | --- | --- |
| A1 | bread | Mass food noun; count *loaves* or *slices*, not ordinary portions as *breads* |
| A2 | information | Uncountable; use *a piece of information*, not *an information* |
| A2 | news | Uncountable with **singular** verb despite final *-s* |
| A2 | police | Plural noun in the law-enforcement sense; **the police are** |
| A2 | data | Oxford permits **uncountable or plural**; specialist technical usage can take plural agreement, so a rigid single-number rule is wrong |
| A2 | experience | Practical knowledge is uncountable; a particular lived event is countable, and must not silently replace the frozen sense |
| B1 | advice | Uncountable; *some advice* or *a piece of advice* |
| B1 | equipment | Uncountable; count *pieces/items of equipment* |
| B1 | traffic | Uncountable road-vehicle sense; count traffic *jams*, not *traffics* |
| B1 | progress | Uncountable advancement sense; *make progress* |
| B1 | analysis | Oxford labels the study/result sense countable **and** uncountable; plural **analyses**, not *analysises* |
| C1 | diagnosis | Oxford labels illness/problem identification countable **and** uncountable; plural **diagnoses**, not *diagnosises* |

**Directly opened on 2026-11-01:** [British Council uncount nouns](https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/uncount-nouns) (lines 7–51), [Cambridge Dictionary editorial grammar article](https://dictionaryblog.cambridge.org/2018/03/21/countable-or-uncountable-and-why-it-matters/) (lines 11–54), [Oxford Online English uncountable nouns lesson](https://www.oxfordonlineenglish.com/uncountable-nouns) (lines 329–390, 491–520, 571–586), and Oxford Advanced Learner's Dictionary entries for [data](https://www.oxfordlearnersdictionaries.com/definition/english/data) (lines 111–128), [police](https://www.oxfordlearnersdictionaries.com/definition/english/police_1) (103–113), [experience](https://www.oxfordlearnersdictionaries.com/definition/english/experience_1) (107–115), [analysis](https://www.oxfordlearnersdictionaries.com/definition/english/analysis) (103–124), and [diagnosis](https://www.oxfordlearnersdictionaries.com/definition/english/diagnosis) (103–123). Source page-line locators and exact links are preserved per record. These are **grammar/sense observations**, not exact-sense CEFR certificates. Oxford *topic* badges and unrelated footer CEFR labels must not be mistaken for a headword's exact-sense CEFR classification.

**Editorial cautions:** The packet proposes twelve optional original English teaching examples and twelve fluent-Myanmar teaching notes, but these are **self-authored candidates**, not independently checked translations, approved replacement examples, or human signoff. A qualified independent reviewer must check grammar, meaning, natural Myanmar, level, source-backed exact sense, and consistency with the original word/POS. Do not automatically change *data* to singular-only or plural-only; do not turn *experience* into a different countable event sense; do not automatically retier based on grammar pages.

## Fail-closed release protection

The [new auditor](tools/audit_cefr_1000_noun_countability.py) requires the exact twelve records and per-level counts, unchanged frozen bilingual definitions/examples and historical Git provenance, direct source URL/locator/observation, unapproved candidate examples/notes, explicit grammar-only scope and all hold flags. It rejects forged source content, hidden approvals, false audio listening, unexpected CEFR claims, duplicated/deleted records and cross-level drift. It is wired to each of the six parallel A1/A2/B1/B2/C1/ALL structural lanes and documentary no-deploy workflow, with mutation tests in ALL and documentary QC. **Workflow success is only structural/documentary and never substitutes for external human review or real audio listening.**

## Truthful readiness ledger

| Level | First-pass written | Independently approved | Oxford word/POS research observations | Actual final George/Emma listening signoffs |
| --- | ---: | ---: | ---: | ---: |
| A1 | 200 | 0 | 195 | 0 |
| A2 | 200 | 0 | 200 | 0 |
| B1 | 200 | 0 | 200 | 0 |
| B2 | 200 | 0 | 200 | 0 |
| C1 | 200 | 0 | 200 | 0 |
| **Total** | **1,000** | **0** | **995** | **0** |

These twelve direct grammar observations **do not increase** Oxford 3000/5000 CEFR-list coverage. The five A1 exceptions remain *is, are, does, did, rabbit*, already quarantined. Still missing: independent authenticated English/Myanmar/example/exact-sense CEFR and pronunciation review for every retained entry, exactly 200 deduplicated approved headwords/senses per level, final George/Emma headword/example generation and **real listening** signoffs, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages limits, protected 54 lessons and separate IELTS 1,000 bank, existing production audio/privacy verification and confirmed live deployment. **NO MERGE, NO MAIN CHANGE, NO PUBLICATION.**

## Verified GitHub Actions evidence (2026-11-01)

After fixing an intermediate self-test hole that accepted an injected top-level CEFR field, [structural run 41266447895](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41266447895) completed **SUCCESS in all six A1/A2/B1/B2/C1/ALL jobs**; [documentary run 41266448123](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41266448123) completed **SUCCESS, report-only**. Both tested code SHA `402ccbb8675cf83441e32bc5e9e3624b5f891fbc`. Actual ALL and documentary logs confirm **323/323** source, frozen bilingual/provenance, false-approval and forged-listening mutations rejected. Structural ALL artifact `13067139554`; documentary blocker artifact `13067785722`. Documentary and structural logs confirm protected production assets unchanged. The intermediate failures [41266319012](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41266319012) and [41266322341](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41266322341) were repaired before these final successful runs. **These are automated structural/documentary tests only, not independent linguistic approval or listening.**
