# CEFR-1000 exact-sense editorial triage — 2026-11-12

Status: STAGING ONLY; not independent review, not CEFR validation, not release evidence.

## Direct manifest inspection
Source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, inspected 2026-11-12.

| Level | First-pass entries | Entries missing explicit sense_id | Independently approved |
|---|---:|---:|---:|
| A1 | 200 | 200 | 0 |
| A2 | 200 | 200 | 0 |
| B1 | 200 | 200 | 0 |
| B2 | 200 | 200 | 0 |
| C1 | 200 | 200 | 0 |
| **Total** | **1000** | **1000** | **0** |

The `source_path`, `source_index`, and `source_blob_sha` fields document internal draft provenance only; they are **not external lexical-sense or CEFR evidence**. Existing definitions, Myanmar meanings, and examples remain unverified. Do not auto-generate `sense_id` from headword alone and do not change review flags.

## Priority manual source-evidence queue (illustrative, not verdicts)
These C1 records are present in the inspected manifest and require exact-sense confirmation before their C1 placement can be defended:

1. **signature** (noun): handwriting sense; verify that the source's CEFR annotation applies to the *handwritten name* meaning rather than a figurative or characteristic sense. Existing example: “Please add your signature at the bottom of the form.”
2. **copyright** (noun): legal-right sense; confirm whether the reference labels this specific noun meaning C1 and not merely the headword in a wordlist.
3. **conversion** (noun): changing form/use sense; distinguish conversion of a building from religious or currency conversion senses.
4. **trigger** (verb): causation sense; distinguish figurative causation from a physical trigger and document the source's CEFR label for this verb sense.
5. **tribute** (noun): expression of respect sense; distinguish a performance tribute from historical payment or tax senses.
6. **consistently** (adverb): repeated standard over time; check evidence for the adverb itself, not just adjective `consistent`.

For each candidate, capture: headword, POS, precise definition, sense identifier and source entry URL, explicit CEFR evidence (or `UNSUPPORTED`), date observed, source licence/quotation constraints, any conflict with other levels, English-definition edit suggestion, fluent Myanmar meaning suggestion, and example-grammar review. A dictionary definition alone is not proof of CEFR level. A CEFR-tagged headword without sense-level evidence must remain held if senses conflict.

## Gate verification
GitHub Actions run `43136221886` reported five completed successful jobs (A1, A2, B1, B2, C1), as read from job conclusions on 2026-11-12. These are **negative evidence-gate regression tests**, not editorial or device approvals. Raw job logs were not re-read for this note. The current document commit has not been tested.

Release must remain blocked until independent English, Myanmar, example and CEFR-source signoff for all 1,000 entries; explicit sense identity; 4,000 George/Emma audio assets with genuine listening signoff; browser/mobile and physical iPhone Safari evidence; hosting clearance; and confirmed production deployment. Preserve all 54 lessons, the separate IELTS 1,000 bank, existing production voice assets and privacy controls. No deployment authorised while any gate is missing.
