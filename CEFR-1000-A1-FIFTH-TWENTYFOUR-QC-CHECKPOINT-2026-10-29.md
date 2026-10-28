# CEFR 1,000 — A1 fifth Oxford batch and Cambridge exact-sense triage (29 October 2026)

**BLOCKED / STAGING ONLY.** Approved scope is **1,000 total**, A1/A2/B1/B2/C1 **200 each**, NOT the superseded 5,000. All 1,000 remain on editorial hold; **zero human-independent approvals**. This report is not a human review, real audio listening, physical iPhone QA, measured hosting validation or production deployment.

## Direct publisher PDF observations (2026-10-29)

Opened [Oxford University Press's official Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and inspected the following 24 previously uncovered A1 shortlist headwords. All 24 are listed by Oxford at **A1 word/POS level**. The page is **one-based** and the extracted PDF line is **zero-based**. The source **does not verify exact sense, English wording, Myanmar fluency or original examples**.

| Draft word | Draft POS | Oxford PDF page:line | Editorial risk code |
|---|---|---|---|
| work | verb | 4:891 | WORK_EMPLOYMENT_VS_GENERAL_EFFORT |
| year | noun | 4:900 | YEAR_TWELVE_MONTHS_VS_CALENDAR_YEAR |
| love | verb | 2:455 | FAMILY_AFFECTION_VS_ROMANTIC_LOVE |
| man | noun | 2:461 | ADULT_MALE_VS_GENERIC_HUMAN_USAGE |
| use | verb | 4:842 | USE_TOOL_VS_USE_SERVICE_OR_RESOURCE |
| come | verb | 1:163 | COME_DEICTIC_DIRECTION_DEPENDS_ON_SPEAKER |
| help | verb | 2:361 | HELP_VERB_VS_NOUN_AND_ABILITY_MODAL |
| old | adjective | 3:547 | OLD_PERSON_VS_OLD_OBJECT_MYANMAR_POLYSEMY |
| little | adjective | 2:448 | LITTLE_SMALL_SIZE_VS_SMALL_QUANTITY |
| house | noun | 2:380 | HOUSE_BUILDING_VS_HOME_FAMILY |
| place | noun | 3:598 | PLACE_PHYSICAL_LOCATION_VS_ABSTRACT_POSITION |
| give | verb | 2:329 | GIVE_TRANSFER_VS_GIVE_INFORMATION |
| new | adjective | 2:516 | NEW_RECENTLY_MADE_VS_NEW_TO_SPEAKER |
| make | verb | 2:460 | MAKE_CREATE_VS_CAUSATIVE_MAKE |
| look | verb | 2:452 | LOOK_DIRECT_GAZE_VS_APPEAR |
| take | verb | 3:761 | TAKE_CHAIR_EXAMPLE_AMBIGUOUS_CARRY_VS_ACCEPT |
| very | adverb | 4:847 | VERY_DEGREE_MODIFIER_NOT_STANDALONE |
| many | determiner | 2:462 | MANY_COUNTABLE_NOUNS_VS_MUCH_UNCOUNTABLE |
| three | number | 3:797 | THREE_NUMERAL_NOT_ORDINAL_THIRD |
| small | adjective | 3:710 | SMALL_PHYSICAL_SIZE_VS_IMPORTANCE |
| big | adjective | 1:85 | BIG_SIZE_VS_IMPORTANCE_OR_AGE |
| eat | verb | 1:234 | EAT_BREAKFAST_NATURAL_COLLOCATION |
| drink | verb | 1:225 | DRINK_LIQUID_VERB_VS_NOUN |
| happy | adjective | 2:349 | HAPPY_FEELING_VS_CONGRATULATORY_WISH |

[Machine-readable dated source packet](draft/CEFR-1000-OXFORD-A1-FIFTH-TWENTYFOUR-2026-10-29.json) retains all 24 original English definitions, Myanmar meanings and example snapshots; shortlist source path/index/Git blob; Oxford PDF URL, line/page and exact short word/POS excerpts; and separate human-independent review tasks. The unchanged shortlist Git blob is `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. No shortlist text, level, hold or approval flags were changed. **Six original bilingual/example rewrite proposals** (old, little, take, year, house, love) are explicitly unreviewed and unapplied.

The previous four A1 Oxford packets covered **52 distinct A1 shortlist words** (despite some overlapping observations); these 24 new distinct words increase directly observed A1 word/POS coverage to **76/200**, not 76 independent reviews.

## Six Cambridge publisher-indexed sense leads (2026-10-29)

Retrieved Cambridge publisher-owned indexed excerpts. Direct dictionary-page opening returned **HTTP 403**. The following are **search-indexed leads only**, not directly inspected publisher pages, not authoritative proof of an independently verified exact-sense label, and not human signoff.

| Headword | Indexed sense | Indexed CEFR | Publisher dictionary |
|---|---|---|---|
| [work](https://dictionary.cambridge.org/us/dictionary/learner-english/work) | JOB | A1 | Cambridge Learner's Dictionary |
| [little](https://dictionary.cambridge.org/dictionary/learner-english/little) | SMALL | A1 | Cambridge Learner's Dictionary |
| [old](https://dictionary.cambridge.org/dictionary/learner-english/old) | LIVED LONG | A1 | Cambridge Learner's Dictionary |
| [little](https://dictionary.cambridge.org/dictionary/learner-english/little) | SHORT | B2 | Cambridge Learner's Dictionary |
| [old](https://dictionary.cambridge.org/dictionary/learner-english/old) | USED A LOT | A2 | Cambridge Learner's Dictionary |
| [old](https://dictionary.cambridge.org/dictionary/essential-british-english/old) | USED OR OWNED LONG | A1 | Cambridge Essential British English Dictionary |

**Substantive editorial finding:** the draft `work` example is occupational, while its broad effort definition should be narrowed for the A1 job sense. `little` with a dog denotes small size (indexed A1), not the short-duration sense (indexed B2). `old` with a grandfather denotes age (indexed A1), not used/owned objects. The latter used/owned sense is indexed **A2 in Cambridge Learner's Dictionary but A1 in Cambridge Essential British**; this publisher-internal classification difference requires independent reconciliation, not automatic retiering. The Oxford list alone cannot resolve these senses.

## Fail-closed safeguards and CI

Added [fifth-batch integrity auditor](tools/audit_cefr_1000_oxford_a1_fifth_twentyfour.py), binding 24 Oxford page/line/excerpts, exact original bilingual/example snapshots, historical A1 source Git blob and source index, six held rewrite proposals, six Cambridge indexed leads with explicit HTTP 403 caveats and all false-approval flags. **124 negative mutations** cover altered publisher levels/excerpts, Myanmar/examples, upstream provenance, Cambridge labels and fabricated signoff. Mechanical integrity tests are not independent review.

The auditor is invoked in six parallel A1/A2/B1/B2/C1/ALL structural jobs and the documentary **no-deployment** workflow. [Documentary run 40770635890](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40770635890), head `df404e9541182069f4d397dc96be591e12b265e9`, completed **SUCCESS as report-only**; actual job log confirmed **124/124** negative mutations rejected, **0/1,000** independently source-reviewed, **0/1,000** both-voice listening receipts, production not confirmed, and protected production diff **PASS**. [Structural run 40770651445](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40770651445), head `1831a5cd7ded540433b659a17698eb43747fa36e`, completed **SUCCESS**, with actual job conclusions **SUCCESS for all six A1/A2/B1/B2/C1/ALL lanes**. The ALL job log confirmed **124/124** rejected and protected production paths unchanged. Earlier [structural run 40770361318](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40770361318) did pass all six jobs before the six Cambridge leads were added.

An intermediate documentary run [40770621670](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40770621670) **FAILED** due to a Python `false` literal in the new frozen Cambridge data; corrected to `False` in staging commit `df404e9541182069f4d397dc96be591e12b265e9` and verified in successful documentary run above. Do not relabel the failed run as passed.

## Exact release blockers

| Level | First-pass written | Independently checked/approved | Editorial hold |
|---|---:|---:|---:|
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |
| **Total** | **1,000** | **0** | **1,000** |

Final George/Emma both-voice real listening receipts: **0/1,000**. No claim that all 4,000 final clips exist or were listened to. Missing human-independent English/Myanmar/example/exact-sense CEFR review; final voice generation/listening; complete desktop/mobile regression; real physical iPhone Safari QA; measured GitHub Pages hosting size/bandwidth; authenticated approved manifest; and confirmed live production deployment. The existing 54 lessons, separate IELTS 1,000-word bank, established George/Emma audio, privacy and main branch were not altered. **No merge, publish or deployment.**
