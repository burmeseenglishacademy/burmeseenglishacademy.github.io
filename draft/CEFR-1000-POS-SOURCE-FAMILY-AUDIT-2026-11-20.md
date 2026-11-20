# CEFR-1000 part-of-speech and source-family coverage audit — 2026-11-20

**Scope:** exactly the approved 1,000-total A1–C1 provisional shortlist. **Status:** staging only; no independent review or approval inferred.

## Source and method
Read the entire UTF-8 JSON at [provisional shortlist](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json) on 2026-11-20. Blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Grouped the actual 1,000 `entries` by `level`, `part_of_speech`, and `source_path`; separately tested case-folded NFKC headword collisions. This is **mechanical provenance/coverage triage**, not a linguistic CEFR validation.

| Level | First-pass written | Nouns incl. plural | Verbs incl. auxiliary/modal | Adjectives incl. ordinal | Adverbs | Other POS | Independent approvals |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 89 | 33 | 18 | 6 | 54 | 0 |
| A2 | 200 | 118 | 28 | 28 | 15 | 11 | 0 |
| B1 | 200 | 116 | 38 | 31 | 14 | 1 | 0 |
| B2 | 200 | 102 | 30 | 47 | 20 | 1 | 0 |
| C1 | 200 | 87 | 40 | 58 | 15 | 0 | 0 |
| **Total** | **1,000** | **512** | **169** | **182** | **70** | **67** | **0** |

Classification reflects the stored POS labels, not independently checked senses. In particular, A1 has `politeness marker`, `question word`, `exclamation`, and `number` labels that do not map one-to-one to traditional POS; these were included under Other, not silently recategorised. The B1/C1 concentration of content words is an editorial coverage question, not proof of an error. NFKC case-folded headwords had **zero exact collisions** across the 1,000 entries; that does not exclude synonym, lemma/inflection, grammatical-variant or exact-sense duplication.

## Source-family concentration and verification priorities

- A1: all 200 records originate from `draft/A1-EDITORIAL-STARTER.json`.
- B1 and B2: all 200 records in each level originate from `draft/A2-C1-EDITORIAL-STARTER.json`.
- A2: records span `draft/A2-C1-EDITORIAL-STARTER.json` and recovery batches 58–61.
- C1: records span `draft/A2-C1-EDITORIAL-STARTER.json` and recovery batches 57–59.

**Risk:** source-family diversity is not independent lexical evidence. Recovery-batch provenance and editorial-starter provenance cannot be used as CEFR-level attestation. For A2/C1, independently verify the recovered source index/blob for every entry and whether a sense-specific CEFR source actually supports its provisional level. For B1/B2, prioritise a systematic exact-sense review of the single shared starter family rather than treating 200 records as 200 independent evidence sources.

## Actionable editorial intake (not approvals)

1. Add reviewer-visible POS + exact-sense cross-checks to the separate independent-review task intake. Distinguish `a` and `an` as teaching forms from genuinely distinct senses; case-folded uniqueness alone cannot decide this.
2. Sample source-recovery batches for named entities, historical WordNet imports, malformed lemma forms and unsupported CEFR assignments; record each original blob SHA and index alongside the independent dictionary URL, observed date and exact cited sense.
3. Review underrepresented functional vocabulary in B1–C1 **only against the approved 200-per-level selection policy**; do not add words to the manifest or reassign levels without independent evidence and balanced replacement.
4. Require independent English, fluent Myanmar, original-example and exact-sense CEFR judgments before any reviewed/approved field can be true. Author inspection and source URL collection remain separate from independent signoff.
5. Preserve the existing 54 lessons, separate IELTS 1,000-word bank, George/Emma production audio and privacy policy. Keep the release gate closed until independent reviews, complete new voice assets with real listening signoff, browser/mobile and physical iPhone Safari QA, GitHub Pages hosting clearance, and confirmed production preservation/deployment evidence.

## CI and release status

This audit did not execute or inspect a new GitHub Actions workflow run. Earlier historical green jobs cannot be attributed to this documentation change. No audio generation, human listening, physical iPhone QA, hosting clearance, or deployment was performed. **Staging only; 0/1,000 independently approved.**
