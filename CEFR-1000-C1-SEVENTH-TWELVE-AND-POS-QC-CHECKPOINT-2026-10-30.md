# CEFR 1000 C1 seventh Oxford research and exact-POS review checkpoint — 30 October 2026

**STAGING ONLY; RELEASE BLOCKED.** The user-approved scope is **1,000 total** (A1, A2, B1, B2, C1: 200 each), not 5,000. All first-pass entries remain on editorial hold and **0/1,000 have genuine independent signoff**. The existing branch name `cefr-5000-bilingual-qa-staging` is retained for compatibility; no main merge, production publication, or protected-asset edits are authorised without all gates.

## Directly observed Oxford publisher evidence

On **2026-10-30**, directly inspected the official [Oxford 5000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf). Its **B2 section precedes the C1 section at extracted line 704** (zero-based), so the provisional C1 adjective **controversial** is publisher **B2 word/POS**, while the other 11 entries are publisher C1 word/POS. The publisher PDF cannot independently certify the exact draft sense, translation, example or voice.

| C1 draft | Oxford PDF page (1-based) / extracted line (0-based) | Publisher word/POS level | Independent editorial decision needed |
|---|---|---|---|
| controversial | 1 / 127 | B2 | Ordinary disagreement sense appears lower than draft C1; independent exact-sense justification or replacement/retiering |
| legendary | 6 / 1401 | C1 | Very famous real person versus mythical/legendary person; Myanmar wording may imply mythology |
| regulatory | 7 / 1684 | C1 | Rules/governance adjective, not regulator noun |
| integration | 5 / 1354 | C1 | Technical systems integration versus social integration |
| legitimate | 6 / 1405 | C1 | Legally permitted versus reasonable/justified; example selects reasonable reason |
| advocate | 3 / 743 | C1 | Verb support/recommend versus advocate noun |
| custody | 4 / 1032 | C1 | Child custody versus police detention; draft definition combines senses |
| excess | 5 / 1185 | C1 | **Critical noun/adjective mismatch in draft example** |
| operational | 6 / 1533 | C1 | Operational processes versus ready/working status |
| syndrome | 7 / 1882 | C1 | Clinical group of symptoms versus figurative usage |
| fluid | 5 / 1225 | C1 | Liquid/gas broad definition versus brake fluid example |
| amateur | 3 / 768 | C1 | **Critical noun/adjective mismatch in draft example** |

The 12 frozen snapshots and historical source path/index/blob SHA, source URLs, observation dates, exact PDF locators and individual independent-review tasks are in [the seventh C1 source packet](draft/CEFR-1000-OXFORD-C1-SEVENTH-TWELVE-2026-10-30.json). No entry was silently corrected or approved.

## Direct Oxford dictionary exact-sense leads

Also directly inspected the [Oxford excess noun](https://www.oxfordlearnersdictionaries.com/definition/english/excess_1) and [excess adjective](https://www.oxfordlearnersdictionaries.com/definition/english/excess_2) entries on 2026-10-30. The provisional example **“The factory recycled the excess material after production.”** uses `excess` before a noun, i.e. an **adjective**, but the entry's frozen POS is **noun**. An unapproved noun-targeted candidate would be: “The factory reduced an excess of raw material.” Verify the naturalness, collocation, Myanmar meaning and exact CEFR sense independently before any editorial change.

Likewise, the directly inspected [Oxford amateur noun](https://www.oxfordlearnersdictionaries.com/definition/english/amateur_2) and [amateur adjective](https://www.oxfordlearnersdictionaries.com/definition/english/amateur_1) entries confirm that **“The amateur photographer won a local prize.”** uses the **adjective**, not the provisional **noun**. An unapproved noun-targeted candidate is: “The photographer was an amateur when she won the local prize.” These are *editorial proposals only*, not independent approvals, and should not be deployed.

For **custody**, the definition combines care of a child with detention of a suspect; a reviewer should select a single exact sense and ensure the Myanmar phrase and example match. For **legendary**, avoid presenting a literal mythological interpretation as the only meaning when the example concerns a celebrated singer.

## Structural evidence and release gates

Added a staging-only C1 auditor with frozen source and shortlist bindings and **306 negative mutation cases** (25 per word × 12 plus six packet-level mutations), wired into the existing **six parallel CEFR lanes** and documentary no-deployment workflow. Updated cross-batch coverage and reviewer-priority expected counts. Connector-side read-back and in-memory structural/provenance parity checks succeeded; **the new Python auditor and new GitHub Actions jobs have not yet been verified by actual run conclusions/logs**. Do not call them passed until retrieved.

Expected source-research totals after this packet, subject to CI verification: **A1 195/200, A2 84/200, B1 84/200, B2 70/200, C1 63/200 = 496/1,000 distinct**; **515 Oxford observations** including repeats; **504** without direct observations. Priority handoff: **3 unlisted (not a CEFR level), 15 publisher-higher, 158 publisher-lower, 320 matching word/POS still exact-sense-unverified, 504 without observations**. All are *research* counts, never independent signoff.

First-pass written / independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Real George/Emma final headword+example listening receipts: **0/1,000**. Human-independent English/Myanmar/example/exact-sense CEFR signoff, final dual-voice audio generation and listening, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages capacity, preservation verification at actual launch and confirmed production deployment remain **unverified**.

**Release: BLOCKED / STAGING ONLY.** Do not merge, publish, modify main, overwrite existing George/Emma production audio, alter 54 lessons or the separate IELTS 1,000 bank, or claim device/listening/hosting evidence without genuine records.
