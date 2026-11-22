# CEFR-1000 example/headword inflection and exact-token QA audit — 2026-11-22

**Scope:** Approved project size is 1,000 total provisional entries (A1/A2/B1/B2/C1: 200 each), **not** the retired 5,000-word plan. This is a staging-only author-side structural investigation, **not** independent linguistic review, CEFR evidence, or approval.

## Reproducible source provenance
- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, observed 2026-11-22 on `cefr-5000-bilingual-qa-staging`.
- Review tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`, observed 2026-11-22.
- Source URLs: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json and https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json
- Method: case-insensitive Unicode-letter-boundary exact-token search of each `example_sentence` for its `word`, followed by manual author-side inspection of the five nonmatches. This is an engineering heuristic, not proof of example correctness.

## Findings
All 1,000 entries contain an example with terminal `.`, `!` or `?`. There are **zero duplicate lowercased exact headword strings** across all levels, but this does **not** establish deduplication of grammatical variants, lemmas or exact senses (e.g. `a`/`an`). Five examples do not contain the exact orthographic headword as a separate token:

| Level | Headword | Existing example | Preliminary interpretation | Independent reviewer action |
|---|---|---|---|---|
| A1 | hand | Please wash your hands. | Regular plural `hands`; semantically plausible | Verify noun sense and natural Myanmar wording; ensure headword audio says singular `hand` while example audio reads plural |
| A1 | eye | I have two eyes. | Regular plural `eyes`; semantically plausible | Verify singular lemma/plural example relationship and Myanmar plural interpretation |
| B2 | manage | We managed to finish the work before the deadline. | Past-tense `managed`; semantically plausible | Check intended `succeed in doing` sense, grammar, Myanmar translation and source-backed exact-sense CEFR |
| B2 | destroy | The fire destroyed the old warehouse. | Past-tense `destroyed`; semantically plausible | Check tense, transitivity, natural Myanmar rendering and CEFR evidence |
| B2 | grab | She grabbed her bag and ran outside. | Past-tense `grabbed`; semantically plausible | Check doubling of final consonant, context-appropriate Myanmar rendering and CEFR evidence |

**Important:** These are *not* confirmed errors and must not be automatically rewritten to insert exact headword forms. Exact-token-only QA would falsely reject legitimate inflection. Conversely, substring-only matching could accept unrelated words (e.g. `a` in `bag`). A robust future validator should check a reviewed lemma/inflection map, record any accepted inflected forms explicitly, and fail closed for unexplained mismatches. Do not silently normalize proper nouns, homographs or grammatical senses.

## Release implications and next actions
1. Assign the five examples to genuinely independent English, Myanmar and CEFR reviewers; preserve reviewer identities, evidence URLs, observation dates, decisions and signed provenance in a separate approved manifest, not by changing these pending tasks to approved.
2. Add negative structural tests: unrelated substring must fail, valid inflected form must require an explicit reviewed allowance, and changing example text after signoff must invalidate audio/listening attestations.
3. Maintain exactly 200 independently validated, deduplicated headword/sense records per CEFR level before release. A lexical duplicate check alone is insufficient.
4. For George/Emma, verify **both** headword and original example recordings and actually listen to each; morphology mismatch must not be “fixed” by using headword TTS for example text.
5. No inference of physical iPhone Safari tests, hosting clearance, deployment, or preservation of 54 production lessons, separate IELTS bank and existing audio is made here.

## Truthful status
Written first-pass provisional inventory: A1=200, A2=200, B1=200, B2=200, C1=200. Independently approved: A1=0, A2=0, B1=0, B2=0, C1=0. Required final 4,000 George/Emma headword+example audio items with genuine listening signoff: **not verified**. Physical iPhone Safari, browser/mobile regression, GitHub Pages hosting, preserved production assets and live deployment: **not verified**. Historical Actions run `44811286785`: A2/B1/B2/C1 recorded failure; A1 metadata inconsistent (in progress with success conclusion). No current-commit CI success is claimed. **Release remains blocked; staging only.**
