# CEFR-1000: independent reviewer evidence and release gate specification
Observed: 2026-11-23 (Asia/Singapore). Status: **STAGING DESIGN ONLY — NOT APPROVAL OR RELEASE EVIDENCE**.

## Scope and immutable starting evidence
Only the approved 1,000-total scope applies: A1, A2, B1, B2 and C1 each have 200 provisional first-pass entries. Source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551` (inspected 2026-11-23); independent task intake: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, blob `77abf35146825f05e3e58cfdd7a73b3c7302c967` (inspected 2026-11-23). Both declare zero independently approved per level. These are declared counts, not a new manual inspection of every record.

## Proposed independent review evidence contract (not yet implemented)
Each final candidate needs a stable ID, normalized headword, POS, **exact sense identifier**, level, shortlist-source path/index/blob SHA and a frozen hash of the candidate definition, Myanmar meaning and original example pair. Review evidence must identify a real reviewer independent of the author, dated observation, review methodology, decision and exact frozen candidate hash. Store **separate** decisions for (1) English meaning/sense, (2) fluent Myanmar meaning, (3) original example grammar and bilingual semantic alignment, and (4) CEFR evidence for that **same sense and POS**. A dictionary URL without a visible CEFR tag for the matching sense is insufficient. Require a captured citation/quotation within permitted licensing limits, retrieval date, source publisher, and URL. Do not infer CEFR from overall word frequency, other POS, a different dictionary sense, or historical WordNet synsets. Require reviewer acknowledgment of source ambiguity and cross-level duplicates.

Suggested record shape (illustrative, not signoff):
```json
{
  "candidate_id": "CEFR1000-LEVEL-NNNN",
  "candidate_content_sha256": "REQUIRED_ACTUAL_HASH",
  "source_blob_sha": "REQUIRED_ACTUAL_GIT_BLOB",
  "reviewer_id": "REQUIRED_INDEPENDENT_PERSON",
  "independence_attested": false,
  "reviewed_at": null,
  "english": "PENDING",
  "myanmar": "PENDING",
  "example": "PENDING",
  "cefr_exact_sense": "PENDING",
  "cefr_source_url": null,
  "source_observed_at": null,
  "decision": "PENDING"
}
```
The example is intentionally invalid and MUST NOT be interpreted as completed evidence.

## Fail-closed release criteria
1. A signed, frozen **final** manifest contains exactly 200 entries per level and 1,000 total; reject repeated normalized headword+POS+sense identities across all levels and any missing required field. Any replacement or releveling requires a documented human decision and rebalancing.
2. For every final manifest content hash, four independently checked review dimensions are approved by identifiable human reviewers; evidence URLs and observation dates are present, and exact-sense CEFR sources actually support the assigned level. Reject unsigned, stale, mismatched, fabricated or merely author-side decisions.
3. Every final item has headword and example audio for **both** British George and Emma. Check real asset bytes, decoded duration and non-silence; also require per-asset **human listening** evidence linked to immutable file hashes. File presence, waveform checks and synthetic playback alone are not listening signoff.
4. Record actual browser/mobile regression run IDs, outcomes and failures; require documented **physical iPhone Safari** model, iOS version, reviewer, date, tested URL/commit, navigation and audio playback observations. Emulators are not physical-device evidence.
5. Verify GitHub Pages hosting size/build constraints and path/case-sensitive asset loading with measured results. Require an explicit production diff proving all 54 lessons, the separate IELTS 1,000 bank, existing George/Emma production audio and privacy safeguards are preserved.
6. A release gate may only authorize deployment after criteria 1–5 pass. **Deployment confirmation is a separate post-deploy gate:** verify live production URL, deployed revision, public asset checks and preservation after deployment. No CI job can claim this before production actually changes.

## Current editorial blockers
Previously documented author-side investigations flag C1 `signature` (handwritten-name sense reportedly B1 in Cambridge), C1 `upgrade` (equipment/software verb reportedly B2), and A1 `an` (sound-conditioned article grammar evidence does not itself prove A1). Consult the separate dated audit files and verify the sources independently; none is an adjudication. Source landing pages: https://dictionary.cambridge.org/dictionary/learner-english/upgrade ; https://dictionary.cambridge.org/grammar/british-grammar/a-and-the . These links are research leads, not newly independently verified classifications.

## Release decision as of 2026-11-23
A1 200 provisional / 0 independently approved; A2 200 / 0; B1 200 / 0; B2 200 / 0; C1 200 / 0. Final audio inventory/listening, independent signoff, physical iPhone QA, hosting clearance, production-preservation and live deployment evidence: **not established**. **DO NOT MERGE, PUBLISH OR CLAIM READY.** This document adds a proposed evidence contract only; it does not modify shortlist, review tasks, workflows or production.
