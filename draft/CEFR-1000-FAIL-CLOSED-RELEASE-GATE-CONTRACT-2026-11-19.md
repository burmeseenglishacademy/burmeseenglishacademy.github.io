# CEFR-1000 release gate contract — staging-only engineering specification
Observed: 2026-11-19 (UTC). Scope: USER-APPROVED 1,000 total; A1/A2/B1/B2/C1 exactly 200 each. This document is a proposed fail-closed implementation contract, **not evidence that the tests ran** and not independent editorial signoff.

## Authoritative inputs and provenance
- `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (observed blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`).
- `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json` (observed blob SHA `77abf35146825f05e3e58cfdd7a73b3c7302c967`).
- Source of truth is a *future immutable release manifest*, not the provisional shortlist or an administrative review task. The source task's `approval:false` and `PENDING` are not signoffs.

## Structural gate: mandatory failure conditions
1. Manifest absent, malformed, version unknown, or release target not exactly `CEFR-1000`.
2. Any level missing, extra, or count other than 200; global count other than 1000.
3. Duplicate normalized headword + part-of-speech + exact-sense identifier within a level; cross-level same sense without documented, independently adjudicated resolution. Normalize Unicode NFC, whitespace and case for comparisons, but preserve the displayed orthography. Never collapse genuinely different senses solely by spelling.
4. Any missing immutable entry ID, sense definition, POS, Myanmar meaning, original example, Myanmar example translation, evidence URL, observation date, sense-specific CEFR claim, source provenance, or independent reviewer record.
5. Any reviewer is the draft author, reviewer identity missing, timestamp missing, source URL absent, reviewed content hash differs from release content hash, or one of English, Myanmar, example, exact-sense CEFR and pronunciation decisions is not independently signed PASS. A generic course wordlist or WordNet synset is not sufficient exact-sense CEFR evidence.
6. Any named-entity/noncanonical historical hold or cross-level conflict unresolved, or provisional `editorial_hold:true` treated as an approval.
7. Any audio slot missing: for each of 1000 entries require George and Emma British headword and George and Emma example files (minimum 4000 expected files), successful decode, duration/non-silence checks, content-hash linkage and **human listening signoff for each required slot**. A generated file, TTS invocation or automated acoustic check is not a listening signoff.
8. Browser/mobile regression missing, failing, or untraceable to the exact manifest commit; physical iPhone Safari evidence missing (device model, iOS/Safari versions, date, tested build SHA, tester, results and failures).
9. GitHub Pages constraints (static asset sizes, case-sensitive paths, content types, routing, storage/bandwidth, browser fetch and cache behavior) unverified against the deployable bundle.
10. Production deploy confirmation missing, live URL manifest/hash mismatch, or pre/post preservation checks of 54 lessons, separate IELTS 1000 bank, existing George/Emma production audio and privacy policy absent. **Deployment is the last gate**, never inferred from staging tests.

## Parallel CI proposal
Use one GitHub Actions matrix job for `[A1,A2,B1,B2,C1]`, with each job independently validating its 200 entries, source/reviewer/audio records and negative fixtures. A separate aggregation job must depend on all five jobs and independently verify 1000 total, cross-level sense collisions, immutable hashes, signed QA evidence, production-protection diff and the remaining release gates. Each job uploads machine-readable failure reasons; any absent, cancelled, skipped, timed-out or inconclusive job is FAIL, not PASS. Protect the production branch with required status checks. Never allow CI self-tests to mark human signoffs.

## Negative tests required
Reject 199/201 entries, duplicate sense, same-sense cross-level conflict, missing source date, bare WordNet CEFR claim, forged/unsigned review, draft-author self-approval, changed content after signature, missing George example audio, silence-only file, missing listening signoff, browser-only claim of physical iPhone testing, absent Pages evidence, and missing post-deploy asset-preservation hashes.

## Current verified administrative snapshot
| Level | Provisional written first-pass | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1000** | **0** |

The observed JSON declares these counts; they have not been independently recounted in this document. All 1000 remain editorial hold. Final-list audio is not generated/listened to according to the provisional manifest. CI conclusions/logs, physical iPhone QA, hosting signoff, and production deployment are **not verified**. Staging only; do not merge or publish.

## Implementation priority
Implement executable level-specific validator and negative fixtures on this staging branch; add matrix workflow and verify actual run IDs, job conclusions and logs; then add independent-review evidence intake with immutable content hashes. Do not conflate proposed gate coverage with completed QC.
