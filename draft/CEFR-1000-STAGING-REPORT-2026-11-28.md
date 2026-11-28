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

The author-side evidence notes cover selected A1–C1 candidates and are research aids, not independent review records. They preserve source URLs, observation dates, exact-sense distinctions, original shortlist/task provenance, British pronunciation references, proposed Myanmar refinements and newly drafted examples. Coverage is partial; the presence of a note never changes a task's pending status or approval count. The notes include A1 articles, family/education, core nouns, lexical sense boundaries, daily-life/actions and core verbs/adjectives; A2 sense/level audits; B1 exact-sense/level audits; C1 level challenges, political/legal senses, lexical-level risks and C2/A2 conflicts; and a source-provenance gap audit.

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

## Source-provenance and historical-risk audit — 2026-11-28

Added [source-provenance gap and historical-risk audit](CEFR-1000-EVIDENCE-2026-11-28-SOURCE-PROVENANCE-GAP-AUDIT.md), commit `4f580ae814a5db6fdb5ede5429204a0d4b47be94`. It follows all 1,000 shortlist records back to their seven original source JSON files using `source_path` and `source_index`.

Key findings:
- The 200 A1 records all point to the same general Oxford 3000/5000 information URL in `source_level_reference`; it is not a per-entry CEFR label or exact-sense evidence record.
- The other 800 A2–C1 source records have empty `source_level`, `source_english` and `source_burmese` fields. Their proposed/source level values are not evidence.
- All 1,000 independent review tasks still have empty `source_evidence_urls`, null `source_observed_on`, no reviewer/signature and pending review states. Thus source-backed exact-sense CEFR signoff is 0/1,000.
- The original source-status distribution is 200 draft-pending, 704 AI-assisted-draft-pending, 74 source-recovery-first-pass-pending, 7 requiring independent evidence, 14 awaiting cross-corpus triage, and 1 reversible level quarantine.
- The quarantined entry is `alacrity`, task `CEFR1000-C1-1000`. Its original batch59 reason is `C1_VS_C2_UNSUPPORTED_REQUIRES_GRADED_SENSE_SOURCE`. Oxford Advanced Learner's Dictionary displays A2 for the noun: https://www.oxfordlearnersdictionaries.com/us/definition/english/alacrity . Cambridge confirms the “speed and eagerness” sense but shows no CEFR label on the inspected page: https://dictionary.cambridge.org/dictionary/english/alacrity . The original quarantine reason is retained in batch59 but not copied into the shortlist/task record; the new note identifies this traceability gap. No level or hold was changed.
- No WordNet marker or WordNet source path was found in the seven inspected source files. A surface-form scan found no spaces, digits, uppercase, non-ASCII/punctuation or proper-noun POS among the 1,000 selected headwords. These checks do not prove historical WordNet provenance is clear or rule out common-word/proper-name homographs; independent semantic review remains required.

## Explicit CEFR-source release-gate strengthening — 2026-11-28

Updated `scripts/cefr-1000-release-readiness-gate.cjs` in commit `1f0cd84cb1cde3962310cf4e22dec24f91112617` and its synthetic adversarial tests in commit `b62eb65b92d38dbc10302155d45dd1e44d764120`.

Each future approved-manifest entry must now carry a separate CEFR evidence level, CEFR source URL, excerpt reference, excerpt text that identifies both the exact headword and claimed level, and CEFR-source observation date. The gate checks that the cited CEFR level exactly matches the manifest level, the source URL is HTTPS, the excerpt names the headword and level, and the observation date parses. A generic word-list landing page alone cannot satisfy this schema. The synthetic test suite now includes negative cases for a mismatched CEFR label and a generic list reference without an exact headword/level excerpt, in addition to the existing audio transcript, duplicate-content and file-signature checks. These are test fixtures only; they create no real review or audio evidence.

Current-commit CI remains unverified: the combined commit-status endpoint returned no status records for the new gate/test commits, and the available commit-workflow lookup returned no push-run records. No new run ID or successful job conclusion is claimed. The latest historical verified run remains `46125747929` (14/14 jobs successful), which predates these changes.

## Reconciled status after this run

| Level | Written | Unique headwords | Editorial hold | Independent signoffs | Pending tasks |
|---|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 200 | 0 | 200 |
| A2 | 200 | 200 | 200 | 0 | 200 |
| B1 | 200 | 200 | 200 | 0 | 200 |
| B2 | 200 | 200 | 200 | 0 | 200 |
| C1 | 200 | 200 | 200 | 0 | 200 |
| **Total** | **1,000** | **1,000** | **1,000** | **0** | **1,000** |

Release blockers remain unchanged: independent English, Myanmar, original-example and exact-sense CEFR signoff 0/1,000; final George/Emma headword/example audio 0/4,000 generated and actually listened to; desktop/mobile regression not evidenced; physical iPhone Safari review not evidenced; GitHub Pages hosting clearance outstanding; production deployment absent. All production protection and privacy requirements remain in force.


## B1 exact-sense and bilingual audit — 2026-11-28

Added [B1 lexical-sense and level-boundary audit](CEFR-1000-EVIDENCE-2026-11-28-B1-LEVEL-AND-SENSE-AUDIT.md), commit `6ca9576b96612dd792580e935830f88c98b59a56`. It covers fifteen existing B1 tasks, with original shortlist/task provenance, Cambridge source URLs, observation date, exact-sense findings, Myanmar refinements and original example proposals. These are author-side findings only; no shortlist/task content or review/approval fields were changed.

Material findings:
- Exact B1 sense support was found for `direction` (WAY noun), `wonder` (QUESTION verb), `effort` (ENERGY noun), `imagine` (CREATE verb), `organization` (GROUP noun), `protect` (verb) and `secret` (noun).
- `independent` currently uses B2 not-controlled/not-influenced senses; Cambridge's self-reliance sense is B1. A B1 rewrite is proposed, not applied.
- `weekend` is A1, not B1.
- `cash` is A2 for notes/coins; B1 is the broader money-in-any-form sense. Current definition/example point to A2.
- `clearly` is A2 for manner of speaking/understanding; B1 is the certainty/stance adverb. Current definition/example point to A2.
- `impact` is B2 for the selected effect noun sense.
- `civil` has no CEFR label in the inspected Cambridge Learner extract and a C1 signal for the matching ordinary/not-military sense in Cambridge's general English Dictionary.
- `multiple` has no explicit CEFR label in the inspected Learner extract for the selected adjective sense.
- `operation` has a B1 label for the medical noun sense, but not for the selected warehouse activity/operation sense; the level must not be transferred between senses.
- The note flags British `organisation` spelling as an editorial policy question without changing the canonical headword.

Cambridge search-indexed extracts were captured on 2026-11-28. Direct page-opening attempts returned HTTP 403 in this research session, so human reviewers must independently open and verify the live pages before signoff. All fifteen tasks remain pending; none count as independent checks.

## Latest inspected structural CI evidence

Inspected GitHub Actions run [`46125808173`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46125808173) through its actual job list and job logs. All **14/14 jobs** and their reported steps completed successfully. The checkout log for B1 structural job `140920026191` records head commit `0334d2fa046261bd25d445647c72f39c50db0706`; the B1 gate output was `errors: []` and `independent_approval_inferred: false`. Release-blocker job `140920026222` logged “Verified controlled, explicit release denial; no independent approval inferred.” This run is historical relative to the later source-provenance report commit `d9e42704a2ebb5a45f6bbc82e2cb7a7f3e983f75` and this B1 evidence commit; it does not validate those later commits. No current-tip CI success is claimed.

## Reconciled staging inventory

The shortlist and task JSON were reparsed from `cefr-5000-bilingual-qa-staging` during this run. Each level still has exactly 200 written entries, 200 editorial holds, 200 pending review tasks and 0 independently approved entries; the total remains 1,000 written / 0 independently approved. All shortlist review/approval flags remain false and task reviewer/signature/source-evidence fields remain empty or null.

Release blockers remain unchanged: independent English, Myanmar, original-example and source-backed CEFR signoff 0/1,000; final George/Emma headword/example audio 0/4,000 generated and actually listened to; vocabulary-specific desktop/mobile regression not evidenced; physical iPhone Safari review not evidenced; GitHub Pages hosting clearance outstanding; and confirmed production deployment absent. The 54 lessons, separate IELTS bank, established production audio, privacy controls and `main` remain untouched. Remain staging-only.


## CI failure diagnosis and adversarial-fixture repair — 2026-11-28

The push run [46135033907](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46135033907) on head `a226519d117ac0c06ef35c415e7d23200a40ebf3` completed with conclusion `failure`. The actual jobs endpoint showed the adversarial release-audio job failed; the other completed CEFR structural and release-denial jobs reported success. The failed job log pinpointed the test-fixture defect: the negative test changed `manifest.entries[0].source_cefr_level` and the CEFR excerpt only in memory, then rewrote the independent-evidence JSON, but the gate reads the approved-manifest JSON from disk. Consequently the supposedly corrupted manifest never reached the gate and the negative test failed with assertion “A CEFR label that differs from the approved level must be rejected” (actual exit 0).

The gate itself was not shown to accept a persisted mismatched level; the test failed to persist its mutation. The repair in this commit introduces a `writeManifest()` helper and writes the mutated and restored manifest fixture before each relevant adversarial gate invocation. This ensures the wrong-level and generic-excerpt cases exercise the actual on-disk manifest read by the gate. The fixtures remain synthetic and create no genuine review, audio, listener or deployment evidence.

## C1 five-entry source challenge — 2026-11-28

Added `draft/CEFR-1000-EVIDENCE-2026-11-28-C1-C2-CONFLICTS-AND-ALACRITY.md` in the same staging commit. It documents `affable` (Oxford topic C2), `ameliorate` (Oxford topic C2), `acquiescence` (Oxford topic C2), `acrimonious` (Oxford topic C2), and `alacrity` (Oxford OALD Oxford 3000 A2 label), with Cambridge exact-sense definitions, British IPA references, source URLs, observation date, original shortlist/task/source-batch provenance, Myanmar refinements and new example proposals. All five are author-side findings only; no shortlist or review-task decision fields were changed.


## Adversarial fixture repair — verified CI — 2026-11-28

The test-fixture repair and new C1 evidence note were committed on staging as `c85d6080889107d55b4f1e6040d47745b177b5fc`. The branch-only push triggered [GitHub Actions run 46138047343](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46138047343), which was fetched after completion: overall conclusion `success`, **14/14 jobs successful**, head SHA exactly matching the repair commit.

Actual job conclusions were fetched. The five Python level-specific structural jobs succeeded (A1 `140957644658`, A2 `140957644535`, B1 `140957644553`, B2 `140957644568`, C1 `140957644562`). The five Node cross-level/task-ID jobs succeeded (A1 `140957644628`, A2 `140957644585`, B1 `140957644678`, B2 `140957644671`, C1 `140957644641`). The twenty-case Python mutation job `140957644642`, Python release-denial job `140957644608`, Node release-denial job `140957644561`, and adversarial release/audio evidence job `140957644351` also succeeded.

The adversarial log explicitly passed all six cases: a complete synthetic schema fixture; mismatched CEFR level rejection; generic CEFR-list excerpt rejection; wrong audio transcript rejection; duplicate audio-content rejection; and invalid audio signature rejection. The Python release-denial log confirmed “controlled, explicit release denial; no independent approval inferred”; the Node release-denial log confirmed the release state remains `BLOCKED`. These are synthetic schema/negative tests, not real independent review, generated/listened audio, device testing or deployment evidence.

The preceding failed run `46135033907` is retained as a transparent regression record. Its actual failed log identified the test fixture not persisting its in-memory manifest mutation; the corrected fixture now writes the changed manifest to disk before invoking the gate. No production release gate was weakened.

## C1 C2/A2 lexical-level challenge — 2026-11-28

The new author-side note `draft/CEFR-1000-EVIDENCE-2026-11-28-C1-C2-CONFLICTS-AND-ALACRITY.md` records four Oxford topic-list C2 conflicts among C1 candidates (`affable`, `ameliorate`, `acquiescence`, `acrimonious`) and the Oxford OALD Oxford 3000 A2 label for `alacrity`, which is already historically quarantined. Cambridge exact-sense definitions and British pronunciation references, Oxford CEFR evidence URLs, task IDs, source-batch provenance, observation date, Myanmar refinements and original example proposals are retained. These findings are author-side only and do not count as independent checks.


## Report-commit CI confirmation — 2026-11-28

The staging-report update commit `d30cd247b2e5a29b3080c8ba19d4f9ab451e4478` was itself checked by GitHub Actions run [46138175714](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46138175714): overall conclusion `success`, **14/14 jobs successful**, exact head SHA match.

Actual job conclusions and selected logs were fetched:
- Python A1–C1 structural jobs: A1 `140958044599`, A2 `140958044585`, B1 `140958044565`, B2 `140958044543`, C1 `140958044686` — all success.
- Node A1–C1 cross-level/task-ID jobs: A1 `140958044340`, A2 `140958044614`, B1 `140958044573`, B2 `140958044516`, C1 `140958044643` — all success.
- Mutation suite `140958044617`, Python release denial `140958044618`, Node release denial `140958044646`, and adversarial release/audio suite `140958044595` — all success.

The adversarial log again passed the persisted wrong-level, generic CEFR excerpt, wrong transcript, duplicate audio bytes and invalid audio-signature rejection cases. Both release-denial logs explicitly confirm no independent approval is inferred and the provisional release remains blocked. This validates the report and staging safeguards only; it does not constitute linguistic signoff or real audio/device/hosting/deployment evidence.


## A1 everyday vocabulary exact-sense audit — 2026-11-28

Added [A1 daily-life and actions evidence note](CEFR-1000-EVIDENCE-2026-11-28-A1-DAILY-LIFE-AND-ACTIONS.md) in staging commit `3d9266051c4a443ab10ffc22cf4301c3a722eace`. It covers seven existing A1 tasks: `book` (CEFR1000-A1-0030), `chair` (-0095), `house` (-0062), `eat` (-0074), `drink` (-0075), `happy` (-0076) and `small` (-0072).

Cambridge dictionary search-indexed extracts observed on 2026-11-28 show A1 labels for the selected exact noun/verb/adjective senses. The note retains each dictionary URL, UK pronunciation, shortlist definition and Myanmar gloss, original source path/index/blob, task ID, a proposed refined English definition, Burmese meaning, newly written example and Burmese rendering. Important sense boundaries are retained: `drink` liquid A1 vs alcohol A2; `happy` pleased A1 vs willingness/satisfaction A2; `small` physical size A1 vs unimportance A2; and separate meeting/verb senses of `chair` and collective/verb senses of `house`.

Direct dictionary page-opening attempts returned HTTP 403 in this session; the indexed extracts are evidence leads only. Human reviewers must independently open the live pages and sign off. The examples and Myanmar renderings are author-side drafts, not independent originality or native-fluency review. No shortlist or task fields, review flags, editorial holds or approvals were changed; all seven tasks remain pending.


## CI status for the latest A1 evidence update — 2026-11-28

The A1 evidence note was created on staging in commit `3d9266051c4a443ab10ffc22cf4301c3a722eace`; the report update is commit `1c84f4643dc392d9db5d2cc931a97f3856418354`. At the time of this check, GitHub's combined commit-status endpoint returned no status records for the report commit, and the available commit-to-workflow lookup returned no runs (that connector lookup is limited to pull-request-triggered runs). Therefore no current-tip CI run ID, job conclusion or log is claimed for these latest changes. The last fully inspected successful run remains `46138263135` on report commit `8929276f3014f52b3a6bcee326f66fcc291dec04`, with 14/14 jobs successful. Its success predates the A1 evidence/report additions and must not be treated as validation of them. The staging workflow is configured to run on pushes changing these CEFR-1000 Markdown files; its result for the new commits remains to be fetched.


## A1 core verbs and adjective audit — 2026-11-28

Added [A1 core verbs and adjective evidence note](CEFR-1000-EVIDENCE-2026-11-28-A1-CORE-VERBS-AND-ADJECTIVES.md) in staging commit `c17f24a974a7b9d1762f2fc7bea8ca8e6ba5e709`. It covers eight original A1 tasks: `need` (CEFR1000-A1-0050), `come` (-0058), `use` (-0057), `make` (-0066), `look` (-0067), `take` (-0068), `give` (-0064), and `old` (-0060). Cambridge Learner's / Essential British dictionary extracts observed 2026-11-28 provide A1 exact-sense signals for the selected senses. UK IPA, source URLs, source batch/blob SHA, shortlist/task provenance, English-definition refinements, Myanmar register/sense notes, original example grammar and fresh example options are recorded.

Most consequential finding: the shortlist's A1 `give` definition (“hand something to someone”) and example (“Please give me the book.”) most directly select Cambridge's A2 hand-transfer sense. The A1 source sense is “provide someone with something”; the note proposes an A1-aligned definition/example and explicitly leaves the level/example decision to an independent reviewer. `take` also needs a more explicit carry-with-you example; `old` needs separate Myanmar wording for human age versus old/used objects; `use` must retain the verb pronunciation /juːz/ rather than noun /juːs/. The other entries retain A1 senses while documenting A2/B1 neighbouring senses and grammar constraints. All eight remain author-side only; no shortlist/task field, review flag, hold or approval was changed.

## Latest inspected Actions run before the new A1 audit — 2026-11-28

Branch head before the new evidence note was `507c4f2d9c341c38700ab5fe108d4d7488255baf`. GitHub Actions run [`46144929728`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46144929728) completed with overall conclusion **success**, and the jobs endpoint returned **14/14 successful jobs**. Actual job conclusions and logs were fetched:
- Python structural integrity A1–C1: A1 `140978756579`, A2 `140978756552`, B1 `140978756581`, B2 `140978756561`, C1 `140978756584` — all success, each reported `errors: []` and `independent_approval_inferred: false`.
- Node cross-level/task-ID structural A1–C1: A1 `140978756569`, A2 `140978756630`, B1 `140978756583`, B2 `140978756615`, C1 `140978756577` — all success.
- Twenty mutation checks: `140978756682` — success; log confirmed all twenty corruptions rejected.
- Python release denial: `140978756575` — success; log confirmed controlled explicit denial and no inferred independent approval.
- Node approved-manifest release denial: `140978756531` — success; log confirmed the release remains BLOCKED.
- Adversarial audio/evidence checks: `140978756336` — success; all six synthetic checks passed (mismatched CEFR level, generic CEFR excerpt, wrong transcript, duplicate audio bytes, invalid format/signature, and a complete synthetic schema fixture). The log explicitly says no real review or audio evidence was created.

Run `46144929728` validates commit `507c4f2d9c341c38700ab5fe108d4d7488255baf`, not the later evidence-note commit `c17f24a974a7b9d1762f2fc7bea8ca8e6ba5e709` or this report update. The new documentation changes should trigger another push run; current-tip success must be checked separately. Earlier failed adversarial fixture runs remain documented above, along with the repair and successful later regression runs.

## Reconciled inventory after the new A1 audit — 2026-11-28

The actual shortlist and independent-task JSON were reparsed before adding the new evidence note. Results remain A1 200 written / 200 unique / 0 independently approved; A2 200 / 200 / 0; B1 200 / 200 / 0; B2 200 / 200 / 0; C1 200 / 200 / 0. All 1,000 entries remain on editorial hold, all 1,000 independent tasks remain pending, and no reviewer signatures or source-evidence URLs were manufactured. The note does not modify any source JSON.

Release blockers remain unchanged: independent English, Myanmar, original-example and source-backed CEFR signoff 0/1,000; final George/Emma headword/example audio 0/4,000 generated and actually listened to; vocabulary-specific desktop/mobile regression not evidenced; physical iPhone Safari review not evidenced; GitHub Pages hosting clearance outstanding; and confirmed production deployment absent. The 54 lessons, separate IELTS bank, established production audio, privacy controls and `main` remain untouched. Remain staging-only.


## CI verification after the A1 core-verbs audit and report update — 2026-11-28

The new A1 audit commit `c17f24a974a7b9d1762f2fc7bea8ca8e6ba5e709` was validated by [run `46151183354`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46151183354): overall success, **14/14 jobs successful**. The jobs endpoint and logs were inspected. Python A1–C1 structural jobs all reported `errors: []` and `independent_approval_inferred: false`; the five Node level jobs reported 200 provisional entries, 200 review tasks, 0 independently verified, and release blocked, then successfully rejected a canonical task-ID swap. The twenty-case mutation suite passed. The Python and Node release-denial jobs passed. All six synthetic audio/evidence adversarial cases passed; the log expressly states that no real review or audio evidence was created.

The report update commit `c16a5016cb38300fdf5d51d0c1492a672b633f80` was itself validated by [run `46151287643`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46151287643): overall success, **14/14 jobs successful**, exact head SHA match. All actual job conclusions were success. The five Python structural logs each contained `errors: []` and `independent_approval_inferred: false`; the five Node structural logs each recorded the correct 200/200/0 counts and successful canonical task-ID swap rejection. The mutation log ended “All twenty negative cases rejected; provisional release also rejected; no independent review inferred.” The Python release log confirmed controlled explicit release denial. The Node release log confirmed `release: BLOCKED`, zero independent approvals for all five levels, and no approval/deployment claim. The adversarial audio log passed all six synthetic checks and explicitly said no real review or audio evidence was created.

The second run validates the report commit recorded here. This report update will itself create a later documentation commit; its own push-triggered CI must be checked separately and must not be inferred from the preceding successful run.
