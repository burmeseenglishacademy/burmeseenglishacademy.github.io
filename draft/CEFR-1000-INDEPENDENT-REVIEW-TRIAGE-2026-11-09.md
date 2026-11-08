# CEFR-1000 independent-review triage and evidence intake — 2026-11-09

**Status: staging research only. NOT approval, not a release manifest.**

## Provenance and reproducible snapshot

- Inventory: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, read 2026-11-09 (Singapore).
- Project scope: **1,000 total**, 200 at each CEFR level; the earlier 5,000-word concept is superseded.
- Counts below are mechanically derived from the inventory fields. “Written first pass” means nonempty English definition, Myanmar meaning and example; **not** verified accuracy. Independent check requires *all* four content/level flags and release approval, not merely a proposed definition.
- No publisher lookup or real device/audio testing was performed for this snapshot; no external source is implied.

| Level | Provisional entries | Written first pass (unverified) | Independently approved | All three source fields populated |
|---|---:|---:|---:|---:|
| A1 | 200 | 200 | 0 | 0 |
| A2 | 200 | 200 | 0 | 0 |
| B1 | 200 | 200 | 0 | 0 |
| B2 | 200 | 200 | 0 | 0 |
| C1 | 200 | 200 | 0 | 0 |

## High-priority independent adjudication packets

1. **A1 a / an** (source indices 0 and 1, `draft/A1-EDITORIAL-STARTER.json`): distinct written forms but one indefinite-article lexical unit; determine whether a 200-*lexical-sense* quota can count both. Require an independent lexicographer's decision and, if consolidated, an evidence-backed replacement candidate. Do not silently alter counts.
2. **A1 i** (source index 3): lowercase headword conflicts with standard uppercase English first-person pronoun **I**. Check case-sensitive headword identity, examples and British audio text before any final manifest. Independent correction required.
3. **A1 be** (source index 2): provisional broad definition may mix copular linking and other grammatical functions. Independent review must choose the precise sense, matching example, Myanmar translation and CEFR evidence.
4. **A1 this / that** (source indices 7 and 8): distinguish demonstrative determiner from pronoun and discourse uses; publisher evidence must identify the exact sense rather than generic beginner grammar.
5. **A2 public / system / case** (source indices 185, 188, 190): broad polysemous headwords; reviewers must select a precise learner sense and compare the claimed A2 level with publisher's *sense-level* label.
6. **B1 cancer / civil / fan**: verify that the teaching definition and example use the same sense; do not infer CEFR level from topical familiarity or corpus frequency.
7. **B2 client / empire / incident**: independently check exact sense, CEFR level, British usage and idiomatic Myanmar meaning.
8. **C1 abortion / municipal / naval / racism**: review technical, socially sensitive and domain-specific senses carefully; presence in a word list does not prove C1. Use neutral original examples and clear Myanmar wording.

## Required evidence packet per entry (fail closed)

Each independently reviewed record must include: immutable inventory reference (word, level, source path/index/blob SHA); the **specific** English sense and part of speech; a publisher URL resolving to that sense and an observation date; a documented *sense-specific* CEFR level citation (or an explicit unresolved classification); independently checked Myanmar meaning with reviewer identity and date; independently checked original example with grammar/sense match; British headword/example audio files for **both George and Emma** with checksums and real listening reviewer signoff; and explicit review decisions that cannot be synthesized from automated/self-checks.

**Do not copy research notes into `reviewed_*` or `release_approved` flags.** Publisher grammar examples alone do not establish CEFR lexical-sense levels. Historical WordNet labels, named entities, and unattested CEFR claims require explicit rejection or independently corroborated publisher evidence.

## Release barriers

The current inventory has no populated complete three-source evidence packet. Independent approvals remain zero. No evidence in this audit establishes generated George/Emma audio for the final 1,000, actual listening, browser/mobile regression, physical iPhone Safari inspection, GitHub Pages size/hosting clearance, preservation checks for 54 lessons and separate IELTS bank, or confirmed production deployment. Keep the branch staging-only. GitHub Actions results for this documentation commit must be checked separately; a successful structural test never implies release readiness.
