# CEFR-1000 A1 articles and first-person pronoun: source and orthography audit

Observed: 2026-11-21 (UTC date). Author-side research only; NOT independent editorial approval.

## Pinned provisional data
- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- All records remain on hold; no review flags or release data were changed.

## A1-0004 — provisional `i` (pronoun)
- Current provisional definition: “The person who is speaking or writing.” Myanmar: “ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)”. Example: “I am a student.”
- Cambridge Learner's Dictionary lists **I**, pronoun, **A1**, specifically the speaker/writer **as subject of the verb**: https://dictionary.cambridge.org/dictionary/learner-english/i (observed 2026-11-21).
- Orthography defect: stored headword `i` is lowercase, whereas the standard English first-person singular pronoun is written `I` even mid-sentence. Supporting usage explanation: https://languagetool.org/insights/post/grammar-uppercase-i/ (observed 2026-11-21).
- Recommendation for independent reviewer: correct the display lemma to `I`, retain source provenance and the A1 sense; tighten English definition to mention **subject** (avoid conflating object `me`). Burmese gloss is understandable, but the subject-role explanation should be independently assessed in natural Burmese. Example is grammatical and demonstrates subject use.
- Release implication: case-folded uniqueness checks alone must not silently normalize the user-facing spelling; proposed fix requires reviewer adjudication and coordinated task/manifest handling.

## A1-0001 — provisional `a` (article)
- Current definition: “Used before one person or thing when it is not specified.” Myanmar: “တစ်ခု၊ တစ်ယောက် (မသတ်မှတ်ရသေးသော)”. Example: “I have a book.”
- Cambridge British Grammar describes `a/an` as **indefinite articles** and explains `a` before a **consonant sound**, not simply any singular referent. It also limits `a/an` to singular countable nouns in ordinary usage: https://dictionary.cambridge.org/grammar/british-grammar/a-an (observed 2026-11-21).
- Recommendation: make the English and Burmese explanations explicitly cover indefinite singular countable nouns and the consonant-sound condition; avoid suggesting the article is used before every unspecified person/thing. Example is grammatical. This grammar page does **not** independently certify the entry's A1 CEFR level.

## A1-0002 — provisional `an` (article)
- Current definition: “Used before one person or thing when the next word starts with a vowel sound.” Myanmar: “တစ်ခု၊ တစ်ယောက် (သရသံဖြင့်စသော စကားလုံးရှေ့တွင်)”. Example: “She has an apple.”
- Cambridge British Grammar confirms vowel **sound** (not initial vowel letter), including `an hour`, and specifies singular countable nouns: https://dictionary.cambridge.org/grammar/british-grammar/a-an (observed 2026-11-21).
- Recommendation: preserve the sound-based distinction, clarify the countability constraint, and independently assess whether the Myanmar wording communicates sound rather than written letter. Example is grammatical. This grammar page does **not** independently certify the entry's A1 CEFR level.

## Independent-review handoff and unresolved gates
Tasks `CEFR1000-A1-0001`, `CEFR1000-A1-0002`, `CEFR1000-A1-0004` require a separate qualified reviewer to check exact sense, CEFR evidence, fluent Myanmar, examples, and pronunciation. Source URLs and observation date above are research provenance only. **0 independently approved.** No final shortlist, task statuses, audio, protected production files, main branch, or release flags changed.
