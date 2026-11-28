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

The four additional A1 author-side evidence notes in [the 28 November core-noun evidence file](CEFR-1000-EVIDENCE-2026-11-28-A1-CORE-NOUNS.md) concern the exact A1 noun senses of `water`, `food`, `family`, and `friend`. Cambridge Learner’s Dictionary pages explicitly label those senses A1 and distinguish nearby A2/B1/B2 senses where shown. These notes do not count as independent checks or approvals.

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

The current staging workflow file `.github/workflows/cefr-1000-structural-qa.yml` uses an explicit `set +e` / capture / `set -e` sequence and validates the JSON release-denial report. It also runs parallel A1–C1 structural jobs, mutation tests, and Node cross-level structural/release-blocker checks. On 2026-11-28, commit `9ff5680262ba015bf92a544ad37fd752ab32a5cd` added `draft/CEFR-1000-*.md` to the push path filter and corrected the mutation-test step label from “sixteen” to “twenty,” matching the twenty corruption cases in the checked-in script. The workflow file was re-fetched after the update and both changes were confirmed. **A successful run of this current workflow has not yet been verified:** the combined commit-status endpoint returned no status records at the time of inspection, and the available GitHub Actions connector actions do not expose a list-runs operation for this push-triggered run. No success is inferred.

## Production protection

No changes in this run were made to the 54 published lessons, the separate IELTS 1,000-word bank, established George/Emma production audio, or learner privacy controls. No merge to `main`, public deployment, or production modification is authorised before every required gate has genuine evidence.

**Release decision: remain on `cefr-5000-bilingual-qa-staging`. No independent approval is claimed.**
