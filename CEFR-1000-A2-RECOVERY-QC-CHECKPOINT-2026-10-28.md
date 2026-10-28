# CEFR 1,000 staging — A2 historical recovery source/QC checkpoint (2026-10-28)

**Decision: BLOCKED — STAGING ONLY.** Approved scope remains **A1 200, A2 200, B1 200, B2 200, C1 200**, total **1,000**, never the superseded 5,000-word plan. Branch remains `cefr-5000-bilingual-qa-staging`; **no merge, main modification, public deployment or independent signoff**.

## Evidence-based editorial work

New source packet: [12 A2 recovery observations](draft/CEFR-1000-CAMBRIDGE-A2-RECOVERY-TWELVE-2026-10-28.json), committed at `d52324f37ea31fad224e0bd21b077797c4931756`. All 12 are in the unchanged provisional 1,000-word shortlist and originate from earlier `A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*` drafts. Each record preserves original English definition, Myanmar meaning, example, source path, publisher URL, observation date (2026-10-28), observed CEFR label **or explicit null**, sense identifier, reviewer task and **editorial hold**. All source observations are **publisher-owned web-search excerpts**, not authenticated full-page human review or final exact-sense signoff. No publisher text was copied into learner definitions.

| Draft A2 entry | Publisher observation (2026-10-28) | Editorial implication |
| --- | --- | --- |
| [raincoat](https://dictionary.cambridge.org/dictionary/essential-british-english/raincoat) | Cambridge Essential British **A2**, rain protection | Provisional sense broadly aligned; Myanmar and example still unreviewed |
| [toothache](https://dictionary.cambridge.org/dictionary/english/toothache) | Cambridge **A2**, dental pain | Sense broadly aligned; countability and British example still unreviewed |
| [bookshelf](https://dictionary.cambridge.org/dictionary/learner-english/bookshelf) | Cambridge Learner **A2**, shelf for books | Sense broadly aligned; translation/example still unreviewed |
| [postcard](https://dictionary.cambridge.org/dictionary/english/postcard) | Cambridge **A2**, mailable card | Sense broadly aligned; review whether definition is too restrictive |
| [saucepan](https://dictionary.cambridge.org/dictionary/english/saucepan) | Cambridge **B1**, deep cooking pan | **A2 same-sense level conflict**; require independent A2 support or replace/retier |
| [dustbin](https://dictionary.cambridge.org/dictionary/english/dustbin) | Cambridge **B1**, UK household outside rubbish container | **A2 level and definition/example referent conflict**; review UK terminology |
| [washcloth](https://dictionary.cambridge.org/dictionary/english/washcloth) | Cambridge **no observed CEFR**; marked **US**, UK alternatives facecloth/flannel | British English suitability and CEFR evidence missing |
| [shoelace](https://dictionary.cambridge.org/dictionary/english/shoelace) | Cambridge **no observed CEFR**, noun usually plural | Check singular example and British usage; no A2 evidence |
| [lunchbox](https://dictionary.cambridge.org/dictionary/english/lunchbox) | Cambridge **no observed CEFR**, lunch container | Meaning supported but A2 level not substantiated |
| [doormat](https://dictionary.cambridge.org/dictionary/english/doormat) | Cambridge **no observed CEFR**, literal mat vs figurative person | Keep literal sense distinct; no A2 source label |
| [bathrobe](https://dictionary.cambridge.org/dictionary/english/bathrobe) | Cambridge **no observed CEFR**, compare dressing gown | Distinguish post-bath towelling robe vs British dressing gown |
| [sunscreen](https://dictionary.cambridge.org/dictionary/learner-english/sunscreen) | Cambridge **no observed CEFR**; [Collins COBUILD **B2**](https://www.collinsdictionary.com/de/worterbuch/englisch/sunscreen) | Independent A2 exact-sense source and bilingual review required; cannot auto-approve |

**Publisher CEFR evidence distribution:** four Cambridge A2 matches, two Cambridge B1 discrepancies, six Cambridge unlabelled; one separate Collins B2 observation among those six. A publisher word/sense label is **not** independent human curriculum verification.

## Code and actual execution evidence

- New [fail-closed source audit](tools/audit_cefr_1000_a2_recovery_twelve.py) binds the 12 source observations to the exact canonical shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, all bilingual/example snapshots, source URLs, observed CEFR/null labels and hold flags. It rejects **15/15** deliberate source, Myanmar, example, CEFR, false-approval and duplicate mutations in the actual GitHub Actions ALL job. Initial CI runs failed because the auditor incorrectly rejected the valid short editorial risk code `MATCH_A2`; repaired by allowing nonempty short codes and adding an empty-risk negative test in commit `4dec5cd0bd3608a3a7643488406a56084a67bd4a`. The failure was an auditor schema issue, **not** an approved content change.
- Integrated in [six-job parallel structural matrix](.github/workflows/cefr-1000-selection-structural-qa.yml) and [documentary no-deploy gate](.github/workflows/cefr-1000-go-live-qc-gate.yml). Added an **empty** `a2_recovery_twelve_review_receipts` array to [release evidence](draft/CEFR-1000-RELEASE-EVIDENCE.json). [Launch-readiness auditor](tools/audit_cefr_1000_launch_readiness.py) now blocks retained A2 recovery entries without independent source-backed exact-sense, English/Myanmar/example and British-usage reconciliation tied to reviewed-content hashes. Unchanged saucepan, dustbin and sunscreen high-risk drafts cannot be rubber-stamped.
- **Actual verified GitHub Actions structural run [40637802552](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40637802552), commit `4dec5cd0bd3608a3a7643488406a56084a67bd4a`: all A1, A2, B1, B2, C1 and ALL job conclusions SUCCESS.** ALL job `122648703942` logs confirm 1,000 provisional linked review tasks, 0 approvals, 15/15 new mutation rejections, 120 IELTS/CEFR shared headwords still unresolved and protected production diff PASS. This is structural testing, not language signoff.
- **Actual verified documentary run [40637802594](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40637802594), same commit: SUCCESS as report-only, never deployment.** Job `122648704071` logs show 0/1,000 independent reviews, 0/1,000 both-voice real listening receipts, missing browser/device/hosting evidence, and protected production diff PASS. A successful documentary job **does not mean release readiness**.

## Exact content and QC state

| Level | First-pass English/Myanmar/examples | Independently checked/approved | George + Emma final real-listening receipts for complete entries |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

**Still blocked:** independent English, fluent Myanmar, original-example grammar and publisher-backed exact-sense CEFR receipts for every retained entry; historical Oxford/Cambridge and WordNet/named-entity risks; independently resolved 120 IELTS-bank shared headwords; approved 200-per-level manifest; actual generated George/Emma headword/example recordings with human listening; complete browser/mobile regressions and real physical iPhone Safari evidence; measured GitHub Pages site size/bandwidth/deploy budget; final privacy/54-lesson/IELTS/production audio preservation audit; confirmed live production deployment.

**Production:** no merge, no publication, no main changes. Structural CI's protected-path diff checks passed; this does **not** replace a final exhaustive post-deployment asset audit. Human-independent review is still **0/1,000**. Do not send completion notice.
