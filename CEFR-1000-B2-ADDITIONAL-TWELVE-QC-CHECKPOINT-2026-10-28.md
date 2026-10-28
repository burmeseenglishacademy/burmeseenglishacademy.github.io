# CEFR 1,000 — fourth B2 direct Oxford source triage (2026-10-28)

**Release: BLOCKED / STAGING ONLY.** Scope remains exactly **1,000 provisional entries** (A1/A2/B1/B2/C1: 200 each). All 1,000 remain on editorial hold; no human-independent approval, audio listening or public release is asserted. Branch `cefr-5000-bilingual-qa-staging`; main must remain unchanged.

## Direct Oxford publisher observations

Directly inspected [Oxford University Press, *The Oxford 3000 by CEFR level*](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-28**. PDF pages below are one-based; extracted lines are zero-based. These observations classify a **headword/part of speech**, **not the exact draft sense**, and are not independent verification. Four provisional B2 entries have lower Oxford word/POS levels (three B1, one A2).

| B2 draft headword | Oxford word/POS CEFR | PDF page / extracted line | Exact-sense, English, Myanmar or example risk |
|---|---|---|---|
| relief | B2 | 12 / 3132 | Noun emotion of reassurance; distinguish relief aid/assistance |
| shame | B2 | 12 / 3185 | Emotional guilt vs public disgrace; assess Myanmar tone |
| somewhat | B2 | 12 / 3204 | Degree adverb; Myanmar rendering 'တစ်စိတ်တစ်ပိုင်း' may imply a part rather than degree |
| surely | B1 | 10 / 2487 | **Conflict**: B2 draft, Oxford B1 adverb; epistemic/interpersonal pragmatic sense |
| absolute | B2 | 10 / 2594 | Check 'absolute silence' collocation and whether 'complete' sense is covered |
| incident | B2 | 11 / 2932 | Workplace safety-report context; distinguish incident vs accident |
| quit | B1 | 9 / 2346 | **Conflict**: B2 draft, Oxford B1 verb; quitting a job is ordinary sense |
| widely | B2 | 12 / 3307 | Passive 'widely used' example and natural Myanmar adverb |
| worldwide | B1 | 10 / 2582 | **Conflict**: B2 draft, Oxford B1 adjective/adverb; example is adverb |
| anniversary | B2 | 10 / 2622 | Annual recurrence; company tenth anniversary grammar |
| attractive | A2 | 4 / 967 | **Conflict**: B2 draft, Oxford A2 adjective; ordinary appealing design sense |
| broad | B2 | 10 / 2668 | Abstract range vs physical width; example specifically management knowledge |

[Immutable original snapshot packet](draft/CEFR-1000-OXFORD-B2-ADDITIONAL-TWELVE-2026-10-28.json) binds all 12 original English definitions, Myanmar meanings, example sentences, original Git source path/index/blob SHA and Oxford URL, observation date, page/line and source label to the provisional shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. No words were automatically retiered, definitions rewritten or review flags set.

## Mechanical safeguards and evidence

- [Provenance auditor](tools/audit_cefr_1000_oxford_b2_additional_twelve.py) validates all 12 exact snapshots, Git blob binding, 200/level counts, source locators, publisher scope, hold flags and absence of fabricated receipts; it contains **24 deliberately forged negative mutation cases**.
- The six parallel structural A1/A2/B1/B2/C1/ALL jobs [run 40703950423](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40703950423) succeeded at head `438a9847c5b7ed92146085690a46e9a2f8910013`. Actual ALL-job `122870905461` logs confirm **24/24** forged evidence/review mutations rejected and protected production diff PASS.
- The documentary [run 40704000763](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40704000763) succeeded as **report-only** at head `45f02b47f72956ca91fd34fd08605c9e35b7ccde`; its log confirms missing approved manifest and browser/mobile QC, plus 24/24 forged mutations rejected.
- A separate empty `oxford_b2_additional_twelve_review_receipts` collection was added to [release evidence](draft/CEFR-1000-RELEASE-EVIDENCE.json). [Launch readiness](tools/audit_cefr_1000_launch_readiness.py) now requires content-hash-bound **human-independent exact-sense B2 review** for any retained flagged word, and specific source-level discrepancy justification for `surely`, `quit`, `worldwide` and `attractive`. A changed meaning/example invalidates previous content-bound evidence. This is a fail-closed **documentary gate**, not independent verification.
- The **post-amendment** documentary [run 40704074483](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40704074483) succeeded at head `76b7b035dab6e29385326fc325f708205d513863`. Actual job `122871341630` log confirms **24/24** negative mutations rejected, launch still BLOCKED due missing independent review/audio/device/hosting evidence, and protected production diff PASS. Success means the *report-only safeguard ran*, not launch approval.

## Outstanding blockers

First-pass written/independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Final George/Emma real listening receipts **0/1,000**. Independently verified English, natural Myanmar, example grammar and exact-sense CEFR receipts absent; physical iPhone Safari, browser/mobile regression, GitHub Pages hosting measurement and confirmed production deployment absent. Preserve the 54 lessons, separate IELTS 1,000-word bank, production George/Emma audio and privacy. **No merge, publish or main modification.**
