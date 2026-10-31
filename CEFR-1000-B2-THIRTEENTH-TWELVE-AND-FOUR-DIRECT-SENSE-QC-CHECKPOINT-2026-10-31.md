# CEFR 1,000 — B2 thirteenth Oxford word/POS and four dictionary sense leads (31 October 2026)

**Scope:** Approved project size is **1,000 total (A1/A2/B1/B2/C1 = 200 each)**. This is **research on `cefr-5000-bilingual-qa-staging` only**, not a release, independent review, change to the shortlist or a proposed 5,000-word expansion.

## Direct publisher observations

Directly inspected the official [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [additional Oxford 5000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) on **2026-10-31**. Each source locator below is **1-based PDF page / 0-based extracted text line**; it is word-and-POS-level evidence, **not exact-sense CEFR verification**.

| B2 provisional word | Draft POS | Oxford word/POS CEFR | Source locator | Review significance |
|---|---|---|---|---|
| atmosphere | noun | B1 | Oxford 3000 p.7, line 1829 | draft B2 differs; human review |
| poverty | noun | B1 | Oxford 3000 p.9, line 2305 | draft B2 differs; human review |
| sensitive | adjective | B2 | Oxford 3000 p.12, line 3176 | word/POS matches; exact sense unverified |
| dispute | noun | C1 | Oxford 5000 p.5, line 1103 | draft B2 differs; human review |
| crucial | adjective | B2 | Oxford 3000 p.10, line 2750 | word/POS matches; exact sense unverified |
| collaboration | noun | C1 | Oxford 5000 p.4, line 917 | draft B2 differs; human review |
| consideration | noun | B2 | Oxford 3000 p.10, line 2720 | word/POS matches; exact sense unverified |
| reliable | adjective | B1 | Oxford 3000 p.9, line 2369 | draft B2 differs; human review |
| transition | noun | B2 | Oxford 3000 p.12, line 3262 | word/POS matches; exact sense unverified |
| celebrate | verb | A2 | Oxford 3000 p.4, line 1032 | draft B2 differs; human review |
| gallery | noun | A2 | Oxford 3000 p.5, line 1242 | draft B2 differs; human review |
| rough | adjective | B1 | Oxford 3000 p.9, line 2399 | draft B2 differs; human review |

**Summary:** 12 new B2-draft word/POS observations: A2 **2**, B1 **4**, B2 **4**, C1 **2**; **8** level mismatches for human exact-sense review. Publisher word/POS level does not automatically override draft level. These 12 were not previously in the audited B2 Oxford packets.

## Four directly inspected dictionary senses (still unapproved)

- **atmosphere:** [Oxford dictionary](https://www.oxfordlearnersdictionaries.com/definition/english/atmosphere), sense **4**, text lines 164–183, describes a place's mood/feeling, matching the café example. Distinguish sense 1 about the earth's gases and sense 3 about air in a room.
- **sensitive:** [Oxford dictionary](https://www.oxfordlearnersdictionaries.com/definition/english/sensitive), sense **5**, lines 206–215, concerns potentially upsetting/offensive topics or information. Distinguish sensitivity to light, other people's feelings and easily hurt emotions.
- **dispute:** [Oxford noun dictionary](https://www.oxfordlearnersdictionaries.com/definition/english/dispute_1), sense **1**, lines 111–143, describes disagreement between parties. The draft's *settled their dispute* is a plausible noun collocation; distinguish the verb.
- **collaboration:** [Oxford dictionary](https://www.oxfordlearnersdictionaries.com/definition/english/collaboration), sense **1**, lines 105–117, is joint work or cooperation. Distinguish the jointly produced work (sense 2) and disapproving wartime meaning (sense 3).

Four fluent-Myanmar and original-example **self-authored proposals** are preserved in [the research packet](draft/CEFR-1000-OXFORD-B2-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json). None has been independently reviewed or approved. Do **not** mistake Oxford topic badges or the unrelated site-wide *Word of the Day* footer for exact-sense CEFR labels.

## Source binding, structural QC and release gates

- [Source-bound 12-record packet](draft/CEFR-1000-OXFORD-B2-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json): immutable shortlist English/Myanmar/example snapshots, historical source path/index/Git blob SHA, official publisher URLs, observation date, PDF page/line and original examples.
- [Fail-closed B2 thirteenth auditor](tools/audit_cefr_1000_oxford_b2_thirteenth_twelve.py): pinned packet and frozen shortlist blobs; rejects forged publisher levels, PDF locators, Myanmar/English/example drift, historical Git provenance changes and fabricated reviewer receipts. Includes **184 designed adversarial mutations**.
- Integrated into the **six parallel A1/A2/B1/B2/C1/ALL structural jobs** and the **documentary no-deployment gate**. Actual run conclusions/logs must be checked before recording CI as successful.
- Updated cross-batch source coverage expected **A1 195/200, A2 144/200, B1 168/200, B2 166/200, C1 111/200 = 784/1,000 distinct**, **803** observations, **216** without direct Oxford word/POS observation. Reviewer priority expected **3 unlisted, 46 publisher-higher, 298 publisher-lower, 437 matching but exact-sense-unverified, 216 unobserved**. These are research coverage counts, not independent approvals.
- **First-pass written / independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**.
- **Final British George/Emma audio:** no verified final 1,000-word dual-voice generation/listening signoffs; **0/1,000 real listening signoffs**. Existing production voice assets must remain untouched.
- **Missing:** human-independent English/Myanmar/example and exact-sense CEFR review; approved-manifest deduplication; complete final headword+example audio and real listening; approved-corpus browser/mobile regression; physical iPhone Safari evidence; measured GitHub Pages hosting readiness; confirmed deployment; post-deploy verification of 54 lessons, separate IELTS 1,000 bank, production audio and privacy.

**Release: BLOCKED / STAGING ONLY. No merge, main change or publication.**

## Verified GitHub Actions results (2026-10-31)

- [Structural run 41154422476](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41154422476), **SUCCESS**, code SHA `a94dec42a964b307f83bb21fde261bff0c5dc390`; actual A1/A2/B1/B2/C1/ALL job conclusions **success**. ALL job log confirmed **184/184** adversarial publisher, bilingual, grammar, provenance and forged-approval mutations rejected, and protected production assets unchanged. ALL artifact ID **13024436682**.
- [Documentary no-deployment run 41154427253](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41154427253), **SUCCESS / report-only**, code SHA `28302313fe56f1cc58a6c72dd36fcb1a26b3c9cc`; actual job log independently confirmed **184/184** forged mutations rejected, source-bound handoff and release still **BLOCKED_STAGING_ONLY**. Blocker artifact ID **13024661954**.
- Interim CI failures on the coverage-only commit `816bc3f913a11c29da0a6d7b7a2ae14c8f677de4` were caused by temporarily unreconciled reviewer-priority totals; the successful runs above include the reconciled code. These runs verify *structural/documentary controls*, not independent linguistic review, audio listening, iPhone Safari, hosting or deployment.
