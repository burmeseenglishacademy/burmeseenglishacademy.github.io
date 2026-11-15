# CEFR-1000 staging: observed evidence-gap inventory (2026-11-16)

**Scope:** approved 1,000-total A1–C1 plan only. **Status:** editorial triage; NOT independent review, NOT permission to release.

## Reproducible observation
Inspected `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` on `cefr-5000-bilingual-qa-staging`, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, on 2026-11-16 (Singapore date). Counts below are from the actual 1,000 `entries` array, not merely the file's declared counters.

| Level | First-pass written | Editorial holds | Independently approved | Missing explicit sense_id | Empty source_level | Empty source_english | Empty source_burmese |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 0 | 200 | 200 | 200 | 200 |
| A2 | 200 | 200 | 0 | 200 | 200 | 200 | 200 |
| B1 | 200 | 200 | 0 | 200 | 200 | 200 | 200 |
| B2 | 200 | 200 | 0 | 200 | 200 | 200 | 200 |
| C1 | 200 | 200 | 0 | 200 | 200 | 200 | 200 |
| **Total** | **1,000** | **1,000** | **0** | **1,000** | **1,000** | **1,000** | **1,000** |

**Important distinction:** the shortlist has `source_path`, `source_index`, and `source_blob_sha` for its original draft provenance. Blank `source_english`, `source_burmese`, and `source_level` fields do not prove that the original draft lacked these values; they do mean that the shortlist does not itself carry independent exact-sense source evidence. The missing `sense_id` field is an identity blocker for a deduplicated headword/sense release manifest.

## Specific editorial issues requiring human adjudication

1. **A1 indices 0–1, `a` and `an`**: different surface forms of the English indefinite article; review whether the 200-unit target counts canonical lexical entries or spelling forms. Do not remove or replace automatically. Prior staging research: `draft/CEFR-1000-A1-A-AN-LEXEME-DEDUP-RESEARCH-2026-11-15.md`.
2. **A1 index 3, `i`**: lowercase headword is orthographically inappropriate for the first-person singular English pronoun, which is conventionally written **I**. The example already uses `I`. A proposed correction requires a traceable editorial decision and consistency checks; do not silently alter the source.
3. **All 1,000 entries**: exact-sense IDs and source-backed CEFR observations must be gathered and independently evaluated. Historical WordNet-derived data, proper names, or source-file CEFR labels must never be treated as proof of a CEFR assignment.
4. **Deduplication interpretation**: no exact NFKC-casefold headword duplicates were observed across the 1,000 entries in this pass. This does **not** establish distinct lexical senses: `a/an` demonstrates why orthographic uniqueness is insufficient.

## Next evidence-gathering protocol

For each entry, retain original draft path/index/blob SHA, proposed canonical lemma, part of speech, exact sense definition, authentic source URL, source title/publisher, observation timestamp with timezone, exact supporting quotation or paraphrased finding, CEFR source type (explicit sense-level vs inference), and unresolved ambiguities. Record independent English, fluent Myanmar, example-grammar, and CEFR reviewer identities and signed outcomes separately. Unsubstantiated or conflicting levels remain held. Never copy self-assessed outcomes into independent approval fields.

## Release readiness

The observed inventory is a **first pass**, not a final deduplicated approved manifest. Audio generation, actual listening attestations for both British George/Emma headwords and examples, browser/mobile regression, physical iPhone Safari evidence, GitHub Pages limits, CI for the release SHA, production-preservation verification and deployment confirmation remain **not established by this audit**. Production and main must remain unchanged.

No approval flags or original shortlist entries were modified by this report.
