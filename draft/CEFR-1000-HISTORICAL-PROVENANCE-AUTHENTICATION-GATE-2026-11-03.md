# CEFR-1000 historical provenance authentication gate — staging design (2026-11-03)

**Status: proposed control, not implemented or passed. No release authority.** Scope is the user-approved 1,000-entry A1–C1 provisional shortlist, not the superseded 5,000-entry plan.

## Verified baseline and residual exposure

The provisional shortlist blob at `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` is `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; its declared counts are 200 each for A1/A2/B1/B2/C1 and independent approvals are 0 each. Existing `tools/check_cefr_1000_provisional_inventory.py` checks source path syntax, source-index uniqueness and within-path SHA consistency, but **does not authenticate a claimed source blob against Git objects, validate JSON record indices, or compare the selected lexical record with the historical record**. A forged but well-formed SHA/path/index could pass its current checks.

The earlier structural GitHub Actions run [41607329248](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41607329248) reported six successful jobs (ALL, A1, A2, B1, B2, C1), and documentary run [41607329238](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41607329238) reported a successful documentary job. These results predate the later provenance-hardening commit `54745b7df955041ca672165f47385e0bcf73cb43`; they must not be presented as certification of its 22-case suite.

## Implementation acceptance contract

1. Operate only in a staging checkout with sufficient Git history/objects. Do not fetch or modify `main`, merge, deploy or modify production assets. Fail if the required source Git objects are unavailable (for example shallow checkout without needed objects), rather than accepting a plausible SHA.
2. For each of the seven distinct `source_path` / `source_blob_sha` pairs, validate that `git cat-file -t <sha>` returns `blob`, read the exact object bytes with `git cat-file blob <sha>`, and independently recompute its Git blob SHA-1 from the raw bytes. Do not silently substitute the current file at that path.
3. Parse historical JSON strictly, reject duplicate JSON keys, non-array record collections, missing or out-of-bounds `source_index`, and malformed records. First inspect the actual historical schemas; do not assume every file has the same root structure.
4. At each recorded index compare historical headword, POS and source-level information **where present** to the provisional entry. Normalize only documented, conservative whitespace/Unicode conventions; never silently accept semantic, POS or level mismatches. Produce a reviewable mismatch report without changing the provisional entry or claiming CEFR correctness.
5. Pin the expected historical source-path/blob pairs in a separate reviewed lockfile; otherwise an attacker can replace both the claimed SHA and the record in a coordinated edit. Require an independently reviewed change process for this lockfile. A passing Git object lookup alone does not establish trust or editorial quality.
6. Add adversarial cases for missing object, non-blob object, wrong historical index, altered headword, altered POS, wrong pinned SHA, duplicate JSON key and unsupported historical schema. Every forged case must fail closed; preserve a positive fixture for each genuine source schema.
7. Run authentication alongside the existing A1/A2/B1/B2/C1/ALL parallel CI structural jobs, then inspect **actual** run/job conclusions and raw logs for positive and negative tests. A successful parent workflow without logs is insufficient evidence that each mutation ran.

## Release gate remains closed

Written first-pass/independently signed off: **A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0**. No independently reviewed exact-sense CEFR evidence or fluent Myanmar/example signoff is established by this document. The 4,000 George/Emma headword/example assets and genuine listening signoffs, browser/mobile regression, physical iPhone Safari evidence, GitHub Pages hosting clearance, protected 54 lessons / separate IELTS bank / existing audio and privacy checks, and confirmed public deployment are not certified. **Staging only; do not publish.**
