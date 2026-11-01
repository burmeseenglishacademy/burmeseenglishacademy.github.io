# CEFR 1,000 A1 irregular plurals and count/sense QC — 2026-11-01

**Status: STAGING ONLY — NOT INDEPENDENTLY APPROVED — RELEASE BLOCKED.** Scope is the user-approved 1,000 (A1/A2/B1/B2/C1 200 each), not the superseded 5,000. Work exclusively on `cefr-5000-bilingual-qa-staging`. No production edits, merge or deployment.

## Direct publisher observations (2026-11-01)

Eight frozen A1 cards were cross-checked against directly opened Oxford Advanced Learner's Dictionary pages. Source URLs, line locators, historical source Git blob/index, original English/Myanmar/examples and unapproved suggestions are preserved in [the eight-record research packet](draft/CEFR-1000-A1-IRREGULAR-PLURALS-AND-COUNT-SENSE-EIGHT-2026-11-01.json). Oxford page observations support **grammar and sense boundaries**, not independent exact-sense CEFR labels. Oxford topic labels must not be treated as human CEFR signoff.

- **man → men**, **woman → women**, **child → children**, **foot → feet**: irregular plurals; the original singular examples are grammatical. British plural pronunciations differ, especially woman/women and foot/feet. No actual George/Emma listening was performed.
- **fish**: usual plural **fish**, with **fishes** possible for different kinds; countable animal versus uncountable food. Original sentence illustrates the animal.
- **hair**: uncountable collective head hair versus countable individual strands. Original sentence is correct.
- **chicken**: countable living bird versus uncountable meat. Original garden example is correct; Myanmar must preserve the animal sense.
- **orange**: original colour **adjective** is not the noun for a fruit. The original sentence is grammatical and POS-consistent.

All eight are held research leads, not eight proven errors. Original first-pass shortlist remains unchanged. The independent reviewer must decide English sense, fluent Myanmar, grammar, source-backed CEFR, plural pronunciation and whether any alternative should be adopted. Unapproved examples and Myanmar notes are illustrative only.

## Structural QC

A new fail-closed auditor `tools/audit_cefr_1000_a1_irregular_plurals_eight.py` binds all eight records to the frozen shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, validates 1,000 total / 200 per level / unique words / all editorial holds, rejects altered original bilingual/example/source provenance, and tests adversarial tampering and fake independent approval/listening. Wired to all six CEFR matrix lanes (A1/A2/B1/B2/C1/ALL) and the documentary NO DEPLOY workflow. CI run IDs/conclusions must be recorded only after real GitHub Actions inspection; no success claimed at authoring time.

## Release blockers

First-pass written / independently checked: A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. Approved manifest absent. George/Emma final listening receipts **0/1,000**; browser/mobile receipts **0**; real physical iPhone Safari review, measured Pages hosting, human linguistic approval and confirmed deployment all absent. The 54 lessons, separate IELTS 1,000 bank, production voices and privacy assets must remain protected. **Do not publish.**
