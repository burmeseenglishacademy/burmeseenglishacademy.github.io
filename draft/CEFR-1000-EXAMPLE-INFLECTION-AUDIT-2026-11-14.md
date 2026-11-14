# CEFR-1000 example-inflection audit — 2026-11-14

**Status: staging-only, machine-assisted editorial triage; NOT independent review or approval.**

## Scope and reproducibility

Examined all 1000 entries in `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` at blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551` on branch `cefr-5000-bilingual-qa-staging` (observation date 2026-11-14). Per-level first-pass counts: A1 200; A2 200; B1 200; B2 200; C1 200. Independently approved: 0 at every level. These are provisional written entries, not signed-off entries.

A literal case-insensitive whole-word search for each headword within its example found **five apparent misses**, listed below. Manual examination shows that each example uses an ordinary inflected form; therefore these are **false positives for an exact-token check**, not demonstrated grammar errors. A validator that requires an exact surface headword would incorrectly reject them. Conversely, accepting arbitrary substrings could miss real example/sense mismatches.

| Global zero-based index | Level | Headword | Existing example | Original source path | Source index | Source blob SHA |
|---:|---|---|---|---|---:|---|
| 170 | A1 | hand | Please wash your hands. | draft/A1-EDITORIAL-STARTER.json | 172 | ff1e93f60828ef2f94c9146522ce94075183b0ae |
| 171 | A1 | eye | I have two eyes. | draft/A1-EDITORIAL-STARTER.json | 173 | ff1e93f60828ef2f94c9146522ce94075183b0ae |
| 616 | B2 | manage | We managed to finish the work before the deadline. | draft/A2-C1-EDITORIAL-STARTER.json | 101 | b04dd85db5cfae131c25aa4c73109778991b6fdc |
| 654 | B2 | destroy | The fire destroyed the old warehouse. | draft/A2-C1-EDITORIAL-STARTER.json | 253 | b04dd85db5cfae131c25aa4c73109778991b6fdc |
| 657 | B2 | grab | She grabbed her bag and ran outside. | draft/A2-C1-EDITORIAL-STARTER.json | 256 | b04dd85db5cfae131c25aa4c73109778991b6fdc |

## Editorial observations (unapproved)

- A1 **hand → hands** and **eye → eyes**: regular plural nouns. Original examples are natural, simple English; keep plural inflection eligible, but an independent reviewer must verify the intended noun sense and fluent Myanmar explanation.
- B2 **manage → managed**: regular past-tense verb. The construction *managed to finish* conveys successful completion despite difficulty; check that the Myanmar meaning reflects this exact sense rather than general management of people/resources. Do not infer a CEFR level from inflection.
- B2 **destroy → destroyed** and **grab → grabbed**: regular past-tense verbs; the doubled final consonant in *grabbed* is expected. Review sense and Myanmar meaning separately, and ensure eventual speech audio reads the inflected example as written.

## Additional automated checks

- Case-insensitive exact headword duplicates: **0** (does not establish sense-level uniqueness; `a`/`an` still need semantic editorial adjudication).
- Example sentences lacking terminal `.`, `!`, or `?`: **0**.
- Non-ASCII headword forms: **0** (not evidence of canonical capitalization; A1 `i` remains an identified issue).

## Recommended fail-closed handling

1. Distinguish **lexical lemma**, **attested surface form**, and **exact sense**; do not mark an entry approved merely because a morphological matcher succeeds.
2. Store reviewer-confirmed example headword spans or accepted inflected forms; require human-independent signoff on sense, CEFR evidence, English, Myanmar, and example before release.
3. Add regression fixtures for `hands`, `eyes`, `managed`, `destroyed`, `grabbed` and a deliberately unrelated example that must fail. A form matcher alone is not a release gate.
4. Preserve source-path/index/blob provenance; source URLs and dated exact-sense CEFR dictionary observations remain required independently and are **not provided by this mechanical audit**.
5. Keep all 1,000 entries on editorial hold. George/Emma final headword+example audio, real listening signoff, physical iPhone Safari, browser/mobile regression, hosting and production deployment remain unverified and blocking.

No source entry, review flag, production content, or release manifest is changed by this document.
