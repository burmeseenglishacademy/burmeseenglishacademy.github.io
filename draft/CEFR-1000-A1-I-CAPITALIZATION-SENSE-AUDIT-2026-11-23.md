# CEFR-1000 A1 pronoun I: canonical capitalization, exact sense and Myanmar register audit

Observed: 2026-11-23 UTC. **Author-side evidence gathering only; not independent review or approval.** Applies solely to the approved 1,000-total provisional CEFR shortlist.

## Pinned provenance
- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Review tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, previously observed blob `77abf35146825f05e3e58cfdd7a73b3c7302c967` (recheck before adjudication).
- Source: `draft/A1-EDITORIAL-STARTER.json`, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`, source_index 3.
- Task `CEFR1000-A1-0004`, global ordinal 4; provisional word `i`, POS pronoun, definition “The person who is speaking or writing.”; Myanmar `ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)`; example “I am a student.”

## Observed external evidence (2026-11-23)
1. Cambridge Learner's Dictionary, **I** (pronoun), **A1**, explicitly defines the speaker/writer **as the subject of the verb**: https://dictionary.cambridge.org/dictionary/learner-english/i
2. Cambridge Essential British English, **I** (pronoun), **A1**, same subject-pronoun sense: https://dictionary.cambridge.org/us/dictionary/essential-british-english/i
3. British Council LearnEnglish, capitalization: the pronoun **I** requires a capital letter: https://learnenglish.britishcouncil.org/comment/215620
4. British Council LearnEnglish, personal pronouns: distinguishes subject **I** from object **me**: https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/personal-pronouns

## Specific editorial defects / risks
- **Canonical headword defect:** stored `i` is lowercase, but the pronoun's standard orthography is `I` even inside a sentence. This is not merely a display-style preference. A case-folding uniqueness algorithm may treat `i` and `I` as the same identity; display/audio/manifest code must retain canonical case without creating a second slot.
- **Exact-sense gap:** provisional definition says “the person who is speaking or writing,” but omits **subject of the verb**, inviting confusion with `me` and `my`.
- **Myanmar nuance:** `ကျွန်တော်` and `ကျွန်မ` are common polite self-references; Myanmar self-reference also depends on speaker, context and register. Do not claim a fixed one-to-one gender mapping or imply these are the only acceptable forms.
- **Example:** “I am a student.” is grammatical and demonstrates subject use; it does not demonstrate that the pronoun remains capitalized in mid-sentence.

## Author-only revision candidates — NOT independently approved
- Canonical headword: `I` (pronoun).
- English: “The word a speaker or writer uses for themselves as the subject of a verb.”
- Myanmar: `ပြောသူ သို့မဟုတ် ရေးသူက မိမိကိုယ်ကို ဝါကျ၏ ကတ္တားအဖြစ် ရည်ညွှန်းရာတွင် သုံးသော နာမ်စား။ အခြေအနေနှင့် ပြောဆိုပုံအလိုက် ‘ကျွန်တော်’၊ ‘ကျွန်မ’ စသည်ဖြင့် ပြန်ဆိုနိုင်သည်။`
- Original example: “My sister and I study English together.” (subject in coordinated noun phrase; `I` capitalized mid-sentence).
- Original contrast example for reviewer discussion only: “My sister called me.” (`me` object; not a second vocabulary entry).

## Independent adjudication and safeguards
A separate qualified reviewer must verify exact Cambridge A1 sense, English definition, natural Myanmar wording and social register, original example grammar, headword capitalization, and pronunciation. Record reviewer identity, date, exact source URLs and independently checked observations without inferring approval from this audit. If the headword is changed to `I`, keep the **same slot and provenance** and require case-insensitive cross-level identity uniqueness, exact 200 per level, stable review-task joins and explicit display-case checks; do not silently rewrite the pinned shortlist. The published headword and British George/Emma headword audio text must use canonical `I`, with actual generated files and real human listening signoff still required.

## Release status
A1/A2/B1/B2/C1 each have 200 provisional first-pass entries; independent approvals are **0/0/0/0/0**. This document does not change shortlist or reviewer flags and provides no audio, listening, physical iPhone Safari, CI run, hosting or deployment evidence. Production lessons, IELTS bank, existing George/Emma assets and main remain protected. **Release blocked.**
