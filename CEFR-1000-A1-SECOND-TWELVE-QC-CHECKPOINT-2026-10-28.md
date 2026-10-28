# CEFR 1,000 — A1 second Oxford publisher-source and QC checkpoint (2026-10-28)

**Release: BLOCKED / STAGING ONLY.** Scope is the user-approved **1,000 total** entries: A1/A2/B1/B2/C1 **200 each**, not the superseded 5,000. Work is exclusively on `cefr-5000-bilingual-qa-staging`. Original 1,000-row shortlist remains unchanged at blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

## Twelve new direct official Oxford PDF word/POS observations

Source: Oxford University Press, [The Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), directly inspected **2026-10-28**. The 12 headwords are listed in Oxford's **A1** section; the source **does not independently verify the exact draft sense, English wording, fluent Myanmar, example grammar or real pronunciation**. Page is 1-based; PDF-extracted line is 0-based.

| Draft word | Draft POS | Oxford PDF word/POS entry | Page / line | Independent editorial task theme |
| --- | --- | --- | --- | --- |
| the | article | the definite article | 3 / 782 | ARTICLE DEFINITION NOT MYANMAR EQUIVALENT |
| this | determiner | this det./pron. | 3 / 795 | DETERMINER VS PRONOUN SCOPE |
| that | determiner | that det., pron., conj. | 3 / 781 | POLYFUNCTIONAL HEADWORD SCOPE |
| he | pronoun | he pron. | 2 / 355 | GENDER AND REFERENCE |
| she | pronoun | she pron. | 3 / 686 | GENDER AND REFERENCE |
| it | pronoun | it pron. | 2 / 405 | MISSING ANTECEDENT AND DUMMY IT |
| my | determiner | my det. | 2 / 508 | MYANMAR REGISTER |
| your | determiner | your det. | 4 / 906 | MYANMAR REGISTER |
| yes | exclamation | yes exclam. | 4 / 902 | AFFIRMATION REGISTER |
| no | exclamation | no exclam., det. | 3 / 526 | EXCLAMATION VS DETERMINER |
| please | politeness marker | please exclam. | 3 / 604 | POS LABEL MISMATCH |
| hello | exclamation | hello exclam./n. | 2 / 360 | EXCLAMATION VS NOUN |

Notable editorial holds: `please` is labelled **politeness marker** in the draft while Oxford lists **exclamation**; `it` has a first-pass example without the antecedent required by its definition; `this` and `that` use determiner examples although Oxford also lists other grammatical functions; `the` has a metalinguistic Myanmar explanation, not an ordinary direct translation. The 12 records retain original English/Myanmar/example strings, source path/index/blob, dated publisher URL, PDF page/line/excerpt, specific editorial task, hold flags and null independent-review receipt. These are **review candidates, not approved corrections**. No draft content was rewritten.

[Read the immutable-source-bound evidence packet](draft/CEFR-1000-OXFORD-A1-SECOND-TWELVE-2026-10-28.json). [Read the fail-closed auditor](tools/audit_cefr_1000_oxford_a1_second_twelve.py).

## Verified GitHub Actions results (actual jobs and logs)

- [Structural run 40682100755](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40682100755), workflow commit `da491a7c154296e1f7afcfb85103c22f613f58d3`: **A1, A2, B1, B2, C1 and ALL jobs succeeded**. ALL job `122795124597` logged **26/26 negative source/approval mutations rejected** by the new auditor, exact 1,000 first-pass shortlist and 0 approvals; production-path diff **PASS**.
- [Documentary no-deploy run 40682115310](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40682115310), workflow commit `2ffd2d37676d7233f8bcfe76630776bbf6c52599`: job `122795171547` **succeeded as a report-only staging check**, including the new auditor's 26/26 negative mutations. Its log explicitly records release blockers and protected production-path diff **PASS**.
- Packet commit `4dd9a1e9248e91861a0d9e21aab21939b4011420`; new auditor commit `5efb9f14a87124e8e9f770460b22f8a6ff96cb0f`. **A CI success is mechanical validation, never independent bilingual or exact-sense review.**

## Exact counts and release decision

| CEFR | First-pass written | Independently approved | Final both-voice listening signoffs |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

Outstanding mandatory gates: separate independent human exact-sense CEFR/English/Myanmar/example approvals for all 1,000 and editorial conflict resolution; generated final British George/Emma headword and example audio plus actual listening signoffs; desktop/mobile browser regression; **physical iPhone Safari** testing; measured GitHub Pages hosting limits; full final protected-assets verification; and actual approved production deployment confirmation. No main merge, main modification, publication or release was performed. Protect the 54 lessons, independent IELTS 1,000-word bank, established George/Emma production audio and privacy controls.

**Do not claim completion, independent review, device testing or deployment.**
