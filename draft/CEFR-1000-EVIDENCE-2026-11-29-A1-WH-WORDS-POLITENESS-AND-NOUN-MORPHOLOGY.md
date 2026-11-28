# A1 wh-words, politeness and noun morphology audit — 2026-11-29

**Scope:** Author-side exact-sense and grammar observations for the user-approved 1,000-word project. Not independent review, not an approved manifest and not a release decision.

## Provenance

- Repository: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io
- Branch: `cefr-5000-bilingual-qa-staging`
- Shortlist blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Review-task blob: `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- Source files: `draft/A1-EDITORIAL-STARTER.json` and `draft/A2-C1-EDITORIAL-STARTER.json`, as recorded per entry.
- Observation date: **2026-11-29 (Asia/Singapore)**.
- Task IDs, source indices, current wording and examples were read from the frozen shortlist and separate review-task inventory. No shortlist or task record was changed.

## 1. High-priority cross-level conflict: person / people

### person — provisional A2, task CEFR1000-A2-0216, source index 191

- **Shortlist:** “One human being considered as an individual.” Myanmar `လူတစ်ဦး`. Example: “Only one person can enter at a time.”
- **Exact-sense source:** Cambridge Learner's Dictionary labels the ordinary countable human-being sense A1 and explicitly gives the irregular plural `people`.
- **Source:** https://dictionary.cambridge.org/us/dictionary/learner-english/person
- **Finding:** The shortlist's A2 placement conflicts with Cambridge's A1 label for the same ordinary individual-human sense. This is a direct level challenge, not merely a word-form issue.
- **Myanmar/example:** The gloss is accurate. The sentence is grammatical and natural. `Only one person can enter at a time.` selects the singular countable sense.
- **Disposition:** High-priority A2→A1 adjudication candidate. Do not move it automatically because the A1 target must remain exactly 200 after any rebalancing.

### people — provisional A1, task CEFR1000-A1-0043, source index 43

- **Shortlist:** “More than one person.” Myanmar `လူတွေ၊ လူများ`. Example: “Many people are here.”
- **Exact-sense source:** Cambridge Learner's Dictionary gives a separate `people` headword and labels the ordinary plural-of-person sense A1. It also distinguishes the collective `the people` and the race/nation sense `peoples`.
- **Sources:** https://dictionary.cambridge.org/us/dictionary/learner-english/people ; https://dictionary.cambridge.org/uk/grammar/british-grammar/person-persons-or-people
- **Morphology note:** `people` is the irregular plural of `person`; it is a legitimate learner-dictionary headword and should be linked to `person` as an inflectional family. It is not a duplicate spelling of the singular, but the curriculum should not conceal the relationship.
- **Myanmar/example:** Current gloss is understandable. `ဒီမှာ လူတွေအများကြီး ရှိတယ်။` is a natural sentence translation. The English example is grammatical.
- **Disposition:** Positive A1 source lead, with explicit irregular-plural linkage to `person`.

### police — provisional A2, task CEFR1000-A2-0266, source index 432

- **Shortlist:** “The public service whose officers enforce the law and protect people.” Myanmar `ရဲတပ်ဖွဲ့`. Example: “The police asked drivers to use another road.”
- **Exact-sense source:** Cambridge Learner's Dictionary labels `police` a plural noun at A2. It defines both the official organization and the people working for it, and gives plural agreement such as “The police were baffled…”.
- **Source:** https://dictionary.cambridge.org/dictionary/learner-english/police
- **Morphology/grammar distinction:** Unlike `people`, which is the irregular plural of `person`, `police` is a plural-only collective noun in this sense. Do not infer a singular `a police`; use `a police officer`. British English normally uses plural agreement: `The police are …`.
- **Example option:** “The police are asking drivers to use another road.” Myanmar: `ရဲတွေက ယာဉ်မောင်းတွေကို တခြားလမ်းကို အသုံးပြုဖို့ ပြောနေကြတယ်။`
- **Disposition:** Positive A2 exact-sense lead. The current past-tense example is grammatical, but it does not visibly teach plural agreement because past-tense `asked` has the same form for singular and plural subjects.

## 2. Politeness function and part-of-speech precision

### please — provisional A1, task CEFR1000-A1-0017, source index 16

- **Shortlist:** POS `politeness marker`; definition “Used to make a request polite.” Myanmar `ကျေးဇူးပြု၍`. Example: “Please open the door.”
- **Exact-sense source:** Cambridge Learner's Dictionary labels `please` an exclamation at A1 for polite requests and polite acceptance. It separately labels the verb meaning “make someone happy” B1.
- **Sources:** https://dictionary.cambridge.org/us/dictionary/learner-english/please ; https://dictionary.cambridge.org/grammar/british-grammar/requests
- **POS risk:** `politeness marker` describes its discourse function, not the conventional dictionary part of speech. Retain the function tag if useful, but store `exclamation / interjection` as the grammatical category so POS data is comparable with dictionaries and other entries.
- **Myanmar note:** `ကျေးဇူးပြု၍` is accurate but formal/written. A natural polite sentence is `ကျေးဇူးပြုပြီး တံခါးဖွင့်ပေးပါ။`
- **Example:** The imperative is grammatical and the initial `please` performs the A1 politeness function. Do not confuse it with the B1 verb `please` meaning satisfy/make happy.
- **Disposition:** Positive A1 exact-sense lead; POS taxonomy refinement needed.

## 3. A1 wh-word exact-sense and POS audit

The shortlist groups these entries under POS `question word`. This is a useful functional family label, but it is not a precise part of speech. Cambridge identifies different categories: `where/when/why/how` are adverbs in the listed question senses; `who` is a pronoun; `what` and `which` can be pronouns or determiners. The data model should keep a `wh-word` function tag separate from the actual POS.

### where — A1, task CEFR1000-A1-0112, source index 112

- **Shortlist:** “Used to ask about a place.” Myanmar `ဘယ်မှာ၊ ဘယ်နေရာမှာ`. Example: “Where is your bag?”
- **Exact-sense source:** Cambridge Learner's Dictionary labels the place/position question adverb A1; its place conjunction is A2.
- **Source:** https://dictionary.cambridge.org/us/dictionary/learner-english/where
- **Example/translation:** Correct and natural. Myanmar option: `သင့်အိတ်က ဘယ်မှာလဲ။`
- **POS proposal:** adverb (interrogative wh-word).

### when — A1, task CEFR1000-A1-0113, source index 113

- **Shortlist:** “Used to ask about a time.” Myanmar `ဘယ်အချိန်မှာ`. Example: “When do you go home?”
- **Exact-sense source:** Cambridge Learner's Dictionary labels the question adverb asking at what time something happened or will happen A1. The time conjunction sense is A2.
- **Source:** https://dictionary.cambridge.org/dictionary/learner-english/when
- **Example/translation:** Grammatically correct; it asks about a habitual time. A more natural Burmese translation is `ဘယ်အချိန် အိမ်ပြန်လေ့ရှိလဲ။`
- **POS proposal:** adverb (interrogative wh-word); do not combine the A2 conjunction sense under the A1 label.

### why — A1, task CEFR1000-A1-0114, source index 114

- **Shortlist:** “Used to ask for a reason.” Myanmar `ဘာကြောင့်၊ ဘာလို့`. Example: “Why are you sad?”
- **Exact-sense source:** Cambridge Learner's Dictionary labels the reason-question adverb A1; `Why don't you…?` / `Why not…?` suggestion patterns are A2, and agreement `why not?` is B1.
- **Source:** https://dictionary.cambridge.org/us/dictionary/learner-english/why
- **Example/translation:** Correct and natural. Myanmar option: `ဘာကြောင့် ဝမ်းနည်းနေတာလဲ။`
- **POS proposal:** adverb (interrogative wh-word). Keep the A2 suggestion pattern and B1 agreement use separate.

### how — A1, task CEFR1000-A1-0115, source index 115

- **Shortlist:** “Used to ask about a way or condition.” Myanmar `ဘယ်လို၊ မည်သို့`. Example: “How are you today?”
- **Exact-sense source:** Cambridge marks `how are you?` A1 for asking whether someone is well; the broader “in what way/by what method” sense is A2.
- **Source:** https://dictionary.cambridge.org/dictionary/english/how?topic=strange-suspicious-and-unnatural
- **Level/sense risk:** The example selects the A1 state/greeting sense, but the current definition foregrounds the broader manner sense. This is a sense-definition mismatch even though the example itself is A1 and natural.
- **Myanmar note:** For the example, `ဒီနေ့ နေကောင်းလား။` is more natural than a literal `ဘယ်လို` translation.
- **Definition proposal:** “Used to ask about someone's condition or the way something is done.” If the entry keeps the A1 example as its core sense, prioritize the condition/greeting meaning and keep manner questions separate.
- **POS proposal:** adverb (interrogative wh-word).

### what — A1, task CEFR1000-A1-0116, source index 116

- **Shortlist:** “Used to ask about a thing or information.” Myanmar `ဘာ၊ ဘယ်အရာ`. Example: “What is your name?”
- **Exact-sense source:** Cambridge Learner's Dictionary labels the information-seeking pronoun/determiner A1; the fused-relative `what` meaning “the thing that” is B1.
- **Source:** https://dictionary.cambridge.org/dictionary/learner-english/what
- **Example/translation:** Correct and natural. Myanmar option: `နာမည် ဘယ်လိုခေါ်လဲ။`
- **POS proposal:** pronoun / determiner (interrogative wh-word), depending on the entry's selected pattern. Keep the B1 fused-relative use separate.

### who — A1, task CEFR1000-A1-0117, source index 117

- **Shortlist:** “Used to ask which person.” Myanmar `ဘယ်သူ`. Example: “Who is your teacher?”
- **Exact-sense source:** Cambridge Learner's Dictionary labels asking a person's name/identity A1. Relative-clause `who` is A2 and the non-defining additional-information use is B1.
- **Source:** https://dictionary.cambridge.org/us/dictionary/learner-english/who
- **Example/translation:** Correct and natural. Myanmar option: `သင့်ဆရာ/ဆရာမက ဘယ်သူလဲ။`
- **POS proposal:** pronoun (interrogative wh-word). Keep relative-pronoun patterns separate.

### which — A1, task CEFR1000-A1-0118, source index 118

- **Shortlist:** “Used to ask someone to choose from a group.” Myanmar `ဘယ်ဟာ၊ ဘယ်တစ်ခု`. Example: “Which book do you want?”
- **Exact-sense source:** Cambridge English Dictionary labels the question determiner/pronoun A1 for choosing from a fixed or limited set of answers or possibilities.
- **Source:** https://dictionary.cambridge.org/dictionary/english/which?topic=question-words-and-expressions
- **Example/translation:** Correct and natural when the available books form a limited set. Myanmar option: `ဘယ်စာအုပ်ကို လိုချင်လဲ။`
- **POS proposal:** determiner in `which book`; pronoun when used without a noun (for example, `Which is mine?`).

## Consolidated editorial risks

1. **Cross-level:** `person` is A2 in the shortlist but Cambridge labels the same ordinary countable human-being sense A1. `people` is A1 and is the irregular plural of `person`; these entries should be linked and the level conflict adjudicated before release.
2. **POS taxonomy:** `question word` and `politeness marker` are functional labels, not precise dictionary POS categories. Store function tags separately from POS.
3. **Morphology:** distinguish irregular plural `people` from plural-only collective `police`; do not treat both as the same kind of plural morphology.
4. **Sense boundary:** `how` example `How are you today?` selects the A1 state/greeting sense, whereas “way/method” is A2 in Cambridge. Keep these readings separate.
5. **Within-word level boundaries:** `where` question adverb A1 vs conjunction A2; `when` question adverb A1 vs conjunction A2; `why` reason question A1 vs suggestions A2 and agreement B1; `who` interrogative A1 vs relative-clause A2/B1; `what` information question A1 vs fused-relative B1; `please` request exclamation A1 vs verb “make happy” B1.

## Integrity boundary

All eleven entries remain on editorial hold. Their English, Myanmar, example and CEFR independent-review fields remain pending. No reviewer was assigned, no task was signed, no approval flag was changed, and no level was moved. This is source-supported author research only.
