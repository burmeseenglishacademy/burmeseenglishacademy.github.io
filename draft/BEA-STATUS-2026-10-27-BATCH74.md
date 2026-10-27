# BEA CEFR 5,000 — Batch74 staging evidence report
**27 October 2026, Singapore. STAGING ONLY. NOT INDEPENDENTLY APPROVED, MERGED, DEPLOYED OR RELEASED.**

## Substantive bilingual editorial drafting
- Wrote **60 new original English-definition / natural Myanmar-meaning / original English-example drafts**: **A2 15, B1 15, B2 15, C1 15**.
- Each entry has a proposed part of speech, a single targeted sense, its own example sentence, explicit unverified source fields and a reversible editorial hold. There are **28 additional targeted editorial-risk flags** for level uncertainty, uncommon register, sense ambiguity, legal/specialist uses or British variants. Risk flags do not imply the other entries are independently checked.
- Wrote **60 separate independent-review task records** for English dictionary sense/POS, fluent Myanmar meaning, grammatical example, source-supported sense-specific CEFR and real George/Emma audio listening. Every task is pending; no review is falsely marked complete.
- Wrote **60 reversible quarantine records**. All 60 drafts are **held, unapproved, not in the published vocabulary dataset, and not audio-generated**.

## Observed candidate screening, not editorial approval
- Prepared **549 A2–C1 candidate-level rows**: A2 82, B1 133, B2 137, C1 197. Screened all against the 5,000-word unverified seed pool and **4,658 distinct previously authored staged wordforms**.
- Actual GitHub Actions candidate run [40440285272](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40440285272) succeeded across A2, B1, B2, C1 and ALL. Decoded ALL-job log **121978723102** reported **261 mechanically clear-only** candidate rows and **288 flagged/quarantined** rows; per-level clear-only: A2 43, B1 47, B2 66, C1 105. Persisted every screening result and risk code in `draft/BATCH74-CANDIDATE-TRIAGE.json`, preserving the observed raw totals. The corrected candidate run [40440303580](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40440303580) also succeeded across the matrix.
- A further cross-level candidate comparison detected **nine wordforms proposed at two levels**: *credibility, resilience, transparency, complacency, austerity, corroboration, disillusionment, reciprocity, scepticism*. All nine have an additional reversible hold overlay `draft/BATCH74-CROSS-LEVEL-CANDIDATE-HOLDS.json`. This overlay is separate from the raw 261/288 mechanical totals; notably *scepticism* appeared mechanically clear at B2 and C1 but is **not** treated as CEFR-resolved. None of the 60 selected drafts is in the nine-conflict overlay.
- Proper names, suspect WordNet seed senses, already-authored headwords, existing editorial holds and provisional pool-level disagreements are screened and held rather than used as filler. A mechanically clear candidate is **not** an independently approved word or CEFR classification.

## Actual structural GitHub Actions and production guard
- Final Batch74 structural workflow [40440540175](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40440540175), at staging commit `8810b6f6120c297e7ebd9e0275595a9ecfacfc1e`, **completed successfully** in all five A2/B1/B2/C1/ALL jobs.
- Decoded ALL-job log **121979571946**: `BATCH74 ALL checked 60 risk flags 28 problems []`; `PASS: STRUCTURAL ONLY. Zero independent approvals. No audio, merge or publication.`; `PASS: protected production assets unchanged`. The nonpublishing report artifact was uploaded (artifact ID **12705787846**). Earlier Batch74 structural run [40440480997](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40440480997) also passed all five jobs before the additional cross-level hold check.
- Previous Batch73 run [40431072011](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40431072011) has now been independently inspected: all five jobs **passed**, with ALL-job log showing **50 drafts, 35 risk flags, no structural problems and protected assets unchanged**. This resolves Batch73's earlier *run status not yet observed* limitation; it does **not** grant linguistic approval.
- The structural audit explicitly checks the CEFR publication placeholder still contains `entries: []` and `UNVERIFIED_DRAFT_DO_NOT_PUBLISH`. The workflow has **no deployment step**. Protected production files are diff-checked against `main`: 54 lessons' content, IELTS 1,000 bank, George/Emma audio/player and privacy assets were not modified.

## Exact ledger: written versus independently checked
The official structurally eligible first-pass written ledger **remains unchanged**; quarantined drafts do not count towards eligibility.

| Level | Target | Eligible first-pass written | Independently checked / approved | New Batch74 held drafts |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 654 | 0 | 15 |
| B1 | 1,000 | 947 | 0 | 15 |
| B2 | 1,300 | 1,133 | 0 | 15 |
| C1 | 1,500 | 956 | 0 | 15 |
| **Total** | **5,000** | **4,190** | **0** | **60** |

**810 eligible slots remain.** The staging corpus has a derived **4,718 distinct authored wordforms** (4,658 observed by preflight before Batch74 + 60 noncolliding drafts). This is a written staging-inventory count, **not 4,718 approved words**. Derived per-level proposed distinct authored counts including held drafts: A1 500, A2 774, B1 1,059, B2 1,252, C1 1,157. Their sum exceeds the distinct count because of historical cross-level overlaps; the **24 previously quarantined cross-level wordforms remain unresolved**. The nine new candidate-only conflicts are separate and are not added to the authored inventory.

## Staging commit and test trail
- Candidate shortlist: `74925acbad8e0d7d5894abdded43006a0239678b`
- Candidate workflow / literal-pipe correction: `41bacd051bed6d57344f30e15f3040112560be45`, `e0cb3c56b4b16a63825d1d1bdc9b14e369ef7070`
- Bilingual drafts: `c2f0d8b307820428a41d8ef6f378be1e79460cf8`
- Independent-review tasks: `596109ee3e819e98b7f5bcf68304144df3a2b9fc`
- Reversible quarantine: `aa94ff947e38c3002e1271c2686d68b8b862a8ba`
- Observed candidate triage: `da3fa729a17ca1e64c6ac0aa2770c82b56a42ba6`
- Structural auditor / initial matrix workflow: `83805e504970870c8fc04b295598c52331e3cef2`, `6286960a78b627a7c0708aeded5363c582b18299`
- Cross-level candidate hold overlay: `927f3f353a0e1b4e935d1984b5604c5f30bb2421`
- Strengthened audit and final workflow: `076a9b48e1c6827b60da171bd481bc9afb66f63c`, `8810b6f6120c297e7ebd9e0275595a9ecfacfc1e`

## Blockers and release conditions
**No independent English learner-dictionary review, independent fluent Myanmar sense review, independent grammatical example review, or source-backed CEFR approval has occurred for the 60 new drafts.** Existing historical approval ledger remains zero. No new George/Emma pronunciation files were generated or actually listened to. No browser/mobile or physical iPhone Safari playback validation, hosting-limit approval, or production deployment has occurred. Historical duplicate occurrences and cross-level holds require reconciliation. A successful structural workflow cannot substitute for linguistic, audio, device or hosting evidence.

**Release gate remains closed.** Do not merge, publish or claim full completion. Continue high-throughput original drafts only from defensible candidates, and prioritise independent sense-level reviews, unresolved cross-level holds and real pronunciation/device evidence before approval.
