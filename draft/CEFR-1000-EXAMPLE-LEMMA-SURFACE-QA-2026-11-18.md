# CEFR-1000 example surface-form and lemma QA — 2026-11-18

**Status: staging editorial investigation only; no independent signoff.** Scope is the user-approved 1,000 entries (200 each A1/A2/B1/B2/C1), not the superseded 5,000-word plan.

## Provenance and method
- Provisional shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, read 2026-11-18.
- Independent intake tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`, read 2026-11-18.
- Mechanically compared each headword with its provisional example using a case-insensitive, word-boundary **exact surface-form** match; this is **not** lemmatization, grammar checking or linguistic verification. All 1,000 provisional entries were scanned.
- This is internal inventory evidence, not external CEFR source evidence; no dictionary CEFR claim is made.

## Five exact-surface mismatches requiring context-sensitive treatment

| Level | Headword | Existing example | Editorial interpretation |
|---|---|---|---|
| A1 | hand | Please wash your hands. | Plural `hands` is the ordinary inflected form; do not mark as missing vocabulary |
| A1 | eye | I have two eyes. | Plural `eyes` is grammatical and appropriate for `two` |
| B2 | manage | We managed to finish the work before the deadline. | Past-tense `managed`; independently verify the intended 'succeed in doing' sense and level |
| B2 | destroy | The fire destroyed the old warehouse. | Past-tense `destroyed`; independently verify sense and level |
| B2 | grab | She grabbed her bag and ran outside. | Past-tense `grabbed`; independently verify sense and level |

**Observed mismatch counts:** A1 2/200, A2 0/200, B1 0/200, B2 3/200, C1 0/200; 5/1,000 total. These are not five errors: they are five cases where an exact-string-only validator would falsely reject grammatical inflection. Conversely, simply accepting substring matches could falsely accept an unrelated word. A release validator should use a documented lemma/inflection policy and independently review sense-in-context.

## Release safeguards
1. Do not automatically rewrite grammatical examples just to match the citation headword; retain reviewer control.
2. Fail closed if an example cannot be linked to the intended headword **and exact sense** by independent editorial evidence. A lexical morphology exception is not itself approval.
3. Require per-entry reviewer identity, dated source-backed exact-sense CEFR decision, independent English/Myanmar/example decisions and genuine audio-listening evidence before release.
4. Require exactly 200 deduplicated approved senses per level, complete George/Emma headword and example audio, physical iPhone Safari evidence, mobile/browser regression, hosting clearance and confirmed deployment.
5. No production or approval flags were changed. The known A1 lowercase `i` headword and cross-level sense risks remain unresolved.

## Truthful inventory state
| Level | Provisional written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

Final-list audio generation and real George/Emma listening signoff: not verified. Browser/mobile and physical iPhone Safari: not verified. Current-commit Actions parallel job conclusions: not verified. GitHub Pages limits and production deployment: not cleared. **DO NOT MERGE OR PUBLISH.**
