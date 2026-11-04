# CEFR-1000: Cross-level lexical-identity audit and release invariant (2026-11-05)

**Scope:** staging only; frozen provisional shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Observation date: 2026-11-05 (Singapore). Source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` read directly through GitHub connector. This is **internal structural evidence, not publisher-backed CEFR evidence or independent linguistic review**.

## Reproducible observations

- Parsed **1,000** entries. The manifest declares A1=200, A2=200, B1=200, B2=200, C1=200, with **0 independently approved** in every level.
- Grouping entries by Unicode lowercased `word` yielded **zero repeated headword strings across the entire 1,000-entry shortlist**, even when part of speech differs. This is a stronger current inventory property than merely avoiding duplicate `(word, POS)` keys, but it **does not prove** 1,000 unique lexical senses or correct CEFR allocation.
- A simple scan for uppercase initials, digits, whitespace, hyphens and apostrophes in the headword found **no entries**. This is an orthographic screening observation, not a claim that all headwords are correctly cased: the known first-person pronoun `i` is lowercased and must be resolved by a specific lexical rule.
- There are **461** definitions beginning with `to `, `a ` or `an `. This is descriptive only; these are normal definition constructions, not 461 defects.

## Fail-closed identity and CEFR review contract

1. The eventual approved manifest must have exactly 200 records for each A1/A2/B1/B2/C1 and exactly 1,000 records total. Reject unknown levels, missing IDs, blank headwords, or empty POS/sense fields.
2. Preserve both an immutable **entry ID** and a normalized **lexeme/sense ID**. A headword is not sufficient to identify a sense: homographs (e.g., `conduct` noun/verb, `permit` noun/verb) require separate POS, sense definitions, and exact-sense pronunciation.
3. Detect exact duplicate headword/POS/sense IDs across levels and raise a **human review conflict**, not an automatic deletion. Independently assess morphological relatives (`be/is/are`, `person/people`, `good/better`, `bad/worst`) without falsely treating all related forms as identical lexical entries.
4. For each entry require independent reviewer identity and dated signoff **separately** for English definition, fluent Myanmar meaning, original example, CEFR publisher source and exact sense, and pronunciation. Source records must contain URL, access/observation date, publisher, quoted or precisely identified sense and its CEFR mapping. A general dictionary page or historical WordNet sense is **not** CEFR proof.
5. Treat missing evidence, reviewer identity, mismatched sense, rejected conflict, stale source, or any `editorial_hold=true` as **release failure**. Self-authored audit notes must never set independent approval flags.
6. Audio gate: expected **4,000** distinct George/Emma × headword/example assets for 1,000 approved records. Bind audio to approved entry ID, text hash, voice, audio file hash, and actual human listening signoff. File existence, synthetic generation success, or waveform inspection is not listening verification.
7. Require actual browser/mobile regression evidence, **physical iPhone Safari** reviewer evidence, GitHub Pages hosting clearance, production deployment verification, and preservation checks for 54 lessons, the separate IELTS 1,000-word bank, and existing production George/Emma audio. Do not infer these from structural CI.

## Suggested adversarial test fixtures

- Duplicate exact sense at B1 and B2: reject.
- Same spelling with distinct noun/verb sense but no explicit sense ID: reject as ambiguous.
- `i` as first-person pronoun with lowercase orthography: reject pending correction; retain lowercase article `a`.
- Two reviewer fields populated by the same author as the initial editorial work: reject as not independent.
- CEFR URL exists but points to a general headword page without the claimed exact sense/level: reject.
- One missing Emma example audio or one audio hash mismatch: reject.
- All 4,000 audio files present but zero listening evidence: reject.
- All structural CI jobs pass but no physical iPhone Safari evidence: reject.

## Status and provenance

This audit did not alter the shortlist, review flags, existing production, or main branch. No new publisher-backed CEFR lookup, human-independent approval, audio listening, device QA, or deployment was established here. Earlier CI run `41801157929` pertains to a prior commit and is **not** a CI conclusion for this document. The project remains staging-only and release-blocked. Next high-value work: implement the identity/sense invariant as executable CI with negative fixtures, then collect independently attributable publisher sense-level evidence.
