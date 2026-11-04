# CEFR-1000: complete five-lane raw CI-log verification and example-length triage

Observed: 2026-11-05 (Singapore). **Staging evidence only — NOT release clearance.**

## Frozen data and scope
Read `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` directly from `cefr-5000-bilingual-qa-staging`; blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Exactly 1,000 first-pass records: A1 200, A2 200, B1 200, B2 200, C1 200. No duplicate case-normalised headwords found. Independent approvals: **A1 0, A2 0, B1 0, B2 0, C1 0**. All entries remain editorial hold. Source provenance fields remain present. This is not evidence that exact-sense CEFR labels or Myanmar translations are correct.

## Actual GitHub Actions raw logs
Run [41801157929](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41801157929), associated with previously verified commit `d21a9a3e9241a6a8887c3fc96ad40f55908ac201`. Retrieved all four previously uninspected raw job logs on 2026-11-05, in addition to the previously inspected A1 log. All five jobs concluded **success**. Each retrieved A2–C1 log contains `Ran 14 tests` and `Ran 10 tests` and no failure summary; the lane inventory assertion and deliberate missing-release-evidence rejection are visible. Job IDs:

| Lane | Job ID | Conclusion | Shared / lane tests |
|---|---:|---|---|
| A1 | 126476956545 | success | 14 / 10 (previously inspected) |
| A2 | 126476956833 | success | 14 / 10 |
| B1 | 126476956739 | success | 14 / 10 |
| B2 | 126476956787 | success | 14 / 10 |
| C1 | 126476956858 | success | 14 / 10 |

CI scope is **structural**; the workflow does not independently evaluate dictionary evidence, spoken audio quality or physical Safari behaviour. The retrieved logs also warn that Node.js 20 actions are being forced to Node.js 24 (`actions/checkout@v4`, `actions/setup-python@v5`); maintenance follow-up should assess supported action upgrades without changing production.

## New full-shortlist editorial triage: example length
A scan of all 1,000 provisional examples found **8 examples shorter than four whitespace-delimited words**, all A1. This is a *review queue*, not a grammar failure; concise imperative and declarative sentences can be excellent A1 examples.

| Word | Existing example | Review decision needed |
|---|---|---|
| me | Please help me. | Keep if object-pronoun sense and Myanmar explanation align |
| here | Please sit here. | Distinguish location from discourse-marker senses |
| come | Please come here. | Verify motion-towards-speaker sense |
| are | They are friends. | Confirm inflected-form inclusion policy for `be` |
| today | Today is Monday. | Review contextual day-of-week example for portability |
| yesterday | Yesterday was Sunday. | Review contextual day-of-week example for portability |
| face | Wash your face. | Confirm noun sense rather than verb |
| sit | Please sit here. | Check imperative and sitting-posture sense |

No examples exceeded 20 whitespace-delimited words, none lacked final sentence punctuation, and no Myanmar meaning field was blank. These are mechanical checks, not fluency or linguistic signoff. The scan also found 12 naive case-insensitive definition/headword substring matches, but this heuristic confuses short headwords (`i`, `in`, `to`) with substrings of unrelated words; **do not** label these as circular definitions or fail release on this heuristic. Exact tokenisation and human sense review are required.

## Remaining release blockers
No independently signed English/Myanmar/example/source-backed CEFR review; no final George/Emma headword-and-example audio plus real listening signoff; no browser/mobile regression or physical iPhone Safari QA evidence; no hosting clearance or confirmed production deployment. Preserve 54 lessons, the separate IELTS 1,000 bank, established George/Emma production assets and privacy. Do not alter `main`, merge or publish. The existing frozen shortlist and review flags were not edited in this run.
