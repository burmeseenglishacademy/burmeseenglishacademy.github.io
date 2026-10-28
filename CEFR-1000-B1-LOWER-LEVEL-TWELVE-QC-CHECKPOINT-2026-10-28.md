# CEFR 1,000 — twelve additional direct Oxford B1-draft word/POS observations (2026-10-28)

**Release decision: BLOCKED / STAGING ONLY.** User-approved scope: exactly **1,000 total**, A1/A2/B1/B2/C1 **200 each**. The former 5,000 plan is superseded. All 1,000 remain editorial holds; **0 independently approved**. The branch name `cefr-5000-bilingual-qa-staging` is intentionally retained. No merge, main edit, release, production deployment, physical iPhone review or real listening was performed.

## Publisher source and 12 editorial findings

**Directly inspected publisher-owned source:** [Oxford University Press, *The Oxford 3000 by CEFR level* (official PDF)](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), observed **2026-10-28**. Page numbers below are **1-based PDF pages**; line locators are **0-based extracted text lines**. Source contains **word/part-of-speech-level** classifications, **not publisher-verified exact dictionary senses**. A source difference flags human review; it does not prove that the proposed teaching level is wrong.

[Machine-readable provenance packet](draft/CEFR-1000-OXFORD-B1-LOWER-LEVEL-TWELVE-2026-10-28.json) retains each unchanged B1 draft's English definition, original Myanmar meaning, original example, source file/index/blob SHA, publisher URL, observation date, page/line locator, editorial risk and independent reviewer task.

| B1 draft headword | Official Oxford 3000 word/POS level | PDF page, line | Editorial interpretation |
| --- | --- | --- | --- |
| address (noun) | A1 | 1, 13 | Ordinary postal-address meaning; requires independent B1 sense justification |
| advice (noun) | A1 | 1, 15 | Common advice sense; independently review uncountable use and Myanmar |
| explain (verb) | A1 | 2, 261 | Ordinary explanation sense; a B1 example alone does not justify B1 |
| grow (verb) | A1 | 2, 341 | Basic plant-growth sense; independently justify a distinct B1 sense |
| machine (noun) | A1 | 2, 457 | General powered-equipment sense; specialised example is not proof of B1 |
| trip (noun) | A1 | 4, 820 | Common journey sense; check overly narrow return-journey wording |
| competition (noun) | A2 | 4, 1069 | Common contest sense; independently verify B1-specific teaching target |
| learning (noun) | A2 | 5, 1351 | General acquiring-knowledge sense; check Myanmar and B1 distinction |
| necessary (adjective) | A2 | 6, 1415 | General needed/essential sense; no independently supported B1 distinction |
| protect (verb) | A2 | 6, 1509 | Common protect-from construction; verify source-backed B1 specificity |
| secret (noun) | A2 (adjective/noun) | 6, 1594 | Common concealed-information noun; review collocation and Myanmar |
| analysis (noun) | B1 | 7, 1813 | Word/POS level matches, but exact sense and bilingual example remain unapproved |

**New observations:** 12 B1-draft entries; **11** have a lower Oxford word/POS classification (6 A1, 5 A2); **1** matches B1. These are existing entries, **not** 12 new words, and no source-derived retiering or content rewrite was made. A1/A2 word/POS evidence alone is insufficient for a final B1 exact-sense approval. Independent reviewers must either find genuine B1 exact-sense publisher evidence and revise/justify any conflicting draft, or independently select and verify a replacement/level correction while preserving exactly 200 entries per level.

## Safeguards and actual CI execution

- Added [fail-closed source/hold auditor](tools/audit_cefr_1000_oxford_b1_lower_twelve.py): pins official publisher metadata and page/line observations, canonical bilingual/example/source snapshots, unchanged 1,000-shortlist blob, all 12 editorial holds and zero approvals. **26 negative mutations** cover forged publisher labels/locators, changed Myanmar or English, altered examples, provenance tampering, false review/approval, duplicates and omitted holds.
- Integrated the auditor into the [parallel six-job A1/A2/B1/B2/C1/ALL structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) and the [documentary no-deploy workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml). Added an empty `oxford_b1_lower_twelve_review_receipts` collection to the release ledger; no reviewer evidence was invented.
- Updated the launch-readiness auditor: retained flagged B1 entries require a separate independently attested direct-publisher **exact-sense B1** receipt, reviewed-content SHA-256, correct POS and explicit rationale. For the 11 lower-level conflicts, unchanged original basic definition+example cannot be rubber-stamped. Receipt structure alone **cannot authenticate the reviewer or actual publisher observation**.
- **Actual initial failure and repair:** GitHub Actions [structural run 40649787879](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40649787879) and subsequent documentary checks failed because the new auditor demanded uppercase `NOT` in a provenance caveat that correctly used lowercase `not`. Fixed the auditor's case-sensitive check in commit [461c4d65e7f82bfc4bad831345f62283a2bc55e9](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/461c4d65e7f82bfc4bad831345f62283a2bc55e9), without relaxing source integrity or review holds.
- **Verified post-fix structural run [40649874323](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40649874323)**: six actual job conclusions **A1 success, A2 success, B1 success, B2 success, C1 success, ALL success**. The ALL job [122687194154](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40649874323/job/122687194154) tests the new auditor, including 26/26 negative mutations rejected.
- **Verified documentary no-deploy run [40649874402](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40649874402)**: job [122687193087](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40649874402/job/122687193087) succeeded as **report-only**, with the new 26 negative mutations rejected. Its actual log reports **0/1,000** independent source reviews and **0/1,000** both-voice real listening receipts, plus missing physical iPhone, desktop/mobile, hosting, approved manifest and production evidence. Protected production paths passed the staging-vs-main diff check. A documentary job success is **not** a release PASS.

## Exact counts and outstanding gates

| Level | First-pass English + Myanmar + example written | Independently checked/approved | Final George/Emma listening receipts |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

**Still mandatory:** independently verified English, natural Myanmar, original example grammar, and exact-sense CEFR for every entry; cross-level and WordNet/named-entity and shared IELTS wordform decisions; exactly 200 deduplicated approved headwords/senses per level; generated George/Emma headword **and** sentence audio with real listening signoff; desktop/mobile regressions; physical iPhone Safari and British-voice evidence; measured [GitHub Pages hosting limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits); complete production asset/privacy preservation; and confirmed live deployment **only after** all prelaunch gates pass.

The 54 existing lessons, separate IELTS 1,000-word bank, production George/Emma audio and privacy files were not edited. **No launch and no completion notification.**
