# CEFR-1000 targeted exact-sense and morphological false-positive review — 2026-11-04

**Scope:** staging-only, frozen provisional shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Observed 2026-11-04. **Not independent review; no entry approved.** This document contains source-text observations, not externally corroborated CEFR classifications.

## Exact source records
| Headword | Proposed CEFR | POS | First-pass definition | First-pass Myanmar | First-pass example |
|---|---|---|---|---|---|
| i | A1 | pronoun | The person who is speaking or writing. | ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား) | I am a student. |
| is | A1 | verb | The present form of be used with he, she, it or a singular subject. | ဖြစ်တယ်၊ ရှိတယ် (အနည်းကိန်းနှင့်တွဲသုံး) | She is at home. |
| like | A1 | verb | To enjoy or feel pleased about something. | ကြိုက်နှစ်သက်သည် | I like this song. |
| likely | A2 | adjective | Expected to happen or probably true. | ဖြစ်နိုင်ခြေများသော | It is likely to rain before evening. |
| train | A1 | noun | A set of connected vehicles that travels on railway tracks. | ရထား | The train arrives at nine. |
| training | A2 | noun | The process of learning skills needed for a job or activity. | လေ့ကျင့်သင်ကြားမှု | New workers receive safety training. |
| month | A1 | noun | One of the twelve parts of a year. | လ၊ တစ်လ | Next month is December. |
| monthly | B2 | adjective | Happening or produced once every month. | လစဉ်ဖြစ်သော | Our monthly meeting takes place on Friday. |
| actual | B1 | adjective | Real, rather than planned, expected, or imagined. | အမှန်တကယ်ဖြစ်သော | The actual cost was lower than our estimate. |
| actually | A2 | adverb | Used to say what is true, especially when it differs from what someone expected. | တကယ်တော့၊ အမှန်တကယ် | I thought it was Tuesday, but it is actually Wednesday. |
| exact | B2 | adjective | Completely correct or precise, without approximation. | အတိအကျဖြစ်သော | Please record the exact weight of each package. |
| exactly | A2 | adverb | In a completely correct or precise way. | တိတိကျကျ၊ အတိအကျ | Please tell me exactly where to meet you. |
| complex | B1 | adjective | Made of many connected parts and difficult to understand. | ရှုပ်ထွေးသော၊ အစိတ်အပိုင်းများစွာပါဝင်သော | The engineer explained the complex process clearly. |
| complexity | C1 | noun | The state of having many connected parts that are difficult to understand. | ရှုပ်ထွေးမှု | The complexity of the contract delayed the agreement. |
| consistent | B2 | adjective | Remaining at a similar standard or following the same pattern over time. | တစ်သမတ်တည်းဖြစ်သော | His results have been consistent throughout the year. |
| consistently | C1 | adverb | In the same way or to the same standard over time. | အမြဲတစေ တစ်သမတ်တည်း | The factory consistently meets its quality targets. |
| server | B2 | noun | A computer that provides data or services to other computers. | ကွန်ပျူတာများကို ဒေတာ သို့မဟုတ် ဝန်ဆောင်မှုပေးသည့် ဆာဗာ | The server stores customer records securely. |
| serve | B1 | verb | To provide food or drinks to someone. | အစားအစာ၊ သောက်စရာ တည်ခင်းပေးသည် | They serve breakfast from seven o'clock. |

## Editorial decisions to investigate (not approved changes)
- `i`: canonical standalone first-person pronoun should be written `I`. Check capitalization in headword, example, search index, audio filename mapping, and case-normalized uniqueness. Do not silently modify the frozen source.
- `is` vs `i`: mechanical stripping of terminal `s` creates a **false morphological family**. Their distinct grammatical roles and senses require separate reviews.
- `like` vs `likely`: shared spelling does not license transferring CEFR placement or meanings; verify distinct adjective and verb senses with publisher evidence.
- `train` (rail vehicle) vs `training` (skill acquisition): despite superficial morphological relation, the shortlisted senses are semantically distinct. Do not transfer the level from noun `train` to noun `training`.
- `month` / `monthly`, `actual` / `actually`, `exact` / `exactly`, `complex` / `complexity`, `consistent` / `consistently`: plausible lexical families, but derivational family membership **does not prove equal CEFR level**. Seek publisher-backed exact POS/sense evidence for each entry.
- Check Myanmar translations for the *listed* POS and sense rather than generic dictionary synonyms; ensure examples actually illustrate the specified meaning and are natural, grammatical, original sentences.
- No automated stemmer or word-family grouping should mark a cross-level conflict as resolved. Review records must distinguish `false_positive`, `related_distinct_sense`, and `needs_evidence`.

## Evidence and release controls
- Required future independent review: English definition, Myanmar meaning, original example, POS/sense-specific publisher CEFR source, and human reviewer identity/signoff, with source URL, observation date, and provenance.
- Research starting points **not consulted for this report**: https://dictionary.cambridge.org/ ; https://www.oxfordlearnersdictionaries.com/ ; https://www.englishprofile.org/ . Do not represent these links as confirmed sense-level evidence.
- Counts remain A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0 (first-pass/independently approved). All 1,000 editorial holds remain.
- Audio: 4,000 final George/Emma headword/example recordings plus real listening signoff unverified. Browser/mobile and physical iPhone Safari evidence, GitHub Pages hosting review and production deployment unverified.
- This report makes no edits to the shortlist, review flags, production, 54 lessons, IELTS bank, or established production audio.
