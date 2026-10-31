# CEFR 1,000 — B2 fourteenth twelve Oxford word/POS and four direct sense leads (31 October 2026)

**Staging only; release BLOCKED.** Approved project scope is **1,000 total**, exactly 200 provisional first-pass entries in each of A1, A2, B1, B2, C1. Frozen shortlist and independent-review tasks remain unchanged. This is publisher research and assistant editorial triage, **not independent linguistic or CEFR signoff**.

## Direct publisher observations

On **2026-10-31**, inspected [Oxford 3000 official CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf). The following 12 B2-draft entries had not appeared in the preceding B2 Oxford source packets. PDF page numbers are 1-based and extracted line numbers are 0-based as displayed by the web text extractor.

| Draft B2 word/POS | Oxford word/POS CEFR | PDF page / extracted line | Reviewer concern |
| --- | --- | --- | --- |
| tone (noun) | B2 | 12 / 3257 | Voice emotion versus document atmosphere or musical tone |
| topic (noun) | A1 | 4 / 813 | Elementary discussion subject, not automatically B2 |
| vast (adjective) | B2 | 12 / 3286 | Large area/quantity sense |
| earn (verb) | A2 | 5 / 1151 | Receive pay versus earn respect |
| ignore (verb) | B1 | 8 / 2131 | Deliberately disregard versus fail to notice |
| meanwhile (adverb) | B1 | 9 / 2209 | Simultaneous events and punctuation |
| necessarily (adverb) | B1 | 9 / 2231 | Draft affirmative definition versus negated example |
| practical (adjective) | B1 | 9 / 2308 | Workable solution versus hands-on or sensible person |
| rescue (verb) | B2 | 12 / 3138 | Verb/noun distinction |
| stable (adjective) | B2 | 12 / 3214 | Reliable supply versus physical balance |
| temporary (adjective) | B2 | 12 / 3249 | Limited duration |
| technique (noun) | B1 | 10 / 2498 | Countable method versus uncountable skill |

**Publisher distribution: A1 1, A2 1, B1 5, B2 5, C1 0; seven B2 placement discrepancies.** Oxford word/POS level does not automatically apply to the specific taught sense.

## Four directly inspected Oxford dictionary senses

- [tone noun](https://www.oxfordlearnersdictionaries.com/definition/english/tone_1), sense 1, page-text lines 103–125: emotional quality of voice; the draft example concerns a calm speaking tone. Sense 2 concerns the character of writing/events and must not be merged.
- [necessarily adverb](https://www.oxfordlearnersdictionaries.com/definition/english/necessarily), *not necessarily* idiom, page-text lines 123–132: a claim is not definitely or always true. The draft defines the affirmative adverb but illustrates the negated construction; this needs a human choice of target sense and aligned Myanmar/example.
- [practical adjective](https://www.oxfordlearnersdictionaries.com/definition/english/practical_1), sense 2, page-text lines 138–147: a sensible/workable course of action; the draft's solution example fits this sense more closely than the broad definition.
- [technique noun](https://www.oxfordlearnersdictionaries.com/definition/english/technique), sense 1, page-text lines 103–125: a countable method requiring learnt skill, distinct from sense 2, uncountable skill in performing a task.

No dictionary topic badge or Word-of-the-Day footer has been treated as an exact-sense CEFR rating. Four self-authored alternative Myanmar meanings and original example sentences are stored as **UNAPPROVED_EDITORIAL_PROPOSAL**, separate from the frozen shortlist.

## Provenance, tests, and release blockers

The [12-record evidence packet](draft/CEFR-1000-OXFORD-B2-FOURTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json) binds every original English definition, Myanmar meaning, example, part of speech, historical source file/index/blob and the publisher URL/date/page/line. The [standalone fail-closed auditor](tools/audit_cefr_1000_oxford_b2_fourteenth_twelve.py) checks these bindings against the actual historical Git source and rejects **208 synthetic mutation cases** when run with `--self-test`. It is wired into the six parallel CEFR structural lanes and the no-deployment documentary gate. The 12 records are **not yet included** in the older consolidated Oxford coverage/handoff constants (which still report 840 distinct); counting them separately gives 852 researched distinct headwords, subject to cross-batch reconciliation and actual CI.

GitHub Actions runs triggered by the staging workflow updates: [structural 41190002806](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41190002806) (code SHA `d17035862a6578b27a61ca3f7b0ab1bfd3b746fb`) and [documentary 41190006063](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41190006063) (code SHA `2ecef7e5c8f3266e22eb239f612118599f5ab5a2`). **Job conclusions/logs must be checked before asserting PASS**; these are not release approvals.

First-pass written/independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. George/Emma final word+example audio real-listening receipts **0/1,000**. No independent English/Myanmar/example/exact-sense CEFR review, final approved manifest, final audio generation and listening, approved-corpus browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting readiness or production deployment proof. Existing 54 lessons, separate IELTS 1,000, production George/Emma audio and privacy remain protected. **NO MERGE, NO MAIN CHANGE, NO PUBLICATION.**
