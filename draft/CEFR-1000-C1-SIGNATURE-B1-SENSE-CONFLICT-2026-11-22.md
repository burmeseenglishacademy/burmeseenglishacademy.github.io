# CEFR-1000 C1 `signature` exact-sense placement audit — 2026-11-22

**Scope:** User-approved 1,000-total shortlist only (A1/A2/B1/B2/C1 = 200 each). **Status:** AUTHOR RESEARCH / EDITORIAL HOLD; NOT independent review, not a CEFR signoff, not a production change.

## Reproducible provisional record and provenance

- Task: `CEFR1000-C1-0804`; headword `signature`, noun, provisionally **C1**.
- Definition: “A person's name written in their own handwriting.”
- Myanmar first pass: `လက်မှတ်ရေးထိုးချက်`.
- Original provisional example: “Please add your signature at the bottom of the form.”
- Source: `draft/A2-C1-EDITORIAL-STARTER.json`, index 75, blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`.
- Provisional shortlist blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; independent-review task file blob: `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- Repository: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io ; branch `cefr-5000-bilingual-qa-staging`.
- Observation date for external references: **2026-11-22**. Dictionary labels are externally published evidence, not human-independent editorial signoff.

## Exact-sense evidence (observed 2026-11-22)

1. Cambridge Learner's Dictionary: https://dictionary.cambridge.org/dictionary/learner-english/signature — **B1**, countable noun, the individual's distinctive handwritten name.
2. Cambridge Essential British English: https://dictionary.cambridge.org/dictionary/essential-british-english/signature — **B1**, same handwritten-name sense.
3. Cambridge Advanced Learner's Dictionary: https://dictionary.cambridge.org/dictionary/english/signature — the **NAME** noun sense is explicitly **B1**; separate ungraded senses include a characteristic identifying a person or thing, and the formal act of signing.

**Conflict:** the provisional C1 definition and example select the ordinary **NAME** sense labelled B1 by all three Cambridge references. This is stronger than a general headword-level mismatch: the exact sense aligns. It is **not** evidence that every possible sense of `signature` is B1. Do not relabel the existing record as a more advanced technical sense to preserve C1 without a new definition, example, source-backed CEFR label and independent adjudication.

## English, Myanmar and example editorial proposals (NOT APPROVED)

- Candidate English definition: “A person's name written by that person in a usual personal style, often to confirm agreement or identify the signer.”
- Myanmar candidate: `လက်မှတ်၊ ကိုယ်တိုင်ရေးထိုးထားသော အမည်လက်မှတ်`. The existing `လက်မှတ်ရေးထိုးချက်` may suggest the **act of signing**, not the physical written-name mark; an independent fluent Myanmar reviewer must resolve natural register and avoid conflating `signature` with `signing`.
- New original example: “Please put your signature below your printed name.”
- Candidate Myanmar example: `ပုံနှိပ်ရေးထားတဲ့ သင့်နာမည်အောက်မှာ လက်မှတ်ထိုးပေးပါ။` This is author-written and requires independent Myanmar, English and grammar review.
- Countability: the intended sense is a countable noun (`a signature`, `signatures`). Distinguish from formal uncountable `awaiting signature`, adjective `signature dish`, and technical identifying `chemical signature`. None of those alternatives is established as C1 by these three sources.

## Required disposition and safeguards

1. Independent CEFR reviewer confirms the exact noun sense, source labels, publication context, and appropriate final level; independently check English, Myanmar, original example and pronunciation.
2. If a move C1 → B1 is authorised, prepare a **balanced** 200/200/200/200/200 transaction with a separately reviewed replacement C1 item and deduplicated headword/sense checks. Do not mutate the provisional inventory or reviewer decisions in this research pass.
3. Preserve original task ID, source index, blob and evidence URLs in the adjudication trail; migration must not silently renumber evidence or count self-review as independent.
4. Keep all 1,000 editorial holds and release gate closed pending real independent approvals, 4,000 George/Emma headword/example recordings and listening attestations, browser/mobile and physical iPhone Safari QA, hosting and protected-asset checks, and confirmed production deployment.

## CI observation, not a current pass

Requeried historical GitHub Actions run [44811286785](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44811286785) on 2026-11-22: jobs A2 `136548182394`, B1 `136548182133`, B2 `136548182423`, C1 `136548182486` reported completed/failure; A1 `136548182598` reported inconsistent in_progress/success. The connector returned **no pull-request-associated workflow runs** for preceding commit `8fb4b31eec2e6866d187ce5f0a57d319663e2755`. These historical results do not prove that current parallel structural tests passed; fresh job logs/conclusions must be verified separately.

**Truthful staging count:** first-pass written entries A1=200, A2=200, B1=200, B2=200, C1=200; independently approved A1=0, A2=0, B1=0, B2=0, C1=0. No new audio or real-device signoff evidenced. **Release blocked; staging only.**
