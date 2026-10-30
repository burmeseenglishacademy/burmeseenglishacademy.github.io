# CEFR 1,000 — B1 eleventh Oxford source and exact-sense triage (30 October 2026)

**Staging only:** branch `cefr-5000-bilingual-qa-staging`. Scope is 1,000 total: 200 A1, 200 A2, 200 B1, 200 B2, 200 C1. This is **research**, not human-independent approval. The provisional shortlist and review flags remain frozen, and neither production nor the separate IELTS bank is modified.

## Twelve previously unobserved B1-draft word/POS leads

| B1 draft | Oxford word/POS list level | Publisher evidence |
|---|---|---|
| foundation (noun) | B2 | Oxford 5000 CEFR PDF, page 2, extracted line 265 |
| gain (verb) | B2 | Oxford 3000 CEFR PDF, page 11, line 2886 |
| influence (verb) | B1 | Oxford 3000 CEFR PDF, page 8, line 2148 |
| improve (verb) | A1 | Oxford 3000 CEFR PDF, page 2, line 393 |
| prevent (verb) | A2 | Oxford 3000 CEFR PDF, page 6, line 1495 |
| advantage (noun) | A2 | Oxford 3000 CEFR PDF, page 4, line 920 |
| aware (adjective) | B1 | Oxford 3000 CEFR PDF, page 7, line 1837 |
| decide (verb) | A1 | Oxford 3000 CEFR PDF, page 1, line 198 |
| progress (noun) | A2 | Oxford 3000 CEFR PDF, page 6, line 1506 |
| concept (noun) | B2 | Oxford 3000 CEFR PDF, page 10, line 2711 |
| academic (adjective) | B1 | Oxford 3000 CEFR PDF, page 7, line 1784 |
| accurate (adjective) | B2 | Oxford 3000 CEFR PDF, page 10, line 2599 |

Publisher source PDFs: [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf), directly inspected 2026-10-30. This batch has **4 publisher-higher, 5 publisher-lower, 3 matching word/POS labels**; nine provisional-level discrepancies require independent exact-sense reconciliation.

## Four directly opened dictionary sense leads

1. **foundation**: [Oxford noun, sense 4](https://www.oxfordlearnersdictionaries.com/definition/english/foundation) (page-text lines 170–180) means the physical structural base of a building, normally plural *foundations*. The dictionary's **Buildings c1** is a topic badge, not evidence that the Oxford 5000 headword is C1. Original B1-draft singular wording and the unapproved alternative require a fluent Myanmar and example review.
2. **gain**: [Oxford verb, sense 3](https://www.oxfordlearnersdictionaries.com/definition/english/gain_1) (lines 181–192) supports gradually gaining confidence. The distinction from winning access, influence or prizes matters.
3. **influence**: [Oxford verb, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/influence_2) (lines 112–128) describes affecting a person's behaviour or thinking; the frozen example about friends influencing choices fits this transitive sense.
4. **concept**: [Oxford noun, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/concept) (lines 119–145) is an abstract idea/principle; a teaching example differs from the product/design proposal sense.

The [12-record source packet](draft/CEFR-1000-OXFORD-B1-ELEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json) preserves original English/Myanmar/example text, historical Git path/index/blob, publisher PDF URL/date/page/line/word/POS, four dictionary page/line locators, sense and grammar risks, and four original **unapproved** bilingual/example alternatives. The [fail-closed source auditor](tools/audit_cefr_1000_oxford_b1_eleventh_twelve.py) binds this packet to the frozen shortlist and rejects fabricated publisher labels, altered Myanmar/example/provenance, false human signoff and tampered dictionary leads; it is wired into six parallel CEFR structural lanes and report-only launch QC.

## Updated editorial coverage — subject to successful CI reconciliation

Direct Oxford word/POS observations should reconcile to **A1 195/200, A2 120/200, B1 144/200, B2 130/200, C1 111/200 = 700/1,000 distinct**, with 300 unobserved; 719 observations including historical duplicates. Expected reviewer queue: **3 unlisted (not a CEFR label), 40 publisher-higher, 244 publisher-lower, 413 matching word/POS requiring exact-sense verification, 300 unobserved**. These are **research classifications only**, not independently approved.

First-pass written / independently approved remains **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Real final George/Emma headword-and-example listening signoffs remain **0/1,000**. Human-independent English/Myanmar/example and source-backed CEFR review, final dual-voice audio/listening, browser/mobile regression, physical iPhone Safari, measured GitHub Pages hosting, protected-assets/privacy signoff and confirmed production deployment are outstanding. **Release BLOCKED / STAGING ONLY**; no merge, main modification or publication.

GitHub Actions results must be recorded only after actual job conclusions and logs are inspected; passing structural/documentary CI never constitutes independent language, audio or device signoff.
