# CEFR 1,000 — B1 fourteenth Oxford source and four sense leads (31 October 2026)

**STAGING ONLY — NO INDEPENDENT APPROVAL — NO DEPLOYMENT.** Scope is the user-approved **1,000 total** (A1/A2/B1/B2/C1 = 200 each), not the superseded 5,000-word project. Work was confined to `cefr-5000-bilingual-qa-staging`.

## Direct publisher observations and exact-sense limitations

On **2026-10-31**, directly inspected Oxford University Press's official [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf). All 12 entries were previously without a direct Oxford word/POS observation in the cross-batch source auditor. These are **publisher word/POS or word-form leads, NOT independently approved CEFR levels for the draft's exact senses**.

| Draft B1 word | Oxford reference | PDF page / extracted line | Editorial action for independent human reviewer |
|---|---|---|---|
| brand (noun) | B1, `brand n., v.` | 7 / 1863 | Product identity, not figurative type or verb; confirm brand-vs-brand-name Myanmar nuance |
| cent (noun) | A1, `cent n.` | 1 / 135 | B1 draft above publisher word/POS; confirm currency definition |
| count (verb) | A2, `count v.` | 4 / 1087 | Distinguish counting objects from `count on` or `count as` |
| fourth (draft *ordinal adjective*) | A1, `fourth number` | 2 / 311 | **Explicit POS conflict:** Oxford calls this an ordinal number; no exact-POS equivalence established |
| mental (adjective) | B1, `mental adj.` | 9 / 2212 | Mind/thinking sense, appropriate register and non-stigmatising usage |
| mostly (adverb) | A2, `mostly adv.` | 6 / 1405 | Mainly, not entirely |
| owner (noun) | A2, `owner n.` | 6 / 1446 | Ownership rather than management |
| previously (adverb) | B1, `previously adv.` | 9 / 2318 | Earlier time, distinguish adjective `previous` |
| realize (verb) | A2, `realize v.` | 6 / 1529 | Awareness sense, not achieving ambitions; British `realise` is also valid |
| click (verb) | B1, `click v., n.` | 7 / 1899 | Computer-interface action, not clicking sound |
| faith (noun) | B2, `faith n.` | 11 / 2849 | Uncountable trust in a team's ability, not religious belief |
| fashion (noun) | A2, `fashion n.` | 5 / 1201 | Clothing styles, not a manner of doing something |

Publisher word/POS level counts: **A1 2, A2 5, B1 4, B2 1**. Against draft B1, **8 placement discrepancies**, with the `fourth` POS mismatch separately and prominently flagged. The source's PDF page numbers are 1-based; extracted line indices are from the directly inspected PDF text.

Four directly inspected dictionary headword pages further constrain exact senses:

- [brand noun](https://www.oxfordlearnersdictionaries.com/definition/english/brand_1), sense 1, page-text lines 105–124: company product/service identity.
- [fourth ordinal number](https://www.oxfordlearnersdictionaries.com/definition/english/fourth_1), page-text lines 88–113: fourth floor example is grammatical, but the draft's *ordinal adjective* POS requires editorial reconciliation.
- [realize verb](https://www.oxfordlearnersdictionaries.com/definition/english/realize), sense 1, page-text lines 107–132: become aware of a fact; British spelling `realise` also accepted.
- [faith noun](https://www.oxfordlearnersdictionaries.com/definition/english/faith_1), sense 1, page-text lines 105–114: uncountable confidence in somebody's ability. Oxford's religion topic label and unrelated Word of the Day footer must not be treated as the intended sense's CEFR label.

The [12-record research packet](draft/CEFR-1000-OXFORD-B1-FOURTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json) retains original English definitions, fluent-Myanmar first-pass snapshots, original examples, source path/index/Git blob provenance, publisher URLs/date/page/line/excerpt, all 12 editorial risks and four **unapproved** Myanmar/example rewrite candidates. No frozen shortlist, independent-review receipt or approval flag was changed.

## Automated safeguards and actual GitHub Actions evidence

Added [source-bound fail-closed auditor](tools/audit_cefr_1000_oxford_b1_fourteenth_twelve.py) to all six parallel structural lanes and documentary no-deployment QC, with explicit trigger paths. It pins the frozen shortlist Git blob and research packet Git blob, verifies every source locator, publisher level, bilingual/example snapshot and historical provenance, and rejects fabricated approval/receipts, altered sense leads and unapproved proposal changes.

**Verified actual Actions run conclusions and logs** for code SHA `d7438efbf6a6fd0fdd19d715fca048dd9b9620fb`:

- [Structural run 41163678055](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41163678055): **SUCCESS** for **A1, A2, B1, B2, C1, ALL**. ALL job `124426516224` explicitly logged **333/333 forged mutations rejected** by the new B1 auditor. ALL artifact ID `13028305378`.
- [Documentary run 41163678104](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41163678104): **SUCCESS**, **report-only, never deploy**. Documentary job `124426516384` explicitly logged **333/333 forged mutations rejected** and release blocked. Blocker artifact ID `13027374346`.
- An intermediate failure at SHA `98662cfae167fb2f51503eb4865f1bd00bd26a34` was traced to a stale hardcoded **796** in the reviewer handoff; corrected to **808** before the successful runs. This was a test-count reconciliation, not an independent review or release event.

Reconciled direct Oxford observations to **A1 195/200, A2 156/200, B1 180/200, B2 166/200, C1 111/200 = 808/1,000 distinct**, **827 total observations**, **192** without direct Oxford word/POS observations. Human exact-sense review priorities: **3 unlisted (not a CEFR label), 47 publisher-higher, 310 publisher-lower, 448 matching word/POS but sense unverified, 192 unobserved**. These are queue categories, not independently verified content.

## Fail-closed release status

First-pass written/independently approved remains **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Final George/Emma headword and example audio generation is not release-verified; **real listening signoffs 0/1,000**. Independent human English/Myanmar/example/CEFR and pronunciation signoff, approved-manifest exact-sense deduplication, approved-corpus browser/mobile regression, **physical iPhone Safari evidence**, measured GitHub Pages hosting readiness, and confirmed live deployment with preserved production assets remain missing.

Git comparison against prior staging head `f7f2469457f5f7049d9fb910c5f4d7476a332667` showed only research packet, auditor, coverage/reviewer scripts and two staging-only QA workflows changed before this checkpoint. No main-branch modification, merge, publication or changes to the protected 54 lessons, separate IELTS 1,000 bank, existing George/Emma production audio or privacy assets.

**RELEASE BLOCKED / STAGING ONLY.**
