# CEFR-1000 shortlist-to-review-task provenance join audit — 2026-11-22

**Scope:** approved 1,000-total project only. Author-side structural audit; **not** independent editorial signoff, CEFR evidence or release approval. Production remains protected.

## Reproducible input provenance
- Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`
- Review tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`
- Repository branch: `cefr-5000-bilingual-qa-staging`; observed 2026-11-22.
- Method: parse both JSON documents and compare **every positional pair** for headword, level, part of speech, source path, source index, source blob SHA, and the review task's pinned shortlist blob SHA. Check counts independently. This is a positional binding check, not a substitute for semantic sense comparison or a uniqueness validator.

## Observed results
- 1,000 provisional shortlist entries and 1,000 administrative review tasks.
- Per-level first-pass written counts: A1 **200**, A2 **200**, B1 **200**, B2 **200**, C1 **200**.
- Independently approved: A1 **0**, A2 **0**, B1 **0**, B2 **0**, C1 **0**.
- Positional provenance mismatches across the seven compared fields: **0 / 1,000**.
- Source-path distribution: A1 editorial starter **200**; A2–C1 editorial starter **704**; source recovery batches 57 **42**, 58 **32**, 59 **8**, 60 **5**, 61 **9** (sum **1,000**).
- These numbers show administrative traceability only. They do **not** show that any source entry has independently corroborated dictionary-sense CEFR evidence or accurate Myanmar text.

## Fail-closed implications and next tests
1. Preserve the task-to-shortlist SHA binding when any provisional entry is changed; reject stale review-task snapshots rather than silently accepting mismatched revisions.
2. Add negative regression cases changing a source index, source blob SHA, POS or headword while retaining a superficially plausible task ID; each must fail independently. Existing task-ID swap regression is not sufficient to prove all provenance fields are enforced.
3. Independently inspect original source files at their pinned blob SHAs before treating their content as reliable. A matching pointer does not authenticate linguistic correctness.
4. Do not count author research or unassigned tasks as independent verification. Require attributable human-independent English, Myanmar, original-example and **exact-sense** CEFR signoff with observed source URL/date for every final sense.
5. Final release must additionally prove exactly 200 deduplicated senses per level, all 4,000 British George/Emma headword/example files generated **and listened to**, mobile/browser and physical iPhone Safari checks, GitHub Pages hosting clearance, protected 54 lessons/IELTS bank/existing audio/privacy, and confirmed production deployment. Missing evidence means **NO RELEASE**.
6. GitHub Actions level-specific **current-commit** job conclusions and logs were not verified by this audit; historical failures cannot be treated as passes.

**Release state: STAGING ONLY; editorial hold on all 1,000.** No approval flags or production files modified.
