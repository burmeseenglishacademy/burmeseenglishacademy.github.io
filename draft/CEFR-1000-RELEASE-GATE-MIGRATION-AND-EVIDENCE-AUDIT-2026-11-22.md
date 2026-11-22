# CEFR-1000 release gate: exact-sense reclassification and evidence integrity audit (2026-11-22)

Scope: **1,000 total only** (A1/A2/B1/B2/C1: 200 each). Staging branch only. This is an author-side engineering audit, **not** independent linguistic approval, CI execution, listening, iPhone testing, or deployment.

## Reproducible source inventory

- `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`: declared 200 each; all 1,000 on editorial hold; independent approvals 0 each; first-pass bilingual text only.
- `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`: 200 tasks each, zero independently approved; source URLs empty; reviewer signatures absent.
- `scripts/cefr-1000-release-readiness-gate.cjs`, blob `c545edc70c427c1a53248dc87298ac28598f3c03`: requires approved manifest, independent evidence register, 4,000 unique checked audio files and listening attestations, physical iPhone Safari, hosting, asset-preservation, privacy and deployment evidence.
- `scripts/cefr-1000-level-structural-qa.cjs`, blob `d78091d1685709612d395abc203d963115ed90fa`: enforces five level counts, editorial holds, task positional alignment, global normalized headword uniqueness. Structural checks do **not** establish CEFR validity.

Observed on 2026-11-22 via the connected GitHub repository on `cefr-5000-bilingual-qa-staging`. Repository source: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/tree/cefr-5000-bilingual-qa-staging

## Release-gate design findings requiring resolution

1. **Cross-level reassignment currently cannot pass without explicit migration.** The release gate compares each approved entry's level against the original provisional level (`original.level===e.level`). Prior author audits identify candidate CEFR conflicts, including `weekend` B1 versus A1 evidence, `ship` B1 versus A2, `actively` C1 versus B2, and `upgrade` C1 versus B2. Independently confirmed corrections would need an explicit, version-pinned replacement mapping, an independently reviewed 200-per-level rebalance and a reviewed migration policy. Do not weaken the equality assertion or silently overwrite the original provenance.
2. **A successful schema check is not cryptographic proof of independence.** The gate checks nonempty reviewer identifiers, signatures represented as timestamps, HTTPS links and distinct author/reviewer strings; it does not independently authenticate reviewer identity, verify signatures, or retrieve and validate external source content. Require independently controlled attestations, immutable review artifacts and reviewer authorization checks before treating a passing schema as actual signoff.
3. **Exact-sense and headword deduplication require human adjudication.** NFKC/casefold uniqueness does not catch semantic duplication such as the related indefinite-article forms `a` and `an`. A distinct headword count alone is insufficient for 1,000 genuinely distinct instructional targets. Preserve the disputed pairs in the audit queue until an independent editor decides the curriculum unit.
4. **Production deployment evidence is post-release by nature.** The gate demands a production commit and deployment evidence. Keep it as a final *verification* gate, separate from the pre-deployment approval decision. Do not force a passing result by inventing production proof or deploying before pre-release QC; a staged preflight and a post-deploy verification stage should remain distinct.
5. **The gate is not currently an executable deployment authorization.** It prints `EVIDENCE_SCHEMA_CHECK_PASSED_NOT_DEPLOYMENT_AUTHORIZATION` when schema checks pass. Maintain protected manual authorization, signed reviewer evidence and a separate non-mutating production integrity check. Never infer launch authorization from the presence of JSON fields.

## Required next engineering work

- Add explicit approved-manifest mapping for independently adjudicated reassignments with source and task provenance; reject all unmapped reclassifications, and enforce exactly 200 final entries at each level.
- Add regression fixtures: duplicate semantic headwords, swapped task IDs, fake reviewer signatures, missing listening records, missing physical iPhone Safari evidence, and missing protected-asset baselines must all fail.
- Capture real GitHub Actions **job** conclusions and logs for a new commit on this branch, rather than relying on the historical run `44811286785` or PR-only run lookups.
- Continue external exact-sense dictionary evidence research and human-independent English/Myanmar/example/CEFR review. Author research must not change any `reviewed_*`, `approval` or `release_approved` flags.

## Truthful status at audit time

| Level | Provisional bilingual entries | Independently checked | Independently approved |
|---|---:|---:|---:|
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

Final-list George/Emma audio: no verified 4,000-file generation or real listening signoff. Physical iPhone Safari: no verified evidence. Current-commit CI: not verified in this audit. Hosting clearance, protected production assets and live deployment: not verified. **Release remains blocked; no merge or production changes authorized.**
