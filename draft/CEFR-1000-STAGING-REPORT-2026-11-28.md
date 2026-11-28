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



## C1 political, institutional and legal sense evidence addition

On 2026-11-28, an author-side evidence note was added at `draft/CEFR-1000-EVIDENCE-2026-11-28-C1-POLITICAL-AND-LEGAL-SENSES.md` for seven existing C1 candidates (all still pending):
- `civilian` (CEFR1000-C1-0829): Cambridge labels the selected noun sense C2, conflicting with shortlist C1.
- `coalition` (CEFR1000-C1-0830): Cambridge supports the political-alliance sense but the inspected Cambridge entries show no CEFR label; Wordmom shows B2, treated only as a low-confidence warning.
- `controversial` (CEFR1000-C1-0831): Cambridge labels the exact adjective sense B2, conflicting with C1.
- `dominant` (CEFR1000-C1-0833): Cambridge labels the selected general adjective sense C1; specialised biological, anatomical, psychological and music senses are kept separate.
- `furthermore` (CEFR1000-C1-0834): Cambridge labels the formal connective B2, conflicting with C1.
- `treasury` (CEFR1000-C1-0822): government-department sense supported by Collins/Cambridge, but no authoritative CEFR label found in those entries; secondary B2 and inconsistent frequency-based B2/C1 signals are not sufficient for approval. The note flags generic lowercase `treasury` versus named institutional `the Treasury`, and distinguishes department, funds, storehouse and collection senses.
- `warrant` (CEFR1000-C1-0824): Cambridge confirms the legal-document noun sense; Oxford Advanced Learner's search metadata exposed a “Law and justice C1” topic tag, but direct opening returned HTTP 403. The tag needs human verification and must not be generalised to the verb or other noun senses.

The evidence note includes source URLs, observation date, source shortlist/task provenance, Myanmar refinements and original example proposals. It is author-side research only. No review-task source fields, reviewer identity, timestamps, reviewed flags, approval flags, shortlist entries or levels were changed. Evidence-note correction commit: `741057791c14b63d121ccd7c2cc2106e2c55c71c`.


## Release-gate audio integrity hardening

On 2026-11-28, `scripts/cefr-1000-release-readiness-gate.cjs` was strengthened before any final audio is generated:
- Every George/Emma headword audio record must carry `spoken_text` exactly matching the approved manifest headword; every example recording must match the approved example sentence.
- Audio files must use a declared `mp3`, `wav`, `ogg` or `flac` format whose extension matches and whose file header has the corresponding basic container/signature marker.
- SHA-256 content digests must be unique across all 4,000 voice/utterance slots, not merely within each task. File paths remain unique, confined to staging `draft/`, regular (not symlinked), nonempty and checksum-verified.
- Existing checks for exactly 1,000 records in each of four audio categories, one record per manifest task, British George/Emma identity, `en-GB`, generator provenance, listener identity/time and listening-evidence URL remain in force.

Added `scripts/cefr1000_release_gate_negative_tests.cjs` and a dedicated workflow job. The test uses a temporary synthetic fixture only (not repository release evidence or actual audio) and verifies: complete evidence-schema fixture passes schema validation only; wrong spoken text is rejected; duplicate audio bytes across different tasks are rejected; and invalid audio signature is rejected.

## Current verified staging CI

After updating the workflow actions to Node 24-compatible major versions (`actions/checkout@v7`, `actions/setup-python@v7`, `actions/setup-node@v7`; Node 22 remains the test runtime), the latest workflow run is [`46125363914`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46125363914), head commit `e900532a24f6e64ab85fbd745f3d69bf1496bafc`, completed `success` with **14/14 jobs successful**. Actual job conclusions and logs were fetched:
- Python structural integrity A1/A2/B1/B2/C1: successful.
- Node cross-level structural/task-ID A1/A2/B1/B2/C1: successful.
- Twenty-case provisional-data mutation tests: successful.
- Python release-denial check and Node approved-manifest release-denial check: successful.
- New adversarial audio-evidence tests, job `140918654114`: successful; logs show all four expected PASS assertions.
- No Node 20 deprecation or punycode warnings appeared in the current run logs.

This CI run validates structural and synthetic adversarial safeguards only. It does not generate or listen to actual George/Emma assets and does not supply independent review, browser/mobile QA, physical iPhone Safari evidence, hosting clearance or deployment.

The seven C1 candidates documented in the new evidence note remain author-side research only. The provisional shortlist and independent review task files were re-read after these changes: each level still has exactly 200 written entries, 200 unique headwords, 200 editorial holds, 200 pending tasks and zero independently approved entries. No linguistic review fields, evidence URLs, reviewer identities or approval flags were changed.


## A2 sense-boundary evidence addition

On 2026-11-28, ten A2 candidates were documented in `draft/CEFR-1000-EVIDENCE-2026-11-28-A2-SENSE-AND-LEVEL-BOUNDARIES.md`:
- `order` (CEFR1000-A2-0226): Cambridge A2 request-for-goods noun; exact-sense match.
- `service` (CEFR1000-A2-0227): Cambridge B1 customer-help/system senses; the current shuttle-service example is B1, conflicting with A2.
- `season` (CEFR1000-A2-0228): Cambridge B1 annual/weather-period noun; conflicts with A2.
- `area` (CEFR1000-A2-0229): A2 region sense is supported, but the current reserved-for-visitors example is the B1 designated-purpose sense.
- `business` (CEFR1000-A2-0230): current definition describes the A1 buying/selling activity, while the example describes the A2 company/organisation sense; refine definition to match the example.
- `however` (CEFR1000-A2-0231): Cambridge A2 contrast use is supported; keep separate from B2 degree use and other senses.
- `actually` (CEFR1000-A2-0233): Cambridge A2 truth use is supported; current definition risks blending the B1 surprise sense and B2 disagreement/refusal sense.
- `less` (CEFR1000-A2-0234): Cambridge A2 quantifier use is supported; the example correctly uses uncountable `sugar`.
- `party` (CEFR1000-A2-0235): Cambridge labels the selected social-event noun A1, conflicting with shortlist A2.
- `whole` (CEFR1000-A2-0236): Cambridge A2 adjective sense is supported.

The note includes source URLs, observation date, shortlist/task/source-blob provenance, Myanmar refinements and original example proposals. These are author-side findings only. All ten tasks remain pending; no shortlist or review fields were changed.

## Latest CI after A2 evidence addition

GitHub Actions run [`46125609306`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46125609306), head commit `908a4be7275dc5e1bcb25418a0141140b783177a`, completed with conclusion `success`: **14/14 jobs successful**. Actual job conclusions and logs were fetched. The five Python level-specific structural jobs, five Node cross-level/task-ID jobs, twenty-case provisional mutation tests, both release-denial checks, and the new adversarial audio evidence job all succeeded. The audio test log confirmed the four expected PASS cases. No Node 20 deprecation or punycode warnings appeared in the logs.

This confirms staging structure and synthetic gate tests only. It does not change the independent approval count or provide actual audio/listening, browser/mobile, physical iPhone, hosting or production-deployment evidence.


## Reconciled inventory snapshot and report-commit CI

A fresh parse of the staging JSON files on 2026-11-28 reconfirmed 1,000 total entries, 1,000 unique normalized headwords, 1,000 unique task IDs, and exact source/task positional provenance. The release statuses remain `PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH` and `ALL_PENDING_NOT_INDEPENDENTLY_REVIEWED_DO_NOT_PUBLISH`.

| CEFR | Written | Unique headwords | Independent signoffs | Pending independent tasks | Editorial holds |
|---|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 0 | 200 | 200 |
| A2 | 200 | 200 | 0 | 200 | 200 |
| B1 | 200 | 200 | 0 | 200 | 200 |
| B2 | 200 | 200 | 0 | 200 | 200 |
| C1 | 200 | 200 | 0 | 200 | 200 |
| **Total** | **1,000** | **1,000** | **0** | **1,000** | **1,000** |

The report commit `8e5aab2cae8fd8eb152bc6f8a57a51c4f74372ec` itself was checked by GitHub Actions run [`46125671974`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46125671974): completed `success`, **14/14 jobs successful**. Actual conclusions and logs were fetched. The adversarial audio test passed all four synthetic cases; all five CEFR Python jobs, all five Node jobs, the twenty-case mutation suite and both release-denial checks passed. No Node 20 deprecation or punycode warnings appeared. These remain structural/synthetic checks only, not independent review or launch authorization.


## Final report-commit CI confirmation

The report/count reconciliation commit `3d5dfec4cd6f6f7ab55a39496862845e493ee91b` was validated by GitHub Actions run [`46125747929`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46125747929). The run completed with conclusion `success`: **14/14 jobs successful**. All 14 job conclusions and logs were fetched. The five Python level-specific structural jobs, five Node level-specific cross-level/task-ID jobs, twenty-case provisional-data mutation suite, Python release-denial check, Node release-denial check and adversarial audio-evidence test all succeeded. Logs explicitly reported `independently_verified: 0` for each Node level job and `release: BLOCKED`. The audio test passed the synthetic wrong-text, duplicate-content and invalid-signature rejection cases. No Node 20 deprecation or punycode warnings appeared.

This is the latest verified CI run at the time of this report update; passing it confirms the staging safeguards, not independent vocabulary approval, real audio, listening, device QA, hosting clearance or production deployment.


## A1 lexical sense-boundary evidence addition — 2026-11-28

Added `draft/CEFR-1000-EVIDENCE-2026-11-28-A1-LEXICAL-SENSE-BOUNDARIES.md` in commit `275ae8fe13eb7ff8825a5347fd0195d87699b552`. It records source URLs, observation date, shortlist/task provenance, exact-sense CEFR distinctions, British pronunciation where relevant, Myanmar refinements and original example options for fourteen additional A1 tasks: `book` (0030), `place` (0063), `time` (0042), `people` (0043), `house` (0062), `help` (0059), `see` (0046), `want` (0048), `know` (0045), `go` (0049), `day` (0052), `work` (0053), `old` (0060) and `little` (0061). These are author-side source findings only; none is counted as an independent check.

The most material finding is `time`: the shortlist's current “What clocks measure in hours and minutes” definition corresponds to Cambridge's A2 duration sense, while “What time is it?” illustrates the A1 clock-time/particular-point sense. The note recommends that the independent reviewer choose one sense and align the level, definition, Myanmar gloss and example. It also flags the broad A1 `work` definition, the A1/B2 distinction for `help`, the mixed visual/meet Myanmar gloss for `see`, the broad `know` definition, the adjective/quantifier Myanmar ambiguity for `little`, and examples that could invite A2 readings for `day`.

A fresh parse of the two JSON files after this evidence commit produced:

| Level | Written | Unique normalized headwords | Editorial holds | Independently approved | Pending review tasks |
|---|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 200 | 0 | 200 |
| A2 | 200 | 200 | 200 | 0 | 200 |
| B1 | 200 | 200 | 200 | 0 | 200 |
| B2 | 200 | 200 | 200 | 0 | 200 |
| C1 | 200 | 200 | 200 | 0 | 200 |
| **Total** | **1000** | **1000** | **1000** | **0** | **1000** |

Structural reconciliation: all shortlist review flags and release approvals remain false: `true`; task IDs are globally unique: `true`; each review task remains positionally matched to its shortlist entry: `true`. No provisional content or review-task decision fields were changed by this evidence addition.

The new evidence commit's combined commit-status endpoint returned no status records, so no new CI result is claimed for `275ae8fe13eb7ff8825a5347fd0195d87699b552`. The previous verified structural run remains historical evidence only; current-commit workflow execution must be checked separately. This addition does not change the release blockers: independent English/Myanmar/example/CEFR signoff remains 0/1,000; final George/Emma audio remains 0/4,000 assets generated and actually listened to; vocabulary-specific desktop/mobile and physical iPhone Safari QA are not evidenced; GitHub Pages hosting clearance is outstanding; and production deployment is neither authorised by evidence nor performed.

## A2 and C1 exact-sense audit additions — 2026-11-28

Added two author-side source research notes on the staging branch:

- [A2 exact-sense audit](CEFR-1000-EVIDENCE-2026-11-28-A2-EXACT-SENSE-AUDIT.md), commit `a3d94cc18798fe35bab07a266a42107c2084169f`. Nine existing A2 tasks are covered: `world`, `life`, `through`, `while`, `part`, `team`, `someone`, `must`, and `company`. Cambridge evidence supports the selected A2 senses of `through`, the DURING conjunction use of `while`, `someone`, and the business-organisation sense of `company`. Material level/sense risks: `world` and `part` currently illustrate A1 senses; `team` conflates A2 sports and B1 work-group senses and its example is ambiguous; `life` does not identify a clearly A2 sense (the inspected Cambridge senses are A1/B1/B2); and `must` has grammar evidence but no inspected Cambridge CEFR label. Original example and Myanmar refinements are proposed without changing the provisional records.
- [C1 lexical level risk audit](CEFR-1000-EVIDENCE-2026-11-28-C1-LEXICAL-LEVEL-RISK-AUDIT.md), commit `8fdf7b3f563fe42a02ab63c45fb487eeccbb7874`. Ten existing C1 tasks are covered: `coalesce`, `conjecture`, `conscientious`, `culpability`, `disparage`, `disproportionate`, `dissonance`, `entrench`, `fortitude`, and `superfluous`. Cambridge explicitly labels `conscientious` C1 and displays C1 for `entrench` on its Traditional Chinese dictionary page (with the English page confirming the sense). Cambridge labels `superfluous` C2, a direct conflict with the shortlist's C1 placement. The other seven entries have useful meaning evidence on the inspected Cambridge pages, but no visible CEFR level there; they remain unsubstantiated at C1 rather than being promoted by author judgement.

Both notes preserve the current shortlist/task blob SHAs, original source-file provenance, task IDs, observation date, Cambridge source URLs, British pronunciation references where shown, Myanmar refinements and original example proposals. They are author-side findings only. No review-task evidence fields, shortlist entries, source levels, editorial holds, reviewer identities or approval flags were changed.

The inventory remains exactly 200 written entries per level (1,000 total), with 200 editorial holds and 0 independent signoffs at each level. The new documentation commits are staging-only. Current-commit CI conclusions/logs have not yet been verified for these commits; the latest historical verified run remains `46125747929` (14/14 jobs successful) and must not be represented as validation of these new commits.

Release blockers remain unchanged: independent English, Myanmar, original-example and source-backed CEFR signoff 0/1,000; final George/Emma headword/example audio 0/4,000 assets generated and actually listened to; desktop/mobile browser regression not evidenced; physical iPhone Safari review not evidenced; GitHub Pages hosting clearance outstanding; and confirmed production deployment absent. All production-protection requirements remain in force.
