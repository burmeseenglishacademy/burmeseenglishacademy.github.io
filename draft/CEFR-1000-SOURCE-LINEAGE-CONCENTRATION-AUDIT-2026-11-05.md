# CEFR-1000 source-lineage concentration and release-blocking audit — 2026-11-05

**Scope:** user-approved 1,000 total (A1/A2/B1/B2/C1 = 200 each), staging only. **Observation date:** 2026-11-05 Singapore. **Observed repository blob:** `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` at `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. This is an inventory/provenance analysis, **not** independent dictionary/CEFR validation.

## Directly calculated per-level inventory and source provenance

| Level | First-pass written | Independently approved | All five review booleans true | Source paths and counts |
|---|---:|---:|---:|---|
| A1 | 200 | 0 | 0 | `draft/A1-EDITORIAL-STARTER.json` (200) |
| A2 | 200 | 0 | 0 | `draft/A2-C1-EDITORIAL-STARTER.json` (179); `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json` (4); `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json` (3); `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json` (5); `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json` (9) |
| B1 | 200 | 0 | 0 | `draft/A2-C1-EDITORIAL-STARTER.json` (200) |
| B2 | 200 | 0 | 0 | `draft/A2-C1-EDITORIAL-STARTER.json` (200) |
| C1 | 200 | 0 | 0 | `draft/A2-C1-EDITORIAL-STARTER.json` (125); `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json` (42); `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json` (28); `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json` (5) |

## Source-lineage risk

Across the entire 1,000 entries, source files contribute: `draft/A1-EDITORIAL-STARTER.json` **200**; `draft/A2-C1-EDITORIAL-STARTER.json` **704**; `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json` **32**; `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json` **8**; `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json` **5**; `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json` **9**; `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json` **42**. The two starter files alone contribute **904/1,000 (90.4%)**; this is **draft lineage**, not external publisher-backed CEFR evidence. A source path, source index, or source blob hash must never be accepted as a publisher URL, independent reviewer identity, or exact-sense CEFR citation.

## Fail-closed acceptance criteria for future implementation

1. Each entry must bind a stable sense ID to the exact headword, POS, English definition, Myanmar meaning and example, with independent reviewer identity and timestamp per review dimension; reject self-review and absent attestations.
2. Require a genuine third-party publisher URL, observed date, publisher sense identifier or unambiguous sense excerpt, explicit CEFR evidence and a reviewer decision linking that evidence to the exact sense. Reject WordNet-only evidence, inferred CEFR from frequency, generic dictionary homepages and bare internal source paths.
3. Count 200 independently approved **distinct senses** at each CEFR level, not just 200 draft rows; reject duplicate normalized sense IDs across levels, including inflectional aliases unless a separately documented sense distinction is independently justified.
4. For each approved entry require four manifest-bound files (George headword, George example, Emma headword, Emma example): 4,000 total; validate hashes and audio identity and record real human listening decisions. No generation or listening is evidenced by this audit.
5. Require actual browser/mobile regression, physical iPhone Safari signoff, Pages asset/hosting assessment, protection of 54 lessons and separate IELTS 1,000 bank and existing production audio, and observed live production deployment before any release-ready claim.

## Specific editorial follow-up

The A1 entry `i` (source index 3) remains lowercase, requiring an orthographic correction **only after** appropriate editorial review; do not mistake this for a CEFR or audio approval. Source-backed exact-sense investigation should prioritise previously flagged `civil`, `permit`, `conduct`, `fine`, and everyday C1 senses; these remain unresolved. This report contains no newly retrieved publisher CEFR evidence and does not alter shortlist flags.

**Release decision:** BLOCKED — independent review 0/1,000, final George/Emma audio listening not verified, physical iPhone QA not verified, production deployment not verified. No merge or publish authorised by this report.
