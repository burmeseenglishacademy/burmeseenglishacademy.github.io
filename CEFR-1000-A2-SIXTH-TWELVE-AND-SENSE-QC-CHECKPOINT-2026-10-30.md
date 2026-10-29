# CEFR 1,000 — sixth A2 Oxford twelve and two exact-sense research leads (30 October 2026)

**STAGING ONLY / RELEASE BLOCKED.** The user-approved scope is exactly **1,000 total** (A1 200, A2 200, B1 200, B2 200, C1 200), not the superseded 5,000. Work is confined to `cefr-5000-bilingual-qa-staging`; the branch name is deliberately unchanged. Frozen shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`). All entries remain on editorial hold, with **zero independent approvals**.

## New directly observed Oxford word/POS research

The [official Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) was directly inspected on **2026-10-30**. The twelve new, previously unobserved A2-draft entries are:

| Draft A2 word | Oxford PDF word/POS level | Source PDF page / extracted line (1-based / 0-based) | Independent editorial priority |
|---|---|---|---|
| human | A2 | 5 / 1288 | Adjective versus noun; human vs machine/animal |
| special | A1 | 3 / 728 | Unusual vs important vs particular-purpose |
| either | A2 | 5 / 1156 | Determiner before singular noun, not conjunction |
| rather | A2 | 6 / 1526 | Degree adverb, not preference |
| real | A1 | 3 / 641 | Authentic dinosaur bone vs merely existing |
| set | B1 | 9 / 2419 | Oxford specifically lists **set (put) v.**, higher than draft A2 |
| thought | A2 | 7 / 1704 | Countable noun vs past-tense verb |
| bad | A1 | 1 / 57 | Weather vs poor quality/morality |
| mean | A1 | 2 / 472 | Signify a warning sign vs intend |
| though | B1 | 10 / 2507 | Concessive conjunction and British collective grammar |
| least | A2 | 5 / 1352 | The least effort vs at least |
| news | A1 | 2 / 517 | Uncountable noun and recent-information sense |

**Source breakdown:** five Oxford A1 labels, five A2 labels, two B1 labels; **seven draft-versus-publisher word/POS level discrepancies**. This is word/POS evidence, **not independent exact-sense CEFR approval**. All 12 records preserve original English definition, fluent-Myanmar review target, original example, historical source path/index/Git blob, dated publisher URL, PDF page/line, and explicit pending independent reviewer task in [the research packet](draft/CEFR-1000-OXFORD-A2-SIXTH-TWELVE-2026-10-30.json). No shortlist content or approval flags were changed.

## Direct-sense and cross-publisher leads

The separate [two-entry sense triage](draft/CEFR-1000-A2-SIXTH-SENSE-TRIAGE-2026-10-30.json) preserves original snapshots/provenance and unresolved independent tasks.

- **set:** Directly read [Oxford Advanced Learner's Dictionary, set verb](https://www.oxfordlearnersdictionaries.com/us/definition/english/set_1) on 2026-10-30, *put/start*, numbered **sense 8**, web lines 182–189. The placement meaning matches the draft example about setting cups on a table. The Oxford 3000 PDF puts the **set (put)** verb at **B1**, not the draft A2. The dictionary page does **not** give a separately verified CEFR label for sense 8; a B1 topic label elsewhere on that page belongs to a different sense. Do not transplant it or automatically retier.
- **news:** Cambridge Dictionary's [publisher-indexed news entry](https://dictionary.cambridge.org/dictionary/english/news), observed 2026-10-30, distinguishes **A2** recent-event information from **B1** the radio/TV news programme. Its full page returned **HTTP 403**, so these are publisher-indexed sense leads, **not completed direct-page confirmation**. Oxford 3000 lists news n. at **A1**. The draft example *heard the news on the radio* may be ambiguous between information and a programme; independent source-backed sense selection and Myanmar/example review are needed. Cambridge's [news grammar guidance](https://dictionary.cambridge.org/grammar/british-grammar/news) describes uncountable news with singular agreement; this is a grammar lead, not a CEFR verdict.

## Reconciled research and review handoff

| Draft level | First-pass written | Distinct direct Oxford word/POS observations | Independently approved |
|---|---:|---:|---:|
| A1 | 200 | 172 | 0 |
| A2 | 200 | **84** | 0 |
| B1 | 200 | 84 | 0 |
| B2 | 200 | 70 | 0 |
| C1 | 200 | 51 | 0 |
| **Total** | **1,000** | **461** | **0** |

The audited packets now hold **480 observations for 461 distinct words** (19 repeat observations, not extra coverage); **539** lack a direct Oxford word/POS observation. Reviewer priorities: **157 publisher-lower**, **15 publisher-higher**, **3 absent from inspected core PDFs (not CEFR levels)**, **286 matching word/POS but exact-sense-unverified**, **539 unobserved**. All 1,000 remain pending independent English/Myanmar/example/exact-sense and pronunciation review.

## Executed staging-only CI (no deployment)

- [Six parallel structural lanes — run **40917002738**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40917002738): **SUCCESS**, all **A1/A2/B1/B2/C1/ALL** job conclusions checked. Actual ALL-job logs show **306/306** new sixth-A2 forged Oxford, bilingual, historical provenance and fake-review mutations rejected, **145/145** reviewer-handoff mutations rejected, and the reconciled **461 / 539** counts. A source-bound, **unapproved** 1,000-item reviewer handoff artifact was generated. The tests do **not** represent human signoff.
- [Documentary go-live gate — run **40917002780**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40917002780): **SUCCESS as report-only**, actual logs retain zero independent review, zero real both-voice listening, missing approved manifest, iPhone/hosting/production evidence and release **BLOCKED**. Protected production diff check passed.
- Both verified runs used staging code commit **`04f4a7ed58946e2c7d9b7413e2ab47a7439d0fd7`**, following initial research/integration commit **`8d505b9693e6dfbe98e704bc4d988eef88b6e148`**. The separate two-sense triage was subsequently committed as **`f360d7fd3d740241118713197a2acc7f263f6cf0`**; it is **not** itself a human-approved source receipt or part of the preceding verified CI head.

## Fail-closed release blockers

First-pass written / independently checked remain **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Full British **George and Emma** headword and example audio **real listening signoffs remain 0/1,000**. Independent linguistic and CEFR signoffs, final audio generation/listening, approved-corpus browser/mobile regression, **physical iPhone Safari** review, measured GitHub Pages hosting limits, approved release manifest and confirmed live production deployment are missing. Preserve the **54 lessons**, separate **IELTS 1,000-word bank**, established George/Emma production audio and privacy. **NO MERGE, MAIN MODIFICATION, PUBLICATION OR DEPLOYMENT. STAGING ONLY.**
