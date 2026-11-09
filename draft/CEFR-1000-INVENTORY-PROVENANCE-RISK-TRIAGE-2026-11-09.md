# CEFR-1000 provisional inventory: provenance and review-risk triage (2026-11-09)

**Status: staging-only, NOT independent CEFR verification.** This is a reproducible structural and editorial triage of the existing provisional JSON, not a publisher CEFR assessment. Observation date: 2026-11-09 (Singapore). Source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Source URLs: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json ; https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json .

## Exact inventory snapshot

| Level | Provisional entries | Nonempty first-pass English/Myanmar/example | Independently approved (all review gates) |
|---|---:|---:|---:|
| A1 | 200 | 200 | 0 |
| A2 | 200 | 200 | 0 |
| B1 | 200 | 200 | 0 |
| B2 | 200 | 200 | 0 |
| C1 | 200 | 200 | 0 |

The counts of written fields are **not** proof of grammatical correctness, Myanmar fluency, CEFR suitability, genuine independent review, or usable audio. All entries retain editorial hold. No review flags were changed.

## High-priority source-provenance triage

The following are **examples for further investigation**, not confirmed wrong CEFR assignments. These terms were located in the actual inventory and their original `source_path` and `source_index` are recorded for audit.

| Provisional level | Headword | Part of speech | Original source/index |
|---|---|---|---|
| A2 | washcloth | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json #2 |
| A2 | postcard | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json #3 |
| A2 | sunflower | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json #4 |
| A2 | dustbin | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #1 |
| A2 | bathrobe | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #3 |
| A2 | snowman | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #6 |
| A2 | hairbrush | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #8 |
| A2 | toothbrush | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #9 |
| A2 | crossroads | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #11 |
| A2 | wheelbarrow | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #12 |
| A2 | greenhouse | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #13 |
| A2 | backseat | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json #15 |
| C1 | obfuscate | verb | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json #45 |
| C1 | alacrity | noun | draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json #29 |

A2 compound nouns near the end of its shortlist (e.g. washcloth, bathrobe, wheelbarrow, greenhouse) warrant exact-sense and learner-level checks: familiar component words do **not** establish a compound's CEFR level. C1 rarer words (e.g. alacrity, obfuscate) need publisher-backed exact-sense evidence and suitability review; rarity is not itself C1 evidence. Do not promote any entries simply because an English dictionary lists the word. Avoid deriving CEFR from WordNet synsets, word frequency, or a named entity.

## Independent reviewer acceptance checklist

For **each** entry: (1) verify canonical spelling, POS and exact sense against a dated publisher URL; (2) record the publisher's explicit sense-level CEFR tag, or mark `CEFR_UNSUBSTANTIATED`; (3) check original English definition against that exact sense; (4) independently validate fluent, context-specific Myanmar; (5) check original example grammar and Myanmar translation; (6) check British pronunciation, including stress and variant; (7) independently sign off all review fields with reviewer identity/date and evidence. An editor's own proposed changes must never flip independent flags.

## Fail-closed release notes

A manifest must reject missing or conflicting evidence, duplicate canonical headword/sense units, any level other than exactly 200 approved entries, any non-independent review, any missing George/Emma headword **or** example audio, absent genuine listening records, unverified mobile/browser/physical iPhone Safari evidence, unresolved GitHub Pages constraints, and unverified live deployment/preservation checks. The provisional file must never be treated as a release manifest. Preserve the existing 54 lessons, separate IELTS 1,000 bank, established production audio, and privacy protections.

## CI provenance boundary

Earlier run https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42533452770 (commit `48e50c17c9ca728615b4a3375eedc1c431346618`) was reported successful; that result is **not** a test of this new document or a production release. Confirm job-level conclusions and logs for the exact new commit before claiming fresh CI success.
