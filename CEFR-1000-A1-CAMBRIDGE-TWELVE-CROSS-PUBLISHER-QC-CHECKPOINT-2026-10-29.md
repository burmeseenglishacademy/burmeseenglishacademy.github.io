# CEFR 1,000 — A1 Cambridge twelve exact-sense leads and four cross-publisher conflicts (staging only)

**Observed:** 2026-10-29. **Branch:** `cefr-5000-bilingual-qa-staging`. **Scope:** user-approved 1,000 total, exactly 200 first-pass entries per A1/A2/B1/B2/C1. **Status: BLOCKED / STAGING ONLY.**

## Source-backed editorial work, not independent signoff

Inspected publisher-owned Cambridge Dictionary **search-indexed page text** on 2026-10-29 for the twelve A1-draft nouns previously recorded against the official [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf). Attempts to open the Cambridge dictionary pages directly returned **HTTP 403**, so these are **indexed publisher sense leads**, not a complete direct-publisher page inspection or human verification. No source quotation has been invented. URLs, observation date, access limitation, sense label, original English/Myanmar/example snapshot and historical Git provenance are retained in [the research packet](draft/CEFR-1000-CAMBRIDGE-A1-FAMILY-AND-EVERYDAY-TWELVE-2026-10-29.json).

| A1 provisional headword | Cambridge indexed sense label | Human editorial review focus |
|---|---|---|
| [sister](https://dictionary.cambridge.org/dictionary/english/sister) | A1 | Older/younger sibling translation and unrelated religious/medical senses |
| [son](https://dictionary.cambridge.org/dictionary/english/son) | A1 | Parent-child sense, not address to a boy |
| [daughter](https://dictionary.cambridge.org/dictionary/english/daughter) | A1 | Parent-child sense, not stepdaughter |
| [grandmother](https://dictionary.cambridge.org/dictionary/english/grandmother) | A2 | Oxford A1 word/POS versus Cambridge A2 same family sense; Myanmar spelling |
| [grandfather](https://dictionary.cambridge.org/dictionary/english/grandfather) | A2 | Oxford A1 word/POS versus Cambridge A2 same family sense |
| [uncle](https://dictionary.cambridge.org/dictionary/learner-english/uncle) | A2 | Oxford A1 word/POS versus Cambridge A2 kinship sense; marriage relation |
| [aunt](https://dictionary.cambridge.org/dictionary/english/aunt) | A2 | Oxford A1 word/POS versus Cambridge A2 kinship sense; marriage relation |
| [phone](https://dictionary.cambridge.org/dictionary/english/phone) | A1 | Device noun, not verb or phonetic unit |
| [computer](https://dictionary.cambridge.org/dictionary/english/computer) | A1 | Information-processing machine, not any electronic device |
| [picture](https://dictionary.cambridge.org/dictionary/english/picture) | A1 | Image noun A1 versus screen image B2 and imagine verb C1 |
| [bag](https://dictionary.cambridge.org/dictionary/english/bag) | A1 | Carrying container, not other senses |
| [money](https://dictionary.cambridge.org/dictionary/english/money) | A1 | Uncountable money can include non-cash funds; draft definition may be narrow |

**Four specific cross-publisher conflicts:** `grandmother`, `grandfather`, `uncle` and `aunt` are **Oxford A1 word/POS** but **Cambridge A2 family-relationship senses**. These are not automatically reclassified. Independent reviewers must check the actual publisher entry, the exact intended sense, English/Myanmar meaning, original example, CEFR rationale and British use before deciding whether to retain, rewrite, retier or replace. The remaining eight have Cambridge A1 indexed sense leads, but no independent approval.

The draft definition of `money` mentions only coins/notes; Cambridge A1 usage also includes amounts held or spent. `picture` has a broad A1 image noun but separate higher-level senses. `phone` must remain the communication-device noun, not the verb or specialized phonetics sense. Proposed corrections remain **unapplied**.

## Actual fail-closed CI verification

Created [a 12-record integrity auditor](tools/audit_cefr_1000_cambridge_a1_twelve.py) that binds every Cambridge lead to its original Oxford ninth-batch PDF observation and frozen 1,000-entry shortlist, including Git blob SHA, original English, Myanmar, example, source URL, date, CEFR label, source access limitations and editorial hold. It rejects forged independent receipts, changed levels, invented source excerpts, replaced URLs, changed bilingual snapshots and count-preserving duplicate edits.

- [Structural run 40868377736](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40868377736), code head `f56605f9985b45730096822f56abc8ed9f5f9ef2`: **SUCCESS across all six A1/A2/B1/B2/C1/ALL jobs**. Actual ALL-job logs: **234/234** new negative mutations rejected, four conflicts retained, **145/145** source-bound reviewer-handoff mutations rejected, and protected production paths unchanged.
- [Documentary no-deployment run 40868391538](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40868391538), head `839f38e0a9d8c426c17472371c84473b488471e1`: **SUCCESS as report-only**, **234/234** new mutations rejected; explicit release blockers retained and protected production assets passed. A successful report-only workflow is **not** release approval.
- Compared baseline `252939f46278ef7eb8c5652168603959303e4377` with code head `839f38e0a9d8c426c17472371c84473b488471e1`: exactly four staging-only research/audit/workflow files changed; **no production files modified**.

## Truthful unchanged coverage and mandatory blockers

| Level | First-pass written | Direct Oxford word/POS coverage | Human-independent approved |
|---|---:|---:|---:|
| A1 | 200 | 136 | 0 |
| A2 | 200 | 72 | 0 |
| B1 | 200 | 84 | 0 |
| B2 | 200 | 70 | 0 |
| C1 | 200 | 51 | 0 |
| **Total** | **1,000** | **413** | **0** |

These **12 Cambridge indexed leads cover already-observed words**, so distinct Oxford coverage remains **413/1,000**; **587** lack a direct Oxford observation. The existing Oxford reviewer queue still has **152 lower publisher word/POS labels, 13 higher, 3 unlisted, and 245 matching word/POS classifications** needing independent exact-sense checks. The four new Cambridge conflicts are a **separate cross-publisher research dimension**, not additions to those Oxford-only counts.

**Final George/Emma real listening signoffs: 0/1,000.** Missing: authenticated independent English, fluent Myanmar, original example and source-backed CEFR signoffs for every word; final British George/Emma headword and example audio generated and actually listened to; desktop/mobile browser regression; real physical iPhone Safari and audio review; measured GitHub Pages hosting limits; release-candidate approval; verified preservation of the 54 lessons, separate IELTS 1,000-word bank, existing George/Emma audio and privacy; and confirmed production deployment.

**No merge, main-branch edit, public publication, fabricated review, physical-device claim or deployment claim. Release BLOCKED / STAGING ONLY.**
