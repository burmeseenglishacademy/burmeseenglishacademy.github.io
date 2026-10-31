# CEFR 1,000 — C1 fifteenth Oxford absence and direct sense triage (2026-11-01)

**Scope:** the user-approved **1,000 total** A1–C1 (200 per level), **not** the abandoned 5,000-word plan. Branch `cefr-5000-bilingual-qa-staging` only. **Release BLOCKED; no production publication.**

## Publisher observations and editorial work

On **1 November 2026**, both [Oxford 3000 by CEFR](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) (12 pages) and [Oxford 5000 by CEFR](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) (8 pages) were directly inspected for twelve **previously unobserved** provisional C1 word/POS pairs: **embellish, endemic, enigma, ephemeral, exacerbate, exonerate, fallacy, fervent, galvanize, incongruous, introspection, juxtapose**. All twelve were **absent from both inspected core lists**. Absence is **not** an Oxford CEFR classification and is **not** independent confirmation of C1.

Four [direct Oxford dictionary](https://www.oxfordlearnersdictionaries.com/) sense checks:
- [embellish](https://www.oxfordlearnersdictionaries.com/definition/english/embellish), page text lines 88–116: formal verb sense 1 decorates a physical object; sense 2 adds potentially untrue details to a story. Draft combines senses; example illustrates the latter.
- [endemic](https://www.oxfordlearnersdictionaries.com/definition/english/endemic), lines 88–108: `endemic in/among` for persistent presence, `endemic to` for native species; do not conflate disease prevalence and species nativeness.
- [exonerate](https://www.oxfordlearnersdictionaries.com/definition/english/exonerate), lines 88–114: formal official declaration of non-responsibility; patterns `exonerate somebody from/of something`. Draft's broad “show” meaning needs review.
- [juxtapose](https://www.oxfordlearnersdictionaries.com/definition/english/juxtapose), lines 88–112: often passive, `juxtapose A with/and B`; highlights contrast **or** a new relationship, whereas the draft describes only differences.

These are **direct dictionary sense leads, not source-backed independent exact-sense CEFR approvals**. Do not attribute unrelated Oxford “Word of the Day” footer CEFR labels to these headwords.

## Provenance and editorial hold

The [twelve-record evidence packet](draft/CEFR-1000-OXFORD-C1-FIFTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-11-01.json) preserves original English definitions, Myanmar meanings, original examples, source path, source indices **28–39**, source Git blob `7eaf88b9ed7687b26ccde713262f10fb209743a8`, official URLs, observation date, four dictionary locators and four **unapproved** Myanmar/example alternatives. Shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551` remains frozen. All twelve are on editorial hold; **zero independent reviewer receipts**, **zero actual listening signoffs**, and **no approval flags changed**.

The [fail-closed source/provenance auditor](tools/audit_cefr_1000_oxford_c1_fifteenth_twelve.py) binds the packet and original historical Git source and defines **185 adversarial forged-evidence/approval mutations**. It is wired into six parallel CEFR structural lanes and documentary no-deployment QC. Passing these structural tests would **not** establish human linguistic review.

## CI-verified source reconciliation (not independent linguistic approval)

Actual [parallel structural run 41231670762](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41231670762) completed **SUCCESS** in all **A1/A2/B1/B2/C1/ALL** jobs; [documentary no-deploy run 41231670795](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41231670795) completed **SUCCESS, report-only**. Both tested code SHA `74aa3401a4f635ae16c0b058789189e1847df7eb`. Actual ALL and documentary logs confirmed **185/185** forged C1 source/approval mutations rejected; ALL logs also confirmed **25/25** cross-batch and **5/5** reviewer-handoff mutations rejected, and documentary logs confirmed protected production assets unchanged. Structural ALL artifact ID `13053549013`; documentary blocker artifact ID `13053708478`. An intermediate code SHA `dfc7d8609b8fe925747d0277b5dd702ffbbf3d6d` failed from temporarily inconsistent handoff counts; corrected before the final successful runs.

The CI-verified cross-batch Oxford **research observation** totals are A1 **195/200**, A2 **200/200**, B1 **200/200**, B2 **200/200**, C1 **159/200** = **954/1,000 distinct**, with **973 source packet observations**. Remaining without Oxford observations: **46**. Human review priority expectations: **70 unlisted (not CEFR labels)**, **61 publisher-higher**, **352 publisher-lower**, **471 word/POS matching but exact-sense unverified**, **46 unobserved**. These are source observations, not 954 approvals. Actual job conclusions and logs were inspected; this is structural research QC, not independent human review.

**First-pass written / independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. Final British George/Emma **actual listening signoffs: 0/1,000**. Independent human English/Myanmar/example/exact-sense CEFR review, approved deduplicated manifest, complete final dual-voice audio and real listening, browser/mobile and physical iPhone Safari evidence, measured Pages release artifact/hosting and confirmed production deployment remain missing.

**Production protection:** do not merge or modify main; preserve 54 lessons, separate IELTS 1,000-word bank, established George/Emma audio, and privacy features. **STAGING ONLY / NO PUBLICATION.**
