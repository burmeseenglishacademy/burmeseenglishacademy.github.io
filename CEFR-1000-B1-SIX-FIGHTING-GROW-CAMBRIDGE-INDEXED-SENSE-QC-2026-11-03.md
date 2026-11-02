# CEFR 1,000 — B1 six-word Cambridge indexed exact-sense research, 3 November 2026

**STAGING ONLY — editorial research, not independent approval.** Approved project scope is 1,000 TOTAL, not the superseded 5,000: A1/A2/B1/B2/C1 each have 200 first-pass written candidates and **0 independently approved**. The frozen shortlist Git blob is `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. The existing separate IELTS 1,000-word bank, 54 lessons, production George/Emma audio and privacy settings remain out of scope for edits.

## New exact-sense leads from publisher-owned search-index results

Observed **2026-11-03** from Cambridge Dictionary publisher-owned indexed pages. These pages were exposed through search results; **not** independent human source verification, and not a claimed direct full-page human review. Preserve publisher URLs and revisit the current page and exact sense with an independent editor.

| Frozen B1 card | Cambridge indexed sense / CEFR | Editorial finding |
| --- | --- | --- |
| [fighting](https://dictionary.cambridge.org/dictionary/english/fighting), noun uncountable | **B2** for fighting activity, especially in war | **Conflict:** provisional B1 uncountable noun and example “The fighting stopped before sunrise.” match the B2 research sense. Do not borrow B1 from the different countable noun *fight* or the verb *fight*. |
| [damage](https://dictionary.cambridge.org/dictionary/english/damage), noun uncountable | **B1** for harm or injury | Alignment lead; distinguish plural legal *damages* and the verb. |
| [directly](https://dictionary.cambridge.org/dictionary/english/directly), adverb | **B1** for no intermediary | Alignment lead; distinguish direct connection from a frank or honest reply. |
| [disease](https://dictionary.cambridge.org/dictionary/english/disease), noun countable/uncountable | **B1** for illness | Alignment lead; avoid overbroad inclusion of injuries and check countability. |
| [doubt](https://dictionary.cambridge.org/dictionary/english/doubt), noun countable/uncountable | **B1** for uncertainty | Alignment lead; distinguish the verb and idiomatic *no doubt*. |
| [grow](https://dictionary.cambridge.org/dictionary/english/grow), verb | **A2** for becoming bigger/plant development; distinct **B1** hair growth | **Conflict:** the B1 frozen definition and plant example match the indexed A2 sense, not the separately indexed B1 hair-growth sense. |

The six original English definitions, Myanmar glosses, original examples and historical source paths/indexes/blob hashes are preserved verbatim in [the research packet](draft/CEFR-1000-B1-SIX-FIGHTING-GROW-CAMBRIDGE-INDEXED-SENSE-2026-11-03.json), with six **unapproved** English/Myanmar/example teaching alternatives. These alternatives are for independent bilingual editing, not learner release. No CEFR level, definition, Myanmar meaning, example or review flag in the frozen shortlist was changed.

## Fail-closed mechanical QA

The [six-record auditor](tools/audit_cefr_1000_b1_six_fighting_grow_indexed.py) pins the frozen shortlist and new research packet Git blob hashes, checks the five actual 200-word quotas, global written-headword uniqueness, all hold and false approval flags, historical source linkage, six publisher URL/sense/level/conflict observations and source-access honesty. Its synthetic negative tests reject forged independent approvals, altered publisher levels/URLs, future observations, inflated direct-source claims and altered frozen text. These checks **cannot** authenticate a human editor, source exact-sense judgment, real audio listening or device QA.

Both staging-only GitHub Actions workflows now invoke this auditor: A1/A2/B1/B2/C1/ALL parallel structural lanes and documentary no-deployment gate. As of authoring this checkpoint, the new push-triggered runs had started but were **not yet verified complete**. Do not describe this auditor as CI-passed until the actual run/job conclusions and decoded logs have been checked. Previous structural run [41486672330](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41486672330) was **cancelled** after A1/A2/B2/C1/ALL success because the B1 lane was cancelled, so it was **not** an all-six-lane success; the documentary [41486697252](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41486697252) succeeded as a blocker-reporting workflow.

## Release blockers remain unchanged

Written/independently approved: **A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0**. All 1,000 are on editorial hold. No approved manifest; no genuine independent English, Myanmar, original-example and exact-sense CEFR signoffs; no complete British George/Emma headword/example recordings with real listening receipts; no final browser/mobile or physical iPhone Safari QA; no measured GitHub Pages hosting clearance; no signed production asset preservation and confirmed live deployment. **RELEASE BLOCKED — STAGING ONLY.** No merge, publication or main-branch modification is authorised by these findings.
