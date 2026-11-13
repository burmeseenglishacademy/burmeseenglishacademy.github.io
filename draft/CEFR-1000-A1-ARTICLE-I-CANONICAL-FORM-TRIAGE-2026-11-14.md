# CEFR-1000 A1 source-grounded editorial triage — 2026-11-14

**Scope:** Staging-only research; not an independent review, approval, release manifest, or audio listening record. All 1,000 entries remain on editorial hold.

## Provenance
- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; Git blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; retrieved from `cefr-5000-bilingual-qa-staging` on 2026-11-14.
- Entry positions below are **zero-based** `entries[]` indices, not review task IDs.
- Original upstream provenance for these entries: `draft/A1-EDITORIAL-STARTER.json`, source blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`, source indices 0, 1, and 3.
- Public reference pages observed 2026-11-14: British Council https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/indefinite-article ; Cambridge Learner's Dictionary https://dictionary.cambridge.org/dictionary/learner-english/i . These references support grammatical or learner-level observations, not independent signoff of the shortlist.

## A1 index 0 — `a` (article)
- Existing English: “Used before one person or thing when it is not specified.”
- Existing Myanmar: “တစ်ခု၊ တစ်ယောက် (မသတ်မှတ်ရသေးသော)”
- Existing example: “I have a book.”
- **Exact-sense issue:** British Council explains `a/an` as a single indefinite-article grammar topic, used with singular nouns, and selects `a` by *consonant sound* (not initial written letter). The current entry is broadly correct but omits this pronunciation-conditioned form selection. The two-form split raises a deduplication policy question: do `a` and `an` occupy two distinct vocabulary senses, or one grammar concept with two spellings?
- Proposed unapproved teaching note: “Use `a` before a singular countable noun phrase beginning with a consonant sound, when the referent is not specifically identified.” Myanmar draft: “တိတိကျကျ မသတ်မှတ်ထားသော တစ်ဦး/တစ်ခုကို ပြောရာတွင် ဗျည်းသံဖြင့် စသော နာမ်စကားစုရှေ့၌ သုံးသော အကန့်အသတ်မရှိသော article ဖြစ်သည်။”
- New original test example (not a replacement yet): “My sister studies at a university.” Check `university` begins with /j/ and therefore takes `a`.

## A1 index 1 — `an` (article)
- Existing English: “Used before one person or thing when the next word starts with a vowel sound.”
- Existing Myanmar: “တစ်ခု၊ တစ်ယောက် (သရသံဖြင့်စသော စကားလုံးရှေ့တွင်)”
- Existing example: “She has an apple.”
- **Exact-sense issue:** British Council confirms selection by *vowel sound*, including silent-h `hour`; `an` is a form of the same indefinite article as `a`, not a separate semantic meaning. The current English omits the singular countable noun constraint and non-specific reference.
- Proposed unapproved teaching note: “Use `an` before a singular countable noun phrase beginning with a vowel sound when its referent is not specifically identified.” Myanmar draft: “တိတိကျကျ မသတ်မှတ်ထားသော တစ်ဦး/တစ်ခုကို ပြောရာတွင် သရသံဖြင့် စသော နာမ်စကားစုရှေ့၌ သုံးသော အကန့်အသတ်မရှိသော article ဖြစ်သည်။”
- New original test example: “We waited for an hour.” The `h` is silent; no spelling-based shortcut should be taught.

## A1 index 3 — `i` (pronoun)
- Existing shortlist spelling: lowercase `i`; original English “The person who is speaking or writing.”; Myanmar “ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)”; example “I am a student.”
- **Canonical-form and exact-sense risk:** Cambridge Learner's Dictionary presents **`I`**, explicitly **A1**, as the first-person *subject* pronoun. Lowercase `i` is not the normal English orthographic headword. The current definition omits subject function, potentially confusing it with object `me`. The example already uses the correct capital.
- Proposed unapproved headword: `I` (capital). Proposed English: “The pronoun a speaker or writer uses as the subject when referring to themselves.” Myanmar draft: “မိမိကိုယ်ကို ဝါကျ၏ ကတ္တားအဖြစ် ရည်ညွှန်းရာတွင် သုံးသော နာမ်စား (အင်္ဂလိပ်စာတွင် `I` ဟု စာလုံးအကြီးဖြင့် ရေးသည်)။”
- New original test example: “I work in a small shop.”
- **Normalization safeguard:** If the pipeline lowercases for case-insensitive deduplication, preserve canonical display spelling `I`; require a separate collision check against other normalized entries and audio filename keys. Do not silently change the provisional shortlist or its provenance.

## Independent adjudication required
1. Decide whether `a`/`an` count as one lexical sense and, if so, source and independently review a genuine replacement to keep exactly 200 A1 slots.
2. Confirm grammar scope, idiomatic Myanmar phrasing, original example accuracy, and CEFR **exact sense** (the British Council page says beginner; it is not an independent per-headword A1 CEFR rating).
3. Approve or reject the uppercase `I` canonical display change, and verify downstream search, deduplication, UI, and George/Emma audio mappings.
4. Obtain named independent English, Myanmar, example, CEFR/source and pronunciation reviewers with recorded evidence; none is claimed here.

**Gate status:** A1–C1 each 200 first-pass entries; independently approved 0 per level. George/Emma shortlist audio generation and actual listening signoff, mobile/browser and physical iPhone Safari QA, hosting verification and deployment remain unverified or outstanding. **Do not publish.**
