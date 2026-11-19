# CEFR-1000 A1 “I” — canonical headword and exact-sense evidence (2026-11-19)

**Scope:** editorial evidence only; not an independent review, approval, or publication authorisation. Branch: `cefr-5000-bilingual-qa-staging`. Approved project scope: exactly 200 entries each for A1, A2, B1, B2 and C1 (1,000 total).

## Frozen provisional record and provenance
- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; observed blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- A1 source index **3**: `draft/A1-EDITORIAL-STARTER.json`, source blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- Stored headword **`i`** (lowercase); part of speech pronoun; English definition “The person who is speaking or writing.”; Myanmar “ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)”; example “I am a student.”
- Provisional status remains editorial hold; no independently reviewed or approved flags changed. Corresponding global review-task ID is expected to be `CEFR1000-A1-0004` (confirm against task record before editorial action).

## Observed independent published references (accessed 2026-11-19)
1. Cambridge **Essential British English Dictionary**, [I](https://dictionary.cambridge.org/dictionary/essential-british-english/i): **A1**, pronoun, first-person speaker/writer in the **subject** role; British /aɪ/. The exact intended subject-pronoun sense is directly supported.
2. Cambridge **Learner's Dictionary**, [I](https://dictionary.cambridge.org/dictionary/learner-english/i): **A1**, subject pronoun. Corroborates the specific lexical sense, not every use of lowercase letter `i`.
3. British Council LearnEnglish, [Capital letters and apostrophes](https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/capital-letters-apostrophes): specifically requires a capital **I** for the pronoun. This is a capitalisation rule, **not** a lexical CEFR rating.

## Editorial issue and proposed candidate (NOT accepted)
The lowercase `i` is a noncanonical display headword for the English first-person subject pronoun. Its existing example correctly uses uppercase `I`, so the headword/example mismatch is actionable. Distinguish the pronoun from the letter name, symbols, and product-name prefixes. A generic case-folding deduplicator may regard `i` and `I` as identical, but display should preserve the canonical uppercase form.

- **Proposed headword:** `I` (pronoun, A1).
- **Proposed English definition:** “The word a speaker or writer uses to refer to themselves as the subject of a sentence.”
- **Proposed Myanmar meaning:** “စကားပြောသူ သို့မဟုတ် စာရေးသူက မိမိကိုယ်ကို ရည်ညွှန်းရာတွင် ဝါကျ၏ ကတ္တားအဖြစ် သုံးသော နာမ်စား (ကျွန်တော်၊ ကျွန်မ)။”
- **New original example:** “My sister likes tea, but I prefer water.”
- **Proposed Myanmar example:** “ကျွန်တော့်ညီမက လက်ဖက်ရည်ကြိုက်ပေမယ့် ကျွန်တော်ကတော့ ရေကို ပိုကြိုက်တယ်။”
- **Example nuance:** Myanmar first-person rendering varies with speaker identity/register; reviewer should check inclusivity and naturalness, and may choose a different natural translation.

## Required independent review and release consequences
A qualified reviewer must confirm the exact A1 subject-pronoun sense, Myanmar translation, grammatical English example and Myanmar example independently, and record source evidence with identity/date. If the headword is corrected, check case-insensitive deduplication against every level, immutable review-task linkage, downstream audio file keys and generated manifests. Do **not** count this research as independent signoff or mutate the frozen provisional shortlist. Do not generate/claim completed George/Emma listening or iPhone Safari QA from text research.

**Staging truth:** A1/A2/B1/B2/C1 each have 200 first-pass provisional records and **0 independently approved**. Final bilingual review, all final-voice audio with real listening, browser/mobile and physical iPhone testing, hosting clearance and confirmed production deployment are still blocked. Production and the separate IELTS bank are out of scope.
