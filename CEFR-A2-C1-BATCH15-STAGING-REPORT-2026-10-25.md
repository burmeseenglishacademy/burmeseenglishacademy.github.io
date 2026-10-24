# BEA CEFR A2–C1 Batch15 staging checkpoint
Date: 25 October 2026 (SGT). Branch: `cefr-5000-bilingual-qa-staging`.

**STAGING ONLY — NOT RELEASE READY; DO NOT MERGE.**

## Substantive work
- Added **60 original bilingual first-pass drafts**, 15 each in A2, B1, B2, C1. Each has a new English definition, Burmese meaning, part of speech and contextual example; **all are unverified**.
- Created 60 separate source-evidence/independent-review tasks for English sense, Myanmar naturalness, grammar, CEFR level and both audio voices. Reference URLs are unvisited lookup leads, not verification.
- Quarantined 12 additional high-risk provisional candidates for proper-name/demonym, polysemy and CEFR-level review; none is counted as drafted or independently rejected.
- Added five-way staging-only structural GitHub Actions QA, with no deployment step.

## Exact unique first-pass draft inventory
| Level | Target | Unique drafts | Independently approved |
|---|---:|---:|---:|
| A1 | 500 | 500 | 0 |
| A2 | 700 | 298 | 0 |
| B1 | 1,000 | 296 | 0 |
| B2 | 1,300 | 298 | 0 |
| C1 | 1,500 | 276 | 0 |
| **Total** | **5,000** | **1,668** | **0** |

A2–C1 unique drafts **1,168** (previous 1,108 + 60). Older draft files include **182 identical duplicate rows**, deliberately excluded from counts. **3,332** unique drafts remain unwritten. CEFR levels are provisional and can change after review.

## CI and release blockers
Batch15 CI: **completed SUCCESS**, [run 40110043887](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40110043887), commit `aa4d7b3338a67ef99c0d8e0c3c485acefc3f9c5e`; all five jobs (A2, B1, B2, C1, ALL) completed successfully. The ALL job log explicitly confirmed A2=298, B1=296, B2=298, C1=276; 1,168 unique A2–C1 drafts, 182 legacy identical duplicates excluded, zero independent approvals. An earlier initial run [40109970940](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40109970940) FAILED because the newly cloned audit still expected 42 rather than 60 entries. The assertion was corrected in commit `493d3456bdaea9694b66d8978937411cac8fdf03`, and a final example wording improvement in commit `aa4d7b3338a67ef99c0d8e0c3c485acefc3f9c5e` triggered the successful final run. Five-way audit tests uniqueness, candidate alignment, quarantine separation, false approval flags, structural completeness, headword presence in examples and production isolation; none of these tests establishes linguistic accuracy.

No George/Emma audio generated for this batch, no listening approval, no real-device iPhone Safari test, no verified hosting capacity, and no production deployment. Existing 54 lessons, IELTS 1,000 bank, production George/Emma audio and privacy remain untouched. Production `main` was rechecked at `dca0db7aa30118ecc18350db8dc406e6cac91554` after the successful QA run. No production files or Firebase data were modified.
