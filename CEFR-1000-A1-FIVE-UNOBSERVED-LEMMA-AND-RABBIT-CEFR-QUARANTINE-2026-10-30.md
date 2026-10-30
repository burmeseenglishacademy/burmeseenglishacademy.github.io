# CEFR 1,000 — Final five A1 Oxford-unobserved entries: lemma and rabbit exact-sense quarantine

**Observed:** 2026-10-30 (Singapore). **Scope:** approved **1,000 total** (A1/A2/B1/B2/C1 **200 each**), **staging branch only**. **Status:** **BLOCKED / independent review required**. No source research here constitutes an independent human signoff.

## Evidence and exact editorial risks

The 14 existing A1 Oxford PDF packets contain **203 observations of 195 distinct A1 shortlist headwords**. The five remaining A1 shortlist headwords without a direct Oxford core-list word/POS observation are **is, are, does, did, rabbit**. Their absence is **not** a CEFR label. The remaining 195 observations remain word/POS leads, not exact-sense CEFR approvals.

| Provisional A1 word | Dated direct publisher observation | Independent editorial blocker |
|---|---|---|
| **is** | Cambridge English Grammar Today [be forms](https://dictionary.cambridge.org/grammar/british-grammar/be-) identifies *is* as third-person singular present of **be** | *be* already has its own A1 card. An inflected grammar form is not automatically a second lexical headword. Original “She is at home.” is grammatical; location vs identity needs Myanmar sense review. |
| **are** | Same [Cambridge be forms](https://dictionary.cambridge.org/grammar/british-grammar/be-) lists *are* with you/we/they | Duplicate lemma family **be**; grammar card should be separate from the lexical quota unless independently justified under a genuinely distinct sense policy. |
| **does** | Cambridge [do forms and auxiliary use](https://dictionary.cambridge.org/grammar/british-grammar/do) identifies *does* as third-person singular present of **do** | Existing A1 *do* card already covers lemma. “Does he work here?” is grammatical, but not a separate lexical lemma. |
| **did** | Same [Cambridge do grammar](https://dictionary.cambridge.org/grammar/british-grammar/do) identifies *did* as past form of **do** | Existing A1 *do* card. “Did you eat breakfast?” is grammatical; first-pass Myanmar description omits negative usage. |
| **rabbit** | [Cambridge English Dictionary rabbit](https://dictionary.cambridge.org/dictionary/english/rabbit) labels the animal noun **A2**; [Oxford Advanced Learner's Dictionary rabbit](https://www.oxfordlearnersdictionaries.com/us/definition/english/rabbit_1) displays **Animals a2** as a topic label | The provisional **A1** animal sense conflicts with the directly observed Cambridge **A2** sense label. Oxford topic badges are not Oxford core-list headword/POS labels. No automatic A2 reassignment; independent A1 curriculum rationale or replacement required. |

Source date is **2026-10-30**. Publisher pages and their grammatical/sense descriptions were inspected directly; no Cambridge CEFR level was inferred for the four grammatical inflections. The rabbit Oxford topic label was not promoted to a lexical CEFR classification.

## Proposed resolution — not applied

1. Preserve **is/are/does/did** as useful A1 *grammar forms* outside the counted lexical 200-word quota; propose **four replacement A1 lexical headwords/senses** with dated publisher exact-sense CEFR evidence, original English definitions, natural Myanmar and grammatical original examples. Human-independent reviewer must approve before changing the frozen shortlist.
2. Have an independent reviewer decide whether **rabbit** should be excluded/replaced in A1 or whether a documented, independently justified A1 pedagogical exception is appropriate. The directly observed Cambridge animal sense is **A2**; do not claim A1 publisher backing or silently retier.
3. Require content-hash-bound independent English/Myanmar/example/exact-sense CEFR receipts and later George/Emma headword/example recordings with actual listening signoff. Run approved-corpus desktop/mobile regression, **physical iPhone Safari** review, GitHub Pages measured capacity and preserved-production verification before any deployment.

## Implemented safeguards

- [Five-entry source/provenance packet](draft/CEFR-1000-A1-FIVE-REMAINING-MORPHOLOGY-AND-RABBIT-SENSE-QUARANTINE-2026-10-30.json) freezes original English/Myanmar/examples, historical Git source blob, grammar/sense source URLs, observation date and all independent-review holds.
- [A1 quarantine auditor](tools/audit_cefr_1000_a1_five_morphology.py) cross-checks the **exact five** missing from all Oxford A1 packets, checks 200 A1 first-pass entries and zero approvals, binds Cambridge research to the frozen source, and rejects forged publisher, bilingual, reviewer and listening data.
- [Release validator](tools/validate_cefr_release.py) now **rejects is/are/does/did as independent lexical vocabulary entries** rather than letting 200 unique surface strings mask a four-item lemma-count shortfall. [Negative tests](tests/cefr-release-evidence-gate.py) cover all four forms and confirm base lemmas *be/do* remain valid.
- Both [parallel six-lane structural QA](.github/workflows/cefr-1000-selection-structural-qa.yml) and [documentary no-deployment QC](.github/workflows/cefr-1000-go-live-qc-gate.yml) invoke the new auditor. This is **structural QC only**; verify the new actual run IDs, job conclusions and logs before claiming CI success.

**Unchanged global Oxford word/POS research:** A1 **195/200**, A2 **108/200**, B1 **108/200**, B2 **106/200**, C1 **87/200** = **604/1,000** distinct, **623** observations, **396** without direct Oxford word/POS observations. This new Cambridge grammar/sense packet does **not** increase Oxford coverage or independent approval counts.

**First-pass written / independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. **Real George/Emma final listening:** **0/1,000**. No physical iPhone QA, measured Pages readiness, approved final corpus, or confirmed live deployment. Existing **54 lessons**, separate IELTS **1,000** bank, established George/Emma production audio and privacy must remain unchanged. **No merge, no main edit, no publication.**
