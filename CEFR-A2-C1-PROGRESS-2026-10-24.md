# Burmese English Academy — A2–C1 bounded staging progress (24 Oct 2026 SGT)

**Release decision: BLOCKED / NOT COMPLETE / DO NOT NOTIFY AS COMPLETE.**
Production `main` remains at `dca0db7aa30118ecc18350db8dc406e6cac91554`; staging work is separate.
The default branch has no `cefr-vocabulary-data.js`, confirming this new CEFR corpus has not been deployed there.

## Work actually completed

- Created **40 additional original bilingual draft entries** (English learner definition, Myanmar meaning, part of speech, and original example), for **80 total** in `draft/A2-C1-EDITORIAL-STARTER.json`: **A2 20 / 700**, **B1 20 / 1,000**, **B2 20 / 1,300**, **C1 20 / 1,500**. All 80 are AI-assisted *drafts*, **0 independently reviewed**. These are not approved CEFR assignments.
- Preserved **45 non-public 100-word work packets** for all **4,500 A2–C1 provisional candidates**; **4,420** candidates have no original bilingual first draft yet.
- Added **8 word-specific English dictionary source-page observations** to `draft/A2-C1-SOURCE-EVIDENCE-REVIEW.json`. Each observation has a real page URL, observed dictionary sense, CEFR annotation and date. None verifies the Burmese meaning or grants editorial approval.
- **Four sense-level conflicts** require human reassignment, not automatic overwriting:
  - `great` A2 candidate, *very good* sense A1 on Cambridge: https://dictionary.cambridge.org/dictionary/english/great
  - `retail` B2 candidate, *selling to the public* noun sense C1: https://dictionary.cambridge.org/dictionary/english/retail
  - `accuracy` C1 candidate, *correctness/exactness* noun sense B2: https://dictionary.cambridge.org/dictionary/english/accuracy
  - `spider` C1 candidate, animal noun sense B1: https://dictionary.cambridge.org/dictionary/english/spider
- Four additional observed sense pages: `effort` B1 https://dictionary.cambridge.org/dictionary/english/effort ; `relief` B2 https://dictionary.cambridge.org/dictionary/english/relief ; `client` B2 https://dictionary.cambridge.org/dictionary/english/client ; `abortion` C1 https://dictionary.cambridge.org/dictionary/english/abortion .
- Improved the draft sense wording for `abortion` to distinguish deliberate termination from miscarriage, and clarified `worst` phrasing. These remain unverified Myanmar/English drafts.
- Updated `tools/audit_cefr_a2_c1_drafts.py` to validate all 80 drafts, actual word-specific source URL structure, source-level conflicts, no premature approval, and source-observation provenance.
- **GitHub Actions succeeded**: [A2–C1 source-evidence/draft QA 40002771791](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40002771791) and [45-packet staging audit 40002690533](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40002690533). These are **structural/inventory** passes, not translation or pronunciation certification.
- Existing A1 browser/integration regressions were last run earlier in this staging effort ([browser regression 40000843041](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40000843041), [integration 40000819628](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40000819628)). **No claim of new full cross-device or physical iPhone testing.**
- No merge to `main`, no new published CEFR data or George/Emma files, no change to existing 54 lessons or 1,000 IELTS bank.

## Full 5,000-word release gate: actual evidence status

| Required criterion | Evidence |
| --- | --- |
| A1 500 | 500 editorial first drafts, **0 independent approvals** (previous checkpoint) |
| A2 700 | 20 first drafts, **0 independent approvals** |
| B1 1,000 | 20 first drafts, **0 independent approvals** |
| B2 1,300 | 20 first drafts, **0 independent approvals** |
| C1 1,500 | 20 first drafts, **0 independent approvals** |
| Every word has sense-specific English/CEFR and independent Burmese source review | **NO**. Only 8 A2–C1 source-page observations; 4 provisional level conflicts already detected |
| Both George and Emma audio for every word/example, independently listened to | **NO**. Existing production audio is preserved; CEFR-wide complete audio has not been made/approved |
| Desktop browser, emulated mobile and real physical iPhone Safari QA | **NO**. Older staging browser regression does not count as a physical iPhone test |
| Production deploy, live link, full release acceptance checks | **NO**. `main` unchanged, CEFR data not released |

**Important:** 5,000 provisional frequency-ranked words are not 5,000 valid CEFR assignments. The observed mismatches show why sense-level editorial reclassification and independent English–Myanmar review are mandatory. Never use draft QA success to bypass the release gate.

**Next bounded work:** continue original definitions, Burmese drafts and examples; expand actual word-specific source observations; have qualified independent reviewers resolve CEFR/sense/translation issues; generate and listen-test both voices only after the text is frozen; then do device QA and release checks. Do not send a completion notification before every gate passes.
