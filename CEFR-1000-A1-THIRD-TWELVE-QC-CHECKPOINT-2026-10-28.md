# CEFR 1,000 — third A1 Oxford direct-PDF editorial QC, 2026-10-28

**Release decision: BLOCKED / STAGING ONLY.** User-approved scope: **1,000 total** entries, **200 each A1, A2, B1, B2, C1**; superseded 5,000 plan is not in scope. This checkpoint is *not* independent language, CEFR, audio or deployment signoff. Branch: `cefr-5000-bilingual-qa-staging`; main unchanged.

## Direct publisher source and exact observation locators

On **2026-10-28** the [official Oxford University Press Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) was inspected as publisher PDF text. Page numbers below are **one-based**; extracted lines are **zero-based**. Oxford A1 word/POS observations are **not exact-sense evidence** or independent approval.

| Provisional A1 word | Oxford A1 word/POS observation | PDF page / line | Specific independent editorial risk |
| --- | --- | --- | --- |
| goodbye | `goodbye exclam./n.` | 2 / 333 | Interjection versus noun; natural Myanmar farewell register |
| thank | `thank v.` | 3 / 779 | Original `I thank my teacher.` is grammatical but stilted for everyday A1 speech |
| water | `water n.` | 4 / 861 | English definition only covers drinkable water; intended sense scope needs review |
| food | `food n.` | 2 / 302 | Uncountable collective noun and Myanmar usage |
| home | `home n., adv.` | 2 / 372 | **Critical: draft POS noun but original example `I go home after school.` uses `home` adverbially** |
| family | `family n., adj.` | 2 / 268 | Noun example must not silently cover adjective use |
| mother | `mother n.` | 2 / 497 | Myanmar kinship register and intended parent sense |
| father | `father n.` | 2 / 276 | Myanmar kinship register and beginner example |
| school | `school n.` | 3 / 669 | Building/place versus educational institution |
| teacher | `teacher n.` | 3 / 767 | Gender-neutral English noun and Myanmar equivalents |
| student | `student n.` | 3 / 745 | School/college/university scope and inclusive Myanmar |
| book | `book n.` | 1 / 96 | Oxford A1 noun versus separately listed A2 verb `book` |

[Source packet](draft/CEFR-1000-OXFORD-A1-THIRD-TWELVE-2026-10-28.json) retains **all 12 original** English definition, Myanmar meaning and example strings, original source path/index/blob SHA, publisher URL/date/page/line/label, individual reviewer tasks, and explicit `editorial_hold: true`, `independently_reviewed: false`, `release_approved: false` and null independent receipts. Original shortlist blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. No draft rewrites or automatic retiering.

## Concrete safeguards implemented and actually executed

- [Third A1 evidence auditor](tools/audit_cefr_1000_oxford_a1_third_twelve.py) verifies packet-to-shortlist bilingual/example/source binding and publisher locators. Its **28/28 negative mutations** were rejected in actual CI, including forged publisher data, false review/approval, duplicated words and altered `home` editorial risk.
- The [six-job parallel structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) passed **A1, A2, B1, B2, C1, ALL** in [GitHub Actions run 40695641596](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40695641596), head `d65dc65575a3e93782c3eb022d1fc8381ce8d57a`. The ALL job `122841549010` log confirms **28/28** negative mutations rejected.
- The [documentary no-deploy workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml) passed as **report-only** in [run 40695797697](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40695797697), job `122842098290`, head `acef286c1eafa562c204444676d1c1515ce8f323`. Logs show third-batch source audit 28/28, rejection of a forged A1 receipt, `source-reviewed 0 /1000`, `both-voice listening 0 /1000`, and protected production assets diff PASS.
- [Launch-readiness auditor](tools/audit_cefr_1000_launch_readiness.py) now requires separate human-independent A1 exact-sense receipt and content-bound review for all retained 12, a substantive noun-example resolution for `home`, and a naturalness review for `thank`. The new [release evidence field](draft/CEFR-1000-RELEASE-EVIDENCE.json) is an **empty array**, not fabricated human approval. These are documentary checks; reviewer identity and linguistic accuracy cannot be established by code alone.

## Exact current counts and non-negotiable blockers

| Level | First-pass English/Myanmar/example written | Independently checked and approved | Final both-voice listening receipts |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

Final George and Emma headword/example audio generation and **real listening signoff** are not established. Independent English, fluent Myanmar, grammar and exact-sense CEFR review, physical iPhone Safari evidence, complete desktop/mobile regression, measured GitHub Pages hosting size/bandwidth, approved manifest, final protected-production-assets verification and live deployment confirmation are missing. Protected production diff in this CI run passed, but it is **not** an exhaustive physical/audio listening or production-release audit.

**No merge, no publication, no main-branch modification, no independent approval and no release-completion claim.** Public launch remains conditional on all evidence gates.
