# CEFR-1000 historical provenance full-source readback — 2026-11-04

**Scope:** staging-only evidence; no approval, publication, or independent linguistic validation. Observed 2026-11-04 (SGT). Provisional inventory blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

## Direct readback results

Fetched all seven historical source JSON files from the existing staging branch using GitHub file reads, compared returned blob SHA with the per-entry historical SHA, and compared all 1,000 provisional entries at their recorded source indices across word, part of speech, English definition, Burmese gloss, example sentence, and level. All seven current source blobs match the recorded SHA. **All 1,000 entries match all six compared fields when the historical schema's `proposed_level` is correctly mapped to shortlist `level` for recovery batches.** The 96 recovery-batch records use `proposed_level` instead of `level`; this is a schema difference, not a CEFR level change. None is evidence of CEFR validation. No other compared field differs. This authenticates current blob-to-shortlist consistency, not publisher CEFR evidence or independent review.

| Historical source | Source blob SHA | Selected | Schema-mapped level mismatches |
|---|---|---:|---:|
| [draft/A1-EDITORIAL-STARTER.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A1-EDITORIAL-STARTER.json) | `ff1e93f60828ef2f94c9146522ce94075183b0ae` | 200 | 0 |
| [draft/A2-C1-EDITORIAL-STARTER.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-EDITORIAL-STARTER.json) | `b04dd85db5cfae131c25aa4c73109778991b6fdc` | 704 | 0 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json) | `da7df62123acfac89a0acedad4652ec499c7ed3d` | 32 | 32 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json) | `228c772697e4879f6b8a30f85709d188a1df266c` | 8 | 8 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json) | `96d54ddb6fdc204e8cbea45e8c97a6c98fb17b11` | 5 | 5 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json) | `6a10ae41eb41370a9a5b74d907fa395bb43e18d8` | 9 | 9 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json) | `7eaf88b9ed7687b26ccde713262f10fb209743a8` | 42 | 42 |

### Schema mapping correction

The 96 recovery records have `proposed_level` (21 A2 and 75 C1), while the shortlist uses `level`. All 96 proposed values agree with the shortlist levels. **No level discrepancies were found.** The original table below is replaced by this correction; do not interpret the earlier `undefined → level` comparison as evidence of reassignment.

## Required safeguards and editorial next steps

1. Treat all 96 schema-mapped proposed levels as unverified editorial proposals requiring source-backed exact-sense CEFR justification and human-independent review; do not treat source proposals as authoritative.
2. Add an automated staging gate comparing all historical source records and their immutable Git blob SHAs, with schema-aware `level`/`proposed_level` mapping and fail-closed handling of missing or conflicting fields. Do not auto-approve proposed levels.
3. Require original publisher URLs, observed dates, specific sense/POS, evidence quality and fluent Myanmar/example review for every entry. Historical source files and WordNet are not CEFR authorities.
4. Continue to block release: A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0 first-pass written/independently approved; all 1,000 held. Audio (4,000 George/Emma headword/example recordings) and actual listening signoff, browser/mobile and physical iPhone Safari review, Pages hosting, and confirmed deployment remain unverified. Preserve production 54 lessons, separate IELTS bank, existing audio and privacy.

**Reproducibility:** Fetch `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` and each distinct `source_path` at branch `cefr-5000-bilingual-qa-staging`; verify fetched blob SHA equals `source_blob_sha`; compare `source.entries[source_index]` against the shortlist entry for six fields listed above, mapping `proposed_level` to `level` only for recovery-batch schemas. This is a current-branch GitHub API readback; independently pinned historical commits and a protected exception ledger remain future gates.
