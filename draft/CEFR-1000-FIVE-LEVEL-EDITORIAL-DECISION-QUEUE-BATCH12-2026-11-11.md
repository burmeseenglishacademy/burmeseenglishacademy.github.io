# CEFR-1000 five-level editorial decision queue — 2026-11-11 (batch 12)

**STAGING ONLY — NOT VERIFIED — DO NOT PUBLISH.** Scope: exactly 1,000 entries, 200 each at A1, A2, B1, B2, C1. This dossier records direct provisional-text observations and *proposed* human-review tasks, not independent language, source, or CEFR approval.

## Provenance and method
Observed 2026-11-11 from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` on `cefr-5000-bilingual-qa-staging`, Git blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Entries below retain their original starter path and index. Candidate changes must not be applied to the released manifest until independent English, Myanmar, example, and exact-sense publisher CEFR review is complete. No publisher page was inspected in this batch; do **not** interpret publisher lookup destinations as evidence.

| Level | Headword / POS | Starter index | Directly observed issue | Proposed reviewer action |
|---|---|---:|---|---|
| A1 | `drink` / verb | 75 | English definition “To take a liquid into your mouth and swallow it” and example “They drink tea every morning” align; Myanmar `သောက်သည်` is natural, but sense boundary with the noun and alcoholic-drink usage remains unspecified | Retain basic beverage verb sense provisionally; record exact verb sense and CEFR evidence, confirm example is original and age-appropriate |
| A2 | `human` / adjective | 469 | Definition “Relating to people rather than animals or machines” frames a contrast; example “Human decisions can sometimes be difficult” does not explicitly show the contrast and could be interpreted as a broad modifier | Independent reviewer to test clearer example (e.g. “Human judgement is needed when the computer makes a mistake”) for naturalness and pedagogical fit; check Myanmar `လူသားနှင့်ဆိုင်သော` register |
| B1 | `economy` / noun | 311 | Definition describes an economic system in a place, example “Tourism plays an important role in the island's economy”; Myanmar `စီးပွားရေးစနစ်၊ နိုင်ငံ့စီးပွားရေး` may suggest a *national* economy despite an island/local example | Consider `ဒေသတစ်ခု၏ စီးပွားရေး` as a context-aligned Myanmar alternative, subject to independent fluency review; establish exact noun sense and level |
| B2 | `defeat` / verb | 328 | Definition “To win against someone in a contest, game, or conflict” describes the winner's action; example “The visiting team managed to defeat the champions” is aligned, but English explanation may obscure the direct-object construction and opponent as the one defeated | Test candidate “To win against an opponent in a game, competition, or conflict” and confirm `အနိုင်ယူသည်၊ ရှုံးနိမ့်စေသည်` is appropriate for the selected sense; independent grammar/level check |
| C1 | `additionally` / adverb | 461 | Example “The course covers safety; additionally, it includes practical training” is grammatical but fairly formal; CEFR classification for this exact linking-adverb use has not been established | Request exact POS/sense publisher evidence; independent reviewer to assess punctuation, Myanmar `ထို့အပြင်၊ နောက်ထပ်အနေဖြင့်`, and whether example suits the intended learner level |

All four A2–C1 entries above derive from `draft/A2-C1-EDITORIAL-STARTER.json`; A1 derives from `draft/A1-EDITORIAL-STARTER.json`. The source indices are `source_index` values, **not** row numbers in the provisional shortlist. These observations do not establish publisher CEFR classifications.

## Publisher evidence collection checklist (not yet observed)
For each entry, reviewers should inspect the exact headword, POS and sense in a reputable learner dictionary, preserve the full canonical URL, access date, dictionary edition or version if given, and an exact locator or short excerpt. Suggested starting points for research (unverified as exact-sense pages): https://www.oxfordlearnersdictionaries.com/ and https://dictionary.cambridge.org/ . If no publisher explicitly supports the proposed CEFR for that exact sense, record `CEFR_UNSUBSTANTIATED` and block approval rather than inferring it from general familiarity.

## Release ledger, observed metadata only
| Level | First-pass written | Independently checked/approved | Remaining on editorial hold |
|---|---:|---:|---:|
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |

Audio: shortlist metadata says final George/Emma audio **not generated / not listened**. Required eventual inventory: 4,000 artifacts and 4,000 genuine content-bound listening attestations. Browser/mobile, physical iPhone Safari, hosting, production deployment and production-asset preservation are not verified in this dossier. Historical CI success must not be reused as current-head release evidence. **Release decision: BLOCK.**
