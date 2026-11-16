# CEFR-1000 independent-review intake integrity — 2026-11-16

**Scope:** the approved 1,000-total project, exactly 200 provisional A1/A2/B1/B2/C1 entries. **Status:** staging-only; no independent signoff.

## Directly observed repository evidence
- `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` was fetched from staging; Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. It declares 200 entries per level, zero independently approved at each level, and first-pass-unverified English, Myanmar and examples. This is a *declared* inventory, not a new independent lexical count.
- `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json` was fetched from the same staging branch on 2026-11-16; Git blob `88f472e4c79e5e9b6ae5957f5244f9cb60dc0ef2`; its returned UTF-8 content length was **zero bytes**. An empty file is not valid JSON and supplies no reviewer assignments, decisions or signoff. Do not treat its filename as evidence of review.
- The staging workflow `.github/workflows/cefr1000-staging-qa.yml` (blob `3f10b70da9fd86ca1d42b9c9d5881c961b3c1456`) runs five level-specific provisional jobs and five adversarial regression jobs. Structural CI does not certify linguistic accuracy, audio listening, mobile QA or release readiness.

## Critical recovery decision (editorial hold)
The independent-review task source is unusable as currently returned. Restore the intended task records from a verified prior commit or reconstruct *new pending assignments* from the 1,000 provisional entries, clearly recording their provenance and creation date. Never infer that reviewers completed any assignment. A restored task queue should require a stable entry/sense ID, CEFR level, source shortlist blob SHA, independent reviewer identity, review timestamp, English decision, fluent Myanmar decision, original-example decision, exact-sense CEFR evidence URL and observation date, plus evidence-backed acceptance or rejection. All absent fields must fail closed. The original shortlist must remain unchanged until authorized editorial changes are separately reviewed.

## Release-blocking acceptance checks
1. Parse both JSON files strictly; reject empty, truncated or non-object review manifests. Reconcile exactly 200 unique canonical headword-and-sense keys per level and 1,000 total without cross-level conflicts.
2. Match each independently signed review to the exact shortlist entry and immutable content version; disallow self-evaluation, missing independent reviewer, unsupported source, generic lemma-only CEFR evidence, stale content hashes or conflicting review outcomes.
3. Require separate positive independent English, Myanmar, example and CEFR decisions; preserve source URLs and dated observations. Provisional drafts and automated checks are **not** signoff.
4. Verify generated British George/Emma audio for both headword and example for each approved entry, with real recorded listening decisions; missing or synthetic listening attestations block release.
5. Require browser/mobile regression, evidence from a real physical iPhone Safari test, GitHub Pages hosting checks, production asset-preservation checks and a confirmed deployment. No merge, main edit or publication while any gate fails.

## Evidence boundaries
No source-backed exact-sense CEFR assignments, independent reviewer approvals, completed voice listening, physical iPhone QA or production deployment are established by this document. The separate IELTS vocabulary bank, 54 existing lessons, existing George/Emma production audio and privacy settings are out of scope and must remain untouched.

**Next safe action:** repair the empty task manifest on staging with verifiable pending-only assignments, then independently review the highest-risk ambiguous senses before any release decision.
