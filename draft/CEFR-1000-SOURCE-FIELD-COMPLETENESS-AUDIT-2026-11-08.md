# CEFR-1000 source-field completeness and provenance audit — 2026-11-08

**Scope:** staging-only, user-approved 1,000-total project. This is an automated inventory audit, **not** independent linguistic or CEFR review and not release authorization.

## Reproducible input
- Inventory: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`
- Git blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`
- Observation date: 2026-11-08
- Audit method: parse all `entries`, group by `level`, count non-empty source evidence fields, editorial holds, and approval flags. These fields are **not** equivalent to externally verified source URLs or publisher sense labels.

| Level | Written first-pass | Editorial hold | Independently approved | Nonempty source_english | Nonempty source_burmese | Nonempty source_level |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 0 | 0 | 0 | 0 |
| A2 | 200 | 200 | 0 | 0 | 0 | 0 |
| B1 | 200 | 200 | 0 | 0 | 0 | 0 |
| B2 | 200 | 200 | 0 | 0 | 0 | 0 |
| C1 | 200 | 200 | 0 | 0 | 0 | 0 |
| **Total** | **1000** | **1000** | **0** | **0** | **0** | **0** |

## Findings and action plan
1. All 1,000 provisional entries have empty `source_english`, `source_burmese`, and `source_level` fields. These are **source-evidence completeness gaps**, not proof that no separate research dossiers exist. Do not backfill these fields with unverifiable URLs or self-certification. Build a sense-specific evidence register with URL, publisher, exact POS/sense, displayed CEFR label (if any), observed date, and reviewer provenance.
2. No exact duplicate lowercased `word` strings were observed among 1,000 entries. This **does not** establish 1,000 distinct lexical units or senses: `a` and `an` remain a known morphological/article-unit conflict. A case-normalized uniqueness check cannot detect semantic equivalence.
3. A1 entry `i` is lowercase in the provisional inventory, while its example correctly uses `I`. Proposed correction requires controlled editorial revision, not an automatic alteration of the held manifest.
4. Every entry retains `editorial_hold=true`; none is `release_approved=true`. Independent English, fluent Myanmar, example grammar, source-backed CEFR and pronunciation review remain absent from approved release evidence.
5. Next useful batches: collect exact-sense publisher evidence for A1 pronouns/articles and high-risk cross-level senses; independently adjudicate the a/an lexical unit and replace/rebalance only after review; then repeat for A2–C1 with evidence linked by stable inventory provenance (`source_path`, `source_index`, `source_blob_sha`).
6. Audio remains unverified for final 1,000: both British voices (George/Emma), headword and example clips, genuine listening signoff and integrity mapping are required. Browser/mobile, physical iPhone Safari, GitHub Pages hosting and verified production deployment remain release blockers.

**Fail-closed decision:** STAGING ONLY. This audit must not be interpreted as independent approval, a passing audio test, a device test, or a production launch. Protect 54 existing lessons, separate IELTS 1,000 bank, production audio and privacy assets.
