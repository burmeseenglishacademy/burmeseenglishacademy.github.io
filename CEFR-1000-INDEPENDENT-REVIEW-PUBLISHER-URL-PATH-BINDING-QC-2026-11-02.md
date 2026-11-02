# CEFR 1,000 — independent publisher URL source-binding repair (2 November 2026)

**Scope:** user-approved 1,000 total (A1/A2/B1/B2/C1: 200 each), not 5,000. **Branch:** `cefr-5000-bilingual-qa-staging`. **Release:** BLOCKED, staging only.

## Real defect found and corrected

The release documentary ledger `tools/audit_cefr_1000_launch_readiness.py` used to accept an alleged dictionary source when the reviewed headword appeared as *any* URL path segment, after splitting underscore suffixes. For `apple`, the former rule admitted `https://dictionary.cambridge.org/blog/apple`, `https://dictionary.cambridge.org/dictionary/english/banana/apple`, and `https://www.oxfordlearnersdictionaries.com/definition/english/banana_apple`. None identifies the exact target publisher entry. This is a structural vulnerability, not evidence that any real reviewer forged a receipt.

The replacement requires exact publisher path shapes: Cambridge `/dictionary/english/apple`; Oxford `/definition/english/apple` with optional numbered homograph suffix `_1`, `_2`, etc. Non-entry, nested, wrong-headword, spoofed underscore and URL user-info paths fail. Broad Oxford PDF locators remain separate research evidence but cannot satisfy direct publisher exact-sense CEFR review. A correctly shaped URL is still **not proof** of an observed source, CEFR classification or human review.

The existing mock-only regression suite now adds **12 negative URL variants** checked against both English-sense and sense-specific CEFR stages, plus **four valid structural URL controls**. All six parallel A1/A2/B1/B2/C1/ALL structural lanes invoke the tests; the documentary no-deploy workflow already invokes them. Actual new GitHub Actions run conclusions and logs must be inspected before any CI pass is claimed.

## Editorial and release blockers

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

All 1,000 remain on editorial hold. Human-independent English/Myanmar/example/exact-sense CEFR receipts, approved manifest, complete British George/Emma headword and example audio and **actual** listening signoffs, integrated browser/mobile regression, physical iPhone Safari, measured GitHub Pages hosting and confirmed production deployment are outstanding. Frozen shortlist, review flags, protected 54 lessons, separate IELTS 1,000-word bank, existing production George/Emma audio and privacy remain unchanged. No merge, main edit, publication or listening/device claims.

Previously verified baseline only: [structural run 41371171713](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41371171713) at `f0f51f8a34485efee690c9b4dd3389faf0422ca5`; it predates this repair.
