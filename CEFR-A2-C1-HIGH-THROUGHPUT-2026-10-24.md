# Burmese English Academy — high-throughput A2–C1 editorial checkpoint
**Date:** 24 October 2026 (Singapore)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release:** BLOCKED — staging-only, unpublished and independently unapproved.

## Concrete work performed

1. Added **100 original bilingual editorial drafts**: 25 each in A2, B1, B2 and C1, each with a newly written English learner definition, natural Burmese first-pass meaning, part of speech, and grammatical example. All five independent review flags remain **false**. Added no audio.
2. Total first-pass draft inventory is **284 of 4,500 A2–C1 targets** (**A2 71/700; B1 71/1,000; B2 71/1,300; C1 71/1,500**). **4,216** still have no first-pass bilingual draft. The separate 500 A1 candidate inventory is also NOT proven independently reviewed.
3. Added **four** Cambridge word-specific CEFR/sense observations: `damage` B1 noun (aligned), `overall` B2 adjective (**conflicts** with provisional B1), `peak` B2 noun in the highest-value sense (aligned), and `automatically` B2 adverb (aligned). The evidence file now contains **21** unapproved observations, **8** provisional CEFR conflicts. Cambridge page text and markers were visible in search-index results; attempted direct page opens returned HTTP 403. This is **not** independent editorial or Burmese-translation review.
4. Added `draft/A2-C1-CANDIDATE-QUARANTINE.json` with **20 undrafted candidates held for manual editorial triage**: **3** sourced CEFR conflicts (`government` provisional A2 / observed B1; `protein` B2 / C1; `toxic` C1 / B2), **7** problematic WordNet-first-sense clues, and **10** likely proper names/brand/place names. These are holds for review, not definitive rejection or correction of levels.
5. Added `tools/list_cefr_editorial_priority.py` and its staging-only CI preview to exclude known risky headwords from the next high-throughput drafting queue. Added `tools/audit_cefr_quarantine.py` and quarantine CI to reject premature drafting or approval of held entries.
6. Strengthened `tools/audit_cefr_a2_c1_drafts.py` to detect duplicate examples and examples lacking the literal headword/inflection spelling. **This is a basic text heuristic, not a grammar or semantic assessment.** The 284 drafts passed the structural checks.
7. Existing 45 unpublished 100-word review packets continue to cover all **4,500** provisional A2–C1 candidate positions, now containing the **284** initial bilingual drafts and **21** word-specific observations. Review packets are not completed vocabulary.

## Executed CI evidence

- [Original bilingual draft/source structural QA — 40054000045](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40054000045): **success**, 284 drafts / 21 observations / 8 flagged level conflicts; no false approvals.
- [45 unpublished review packets — 40053875589](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40053875589): **success**, 4,500 candidates, 4,216 lacking first drafts.
- [Four parallel A2/B1/B2/C1 QC jobs — 40053875616](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40053875616): **all four success**.
- [Quarantine holdout validation — 40053912944](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40053912944): **success**, 20 held, 3 documented source-level conflicts.
- [Curated candidate preview — 40053961012](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40053961012): **success**, shortlist for future editorial work, not CEFR approval.

**Intermediate CI failures were found and repaired:** initial 100 new entries did not match the pre-existing provenance-prefix assertion, and the four new source observations did not use the existing canonical URL/source-name schema. Repaired in staging; the final source and draft QA run above passed. Do not describe earlier failed commits as passing.

## Remaining release blockers

- **0 independently approved** A2–C1 English senses, Burmese meanings, grammatical examples, CEFR levels or pronunciation checks. Cambridge sense-level observations do not imply approval.
- **4,216** first-pass bilingual A2–C1 drafts still to prepare, plus independent sense-by-sense review and any curriculum headword replacement/reclassification. All 5,000 words, including A1, must meet final acceptance criteria.
- No complete new George/Emma vocabulary audio set or individual pronunciation-listening QA. Existing British audio remains untouched.
- Browser/mobile accessibility and real physical iPhone Safari regression, full host storage/bandwidth checks, production deployment and live checks of the **new 5,000-word release** are **not completed**.
- `main` remains at `dca0db7aa30118ecc18350db8dc406e6cac91554`; existing 54 lessons, separate IELTS 1,000 vocabulary and George/Emma audio are preserved. No changes to live Firebase or production were made.

## Specific word-level evidence references (observations, not independent approvals)

- [damage](https://dictionary.cambridge.org/dictionary/english/damage): B1 noun, physical harm.
- [overall](https://dictionary.cambridge.org/dictionary/english/overall): B2 adjective, considering everything (provisional B1 **conflict**).
- [peak](https://dictionary.cambridge.org/dictionary/english/peak): B2 noun, highest level/value (mountain-top noun has a different level).
- [automatically](https://dictionary.cambridge.org/dictionary/english/automatically): B2 adverb, without human control.
- [government](https://dictionary.cambridge.org/dictionary/learner-english/government): B1 noun for official governing group; provisional A2 candidate held.
- [protein](https://dictionary.cambridge.org/dictionary/english/protein): C1 food/body-substance noun; provisional B2 candidate held.
- [toxic](https://dictionary.cambridge.org/dictionary/english/toxic): B2 poisonous adjective; provisional C1 candidate held.

**No release announcement is justified.** Preserve staging-only status until independent review, all audio and real-device tests, production deployment and live checks have actual evidence.
