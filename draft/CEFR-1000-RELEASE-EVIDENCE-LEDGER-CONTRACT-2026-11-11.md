# CEFR-1000 release evidence ledger contract — 2026-11-11

Status: **STAGING / NOT APPROVED / DO NOT DEPLOY**. Scope is **1,000 total**, exactly 200 each at A1, A2, B1, B2 and C1; never substitute the historical 5,000-word plan.

## Directly observed source state

Read on 2026-11-11 from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` at staging, Git blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Its metadata records 200 provisional written entries at each level, zero independently approved at each level, `FIRST_PASS_UNVERIFIED` English/Myanmar/examples, `NOT_OBSERVED` independent evidence, `NOT_GENERATED_FOR_FINAL_SHORTLIST_NOT_LISTENED` audio, and `UNMODIFIED` production. These are **metadata claims**, not an independent exhaustive inventory or language audit.

## Evidence record required per final sense (proposed schema; not a fabricated attestation)

- `entry_id`: immutable normalized headword + POS + sense identifier, not headword alone; `level`: exactly one of A1/A2/B1/B2/C1.
- `english_definition`, `myanmar_meaning`, `original_example`: final text and SHA-256 of canonical UTF-8 serialization. Reject blank or changed text after signoff.
- `publisher_evidence`: publisher name, exact accessible URL, publication/version when available, observation date UTC, exact headword/POS/sense evidence, explicitly stated CEFR level if publisher actually states one, and evidence excerpt or page/section locator. A generic dictionary homepage or word-only level is **not** sense-level proof. Unknown CEFR = BLOCK.
- `review_english`, `review_myanmar`, `review_example`, `review_cefr`: separate human-independent reviewer identity, timestamp, verdict, record-content hash and notes; no self-signoff; reject absent, stale, conflicting or revoked review.
- `audio`: for each of George and Emma, both headword and example, require file path, SHA-256, voice/model provenance, generation timestamp, exact spoken-text hash, audio format, duration and genuine listening attestation tied to that audio digest by an independent listener. File existence, synthesized metadata, waveform inspection or hash alone does not establish listening.
- `device_qa`: tested build SHA, browser/version, real physical iPhone model, iOS/Safari version, dated test session, tester and observable playback/interaction outcomes; simulator and desktop emulation are not substitutes.
- `hosting_qa`: GitHub Pages artifact inventory and size/transfer estimates, actual published URL, HTTP checks and build/deployment logs. Estimate is not proof of hosting clearance.

## Fail-closed release decision

1. Verify manifest is precisely 1,000 distinct **headword/POS/sense** identities, 200 per level; reject cross-level duplicate identities, ambiguous senses and unapproved substitutions. Additionally report repeated headwords with distinct senses for manual adjudication.
2. Every final entry must have four independent signed-off language/CEFR review dimensions, with valid source-backed exact-sense CEFR evidence and immutable matching content hashes.
3. Require all **4,000** expected audio artifacts (1,000 entries × 2 voices × headword/example), and **4,000** matching real listening attestations. A new audio digest invalidates its old listening signoff.
4. Require parallel A1–C1 structural and adversarial CI jobs on the **release candidate SHA**, not a historical commit. Fail if a job is absent, cancelled, skipped, timed out or not conclusively successful. Inspect actual job conclusions and failure logs.
5. Require browser/mobile regression and **physical iPhone Safari** evidence against the same release candidate, plus verified GitHub Pages limits and production protection comparison for 54 lessons, separate IELTS 1,000 bank, existing George/Emma production audio and privacy.
6. Only after all prior gates pass may authorized launch occur. Require production deploy success and post-deploy checks of actual live assets; absence of evidence must remain BLOCK, never auto-waive.

## Observed CI boundary

GitHub Actions run [42768895735](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42768895735) was retrieved on 2026-11-11: ten jobs returned `completed/success` (five provisional structural A1–C1 and five adversarial A1–C1). **This historical run does not verify current staging HEAD**. The run's job logs and current-HEAD CI were not examined here.

## Release blocker ledger (as observed)

| Level | First-pass written (shortlist metadata) | Independently approved (metadata) |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

No human-independent signoff, audio completion/listening, physical-device QA, hosting clearance or production deployment is established by this ledger. This document defines acceptance criteria only; it is **not** an approval record. Keep all changes on `cefr-5000-bilingual-qa-staging` and do not modify main.
