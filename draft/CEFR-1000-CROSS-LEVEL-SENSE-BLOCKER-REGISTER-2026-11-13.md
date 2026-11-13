# CEFR-1000 cross-level exact-sense blocker register — 2026-11-13

**Scope:** approved 1,000-total target only; staging branch `cefr-5000-bilingual-qa-staging`. This is an internal editorial triage record, **not independent review, CEFR certification, or permission to publish**.

## Reproducible snapshot
Read `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` from staging on 2026-11-13; blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. The 1,000 entries contain 200 first-pass English definitions, Myanmar meanings and examples per level (A1/A2/B1/B2/C1). Independent approvals are **0/200 for every level**. All 200 per level lack populated `source_level`; `source_english` and `source_burmese` are also empty. This is a **manifest field audit**, not a claim that external research was performed for every entry.

| Level | First-pass written | Independently approved | Missing source_level | Release |
|---|---:|---:|---:|---|
| A1 | 200 | 0 | 200 | HOLD |
| A2 | 200 | 0 | 200 | HOLD |
| B1 | 200 | 0 | 200 | HOLD |
| B2 | 200 | 0 | 200 | HOLD |
| C1 | 200 | 0 | 200 | HOLD |

## High-priority review tickets, preserving source identity
1. **A1 `i`, pronoun** — source `draft/A1-EDITORIAL-STARTER.json`, index 3, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`. Manifest headword is lowercase `i`, but the original example is `I am a student.`. Normalize the orthographic display to capital `I` only after confirming canonical headword rules; check normalization-based deduplication. Myanmar `ကျွန်တော်၊ ကျွန်မ` is context-sensitive and should not be replaced by a single gendered gloss without review.
2. **B1 `independent`, adjective** — source `draft/A2-C1-EDITORIAL-STARTER.json`, index 11, blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`. Definition `Not controlled by another person or organisation.`; example `The team made an independent decision.`. Ask reviewers to distinguish institutional autonomy from a decision made without influence; verify example alignment and Myanmar `အမှီအခိုကင်းသော၊ လွတ်လပ်သော`.
3. **B1 `wonder`, verb** — same source, index 13. `I wonder why the shop is closed today.` exemplifies curiosity rather than amazement. Explicitly restrict the CEFR lookup to the curiosity verb sense, not the unrelated noun or amazement senses.
4. **B2 `anniversary`, noun** — same source, index 107. Example `The company celebrated its tenth anniversary.`; inspect the commemorative-date sense specifically. Prior staging research flagged a possible B1-versus-B2 conflict; do not silently relevel or treat that prior self-research as independent approval.
5. **C1 `signature`, noun** — same source, index 75. Example `Please add your signature at the bottom of the form.`; this is the handwritten-name sense, not `signature` as a distinctive characteristic. Prior research flagged a possible B1-versus-C1 conflict. Seek exact-sense independent adjudication.
6. **C1 `upgrade`, verb** — same source, index 263. `We will upgrade the software next month.` is the improvement/replacement sense; prior research flagged possible B2-versus-C1 conflict. Do not infer C1 from technical subject matter.
7. **C1 `neutral`, adjective** — same source, index 155. `The mediator remained neutral during the talks.` exemplifies nonpartisanship; do not substitute the electrical or colour sense when collecting CEFR evidence.

## Independent-review evidence protocol
For each ticket, record **exact headword, POS, meaning/sense, source publisher, exact source page URL, source-stated CEFR level (or explicitly 'no level supplied'), access/observation date, quotation-length-safe evidence notes, reviewer identity and independent timestamp**. A dictionary page that does not explicitly grade the *same sense* must not be counted as level evidence. Verify natural Myanmar grammar and register with a fluent independent reviewer, and confirm the example uses the graded sense. The existing review-task file must remain the authoritative review workflow; this register does not change any `reviewed_*`, `release_approved`, or editorial-hold flags.

Research entry points for reviewers (**not newly verified sources in this run**):
- Cambridge Dictionary: https://dictionary.cambridge.org/
- English Vocabulary Profile: https://www.englishprofile.org/wordlists
- British Council LearnEnglish: https://learnenglish.britishcouncil.org/

## Release-blocker inventory
No evidence here establishes independent review, final approved lexical-sense manifest, George/Emma four-recordings-per-entry generation and actual listening, browser/mobile regression, physical iPhone Safari QA, GitHub Pages hosting clearance, or production deployment. Existing production 54 lessons, separate IELTS 1,000-word bank, audio and privacy remain protected. **Do not merge, publish or promote.**
