# CEFR 1000 — pronoun orthography and audio-text identity gate (2026-11-05)

**Scope:** staging-only editorial QA; no independent approval, no audio generated/listened, no deployment. Frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; 1,000 entries, exactly 200 each A1–C1, zero independent approvals. Read directly from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` on 2026-11-05.

## Confirmed concrete defect

A1 entry at zero-based shortlist index **3** has `word: "i"`, POS pronoun, definition "The person who is speaking or writing.", Myanmar meaning `ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)`, and example `I am a student.`. Source provenance: `draft/A1-EDITORIAL-STARTER.json`, zero-based `source_index: 3`. The English first-person singular subject pronoun must be written **I** (capital letter) even in isolation. This is an orthographic defect in the headword, **not** evidence that the CEFR level or translation has been independently verified. Do not silently change the frozen manifest until editorial policy for case-sensitive headwords, stable audio identifiers, and source-backed exact-sense review is decided.

**Proposed editorial correction:** display headword `I`; example remains `I am a student.`; Myanmar candidate remains `ကျွန်တော် / ကျွန်မ` (speaker-dependent). Human reviewer should confirm register and naturalness. Distinguish the valid A1 article `a` at index 0, which must stay lowercase except at sentence start. A global uppercase-first-letter rule would be wrong.

## Fail-closed release checks to implement before launch

1. Case-sensitive English orthography review: reject lowercase standalone pronoun `i` specifically, while allowing lowercase article `a`. Do not indiscriminately title-case words.
2. Separate canonical headword text, optional display casing and immutable asset identifier. Require headword-audio text and example-audio text to match the *approved* manifest revision exactly, with hash/provenance.
3. For each approved entry require both George and Emma British voice **headword and example** assets, real human listening signoff with reviewer/date/file hash, and no missing/empty/placeholder files. Expected minimum: 1,000 × 2 voices × 2 utterances = **4,000** audio assets (unless a documented manifest specifies a different approved packaging model).
4. Require independent English, Myanmar, example, exact-sense CEFR source and pronunciation reviewer attestations; source URL, observation date, sense-specific quote/identifier and reviewer identity. Never infer signoff from automation's own text checks.
5. Verify 200 unique approved headword/sense pairs per level and cross-level sense conflicts; reject ambiguous morphology and named-entity risks pending reviewer decisions.
6. Require real mobile-browser regression, **physical iPhone Safari** reviewer evidence, GitHub Pages hosting validation and confirmed deployment plus production asset preservation before flipping release readiness.

## Inventory audit

Programmatically checked all 1,000 provisional records on 2026-11-05: exactly 200 per level; no duplicate case-folded `word|part_of_speech` pairs; only one standalone single-character alphabetic headword besides the valid article `a` is the lowercase `i`. These are structural observations only. Source-backed CEFR evidence for this pronoun was **not** collected in this pass; independent reviewers must supply it.

**Status:** release blocked; no approval flags, frozen shortlist, main branch, production audio, IELTS bank or 54 lessons changed.
