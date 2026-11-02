# CEFR 1,000 — five B2 publisher-indexed exact-sense research cards (3 November 2026)

**RELEASE BLOCKED — STAGING ONLY.** Scope: 1,000 TOTAL, A1/A2/B1/B2/C1 exactly 200 provisional written entries each; **0 independently approved at every level**. Do not merge, publish, alter `main`, change the 54 lessons or separate IELTS 1,000-word bank, or touch established George/Emma production audio or privacy settings.

## Research provenance and observations

The five frozen records are from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, and historical `draft/A2-C1-EDITORIAL-STARTER.json`, blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`. Original indexes: **respond 236, conduct 250, consistent 452, establish 625, occur 906**. Observed **2026-11-03** from Cambridge publisher-owned search-index snippets; direct Cambridge page opens failed HTTP 403. Publisher-index results are **research leads only**, not independent linguistic signoffs.

| Frozen B2 entry | Cambridge indexed sense/level | Finding and outstanding editorial issue |
|---|---|---|
| [respond](https://dictionary.cambridge.org/dictionary/learner-english/respond) | ANSWER/REACT — **B2** | Intransitive, normally *respond to* a request. Frozen example is grammatical. Distinguish response to medical treatment. |
| [conduct](https://dictionary.cambridge.org/dictionary/english/conduct) | ORGANIZE/PERFORM — **B2** | Transitive verb; original safety-inspection example is grammatical. UK verb /kənˈdʌkt/ vs noun /ˈkɒndʌkt/ requires George/Emma pronunciation review. |
| [consistent](https://dictionary.cambridge.org/us/dictionary/english/consistent) | NOT CHANGING — **C2** | **Higher-level same-sense conflict** with provisional B2. Frozen results-over-time definition/example correspond to the Cambridge indexed sense. Independent exact-sense decision required; do not silently relabel. |
| [establish](https://dictionary.cambridge.org/us/dictionary/english/establish) | START ORGANIZATION — **B2** | The frozen definition also says *system*, beyond the narrowly indexed organization/company sense. A relationship sense is separately indexed **C1**. |
| [occur](https://dictionary.cambridge.org/dictionary/english/occur) | HAPPEN — **B2** | Intransitive; frozen power-cut example grammatical. *Occurred/occurring* double **r**; *occur to somebody* and EXIST are distinct senses. |

Source URLs, observation date, historical source hashes, frozen English/Myanmar/examples, UK pronunciation leads and unapproved alternatives are recorded in [the five-card packet](draft/CEFR-1000-B2-FIVE-RESPOND-CONDUCT-CONSISTENT-ESTABLISH-OCCUR-CAMBRIDGE-2026-11-03.json). The alternatives are **not independent review**. Fluent Myanmar meaning and English example/CEFR exact-sense still require external independent human verification.

## Staging QA safeguard

Added [fail-closed five-card auditor](tools/audit_cefr_1000_b2_five_respond_consistent.py), pinned to frozen packet, shortlist and historical Git blob SHAs. It checks five 200-entry quotas, 1,000 globally unique written headwords, historical original records, indexed publisher URL/date/sense and source-access caveats, zero independent approvals and all editorial holds. It rejects 80 programmed synthetic tamper cases (15 per card × 5 plus five level approvals) for forged review flags, source claims, CEFR labels, publisher URLs and Myanmar text. **This is a programmatic test design, not proof of an actual passing CI run.**

Integrated the auditor into all six parallel CEFR structural lanes (A1/A2/B1/B2/C1/ALL) and the documentary NO DEPLOY gate. Relevant staging commits: packet `e2f6092c9d5b4f403f887f2d3f09f597d73131e6`, auditor `3daa81bb5a555a75e67b316f05b3f9f05baecd51`, delimiter fix `92a1d0fdf315c4bef06ccfb69e530daaf0449907`, structural workflow `101b77e2aa24070cff29e95d4f269395d1504414`, documentary workflow `7848ad99dedf58a80eac663b0bc211dbb85c6fe0`. **New push-triggered run IDs, job conclusions and decoded logs not retrievable via available GitHub connector; do not claim the new auditor CI-passed.** Previous structural run [41535606132](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41535606132) and documentary run [41535606131](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41535606131) predate this five-card audit.

## Release gate status

| Level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

No approved 1,000-word release manifest; no independent English/Myanmar/example/CEFR signoff; no complete George/Emma headword+example audio or **real listening** evidence; no completed browser/mobile regression or **physical iPhone Safari** QA; no measured GitHub Pages hosting clearance; no verified production deployment. **Staging only.**
