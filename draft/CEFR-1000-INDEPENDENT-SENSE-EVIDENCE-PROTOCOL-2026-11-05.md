# CEFR-1000 independent exact-sense evidence collection protocol (staging only)

Observed: 2026-11-05. Scope: exactly 200 provisional entries each at A1, A2, B1, B2 and C1 (1,000 total). **Zero entries independently approved.** This document is a research protocol, not a review or evidence that any entry meets a CEFR level.

## Authoritative lookup starting points (NOT attestations for individual entries)

- Cambridge Dictionary, English dictionary: https://dictionary.cambridge.org/dictionary/english/ — locate exact lemma, part of speech, sense, British pronunciation and example; record exact entry URL and access date.
- Cambridge English Profile / English Vocabulary Profile: https://www.englishprofile.org/wordlists — inspect the particular word + part of speech + sense + CEFR level, where accessible. A dictionary headword page alone is **not** proof of CEFR assignment.
- Council of Europe CEFR Companion Volume: https://www.coe.int/en/web/common-european-framework-reference-languages — framework descriptions, **not** word-by-word level evidence.
- Oxford Learner's Dictionaries: https://www.oxfordlearnersdictionaries.com/ — second dictionary sense/POS and British pronunciation cross-check; do not infer CEFR from word-list presence without explicit sense-level designation.

The links above are research entry points, not claims of pages being accessed or a particular sense being found. Record source publisher, exact URL, observed-on date (YYYY-MM-DD), headword, POS, sense number/definition paraphrase, displayed CEFR marking, and any licensing limits. If an exact sense-level CEFR designation is absent, record **UNSUBSTANTIATED** and keep editorial hold. Never copy dictionary examples verbatim into the app; write original example sentences.

## Reviewer evidence schema (one record per candidate sense)

```json
{
  "candidate_level": "A1",
  "headword": "a",
  "part_of_speech": "article",
  "proposed_exact_sense": "indefinite article before a singular count noun",
  "publisher": null,
  "publisher_entry_url": null,
  "publisher_observed_on": null,
  "publisher_sense_identifier": null,
  "publisher_cefr_level_for_this_sense": null,
  "source_support_status": "UNSUBSTANTIATED",
  "english_definition_review": "PENDING_INDEPENDENT_REVIEW",
  "myanmar_translation_review": "PENDING_INDEPENDENT_REVIEW",
  "original_example_review": "PENDING_INDEPENDENT_REVIEW",
  "cross_level_collision_review": "PENDING",
  "reviewer_identity_and_independence": null,
  "reviewer_signed_on": null,
  "release_approved": false
}
```

The example is a **blank template**, not completed source research or an independent signoff. Keep evidence in staging review artifacts; do not set approval flags from self-evaluation or source lookup alone.

## Review sequence

1. Inspect provisional entry and its original source path, source index and blob SHA. Preserve the full chain of provenance.
2. Disambiguate lemma, inflection, part of speech, and *exact sense*; check capitalization, named entities, proper nouns, historical WordNet contamination, homographs and cross-level duplicates.
3. Record publisher-backed exact-sense CEFR evidence, with explicit observation date and source URL. If sources disagree, preserve both, explain conflict and leave on hold.
4. Have independent qualified reviewers check English meaning, fluent Myanmar meaning, natural original example grammar and contextual sense alignment; record reviewer provenance and dates separately.
5. Independently review pronunciation and British George/Emma headword and example audio. Generated files alone do not establish real listening signoff.
6. Only after all entries pass independent review should the approved manifest be considered for structural, audio, browser/mobile, physical iPhone Safari, GitHub Pages and production preservation gates.

## First two high-priority sense checks

- **A1 `a` (article)**: provisional source `draft/A1-EDITORIAL-STARTER.json`, source index 0. Clarify article use before consonant *sounds*, not simply consonant letters; retain the current entry on hold pending source-backed exact-sense CEFR and independent Myanmar/English/example review.
- **A1 `an` (article)**: same provisional source, index 1. Distinguish vowel *sound* from written initial vowel; test cases such as *an hour* and *a university* during independent review. Current example “She has an apple.” is a first-pass sentence, not approved.

No dictionary source was independently verified for these two entries in this protocol. All 1,000 remain on editorial hold, with zero independently checked.

## Release blockers

Full independent English, Myanmar, original-example and exact-sense CEFR review; deduplicated approved 200-per-level manifest; 4,000 final George/Emma headword/example audio assets with real listening evidence; browser and mobile regressions; real physical iPhone Safari QA; GitHub Pages hosting clearance; confirmed production deployment; and preserved 54 lessons, separate IELTS 1,000-word bank, existing George/Emma production audio and privacy protections. **Never merge, publish or alter main to bypass these gates.**
