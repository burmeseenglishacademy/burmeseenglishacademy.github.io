# CEFR 1,000 — A2 fifteenth Oxford batch, 31 October 2026

**STAGING ONLY — NO HUMAN-INDEPENDENT APPROVAL, AUDIO LISTENING, IPHONE QA, MERGE OR PUBLICATION.** Scope is exactly **1,000** first-pass draft entries: **200 each A1/A2/B1/B2/C1**, not the superseded 5,000-word proposal. Branch: `cefr-5000-bilingual-qa-staging`. Frozen shortlist and independent-review task files remain unchanged.

## Direct source observations and editorial limits

Official publisher [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) inspected **2026-10-31**; page numbers are **1-based**, extracted line numbers are those of the web text extraction (0-based). All twelve entries were previously unobserved in the direct Oxford batch ledger.

| Draft A2 word/POS | Publisher word/POS level | Official PDF page / extracted line | Exact publisher line |
|---|---|---|---|
| similar / adjective | A1 | 3 / 697 | `similar adj.` |
| common / adjective | A1 | 1 / 164 | `common adj.` |
| likely / adjective | A2 | 5 / 1362 | `likely adj.` |
| fine / adjective | A1 | 2 / 290 | `fine adj.` |
| couple / noun | A2 | 4 / 1088 | `couple n.` |
| online / adverb | A1 | 3 / 552 | `online adj., adv.` |
| return / verb | A1 | 3 / 651 | `return v., n.` |
| wish / verb | A2 | 7 / 1769 | `wish v., n.` |
| finally / adverb | A2 | 5 / 1213 | `finally adv.` |
| guess / verb | A1 | 2 / 342 | `guess v., n.` |
| gold / noun | A2 | 5 / 1250 | `gold n., adj.` |
| middle / noun | A2 | 6 / 1396 | `middle n., adj.` |

**Six A1 word/POS classifications conflict with provisional A2 placement; six A2 classifications match.** This is a publisher **word/POS comparison**, NOT a source-backed exact-sense CEFR decision and not independent review. Source excerpts, dates, URLs, frozen English/Myanmar/example snapshots, historical Git source paths/indices/blob SHAs, editorial risks and reviewer holds are in [the 12-record packet](draft/CEFR-1000-OXFORD-A2-FIFTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json).

Four publisher dictionary pages were directly inspected on **2026-10-31**, solely as sense leads:

- [fine adjective](https://www.oxfordlearnersdictionaries.com/definition/english/fine_1), **sense 3, lines 178–185**: accepting an action or decision. Draft English defines acceptable/good enough, but its weather example concerns a *different sense*. Editorial alternative (not approved): “The suggested meeting time is fine with everyone.”
- [couple noun](https://www.oxfordlearnersdictionaries.com/definition/english/couple_1), **sense 2, lines 103–126**: `a couple of friends` may denote a small number, not strictly two. The original draft definition is too narrow for its example; romantic couple is another sense. Editorial alternative (not approved): “A couple of volunteers stayed behind to tidy the hall.”
- [online adverb](https://www.oxfordlearnersdictionaries.com/definition/english/online_2), **sense 1, lines 88–119**: internet-mediated action, not online adjective or system-operation sense. Editorial alternative (not approved): “You can submit the application online.”
- [wish verb](https://www.oxfordlearnersdictionaries.com/definition/english/wish_1), **sense 1, lines 114–129**: unreal or unlikely desire with past-form clause or `could`; distinguish formal `wish to` and greetings. Editorial alternative (not approved): “I wish I had more time to practise English.”

Fluent Myanmar rewrite proposals remain unapproved in the packet. The dictionary's unrelated **Word of the Day** footer is never a CEFR label for the inspected entry. No assistant self-evaluation may mark independent-review flags true.

## Structural QC and reviewer handoff

New [fail-closed source auditor](tools/audit_cefr_1000_oxford_a2_fifteenth_twelve.py) pins the packet's Git blob SHA, shortlist blob SHA, publisher URL, exact word/POS, source level, PDF page/line, snapshot, source provenance and false-signoff guards. The six parallel CEFR structural jobs and documentary no-deploy job now invoke the auditor. CI conclusions must be checked from actual GitHub Actions jobs/logs; code changes alone are **not** a successful CI claim.

Expected cross-batch direct Oxford word/POS coverage after this batch: **A1 195/200, A2 168/200, B1 200/200, B2 166/200, C1 111/200 = 840/1,000 distinct**; **859** total source observations and **160** entries without direct Oxford observations. Reviewer priority expectations: **3 unlisted (not CEFR evidence), 52 publisher-higher, 330 publisher-lower, 455 matching word/POS but exact-sense-unverified, 160 without direct observation**. These are source triage categories, not human approval.

| CEFR draft level | First-pass written | Independently approved | Final George/Emma real listening signoffs |
|---|---:|---:|---:|
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

**Release blocked** pending signed independent exact-sense CEFR, English, fluent Myanmar, original-example and pronunciation review; approved-manifest deduplication (200 each); final George/Emma headword+example audio generated and actually listened to; approved-corpus browser/mobile regression and real physical iPhone Safari evidence; measured GitHub Pages limits; confirmed deployment and preservation of 54 lessons, separate IELTS 1,000 bank, existing production audio and privacy. No production action is authorised until every gate is evidenced.
