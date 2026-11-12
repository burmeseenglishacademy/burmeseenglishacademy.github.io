# CEFR-1000 A1 lexical-form and example alignment audit — 2026-11-12

**Scope:** Approved 1,000-total project only; provisional manifest `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`). Read-only inspection of entries; no manifest edits or approvals. **Observation date:** 2026-11-12. Research and proposed changes are assistant-authored editorial triage, NOT independent human verification.

## 1. A1 `thank` (verb): explicit level conflict
Manifest: verb, “To tell someone that you are grateful”; example “I thank my teacher.”; Myanmar `ကျေးဇူးတင်သည်`.
Cambridge Advanced Learner's Dictionary labels the **transitive verb** `thank` **A2**, not A1: https://dictionary.cambridge.org/dictionary/english/thank (observed 2026-11-12). Oxford confirms the verb's `thank somebody (for something)` valency: https://www.oxfordlearnersdictionaries.com/definition/english/thank (observed 2026-11-12). Collins distinguishes the **A1 conversational formula** “thank you” from the **A2 verb**: https://www.collinsdictionary.com/de/worterbuch/englisch/thank (observed 2026-11-12).
**Disposition:** block A1 verb signoff; do not treat the A1 *thank you* formula as CEFR evidence for the standalone verb. Independently adjudicate replacement or reallocation without changing the 200-per-level target. Candidate more natural original verb example (not approved): “I thanked my teacher for helping me.” Myanmar for the full example: `ကူညီပေးခဲ့တဲ့အတွက် ဆရာမကို ကျေးဇူးတင်ခဲ့တယ်။` Gender of teacher is unspecified in English; a reviewer should choose context-neutral `ဆရာ/ဆရာမ` or rewrite the example.

## 2. A1 `home` (noun): part-of-speech mismatch in example
Manifest: noun “The place where someone lives”; example “I go home after school.”; Myanmar `အိမ်၊ နေအိမ်`.
Cambridge Learner's Dictionary labels the residence **noun** A1 but `home` meaning *to the place where one lives* as an **adverb** A2: https://dictionary.cambridge.org/dictionary/learner-english/home (observed 2026-11-12). Cambridge usage article explains `go home` without *to*: https://dictionaryblog.cambridge.org/2020/07/22/staying-at-home-going-home-or-working-from-home-using-the-word-home/ (observed 2026-11-12).
**Disposition:** keep noun as a candidate, but replace the example with one that actually illustrates noun usage. Original proposal: “Our home has a small garden.” Myanmar proposal: `ကျွန်တော်တို့အိမ်မှာ ဥယျာဉ်လေးတစ်ခု ရှိတယ်။` Do not infer approval or audio readiness.

## 3. A1 `it` (pronoun): ungrounded referent in isolated example
Manifest: “A thing or animal already mentioned”; example “It is a small cat.”; Myanmar `အဲဒါ၊ ၎င်း`.
Cambridge marks the anaphoric thing/animal pronoun A1: https://dictionary.cambridge.org/us/dictionary/english/it (observed 2026-11-12). Its grammar page distinguishes anaphoric from dummy `it`: https://dictionary.cambridge.org/grammar/british-grammar/it%7C (observed 2026-11-12). In isolation, the manifest example does not provide the *already mentioned* referent and may instead be read as presentational reference.
**Disposition:** preserve the A1 sense candidate but use an antecedent in the example. Original proposal: “I have a cat. It is very small.” Myanmar proposal: `ကျွန်တော့်မှာ ကြောင်တစ်ကောင်ရှိတယ်။ အဲဒီကြောင်လေးက အရမ်းသေးတယ်။` Independent reviewer must check whether a two-sentence example fits the UI/audio design.

## Release-gate implications
- Treat lexical-form/sense and part-of-speech alignment as distinct evidence fields; dictionary level for a multiword conversational formula does **not** transfer to a verb lemma.
- Require reviewer to validate that each example illustrates the **same** CEFR-evidenced sense and POS as its entry, including multi-sentence antecedents.
- Record reviewer identity, dated evidence, English/Myanmar/example/level approvals, and independent listening separately. Assistant-authored suggestions never set review flags.
- Maintain A1/A2/B1/B2/C1 targets at **200/200/200/200/200 first-pass**, independently approved **0/0/0/0/0**, all editorial holds. No new audio/listening, browser/mobile, physical iPhone Safari, GitHub Pages clearance or production deployment evidence is asserted.
- Protect 54 lessons, separate IELTS bank, established George/Emma audio, privacy assets and `main`. **Staging only.**
