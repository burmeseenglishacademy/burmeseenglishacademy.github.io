# CEFR 1,000 — A2 seventh twelve Oxford observations and three direct dictionary sense leads
**Observed 30 October 2026 · staging branch only · editorial hold · release blocked**

## Frozen scope and source provenance
- User-approved scope is **1,000 total**, exactly **A1/A2/B1/B2/C1 = 200 each**. The earlier 5,000-word idea is superseded. Branch remains `cefr-5000-bilingual-qa-staging` by policy.
- Frozen first-pass source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. All 1,000 remain editorial holds; **0 independent English, Myanmar, original-example or exact-sense CEFR approvals**. The independent-review task file remains separate and unmodified.
- [Provenance-bound research packet](draft/CEFR-1000-OXFORD-A2-SEVENTH-TWELVE-AND-THREE-DIRECT-SENSE-LEADS-2026-10-30.json) records original definition, Myanmar meaning, example, historical source path/index/blob, official source URL, observation date, 1-based PDF page, 0-based extracted line, verbatim short word/POS excerpt, editorial risk and reviewer task for each of the twelve. No shortlist or human receipt was edited.

## Direct publisher observations — not independent exact-sense labels
Official publisher: [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), directly inspected **30 October 2026**.

| Provisional A2 word | Oxford word/POS level | PDF page / extracted line (0-based) | Observed short excerpt |
|---|---|---|---|
| post | A1 | 3 / 612 | `post n., v.` |
| social | A2 | 6 / 1635 | `social adj.` |
| death | A2 | 5 / 1109 | `death n.` |
| guy | A2 | 5 / 1260 | `guy n.` |
| true | A1 | 4 / 822 | `true adj.` |
| along | A2 | 4 / 936 | `along prep., adv.` |
| matter | A2 | 6 / 1387 | `matter n., v.` |
| pretty | A1 | 3 / 620 | `pretty adj., adv.` |
| bit | A2 | 4 / 999 | `bit n.` |
| hit | A2 | 5 / 1281 | `hit v., n.` |
| past | A1 | 3 / 578 | `past adj., n., prep.` |
| due | B1 | 8 / 1994 | `due adj.` |

Publisher word/POS distribution: **A1 4, A2 7, B1 1**. **Five** publisher-level discrepancies versus the provisional A2 tier require independent resolution. A word/POS list does **not** certify the specific teaching sense or original example.

## Three directly opened Oxford dictionary sense leads (30 October 2026)
1. [post noun](https://www.oxfordlearnersdictionaries.com/definition/english/post_2), page-text lines 190–227: sense 4 covers an online message/blog post; the page also labels the internet topic **a2**. This is a topic label, not proof that the whole word/POS list's A1 classification is the appropriate level for the draft's online sense. Postal mail, job post and upright post are different senses.
2. [pretty adverb](https://www.oxfordlearnersdictionaries.com/definition/english/pretty_1), lines 88–136: `fairly/to some extent` and `very` are distinct scalar readings. The draft's `pretty clear` needs an independently checked intended reading and fluent Myanmar intensity, not an automatic A1 retier.
3. [due adjective](https://www.oxfordlearnersdictionaries.com/definition/english/due_1), lines 149–165: expected/arranged transport arrival matches the draft bus example; this is separate from owed/payment or `due to` causal uses. The Oxford word/POS list's B1 label conflicts with provisional A2, and the dictionary sense example alone does not approve A2.

Other editorial risks recorded in the packet include **guy** register and gender, **death** respectful phrasing, **matter** issue-versus-substance, **bit** quantity-versus-computing unit, and **hit** transitive physical impact. Candidate Myanmar clarifications for independent review only: `due` in the bus example could use **သတ်မှတ်ချိန်အတိုင်း ရောက်ရှိရန်ရှိသော**; `pretty` in `pretty clear` could use **အတော်လေး ရှင်းလင်းသော**. These are unapproved suggestions, **not changes to the frozen shortlist**.

## CI and fail-closed integrity (actual run/job logs checked)
- [Structural run 40975080124](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40975080124) on code SHA `d6b639dd38acc4b77e3e92c910ce24a2d390f8b8`: **SUCCESS in all six parallel A1/A2/B1/B2/C1/ALL jobs**. Actual ALL-job logs show **378/378** seventh-A2 adversarial mutations rejected, **145/145** reviewer-handoff forged mutations rejected, **551** total Oxford observations, **532** distinct draft headwords and unchanged protected production assets.
- [Documentary no-deployment run 40975084949](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40975084949) on code SHA `6875c8cde8e2d2efdb2f07e4061140f952b8f393`: **SUCCESS as a report-only workflow**, **not a release pass**. Actual logs explicitly retain all independent review, audio, browser, physical iPhone, hosting and deployment blockers. Protected 54 lessons, IELTS bank, established George/Emma audio and privacy assets passed the staging-versus-main diff guard.
- The integrity auditor is `tools/audit_cefr_1000_oxford_a2_seventh_twelve.py`. It binds frozen shortlist bilingual/example snapshots, historical provenance, publisher locators, source scope, dictionary lead lines and editorial holds, and rejects false review or approval. CI cannot independently validate human language judgement or whether source text was genuinely observed; the dated direct publisher observations above are the research evidence, not reviewer receipts.
- Intermediate earlier commits triggered CI before all coverage counters and workflow wiring were reconciled; those intermediate results are **not** represented as final passing builds. The verified run IDs above are the final code checks.

## Exact status after this batch
| CEFR level | First-pass written | Independently approved | Direct Oxford word/POS observed |
|---|---:|---:|---:|
| A1 | 200 | 0 | 195 |
| A2 | 200 | 0 | 96 |
| B1 | 200 | 0 | 96 |
| B2 | 200 | 0 | 82 |
| C1 | 200 | 0 | 63 |
| **Total** | **1,000** | **0** | **532** |

Review-priority queue: **468** without direct Oxford observations; **169** publisher-lower word/POS classifications; **20** publisher-higher; **3** unlisted in inspected core PDFs (not a CEFR level); **340** matching word/POS but exact sense still independently unverified. All 1,000 remain on editorial hold.

**Release BLOCKED / STAGING ONLY:** final George/Emma dual-voice word-and-example recordings have **0/1,000 real listening signoffs**; independent English/Myanmar/example/sense CEFR approvals are **0/1,000**; approved-corpus desktop/mobile Chromium and WebKit regression, physical iPhone Safari and British listening evidence, measured GitHub Pages limits, final protected-production verification and confirmed public deployment are missing. No merge, main change, publication or fabricated reviewer/device/listening signoff occurred.
