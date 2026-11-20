# CEFR-1000 raw GitHub Actions log audit — 2026-11-20

**Status: STAGING ONLY / RELEASE BLOCKED.** This audit directly inspected decoded raw logs for all seven jobs of [run 44603665487](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44603665487), **historical commit** `39214de5f6cfc3bf4127556f449c4acc17b6d2f4` (push event, 2026-11-19 UTC). Observation date: **2026-11-20**. These results do **not** establish that later documentation commits ran CI.

## Observed execution evidence

| Job | GitHub job ID | Directly observed raw-log result |
|---|---:|---|
| A1 structural | 135841507141 | JSON `mode=structural`, `level=A1`, `errors=[]`, `independent_approval_inferred=false` |
| A2 structural | 135841507188 | Same output for A2 |
| B1 structural | 135841506894 | Same output for B1 |
| B2 structural | 135841507155 | Same output for B2 |
| C1 structural | 135841507191 | Same output for C1 |
| Negative mutation suite | 135841506263 | 16 individual `PASS rejected:` lines and final `All sixteen negative cases rejected; no independent review inferred.` |
| Release-blocker | 135841506716 | `Verified controlled, explicit release denial; no independent approval inferred.` |

The negative suite explicitly rejected: missing entry, cross-level duplicate, fabricated approval, fake reviewer, wrong source provenance, relabelled task, altered source shortlist SHA, false release status, missing Myanmar meaning, missing English definition, missing example sentence, missing source blob, unverified CEFR evidence URL, fabricated CEFR review, fake signed review, and invalid source index.

**Log provenance:** GitHub Actions decoded job logs retrieved through the GitHub connector on 2026-11-20. Per-job audit URLs follow the pattern `https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44603665487/job/<job-id>`. This audit is of actual output, not merely job conclusion metadata. Node 20 deprecation warnings appeared for checkout/setup-python actions forced onto Node 24; they did not fail these historical jobs. Monitor action-version migration separately.

## Exact inventory and hold

| Level | Provisional first-pass written | Independently checked/approved | Audio generated and actually listened/signed |
|---|---:|---:|---|
| A1 | 200 | 0 | No verified signoff |
| A2 | 200 | 0 | No verified signoff |
| B1 | 200 | 0 | No verified signoff |
| B2 | 200 | 0 | No verified signoff |
| C1 | 200 | 0 | No verified signoff |
| **Total** | **1,000** | **0** | **Not verified** |

Shortlist provenance: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Review tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`, previously inspected 2026-11-20.

**Not established by passing CI:** exact-sense CEFR evidence and independent English/Myanmar/example review; approved 200 deduplicated senses at each level; British George/Emma final headword and example audio with real listening; browser/mobile regression and physical iPhone Safari evidence; GitHub Pages hosting clearance; protected 54 lessons, separate IELTS 1,000 bank, production audio and privacy integrity; confirmed production deployment. Keep all 1,000 on editorial hold, do not merge or publish, and do not infer approval from this audit.
