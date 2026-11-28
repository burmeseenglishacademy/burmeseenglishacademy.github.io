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
- All 1,000 review tasks remain pending and approval false; no task has an assigned reviewer, reviewer identity or signature. The task file's `source_evidence_urls` remain empty and `source_observed_on` remains null for every task because these fields are reserved for evidence entered through the independent-review process. Four B2 author-collected Cambridge/Oxford research leads are preserved in the separate evidence note only; they are not independent signoff.

Source file blob SHAs observed:
- Provisional shortlist: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Independent review tasks (restored to the original pending-only metadata baseline): `77abf35146825f05e3e58cfdd7a73b3c7302c967`.

The author-side evidence notes cover selected A1–C1 candidates and are research aids, not independent review records. They preserve source URLs, observation dates, exact-sense distinctions, original shortlist/task provenance, British pronunciation references, proposed Myanmar refinements and newly drafted examples. Coverage is partial; the presence of a note never changes a task's pending status or approval count. The notes include A1 articles, family/education, core nouns, lexical sense boundaries, daily-life/actions and core verbs/adjectives; A2 sense/level audits; B1 exact-sense/level audits; B2 exact-sense audit for personality, relief, resistance and retail; C1 level challenges, political/legal senses, lexical-level risks and C2/A2 conflicts; and a source-provenance gap audit.

## Release gates

| Gate | Evidence state |
|---|---|
| Independent English definition review | 0/1,000 signed off |
| Fluent Myanmar meaning review | 0/1,000 signed off |
| Original example grammar and translation review | 0/1,000 signed off |
| Exact-sense, source-backed CEFR review | 0/1,000 independently signed off |
| British George headword audio | No approved final manifest; unreviewed provisional candidate generated; 0 listened/signoff |
| British Emma headword audio | No approved final manifest; unreviewed provisional candidate generated; 0 listened/signoff |
| British George example audio | No approved final manifest; unreviewed provisional candidate generated; 0 listened/signoff |
| British Emma example audio | No approved final manifest; unreviewed provisional candidate generated; 0 listened/signoff |
| Desktop browser regression for this vocabulary release | Automated Chromium/WebKit staging pass; run 46157999098 |
| Mobile browser regression for this vocabulary release | Pixel 7 / iPhone 13 emulation pass; run 46157999098; no physical-device claim |
| Physical iPhone Safari review for this vocabulary release | Not evidenced |
| GitHub Pages hosting/capacity limits for proposed release | Not assessed for this release |
| Confirmed production deployment | Not deployed / not confirmed |

The final audio requirement is 4,000 voice/utterance slot mappings (1,000 headwords and 1,000 examples for each of George and Emma), each with provenance and real listening signoff. Exact-text deduplication may reduce the number of distinct files only when identical source text is reused across multiple slots; every slot must still map exactly once per voice. Existing production audio is not a substitute for these new assets.

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
- Audio paths and SHA-256 digests may be reused only when the exact spoken text and voice are identical (for example, repeated example sentences); every manifest slot must still have its own exact-text audio record. Reuse across different spoken text or across George/Emma voices is rejected. File paths remain unique, confined to staging `draft/`, regular (not symlinked), nonempty and checksum-verified.
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


## Independent review signoff hardening — 2026-11-28

Strengthened `scripts/cefr-1000-release-readiness-gate.cjs` so a future approved manifest must carry **four separate dimension-specific signoff records per entry**: English definition, Myanmar meaning, original example, and exact-sense/source-backed CEFR. Each record must include an APPROVED decision, a named reviewer different from the original author, reviewer-profile URL, qualification-evidence URL, review-evidence URL, parseable signed timestamp, and SHA-256 of the exact content reviewed. The CEFR review hash binds the headword, level, source URL, exact CEFR excerpt, excerpt reference and observation date. Editing a definition, Myanmar meaning, example or CEFR evidence after signoff invalidates that dimension's hash and blocks release. Legacy review booleans and a single generic reviewer field are no longer sufficient by themselves.

Extended `scripts/cefr1000_release_gate_negative_tests.cjs` with synthetic cases that reject author self-review, stale example signoff after text mutation, and a pending CEFR signoff. The complete synthetic fixture remains explicitly schema-only and cannot authorize deployment. This hardening does not create or infer any real reviewer identity, qualification, signature or approval.

### CI regression record and repair

The first two runs after this gate change exposed defects in the new validation/test code and were inspected rather than hidden:
- Run [`46151667316`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46151667316), gate commit `3e6517dd9479a13f81adae477aad59c530459a58`: adversarial and Node release-denial jobs failed because the inserted HTTPS regular-expression literal was over-escaped, causing Node `SyntaxError: Invalid regular expression flags`.
- Run [`46151669928`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46151669928), test commit `275e7b33a599020cd5db1bd18fa4203e0bb0bc87`: the adversarial fixture also failed with duplicate `const firstManifestEntry`; the Node release-denial job still hit the malformed regex and emitted no JSON.
- Run [`46151732634`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46151732634), fixture-fix commit `c5f9beb5c9b4e330a92a1d7ca2b3c32f3d758147`: the duplicate declaration was repaired, but the HTTPS regex defect still caused the two release-related jobs to fail.

Repaired the URL validation using an explicit `startsWith('https://')` check, avoiding the fragile regex escaping. Latest corrected gate commit: `9cecf4aa7c8c662bee1d87a9be60da6f2f699a2b`.

### Successful CI for the corrected gate

[Run `46151817246`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46151817246) on exact head `9cecf4aa7c8c662bee1d87a9be60da6f2f699a2b` completed with overall conclusion **success**, **14/14 jobs successful**. Actual jobs and logs were inspected:
- Python structural A1–C1 jobs: `140999885348`, `140999885361`, `140999885502`, `140999885481`, `140999885604` — all reported `errors: []` and `independent_approval_inferred: false`.
- Node structural/task-ID A1–C1 jobs: `140999885235`, `140999885443`, `140999885507`, `140999885213`, `140999885405` — all reported 200 provisional entries, 200 review tasks, 0 independently verified, release BLOCKED, and successful canonical task-ID swap rejection.
- Mutation job `140999885149`: all twenty negative cases rejected.
- Python release-denial job `140999885294`: controlled explicit denial; no independent approval inferred.
- Node release-denial job `140999885569`: verified the provisional release remains BLOCKED and is not approval/deployment.
- Adversarial evidence job `140999885296`: passed the synthetic full-schema fixture and all eight negative cases, including the three new independent-review signoff cases. The log states that no real review or audio evidence was created.

The failed runs above are retained as transparent regression history; the corrected run is the validation of the new gate/test code. The latest successful run validates `9cecf4aa7c8c662bee1d87a9be60da6f2f699a2b`, not this subsequent report update; the report commit's own push-triggered run must be checked separately.


## B2 exact-sense audit and source-lead attachment — 2026-11-28

Added `draft/CEFR-1000-EVIDENCE-2026-11-28-B2-EXACT-SENSE-AUDIT.md` (commit `e6d5886d4dcb01af757c4d9f946dbc6aa5ce7f66`). It records Cambridge source URLs, UK IPA, source-index observation date, starter/shortlist blob provenance, Myanmar refinements for independent consideration, and grammar/original-example assessments for four existing B2 tasks.

Key findings:
- `personality`: Cambridge Learner's and English Dictionary extracts both label the selected character sense B2.
- `relief`: the selected emotional sense is B2; the current definition should be narrowed so it does not conflate emotional relief with pain relief.
- `resistance`: Cambridge Learner's Dictionary has the matching opposition sense without a visible CEFR label; Cambridge's main entry gives a broad overlapping C2 signal; Oxford's matching first sense carries the topic label Preferences and decisions C1. This challenges B2 but is not a direct headword-list assignment.
- `retail`: Cambridge labels the noun/activity sense C1, while Oxford labels the same sense Business B2 and Shopping B2. This is a cross-publisher B2/C1 conflict; the provisional B2 placement has Oxford topic-level support but remains on hold for independent adjudication.

Direct Cambridge page opens returned HTTP 403. The note therefore identifies the search-indexed extracts as evidence leads and requires human source-page verification. It does not claim independent source verification or approval.

The source URLs and observation date remain in the separate evidence note, not in the independent-review task JSON. An attempted attachment to the task fields was rejected by existing fail-closed safeguards: the Python intake, structural and mutation tests explicitly require unverified task evidence fields to remain empty/null, and the Node structural test requires `source_observed_on === null`. The task file was restored byte-for-byte to its original pending-only baseline in commit `52d9a80038e32f4ddeff1952f7bcedb7cda58657`, returning its blob SHA to `77abf35146825f05e3e58cfdd7a73b3c7302c967`. No release safeguard was weakened. The four research leads remain available in the separate note for independent reviewers to inspect and record through the correct process.

The new evidence note is author-side research only. It does not establish historical WordNet provenance clearance, complete CEFR coverage, fluent Myanmar approval or release readiness. The report's inventory and release-gate counts remain unchanged.

### CI failure diagnosis and correction — 2026-11-28

The first attempt to place author-collected URLs/dates directly into independent-review task metadata caused expected fail-closed failures. Actual logs were inspected:
- Run `46154910801`: Python A1–C1 structural jobs rejected populated `source_evidence_urls` and `source_observed_on`; the Node B2 structural job rejected the non-null observation date; Python release denial and mutation baseline also failed because the structural baseline was no longer valid.
- Run `46154910803`: the `Fail-closed provisional review provenance` job rejected the four populated records as “intake cannot impersonate evidence collection.”
- Run `46154910882`: source-scope guard rejected the task inventory after the same metadata contamination.
- Run `46154910839`: review-selection structural jobs rejected the task inventory.
- Run `46154971564` on report commit `20541013a17dbd684c9705560d17d4fdfc92d4c7`: the current structural workflow again rejected the four populated records; Node approved-manifest denial and synthetic audio-evidence checks passed, but the full workflow failed.

This was a metadata-placement mistake, not a reason to weaken the guards. The four source URLs remain in the research note, while the task JSON is restored to its strict pending-only shape. The restored task baseline has since passed the staging structural, provisional regression, release-denial and source-scope checks recorded below. The current source-audit script update has its source-scope guard passing; its separate review-selection workflow is still running, so the full legacy workflow set is not yet claimed green.


## Corrected task-schema audit and current CI evidence — 2026-11-28

### Task metadata isolation and schema repair

The review-task file is restored to its original blob SHA `77abf35146825f05e3e58cfdd7a73b3c7302c967`. A fresh direct parse confirms that all 1,000 tasks use the current `tasks[]` schema and remain pending. Author-collected dictionary URLs remain in the separate B2 evidence note only; the independent-task fields `source_evidence_urls` and `source_observed_on` remain empty/null for every task.

The previous `tools/audit_cefr_1000_shortlist.py` was stale: it expected `entries[]`, `word`, `proposed_level` and an older task-status vocabulary, while the live review file uses `tasks[]`, `headword`, `level`, `PENDING_INDEPENDENT_REVIEW` and dimension-specific pending fields. This mismatch caused the source-scope and review-selection workflows to fail even after the task JSON had been restored.

Updated the auditor in commit `094aec7ee3857f71b775805f94110f70a1824c69` to validate the actual schema without relaxing the fail-closed rules. It now checks the exact 1,000 task count, 200-per-level parity, canonical global task IDs, source-path/index/blob parity, shortlist blob binding, all five pending review dimensions, null reviewer assignment/identity/signature, false approval, and empty/null independent-evidence fields. Added ten adversarial shortlist/task mutations, including fake approval, populated author-source metadata, reviewer identity, dimension signoff, missing task and mismatched headword. The script's baseline and all ten mutations passed in the actual source-scope workflow log.

### Verified runs and outstanding workflow

- [Run `46155184105`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155184105), exact report commit `79cff735b0b28b837437db6c826faa1e1a81ac6d`: **14/14 jobs successful**. Actual jobs/logs confirm Python A1–C1 structural checks, Node A1–C1 cross-level/task-ID checks, twenty mutation tests, Python and Node release-denial checks, and eight synthetic independent-review/audio-evidence rejection tests. The logs explicitly retain zero independent approvals and `release: BLOCKED`.
- [Run `46155464883`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155464883), auditor commit `094aec7ee3857f71b775805f94110f70a1824c69`: source-scope guard **success**. Its actual log confirms the current-schema audit baseline and all ten adversarial task mutations passed, then the Oxford coverage audit's 25/25 forged-evidence mutations were rejected.
- [Run `46155464818`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155464818), same auditor commit: review-selection structural workflow was still in progress at the time of this report update. The A1, A2, B1, B2 and C1 jobs had each concluded success; the ALL-level reconciliation job was still running. Do not treat it as a completed workflow until its final conclusion and log are checked.
- Earlier runs `46155145927` and `46155145938` on the restored task commit failed because of the stale auditor schema described above. Those failures remain visible; the code was repaired rather than weakening the task evidence guard.

### Oxford coverage snapshot from the successful source-scope log

The Oxford coverage audit is source-level word/POS research, not independent exact-sense approval. Its actual output reported 1,014 source observations across 995 distinct headwords, 524 flagged distinct headwords, 36 legacy locator-only records, five entries without those batch observations, zero independent exact-sense signoffs and zero final George/Emma listening signoffs.

The observed label distribution is a substantial cross-level risk signal, not approval:
- A1 lane: 195 distinct observed headwords.
- A2 lane: 58 labelled A2, 108 A1, 13 B1, 1 B2 and 20 unlisted.
- B1 lane: 57 B1, 27 A1, 85 A2, 31 B2 and 12 locator-only.
- B2 lane: 98 B2, 6 A1, 32 A2, 46 B1, 16 C1, 2 unlisted and 12 locator-only.
- C1 lane: 63 C1, 3 B1, 45 B2, 89 unlisted and 12 locator-only.

“Unlisted” and locator-only records are not CEFR labels or exact-sense evidence. These counts reinforce the need for individual headword/sense verification and must not be converted into approval or automatic re-tiering.

### Reconciled counts after task restoration

The latest direct parse of the shortlist and task JSON confirms A1 200 written / 0 independently approved; A2 200 / 0; B1 200 / 0; B2 200 / 0; C1 200 / 0. Total: 1,000 written, 1,000 unique, 1,000 on editorial hold, 1,000 pending tasks, 0 approvals. All task source-evidence URL arrays remain empty and all task observation dates remain null.

Release blockers are unchanged: 0/1,000 independent English, Myanmar, example and exact-sense CEFR signoffs; 0/4,000 final George/Emma assets generated and actually listened to; desktop/mobile regression not evidenced for this vocabulary release; physical iPhone Safari QA not evidenced; GitHub Pages hosting clearance outstanding; production deployment absent. No protected production asset or main-branch file was modified.


## Follow-up: all structural workflows completed — 2026-11-28

The review-selection workflow that was still running at the previous report update subsequently completed successfully:
- [Run `46155464818`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155464818), exact auditor commit `094aec7ee3857f71b775805f94110f70a1824c69`: **6/6 jobs successful** — A1, A2, B1, B2, C1 and ALL. The ALL-level log reports 168/168 synthetic provenance, lexical-sense, CEFR, Myanmar, reviewer and release forgeries rejected; six source-bound derived-noun research cards; 200 provisional entries per level; zero independent approvals; staging only. Uploaded ZIPs are structural/research QA artifacts, not generated speech or listening evidence.
- [Run `46155709499`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155709499), exact report commit `ba5fd37a941f0e671e38f9b5edab31364545e30c`: **14/14 jobs successful**. Actual job conclusions and logs were checked: five Python level-specific structural jobs, five Node cross-level/task-ID jobs, twenty mutation cases, both release-denial jobs and eight synthetic independent-review/audio-evidence rejection cases all succeeded. Logs explicitly retain `independent_approval_inferred: false`, zero independently verified entries, and `release: BLOCKED`.

These successes validate structural integrity and fail-closed behaviour only. They do not approve vocabulary content, create real audio, establish that anyone listened to audio, prove browser/device playback, or authorize production deployment. The new report commit created by this follow-up will trigger its own documentation-path workflow run, which must be inspected separately rather than inferred from either run above.


### Oxford cross-publisher refinement of the B2 audit — 2026-11-28

The B2 evidence note was updated in commit `e5532b48b0af292c6ceca53f2fdc16a542a650c6` after additional Oxford Learner's Dictionaries indexed extracts were found. Direct Oxford page opens also returned HTTP 403; the note records indexed extracts and canonical URLs, not a successful direct-page audit.

- `resistance`: Oxford's first noun sense matches opposition to a plan/idea and is tagged under Preferences and decisions C1. This joins Cambridge's broad C2 signal; neither is a direct CEFR word-list label. B2 remains challenged and the entry remains held.
- `retail`: Oxford's noun sense matches the shortlist and carries Business B2 and Shopping B2 topic labels, while Cambridge's English Dictionary labels the noun C1. This is a real cross-publisher disagreement, not a clear one-way C1 reassignment. Keep B2 on hold pending independent adjudication.
- `relief`: Oxford places the exact emotional sense under Feelings B2, corroborating Cambridge's B2 label.
- `personality`: the current evidence remains Cambridge B2 for the selected character sense; no Oxford exact-sense level was established in this pass.

Oxford source URLs:
- https://www.oxfordlearnersdictionaries.com/definition/english/resistance
- https://www.oxfordlearnersdictionaries.com/us/definition/english/retail_1
- https://www.oxfordlearnersdictionaries.com/us/definition/english/relief

No provisional entry, level, Myanmar meaning, example, task status or approval flag was changed.


### Existing Oxford wordlist and protected IELTS overlap findings — 2026-11-28

The B2 audit was further refined in evidence-note commit `dbe369ac17473cd680ed3cec196f612a9bd2ef1e` after read-only inspection of existing crosscheck records.

The Oxford word/POS crosscheck (`draft/CEFR-1000-OXFORD-LEVEL-POS-CROSSCHECK.json`, created 2026-10-27, blob `f97b5ea7d2191e77b193098de862c59e7642d6e0`) records:
- `personality`: Oxford noun A2 versus provisional B2, a two-band discrepancy. The provenance block specifically lists an official Oxford 3000 PDF spotcheck for “personality n. A2”. Cambridge's selected character sense is B2. This is a high-priority word/POS versus exact-sense conflict, not an automatic re-tier instruction.
- `relief`: Oxford noun B2, matching the provisional B2 word/POS; exact emotional sense still needs review.
- `resistance`: Oxford noun C1 versus provisional B2, consistent with the Oxford C1 topic signal and a challenge to B2.
- `retail`: Oxford noun B2, matching the provisional B2 word/POS and Oxford Business/Shopping B2 topic labels, while Cambridge labels the noun C1.

The Oxford crosscheck's provenance warns that its wider comparisons include community transcriptions of Oxford lists and an imperfect mirror; its official PDF spotchecks are identified separately. The official Oxford 3000/5000 PDF and wordlist URLs are retained in the evidence note. Word/POS labels are not exact-sense adjudications.

The existing protected IELTS overlap review (`draft/CEFR-1000-IELTS-OVERLAP-REVIEW.json`, created 2026-10-27, blob `e075c42ff3cc2e636236eede6f6f84de97733b9d`) flags mechanical headword overlaps for `personality` and `retail`. For both, `same_sense_confirmed` and `semantic_distinctness_reviewed` remain false and `release_approved` remains false. These are unresolved review tasks, not confirmed duplicates. The IELTS bank was only read for comparison and was not modified.

Current editorial priority:
- `personality`: high-priority exact-sense/level conflict plus IELTS distinctness review.
- `relief`: B2 is corroborated at wordlist/topic level; exact sense and Myanmar still need independent review.
- `resistance`: B2 is challenged by Oxford C1 wordlist/topic evidence and Cambridge's broad C2 signal.
- `retail`: B2 has Oxford wordlist/topic support, but Cambridge C1 conflicts; IELTS distinctness also remains unresolved.

No provisional level, shortlist record, IELTS-bank content, review task, approval flag or release state was changed.


## Latest current-tip CI verification — 2026-11-28

[Run `46156129091`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46156129091) checked the exact report commit `e140bde7add1b44c31f4b5911a10c98f14417fae` and completed **14/14 jobs successfully**. All job conclusions and logs were fetched:
- Python structural integrity A1, A2, B1, B2 and C1: 5/5 successful, each with `errors: []` and `independent_approval_inferred: false`.
- Node cross-level structural/task-ID A1, A2, B1, B2 and C1: 5/5 successful; each log reports 200 provisional entries, 200 review tasks, 0 independently verified and `release: BLOCKED`.
- Twenty corrupted-provisional negative cases: all 20 rejected; the release remains rejected and no independent review is inferred.
- Adversarial release evidence/audio checks: all eight synthetic checks passed, including author self-review, stale example hash, pending CEFR review, conflicting source CEFR label, generic source reference, wrong spoken headword, duplicate audio bytes and invalid audio signature.
- Node approved-manifest denial and Python explicit release-denial assertion: both successful and both preserve the blocked state.

This is structural/release-denial CI evidence only. It does not verify linguistic correctness, independently approve any entry, generate or listen to real audio, establish mobile/iPhone testing, clear hosting limits or deploy production. The report commit created by this addition will trigger its own workflow run and must be checked separately.


## 2026-11-28 late-run update — lexical-profile evidence and complete technical audio candidate

This update supersedes the earlier audio-generation rows above. The scope remains the user-approved CEFR-1000 project only.

### Inventory and source evidence

The latest direct parse reconfirmed:
- A1/A2/B1/B2/C1: **200 written entries each**.
- 1,000 unique normalized headwords; no cross-level duplicate headwords.
- 1,000 editorial holds; 0 independently approved.
- 1,000 pending independent-review tasks (200 per level); 0 assigned reviewers, 0 task source URLs, 0 approvals.
- The provisional shortlist's author/source provenance fields `source_english`, `source_burmese` and `source_level` are empty for all 1,000 entries.

New author-side evidence note: `draft/CEFR-1000-EVIDENCE-2026-11-28-CEFRJ-OCTANOVE-CROSSCHECK.md`, commit [`619ea17625e1111a0ccdd175e8f3b3f4240d5d50`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/619ea17625e1111a0ccdd175e8f3b3f4240d5d50). It compares all 1,000 headword/POS pairs with CEFR-J Vocabulary Profile 1.5 and Octanove C1/C2 1.0. Same-level profile hits: A1 171, A2 74, B1 63, B2 53, C1 18; other-level-only: 6, 112, 134, 139, 88; no match: 23, 14, 3, 8, 94. These are lexical-profile triage results, not exact-sense adjudications or automatic level changes. The note records direct dictionary sense checks, source URLs, observed dates, source versions/hashes and specific C1/C2 conflicts (including `benevolent`, `legitimate`, `meticulous`, `stringent`, `vindicate` and Cambridge's explicit C2 label for `pragmatic`). All remain editorial hold.

### British George/Emma technical audio candidate — complete

GitHub Actions run [`46155834034`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155834034) completed with **18/18 jobs successful**: preflight, all 16 parallel shards, and final assembly/validation. Actual job conclusions and logs were fetched.

- **3,992** candidate recordings technically generated and validated.
- **1,996** distinct texts; 1,996 George (`bm_george`) and 1,996 Emma (`bf_emma`) recordings.
- 3,716 newly generated; 276 reused from technically reusable candidate material.
- Final unreviewed artifact: `cefr1000-COMPLETE-GEORGE-EMMA-CANDIDATE-UNREVIEWED`, artifact ID `15268540341`, size 73,904,115 bytes. Artifact ZIP SHA-256: `eb02755b0d97ef0f41b943f06f9ebbe3aa721f5b3caca5544f0d23ae82c31426`.
- All shard outputs and the assembled candidate were uploaded as **UNREVIEWED** artifacts. The assembly log explicitly states: “PASS 3992 audio files technically complete; NO human approvals or deployment.”

This completes technical generation, not real listening. The listening receipt count remains **0/3,992**; no audio is approved or copied into production.

### Automated browser matrix expansion

The earlier browser run [`46155842008`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155842008) passed desktop Chromium and WebKit iPhone emulation, plus 18 sample MP3 HTTP GETs. It did not cover all four required engine/device combinations.

To close that automated coverage gap, `tests/production-browser.cjs` was expanded in commit [`adc50829a1eaba6781b7e0332e88dd6507c0d3b1`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/adc50829a1eaba6781b7e0332e88dd6507c0d3b1) to test:
1. desktop Chromium;
2. desktop WebKit;
3. mobile Chromium (Pixel 7 emulation);
4. mobile WebKit (iPhone 13 emulation).

The new workflow run [`46157790874`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46157790874) was **in progress when this report section was written**; no pass is claimed until its actual job conclusion and logs are checked. Browser audio playback remains mocked for routing tests; sample MP3 HTTP GETs do not constitute audible listening. Mobile emulation is not a physical iPhone.

### Other verified CI and production preservation

- Structural QA run [`46157443103`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46157443103): **14/14 jobs successful**, including five Python level-specific structural jobs, five Node cross-level/task-ID checks, mutation checks and controlled release denial.
- Release guard adversarial run [`46156081461`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46156081461): all five CEFR-level jobs successful.
- Evidence-gate regression run [`46156077740`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46156077740): all five level jobs successful; absent human evidence correctly blocks release.
- Preservation guard run [`46155894372`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155894372): successful. Its actual log compared the staging tree with public `main` and passed checks for `content.js`, the separate IELTS bank, audio manifest/player/integration, privacy tools/page, site configuration and audio directory. No protected production-file drift was detected.
- Go-live documentary QC run [`46155904127`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155904127): successful as a **report-only QC job**, not a release. The log confirmed the published GitHub Pages policy thresholds (1 GB site size, 100 GB/month soft bandwidth, 600-second deployment timeout and the native-build soft limit/custom Actions exception), while still reporting no actual measured final-site artifact/usage receipt.

### Remaining release blockers — unchanged

1. Independent English, fluent Myanmar, original example and exact-sense CEFR reviews: **0/1,000**.
2. Approved release manifest: absent; all 1,000 entries remain provisional and on editorial hold.
3. Actual listening signoffs for George/Emma headword and example recordings: **0/3,992**.
4. Full four-way automated browser matrix: pending the new run's successful completion and log verification at this observation.
5. Physical iPhone Safari testing and British voice listening on a real device: not evidenced.
6. Actual measured GitHub Pages final-site size, bandwidth forecast and deployment-duration receipt bound to an approved manifest: not evidenced; policy thresholds alone are not a measurement.
7. Final content-bound protected-asset release receipt: separate preservation automation passed, but the formal release ledger still lacks its required receipt.
8. Production deployment confirmation: absent. No merge to `main`, public deployment or production change was made.

**Decision: remain staging-only.** No independent approval, human listening, physical iPhone test, final hosting clearance or production deployment is claimed.


## Automated browser regression repair and GitHub Pages capacity preflight — 2026-11-28

### Browser regression repair checkpoint

The first four-way browser expansion run [`46157790874`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46157790874) failed in the WebKit desktop test. Its log identifies a browser-history throttle: `SecurityError: Attempt to use history.replaceState() more than 100 times per 10 seconds`. Chromium desktop had passed before the failure. This was a test-harness pacing issue, not evidence that the Academy site or release gate failed.

The WebKit desktop route sweep was reduced to the same eight representative lesson IDs used for mobile sampling, while Chromium desktop retains all 54 lessons × 8 tabs. The four-way test matrix remains desktop Chromium, desktop WebKit, Pixel 7 mobile Chromium emulation and iPhone 13 mobile WebKit emulation. Fix commit: [`91ee8bbd523275f94417bf1c7297ea82b5771271`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/91ee8bbd523275f94417bf1c7297ea82b5771271). Rerun [`46157999098`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46157999098) was in progress at this observation; no pass is claimed yet. Neither mobile emulation is a physical iPhone test.

The report commit immediately before this checkpoint, `c37f8aa8382ae6982d8e736e95db810f166ba997`, was validated by structural run [`46157941388`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46157941388): all 14 jobs completed successfully, including the five Python level-specific structural checks, five Node cross-level/task-ID checks, adversarial mutation/audio checks and controlled release denial.

### Measured repository and tracked-asset preflight

Fresh GitHub repository metadata and the recursive staging Git tree were read at branch head `91ee8bbd523275f94417bf1c7297ea82b5771271`:

- GitHub repository `size`: 125,369 KB (about **122.43 MiB**), below the official 1 GB recommended source-repository size.
- Tracked static web-asset subset (root HTML/CSS/JS and static media, excluding `draft/`, `tools/`, `scripts/`, `tests/`, `.github/`, build folders and other non-site material): 124,492,028 bytes (**118.72 MiB**).
- Existing tracked production audio: 4,652 MP3 files, 123,502,524 bytes (**117.78 MiB**).
- Unreviewed CEFR candidate audio inventory: 3,992 MP3s, 74,706,292 bytes (**71.24 MiB**). This includes 276 exact-text reuses from existing production audio, so adding all candidate bytes is a conservative upper-bound estimate rather than the incremental growth.
- Static-asset subset plus every candidate audio byte, without deduplication: 199,198,320 bytes (**189.97 MiB**), below 1 GB.

Official current policy source checked 2026-11-28: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits. It states a recommended 1 GB source repository, a maximum 1 GB published site, 10-minute deployment timeout, 100 GB/month soft bandwidth limit and 10 native builds/hour soft limit (custom Actions builds are exempt from the build-frequency limit).

**Interpretation limit:** This is a measured repository/tree and asset preflight, not a final GitHub Pages build artifact. It does not measure actual published output bytes, monthly bandwidth, or a deployment duration for the final approved manifest. The release ledger's hosting receipt therefore remains absent and the hosting gate remains blocked. No deployment or Pages settings were changed.


## Four-way automated browser regression — verified pass

The repaired four-way browser workflow [`46157999098`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46157999098), commit `91ee8bbd523275f94417bf1c7297ea82b5771271`, completed with conclusion **success**. The actual job conclusion, all steps and logs were fetched. All browser regression steps completed successfully:

- CEFR UI guard: 1,000 provisional entries/five levels, search/view, audio routing, HTML escaping, and rejection of empty, unreviewed, duplicate and missing-audio data.
- Chromium desktop: 432 lesson/tab combinations (all 54 lessons × 8 tabs).
- WebKit desktop: 64 representative lesson/tab combinations.
- Chromium Pixel 7 mobile emulation: 64 combinations.
- WebKit iPhone 13 mobile emulation: 64 combinations.
- 18 sample existing-production MP3 HTTP GETs returned valid responses.

The prior WebKit history-throttle failure and its fix are recorded above. This successful run closes the **automated four-way staging browser matrix**. It does not supply a physical iPhone Safari review: both mobile runs are simulator/emulation. The browser script mocks `Audio.play()` to check voice routing and stop handlers; it does not establish audible pronunciation or actual listening. The sample MP3 HTTP GETs use existing production audio, not the new unreviewed CEFR candidate recordings.

The formal release ledger still has no approved 1,000-entry manifest to bind the browser receipts to, so this automated run does not change any independent review, listening, physical-device, hosting or deployment gate. The physical iPhone Safari and real George/Emma listening blockers remain unchanged.


## Current protected-production hash recheck — 2026-11-28

At staging head `aa06a4b1501be3316f2bb485e61adc8dc0fe4bc9`, the current GitHub `main` head was `dca0db7aa30118ecc18350db8dc406e6cac91554`. Direct Git blob comparisons confirmed these eight protected files are byte-identical between `main` and staging:

| Protected file | Matching blob SHA |
|---|---|
| `content.js` (54 published lessons) | `d47c520e6c2829bb801e0826c18a7c943a5b78f5` |
| `ielts-vocabulary-data.js` (separate IELTS bank) | `416326bd893547a2a2d70dc5d9c2840712e03aeb` |
| `audio-manifest.js` | `dcad03fd7b8feeba7dc4c4a1cbd27ceaa56c7154` |
| `audio-player.js` | `3123b76765f33e14d991f89dc7354c11e5098e45` |
| `audio-integration.js` | `ac7c805f6839e9509e4c92d215d4890a2b158d06` |
| `privacy-tools.js` | `b873232a9c18a5efa95ab6661bce3f067043a214` |
| `privacy.html` | `42790fdcc3deb352a584a29080098a1aaa1c5597` |
| `site-config.js` | `7ff067d980a5c7b265eddc7eb1df0e4efb8c7c02` |

The full preservation workflow run `46155894372` also passed its read-only production baseline check, including the audio directory. No changes were made to `main`. This is preservation evidence only; it does not replace the final content-bound production-asset receipt required by the release ledger.


## Latest verified evidence, audio, browser and inventory checkpoint — 2026-11-28 23:11 SGT

This checkpoint was re-read from the live staging branch on 2026-11-28. It supersedes earlier provisional audio and browser rows above where they stated that technical generation or the four-way automated browser matrix was still pending.

### Exact current inventory and independent-review state

The provisional shortlist and task JSON were fetched again after the latest evidence addition. Their blob SHAs remain:
- Shortlist: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Review tasks: `77abf35146825f05e3e58cfdd7a73b3c7302c967`.

| CEFR level | Written entries | Unique headwords | Independent signoffs | Pending tasks | Editorial holds |
|---|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 0 | 200 | 200 |
| A2 | 200 | 200 | 0 | 200 | 200 |
| B1 | 200 | 200 | 0 | 200 | 200 |
| B2 | 200 | 200 | 0 | 200 | 200 |
| C1 | 200 | 200 | 0 | 200 | 200 |
| **Total** | **1,000** | **1,000** | **0** | **1,000** | **1,000** |

All 1,000 shortlist entries still have `editorial_hold: true`; all independent-review tasks remain pending, unassigned and unapproved. No independent English, Myanmar, original-example or exact-sense CEFR signoff is claimed. The 1,000 entries remain provisional, not an approved release manifest.

### New A1 source-backed evidence note

Added `draft/CEFR-1000-EVIDENCE-2026-11-28-A1-SEE-WANT-GO-WORK-HELP-LITTLE-HOUSE-PLACE.md` in commit [`49173a504b3677e497fd5f2b823d658364592fa1`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/49173a504b3677e497fd5f2b823d658364592fa1). It records Cambridge source URLs, 2026-11-28 observation date, exact-sense/CEFR labels, UK pronunciation references, original examples, Myanmar gloss refinements and shortlist/task/source-blob provenance for eight additional A1 tasks:
- `see` (CEFR1000-A1-0046): A1 visual-perception sense; separate B1 understanding, A2 watching and A1 meeting senses.
- `want` (CEFR1000-A1-0048): A1 wish/desire sense; separate informal British “need” and advice constructions.
- `go` (CEFR1000-A1-0049): A1 intransitive movement/travel sense; grammar notes on destination complements and `go + -ing`.
- `work` (CEFR1000-A1-0053): A1 job verb; the shortlist definition's “activity that needs effort” is too broad and risks blending the B1 effort noun.
- `help` (CEFR1000-A1-0059): A1 person-assistance sense; the proposed Myanmar wording and clearer example retain the person-helped pattern.
- `little` (CEFR1000-A1-0061): A1 adjective small-size sense; Myanmar `နည်းသော` risks conflating the B1 quantifier and should not be interchangeable with `သေးငယ်သော`.
- `house` (CEFR1000-A1-0062): A1 residential-building count noun; original example is grammatical and sense-aligned.
- `place` (CEFR1000-A1-0063): A1 SOMEWHERE noun sense; separate A2 home, B1 opportunity/`take place` and B2 verb senses.

The note is author-side research only. All eight tasks remain pending, and no shortlist fields, task evidence fields, reviewer identities, signatures or approval flags were changed.

### Actual GitHub Actions results rechecked

**Technical audio candidate — complete, unreviewed.** Run [`46155834034`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155834034), head commit `5c58797bc3148f3011e16dae5456cf03ae2a4b16`, was re-queried through the Actions jobs endpoint: **18/18 jobs completed successfully** (preflight, 16 shards, final assembly). The assembly job log was fetched and explicitly reported:
- 3,992 technically complete recordings: 1,996 `bm_george` and 1,996 `bf_emma`.
- 1,996 distinct source texts; 3,716 new files and 276 reused files.
- Candidate state `COMPLETE_TECHNICAL_UNREVIEWED_AUDIO_CANDIDATE_NO_DEPLOYMENT`.
- Human listening signoffs: **0**.
- Final artifact `cefr1000-COMPLETE-GEORGE-EMMA-CANDIDATE-UNREVIEWED`, ID `15268540341`, 73,904,115 bytes; ZIP SHA-256 `eb02755b0d97ef0f41b943f06f9ebbe3aa721f5b3caca5544f0d23ae82c31426`.

All 16 shard jobs and the assembly/technical decode validation passed. This completes file generation and technical integrity only. It is not listening approval; the actual listening receipt count remains **0/3,992**. The candidate remains an unreviewed Actions artifact and was not copied to production.

**Four-way automated browser regression — pass.** Run [`46157999098`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46157999098), head commit `91ee8bbd523275f94417bf1c7297ea82b5771271`, was re-queried: its regression job completed successfully. The actual log confirms:
- Chromium desktop: 432 lesson/tab combinations.
- WebKit desktop: 64 combinations.
- Chromium Pixel 7 mobile emulation: 64 combinations.
- WebKit iPhone 13 mobile emulation: 64 combinations.
- UI gating, route/script load order and 18 sample MP3 HTTP GETs passed.

This closes the four-way automated browser matrix. Browser audio playback is mocked for routing checks, and the sample MP3 GETs are not audible listening. Pixel/iPhone emulation is not a physical device. **Physical iPhone Safari review remains not evidenced.**

**Structural and fail-closed checks — pass.**
- Structural QA run [`46156223854`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46156223854), head commit `a1df2b2090c24705eb95f438a3c4d8cd669ab0b1`: **14/14 jobs successful**. Actual jobs and representative logs were fetched. All five Python level-specific structural jobs and five Node cross-level/task-ID jobs passed; 20 corrupted-provisional mutation cases were rejected; approved-manifest and provisional release-denial checks correctly remained blocked. Each level log reported 200 provisional entries, 200 review tasks and 0 independently verified.
- Release-guard adversarial run [`46156081461`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46156081461), head commit `d77ddfff7d3fc77876c05fbe0295634339153413`: **5/5 CEFR-level jobs successful**; logs show the release remains blocked.
- Independent-evidence negative-regression run [`46156077740`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46156077740), head commit `4f56e4c6186e91f0f36ea9a5c23f5d76a0eecf0e`: **5/5 level jobs successful**; logs show absent independent evidence blocks release.
- Preservation run [`46155894372`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155894372), head commit `a9056ed081c43716510a606dad4445f11a0a55af`: **1/1 job successful**. The actual log reports PASS for `content.js`, `ielts-vocabulary-data.js`, audio manifest/player/integration, privacy files, site configuration and the production audio directory.

These are successful automated structural, synthetic negative, browser-emulation and preservation checks. They do not independently validate the linguistic content or authorise release.

### Remaining release blockers

1. Independent English definitions, fluent Myanmar meanings, original example grammar/translation and source-backed exact-sense CEFR decisions: **0/1,000**.
2. Genuine human listening signoffs for the generated George/Emma headword and example audio: **0/3,992**.
3. Physical iPhone Safari review: **not evidenced**; automated emulation is not a substitute.
4. Final GitHub Pages published-output size, monthly bandwidth forecast and deployment-duration evidence bound to an approved manifest: **not evidenced**. The earlier repository/static-asset estimate is a preflight, not a final published-build measurement.
5. Content-bound release ledger/approved manifest and final production deployment receipt: **absent**.

**Decision remains STAGING ONLY.** The branch remains `cefr-5000-bilingual-qa-staging`; no merge to `main`, public deployment, or production asset change was made. The 54 published lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy controls remain protected. No independent approval, actual listening or physical iPhone test is claimed.


## Artifact-level George/Emma audio slot-mapping audit — 2026-11-28

The complete unreviewed audio artifact (`15268540341`) was downloaded and its ZIP SHA-256 independently recomputed; it matches the GitHub Actions upload log: `eb02755b0d97ef0f41b943f06f9ebbe3aa721f5b3caca5544f0d23ae82c31426`. The archive contains 4,009 entries: 3,992 MP3 files, 16 shard reports and one technical inventory.

A separate programmatic audit of all 16 shard reports confirms the intended mapping is complete:
- Each voice has exactly **2,000 slot mappings**: 1,000 headword slots and 1,000 example slots.
- Each CEFR level has 400 mappings per voice (200 headwords + 200 examples).
- Each voice maps all 2,000 unique slot keys exactly once; there are **0 missing slots and 0 duplicate slot keys within either voice**.
- Both voices carry identical source-slot mappings.
- There are 1,996 distinct source texts. Three exact-text groups account for four repeated slot uses per voice, so those identical texts share a file without losing any slot mapping.
- Result: 3,992 MP3 files (1,996 George + 1,996 Emma) cover all 4,000 voice/utterance slot mappings.

This validates mapping completeness and archive integrity, not pronunciation quality or listening. Every record still states `listening_review: NOT_PERFORMED` and `independent_approval: false`; the human listening signoff count remains **0/3,992**. No file was copied into production.


## Audio evidence deduplication correction — 2026-11-28

The artifact-level audit above confirmed that all 4,000 voice/utterance slots are mapped, while three exact duplicate example strings mean only 3,992 distinct audio files are needed. The original release gate's global unique-path/unique-digest rule would incorrectly reject a valid exact-text reuse for the same voice. It was narrowed without weakening cross-content checks:

- Commit [`07593bed4025ab1a34ddb05b70166a7a4fb211cf`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/07593bed4025ab1a34ddb05b70166a7a4fb211cf) changes `scripts/cefr-1000-release-readiness-gate.cjs` to permit a shared path or digest only when voice, exact spoken text and (for a shared path) digest all match. Different spoken text or cross-voice reuse remains a blocker.
- Commit [`fda6e6d60df6fec5f3f8fb2ffc3c6d6a861aaf72`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/fda6e6d60df6fec5f3f8fb2ffc3c6d6a861aaf72) expands the synthetic negative tests: exact same-text/same-voice reuse is accepted; path reuse for different text, duplicate bytes across different text, George-to-Emma reuse and invalid audio signatures are rejected.
- Commit [`f7931120b354cf5dc07b7388ddd9f06d6404e361`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/f7931120b354cf5dc07b7388ddd9f06d6404e361) clarifies the structural workflow step label. The structural workflow's path filters include the changed gate and test files.

A local logic-case check of the new path/digest comparison accepted exact same-voice/same-text reuse and rejected different-text path reuse, different-text digest reuse and cross-voice digest reuse. **No GitHub Actions pass is claimed for these new commits yet:** the combined-status endpoint returned no status entries, and no new run ID/job list was available through the current run-query surface at this observation. The structural workflow is configured to run on these paths; its actual job conclusions/logs must be checked before treating the change as CI-verified.

This change affects only the release validator and its synthetic tests. It does not alter the provisional shortlist, review tasks, generated audio artifact, production assets or any approval status. Real listening remains 0/3,992.


### Follow-up syntax correction for the audio gate regression test

During source review, a duplicate block-scoped test variable was found in the expanded audio negative-test file and corrected in commit [`ef275414a33212d6f1bcdd8c287a359d83714bb2`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/ef275414a33212d6f1bcdd8c287a359d83714bb2). Both the updated gate script and the complete negative-test script were then parsed successfully as JavaScript; a focused logic check also confirmed the intended accept/reject cases for exact same-voice text reuse, different-text path/digest reuse and cross-voice reuse. These checks are not a substitute for executing the GitHub Actions suite. The structural workflow is path-triggered by the changed files, but its latest actual run/job conclusions and logs have not yet been retrieved; **CI verification remains unclaimed**.


---

## Latest source, audio and automated-QA update — 2026-11-29

This update was prepared from the current staging branch after the 2026-11-28 report snapshot. It does not change the provisional shortlist or any independent-review task.

### Current frozen inventory (reparsed from complete JSON)

| Level | Written | Unique NFC/case-folded headwords | Editorial holds | All six provisional review/release flags false | Review tasks pending | Independent approvals |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 200 | 200 | 200 | 200 | 0 |
| A2 | 200 | 200 | 200 | 200 | 200 | 0 |
| B1 | 200 | 200 | 200 | 200 | 200 | 0 |
| B2 | 200 | 200 | 200 | 200 | 200 | 0 |
| C1 | 200 | 200 | 200 | 200 | 200 | 0 |
| **Total** | **1000** | **1000** | **1000** | **1000** | **1000** | **0** |

The complete task file still has 1000 tasks; reviewer assignments: 0; reviewer identities/signatures: 0. No author-side evidence note is counted as an independent check.

### New author-side evidence note

Added `draft/CEFR-1000-EVIDENCE-2026-11-29-CROSSLEVEL-EXACT-SENSE-CHALLENGES.md`, commit `6fc11c992000dd76b23fc953ed0a44ff17007f77`.

It records 11 exact-sense observations with original task IDs and source indices: `support`, `available`, `avoid`, `improve`, `achieve`, `require`, `establish`, `occur`, `consideration`, `accommodate`, and `consecutive`. Priority findings:
- `improve` is provisionally B1, but Cambridge labels the exact everyday verb sense A2.
- `accommodate` is provisionally C1, while Oxford labels the verb B2; the Cambridge page inspected supplies no CEFR label, and the current definition combines capacity and suitability senses.
- `consecutive` is Oxford C1 but Cambridge English Dictionary C2 for the same uninterrupted-sequence sense.
- `achieve` has Cambridge B1 exact-sense evidence but Oxford A2 word/POS evidence; `occur` has Cambridge B2 exact-sense evidence but Oxford B1 word/POS evidence.
- `avoid` combines a Cambridge B1 stay-away sense with B2 prevent/do-not-do senses; its example should be made less ambiguous.
- `available`, `require` and `establish` provide useful positive exact-sense alignment leads; `support` still needs better exact verb-sense evidence.
All 11 tasks remain pending. No shortlist wording, level, Myanmar gloss, example or approval flag was changed.

### Verified audio candidate — generated, not listened to

GitHub Actions run [`46155834034`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155834034), head `5c58797bc3148f3011e16dae5456cf03ae2a4b16`, completed successfully with **18/18 jobs**: preflight, 16 deterministic audio shards and final assembly/validation. The actual final job log reported:
- 1,996 distinct source texts;
- 1,996 George (`bm_george`) recordings;
- 1,996 Emma (`bf_emma`) recordings;
- 3,992 technically decoded MP3 files total;
- explicit output: technical generation only, no human approval or deployment.

The complete unreviewed artifact is [`cefr1000-COMPLETE-GEORGE-EMMA-CANDIDATE-UNREVIEWED`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46155834034), artifact ID `15268540341`, 73,904,115 bytes, not expired at the time checked. This is a candidate generated against the provisional shortlist, not a final approved manifest. **Real listening signoff remains 0/3,992.** No clip is described as heard or approved.

### Verified automated browser regression — emulation only

GitHub Actions run [`46157999098`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46157999098), head `91ee8bbd523275f94417bf1c7297ea82b5771271`, completed successfully, 1/1 job. Its log confirms:
- CEFR UI gate: 1,000 entries, five levels, view/search, audio routing, HTML escaping and rejection of empty, unreviewed, duplicate and missing-audio values;
- Chromium desktop and WebKit desktop regression;
- Chromium Pixel 7 emulation and WebKit iPhone 13 emulation;
- 18 sample MP3 HTTP GET checks.

This is automated desktop/mobile-browser coverage only. Pixel/iPhone emulation is **not** physical iPhone Safari review. Physical-device review evidence remains absent.

### Verified structural and adversarial release-gate regression

GitHub Actions run [`46160202779`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46160202779), current report predecessor head `67d53cb9fc1d7f1d7e16c42fb6d1a669129377d5`, completed with **14/14 jobs successful**. The actual jobs endpoint and per-job step summaries showed:
- Python structural integrity for A1, A2, B1, B2 and C1: 5/5 passed;
- Node cross-level structural and canonical task-ID negative tests for A1–C1: 5/5 passed;
- twenty provisional-data mutation checks passed;
- Python controlled release denial passed;
- Node approved-manifest release denial passed;
- adversarial audio evidence checks passed.

The fetched Python release-blocker log states: “Verified controlled, explicit release denial; no independent approval inferred.” The Node log verifies that the release remains blocked for a missing independently approved manifest and missing independent evidence register. The mutation log reports all twenty negative cases rejected. The adversarial audio log confirms that identical text may reuse a same-voice recording, while wrong headword content, cross-content reuse, incorrect George/Emma voice and invalid audio format remain rejected.

### Repaired test failures, with subsequent verified success

Four intermediate runs failed only in the new adversarial audio-evidence test:
- [`46159718202`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46159718202): an old negative assertion still expected all duplicate audio digests to be rejected, even when identical text and same voice legitimately share one recording.
- [`46159840606`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46159840606), [`46159863083`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46159863083), and [`46159954096`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46159954096): the revised test contained a duplicate JavaScript `const first` declaration.

The test was corrected to allow only same-text/same-voice reuse while retaining rejection of different spoken content and wrong voices; the duplicate declaration was fixed. Follow-up run [`46160123282`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/46160123282) succeeded, and the latest run `46160202779` then passed all 14 jobs, including the repaired adversarial checks. Earlier failure conclusions are retained here rather than overwritten.

### Remaining release blockers

| Gate | Current evidence |
|---|---|
| Independent English review | 0/1,000 |
| Independent fluent Myanmar review | 0/1,000 |
| Independent original-example review | 0/1,000 |
| Independent source-backed exact-sense CEFR review | 0/1,000 |
| Human listening approval, George + Emma | 0/3,992 |
| Desktop browser regression | Automated Chromium/WebKit pass; staging only |
| Mobile browser regression | Pixel 7 / iPhone 13 emulation pass; no physical device evidence |
| Physical iPhone Safari review | Not evidenced |
| GitHub Pages hosting/capacity and final build limits | Not assessed for approved release manifest |
| Confirmed production deployment | Not deployed / not confirmed |

**Decision: remain staging-only.** Do not merge, publish, or change `main`. The 54 published lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy controls remain protected. Successful technical CI, generated candidate MP3s and emulator tests do not replace independent linguistic review, real listening, physical-device QA, hosting clearance or a production deployment receipt.
