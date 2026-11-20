# CEFR-1000 A1 pronoun “I”: orthography and display audit (author research only)

Observed on: 2026-11-21 (Singapore). Scope: user-approved **1,000 total** (200 per A1–C1), staging only.

## Direct observations from pinned staging inventory
- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- A1 entry `word: "i"`, `part_of_speech: "pronoun"`, `english_definition: "The person who is speaking or writing."`, `burmese_meaning: "ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)"`, `example_sentence: "I am a student."`.
- Original source: `draft/A1-EDITORIAL-STARTER.json`, source index **3**, source blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- Corresponding intake task: `CEFR1000-A1-0004` in `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, source blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`. Its independent-review fields remain pending.
- The **headword** is lower-case `i` while its own example correctly uses capital `I`. This is a concrete orthography/display discrepancy; it is not evidence of a wrong CEFR assignment.

## Editorial candidate, not approved
For the English first-person singular subject pronoun, display the headword as **I** (capital letter), preserving the existing exact sense and example until independent review. A distinct normalized search key `i` can be retained for case-insensitive lookup, but must not override the canonical displayed spelling or British TTS text. A production implementation should avoid changing every headword to title case: ordinary words such as `house` remain lower-case, and `I` is a specific exception.

Myanmar note: `ကျွန်တော်` and `ကျွန်မ` are context- and speaker-dependent equivalents, not a single mandatory translation. Independent Myanmar review should check register and learner clarity, and whether `ငါ` belongs as a contextual alternative rather than a default gloss.

## External source leads — NOT independently checked in this run
- Cambridge English Dictionary, `I`: https://dictionary.cambridge.org/dictionary/english/i
- Cambridge Learner's Dictionary, `I`: https://dictionary.cambridge.org/dictionary/learner-english/i

These are **research leads**, not asserted exact-sense/CEFR observations. No CEFR level is certified by this note. An independent reviewer must open the actual entry, record the exact relevant sense and any explicit CEFR label, observation date, source URL, and signoff.

## Release-safe next actions
1. Independent English reviewer checks canonical pronoun spelling, definition, example, and exact-sense CEFR evidence.
2. Independent fluent Myanmar reviewer verifies translation register and contextual suitability.
3. After independent approval, change only the approved final manifest/display pipeline with provenance preserved; verify headword search normalization, UI capitalization and George/Emma headword speech.
4. Keep the provisional shortlist and all reviewer flags unchanged until real independent signoff; no generated audio or listening QA is implied here.

**Status:** AUTHOR-RESEARCH / EDITORIAL HOLD. Not independent verification, not a release approval, not a production change.
