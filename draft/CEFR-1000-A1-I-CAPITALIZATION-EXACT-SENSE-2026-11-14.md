# CEFR-1000 A1 “i” / “I”: canonical orthography and exact-sense evidence (2026-11-14)

**Scope:** Editorial observation only, not independent verification, not a shortlist edit or release approval. Staging branch `cefr-5000-bilingual-qa-staging`.

## Provenance and observed provisional record

- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; global zero-based index **3**; level A1; source `draft/A1-EDITORIAL-STARTER.json`, source index **3**, source blob SHA `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- Stored headword **`i`** (lowercase); part of speech `pronoun`; stored English definition: “The person who is speaking or writing.” Stored Myanmar: “ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)”. Stored example: “I am a student.”
- All independent-review booleans remain false; editorial hold remains true. The example is grammatical but the stored headword is **not standard English orthography**. English first-person singular subject pronoun is conventionally always uppercase **`I`**, even mid-sentence. A case-insensitive deduplication audit alone will not catch this.
- Do **not** silently correct the source shortlist or turn this into approval; ask the independent reviewer to adjudicate canonical display spelling and whether casefolded identity should remain `i` for uniqueness.

## Source observations (observed 2026-11-14)

1. [Cambridge Learner’s Dictionary — I](https://dictionary.cambridge.org/us/dictionary/learner-english/i) explicitly labels the **first-person singular subject pronoun** **A1**, and distinguishes the speaker/writer as subject of a verb. This is **exact-sense A1 support** for the candidate; it does not validate the Myanmar translation or provide independent editorial signoff.
2. [Cambridge Grammar — personal pronouns](https://dictionary.cambridge.org/uk/grammar/british-grammar/pronouns-personal-i-me-you-him-it-they-) explicitly distinguishes **I (subject)** from **me (object)**, and illustrates that the speaker/writer uses both in different syntactic positions. Grammar support is not a separate CEFR level rating.
3. [Cambridge English Dictionary — he](https://dictionary.cambridge.org/us/dictionary/english/he?topic=personal-pronouns) demonstrates why a pronoun's ordinary subject sense and archaic/generic uses must be treated separately; **do not transfer** its A1 tag to `I` or to other pronouns.

## Proposed unapproved editorial candidate

- Canonical headword: **I** (capital letter); grammatical label: **personal pronoun, first-person singular, subject form**.
- English definition: “The word a speaker or writer uses for themselves as the subject of a verb.”
- Myanmar candidate: **ကျွန်တော် / ကျွန်မ (ပြောသူ သို့မဟုတ် ရေးသူက မိမိကိုယ်ကို ဝါကျ၏ ကတ္တားအဖြစ် ရည်ညွှန်းရာတွင် သုံးသော နာမ်စား)**. Reviewer should check register, gendered alternatives, learner naturalness, and whether the metalanguage “ကတ္တား” needs a beginner-friendly explanation.
- Original example: **“I work in a small shop.”** Grammar: first-person subject `I` + present-simple verb `work`. Candidate Myanmar example translation: **“ကျွန်တော် ဆိုင်လေးတစ်ဆိုင်မှာ အလုပ်လုပ်ပါတယ်။”** Independent bilingual reviewer should verify that the gender/register choice is appropriate and decide whether parallel forms are needed.
- Distinguish from object pronoun **me** and from possessive determiner **my**; do not infer those headwords' CEFR labels from the evidence above.

## Required independent adjudication and safeguards

- Reviewer must inspect live dictionary sense and record source URL, access date, exact sense, and CEFR observation; independently evaluate English, Myanmar, original example and pronunciation.
- Introduce a **canonical-capitalization exception check** for the exact headword `I` in eventual approved manifest; a lowercased `i` must be rejected even if the example contains uppercase `I`. Do not force title case for ordinary headwords.
- Preserve casefolded duplicate checks so `I` and `i` cannot occupy two slots; maintain exactly 200 independently approved nonduplicated senses per level and 1,000 total.
- No George/Emma audio, listening signoff, mobile/iPhone test, hosting validation, or production release is implied by this observation.

## Release posture

A1/A2/B1/B2/C1: **200 provisional first-pass written entries each; 0 independently checked/approved each**. The provisional `i` record remains on hold. Previously inspected GitHub Actions run [43520974102](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/43520974102) has five successful level-specific negative-gate jobs, but it tested an earlier commit and **does not certify this documentation commit**. No approved manifest, final audio/listening evidence, physical iPhone Safari signoff, hosting clearance, or confirmed deployment. **DO NOT PUBLISH**.
