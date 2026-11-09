# CEFR-1000 inflected-example audit — 2026-11-09

**Scope:** Staging-only, provisional shortlist `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; observed blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. This is an automated editorial triage, **not** an independent review, CEFR assessment, or publication approval.

## Reproducible structural observation

All 1,000 entries were inspected in the staging shortlist: A1=200, A2=200, B1=200, B2=200, C1=200. Each entry has a nonempty English definition, Myanmar meaning, and example. NFKC + lowercase + trim headword comparison found **zero duplicated headword strings** across all levels. This does **not** establish unique exact senses or CEFR correctness. A literal case-insensitive whole-word match between the headword and example found five examples without the *uninflected* headword. These are **not necessarily grammatical errors**; inflection is expected in natural English.

| Level | Headword | Example in provisional inventory | Source provenance | Editorial interpretation |
|---|---|---|---|---|
| A1 | hand | Please wash your hands. | `draft/A1-EDITORIAL-STARTER.json` index 172 | Plural noun *hands*; valid natural usage; check A1 learner comprehension |
| A1 | eye | I have two eyes. | `draft/A1-EDITORIAL-STARTER.json` index 173 | Plural noun *eyes*; valid natural usage |
| B2 | manage | We managed to finish the work before the deadline. | `draft/A2-C1-EDITORIAL-STARTER.json` index 101 | Past tense *managed*; review exact *manage to do* sense and level |
| B2 | destroy | The fire destroyed the old warehouse. | `draft/A2-C1-EDITORIAL-STARTER.json` index 253 | Past tense *destroyed*; valid conjugation |
| B2 | grab | She grabbed her bag and ran outside. | `draft/A2-C1-EDITORIAL-STARTER.json` index 256 | Past tense *grabbed*; valid consonant doubling |

## Release-test design recommendation

Do **not** add a fail-closed test requiring the exact uninflected headword as a substring of each example: that would reject valid morphology. Instead require independent example review with recorded reviewer identity, date, exact sense, and grammatical judgement. A nonblocking morphology-aware triage can flag examples where no inflected or exact-sense use is found. Preserve original example text until an independent reviewer signs off.

## Remaining evidence gaps

The audit did not validate source-backed CEFR classifications, exact-sense uniqueness, natural Myanmar translation, British pronunciation, or independent reviewer identity. All 1,000 remain on editorial hold and independently approved counts remain A1=0, A2=0, B1=0, B2=0, C1=0. George/Emma final audio generation and actual listening signoff, browser/mobile regression, physical iPhone Safari, GitHub Pages constraints, and confirmed deployment are not established by this report. No production changes are authorised.
