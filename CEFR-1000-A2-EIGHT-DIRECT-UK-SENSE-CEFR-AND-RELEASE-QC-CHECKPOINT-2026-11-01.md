# CEFR 1,000 — A2 eight British-English sense and CEFR triage (1 November 2026)

**STAGING ONLY / RELEASE BLOCKED.** Branch `cefr-5000-bilingual-qa-staging`; approved project size remains **1,000 total** (A1/A2/B1/B2/C1 = 200 each). This is source research and mechanical QC, **not independent review, CEFR certification, audio listening, physical iPhone testing or deployment**.

## Publisher-source inspection and editorial handoff

Eight existing A2 provisional cards were compared against directly opened Oxford Advanced Learner's Dictionary headword pages on **2026-11-01**. The full original English, Myanmar, examples, source paths, source indices and historical blob SHAs are frozen in [the eight-record packet](draft/CEFR-1000-A2-EIGHT-DIRECT-UK-SENSE-AND-CEFR-TRIAGE-2026-11-01.json). All proposed Myanmar/example alternatives are **unapproved**.

| Frozen A2 word | Direct publisher page and page-line locator | Meaning, grammar or level risk |
|---|---|---|
| **program** (noun) | [Oxford program](https://www.oxfordlearnersdictionaries.com/us/definition/english/program_1), lines 103–123 | UK **program** is correct for computer instructions; **programme** is the British spelling for other noun senses. Do not mechanically replace the computer sense with *programme*. Oxford Computers a2 is a **topic badge**, not independent exact-sense CEFR signoff. |
| **public** (noun) | [Oxford public](https://www.oxfordlearnersdictionaries.com/definition/english/public_2), lines 103–124 | **the public** is a collective noun; Oxford allows singular/plural agreement. Do not confuse with *public* adjective or omit *the* indiscriminately. People-in-society a2 is a topic badge. |
| **college** (noun) | [Oxford college](https://www.oxfordlearnersdictionaries.com/definition/english/college), lines 103–159 | UK further education/training after school differs from US degree-institution use. Existing draft wording is broad; independent reviewer must confirm teaching context. |
| **post** (noun) | [Oxford post](https://www.oxfordlearnersdictionaries.com/definition/english/post_2), lines 186–224 | Countable internet/blog **post** differs from British uncountable postal **post** and a job **post**. Phones/internet a2 is a topic badge, not an exact-sense CEFR review. |
| **term** (noun) | [Oxford term](https://www.oxfordlearnersdictionaries.com/definition/english/term_1), lines 107–139, 180–188 | The draft means technical **word/expression** (sense 1), not a school **term** (sense 2). A B1 topic badge for school terms must not be assigned to the technical-word sense. |
| **pretty** (adverb) | [Oxford pretty](https://www.oxfordlearnersdictionaries.com/us/definition/english/pretty_1), lines 103–127 | Informal degree adverb (*fairly*) differs from attractive adjective. Cambridge search-index adverb B1 conflicts with draft A2; **direct Cambridge page opened with HTTP 403**, so indexed CEFR is a research lead, not independent evidence. |
| **due** (adjective) | [Oxford due](https://www.oxfordlearnersdictionaries.com/definition/english/due_1), expected-arrival sense | Predicative expected-time use differs from *due to* = caused by, payments due and *in due course*. Cambridge index labels the expected sense B1 versus draft A2; direct Cambridge page HTTP 403. |
| **worth** (adjective) | [Oxford worth](https://www.oxfordlearnersdictionaries.com/us/definition/english/worth_1), lines 103–115, 132–165 | Predicative, preposition-like **worth** followed by money/value differs from *worth doing* and noun *worth*. Cambridge index labels monetary adjective B1 versus draft A2; direct Cambridge page HTTP 403. |

**Three provisional CEFR conflicts** (pretty, due, worth) need independent exact-sense assessment. They are **not automatic level changes**. Oxford dictionary topic labels, unrelated Oxford footer word-list labels and Cambridge indexed snippets must not be converted into independent publisher exact-sense CEFR approval. No publisher quotation is copied into the teaching dataset.

## Mechanical release safeguards

- [Source-bound auditor](tools/audit_cefr_1000_a2_uk_sense_eight.py) pins the research packet and original shortlist Git blobs, checks all eight historical bilingual/example/provenance snapshots, validates exact URLs and dated observations, and rejects injected approval/listening fields and altered frozen flags.
- [Parallel six-lane structural QA](.github/workflows/cefr-1000-selection-structural-qa.yml) now invokes the auditor for A1/A2/B1/B2/C1/ALL, with adversarial self-tests in ALL. [Documentary no-deployment QC](.github/workflows/cefr-1000-go-live-qc-gate.yml) also invokes adversarial self-tests.
- Research packet commit `8cca0e48fec60beaa2e31b96596d5c5a48caa915`; corrected audit commit `8ce3d28497268627467178b1d5c48eedfe6c5085`; structural workflow commit `2c70c55105c4f7476b5ece78987447e0ec70eff9`; documentary workflow commit `35bbce787e72d8c11d611bb0353c2c4015713896`.
- **CI status: NOT VERIFIED for these new commits.** The GitHub connector's commit-run lookup is limited to PR-triggered runs and returned no push run IDs; combined commit statuses were empty. Do not report successful runs or mutation counts until actual job conclusions/logs are retrieved. Earlier runs do not certify this new code.
- Comparison from previous checkpoint `a99a5be8acaeb8d350a50126ec0453ad904f6151` to the staging branch found **five commits and four changed paths only**: this research packet, auditor, and two staging QA workflows. No protected production asset was changed in this comparison.

## Unchanged release blockers

First-pass written/independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Oxford word/POS observation coverage previously reported **995/1,000**, which is not independently approved evidence. Final George/Emma actual listening signoffs **0/1,000**. Independent human English/Myanmar/example/exact-sense CEFR approval, deduplicated approved release manifest, both British voices for headwords and examples with real listening, desktop/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting readiness and confirmed production deployment remain missing.

**No merge, no main change, no publication.** Keep the existing 54 lessons, separate IELTS 1,000-word bank, production George/Emma audio and privacy assets protected.
