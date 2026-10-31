# CEFR 1,000 B1 thirteenth direct Oxford batch — editorial staging checkpoint

**Observation date:** 2026-10-31. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED / STAGING ONLY. This is the **approved 1,000-total plan** (A1/A2/B1/B2/C1: 200 each), not the superseded 5,000-word project.

## Direct publisher research, not independent CEFR signoff

Directly checked the [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on 2026-10-31. The following **12 previously unobserved B1-draft word/POS entries** are now captured with exact page and web-extracted-line locators, frozen shortlist English/Myanmar/example snapshots, and historical Git source path/index/blob in [the source-bound research packet](draft/CEFR-1000-OXFORD-B1-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json).

| Draft B1 word | Oxford word/POS level | PDF page / extracted line | Editorial exact-sense risk |
|---|---|---|---|
| village (noun) | A1 | 4 / 849 | Rural settlement vs local community |
| apply (verb) | A2 | 4 / 952 | Apply **for** a course vs apply **to** a body / apply a method |
| authority (noun) | B1 | 7 / 1834 | Uncountable right/power vs official body or permission |
| method (noun) | A2 | 6 / 1395 | Method vs a particular procedural step |
| healthy (adjective) | A1 | 2 / 358 | Draft defines healthy person, example describes healthy **diet** |
| option (noun) | A2 | 6 / 1437 | Choice among alternatives |
| trouble (noun) | A2 | 7 / 1726 | Uncountable difficulty; **have trouble finding** |
| apart (adverb) | B1 | 7 / 1819 | Physical distance vs figurative separation or **apart from** |
| gift (noun) | A2 | 5 / 1247 | Present vs natural talent |
| require (verb) | B1 | 9 / 2382 | Need vs obligation; weekend-work complement |
| wood (noun) | A2 | 7 / 1770 | Material (uncountable) vs woodland (countable) |
| background (noun) | A2 | 4 / 977 | Education/work experience vs image or historical context |

Publisher distribution: **A1 two, A2 seven, B1 three**, giving **nine provisional B1 word/POS placement discrepancies**. These are research leads for independent exact-sense reviewers, not instructions to retier automatically. Oxford word/POS list levels do not independently certify every dictionary sense.

## Four direct dictionary sense leads and unapproved alternatives

Direct Oxford dictionary entries inspected on 2026-10-31: [apply](https://www.oxfordlearnersdictionaries.com/definition/english/apply) (sense 1, web lines 110–129), [authority](https://www.oxfordlearnersdictionaries.com/definition/english/authority) (sense 2, lines 150–160), [apart](https://www.oxfordlearnersdictionaries.com/definition/english/apart) (sense 1, lines 107–112), and [background](https://www.oxfordlearnersdictionaries.com/definition/english/background) (sense 1, lines 106–134). The research packet includes four **self-authored, unapproved** Myanmar and original-example proposals. Oxford's dictionary topic labels, when present, are **not** substitutes for exact-sense CEFR review. The draft's healthy definition/example mismatch is separately flagged for human review.

## Fail-closed QC and coverage

Added [source-bound auditor](tools/audit_cefr_1000_oxford_b1_thirteenth_twelve.py) and integrated it into **six parallel structural lanes** (A1, A2, B1, B2, C1, ALL) plus the **documentary no-deployment** workflow. The auditor checks 12 publisher locators and classifications, original bilingual/example snapshots, historical Git provenance, 4 dictionary-sense leads, approval holds and frozen blob IDs; the ALL and documentary jobs additionally exercise **144 adversarial mutations** (publisher/source, Myanmar, provenance, fake independent receipt and fake release approval). This is structural QC, not real human review.

After this batch, expected direct Oxford word/POS coverage: **A1 195/200, A2 144/200, B1 168/200, B2 154/200, C1 111/200 = 772/1,000 distinct**, 791 observations including duplicate research observations; **228** without direct Oxford observation. Human review queue: **3 unlisted / 44 publisher-higher / 292 publisher-lower / 433 matching word/POS but exact-sense-unverified / 228 unobserved**. The coverage auditor and source-bound reviewer-handoff counts were updated together.

**First-pass written / independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. Final George/Emma real listening signoffs: **0/1,000**. Independent human English, fluent Myanmar, original-example, exact-sense CEFR and pronunciation signoff; final dual-voice headword+example generation and listening; approved-manifest deduplication; browser/mobile regression; physical iPhone Safari; measured GitHub Pages limits; and confirmed production deployment remain **unverified**.

The new source packet, scripts and workflows are confined to the staging branch; existing 54 lessons, separate IELTS 1,000 bank, established George/Emma production audio and privacy settings are not edited. **Do not merge, publish or change main.** GitHub Actions success, if observed, is evidence of structural test completion only, never launch clearance.

## Verified GitHub Actions (structural only, no launch)

- [Structural run 41149241837](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41149241837): **SUCCESS** across A1/A2/B1/B2/C1/ALL, code SHA `1e25c59ef24db70a45bceca17b28e772d950069b`. Actual ALL logs: **144/144** new adversarial mutations rejected, **772 distinct** Oxford word/POS research entries, **791** observations, protected production paths unchanged; ALL artifact ID `13022481358`.
- [Documentary no-deploy run 41149254668](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41149254668): **SUCCESS, report-only**, code SHA `a40a06e8cbe5411ce4fbd470ace3c92d64313a66`. Actual logs: **144/144** new adversarial mutations rejected, human reviewer queue **3/44/292/433/228**, no verified physical iPhone Safari or British audio listening, and production assets protected; blocker artifact ID `13021454972`.
- An earlier intermediate run at SHA `b15e81ca89e91a9b82691c45d49c5024533a99d9` failed because coverage was advanced before the reviewer-handoff expected totals were reconciled. That count mismatch was repaired; the later successful runs above were inspected by job conclusions and logs. **Success does not mean independent linguistic verification, real listening, mobile QA or deployment.**
