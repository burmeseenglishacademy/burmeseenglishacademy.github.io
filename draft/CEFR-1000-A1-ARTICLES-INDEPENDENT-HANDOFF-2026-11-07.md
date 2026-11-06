# CEFR-1000: A1 articles and independent-review handoff (7 November 2026)

**Scope:** 1,000 TOTAL words, exactly 200 each at A1/A2/B1/B2/C1. Staging only. No editorial or independent approval implied.

## Reproducible provenance
- Inventory: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; observed Git blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551` on 2026-11-07.
- Review tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`; observed blob SHA `88f472e4c79e5e9b6ae5957f5244f9cb60dc0ef2`. GitHub fetch_file returned an **empty content field**: this is NOT evidence that tasks do not exist. Obtain full bytes before relying on it.
- A1 provisional source: `draft/A1-EDITORIAL-STARTER.json`, blob SHA `ff1e93f60828ef2f94c9146522ce94075183b0ae` (as embedded in shortlist). These source paths and SHAs are provenance, not CEFR validation.

## Exact-sense editorial triage: indefinite articles
| Headword | Provisional A1 English definition | Myanmar provisional | Provisional example | Specific concern |
| --- | --- | --- | --- | --- |
| a | Used before one person or thing when it is not specified. | တစ်ခု၊ တစ်ယောက် (မသတ်မှတ်ရသေးသော) | I have a book. | Singular count nouns, first mention and phonetic **consonant sound** condition are not fully expressed; 'one person or thing' alone is insufficient. |
| an | Used before one person or thing when the next word starts with a vowel sound. | တစ်ခု၊ တစ်ယောက် (သရသံဖြင့်စသော စကားလုံးရှေ့တွင်) | She has an apple. | Should explicitly specify **singular countable noun phrase** and sound rather than spelling. Example is grammatical but tests only an uncomplicated vowel-initial noun. |

**Proposed editorial candidates only, not replacement text or independently checked:**
- `a`: “Used before a singular countable noun when introducing someone or something not identified, usually before a consonant sound.” Myanmar candidate: “တိတိကျကျ မသတ်မှတ်ထားသေးသော ရေတွက်နိုင်သည့် အနည်းကိန်းနာမ်ရှေ့တွင် ဗျည်းသံဖြင့် စသောအခါ သုံးသော စကားလုံး။”
- `an`: “Used before a singular countable noun when introducing someone or something not identified, before a vowel sound.” Myanmar candidate: “တိတိကျကျ မသတ်မှတ်ထားသေးသော ရေတွက်နိုင်သည့် အနည်းကိန်းနာမ်ရှေ့တွင် သရသံဖြင့် စသောအခါ သုံးသော စကားလုံး။”
- Original additional test examples for reviewer evaluation: “She is an engineer.” “He is a university student.” “It took an hour.” These distinguish pronunciation from initial letters; they are NOT substitutes for the original example without review.

## External publisher lookup queue (NOT observed or validated in this run)
- Cambridge Dictionary, `a`: https://dictionary.cambridge.org/dictionary/english/a
- Cambridge Dictionary, `an`: https://dictionary.cambridge.org/dictionary/english/an
- British Council LearnEnglish grammar, articles: https://learnenglish.britishcouncil.org/grammar/english-grammar-reference/articles-a-an-the

The above URLs are **lookup targets only**, not citations for verified CEFR labels. A reviewer must capture publisher, access date, exact grammatical sense, CEFR label if actually present, and any mismatch before assigning source-backed review. Do not infer a CEFR label from the dictionary headword or from an unlabeled grammar page.

## Independent review acceptance checklist
For EACH entry: (1) independently verify English sense and part of speech; (2) independently assess fluent Myanmar translation, meaning and register; (3) check example grammar, originality and exact sense; (4) capture actual publisher sense-level CEFR evidence with URL/date, or mark unsupported; (5) British pronunciation and audio script review; (6) record reviewer identity, evidence timestamp and signoff in the approved review workflow. Editorial self-assessment never counts as independent verification.

## Fail-closed release status as of this observation
| Level | First-pass written | Independently approved |
| --- | ---: | ---: |
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

Existing negative-test workflow run [42171173516](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42171173516), head `9ded2d49c87f8b28bbc653ce5b6da2f6293bee7f`, has five **successful** level-specific jobs (A1 job 127739084193; A2 127739084475; B1 127739084439; B2 127739084470; C1 127739084342). These only demonstrate tested guard rejection behaviour, not a successful release gate for this documentation commit.

Blocked: independent English/Myanmar/example/source-backed CEFR signoff (0/1000); final-shortlist George and Emma headword + sentence audio generation and actual listening signoff (unverified); browser/mobile regressions (unverified); physical iPhone Safari testing (unverified); GitHub Pages limits and hosting clearance (unverified); verified live deployment (not performed). Preserve 54 lessons, separate IELTS 1,000 bank, established George/Emma production assets and privacy protections. **Do not merge or publish.**
