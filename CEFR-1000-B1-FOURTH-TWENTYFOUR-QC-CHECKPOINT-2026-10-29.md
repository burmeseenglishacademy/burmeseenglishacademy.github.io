# CEFR 1,000 — fourth B1 Oxford 24-word source and QA checkpoint (29 October 2026)

**BLOCKED / STAGING ONLY.** Approved project scope remains **exactly 1,000 provisional entries**, A1/A2/B1/B2/C1 **200 each**. Work branch: `cefr-5000-bilingual-qa-staging` (branch name retained). This is publisher word/POS research and content-integrity QA, **not** independent human English/Myanmar/CEFR approval, voice listening, physical iPhone testing or deployment.

## Direct publisher research and provenance

Directly inspected the [official Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-29**. Added [24 B1-shortlist evidence records](draft/CEFR-1000-OXFORD-B1-FOURTH-TWENTYFOUR-2026-10-29.json) containing publisher URL, observation date, PDF page (one-based), extracted text line (zero-based), short verbatim word/POS entry, original English definition, Myanmar meaning, example, source path/index/blob SHA, editorial risk and a separate independent-review task. Frozen provisional shortlist Git blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

**Oxford word/POS-level findings:** A1 **2**, A2 **10**, B1 **11**, B2 **1**. This means **13 of the 24** differ from the provisional B1 placement at word/POS level; **12 are lower** (2 A1 + 10 A2) and **1 is higher** (B2). No automatic re-tiering. Publisher word/POS labels are not proof of the intended dictionary exact sense or CEFR; all 24 retain editorial hold.

| Draft B1 headword | Draft POS | Oxford word/POS level | PDF page:line | Exact-sense or editorial issue |
|---|---|---|---|---|
| `worst` | adjective | A2 | 7:1776 | SUPERLATIVE_A2_VS_B1 |
| `anyway` | adverb | A2 | 4:947 | CONCESSION_A2_VS_B1 |
| `direct` | verb | B1 | 8:1977 | DIRECT_VERB_GUIDE_VS_ADVERB |
| `dream` | noun | A2 | 5:1145 | DREAM_SLEEP_VS_ASPIRATION |
| `easily` | adverb | A2 | 5:1153 | EASILY_WITHOUT_DIFFICULTY_A2 |
| `luck` | noun | A2 | 6:1374 | LUCK_CHANCE_VS_GOOD_FORTUNE |
| `marriage` | noun | B1 | 9:2208 | MARRIAGE_LEGAL_STATE_VS_MARRIED_LIFE |
| `fighting` | noun | B1 | 8:2060 | FIGHTING_PHYSICAL_CONFLICT_VS_OPPOSITION |
| `rich` | adjective | A1 | 3:653 | RICH_WEALTH_A1_VS_B1 |
| `skin` | noun | A2 | 6:1624 | SKIN_BODY_COVERING_A2_VS_B1 |
| `damage` | noun | B1 | 8:1959 | DAMAGE_NOUN_VS_VERB |
| `directly` | adverb | B1 | 8:1978 | DIRECTLY_WITHOUT_INTERMEDIARY_VS_IMMEDIATELY |
| `doubt` | noun | B1 | 8:1989 | DOUBT_NOUN_COLLOCATION |
| `crime` | noun | A2 | 5:1093 | CRIME_GENERAL_VS_SPECIFIC_OFFENCE |
| `fully` | adverb | B2 | 11:2880 | FULLY_COMPLETELY_B2_VS_B1 |
| `male` | adjective | A2 | 6:1378 | MALE_ADJECTIVE_VS_NOUN_MYANMAR |
| `plant` | noun | A1 | 3:601 | PLANT_LIVING_ORGANISM_VS_FACTORY |
| `reality` | noun | B1 | 9:2355 | REALITY_FACT_VS_ACTUAL_CONDITIONS |
| `spot` | noun | B1 | 9:2458 | SPOT_MARK_VS_PLACE |
| `agreement` | noun | B1 | 7:1800 | AGREEMENT_DOCUMENT_VS_MUTUAL_ASSENT |
| `award` | noun | A2 | 4:974 | AWARD_NOUN_A2_VS_VERB_B1 |
| `eventually` | adverb | B1 | 8:2031 | EVENTUALLY_AFTER_TIME_VS_FINAL_RESULT |
| `challenge` | noun | B1 | 7:1885 | CHALLENGE_DIFFICULT_TASK_VS_CONTEST |
| `comment` | noun | A2 | 4:1065 | COMMENT_NOUN_A2_VS_VERB_B1 |

**High-priority cases:** `award` is an A2 noun in the Oxford list but has a separate B1 verb entry; `comment` similarly has an A2 noun and B1 verb. `fully` is Oxford B2 (higher than draft B1). `rich` and `plant` are Oxford A1; `worst`, `anyway`, `dream`, `easily`, `luck`, `skin`, `crime`, `male`, `award` and `comment` are A2. Review `marriage` for legal relationship versus married life, `agreement` for arrangement versus signed document, `doubt` for idiomatic noun collocation, and `male` for adjective-versus-noun Myanmar register. These are editorial tasks, not final corrections.

## Cross-publisher exact-sense research leads (NOT direct verification)

Cambridge Dictionary publisher-indexed search results on **2026-10-29** identify four sense-labelled leads. **Direct Cambridge dictionary page fetches returned HTTP 403**, so these are search-indexed observations only and cannot qualify as independent exact-sense review receipts. They are preserved with URLs, dates, sense headings and source-access limitations in the same research packet.

| Word | Oxford word/POS | Cambridge indexed exact-sense lead | Review implication |
|---|---|---|---|
| `fully` | B2 adverb | [COMPLETELY B1](https://dictionary.cambridge.org/dictionary/english/fully) | Oxford B2 versus Cambridge B1; the B1 draft may be defensible for this sense but needs independent direct-page verification |
| `award` | A2 noun | [noun PRIZE B2](https://dictionary.cambridge.org/dictionary/english/award) | Oxford A2 versus Cambridge B2; separate prize from court/official monetary award and noun from verb |
| `comment` | A2 noun | [opinion comment noun B1](https://dictionary.cambridge.org/dictionary/english/comment) | Oxford A2 versus Cambridge B1; do not confuse with Oxford B1 verb |
| `marriage` | B1 noun | [TWO PEOPLE B1](https://dictionary.cambridge.org/dictionary/english/marriage) | Matching B1 labels at different evidence scopes; still verify legal relationship versus ceremony and duration |

## Fail-closed safeguards and actual CI

Added [B1 24-word source auditor](tools/audit_cefr_1000_oxford_b1_fourth_twentyfour.py), checking exact Oxford metadata, frozen bilingual/example snapshots, source Git provenance, word/POS distinctions, independent reviewer tasks, hold flags and rejecting hidden approval fields. Self-test has **113 authored negative mutation cases** (24 each for forged publisher excerpts, Myanmar translations, false reviewer receipts and altered editorial risks; 7 metadata mutations; 2 hidden approval fields; 8 Cambridge source-label/false-verification mutations). Structural workflow runs it in the B1 and ALL lanes of the existing six-job A1/A2/B1/B2/C1/ALL matrix; documentary no-deploy workflow also runs the self-test. The auditor cannot independently authenticate human review or publisher semantics.

**Verified actual GitHub Actions conclusions and logs:** [structural run 40740620860](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40740620860) **success** for all six A1/A2/B1/B2/C1/ALL jobs (head `840a67d66f829ecae60cb1fbd9eeee59e17cc8f1`). ALL job log confirms **24/24** Oxford B1 observations checked and **113/113** forged publisher, Myanmar, editorial, Cambridge-indexed and false-signoff mutations rejected. [Documentary no-deployment run 40740610140](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40740610140) **success as report-only** (head `ff78f7658cc6eb12468181d2ecadb7ec41d00e83`), with the same **113/113** negative tests, explicit `source-reviewed 0/1000`, both-voice listening `0/1000`, deployment false, and protected production assets diff **PASS**. Passing CI is structural evidence integrity, **not** independent CEFR/language approval or launch clearance. No release gate was bypassed.

## Exact release evidence status

| CEFR level | First-pass written | Independently checked/approved | Editorial holds |
|---|---:|---:|---:|
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |
| **Total** | **1,000** | **0** | **1,000** |

The five levels each have 200 unique provisional headwords in the inspected shortlist. All independently reviewed English, Myanmar, example and level flags remain false. **Final George/Emma both-voice headword/example listening signoffs: 0/1,000.** Independent human exact-sense review, final audio generation/listening, desktop/mobile browser regression, real physical iPhone Safari evidence, measured GitHub Pages artifact/bandwidth, production confirmation and protected-asset verification for any eventual release are still required. Existing 54 lessons, separate IELTS 1,000 bank, established George/Emma production audio and privacy assets are protected; **no main merge, publication or deployment is authorised until all gates actually pass**.
