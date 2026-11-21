# CEFR-1000: however / furthermore exact-sense CEFR audit — 2026-11-21

**Status:** author research, NOT independent review or approval. Staging only. No edits to shortlist, review flags, or production.

## Provenance
Repository `burmeseenglishacademy/burmeseenglishacademy.github.io`; branch `cefr-5000-bilingual-qa-staging`.
Provisional shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; review-task Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
Both entries trace to source blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`.
Source observations performed **2026-11-21**; dictionary sense labels are source claims, not an independent reviewer decision.

## A2: however — evidence supports the specified sense, with disambiguation required
- Review task `CEFR1000-A2-0231`; source index **285**; provisional POS **adverb**.
- Existing English definition: “Used to introduce a fact that contrasts with what was just said.”
- Myanmar: **သို့သော်၊ ဒါပေမဲ့**.
- Original example: “The room was small; however, it was comfortable.”
- Cambridge Learner's Dictionary labels **however adverb (COMPARING)** **A2**, explaining the contrasting/surprising fact use. This is aligned with the provisional example and definition.
- **Different senses are NOT interchangeable:** Cambridge labels `however cold/difficult/slowly` (degree) **B2**; its general dictionary additionally labels `however` in the 'in whatever way' sense **C2**. The A2 example uses neither.
- The semicolon + connective adverb + comma is grammatical; `however` should not be treated as a coordinating conjunction equivalent to `but`. Cambridge English Grammar Today warns against conjunction-like substitutions.
- Myanmar nuance: **သို့သော်** is formal written contrast; **ဒါပေမဲ့** is conversational. Independent fluent reviewers should judge whether both are pedagogically suitable at A2 and whether the example context needs a natural Burmese sentence translation.
- Sources: https://dictionary.cambridge.org/dictionary/learner-english/however ; https://dictionary.cambridge.org/dictionary/english/however ; https://dictionary.cambridge.org/grammar/british-grammar/conjunctions-contrasting .

## C1: furthermore — exact-sense level conflict
- Review task `CEFR1000-C1-0834`; source index **278**; provisional POS **adverb**.
- Existing English definition: “Used to add another reason or piece of information.”
- Myanmar: **ထို့အပြင်**.
- Original example: “The plan is costly; furthermore, it will take months to finish.”
- Cambridge Advanced Learner's Dictionary labels the **formal addition / stronger additional point** sense **B2**, not C1. The existing definition and example demonstrate that B2 sense; no C1-specific meaning is established by the record.
- The example is grammatical, with a semicolon joining two independent clauses and a comma after the connective. It is **not evidence of C1** merely because the topic is a plan.
- Myanmar **ထို့အပြင်** is a plausible formal connector but should be independently checked against `furthermore`'s emphasis and register. A more natural spoken Burmese alternative may lose the formal register.
- Source: https://dictionary.cambridge.org/dictionary/english/furthermore (also https://dictionary.cambridge.org/us/dictionary/english/furthermore).

## Required independent adjudication
1. Confirm A2 `however` is strictly the contrasting discourse-adverb sense, not degree/way, with source-backed English/Myanmar/example reviews.
2. Decide whether to relocate, replace, or re-sense C1 `furthermore` without silently changing the fixed **200-per-level** target. Replacements need their own sourced evidence and human-independent review.
3. Preserve the provisional records and `editorial_hold=true` until signoff. Do not mark any review field true based on this audit.
4. After adjudication, regenerate a candidate manifest and re-run the fail-closed release gate, level-specific CI, full audio/listening and device gates. This document does not satisfy any of those gates.

**Inventory context:** 200 provisional per level, 1,000 total; **0 independently approved** per level at observation. No audio, physical iPhone Safari, deployment, or CI execution is claimed here.
