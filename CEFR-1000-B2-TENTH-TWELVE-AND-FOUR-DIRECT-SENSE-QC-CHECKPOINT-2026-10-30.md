# CEFR 1,000 — B2 tenth direct publisher word/POS and sense triage (30 October 2026)

**STAGING ONLY — NOT independently approved — NO DEPLOYMENT.** Scope is the user-approved **1,000 total** (A1/A2/B1/B2/C1 = 200 each), not the obsolete 5,000-word proposal. Work is confined to `cefr-5000-bilingual-qa-staging`. Frozen [shortlist](draft/CEFR-1000-PROVISIONAL-SHORTLIST.json) and separate [independent review tasks](draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json) remain unchanged.

## Primary-source observations

The following 12 **previously unobserved B2-draft** word/POS entries were directly located on **2026-10-30** in the official Oxford 3000 and Oxford 5000 CEFR PDFs. The locators are 1-based PDF page numbers and zero-based web-extracted line indexes. Word/POS classification is **not proof that the intended exact sense belongs to the same CEFR level**.

| Draft B2 headword | POS | Oxford word/POS | PDF | Page | Text line | Editorial concern |
| --- | --- | --- | --- | ---: | ---: | --- |
| engineer | noun | A2 | 3000 | 5 | 1168 | Engineer as professional, not engineering process |
| operate | verb | B2 | 3000 | 11 | 3041 | Transitive machine control, not business operation |
| permission | noun | A2 | 3000 | 6 | 1466 | Uncountable permission versus a permit |
| reply | noun | A2 | 3000 | 6 | 1549 | PDF groups verb and noun; noun intended |
| tradition | noun | A2 | 3000 | 7 | 1719 | Family custom, not formal doctrine |
| visual | adjective | B2 | 3000 | 12 | 3294 | Related to images/seeing |
| criticism | noun | B2 | 3000 | 10 | 2747 | Disapproval versus neutral feedback |
| effectively | adverb | B1 | 3000 | 8 | 2007 | Achieving results, not effectively = virtually |
| historic | adjective | B1 | 3000 | 8 | 2121 | Historically important, not merely historical |
| improvement | noun | B1 | 3000 | 8 | 2141 | Improvement as progress versus individual change |
| philosophy | noun | B2 | 3000 | 12 | 3068 | Guiding teaching beliefs versus academic discipline |
| settlement | noun | C1 | 5000 | 7 | 1764 | Negotiated agreement, not a village or debt repayment |

Primary documents: [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf).

Counts: **A2 4 / B1 3 / B2 4 / C1 1**; **8 of 12** differ from provisional B2. No automatic retiering, replacement or approval was made.

## Direct Oxford dictionary exact-sense leads — research only

- [operate](https://www.oxfordlearnersdictionaries.com/definition/english/operate), sense 2, lines 131–145: transitive control of a machine, matching the draft example; distinguish intransitive functioning and operating a business.
- [settlement](https://www.oxfordlearnersdictionaries.com/definition/english/settlement), sense 1, lines 105–115: a countable agreement resolving a dispute, matching `reached a settlement`; Oxford 5000 PDF lists the noun at C1.
- [historic](https://www.oxfordlearnersdictionaries.com/definition/english/historic), sense 1, lines 107–124: significant in history, contrasted with `historical` as related to the past. **Publisher-surface conflict:** the Oxford 3000 CEFR PDF places `historic adj.` in B1, while the dictionary page footer at lines 165–169 displays **Oxford 5000 C1**. Both observations are retained and the conflict is **unresolved**, not silently overwritten.
- [philosophy](https://www.oxfordlearnersdictionaries.com/definition/english/philosophy), sense 3, lines 152–169: a guiding belief/attitude; matches `teaching philosophy` better than academic philosophy sense 1.

Four alternative Myanmar meanings and original English examples are **assistant editorial proposals only**, recorded in the [source-bound packet](draft/CEFR-1000-OXFORD-B2-TENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json) with original English/Myanmar/example snapshots, historical source path/index/Git blob SHA, direct source URLs, date and locators. The [fail-closed auditor](tools/audit_cefr_1000_oxford_b2_tenth_twelve.py) guards packet integrity, source identity, exact publisher observations, dictionary sense leads, the `historic` conflict and fake review/approval receipts; it includes **229 adversarial mutations**. Structural and documentary workflows include the auditor. **Verified CI:** [six-lane structural run 41073907359](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41073907359) completed **SUCCESS for A1/A2/B1/B2/C1/ALL** at code SHA `59392a9a8d7e45f9b933d6c4f46be674dd19c2ce`. Actual ALL-job logs show **229/229** tenth-B2 adversarial mutations rejected and **145/145** reviewer-handoff mutations rejected. [Documentary no-deploy run 41073928119](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41073928119) completed **SUCCESS, report-only** at SHA `c9c5cd35bd662df09fdd26514e2e31d3a6bb9edb`; logs retained all release blockers.

## Coverage and release blockers

With these 12 new direct Oxford word/POS observations, expected distinct publisher coverage becomes **A1 195/200, A2 120/200, B1 132/200, B2 130/200, C1 111/200 = 688/1,000**. Another **312** have no direct Oxford word/POS observations. Source observations total **707** (including historical duplicates). Expected reviewer queue: **3 unlisted / 36 publisher-higher / 239 publisher-lower / 410 matching but exact-sense-unverified / 312 without direct Oxford observation**. These totals were **confirmed in actual structural and documentary CI logs**. They are research coverage, not independently approved CEFR exact senses.

First-pass written / independently checked: **A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0**. **Final George/Emma real listening signoffs: 0/1,000**. The complete approved-corpus dual-voice headword/example audio generation and human listening, independent English/Myanmar/example/CEFR exact-sense review, browser/mobile regression, real physical iPhone Safari evidence, measured GitHub Pages hosting limits, protected production assets at launch, and confirmed production deployment are all **not verified**.

**Release BLOCKED / STAGING ONLY.** Preserve the 54 live lessons, separate IELTS 1,000-word bank, existing George/Emma production audio and privacy. No main change, merge, publication or production assertion.

## Verified staging scope and production protection

GitHub compare `894545139c30a97efbe1c658f7c18b0579a928ef...5d4ea233973d9cf6f130f2a22a1e90f97fc81846` showed only the B2 research packet, auditor, cross-batch/reviewer scripts, staging workflows and this checkpoint changed. **No main-branch write, merge, or production deployment was performed.** This change-scope check does **not** replace the required final preservation check after a future authorised launch.
