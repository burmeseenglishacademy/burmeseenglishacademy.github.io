# CEFR-1000 source-provenance gap and historical-risk audit

**Observed:** 2026-11-28  
**Scope:** The current 1,000-entry provisional shortlist, its 1,000 review tasks, and the seven original source JSON files referenced by those entries. This is a source-metadata audit, not an independent vocabulary review or approval.

## Files and provenance inspected

- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Review tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, blob SHA `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- `draft/A1-EDITORIAL-STARTER.json`: `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- `draft/A2-C1-EDITORIAL-STARTER.json`: `b04dd85db5cfae131c25aa4c73109778991b6fdc`.
- `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json`: `7eaf88b9ed7687b26ccde713262f10fb209743a8`.
- `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json`: `da7df62123acfac89a0acedad4652ec499c7ed3d`.
- `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json`: `228c772697e4879f6b8a30f85709d188a1df266c`.
- `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json`: `96d54ddb6fdc204e8cbea45e8c97a6c98fb17b11`.
- `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json`: `6a10ae41eb41370a9a5b74d907fa395bb43e18d8`.

The source mappings were checked using each shortlist entry's `source_path` and `source_index`; no source entry was missing.

## CEFR provenance finding

**No exact-sense CEFR label is present in the inspected original source metadata for any of the 1,000 selected entries.**

- **A1 (200 entries):** every source entry has the same `source_level_reference` URL, https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000 . This is the general Oxford 3000/5000 information page, not an individual headword/sense CEFR label or a level-filtered record. The Oxford page explains that the word lists are CEFR-aligned and that the CEFR level appears beside each entry, but the generic information URL does not show which exact level or sense applies to any of these 200 entries: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000
- **A2–C1 (800 entries):** the original `source_level`, `source_english`, and `source_burmese` fields are empty across the selected records in the inspected starter/recovery sources. The recovery batch `proposed_level` is a provisional suggestion, not source evidence.
- **All 1,000 review tasks:** `source_evidence_urls` is empty; `source_observed_on`, reviewer identity, assignment and signature are null; every review dimension is pending and approval is false.

Therefore the current evidence register contains **0/1,000 source-backed exact-sense CEFR signoffs**. This does not mean the words are necessarily at the wrong levels; it means the original metadata cannot substantiate those levels. Each selected sense needs a traceable level-bearing source (or a documented, independently adjudicated alternative) before approval.

## Original source-status distribution

The selected 1,000 entries resolve to these original source statuses:

| Original source status | Count |
|---|---:|
| `DRAFT_PENDING_INDEPENDENT_REVIEW` | 200 |
| `AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW` | 704 |
| `SOURCE_RECOVERY_FIRST_PASS_PENDING_DEDUP_AND_INDEPENDENT_REVIEW` | 74 |
| `FIRST_PASS_UNVERIFIED_REQUIRES_INDEPENDENT_EVIDENCE` | 7 |
| `FIRST_PASS_UNVERIFIED_PENDING_CROSS_CORPUS_TRIAGE` | 14 |
| `REVERSIBLE_QUARANTINE_LEVEL_UNSUPPORTED` | 1 |
| **Total** | **1,000** |

The source-status distribution reinforces that these are provisional editorial inputs, not previously verified vocabulary records.

## Preserved quarantine: alacrity

- **Task:** `CEFR1000-C1-1000`; provisional level C1; noun.
- **Source:** `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json`, index 29, blob SHA `228c772697e4879f6b8a30f85709d188a1df266c`.
- **Original source status:** `REVERSIBLE_QUARANTINE_LEVEL_UNSUPPORTED`.
- **Original hold reason:** `C1_VS_C2_UNSUPPORTED_REQUIRES_GRADED_SENSE_SOURCE`.
- **Oxford evidence:** the Oxford Advanced Learner's Dictionary entry says “From the Word list Oxford 3000” and displays **A2** for the noun: https://www.oxfordlearnersdictionaries.com/us/definition/english/alacrity
- **Cambridge sense evidence:** Cambridge defines the noun as “speed and eagerness” and supplies a UK pronunciation, but the inspected Cambridge page displays no CEFR label: https://dictionary.cambridge.org/dictionary/english/alacrity
- **Level finding:** the Oxford A2 signal is a substantial conflict with the provisional C1 assignment. The selected definition (“Cheerful willingness and speed in doing something”) and example (“The volunteers responded with alacrity when help was requested”) should be independently checked against the Oxford A2 sense, the Cambridge meaning, and any further authoritative level source.
- **Myanmar:** `အလုပ်တစ်ခုကို စိတ်အားထက်သန်ပျော်ရွှင်စွာနှင့် လျင်မြန်စွာ ဆောင်ရွက်လိုစိတ်` broadly conveys the idea, but a reviewer should check whether the gloss overstates happiness and whether `စိတ်အားထက်သန်စွာ လျင်မြန်စွာ ဆောင်ရွက်ခြင်း` better matches the chosen sense.
- **Provenance warning:** the source batch retains the quarantine reason, but the provisional shortlist carries only `editorial_hold: true`; the separate review task does not carry the original reason. The source mapping makes it recoverable, but the reason should be explicitly considered by the independent reviewer. No hold or level field was changed in this audit.

## WordNet and named-entity surface audit

- No field or literal marker containing `WordNet` was found in the shortlist or the seven inspected original source JSON files. None of the 1,000 selected `source_path` values points to a WordNet file.
- The 1,000 selected headwords are unique after NFC/case-fold normalisation. A surface-form heuristic found no headword containing spaces, digits, uppercase letters, or non-ASCII/punctuation characters, and no `proper noun` POS label appears in the selected POS values.
- This is **not** proof that every historical source has been checked for WordNet derivation or that no common-word/proper-name homograph exists. Source provenance for 800 entries is blank, and lowercase spelling cannot by itself exclude a named-entity reading. Independent reviewers must still check each selected sense and context. For example, `apple` currently has a fruit definition and example, which is a common-word sense rather than a brand/name use; that does not clear unrelated homographs elsewhere.

## Required handling

1. Keep all 1,000 candidates on editorial hold.
2. Do not count a generic word-list landing page, a proposed level, a frequency rank, or a WordNet lemma as exact-sense CEFR evidence.
3. Recover and preserve the original `alacrity` quarantine reason during independent adjudication.
4. For each entry, capture a source URL that actually displays or documents the relevant CEFR level, the exact sense, an excerpt/reference, and observation date. If no reliable level source is found, leave the level unresolved for independent decision rather than inferring it.
5. Treat the source-metadata gap as a release blocker; do not backfill reviewer evidence or approval fields from this author-side audit.

No shortlist entry, review task, editorial hold, reviewer field, approval flag, production asset, or release setting was modified.
