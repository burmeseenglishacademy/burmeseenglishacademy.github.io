# CEFR-1000 source-field coverage and CEFR evidence gate — 2026-11-22

**Scope:** User-approved 1,000-total A1–C1 vocabulary, 200 per level; staging only. **Author-side mechanical audit, NOT independent review.**

## Reproducible input and provenance

- Repository: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io
- Branch: `cefr-5000-bilingual-qa-staging`
- Input: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Separate independent-review task input: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- Observed 2026-11-22 (UTC+08:00). The counts below come from parsing the complete shortlist JSON, not the metadata counters alone.

## Exact mechanical findings

| Level | Provisional entries | Blank `source_level` | Blank `source_english` | Blank `source_burmese` | Editorial holds | Release approved |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 200 | 200 | 200 | 0 |
| A2 | 200 | 200 | 200 | 200 | 200 | 0 |
| B1 | 200 | 200 | 200 | 200 | 200 | 0 |
| B2 | 200 | 200 | 200 | 200 | 200 | 0 |
| C1 | 200 | 200 | 200 | 200 | 200 | 0 |
| **Total** | **1000** | **1000** | **1000** | **1000** | **1000** | **0** |

These are *field-coverage* results, not a claim that no source references exist in separate editorial audit documents. A source path and source blob SHA are historical repository provenance, **not** an independently observed dictionary CEFR label. Do not interpret `source_level` as independently verified just because it might later contain text.

## Source interpretation: critical distinction

Oxford Learner's Dictionaries explicitly explains that CEFR measures language abilities and does **not itself grade individual vocabulary items**; Oxford aligns its own wordlists to CEFR as a pedagogical guide. Source observed 2026-11-22:
https://www.oxfordlearnersdictionaries.com/about/wordlists/cefr.html

The Council of Europe's CEFR global scale likewise describes communicative proficiency, not an official headword-by-headword allocation. Source observed 2026-11-22:
https://www.coe.int/en/web/common-european-framework-reference-languages/table-1-cefr-3.3-common-reference-levels-global-scale/

Therefore never claim that a word is officially assigned by the Council of Europe. Capture a **specific publisher's labelled word/sense** with URL, observed date, exact part of speech, dictionary sense/definition, and the scope of the label. If a page has no CEFR label or the label belongs to another sense, record `NO_EXPLICIT_MATCHING_SENSE_LABEL`, not a guessed level.

## Proposed fail-closed release checks (design only; not implemented here)

1. Require a separate approved manifest, never use the provisional shortlist as the public data source.
2. Require 200 entries at each of A1, A2, B1, B2, C1; deduplicate normalized headword+POS+meaning across all levels, with independent human adjudication for semantic duplicates.
3. Require per-entry immutable review task linkage, independently identified reviewer, decision timestamp, and signed-off English, Myanmar, example and exact-sense CEFR checks. Reject empty or self-authored evidence.
4. Require the publisher's explicit sense-level evidence URL, observation date, relevant quote/label and evidence provenance; fail closed on missing, mismatched or ambiguous labels.
5. Require all 4,000 George/Emma headword/example assets to exist and be genuinely listened to, with reviewer/time and source-text alignment. A generated file or waveform check is not listening signoff.
6. Require successful parallel A1–C1 GitHub Actions job conclusions with actual run IDs and logs; mobile/browser regression, physical iPhone Safari evidence, GitHub Pages hosting confirmation, production deployment verification and protected-asset integrity checks.
7. Preserve 54 lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy; no main-branch change or release while any gate is missing.

## Current decision

**BLOCKED / STAGING ONLY.** The 1,000 first-pass entries are written but none independently approved. No audio generation, listening, physical-device testing, CI success, hosting clearance or deployment is asserted by this audit. Independent reviewers must resolve previously documented cross-level sense conflicts before any rebalancing of the 200-per-level target.
