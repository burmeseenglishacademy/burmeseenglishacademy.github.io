# CEFR-1000 A1 article variants: source-backed editorial adjudication (15 November 2026)

**Staging research only. Not an independent review, approval, CEFR release certification, or change to the provisional shortlist.**

## Immutable shortlist provenance
- Repository: `burmeseenglishacademy/burmeseenglishacademy.github.io`; branch `cefr-5000-bilingual-qa-staging`.
- Provisional shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- A1 global entry indices 0 and 1: `a` and `an`, both tagged `article`, both editorial_hold=true and all reviewed flags false.
- Both source records: `draft/A1-EDITORIAL-STARTER.json`, source indices 0 and 1, source blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- Current provisional examples: `I have a book.` and `She has an apple.`; existing Myanmar meanings are explanatory glosses rather than independently checked usage translations.

## Evidence observed 2026-11-15 (URLs and scope)
1. Cambridge English Dictionary, **an**: https://dictionary.cambridge.org/us/dictionary/english/an — explicitly marks the determiner `an` **A1** and describes its use before a vowel **sound**. This supports the exact `an` determiner form and a narrow A1 sense, not independent review of this project's Myanmar or examples.
2. Cambridge Grammar, **A/an and the**: https://dictionary.cambridge.org/grammar/british-grammar/a-an — `a` and `an` are forms of the indefinite article; selection depends on following **sound**, not initial letter. Gives `a university` versus `an hour`. This is grammar evidence, not an entry-specific CEFR label.
3. British Council LearnEnglish, **The indefinite article: 'a' and 'an'**: https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/indefinite-article — categorized **beginner**; confirms singular noun contexts, non-specific reference and consonant/vowel sound distinction. 'Beginner' is not itself proof of an exact CEFR A1 sense.

## Editorial decision needed (not decided here)
The target requires **200 deduplicated headwords/senses per level**. `a` and `an` are distinct orthographic forms, but they express the same indefinite-article function in complementary phonological environments. A headword-only uniqueness check will pass both and **cannot** resolve sense-level duplication. An independent English/CEFR reviewer must decide whether to retain two separate pedagogical form entries with explicitly distinct form-use senses, or treat them as one grammatical lexeme and select a genuine replacement A1 entry. Do **not** silently delete either entry or fill its slot with a fabricated word.

## Proposed unapproved editorial candidates
- `a`: English: "The form of the indefinite article used before a consonant sound when referring to one non-specific person or thing." Myanmar: "နာမ်ရှေ့ရှိ နောက်စကားလုံး၏ အစသံက ဗျည်းသံဖြစ်သောအခါ သုံးသည့် မတိကျသေးသော တစ်ဦး/တစ်ခုကို ညွှန်းသည့် article ပုံစံ။" Original example: "She bought a uniform for school." (The `u` in `uniform` begins with /j/, a consonant sound.)
- `an`: English: "The form of the indefinite article used before a vowel sound when referring to one non-specific person or thing." Myanmar: "နာမ်ရှေ့ရှိ နောက်စကားလုံး၏ အစသံက သရသံဖြစ်သောအခါ သုံးသည့် မတိကျသေးသော တစ်ဦး/တစ်ခုကို ညွှန်းသည့် article ပုံစံ။" Original example: "We waited for an hour." (`hour` begins with a vowel sound despite its written `h`.)
- These Burmese descriptions are draft explanatory glosses, not certified natural Myanmar translations. An independent Myanmar reviewer should decide whether to replace technical phrasing with learner-friendly bilingual notes and test naturalness. In both cases, do not imply `a/an` is always a literal numerical `one`.

## Specific regression / signoff requirements
- Sense-level deduplication must inspect normalized grammatical function and complementary forms, not only Unicode-casefolded spelling.
- Reviewer records should identify BOTH entry IDs, precise form/use contrast, source URLs, observation date, and final keep/merge/replace rationale. Require separate independent English, Myanmar, example and source-backed CEFR attestations bound to final content digest.
- Grammar negative cases: `an university` and `a hour` must be rejected; `a university`, `an hour` accepted. Avoid `a water` as an unqualified mass-noun example.
- Do not change `reviewed_*`, `release_approved`, audio or release metadata. No current human signoff, audio listening, physical iPhone testing, hosting clearance or deployment is asserted.

## Staging inventory at observation
| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

All 1,000 remain on editorial hold. This research does not alter any of those counts.
