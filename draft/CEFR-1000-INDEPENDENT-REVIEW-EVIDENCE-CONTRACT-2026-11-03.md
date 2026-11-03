# CEFR-1000 independent evidence contract — 2026-11-03

**Status:** staging-only specification; NOT independent verification, NOT a release approval.

## Immutable inputs and quotas
- Frozen input: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (observed blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`).
- Separate reviewer assignments: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`.
- Exact target: A1/A2/B1/B2/C1 = 200 **approved lexical senses** each; total 1,000. Do not count orthographic forms as distinct senses without a documented reviewer decision (especially `a` versus `an`); preserve case-sensitive lexical identity (`I` versus `i`).
- The provisional 200-per-level counts are **written first passes**, not approvals. As of this checkpoint, independent approvals are A1=0, A2=0, B1=0, B2=0, C1=0.

## Evidence per lexical sense (mandatory; absent evidence means FAIL)
Each approved entry needs a stable sense identifier, normalized headword, level, part of speech, English definition, fluent Myanmar gloss, original grammatical example, exact-sense CEFR publisher source URL, access/observation date, quoted or paraphrased source sense identifier, reviewer identity independent of drafting, reviewer decision timestamp and review of four separate dimensions: English sense, Myanmar gloss, example grammar, and CEFR placement. If publisher evidence covers only another sense or part of speech, **fail**, rather than inheriting its CEFR level. A search snippet is a research lead, not a verified direct page inspection. Source access failures must be recorded explicitly.

## Independence and conflict resolution
- Self-evaluation, automated checks, AI-generated prose, reviewer-task existence, and GitHub Actions success never count as independent human signoff.
- Require a human-independent review record tied to the exact content digest of each final entry. If wording or level changes, invalidate the corresponding approval.
- Reject conflicting CEFR classifications until the exact sense is resolved; keep the original record and a dated adjudication with URLs. A sense reassigned across levels requires quota rebalancing, deduplication, and renewed review.
- Historical WordNet, named-entity, morphological and unsourced CEFR risks must be checked individually. Do not promote a historical source's generic vocabulary label into exact-sense CEFR evidence.

## Audio and real listening (mandatory)
For every approved sense require George British headword + example and Emma British headword + example: **4 audio assets per sense, 4,000 expected assets for 1,000 senses** (unless a formally approved revised audio policy exists). Require file paths, SHA-256 digests, generator/model provenance, durations, and a *human listening* record per file with reviewer, timestamp, pronunciation and intelligibility verdict. Generating files or checking file headers is not listening. A changed example invalidates its corresponding audio and listening signoff. Never modify existing production George/Emma assets to satisfy staging.

## Device, privacy, hosting and production gates
- Browser/mobile regression evidence must name browser version, viewport/device, build commit, tests and observed results.
- Physical iPhone Safari evidence must name real iPhone model, iOS/Safari version, tester, observation date, screenshots or recorded results and listening tests; simulator-only checks fail.
- Measure GitHub Pages limits against actual artifact count, size, repository footprint and bandwidth/build constraints; include dated official policy URL and measured build results.
- Verify unchanged production 54 lessons, independent IELTS 1,000-word bank, existing George/Emma audio and privacy/no-tracking behavior by pre/post content checksums.
- Only after all gates pass may a separately documented, authorised launch procedure run. Confirm deployed commit, public URL, HTTP success and actual production smoke tests; never equate a green staging workflow with deployment.

## CI fail-closed checks to implement or maintain
1. Reject non-1,000 total, non-200 per level, duplicate normalized headword+sense keys, missing source metadata or unmatched reviewer digests.
2. Reject `approved` or `reviewed` flags without verifiable independent records; reject missing/malformed dates, inaccessible evidence and contradictory sense/POS.
3. Reject missing audio or missing real listening records, digest mismatch, empty files, or unverifiable voice identity.
4. Reject missing real-device QA, hosting evidence, preservation hashes or deployment confirmation.
5. Run A1/A2/B1/B2/C1 independently in parallel and an ALL aggregate gate; inspect each GitHub Actions job conclusion **and logs** before claiming success. Synthetic mutation tests should demonstrate each rejection rule.
6. No workflow may deploy or merge from this staging branch while any gate is absent.

## Open release blockers
All 1,000 entries remain editorially held; 0 independently approved. No verified complete 4,000-asset audio set, no human listening signoffs, no physical iPhone Safari evidence, no measured hosting clearance, and no confirmed production deployment. **RELEASE BLOCKED.** This document establishes requirements; it does not certify their implementation.
