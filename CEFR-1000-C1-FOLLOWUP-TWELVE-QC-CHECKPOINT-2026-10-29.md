# CEFR 1,000 — C1 follow-up Oxford/Cambridge evidence and fail-closed QC (29 October 2026)

**BLOCKED / STAGING ONLY.** User-approved scope remains **1,000 total**: A1/A2/B1/B2/C1 **200 each**, not the superseded 5,000-word plan. All **1,000** provisional entries are on editorial hold; **zero** human-independently approved. This report is not human signoff, audio listening, physical iPhone testing, or release authorisation.

## Direct Oxford publisher observations (2026-10-29)

Directly inspected Oxford University Press's [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) and [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf). Machine-readable [source packet](draft/CEFR-1000-OXFORD-C1-FOLLOWUP-TWELVE-2026-10-29.json) preserves original English/Myanmar/example snapshots, original Git source path/index/blob, publisher URL, observation date, PDF page (one-based), web extracted line (zero-based), exact short word/POS excerpt, editorial risks and independent review tasks. Frozen shortlist Git blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

| C1 provisional word | Oxford word/POS | PDF page:line | Main editorial concern |
|---|---|---|---|
| tribute | C1 noun | 8:1938 | Respectful action versus other tribute senses |
| trigger | **B2 verb** | 3:659 | Lower Oxford level; ordinary causation |
| racism | **B2 noun** | 2:503 | Definition narrows prejudice/discrimination to unfair treatment |
| signature | **B2 noun** | 3:569 | Handwritten versus electronic signature |
| abortion | C1 noun | 3:706 | Neutral, medically precise induced-pregnancy-termination wording |
| consistently | **B2 adverb** | 1:121 | Consistency versus an unqualified "always" |
| conversion | C1 noun | 4:988 | Building repurposing versus religion, currency, units |
| copyright | C1 noun | 4:999 | Copyright ownership versus physical copy ownership |
| diverse | **B2 adjective** | 1:185 | Ordinary group variety does not by itself justify C1 |
| exclusively | C1 adverb | 5:1188 | "Only" versus "for a special purpose" |
| functional | C1 adjective | 5:1241 | Draft definition implies design purpose; example describes operational condition |
| divine | **Not found** in either inspected Oxford core list | none | No Oxford word/POS CEFR label; absence proves no level |

**Result: 6 C1 word/POS matches, 5 B2 conflicts, 1 unlisted.** These are publisher word/POS observations, **not exact-sense CEFR verification**, fluent Myanmar signoff or independent approvals. No automatic retiering.

## Four Cambridge exact-sense leads — search-index evidence only

On 2026-10-29, retrieved publisher-owned indexed excerpts. Direct Cambridge dictionary pages returned **HTTP 403**; do not represent the excerpts as direct-page verification or independent signoff.

- [tribute — RESPECTFUL ACTION](https://dictionary.cambridge.org/us/dictionary/english/tribute): Cambridge Advanced Learner's Dictionary search excerpt labels the intended respect sense **C2**, in tension with Oxford's C1 word/POS listing. Independent C1 sense-level teaching rationale is essential.
- [functional — PRACTICAL](https://dictionary.cambridge.org/dictionary/learner-english/functional): Cambridge Learner's Dictionary indexed the practical-design sense at **B2**. Its separate **WORKING** sense was indexed without a visible CEFR label; the draft definition resembles PRACTICAL while its example illustrates WORKING.
- [divine — GOD-LIKE](https://dictionary.cambridge.org/dictionary/english/divine): Cambridge indexed the religious adjective without a visible CEFR label, distinct from the SPLENDID adjective and GUESS verb. Neither this lead nor absence from Oxford supports an automatic C1 classification.

Three original bilingual/editorial rewrites are recorded as **unreviewed, unapplied proposals** (functional, consistently, racism); all existing shortlist wording and review flags remain unchanged.

## Safeguards and CI

Added `tools/audit_cefr_1000_oxford_c1_followup_twelve.py` to verify 12 fixed publisher observations, immutable bilingual/example snapshots, original Git source blobs and indices, 200-per-level held shortlist, Cambridge indexed source/access caveats, and zero approvals. Its negative suite rejects **209 authored mutations** of source/CEFR/locators, Myanmar/English/examples, historical provenance, Cambridge leads and forged reviewer flags; this is **mechanical integrity checking only**.

Integrated the audit into all six parallel **A1/A2/B1/B2/C1/ALL** GitHub Actions structural lanes and the documentary no-deployment workflow. Strengthened the release-readiness gate and added an empty `oxford_c1_followup_twelve_review_receipts` ledger: retained entries require actual independent content-hash-bound English/Myanmar/example and exact-sense C1 review; the five lower Oxford observations need substantive reconciliation, and the unlisted adjective needs a source beyond the two Oxford core-list PDFs. A fabricated receipt is rejected in gate self-test. The first CI attempt failed on an auditor field-name mismatch (`burmese_meaning` versus packet `myanmar_meaning`); staging commit `be08a4003a16d00ff34cad19fe398e295d6f4a7f` corrected it. Do not claim the failed run passed.

**Verified CI:** [parallel structural run 40766310977](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40766310977), head `4152274af88b4aafc58ae502f9d5e337f0dc9b17`, completed **SUCCESS**. All six A1/A2/B1/B2/C1/ALL jobs individually concluded **success**. Actual ALL job `123091280578` logs confirm **209/209** forged Oxford/Cambridge publisher, bilingual, provenance and reviewer mutations rejected and protected-production diff **PASS**. [Documentary no-deployment run 40766310871](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40766310871), same head, completed **SUCCESS as report-only**; actual job `123091281124` logs confirm **209/209** rejected, fabricated C1 follow-up receipt rejected, `source-reviewed 0/1000`, `both-voice listening 0/1000`, `actual production confirmed False`, missing physical iPhone Safari evidence and protected production diff **PASS**. No deploy. The initial run `40766052534` **failed** because the auditor mistakenly used `myanmar_meaning` to read the source's `burmese_meaning`; staging commit `be08a4003a16d00ff34cad19fe398e295d6f4a7f` repaired it. A successful structural or documentary CI job is **not** human-independent review, listening, device QA, hosting approval or launch confirmation.

## Exact release blockers

| CEFR | First-pass written | Human-independently checked and approved | Held |
|---|---:|---:|---:|
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |
| **Total** | **1,000** | **0** | **1,000** |

Final British George/Emma headword-and-example **real listening receipts: 0/1,000**. No claim that all 4,000 final voice clips exist or were listened to. Missing human-independent English/Myanmar/example/exact-sense CEFR signoffs; complete final voice/audio QC; desktop/mobile regression; **physical iPhone Safari** evidence; measured GitHub Pages size/bandwidth; confirmed production deployment. Existing 54 lessons, separate IELTS 1,000-word bank, established George/Emma production audio, privacy and main branch are protected; no merge or publication. **Release remains BLOCKED / STAGING ONLY.**
