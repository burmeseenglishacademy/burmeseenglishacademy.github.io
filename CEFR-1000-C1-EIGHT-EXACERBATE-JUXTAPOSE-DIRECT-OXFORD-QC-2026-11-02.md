# CEFR 1000 — C1 eight Oxford direct-sense triage (2 November 2026)

**STAGING ONLY / RELEASE BLOCKED.** This is the user-approved **1,000-total** project (A1/A2/B1/B2/C1: **200 each**), not the obsolete 5,000 plan. Branch: `cefr-5000-bilingual-qa-staging`. Frozen shortlist blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; upstream batch57 blob: `7eaf88b9ed7687b26ccde713262f10fb209743a8`.

## New publisher evidence

Directly opened the following **Oxford Advanced Learner's Dictionary** English entries on **2026-11-02**. Line ranges are observed page-text locators, not persistent publisher page hashes. None of the eight directly observed entries established a **word-and-exact-sense C1 CEFR badge**. Do not borrow unrelated Word-of-the-Day footer labels or topic-level `c2` labels. Oxford's dictionary meaning/grammar observations are **not** independent editorial review.

| Held C1 word | Direct Oxford source | Observed page lines | Distinct editorial issue |
|---|---|---|---|
| exacerbate | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/exacerbate) | 111–114 | Transitive 'make worse'; Health problems `c2` is a topic label, not C1 evidence |
| exonerate | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/exonerate) | 111–114 | **Official declaration** of non-responsibility; merely finding exculpatory evidence is not identical |
| fallacy | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/fallacy) | 105–116 | Countable false belief vs countable/uncountable faulty reasoning |
| fervent | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/fervent) | 101–107 | Strong **sincere** feelings; normally attributive before a noun |
| galvanize | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/galvanize_1) | 101–122 | Spur people to act vs specialist **zinc-coating**; British `galvanise` variant and audio spelling |
| incongruous | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/incongruous) | 95–106 | Contextually unsuitable, not merely different |
| introspection | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/introspection) | 95–107 | **Uncountable** self-examination including motives for actions |
| juxtapose | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/juxtapose) | 101–112 | Reveal contrast **or relationship**; `juxtapose A with B`, often passive |

The eight-card [research packet](draft/CEFR-1000-C1-EIGHT-DIRECT-OXFORD-EXACERBATE-JUXTAPOSE-SENSE-2026-11-02.json) retains frozen English/Myanmar/example fields, original Git source path/index/blob, publisher URLs, UK IPA, observed line ranges, risks, and eight original **unapproved** bilingual/example alternatives. The shortlist and review flags remain untouched. Independent reviewers must choose whether to revise, reject, replace, or keep each entry, and separately establish source-backed CEFR placement; this report does not settle that question.

## Mechanical safeguard and tests

New [fail-closed auditor](tools/audit_cefr_1000_c1_eight_exacerbate_juxtapose.py) pins Git blob SHA of both source files and the new research packet, verifies 1,000 unique frozen headwords (200 each), all held, zero review flags, original batch57 provenance, exact publisher entry URL/POS/IPA/line ranges, and prohibits fabricated exact-sense CEFR labels and false English/Myanmar/example/audio/iPhone/launch receipts. Its `--self-test` exercises **184 synthetic adversarial cases** (8 × 23) without creating human approvals. Added to all six parallel A1/A2/B1/B2/C1/ALL structural jobs and documentary **NO DEPLOY** workflow.

**CI evidence limitation:** new workflow run IDs, final job conclusions and job logs are **not yet retrievable**; do **not** claim this new auditor has passed GitHub Actions. Prior verified structural [run 41394722700](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41394722700) and documentary [run 41394736038](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41394736038) predate these edits. Next feasible run must check current run IDs, all six job conclusions and actual logs, and repair failures before recording success.

## Release readiness — unchanged

| Level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

All 1,000 remain on editorial hold. Required independent exact-sense CEFR/English/Myanmar/example signoffs, approved deduplicated manifest, generated George/Emma **headword and example** audio with **real listening**, browser/mobile regression, **physical iPhone Safari** evidence, measured GitHub Pages limits, verified preservation of 54 lessons/separate IELTS bank/existing production audio/privacy, and confirmed production deployment are **not complete**. Do not merge, change main, publish, or imply a launch. Keep existing hourly cadence.
