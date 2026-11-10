# CEFR-1000 publisher-level conflict disposition queue — 2026-11-10

**Scope:** Approved project size is 1,000 provisional entries, 200 each at A1, A2, B1, B2, C1. This document is an editorial work queue, **not** an independently verified CEFR classification. No release or approval fields are modified.

## Evidence and provenance

- Provisional source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, inspected 2026-11-10. Its metadata reports A1/A2/B1/B2/C1 = 200/200/200/200/200 written first-pass; independent approvals = 0/0/0/0/0.
- Earlier direct publisher word/POS spot-observation record: `draft/CEFR-1000-OXFORD-PRIMARY-SOURCE-SPOT-OBSERVATIONS.json`, blob SHA `88b0b3204b26994957ca8278cd271cb869dc10f2`, originally observed 2026-10-27, re-examined 2026-11-10.
- Publisher's source referenced by that record: https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf . **The publisher PDF was not independently re-read during this run.** Historical recorded observations are leads, not fresh source verification or exact-sense approval.

## Four concrete conflicts requiring adjudication

| Headword / POS | Provisional placement in earlier observation | Previously recorded Oxford word/POS level | PDF page (1-based) | Editorial decision required |
|---|---|---|---|---|
| world / noun | A2 | A1 | 11 | Determine whether the intended Earth-and-people sense warrants A2 pedagogically, or replace/rebalance; do not treat word-level A1 as exact-sense proof |
| weekend / noun | B1 | A1 | 11 | Reconcile ordinary Saturday/Sunday sense and British `at the weekend` example with source label; avoid silently claiming B1 publisher backing |
| personality / noun | B2 | A2 | 7 | Verify character-traits sense, natural Myanmar meaning and independent B2 justification; distinguish sense from any specialised uses |
| prepare / verb | B2 | A1 | 8 | Verify 'make ready' sense and grammatical transitivity, independently justify B2 or propose replacement; preserve 200 slots |

These four observations are **not** new Oxford readings. Before approval, an independent reviewer must inspect the live publisher source, capture the exact sense and POS with URL, access date, publisher label (if present), and rationale for any mismatch; separately validate English definition, idiomatic Myanmar translation and original example. Record reviewer identity and evidence-bound content hashes under the release protocol. If a proposed replacement changes counts, cross-level duplication and the full 200-per-level inventory must be rechecked.

## Verified CI scope and outstanding gates

GitHub Actions run https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42768895735, head SHA `e2dd09cae9bf215e3a91030b7de7bdae70bb3151`: API job list inspected 2026-11-10; all five provisional structural and five adversarial jobs report `completed/success`. This run **predates** the current branch head `26f0e79af856be262ce1ba99d8570af712473424` and cannot certify later commits. Job conclusions are not evidence of linguistic approval, audio listening, physical iPhone Safari, hosting clearance or production deployment.

**Fail-closed disposition:** 1,000 provisional written / 0 independently approved; no complete George/Emma headword-and-example audio with genuine listening receipts established; no physical iPhone Safari or full browser/mobile acceptance established; hosting and protected-production verification not established; production deployment not confirmed. Remain staging only. Protect the existing 54 lessons, separate IELTS 1,000 bank, established production voices and privacy.
