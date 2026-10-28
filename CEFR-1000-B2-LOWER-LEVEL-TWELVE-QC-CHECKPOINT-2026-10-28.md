# CEFR 1,000 — additional B2 direct Oxford word/POS source triage (2026-10-28)

**Decision: BLOCKED / STAGING ONLY.** The user-approved scope is **1,000 total words**, A1/A2/B1/B2/C1 **200 each**, not the superseded 5,000-word plan. The intentionally retained staging branch is `cefr-5000-bilingual-qa-staging`. This report documents **source observations**, never independent human English/Myanmar/example/CEFR signoff.

## Direct publisher evidence and exact shortlist snapshots

Directly inspected the [Oxford University Press *Oxford 3000 by CEFR level* PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-28**. Source page numbers are 1-based PDF pages and extracted line locators are 0-based. Oxford 3000 is a **headword/part-of-speech** CEFR list; a label is not a verified dictionary **exact-sense** classification. A mismatch does not itself prove the proposed level is wrong. [Machine-readable source packet](draft/CEFR-1000-OXFORD-B2-LOWER-LEVEL-TWELVE-2026-10-28.json) preserves each original shortlist definition, fluent-Myanmar draft, example, source file/index/blob, publisher URL, date, page/line and an independent-review task.

| B2 provisional headword | Oxford word/POS | PDF page / line | Editorial question |
| --- | --- | --- | --- |
| plastic | A2 | 6 / 1477 | Material noun; draft Myanmar gloss may be unnecessarily wordy |
| childhood | B1 | 7 / 1895 | Ordinary life-stage sense; B2 placement needs distinct source evidence |
| weapon | B1 | 10 / 2567 | Definition may be too narrowly limited to conflict |
| theatre | A1 | 3 / 783 | Building sense, not dramatic art or operating room |
| sight | B1 | 9 / 2434 | Vision ability sense; assess glasses/improved sight example |
| approval | B2 | 10 / 2630 | Word/POS matches; distinguish formal authorisation from favourable opinion |
| print | B2 | 12 / 3092 | Word/POS matches; exact visible-text sense still requires source |
| comedy | A2 | 4 / 1063 | Ordinary humorous show/genre; Myanmar scope needs review |
| advertising | A2 | 4 / 924 | Activity versus one advertisement; ordinary marketing sense |
| survive | B1 | 10 / 2489 | Definition mixes remain alive and business survival; example is plants |
| comparison | B1 | 7 / 1915 | Ordinary comparing sense; no distinct B2 sense demonstrated |
| destroy | A2 | 5 / 1120 | Fire-destroys-building is ordinary physical-destruction sense |

**Ten of twelve** Oxford word/POS labels are lower than the provisional B2 tier: theatre (A1); plastic, comedy, advertising and destroy (A2); childhood, weapon, sight, survive and comparison (B1). Two labels match B2: approval and print. No word was retiered, deleted or automatically approved. Independent reviewers must evaluate intended exact senses, English definitions, natural Myanmar meanings, original-example grammar, and whether a distinct B2 sense can be evidenced. For retained lower-level ordinary senses, the release gate requires a changed definition/example plus an independently checked publisher-backed B2 exact-sense receipt, discrepancy rationale and content hash.

## Safeguards and executed CI

- Created `tools/audit_cefr_1000_oxford_b2_lower_twelve.py`, pinning all twelve source labels and locators to the canonical shortlist, enforcing editorial hold and rejecting **26** fake publisher, Myanmar, English, example, provenance, missing-row, duplicate-row and fabricated independent-review mutations.
- Integrated the auditor into all six parallel structural jobs (A1/A2/B1/B2/C1/ALL) and documentary no-deploy QC.
- Extended `tools/audit_cefr_1000_launch_readiness.py` to reject any retained entry without separate independently verified B2 exact-sense resolution, and added **empty** `oxford_b2_lower_twelve_review_receipts` to the release-evidence template (zero signoffs).
- Initial [structural run 40658307137](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40658307137) failed on a duplicated B2 keyword in generated auditor code; [run 40658392772](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40658392772) still failed the B1 matrix because of a duplicated CLI choice. Both defects were corrected, without weakening release checks.
- [Documentary no-deploy run 40658480572](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40658480572) **SUCCESS** on commit `74a8bb26f2e94c7bb3af4c2e09af5ac7cc428e73`: actual log reports 12 observations, 10 lower-level conflicts, **26/26 negative mutations rejected**, zero independent approvals, and protected production paths unchanged. This is a successful **report-only staging audit**, not release readiness.
- [Structural run 40658480451](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40658480451) **SUCCESS** on commit `74a8bb26f2e94c7bb3af4c2e09af5ac7cc428e73`: verified **all six A1/A2/B1/B2/C1/ALL job conclusions** and the actual ALL-job log; **26/26** source-tampering and fake-review mutations rejected. CI validates structure and source provenance only, not independent language review or launch.

## Exact progress and blockers

| CEFR level | First-pass written | Independently approved | Both-voice final listening signoffs |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

The approved-release manifest, human-independent exact-sense and bilingual signoffs, final George/Emma headword and example recordings with real listening, full browser/mobile regression, **physical iPhone Safari** review, measured GitHub Pages hosting constraints, and confirmed production deployment are all **missing/unverified**. Preserve 54 existing lessons, separate IELTS 1,000-word bank, production George/Emma audio and privacy assets. The CI protected-path diff against main passed, but is not a substitute for a full production asset audit. **No main changes, merge, publication, or real device/listening claims.**
