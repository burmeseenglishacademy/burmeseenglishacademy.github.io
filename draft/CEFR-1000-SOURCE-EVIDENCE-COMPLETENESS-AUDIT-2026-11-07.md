# CEFR-1000 source-evidence completeness audit — 2026-11-07

**Scope:** staging-only first-pass shortlist, NOT the superseded 5,000-word plan. **Inventory blob SHA:** `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Audited file: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`. Observation date: 2026-11-07. This is a deterministic inventory audit, **not** an independent linguistic review or publisher consultation.

## Exact counts from parsed 1,000-entry inventory

| Level | First-pass written | Independently approved | English reviewed | Myanmar reviewed | Example reviewed | CEFR reviewed | Pronunciation reviewed | Empty source_english / source_burmese / source_level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 0 | 0 | 0 | 0 | 0 | 0 | 200 / 200 / 200 |
| A2 | 200 | 0 | 0 | 0 | 0 | 0 | 0 | 200 / 200 / 200 |
| B1 | 200 | 0 | 0 | 0 | 0 | 0 | 0 | 200 / 200 / 200 |
| B2 | 200 | 0 | 0 | 0 | 0 | 0 | 0 | 200 / 200 / 200 |
| C1 | 200 | 0 | 0 | 0 | 0 | 0 | 0 | 200 / 200 / 200 |

**Finding:** Every provisional entry has blank `source_english`, `source_burmese`, and `source_level` fields. These are 3,000 missing field values across 1,000 entries, not evidence of 3,000 different missing references. Source file path/index/blob provenance exists for each entry, but upstream draft provenance does **not** establish independent publisher-backed exact-sense CEFR evidence. Do not infer review from existing research notes or automatically populate source fields from dictionary homepages. No duplicate case-folded headword strings were found across the 1,000 entries; this is **not** sense-level deduplication.

## Actionable independent-review protocol

1. For each entry, require a publisher URL to the **specific sense**, publisher name, observed-on date, captured CEFR label and matching part of speech. Record explicit `NO_PUBLISHER_CEFR_LABEL` where no label is displayed; never infer one from another sense or a general dictionary page.
2. Preserve the original `source_path`, `source_index`, `source_blob_sha` and candidate's exact English definition, Myanmar meaning and example. A separately identified reviewer must compare all three against the cited sense, not merely mark a source URL as present.
3. Log competing classifications in a conflict queue. Existing documented candidates include `historic` (B2 provisional versus B1 publisher evidence), `actual` and `eventually` (B1 provisional versus B2 evidence), `grab` (B2 provisional versus B1 physical-taking sense), `minute` (60-second sense versus short-time example), and `project` (student-project versus general-project sense). Reclassification must preserve exactly 200 independently accepted distinct senses per level; do not silently move entries.
4. Require an independently signed reviewer identity, evidence timestamp and reviewed content hash before setting any `reviewed_*` or `release_approved` field. Researcher self-checks are insufficient.
5. Release guard must reject any missing or stale source evidence, incomplete reviewer signoff, unverified George/Emma headword/example audio and listening signoff, absent browser/mobile/physical iPhone Safari evidence, unverified GitHub Pages constraints, or absent deployment verification. Preserve the 54 lessons, separate IELTS bank, existing production audio and privacy.

## Audio and deployment truth

The provisional manifest reports `NOT_GENERATED_FOR_FINAL_SHORTLIST_NOT_LISTENED`. No genuine George/Emma listening evidence, physical iPhone Safari results, hosting clearance or production deployment was observed in this audit. Production stays unchanged; release remains **BLOCKED**.

## Reproducibility

Parse the inventory JSON; group `entries` by `level`; count each `reviewed_*` boolean strictly equal to `true`, count `release_approved === true`, and count empty trimmed `source_english`, `source_burmese`, `source_level`. Case-fold `word` to check headword-string collisions separately from exact-sense duplication. This report does not claim to have read the independent-review-tasks JSON: its connector response returned an empty content string, so the task-file contents remain unverified here.
