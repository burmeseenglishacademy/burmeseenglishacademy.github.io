# BEA 1,000 — seven B2 exact-sense / British English review leads (2 November 2026)

**Scope:** user-approved **1,000 total**, A1/A2/B1/B2/C1 **200 each**; the superseded 5,000-word plan is not active. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED / STAGING ONLY. The frozen [1,000-word first-pass shortlist](draft/CEFR-1000-PROVISIONAL-SHORTLIST.json) and independent review tasks remain unchanged.

## Evidence provenance and sense conflicts

On **2026-11-02**, all seven linked **Oxford Advanced Learner's Dictionary** headword pages were opened directly and the exact sense and line ranges recorded in the [seven-card research packet](draft/CEFR-1000-B2-SEVEN-QUOTE-TIE-RAW-LIFT-SHOCK-SILENCE-CABINET-EXACT-SENSE-2026-11-02.json). Cambridge Dictionary CEFR labels below came from **public search-index excerpts**, not a direct publisher-page opening: direct Cambridge page requests returned **HTTP 403**. These are publisher leads, **not independent human CEFR approval**.

| Frozen B2 word | Source and observed sense | Editorial action, NOT approved |
|---|---|---|
| [raw](https://www.oxfordlearnersdictionaries.com/definition/english/raw_1) | Oxford lines 107–127 distinguish food from natural materials. [Cambridge indexed English](https://dictionary.cambridge.org/dictionary/english/raw) **B1** for uncooked food, **B2** for unprocessed materials. | Frozen chicken example is the B1 food sense; split the two senses and adjudicate level. |
| [lift](https://www.oxfordlearnersdictionaries.com/definition/english/lift_1) | Oxford 113–126; [Cambridge indexed English](https://dictionary.cambridge.org/dictionary/english/lift) **B1** for raise verb. | Frozen heavy-crate example is literal raise, not British lift (elevator) noun. |
| [shock](https://www.oxfordlearnersdictionaries.com/definition/english/shock_1) | Oxford 106–125; [Cambridge indexed English](https://dictionary.cambridge.org/dictionary/english/shock) **B1** for sudden emotional-surprise noun, **B2** for different verb senses. | Frozen news-as-a-shock example selects B1 noun, not B2 verb or electrical/medical shock. |
| [silence](https://www.oxfordlearnersdictionaries.com/definition/english/silence_1) | Oxford 107–113 and 146–153 distinguish uncountable quiet from a countable pause; [Cambridge indexed English](https://dictionary.cambridge.org/dictionary/english/silence) **B1** uncountable quiet, **B2** countable period. | Frozen definition is B1 quiet; example *a sudden silence* can evoke a pause. Resolve the sense mismatch and countability before retiering. |
| [quote](https://www.oxfordlearnersdictionaries.com/definition/english/quote_1) | Oxford 113–138 documents verb repeating exact words; nearby Literature and writing **b1** is a **topic label**, not an exact-sense CEFR badge. Commercial price quotation is another sense. | Do not turn topic b1 into independent word/sense level evidence. Source-backed exact-sense review still required. |
| [tie](https://www.oxfordlearnersdictionaries.com/definition/english/tie_1) | Oxford 113–123 documents fastening with string/rope; Cambridge indexed [English headword](https://dictionary.cambridge.org/dictionary/english/tie) showed no reliable exact-sense CEFR badge. | Keep B2 level unsubstantiated pending independent CEFR evidence; verify tied/tying British pronunciation separately. |
| [cabinet](https://www.oxfordlearnersdictionaries.com/definition/english/cabinet) | Oxford 149–156 furniture, 105–123 government. [Cambridge **Learner's Dictionary** indexed furniture entry](https://dictionary.cambridge.org/dictionary/learner-english/cabinet) **B2**; Oxford furniture **Houses and homes c1** and government **Politics c1** are **topic labels**, not exact-sense badges. | Provisional B2 furniture sense has a weaker B2 indexed alignment control; distinguish government Cabinet and never claim Oxford C1 exact-sense classification. |

**British English and Myanmar QA:** The packet preserves all seven original English definitions, Myanmar meanings, example sentences, source indexes, original Git blob provenance, and seven *unapproved* bilingual/example alternatives. Specific review priorities are noun countability for **silence**, word-class separation for **shock/lift/cabinet**, food versus industrial materials for **raw**, commercial versus citation meanings for **quote**, and natural collocation/translation for **tie**. Human reviewers must check fluent Myanmar and grammatical examples without accepting any AI self-review as independent signoff.

## Fail-closed mechanical safeguards

[Seven-card auditor](tools/audit_cefr_1000_b2_seven_uk_sense_conflicts.py) pins Git blob hashes for the research packet, original source and 1,000-word shortlist. It enforces exactly 200 unique headwords per level, seven original B2 source-bound records, false independent-review flags, exact publisher URL/access distinctions, date and line locators, substantive English/Myanmar/example alternatives and no fabricated exact-sense Oxford CEFR badges. Synthetic adversarial mutation tests exercise forged reviewer approvals, source paths, language fields, counts, levels and audio claims. The auditor is wired into six parallel **A1/A2/B1/B2/C1/ALL** structural lanes and the documentary **NO DEPLOY** gate. Passing these mechanical tests would not establish semantic accuracy, independent human review, actual listening or physical iPhone testing.

Staging research packet commit `dea6dbbdc10f6e695a24762d4afc53d87f830966`; auditor commit `47131b2b7a6749c28f1369f6ca802f37fc31d044`; parallel workflow commit `ba12e69cf83d97da900e45e242914b79f5df5eed`; documentary workflow commit `0d301f0bb6e102d660b07c3eb77bac063588270e`. Newly triggered [structural run 41387302604](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41387302604) and [documentary run 41387306474](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41387306474) require actual job conclusions and logs before claiming pass.

## Exact release status

| Level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**Missing essential gates:** independent English, Myanmar, example and source-backed exact-sense CEFR approval for all 1,000; signed final manifest; complete George/Emma British headword and example recordings with **real listening** signoffs; desktop/mobile browser regression; real physical iPhone Safari review; measured GitHub Pages hosting limits; release authorization; confirmed live production deployment; final preserved-asset verification. The 54 lessons, separate IELTS 1,000-word bank, existing George/Emma production audio, privacy and main branch are protected and were not edited. **Do not merge, deploy or notify.**

## Verified post-integration GitHub Actions evidence — 2 November 2026

**Structural [run 41387302604](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41387302604): SUCCESS**, testing staging workflow SHA `ba12e69cf83d97da900e45e242914b79f5df5eed`. Actual six job conclusions **A1, A2, B1, B2, C1, ALL = SUCCESS**. ALL job **125090876450** log explicitly reports seven held records, four B2-vs-indexed-B1 sense conflicts, one B2 indexed alignment, two unsubstantiated CEFR leads, zero approvals and **236/236 synthetic mutations rejected**; ALL artifact **13116340810**. The B2 job **125090876464** separately passed the seven-card structural check.

**Documentary [run 41387306474](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41387306474): SUCCESS** at staging SHA `0d301f0bb6e102d660b07c3eb77bac063588270e`. Actual job **125090887167** log confirmed **236/236** synthetic rejections and explicitly reported **0/1000 independent source reviews, 0/1000 both-voice listening**, missing approved manifest, real mobile/physical iPhone QA, measured hosting evidence, final protected-assets verification and release signoff. It also reported **PASS: protected production assets untouched by staging migration**; blocker artifact **13115414571**. This workflow is documentary and does **not deploy**.

These CI results are **mechanical source/flag integrity tests only**, not independent linguistic verification, human review, actual audio listening, physical iPhone Safari testing or permission to publish. **RELEASE BLOCKED — STAGING ONLY.**
