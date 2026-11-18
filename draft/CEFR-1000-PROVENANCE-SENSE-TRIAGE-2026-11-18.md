# CEFR-1000 provisional provenance and sense-risk triage — 2026-11-18

**Status: STAGING RESEARCH ONLY; NOT AN INDEPENDENT REVIEW OR RELEASE APPROVAL.**

## Reproducible input provenance

- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Intake tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- Observed on: 2026-11-18 (UTC). Counts are calculated from the actual JSON arrays, not only their declared metadata.

| Level | Provisional entries | First-pass EN+Myanmar+example present | Independently approved | Entries with all three legacy source-text fields empty |
|---|---:|---:|---:|---:|
| A1 | 200 | 200 | 0 | 200 |
| A2 | 200 | 200 | 0 | 200 |
| B1 | 200 | 200 | 0 | 200 |
| B2 | 200 | 200 | 0 | 200 |
| C1 | 200 | 200 | 0 | 200 |

The last column describes only `source_english`, `source_burmese` and `source_level` fields. **It does not prove that the original source file or its pinned blob is unavailable.** The source path, index and blob SHA must be consulted before judging evidence. Neither populated first-pass fields nor a source blob constitutes independent CEFR evidence.

## Priority exact-sense editorial queue (C1)

1. **signature**, noun, handwriting sense (C1 task): Cambridge learner-dictionary evidence previously collected in `draft/CEFR-1000-C1-SIGNATURE-NEUTRAL-SENSE-EVIDENCE-2026-11-18.md` identifies the handwritten-name sense as B1. Do not silently retain C1 or transfer the CEFR label from a different sense. Resolve via independently reviewed replacement or level reconciliation while preserving 200/level.
2. **conversion**, noun, change-process sense: prior source investigation in `draft/CEFR-1000-C1-CONVERSION-COPYRIGHT-SENSE-RESEARCH-2026-11-18.md` records a Cambridge C2 label for the relevant noun sense. Its related verb's B2 label does not license a C1 noun label. Require an independently sourced exact-sense decision.
3. **copyright**, noun, legal right: earlier research found no explicit CEFR label for the cited noun entry. A law-topic adjective label is not evidence for the noun's level. Require noun-specific CEFR evidence or a documented alternative assessment, not a fabricated dictionary level.
4. **neutral**, adjective, impartial sense: earlier Cambridge evidence supports C1 for the impartial sense, but the original example, Myanmar wording and exact sense still require independent signoff.
5. **divine**, adjective, relating to a god: scrutinise potential mismatch between theological/religious and colloquial 'excellent' senses; do not substitute the latter's CEFR evidence.
6. **treasury**, noun, government finance department: distinguish from money reserves and physical storehouse senses, and check whether a capitalised government institution is intended; avoid treating a proper institutional name as generic headword evidence.
7. **warrant**, noun, legal authorisation document: distinguish from verb 'justify' and other noun senses; legal topic context alone does not establish C1.
8. **upgrade**, verb, improve/replace with newer version: check independently whether this common technological sense is actually C1 rather than a lower level.

Items 5–8 are **triage hypotheses, not sourced CEFR findings**. They require dated dictionary URLs, exact sense, part of speech, British usage, independently checked fluent Myanmar, original grammatical examples and reviewer identity/signoff before decisions.

## Next safe actions

Keep the shortlist and independent-review tasks unchanged. For each queued sense, record authoritative dictionary URL, observation date, exact part of speech and sense identifier, explicit CEFR label if present (or state 'not supplied'), candidate Myanmar phrasing and original example, then assign to a genuinely independent reviewer. Resolve cross-level displacement with global deduplication and exactly 200 entries per level before any release manifest. George/Emma headword+example audio, genuine listening, browser/mobile and physical iPhone Safari QA, GitHub Pages constraints and production preservation remain **unverified or incomplete**; no launch is authorised.
