# BEA CEFR 5,000 — Batch44 staging editorial checkpoint
**26 October 2026 — first-pass drafts, observed source conflicts, no independent approval or publication.**

## Substantive editorial work
- **41 original bilingual first-pass drafts:** A2 0, B1 0, B2 25, C1 16. Definitions, natural Myanmar meaning drafts and original examples remain separate, unpublished fields.
- **41 independent review tasks**, pending English sense/POS, Burmese meaning, example, source-specific CEFR and actual George/Emma listening sign-off.
- **49 reversible candidate holds:** B2 23, C1 26; named entities, abbreviations, lower-tier common words and misleading WordNet senses.
- **8 AI-assisted Cambridge source-page observations**, separately stored, **not independent approvals**. Direct Cambridge pages display B2 for *presumably* and *alter*, C2 for *subtle*, *allegedly* and the area sense of *realm*. *Momentum* is C2 in its physics sense, while its figurative sense lacks an explicit graded label on the inspected page: **held for tier ambiguity**, not asserted C2 for the figurative sense. *Purely* and *nomination* display C1 for the intended senses and remain provisional drafts. These six disputed C1 drafts were **removed from written counts and quarantined**, rather than promoted on a guessed tier.

| Provisional level | Target | Unique first-pass written | Independently approved | Remaining unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 521 | 0 | 179 |
| B1 | 1000 | 747 | 0 | 253 |
| B2 | 1300 | 853 | 0 | 447 |
| C1 | 1500 | 534 | 0 | 966 |
| **TOTAL** | **5000** | **3155** | **0** | **1845** |

A2–C1 unique drafts 2655; 182 historical duplicate rows excluded; 922 reversible candidate holds. All figures are **structural ledger expectations until verified by actual CI**. Level quotas are a curriculum choice, not an authoritative CEFR word count.

## Separate stages and review blockers
1. English: 41 first-pass definitions; 8 AI-assisted Cambridge observations, **0 independently approved**.
2. Myanmar: 41 first-pass meanings, **0 independent Burmese reviewer approvals**.
3. Usage: 41 original contextual examples, **0 independent grammar/collocation approvals**.
4. Source/CEFR: 41 independent source-evidence tasks still pending; 8 preliminary page observations recorded separately with URL and date. No independent CEFR sign-offs.
5. George/Emma: **0 batch44 recordings generated or actually listened to**; physical iPhone Safari untested.
6. Production: protected 54 lessons, IELTS 1000, George/Emma and privacy assets must remain unchanged; public CEFR bank empty. **No merge or deployment**.

## CI evidence and status
- Initial draft commit `2787e534c5e7d5f0530d26a53c429ec8101c6b93`; [run 40235870863](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40235870863) **failed** in B2/C1/ALL because exact headword matching rejected inflected example words *affairs* and *intimates*. Actual job logs inspected; A2/B1 succeeded.
- Example correction commit `8fa72df3a886cd49f2c52ae17002409015d910c4`; subsequent run status must be observed separately. **Do not claim a CI pass before reading actual jobs and logs**.
- Current source-correction commit and five-job QA status: **pending observation**. Automated structural checks do not validate linguistic accuracy or audio.

## Release blockers
1845 unwritten, 922 held, **0/5000 independently approved**, complete George/Emma recordings and real listening, browser/mobile and real-device iPhone Safari, hosting limits and confirmed live deployment. Do not notify completion.

## Observed final Batch44 CI — 26 October 2026
- **Final source-corrected vocabulary/QA commit:** `e6d75bb74b80bfd622e7828d05ad9e272d8b8cb0` (parent `8fa72df3a886cd49f2c52ae17002409015d910c4`). This commit contains the 41 drafts, 49 new reversible holds, eight separate Cambridge source observations, audit, workflow and checkpoint.
- **Actual [GitHub Actions run 40236007013](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40236007013)** on that exact commit: **completed, all five matrix jobs succeeded**, and decoded logs were inspected. A2 job `121297614327`, B1 `121297614390`, B2 `121297614323`, C1 `121297614349`, ALL `121297614218`.
- ALL decoded log printed **A2 521 / B1 747 / B2 853 / C1 534** = **2,655 unique A2–C1 drafts**; with A1 **500**, **3,155 written / 1,845 unwritten**, **922 holds**, **182 historical duplicate rows excluded**, **0 independently approved**. ALL also printed `PASS: production lesson, IELTS, George/Emma audio and privacy assets unchanged` after comparing against `main`.
- Prior corrected-examples run [40235906551](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40235906551) succeeded, but its 47-draft ledger is **superseded** by the later source-conflict quarantines. The initial failed run [40235870863](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40235870863) remains documented; it is not misreported as a pass.
- These five successes are **structural staging-only tests**; no independent linguistic or CEFR approval, no listening, no real-device Safari, no hosting certification, no publication. The completion gate remains closed.
