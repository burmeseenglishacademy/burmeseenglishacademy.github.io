# CEFR-1000 A1 `I` — publisher-backed exact-sense research handoff

Observed: **2026-11-08** (Singapore). **EDITORIAL RESEARCH ONLY — NOT INDEPENDENTLY REVIEWED; DO NOT PUBLISH.**

## Inventory provenance
- Branch: `cefr-5000-bilingual-qa-staging`.
- Inventory: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Stored headword: lowercase `i`, level A1, pronoun, original source `draft/A1-EDITORIAL-STARTER.json`, index **3**, source blob SHA `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- Current definition: “The person who is speaking or writing.” Current Myanmar: “ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)”. Current example: “I am a student.”
- All review flags false, editorial hold true. **Critical presentation issue:** the stored `word` is lowercase `i`; the first-person singular subject pronoun is conventionally capitalised **I** even mid-sentence. Preserve original provenance; require editorial decision on canonical display, search normalization, and headword audio before release.

## Publisher observations and exact-sense evidence
1. Cambridge English Dictionary, https://dictionary.cambridge.org/dictionary/english/i (observed **2026-11-08**): the **pronoun** sense of `I` is explicitly marked **A1**, referring to the speaker/writer **as grammatical subject**. The same entry separately includes `I/i` as a **letter** and a **Roman numeral**; neither should be silently conflated with this A1 pronoun.
2. Cambridge Essential British English, https://dictionary.cambridge.org/dictionary/essential-british-english/i (observed **2026-11-08**): explicitly marks the subject pronoun **A1** and gives British /aɪ/.
3. Cambridge Grammar, https://dictionary.cambridge.org/uk/grammar/british-grammar/pronouns-personal-i-me-you-he-it-etc (observed **2026-11-08**): distinguishes subject `I` from object `me`; the object form cannot replace `I` in ordinary standard subject position.

These publisher pages support **the specified subject-pronoun sense only**, not blanket CEFR approval for all meanings of the written form.

## Editorial proposal — requires independent human signoff
- Canonical displayed headword: **I** (capital letter); normalized matching may remain case-insensitive if it does not merge unrelated letter/numeral senses.
- Part of speech: **subject pronoun**.
- Original concise English definition: “The word a speaker or writer uses to refer to themselves as the subject of a sentence.”
- Proposed natural Myanmar explanation: “ကိုယ့်အကြောင်း ပြောတဲ့အခါ၊ စာရေးတဲ့အခါ ဝါကျရဲ့ ကတ္တားနေရာမှာ သုံးတဲ့ နာမ်စားပါ။ ပြောသူအလိုက် ‘ကျွန်တော်’၊ ‘ကျွန်မ’ စသဖြင့် အဓိပ္ပာယ်ရပါတယ်။”
- Original example A: “I work at a small shop.” — “ကျွန်တော် ဆိုင်လေးတစ်ဆိုင်မှာ အလုပ်လုပ်ပါတယ်။”
- Original example B: “My sister and I cook dinner together.” — “ကျွန်မနဲ့ အစ်မက ညစာကို အတူတူ ချက်ကြပါတယ်။”
- Pronunciation: British /aɪ/; check George and Emma headword and both example recordings **by actual listening**. Do not assert audio exists.
- Grammar QC: **I am**, not *I is*; **She and I are** in subject position; **She called me**, not *She called I*. In sentence-initial and medial positions the pronoun remains uppercase.
- Myanmar QC: pronoun choice varies with speaker and register; avoid implying a single fixed gendered equivalent. Have a fluent independent reviewer verify both examples and tone.

## Release implications
- The lowercase headword may be a deliberate normalization convention; do **not** mutate the provisional JSON without reviewing lookup/audio and duplicate-key behavior. Independently check exact sense, CEFR source, British pronunciation, English, Myanmar, original examples and display capitalization.
- No independent review is recorded. This handoff is not an approval or release gate pass.
