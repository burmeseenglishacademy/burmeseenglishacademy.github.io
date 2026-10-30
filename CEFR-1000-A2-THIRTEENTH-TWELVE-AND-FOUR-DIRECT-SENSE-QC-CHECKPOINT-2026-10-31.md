# CEFR 1,000 — A2 thirteenth direct Oxford source checkpoint (2026-10-31)

**STAGING ONLY. NO INDEPENDENT APPROVAL. NO PRODUCTION RELEASE.**

> **CI VERIFIED, 2026-10-31:** [six-lane structural run 41142905798](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41142905798) **SUCCESS A1/A2/B1/B2/C1/ALL**, [documentary no-deploy run 41142906997](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41142906997) **SUCCESS report-only**. Both tested code SHA `bafd50257665bcad1523ed2ba9332e76ac038868`. Actual ALL/documentary logs confirm **232/232 new adversarial mutations rejected**, **760 distinct direct Oxford word/POS observations / 779 source observations**, human queue **3 unlisted / 44 higher / 283 lower / 430 matching but exact-sense-unverified / 240 unobserved**, zero independent approvals, zero real final dual-voice listening signoffs and protected production paths unchanged. Structural ALL artifact `13019446598`; documentary blocker artifact `13019637231`. CI does not establish linguistic signoff, actual listening, physical iPhone Safari, hosting measurements or live deployment. **BLOCKED / STAGING ONLY.**



## Scope and source observations

Frozen, user-approved target is **1,000 total words, 200 each at A1/A2/B1/B2/C1**, NOT the superseded 5,000-word plan. This checkpoint records **12 new direct Oxford 3000 word/POS observations for provisional A2 entries**, plus **four directly inspected Oxford dictionary sense leads**. Observed on **2026-10-31**. Official publisher source: [The Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf). Source packet: [A2 thirteenth 12-record JSON](draft/CEFR-1000-OXFORD-A2-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json).

| Provisional A2 headword | Oxford word/POS level | Publisher PDF page (1-based), extracted line (0-based) | Exact-sense risk |
| --- | --- | --- | --- |
| club (noun) | A1 | 1, 157 | Interest-group association versus sports venue or weapon |
| film (noun) | A1 | 2, 287 | British film/movie versus photographic film |
| event (noun) | A1 | 1, 249 | Organised event versus a general occurrence |
| watch (verb) | A1 | 4, 860 | Watch a scene versus watch as a timepiece |
| third (draft ordinal adjective) | A1, **number** | 3, 791 | **POS mismatch:** Oxford dictionary calls this an ordinal number, not an adjective |
| form (noun) | A1 | 2, 307 | Document to complete versus shape or verb |
| act (verb) | A2 | 4, 916 | Intransitive taking action versus acting/behaving |
| quite (adverb) | A1 | 3, 634 | British gradable 'fairly' versus non-gradable 'completely' |
| west (noun) | A1 | 4, 872 | Cardinal direction noun versus adjective/adverb |
| final (adjective) | A1 | 2, 288 | Last in sequence versus noun for competition |
| current (adjective) | B1 | 8, 1953 | Present-time adjective; provisional A2 requires rationale |
| program (noun) | A2 | 6, 1505 | Computer software versus TV programme and other senses |

Publisher word/POS labels: **A1 nine / A2 two / B1 one**. Ten provisional A2 placement differences; the **third** draft-POS mismatch is additionally unresolved. A word/POS list is not a publisher-certified classification of a specific dictionary sense, and none of these observations constitutes independent CEFR, English, Myanmar, example or pronunciation signoff.

## Four direct dictionary sense leads

- [third — Oxford ordinal number](https://www.oxfordlearnersdictionaries.com/definition/english/third_1), page text lines 88–115: attributive *third floor* is valid, but draft POS *ordinal adjective* requires editorial reconciliation. The existing draft example is also unusually close to Oxford's own *third floor* illustration; a distinct original alternative is held separately.
- [act — Oxford verb](https://www.oxfordlearnersdictionaries.com/definition/english/act_1), lines 124–146: response-to-situation sense is intransitive; avoid an invented transitive construction.
- [quite — Oxford adverb](https://www.oxfordlearnersdictionaries.com/definition/english/quite), lines 105–123: the draft means fairly in British English, not completely. Intonation and adjective gradability matter.
- [program — Oxford noun](https://www.oxfordlearnersdictionaries.com/definition/english/program_1), lines 88–123: sense 1 refers to computer instructions; British English normally spells software **program** and non-computing senses **programme**. The page's Computers a2 topic tag is not an independent exact-sense CEFR receipt.

All four contain new, **unapproved** fluent-Myanmar and original-English-example proposals, bound to frozen shortlist English/Myanmar/example snapshots and historical source Git path/index/blob. The frozen shortlist and separate independent-review tasks remain unchanged.

## Structural and release-readiness safeguards

Added [fail-closed source auditor](tools/audit_cefr_1000_oxford_a2_thirteenth_twelve.py), pinned to research-packet Git blob `9f1c9619081dd9c2249f97efdaf76a790c6e0dfe` and frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. It rejects publisher URL/label/line changes, forged Myanmar/examples/provenance and reviewer receipts; it defines **232 adversarial mutations**. Wired into all six A1/A2/B1/B2/C1/ALL structural CI lanes (with adversarial test in ALL) and the documentary no-deployment gate. These tests check evidence integrity, **not linguistic truth**.

Cross-batch direct Oxford word/POS observations should now reconcile to **A1 195/200, A2 144/200, B1 156/200, B2 154/200, C1 111/200 = 760/1,000 distinct**, 779 observations, 240 without direct Oxford observations. Reviewer priorities should become **3 unlisted / 44 publisher-higher / 283 publisher-lower / 430 matching but exact-sense-unverified / 240 without direct observation**. These counts require actual CI confirmation before being called verified.

First-pass written/independently approved remain **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Real final George/Emma listening signoffs remain **0/1,000**. Still missing: independent human English/Myanmar/example/source-backed exact-sense CEFR review, approved-manifest deduplication, final dual-voice headword/example audio and actual listening, browser/mobile regression, physical iPhone Safari review, GitHub Pages measured hosting readiness and confirmed production deployment. The 54 existing lessons, separate IELTS 1,000-word bank, existing George/Emma production audio and privacy paths are protected; no merge or deployment authorised.
