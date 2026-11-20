# CEFR-1000 example-form and reuse audit — 2026-11-20

Status: AUTHOR MECHANICAL TRIAGE ONLY; no independent review, CEFR validation, or release permission.

## Scope and reproducibility
Repository: `burmeseenglishacademy/burmeseenglishacademy.github.io`, branch `cefr-5000-bilingual-qa-staging`.
Inspected `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, 1,000 entries (A1/A2/B1/B2/C1: 200 each), and independent-review task blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
Observation date: 2026-11-20. Evidence is **internal corpus inspection**, not external dictionary/CEFR evidence. Source: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json

Method: case-insensitive whole-token literal headword search in each example, with alphabetic boundaries; exact case-insensitive example-sentence duplicate grouping. The headword test deliberately does not lemmatise, and therefore flags valid inflections. It is a triage signal, not a failure criterion.

## Five surface-form mismatches (not necessarily errors)
| Level | Headword | Existing example | Editorial interpretation |
| --- | --- | --- | --- |
| A1 | hand | Please wash your hands. | regular plural, pedagogically acceptable if singular/plural forms are explained |
| A1 | eye | I have two eyes. | regular plural, pedagogically acceptable |
| B2 | manage | We managed to finish the work before the deadline. | past tense, accurately illustrates *manage to* but needs construction-level sense confirmation |
| B2 | destroy | The fire destroyed the old warehouse. | past tense, grammatically natural |
| B2 | grab | She grabbed her bag and ran outside. | past tense, grammatically natural |

**Decision for independent reviewer:** retain natural inflection where helpful; confirm that the exact illustrated sense, grammatical construction and Myanmar meaning align. Do not auto-replace these examples merely to force exact surface headword matching. Potential alternative examples (author drafts, NOT independently approved): “Wash your hand before the nurse checks it.”; “Close one eye and read the letter.”; “Can you manage to carry both boxes?”; “A large fire can destroy a warehouse.”; “Grab the handle before the door closes.” These alternatives also require independent grammar, naturalness and translation review.

## Three repeated example strings across seven records
- `The book is on the table.`: A1 **the** and **table**.
- `What is your name?`: A1 **your**, **name**, **what**.
- `Please sit here.`: A1 **here** and **sit**.

Repeated sentences are not necessarily incorrect: each targets a different lexical item. However, they reduce example diversity and can make isolated headword/example audio feel repetitive. Reviewer should decide whether to retain useful multi-target sentences or provide distinct original examples with appropriate level, context and Myanmar translation. Do not treat example reuse as a duplicated headword/sense.

## Release-gate implications
1. A lexical validator should accept attested inflection through a reviewed lemma/POS mapping, not merely literal substring checks; avoid falsely rejecting these five entries.
2. A separate *warning-only* report can list exact repeated examples; independent human review decides whether reuse is acceptable.
3. No evidence here establishes CEFR level, English or Myanmar accuracy, independent approval, George/Emma audio generation/listening, physical iPhone Safari testing, or hosting/deployment.
4. Exact per-level first-pass written counts: A1=200, A2=200, B1=200, B2=200, C1=200. Independently checked/approved: A1=0, A2=0, B1=0, B2=0, C1=0. Audio and physical-device gates: unverified/incomplete. **Remain staging-only; no production changes.**

This document must never be interpreted as an independent reviewer signature or source-backed CEFR approval.
