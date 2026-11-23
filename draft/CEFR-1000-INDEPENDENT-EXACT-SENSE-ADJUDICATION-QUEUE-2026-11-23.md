# CEFR-1000 independent adjudication: exact-sense conflict decision queue
Observed: 2026-11-23 (Asia/Singapore). Status: AUTHOR-SIDE TRIAGE ONLY — NOT INDEPENDENT REVIEW.

## Scope and provenance
Approved scope is **1,000 total** (A1/A2/B1/B2/C1: 200 each), not the retired 5,000-word scope. The provisional shortlist is `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`). The separate review-task file is `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json` (Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`). All 1,000 entries are first-pass written, on editorial hold, with **zero** independent approvals; the existence of a review task is not a review.

## Priority exact-sense disputes

| Provisional placement | Sense under dispute | Source and observed evidence | Independent reviewer action |
| --- | --- | --- | --- |
| C1 **signature** (noun) | A person's handwritten name, not an identifying characteristic or musical key | Cambridge Learner's Dictionary: https://dictionary.cambridge.org/dictionary/learner-english/signature ; Cambridge English: https://dictionary.cambridge.org/dictionary/english/signature . Earlier staging audit recorded B1 for this same handwritten-name sense. | Re-open source at review time, capture exact sense and explicit level; verify POS, Myanmar rendering for a handwritten signature, and example. If B1 confirmed, reject C1 placement and find a *separately sourced* C1 replacement before any 200-per-level manifest is approved. |
| C1 **upgrade** (verb) | Improve or replace software/equipment, not a higher travel class or noun | Cambridge Learner's Dictionary: https://dictionary.cambridge.org/dictionary/learner-english/upgrade ; Cambridge English: https://dictionary.cambridge.org/dictionary/english/upgrade . Earlier staging audit recorded B2 for this equipment/software verb sense. | Verify verb sense and CEFR label in a fresh visit; disambiguate improve vs replace, check Myanmar and original example, and separately assess British verb stress. Do not retain C1 merely to satisfy quotas. |
| A1 **an** (article) | Indefinite article before a vowel **sound**, not merely a vowel letter | Cambridge Grammar Today: https://dictionary.cambridge.org/grammar/british-grammar/a-and-the . Grammar usage evidence alone does **not** establish A1. | Obtain independent explicitly CEFR-tagged A1 evidence for the same article sense; check `an hour` vs `a university` and singular countability. |

These URLs and level observations are **research leads from prior staging audits**, not fresh independent verification or evidence that the sites were re-opened during this entry. Observation date above is the date this queue was compiled; historical audit observation dates and source-specific provenance must remain attached to each adjudicated record.

## Fail-closed reviewer decision record (one record per headword + POS + exact sense)
A reviewer must record: immutable task ID; shortlist Git blob SHA and source index; original definition, Myanmar meaning and example; explicit exact-sense boundary and POS; evidence URL and the **actual date inspected**; source's explicit CEFR label (or an explicit 'not provided'); proposed CEFR; edited English and fluent Myanmar; original example with grammar and semantic-fit judgment; pronunciation assessment; reviewer identity and signed timestamp; decision (approve/reject/rework) and reason. Separate reviewer identities and authenticated evidence are required for English, Myanmar, example and exact-sense CEFR checks. A self-authored proposal cannot set review flags.

## Inventory replacement policy
A confirmed cross-level mismatch is a **blocking defect**, not permission to silently relabel or reuse a headword. A replacement must have documented source-backed exact-sense CEFR evidence, avoid duplicate headword/POS/sense across all five levels, receive genuine independent signoff and preserve exactly 200 approved entries in *each* level. Keep original audit trail, rejection and replacement provenance. If any check fails, the approved manifest must not be generated.

## Release gates still unverified
No independent approvals; no complete British George/Emma headword + example audio or actual listening signoff; no browser/mobile regression and physical iPhone Safari evidence; no verified GitHub Pages size/hosting clearance; no production-asset preservation or live-deployment verification. Preserve the 54 lessons, separate IELTS 1,000-word bank, established production audio and privacy controls. **Do not merge, deploy or publish from this queue.**
