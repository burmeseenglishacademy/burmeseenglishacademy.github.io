# CEFR-1000 staging report — 2026-11-28

**Status: STAGING ONLY — DO NOT PUBLISH.** This report covers the user-approved 1,000-entry CEFR A1–C1 project only. The superseded 5,000-word plan is out of scope.

## Inventory and review counts

The provisional shortlist and separate review-task file were parsed directly from branch `cefr-5000-bilingual-qa-staging` on 2026-11-28.

| CEFR level | First-pass entries written | Independent checks signed off | Review tasks |
|---|---:|---:|---:|
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |
| **Total** | **1,000** | **0** | **1,000** |

Structural observations:
- 1,000 shortlist entries and 1,000 review tasks.
- 1,000 unique case-folded NFC headwords in the shortlist.
- All 1,000 shortlist entries remain `editorial_hold: true`.
- All provisional `reviewed_english`, `reviewed_burmese`, `reviewed_example`, `reviewed_level`, `reviewed_pronunciation`, and `release_approved` flags remain explicitly false.
- All 1,000 review tasks remain pending, with approval false, no assigned reviewer, no reviewer identity/signature, no observed date, and no claimed source evidence URLs.

Source file blob SHAs observed:
- Provisional shortlist: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Independent review tasks: `77abf35146825f05e3e58cfdd7a73b3c7302c967`.

The author-side evidence notes currently cover nine A1 candidates and five C1 candidates:
- [A1 core nouns: water, food, family, friend](CEFR-1000-EVIDENCE-2026-11-28-A1-CORE-NOUNS.md).
- [A1 family and education: mother, father, school, teacher, student](CEFR-1000-EVIDENCE-2026-11-28-A1-FAMILY-AND-EDUCATION.md).
- [C1 exact-sense level challenges: naval, tribute, divine, municipal, neutral](CEFR-1000-EVIDENCE-2026-11-28-C1-LEVEL-CHALLENGES.md).

The A1 notes record Cambridge exact-sense A1 evidence, British pronunciation references, proposed English-definition refinements, Myanmar meaning/register notes, original example grammar and Burmese renderings. They distinguish A1 school-place from A2 school-period and common parent senses from separate title/formal-verb senses. The C1 note identifies two direct C2 conflicts (`naval`, `tribute`), one C1 assignment not established by the inspected CEFR-labelled source (`divine`), and two exact C1 matches (`municipal`, `neutral`). It also flags the `tribute` example for being too close to the Cambridge source example. These are author-side findings only; none count as independent checks or approvals.

## Release gates

| Gate | Evidence state |
|---|---|
| Independent English definition review | 0/1,000 signed off |
| Fluent Myanmar meaning review | 0/1,000 signed off |
| Original example grammar and translation review | 0/1,000 signed off |
| Exact-sense, source-backed CEFR review | 0/1,000 independently signed off |
| British George headword audio | 0/1,000 generated for final shortlist; 0 listened/signoff |
| British Emma headword audio | 0/1,000 generated for final shortlist; 0 listened/signoff |
| British George example audio | 0/1,000 generated for final shortlist; 0 listened/signoff |
| British Emma example audio | 0/1,000 generated for final shortlist; 0 listened/signoff |
| Desktop browser regression for this vocabulary release | Not evidenced |
| Mobile browser regression for this vocabulary release | Not evidenced |
| Physical iPhone Safari review for this vocabulary release | Not evidenced |
| GitHub Pages hosting/capacity limits for proposed release | Not assessed for this release |
| Confirmed production deployment | Not deployed / not confirmed |

The final audio requirement is 4,000 distinct voice/utterance assets (1,000 headwords and 1,000 examples for each of George and Emma), each with provenance and real listening signoff. Existing production audio is not a substitute for these new assets.

## CI evidence and workflow notes

Historical GitHub Actions run `45235724342` was inspected through its actual job list and failed-job log:
- Five level-specific structural jobs (A1, A2, B1, B2, C1): succeeded.
- Provisional intake/adversarial test job: succeeded.
- `Assert staging release remains denied`: failed (job `137906790608`).

The failed log shows the older job ran `set -uo pipefail` under GitHub's default `bash -e`, then invoked the release-veto script expected to exit nonzero. Bash exited immediately on that command before the following `status=$?` could capture the expected result. This was a test-harness failure, not evidence that release was permitted.

The current staging workflow file `.github/workflows/cefr-1000-structural-qa.yml` uses an explicit `set +e` / capture / `set -e` sequence and validates both the Python and Node JSON release-denial reports. It runs parallel Python and Node A1–C1 structural jobs, twenty mutation checks, canonical task-ID swap negative tests, and two release-denial checks.

**Verified current-workflow run:** GitHub Actions run [`46116573654`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46116573654), head commit `c6320dffe1c314160d9fc7c85b88190f68a204f5`, completed with overall conclusion `success`. The actual jobs endpoint returned **13/13 jobs successful**, and each reported step completed successfully:
- Python structural integrity: A1 `140891645971`, A2 `140891645914`, B1 `140891645944`, B2 `140891645919`, C1 `140891645881`.
- Node cross-level structural and task-ID negative tests: A1 `140891645877`, A2 `140891645879`, B1 `140891645789`, B2 `140891645991`, C1 `140891645842`.
- Twenty mutation checks: `140891645662`.
- Python release denial: `140891645808`.
- Node approved-manifest release denial: `140891645861`.

This is a successful structural/adversarial CI run and successful demonstration that the current provisional release remains blocked. It is **not** independent linguistic approval, audio/listening evidence, browser/mobile or physical iPhone QA, hosting clearance, or production deployment. Historical run `45235724342` had the earlier Bash errexit harness failure described above; the controlled-exit repair is exercised successfully by these later runs.

Two further push-triggered runs were also inspected after the A1 evidence and report updates:
- [Run `46122032860`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46122032860), evidence-file commit `3f0f7ade1b73e12f5f558c70657da21071f9f3e6`: overall `success`, **13/13 jobs successful**.
- [Run `46122072502`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46122072502), report commit `f9b8fbafa567b2a17cf75404d30437b0d7f276ea`: overall `success`, **13/13 jobs successful**.

Both job collections included all five Python level-specific checks, all five Node cross-level/task-ID checks, the twenty-case mutation suite, and both release-denial jobs. The run/job conclusions and step conclusions were fetched from the GitHub Actions API; no result was inferred from a commit alone.

After the C1 level-risk evidence was added, two more runs completed successfully:
- [Run `46122306545`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46122306545), evidence commit `7c83d5f6d10e6b541423ff6db0a253cfed6f9ab4`: `success`, 13/13 jobs successful.
- [Run `46122326512`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46122326512), report commit `3b6fce19a9bfd8ee1c164ffec34d5823c9762630`: `success`, 13/13 jobs successful.

Both included successful A1–C1 Python structural jobs, Node cross-level/task-ID tests, the mutation suite, and Python/Node release-denial checks. The release-denial checks succeeding means the project correctly remains blocked; it does not mean release approval.

## Production protection

No changes in this run were made to the 54 published lessons, the separate IELTS 1,000-word bank, established George/Emma production audio, or learner privacy controls. No merge to `main`, public deployment, or production modification is authorised before every required gate has genuine evidence.

**Release decision: remain on `cefr-5000-bilingual-qa-staging`. No independent approval is claimed.**


## Latest editorial evidence addition

On 2026-11-28, five A1 entries were documented in `draft/CEFR-1000-EVIDENCE-2026-11-28-A1-FAMILY-AND-EDUCATION.md`: `mother`, `father`, `school`, `teacher`, and `student`. Their review task IDs are CEFR1000-A1-0025 through CEFR1000-A1-0029. All five remain pending; no shortlist fields or review flags were changed. Evidence-file commit: `3f0f7ade1b73e12f5f558c70657da21071f9f3e6`.


## C1 level-risk evidence addition

On 2026-11-28, the C1 risk note documented five existing entries: `naval` (Cambridge C2, conflicting with shortlist C1), `tribute` (Cambridge C2, conflicting with shortlist C1, plus example originality concern), `divine` (exact sense supported but no CEFR level shown by the inspected Cambridge learner entry), `municipal` (C1 supported), and `neutral` (C1 supported for the no-opinion adjective sense). Tasks CEFR1000-C1-0801, -0812, -0813, -0814 and -0815 remain pending. Evidence-file commit: `7c83d5f6d10e6b541423ff6db0a253cfed6f9ab4`.
