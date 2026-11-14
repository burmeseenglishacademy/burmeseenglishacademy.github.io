# CEFR-1000 independent review and release evidence contract (staging proposal)
Observed: 2026-11-14. Scope: exactly 1,000 entries, 200 each at A1/A2/B1/B2/C1. This is a proposed fail-closed contract, **not** evidence that any gate has passed.

## Source-of-truth and provenance
Provisional input: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, observed blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Independent-review queue: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`. Existing shortlist has 200 first-pass entries per level and zero independent approvals per level. All editorial holds stay true. The historical branch name is retained; the 5,000-word proposal is superseded.

## Required machine-verifiable evidence for EACH entry
- Stable entry ID, canonical headword, part of speech, **sense ID**, exact English definition, fluent Myanmar meaning, and independently edited grammatical example; provenance back to original source path/index/blob SHA
- CEFR decision for the **specific sense and part of speech**, not a generic word-level label; independent reviewer identity, review timestamp, source URL, source observation date, source quotation/brief claim, and whether source explicitly labels that sense with CEFR
- Separate independent reviewer attestations for English, Myanmar, example and CEFR; reviewer cannot equal the drafting agent or be derived from automated self-evaluation; each attestation binds to a SHA-256 digest of the exact reviewed content, so later edits invalidate approval
- A distinct documented pronunciation review, plus four audio files (George headword, Emma headword, George example, Emma example), each bound to text digest, voice, locale, synthesis settings and file hash
- **Human listening** signoff for every audio asset, with reviewer identity, date, asset hash, playback environment and issue disposition; file presence, waveform existence and synthetic listening simulations are insufficient

## Release manifest invariants (reject on unknown/missing fields)
1. Exactly 200 approved entries in each of five levels; 1,000 overall. No duplicate normalized headwords across levels unless the curriculum explicitly permits a documented distinct-sense exception; no duplicate (headword, part-of-speech, sense) tuple. Unicode NFKC and casefold are for collision detection only: preserve canonical display capitalization (especially `I`).
2. Every source must support the **exact sense and CEFR**; dictionary entries lacking a displayed level, generic grammar-level pages, and WordNet synsets alone do not qualify as explicit CEFR evidence. Named entities and historically held forms require explicit independent adjudication.
3. Every review attestation must be from an actual independent human and must match the current field digest. A boolean flag without reviewer evidence is never sufficient.
4. All 4,000 expected voice/text audio combinations must exist, be hash-verified and have individual real listening signoff. Regeneration invalidates old listening attestations.
5. Browser and mobile regression must be tied to the candidate commit; physical iPhone Safari testing requires device model, iOS/Safari version, tester, date, screenshots or reproducible test evidence and actual listening notes. Desktop emulation does not count.
6. GitHub Actions: five parallel level-specific structural jobs must each conclude success **for the candidate SHA**; inspect job conclusions and failure logs, not merely the workflow badge. A workflow run from an earlier commit does not qualify.
7. Hosting review must confirm GitHub Pages build/size/bandwidth constraints, media loading, caching and privacy posture for the candidate. Preserve 54 existing lessons, separate IELTS 1,000 bank and established George/Emma production audio using before/after asset manifests and hashes.
8. Deployment confirmation must prove production URL serves the candidate commit and assets after publish, with smoke-test evidence. Approval of a staging candidate is not itself a deployment.

## Negative tests required before release
Reject: 199/201 per level; case-only collision; duplicate sense; unknown CEFR source; word-level source substituted for exact-sense CEFR; missing Myanmar review; self-signed review; stale digest after edit; absent George/Emma example audio; changed audio hash after listening; fake iPhone evidence; five passing jobs from an old SHA; missing hosting evidence; altered production lesson or IELTS assets; production URL serving previous build.

## Current truth and blockers
| Level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

Audio for final shortlist: not generated/verified/listened. Semantic deduplication and independent exact-sense CEFR review: unresolved. Physical iPhone Safari: no verified evidence. Hosting and production deployment: not cleared. Previously reported five-job success: run `43520974102` for older SHA `dc2381728dbf765481296fdeb81c5f82a8569715`; **not** evidence for current staging head. No merge, publication, or approval is authorized by this document.
