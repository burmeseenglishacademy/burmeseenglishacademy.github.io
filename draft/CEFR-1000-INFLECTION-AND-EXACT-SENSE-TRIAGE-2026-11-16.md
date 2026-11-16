# CEFR-1000: inflection-aware example audit and exact-sense triage

Observed: 2026-11-16 (Singapore). Scope: **1,000 provisional entries only**, A1–C1 (200 per level). Status: **editorial research, NOT independent review, NOT CEFR approval**.

## Provenance and method

Read `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` from branch `cefr-5000-bilingual-qa-staging`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. For each of the five level partitions, checked presence of English definition, Myanmar meaning and example sentence; performed a *case-insensitive exact surface-token* match of the headword in the example. This deliberately narrow diagnostic does **not** perform lemmatisation, syntactic parsing, word-sense disambiguation, or grammar assessment.

| Level | Provisional entries | Missing any of three first-pass fields | Exact surface-token mismatches | Independently approved |
| --- | ---: | ---: | ---: | ---: |
| A1 | 200 | 0 | 2 | 0 |
| A2 | 200 | 0 | 0 | 0 |
| B1 | 200 | 0 | 0 | 0 |
| B2 | 200 | 0 | 3 | 0 |
| C1 | 200 | 0 | 0 | 0 |
| **Total** | **1,000** | **0** | **5** | **0** |

These figures describe field presence and surface matching, **not** verified lexical quality, correctness of CEFR labels or genuine human signoff. Zero missing fields does not imply zero errors.

## Five flagged examples: all explainable by inflection

| Level | Headword (POS) | Original provisional example | Editorial finding |
| --- | --- | --- | --- |
| A1 | hand (noun) | Please wash your hands. | Regular plural **hands**; example represents the body-part sense. |
| A1 | eye (noun) | I have two eyes. | Regular plural **eyes**; example represents the organ-of-sight sense. |
| B2 | manage (verb) | We managed to finish the work before the deadline. | Past tense **managed**; example targets *manage to + infinitive* (succeed), not managerial control. |
| B2 | destroy (verb) | The fire destroyed the old warehouse. | Past tense **destroyed**; destructive-action sense is plausible. |
| B2 | grab (verb) | She grabbed her bag and ran outside. | Past tense **grabbed**; doubled final consonant. |

**Do not auto-rewrite or fail release solely on these five mismatches.** A strict token-matching validator would incorrectly flag ordinary grammatical examples. Conversely, accepting any inflected form without contextual checks can mask wrong senses. Any future example check should report exact-match and morphology-aware results separately, and require human semantic and grammar review.

## Priority sense and level conflicts requiring independent evidence

1. **B2 `manage`**: `manage to finish` is the success/achievement construction, not the sense of managing staff or resources. Require a source that identifies *this construction* and supports B2 (or re-level it if independent CEFR evidence differs).
2. **C1 `signature`**: current definition/example concern a handwritten name on a form. Do not infer C1 from another advanced meaning such as a distinctive characteristic or technical signature. Independently verify this everyday sense's CEFR level; a lower-level classification is a plausible risk, not a proven correction.
3. **B2 `prepare`**: current sense is everyday readiness (`prepare the documents`). Verify whether B2 is supported for this specific sense rather than a specialised construction.
4. **C1 `copyright`**: legal-right sense may be domain-specific; source-backed CEFR evidence for this sense remains absent.
5. **C1 `divine`**: religious adjective in `divine figure` must not be conflated with the verb *divine* (infer/guess) or informal praise. Check the selected sense and its level.
6. **A1 `i`**: stored lowercase lemma conflicts with standard uppercase first-person pronoun `I` used in the example. Keep on editorial hold until lemma normalisation and stable task identity are explicitly reconciled; do not silently mutate the shortlist or intake provenance.

These are **editorial risk hypotheses** grounded in the actual provisional entries, not independently sourced CEFR findings.

## Independent reviewer evidence required

For each flagged item: record a stable task ID, exact definition/sense and part of speech, original example, fluent Myanmar equivalent, externally observed dictionary/learner profile URL, access date, the precise evidence excerpt or paraphrase permitted by source terms, and a separate reviewer decision/signature. Dictionary grammar evidence alone does not establish a CEFR band. If the source is a general dictionary without an explicit exact-sense CEFR label, record **CEFR evidence unresolved**.

No external source pages were consulted for this diagnostic; source URLs and observation dates must not be fabricated. No independent review, pronunciation listening, physical iPhone test, audio generation, GitHub Actions success or production deployment is asserted. Maintain staging-only release block and protect 54 lessons, the separate IELTS bank and existing George/Emma production assets.
