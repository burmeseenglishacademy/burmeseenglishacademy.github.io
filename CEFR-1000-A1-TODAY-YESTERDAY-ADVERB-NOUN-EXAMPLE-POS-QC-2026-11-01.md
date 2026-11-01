# CEFR 1,000 — A1 time-word adverb/noun example POS source QC (1 November 2026)

**STAGING ONLY — RELEASE BLOCKED.** This checkpoint concerns the user-approved **1,000-total** shortlist (A1/A2/B1/B2/C1 **200 each**), not the superseded 5,000-word project. All entries remain on editorial hold; no independent reviewer or listening receipt is represented here.

## Direct publisher evidence (opened 2026-11-01)

| Held A1 card | Frozen POS / example | Directly observed Oxford distinction | Editorial status |
| --- | --- | --- | --- |
| **today** | adverb — `Today is Monday.` | [Oxford today noun](https://www.oxfordlearnersdictionaries.com/definition/english/today_2), lines 88–116, expressly identifies the frozen example as a **noun-subject** usage. [Oxford today adverb](https://www.oxfordlearnersdictionaries.com/definition/english/today_1), lines 88–112, gives time-modifier examples. | **Example/POS mismatch**; propose unapproved `I have an English lesson today.` |
| **yesterday** | adverb — `Yesterday was Sunday.` | [Oxford yesterday noun](https://www.oxfordlearnersdictionaries.com/definition/english/yesterday_2), lines 88–123, expressly gives the frozen example as a **noun-subject** usage. [Oxford yesterday adverb](https://www.oxfordlearnersdictionaries.com/definition/english/yesterday_1), lines 88–123, gives time-modifier examples. | **Example/POS mismatch**; propose unapproved `I was at home yesterday.` |
| **tomorrow** | adverb — `We have class tomorrow.` | [Oxford tomorrow adverb](https://www.oxfordlearnersdictionaries.com/definition/english/tomorrow_1), lines 88–113, supports the frozen time-modifier example. | **Correct control**; no rewrite required. |

The two original sentences are **grammatically correct English**, but they illustrate the *noun* senses of words whose frozen cards explicitly teach *adverbs*. This is a teaching-example exact-POS issue, not evidence that the headwords or A1 placements are automatically wrong. Oxford's **Time a1** labels are topic classifications and are **not independent publisher exact-sense CEFR signoffs**. No independent review was performed.

## Frozen provenance and unapproved handoff

Source-bound research packet: [A1 temporal POS packet](draft/CEFR-1000-A1-TEMPORAL-ADVERB-NOUN-EXAMPLE-POS-2026-11-01.json). It preserves the original English, Myanmar, example, source path/index/blob SHA, direct Oxford URL, observation date and page locator for all three entries. Proposed Myanmar teaching notes are unapproved. No original shortlist entry, review flag or existing production vocabulary was changed.

Fail-closed audit: [A1 temporal POS auditor](tools/audit_cefr_1000_a1_temporal_example_pos.py). It binds the entire 1,000-row provisional Git blob, verifies 200-per-level counts, uniqueness and editorial holds, checks all frozen source snapshots, and rejects synthetic publisher/grammar/Myanmar/provenance/approval mutations. It is integrated into all six structural CEFR lanes and the documentary **no-deploy** workflow. The [release-readiness auditor](tools/audit_cefr_1000_launch_readiness.py) also blocks any future final **A1 adverb** entry retaining either noun-subject example; an independently reviewed example rewrite or an independently reviewed POS/sense correction is required.

## CI evidence and release blockers

- Structural run [41285743413](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41285743413), code SHA `f71b545f6ec6d088fe37830113bf589367f23939`: launched, final conclusions pending at checkpoint creation.
- Documentary no-deploy run [41285746593](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41285746593), code SHA `277417e2de0310f16882974b120f37df1783e071`: launched, final conclusions pending at checkpoint creation.
- Readiness hardening code SHA `4d3e58a1926ae90b8279c25ee64c0e6300d76378`: separate documentary run must be checked before claiming test success.
- First-pass **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0** written/independently approved. All **1,000 editorial holds** remain. Approved final manifest **absent**; independent word review receipts **0**; George/Emma real listening receipts **0**; automated browser receipts **0**; physical iPhone Safari, measured GitHub Pages hosting and production confirmation **absent**.
- Preserve 54 production lessons, separate IELTS 1,000-word bank, existing George/Emma production audio and privacy assets. **No merge, no main edit, no deployment**.

**Human-independent exact-sense/CEFR, fluent Myanmar, grammar/example and pronunciation review must occur before any approval.** No automated audit or publisher lookup substitutes for that signoff.
