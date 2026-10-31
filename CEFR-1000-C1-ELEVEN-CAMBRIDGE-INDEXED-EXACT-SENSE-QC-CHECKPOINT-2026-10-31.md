# CEFR 1000 — eleven C1 Cambridge indexed exact-sense triage leads (2026-10-31)

**Status: STAGING ONLY / EDITORIAL HOLD.** Approved scope is 1,000 total (A1–C1, 200 each), not the obsolete 5,000 plan. This research neither independently approves any word nor permits a merge, production write or deployment. Branch: `cefr-5000-bilingual-qa-staging`.

## Source and evidence boundaries

On **2026-10-31**, publisher content was examined through publicly indexed Cambridge Dictionary search results. Sampled direct Cambridge page requests returned **HTTP 403**. Publisher labels below are labels visible in those search-index extracts for the stated senses; they are **not** independent human review, and an absent indexed badge is **not** evidence that Cambridge has no CEFR classification. Do not treat indexed labels as direct Oxford word/POS coverage. Frozen shortlist source and historical Git blob provenance, original English/Myanmar/example snapshots, publisher URL, observation date, evidence scope, and unapproved editorial alternatives are recorded in [the eleven-record research packet](draft/CEFR-1000-CAMBRIDGE-C1-ELEVEN-INDEXED-EXACT-SENSE-RISKS-2026-10-31.json).

| Draft C1 word | Cambridge indexed label | Specific editorial issue requiring independent review |
|---|---|---|
| custody (noun) | **C2** | Child guardianship and detention are separate senses; draft definition conflates them while example uses guardianship. [Publisher](https://dictionary.cambridge.org/dictionary/english/custody) |
| fluid (noun) | **C2** | Countable/uncountable flowing substance; C1 draft placement needs independent sense-backed adjudication. [Publisher](https://dictionary.cambridge.org/dictionary/english/fluid) |
| diagnosis (noun) | **C2** | Medical/problem identification; irregular plural **diagnoses**, not *diagnosises*. [Publisher](https://dictionary.cambridge.org/dictionary/english/diagnosis) |
| interpretation (noun) | **C2** | Explanation/opinion sense, distinct from artistic performance; countable/uncountable. [Publisher](https://dictionary.cambridge.org/dictionary/english/interpretation) |
| excess (noun) | **C1** | **Confirmed draft POS/example mismatch**: definition is noun, but “excess material” uses *excess* as an adjective. Replace with a noun example only after independent review. [Publisher](https://dictionary.cambridge.org/dictionary/english/excess) |
| privilege (noun) | **C1** | Special advantage, enjoyable opportunity and legal privilege are different uses. [Publisher](https://dictionary.cambridge.org/dictionary/english/privilege) |
| charter (noun) | No badge visible | Formal document versus hiring a vehicle; the latter is a different sense. [Publisher](https://dictionary.cambridge.org/dictionary/english/charter) |
| operational (adjective) | No badge visible | Activity-related adjective versus working/fully operational state. [Publisher](https://dictionary.cambridge.org/dictionary/english/operational) |
| copyright (noun) | No badge visible | Legal-right noun versus adjective and verb; do not infer CEFR from absence of badge. [Publisher](https://dictionary.cambridge.org/dictionary/english/copyright) |
| asset (noun) | No badge visible | Draft definition includes owned property; draft example concerns a useful person/quality. Sense should be aligned. [Publisher](https://dictionary.cambridge.org/dictionary/english/asset) |
| regulatory (adjective) | No badge visible | Business/official-rule oversight sense; distinguish statutory requirements. [Publisher](https://dictionary.cambridge.org/dictionary/english/regulatory) |

**Publisher-indexed badge distribution:** four C2, two C1, five not visible. All eleven remain unapproved and on editorial hold. Candidate Myanmar rewrites and original examples in the packet are editorial proposals only; they have not been signed off by an independent bilingual reviewer.

## Audit and CI

New fail-closed script: [`tools/audit_cefr_1000_cambridge_c1_eleven_exact_sense.py`](tools/audit_cefr_1000_cambridge_c1_eleven_exact_sense.py). It binds the exact source packet and frozen 1,000-word shortlist to Git blob SHAs, checks 200 words per level, deduplicated headwords, immutable original English/Myanmar/examples and historical provenance, publisher source/sense/CEFR observations, unapproved candidate status and zero independent/audio/production receipts. Its adversarial self-test mutates source claims, labels, sense tags, Myanmar text, source provenance and false review approvals; a passing structural test **does not** certify linguistic accuracy or human approval.

Wired to all six parallel A1/A2/B1/B2/C1/ALL structural GitHub Actions lanes and the documentary no-deployment gate. Workflow changes are confined to staging; both workflows report blockers rather than publish. **Run conclusions must be checked separately before marking CI verified.**

## Honest readiness ledger

| CEFR level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Direct Oxford word/POS observations remain **A1 195, A2 168, B1 200, B2 166, C1 111 = 840/1,000**; 160 lack direct Oxford observations. Cambridge indexed leads do not change that metric. Final George/Emma actual listening signoffs remain **0/1,000**. Approved manifest, independent English/Myanmar/example/exact-sense CEFR human signoff, final headword-and-example audio/listening, browser/mobile and physical iPhone Safari regression, measured GitHub Pages hosting, preserved production asset verification and confirmed live deployment are missing. **NO MERGE / NO MAIN CHANGE / NO PUBLICATION.**

## Verified GitHub Actions results (2026-10-31)

- [Structural run 41182548288](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41182548288) **SUCCESS**, actual job conclusions **A1/A2/B1/B2/C1/ALL all SUCCESS**; ALL job `124482740091`, artifact `13034679533`.
- [Documentary no-deployment run 41182548296](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41182548296) **SUCCESS (report-only, not release-ready)**; job `124482739476`, blocker artifact `13035672235`.
- Both verified runs tested **code SHA `f59d1dd078490fc59436c1e442bef3972fa4dc73`**. Actual ALL and documentary job logs each show **260/260 adversarial source, sense, Myanmar, provenance and false-review mutations rejected**, and protected production assets unchanged.
- The auditor now validates actual historical source blob `b04dd85db5cfae131c25aa4c73109778991b6fdc` and all eleven source indices against the frozen bilingual snapshots, not just the declared provenance fields. An intermediate CI failure exposed a `burmese_meaning` (original source) versus `myanmar_meaning` (research packet) key mapping error; fixed before the final successful runs. The three Myanmar editorial candidates for *fluid*, *diagnosis* and *interpretation* were also refined and remain unapproved.
- Documentary logs still explicitly block missing independently approved 1,000-entry manifest, all independent stage signoffs, final George/Emma actual listening receipts, matched browser/mobile tests, physical iPhone Safari, measured GitHub Pages hosting, final production-preservation evidence and formal release approval. **A successful documentary job is a successful blocker report, NOT permission to launch.**
