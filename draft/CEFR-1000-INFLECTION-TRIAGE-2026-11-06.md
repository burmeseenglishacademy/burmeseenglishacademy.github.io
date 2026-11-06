# CEFR-1000 inflection-aware example triage — 2026-11-06

## Scope and provenance
Read-only audit of `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` at GitHub blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, inspected 2026-11-06. This is a staging editorial audit, **not** a publisher CEFR claim, independent linguistic review, or release approval. The independent review task file returned zero content through the connector; do not interpret this as evidence of completed reviews.

## Counts from parsed entries
| Level | Provisional entries | Nonempty English/Myanmar/example | Independently approved | Exact-surface example mismatches |
|---|---:|---:|---:|---:|
| A1 | 200 | 200 | 0 | 2 |
| A2 | 200 | 200 | 0 | 0 |
| B1 | 200 | 200 | 0 | 0 |
| B2 | 200 | 200 | 0 | 3 |
| C1 | 200 | 200 | 0 | 0 |
| Total | 1000 | 1000 | 0 | 5 |

These are completeness and literal-match counts, **not** correctness, genuine distinct-sense counts, or independently checked counts. No CEFR publisher URLs were validated during this audit.

## Five apparent missing-headword examples: manual diagnosis
- A1 **hand** (noun), “Please wash your hands.” The plural **hands** is a normal inflected form of the target noun; the exact-form heuristic produces a false positive. Myanmar first-pass gloss: “လက်”.
- A1 **eye** (noun), “I have two eyes.” The plural **eyes** is normal; another false positive. Myanmar first-pass gloss: “မျက်လုံး”.
- B2 **manage** (verb), “We managed to finish the work before the deadline.” Past tense **managed** expresses the proposed succeed-despite-difficulty sense; exact-form heuristic false positive.
- B2 **destroy** (verb), “The fire destroyed the old warehouse.” Past tense **destroyed** fits the proposed damage-irreparably sense; exact-form heuristic false positive.
- B2 **grab** (verb), “She grabbed her bag and ran outside.” Past tense **grabbed** fits the proposed sudden-taking-hold sense; exact-form heuristic false positive.

These examples appear grammatically plausible on self-audit but remain unverified. The flagged surface mismatches should **not** be auto-rewritten into ungrammatical examples merely to satisfy literal matching. The correct next safeguard is a POS-sensitive lemma matcher (plural noun, verb inflections, irregular forms) with a separate human exception queue and adversarial tests for substring and homograph errors. A lexical matcher cannot independently certify exact sense, CEFR level, natural Myanmar, or original example quality.

## Release gates
All 1,000 remain editorial hold; independently verified English, Myanmar, examples, and exact-sense publisher CEFR evidence = **0** observed approvals at every level. British George/Emma final-list headword/example audio generation and real listening signoff remain unverified; physical iPhone Safari, browser/mobile regression, GitHub Pages limits and confirmed production deployment remain unverified. Do not merge or publish. Preserve 54 lessons, separate IELTS 1,000 vocabulary bank, established production audio, and privacy protections.

## Next actions
Implement lemma-aware diagnostics without weakening fail-closed release checks; obtain independent human editorial signoff and publisher URL/date/sense evidence; inspect parallel five-lane GitHub Actions jobs on the **new** commit before claiming CI pass. This report itself is not a release gate pass.
