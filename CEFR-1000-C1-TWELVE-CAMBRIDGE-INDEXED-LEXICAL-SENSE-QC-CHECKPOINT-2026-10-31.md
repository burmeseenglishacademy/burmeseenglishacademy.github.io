# CEFR 1000 C1: twelve Cambridge lexical sense leads — staging only

Observed: **2026-10-31**. Branch: `cefr-5000-bilingual-qa-staging`. This checkpoint concerns the **user-approved 1,000-total** (200 each A1/A2/B1/B2/C1), not the superseded 5,000-word plan.

## Substantive research and editorial risks

Source-bound [12-record packet](draft/CEFR-1000-CAMBRIDGE-C1-TWELVE-INDEXED-LEXICAL-SENSE-TRIAGE-2026-10-31.json) captures the frozen English definitions, Myanmar meanings, original example sentences and historical source Git paths, indices and blob SHAs. The publisher research leads are Cambridge Dictionary indexed excerpts observed on 2026-10-31. The attempted direct page requests for six sampled Cambridge URLs returned **HTTP 403**. **No CEFR badge was observed in the twelve indexed excerpts. This does not prove Cambridge has no CEFR badge on a full page; it provides NO evidence for independent C1 assignment.** No Oxford direct word/POS coverage increment is claimed.

| Draft C1 headword | Exact-sense, grammar or translation issue for human review |
|---|---|
| ambivalence | simultaneous opposing feelings vs generic indecision; uncountable noun |
| anachronism | historically misplaced object/person vs merely old-fashioned item |
| antipathy | strong dislike, countable/uncountable, `to/towards/between` |
| arbitrate | making a decision on a dispute vs merely mediating; I/T verb |
| belligerent | hostile argumentative person vs formal state-at-war adjective |
| benevolent | kindly person vs charitable organisation use |
| brevity | conciseness of expression vs short duration; uncountable noun |
| circumspect | risk-aware caution vs shyness; formal register |
| coercion | forced action/threats vs ordinary persuasion; uncountable formal noun |
| conundrum | difficult problem vs second riddle/trick-question sense |
| corroborate | additional supporting evidence vs absolute proof; transitive verb |
| credence | uncountable belief; `lend/give credence to`, not personal credibility |

Each entry includes a **separate unapproved** fluent-Myanmar/example proposal; none replaces the frozen shortlist or is represented as independent review. Original example grammar and sense alignment require external human review.

Publisher sources (all accessed through search-index extracts, **not** directly inspected pages):
[ambivalence](https://dictionary.cambridge.org/dictionary/english/ambivalence),
[anachronism](https://dictionary.cambridge.org/dictionary/english/anachronism),
[antipathy](https://dictionary.cambridge.org/dictionary/english/antipathy),
[arbitrate](https://dictionary.cambridge.org/dictionary/english/arbitrate),
[belligerent](https://dictionary.cambridge.org/dictionary/english/belligerent),
[benevolent](https://dictionary.cambridge.org/dictionary/english/benevolent),
[brevity](https://dictionary.cambridge.org/dictionary/english/brevity),
[circumspect](https://dictionary.cambridge.org/dictionary/english/circumspect),
[coercion](https://dictionary.cambridge.org/dictionary/english/coercion),
[conundrum](https://dictionary.cambridge.org/dictionary/english/conundrum),
[corroborate](https://dictionary.cambridge.org/dictionary/english/corroborate),
[credence](https://dictionary.cambridge.org/dictionary/english/credence).

## Fail-closed safeguards and CI verification boundary

Added [auditor](tools/audit_cefr_1000_cambridge_c1_twelve_lexical.py), anchored to the exact Git blob of the source packet and frozen shortlist. It checks all twelve records, source URL/observation dates, lack of observed CEFR badges, original English/Myanmar/examples, historical Git provenance, risk codes, separate unapproved proposals, 200-per-level counts, zero independent approvals and absent audio/release receipts. The adversarial self-test defines **271** source, language, provenance, reviewer and false-approval mutations that must be rejected. Integrated it into all **six parallel A1/A2/B1/B2/C1/ALL structural lanes** and documentary **no-deploy** workflow.

**Verification limit:** GitHub connector confirmed staging commits and the workflow source modifications, but its available commit-to-workflow lookup returned no runs for the new push commits, and current Actions job IDs/logs could not be retrieved. **Do not claim the 271 negative tests passed in GitHub Actions or claim new workflow success** until actual job conclusions and logs are checked. This checkpoint is an implemented, CI-wired safeguard, **not a verified CI result**.

Staging code/workflow head at this checkpoint: `50d71f39ae2c7234736bb44ae15463a50c7d06e8`. Compare from prior staging head `6a1214485af07c657e84265f940008865b11b567`: five commits changed **only** the two workflow files, one research packet and one auditor. No protected production assets were changed.

## Counts and release decision

| Level | First-pass written | Independently checked/approved | Direct Oxford word/POS observations |
|---|---:|---:|---:|
| A1 | 200 | 0 | 195 |
| A2 | 200 | 0 | 168 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 166 |
| C1 | 200 | 0 | 111 |
| **Total** | **1,000** | **0** | **840** |

**160** still lack direct Oxford word/POS observation. Cambridge lexical research does not change those Oxford figures. Final George/Emma headword+example real listening signoffs: **0/1,000**. Final independently approved 1,000-manifest, complete dual-voice audio generation/listening, source-backed exact-sense CEFR and English/Myanmar/example human review, browser/mobile regression, **physical iPhone Safari** evidence, measured GitHub Pages hosting limits, and confirmed production deployment remain missing. Protect 54 lessons, the separate IELTS 1,000-word bank, established George/Emma production audio and privacy.

**RELEASE BLOCKED / STAGING ONLY. No merge, main modification, public launch or fabricated signoff.**
