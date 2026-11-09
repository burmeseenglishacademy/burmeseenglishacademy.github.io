# CEFR-1000 A1 `i` → `I`: publisher-supported exact-sense editorial dossier

**Observed:** 2026-11-09 (UTC+08:00). **Status:** editorial proposal only; independent review NOT performed. **Scope:** the user-approved 1,000-total CEFR shortlist, not the superseded 5,000 plan.

## Exact inventory provenance

- Inventory: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- A1 entry `word: "i"`, `part_of_speech: "pronoun"`; source `draft/A1-EDITORIAL-STARTER.json`, `source_index: 3`, source blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- Existing first-pass definition: “The person who is speaking or writing.” Existing Myanmar: “ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)”. Existing example: “I am a student.”
- All independent review flags are false; editorial hold true; publisher source fields empty. **Do not alter approval flags on the basis of this dossier.**

## Publisher observations (2026-11-09)

1. Cambridge Learner's Dictionary, https://dictionary.cambridge.org/dictionary/learner-english/i : **I**, pronoun, British pronunciation /aɪ/, explicitly **A1**; the listed sense is the speaking/writing person as **subject of the verb**. The A1 tag belongs to this pronoun sense, not the alphabet letter or Roman numeral.
2. Cambridge English Dictionary, https://dictionary.cambridge.org/us/dictionary/english/i : differentiates **I** (A1 subject pronoun) from **I/i** as the alphabet letter and Roman numeral. Thus matching a lowercased string without POS and sense risks a false dictionary match.
3. British Council LearnEnglish, https://learnenglish.britishcouncil.org/grammar/english-grammar-reference/personal-pronouns : subject **I** contrasts with object **me**. Its beginner grammar framing corroborates usage but is not by itself an exact-sense CEFR rating.
4. British Council IELTS capitalization guidance, https://takeielts.britishcouncil.org/blog/capital-letters-in-english-common-errors-and-how-to-fix-them : first-person pronoun **I** is always capitalized, including inside a sentence.

## Proposed editorial correction, pending independent signoff

- **Canonical headword:** `I` (uppercase), **POS:** pronoun, **level:** A1, **sense:** first-person singular **subject** pronoun.
- **English definition (original):** “The word a speaker or writer uses for themselves as the subject of a verb.”
- **Myanmar meaning (original draft):** “ကျွန်တော်၊ ကျွန်မ၊ ငါ — ပြောသူ သို့မဟုတ် ရေးသူက မိမိကိုယ်ကို ဝါကျ၏ ကတ္တားအဖြစ် ရည်ညွှန်းရာတွင် သုံးသော နာမ်စား။”
- **Original example:** “I read a book every evening.”
- **Myanmar example translation (original draft):** “ညနေတိုင်း ကျွန်တော် စာအုပ်တစ်အုပ် ဖတ်တယ်။” (Speaker-gender/register choice is contextual; independent native-speaker review must check naturalness and alternatives.)
- **Contrast:** “She called me.” Object `me` must not be folded into the A1 `I` subject sense.
- **Audio:** UK /aɪ/ reference is **not** generated George/Emma audio and is **not** listening signoff.

## Release-impact and review instructions

The existing inventory uses lowercase `i` even though its example already uses uppercase `I`. This is a genuine spelling/canonicalization issue, not grounds to delete the lexical item. Preserve the 200 A1 provisional count until an independent reviewer authorizes a versioned correction. Cross-level deduplication should retain case-folded comparison but display canonical capitalization; avoid conflating the pronoun with the letter `i`, a Roman numeral, or unrelated symbols. The release manifest must retain a sense identifier and publisher-specific sense URL.

**Required independent tasks:** separately verify Cambridge's A1 pronoun sense, English definition, natural Myanmar meaning/register, original example grammar and translation, and UK pronunciation; record named human reviewer, review date, decision, exact source URLs, and the approved inventory change. Until then: 200 first-pass A1, 0 independently checked A1, 0 released.

**Other release gates remain unverified:** all 1,000 independent reviews; a/an lexical-unit adjudication; complete George/Emma word+example audio and real listening signoff; browser/mobile and physical iPhone Safari evidence; hosting limits; production deployment and preserved 54 lessons, separate IELTS bank, established audio and privacy. Remain staging only.
