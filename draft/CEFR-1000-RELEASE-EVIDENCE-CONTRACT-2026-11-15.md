# CEFR-1000 release evidence contract — 2026-11-15

Status: **STAGING ONLY / FAIL CLOSED**. This is a proposed machine-checkable acceptance contract, not a review, audio verification, browser test, or release authorization.

## Immutable scope and source
- Candidate source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551` observed 2026-11-15.
- Independent-review task source: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`; current read returned no content, so task inventory and its schema **were not verified**.
- Required counts: A1=200, A2=200, B1=200, B2=200, C1=200; all first-pass written, zero independently approved. The manifest itself reports all review flags false and `editorial_hold=true`.
- The source shortlist currently contains `a` and `an` as separate entries: reviewers must adjudicate whether they represent one lexeme before declaring 200 distinct lexical senses. A1 `i` also requires capitalization correction. Prior research flags C1 `signature` (handwritten name) as a B1 sense; do not silently relabel.

## Per-entry evidence record (required before approval)
Store an immutable entry ID based on the original source path, source index and source blob SHA; canonical spelling, part of speech, **precise sense**, CEFR level and reviewer-approved English definition, natural Myanmar explanation and original example. Record independently verified source URL, publisher, exact sense evidence, explicit CEFR evidence (not merely a general dictionary definition), UTC observation date and citation excerpt within copyright limits. Missing explicit level evidence must remain unresolved, never inferred from a dictionary's mere presence. Record reviewer identity, independent human signoff timestamp, each field's separate approval, and any conflicts with other levels or homographs. Self-authored research cannot populate reviewer signoff.

## Audio evidence (both voices, both assets)
For every approved entry require four linked artifacts: George/headword, George/example, Emma/headword, Emma/example (4,000 assets for 1,000 entries). Each must have actual file path, SHA-256, voice identity, British locale, generator/version, exact text hash, generation timestamp, and a separate human listening-verification record with listener identity, date, device and pass/fail. Missing files, mismatched text, silence, clipping, wrong voice, incorrect Burmese/English phonetics or unlistened assets block release. Do not confuse existing 54-lesson production audio with this new bank.

## CI acceptance
Run five **parallel** level-specific jobs on the exact release commit. Each job validates 200 canonical deduplicated headword/sense records, required fields, no editorial holds, source-backed exact-sense CEFR evidence, all independent reviewer attestations, four audio files per entry and actual listening attestations. A sixth integration job checks exactly 1,000 entries, cross-level duplicates and ambiguous same-headword senses, no protected production asset diffs, and independent browser/mobile/physical iPhone Safari signoff evidence. Save workflow run ID, commit SHA, job IDs, conclusions and relevant logs; a historical green run is not evidence for a later commit. Treat missing, skipped, cancelled, timed-out or stale checks as failure.

## Deployment and preservation
Before launch, verify GitHub Pages hosting size/bandwidth/build constraints against actual release artifacts; check privacy/no-tracking; preserve 54 lessons, separate IELTS 1,000-word bank and existing George/Emma audio using before/after file inventories and checksums. Require physical iPhone Safari evidence with device, iOS/Safari version, date, tested routes, playback and failures. Only after all gates pass may a separately recorded production deployment be confirmed by URL, production commit, deployment ID, live HTTP checks and protected-asset comparison. No automatic merge or publishing from this document.

## Current gate ledger
| Gate | Observed state |
|---|---|
| Written first-pass | 200 each A1/A2/B1/B2/C1; **unverified** |
| Independent review | 0/200 each; blocked |
| Lexeme/sense deduplication | unresolved a/an and other exact-sense conflicts |
| Audio generation and listening | no final-shortlist evidence; blocked |
| Browser/mobile/physical iPhone Safari | no release-specific evidence; blocked |
| Current-commit CI | not established by this document |
| Hosting and protected production assets | not cleared |
| Public deployment | **not performed** |

This document adds a release evidence specification only. It grants no approval and changes no manifest flags.
