# CEFR 1000 — example morphology and repeated-sentence review handoff (1 November 2026)

**STAGING ONLY — NO INDEPENDENT APPROVAL — RELEASE BLOCKED.** This work is exclusively for the user-approved 1,000-entry bilingual CEFR A1–C1 shortlist (200 per level). The superseded 5,000-word proposal is out of scope. The original [frozen shortlist](draft/CEFR-1000-PROVISIONAL-SHORTLIST.json), independent-review tasks, 54 production lessons, separate IELTS 1,000-word bank, existing George/Emma audio and privacy controls remain unchanged.

## Full 1,000-example deterministic scan

An ASCII case-insensitive, word-boundary exact-headword search of **all 1,000 first-pass original examples** found **five examples lacking the literal headword** (A1 2, A2 0, B1 0, B2 3, C1 0). These are **five expected grammatical inflections**, **not five example errors**:

| Draft word / level | Original sentence | Attested form and direct publisher source (opened 2026-11-01) |
| --- | --- | --- |
| **hand / A1** | Please wash your hands. | Plural *hands*, Oxford [hand noun](https://www.oxfordlearnersdictionaries.com/definition/english/hand_1), lines 106–125 |
| **eye / A1** | I have two eyes. | Plural *eyes*, Oxford [eye noun](https://www.oxfordlearnersdictionaries.com/definition/english/eye_1), lines 106–129 |
| **manage / B2** | We managed to finish the work before the deadline. | Past *managed* and *manage to do* success sense, Oxford [manage verb](https://www.oxfordlearnersdictionaries.com/definition/english/manage), lines 103–108, 146–158, 173–178 |
| **destroy / B2** | The fire destroyed the old warehouse. | Past *destroyed*, severe physical damage, Oxford [destroy verb](https://www.oxfordlearnersdictionaries.com/definition/english/destroy), lines 112–125 |
| **grab / B2** | She grabbed her bag and ran outside. | Past *grabbed* (double consonant), sudden physical-taking sense, Oxford [grab verb](https://www.oxfordlearnersdictionaries.com/us/definition/english/grab_1), lines 103–121 |

These publisher observations support **morphology and intended-sense alignment only**. They do not constitute a new Oxford 3000/5000 CEFR classification or independent verification of Myanmar, grammar, pronunciation, or CEFR. Oxford topic badges and unrelated footer labels must not be mistaken for headword/sense CEFR evidence. Cambridge grammar search results were accessible through indexing, but direct opens returned HTTP 403 and were **not counted as directly inspected**.

## Three exact shared-sentence groups: seven held cards

The same complete sentence occurs on multiple cards, with **three groups / seven entries**, all A1. Duplicate sentences are not necessarily incorrect, but can obscure which particular lexical sense or function is being taught.

| Original reused sentence | Frozen cards | Unapproved alternatives for independent reviewer |
| --- | --- | --- |
| The book is on the table. | *the*, *table* | *the*: “The bus is late.” / *table*: “The table has four legs.” |
| What is your name? | *your*, *name*, *what* | *your*: “Your coat is on the chair.” / *name*: “My name is on the list.” / *what*: “What do you want to drink?” |
| Please sit here. | *here*, *sit* | *here*: “Come here, please.” / *sit*: “Please sit on the chair.” |

**These alternatives are editorial proposals, not approved corrections.** A human-independent bilingual reviewer must assess age-appropriate A1 grammar, target sense, fluent Myanmar, British pronunciation and CEFR placement before any replacement. The original examples remain frozen.

## Fail-closed checks and launch blocker status

The [source-bound 5-record/3-group packet](draft/CEFR-1000-EXAMPLE-MORPHOLOGY-AND-SHARED-SENTENCE-TRIAGE-2026-11-01.json) pins original English definitions, Myanmar meanings, examples, historical source paths/indices/Git blobs, publisher URLs, observation date, direct-page locators and unapproved status. The [auditor](tools/audit_cefr_1000_example_morphology_reuse.py) re-scans all 1,000 entries, verifies the frozen Git blob and historical source rows, rejects forged evidence/signoffs and runs adversarial self-tests. It is included in **A1/A2/B1/B2/C1/ALL parallel structural QA** and **documentary-only no-deployment QC**. Passing automated tests cannot count as independent linguistic or listening signoff.

**First-pass written / independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. Oxford core-list observation coverage remains A1 **195/200**, A2 **200/200**, B1 **200/200**, B2 **200/200**, C1 **200/200** — **995/1,000**, including unlisted cases and exact-sense uncertainties. Final George/Emma audio real listening signoffs **0/1,000**. Missing: independent English/Myanmar/example/exact-sense CEFR signoffs; deduplicated approved manifest; full final British dual-voice generation and actual listening; browser/mobile and physical iPhone Safari QA; measured GitHub Pages hosting readiness; confirmed live production deployment and preservation check.

**Do not merge, publish, alter main or claim release.** This checkpoint is a research handoff, not a production launch certificate.

## Verified GitHub Actions results (actual logs, 1 November 2026)

- [Structural run 41254408864](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41254408864): **SUCCESS** for all six parallel jobs **A1/A2/B1/B2/C1/ALL**, testing code SHA `2d2a63fe2b83f5b19283b3cbba5aee685ff292b4`. Actual ALL job log confirmed **199/199** new forged evidence, bilingual, provenance and false-approval mutations rejected, and protected production assets unchanged. ALL artifact ID `13061594634`.
- [Documentary no-deployment run 41254408764](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41254408764): **SUCCESS, report-only**, testing the same code SHA. Actual documentary log independently confirmed **199/199** forged mutations rejected and protected production assets untouched. Blocker-report artifact ID `13062353523`.
- Intermediate structural run `41254366934` failed on a wrong frozen Myanmar field mapping (`myanmar_meaning` vs source `burmese_meaning`); corrected in code commit `2d2a63fe2b83f5b19283b3cbba5aee685ff292b4` and verified by the successful runs above. This is a test repair, not a linguistic approval.

**Launch remains blocked and staging-only.** Successful structural/documentary QA does not establish independent CEFR, English, Myanmar or example review, genuine George/Emma listening, physical iPhone Safari QA, hosting readiness or production deployment.
