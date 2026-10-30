# CEFR 1000 — A2 compound six: Cambridge dictionary sense triage (30 October 2026)

**STAGING ONLY. No independent approval, no publication.** This is the user-approved **1,000-total** project, not the superseded 5,000 plan. The frozen shortlist, 54 production lessons, separate IELTS 1,000-word bank, established George/Emma audio and privacy files were not modified.

## Research and exact retrieval limitations

On **2026-10-30**, six Cambridge University Press dictionary entries were retrieved as **web search-index snippets**. Direct attempts to open the Cambridge pages returned **HTTP 403**. Consequently this is **not** direct live-page inspection and cannot assert page line numbers, complete senses, current page text, or independent exact-sense CEFR signoff. See the provenance-bound [six-record research packet](draft/CEFR-1000-CAMBRIDGE-A2-COMPOUND-SIX-SENSE-TRIAGE-2026-10-30.json). Each record preserves original English/Myanmar/example snapshots, source path/index/blob SHA, publisher URL, observation date, retrieval method, visible badge, risk, editorial suggestions, and all approvals false.

| Draft A2 noun | Cambridge indexed publisher evidence | Editorial issue |
|---|---|---|
| [raincoat](https://dictionary.cambridge.org/dictionary/english/raincoat) | **A2 badge visible**; rain-protective coat | English and Myanmar meaning broadly align; still independently verify exact sense and natural example |
| [lunchbox](https://dictionary.cambridge.org/dictionary/english/lunchbox) | Meaning attested; **no CEFR badge visible** | A container, not its food; **do not infer A2** from missing badge |
| [toothache](https://dictionary.cambridge.org/dictionary/english/toothache) | **A2 badge visible**; countable or uncountable noun | Review British countability, including “have toothache” versus “have a toothache” |
| [sunscreen](https://dictionary.cambridge.org/dictionary/english/sunscreen) | Skin-protective substance attested; **no CEFR badge visible** | More precise Myanmar/English reference to UV protection; **do not infer A2** |
| [shoelace](https://dictionary.cambridge.org/dictionary/english/shoelace) | Countable, **usually plural**; **no CEFR badge visible** | Original singular imperative may be natural for one lace, but plural is generally better for a pair |
| [bookshelf](https://dictionary.cambridge.org/dictionary/english/bookshelf) | **A2 badge visible**; shelf for books, plural **bookshelves** | Distinguish bookshelf from bookcase; “highest bookshelf” context needs review |

The packet contains six **original unapproved Myanmar/example editorial alternatives**, not accepted edits. All source observations are dictionary-sense leads and **must not** be counted as new Oxford core-list PDF word/POS observations. In particular, the three missing Cambridge CEFR badges are unknown, not A2, C1, or “unlisted” classifications.

## Automated integrity and release gates

Added [fail-closed A2 compound auditor](tools/audit_cefr_1000_cambridge_a2_compound_six.py) checking exact source snapshots, publisher URLs, search-index retrieval limits, visible CEFR badges, historical Git provenance, editorial holds, frozen shortlist English/Myanmar/examples, and absence of independent-review approvals. It includes adversarial mutation tests and is called by the six parallel A1/A2/B1/B2/C1/ALL structural lanes and the documentary no-deployment workflow. Passing this auditor would establish **structural integrity only**, not linguistic accuracy, live publisher availability, listening, physical iPhone QA, or release permission.

Structural run: [41042948932](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41042948932), workflow commit `d592fdf2314d6630fea0eecba06b6abb78039975`. Documentary run: [41042955331](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41042955331), workflow commit `4a015d1c2f94ce70dba45d20fd478e675d7119e4`. **Job conclusions and logs must be checked before claiming success.**

## Exact release blockers and next handoff

First-pass written / independently checked: **A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0**. All 1,000 remain editorial holds. Existing direct Oxford word/POS coverage remains **A1 195, A2 108, B1 120, B2 118, C1 99 = 640/1,000**, with **360 without direct Oxford observation**; these six Cambridge snippets do **not** alter that count. Final George/Emma headword-and-example real listening signoffs: **0/1,000**. Human-independent English, fluent Myanmar, original examples and exact-sense CEFR signoff, final audio generation and real listening, approved-corpus desktop/mobile browser regression, physical iPhone Safari evidence, measured GitHub Pages readiness, preservation/privacy verification and confirmed production deployment are absent. **No merge, main change, or publication. Release BLOCKED / STAGING ONLY.**

## Final CI verification (same staging-only change)

After diagnosing and repairing a snapshot-key mismatch (the frozen shortlist stores `burmese_meaning`, whereas the evidence packet calls its field `myanmar_meaning`), verified [structural run 41043149402](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41043149402), **SUCCESS across all six A1/A2/B1/B2/C1/ALL jobs**. Verified [documentary no-deploy run 41043149405](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41043149405), **SUCCESS report-only**. Both use SHA `54a09b2741da9302e91b772d0f2f4216e73644e7`. Actual ALL-job and documentary logs confirm **179/179** forged evidence/translation/provenance/review-state mutations rejected, three indexed A2 badges versus three unknown badges, and protected production assets unchanged. Earlier runs 41042948932, 41042955331, 41043074490 and 41043074480 are **not** counted as successful final-state verification. CI success does not approve vocabulary, audio, iPhone testing, hosting or deployment.
