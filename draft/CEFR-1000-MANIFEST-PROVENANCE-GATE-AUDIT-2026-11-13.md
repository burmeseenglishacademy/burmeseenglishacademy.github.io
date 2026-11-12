# CEFR-1000 manifest provenance and fail-closed gate audit — 2026-11-13

Scope: **approved 1,000-total target only** (A1/A2/B1/B2/C1: 200 each). Staging-only research, **not** an independent review, CI result, audio verification, or launch authorization.

## Reproducible input
- Inspected `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` on `cefr-5000-bilingual-qa-staging`.
- Observed Git blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Observation date: 2026-11-13 (Singapore).
- The JSON's `release_status` remains `PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH`.
- Counts below were calculated directly from all `entries`, not copied from the summary counters.

| Level | Entries with English + Myanmar + example first-pass text | Independent release approvals | Editorial holds | Nonblank source_english | Nonblank source_burmese | Nonblank source_level |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 0 | 200 | 0 | 0 | 0 |
| A2 | 200 | 0 | 200 | 0 | 0 | 0 |
| B1 | 200 | 0 | 200 | 0 | 0 | 0 |
| B2 | 200 | 0 | 200 | 0 | 0 | 0 |
| C1 | 200 | 0 | 200 | 0 | 0 | 0 |
| **Total** | **1,000** | **0** | **1,000** | **0** | **0** | **0** |

All 1,000 provisional headwords are distinct under lowercase/trim normalization, but this **does not** establish distinct *senses*. First-pass written count is not independently checked count. Source-backed research may exist in separate observation reports, but the six-column inventory above describes only the manifest's own fields.

## Release-blocking evidence gap
The manifest has no nonblank `source_english`, `source_burmese`, or `source_level` fields. Source-path and source-blob provenance point to earlier drafts, **not independent dictionary/CEFR verification**. Every `editorial_hold` is true. The existing entry flags must remain false unless a genuinely separate reviewer has completed and recorded signoff.

A release validator must refuse to authorize production if any of these are missing: exact sense ID; exact-sense level evidence with URL, observation date and source provenance; independently signed English, fluent Myanmar, original-example and pronunciation reviews; 200 unique headword/sense keys in each level and no unresolved cross-level conflicts; all 4,000 required George/Emma × headword/example audio assets with actual listening signoffs; browser/mobile regression evidence; physical iPhone Safari evidence; GitHub Pages asset/size/hosting review; and verified deployment plus preservation checks for 54 lessons, separate IELTS bank, existing production audio and privacy controls. Mere existence of a report or a green structural test cannot satisfy any human/physical/production gate.

## Concrete cases for independent adjudication
These examples are present in the inspected manifest; prior staging research reports discuss their potential CEFR or sense mismatch. Re-evaluate against the cited primary sources in those reports rather than accepting this audit as fresh source evidence:
- `i` (A1 pronoun) is lowercased although the sentence uses capital `I`; exact orthographic identity needs resolution.
- `home` (A1 noun) uses `I go home after school.`, in which `home` is directional, not the stated noun sense.
- `thank` (A1 verb), `prepare` (B2 verb), `calm` (B2 adjective), `tribute` (C1 noun), and `conversion` (C1 noun) have prior level-conflict observations. None is automatically reclassified here.

## Next staging work
1. Move externally supported exact-sense observations into a separate *unapproved evidence ledger* with source URLs, retrieval dates, sense quotes/paraphrases and reviewer action; do not fill approval fields automatically.
2. Extend negative-regression tests so a manifest with 1,000 well-formed first-pass entries but zero independently signed source-level reviews is explicitly **release denied**. Also reject audio-file existence without listening evidence, simulator-only Safari claims, or a deployment URL without actual production preservation checks.
3. Run parallel level-specific CI on the actual changed commit, inspect each job conclusion and failure logs. This documentation commit has **no CI verification claimed**.
4. Keep staging separate from `main` and do not publish until all human, listening, physical-device, hosting and production gates are genuinely satisfied.
