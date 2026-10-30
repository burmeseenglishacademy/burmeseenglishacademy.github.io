# CEFR 1,000 — seventh B2-draft Oxford twelve and four sense leads
**Observed:** 2026-10-30. **Branch:** `cefr-5000-bilingual-qa-staging`. **Scope:** user-approved **1,000 TOTAL** (A1/A2/B1/B2/C1 200 each), NOT the superseded 5,000-word plan. **Disposition:** research / editorial hold only; no independent review, release, merge, main change or production deployment.

## Direct publisher word/POS observations
Directly opened [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) on **2026-10-30**. PDF page numbers below are **1-based**; extracted lines are **0-based web text locators**. The original English definition, Myanmar meaning, example sentence, historical Git blob/path/index and independent-review task for every entry are preserved in [the evidence packet](draft/CEFR-1000-OXFORD-B2-SEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json).

| B2 draft headword | POS | Oxford PDF word/POS level | PDF/page:line | Review status |
|---|---|---|---|---|
| speaker | noun | A2 | 3000/6:1645 | lower-level conflict |
| percentage | noun | B1 | 3000/9:2273 | lower-level conflict |
| household | noun | B2 | 3000/11:2914 | exact sense unverified |
| occur | verb | B1 | 3000/9:2247 | lower-level conflict |
| alongside | preposition | C1 | 5000/3:766 | higher-level conflict and publisher badge conflict |
| anxiety | noun | B2 | 5000/1:31 | exact sense unverified |
| charity | noun | A2 | 3000/4:1038 | lower-level conflict and publisher badge conflict |
| discovery | noun | A2 | 3000/5:1134 | lower-level conflict |
| formal | adjective | A2 | 3000/5:1231 | lower-level conflict |
| formula | noun | C1 | 5000/5:1229 | higher-level conflict and publisher badge conflict |
| innocent | adjective | B1 | 3000/8:2152 | lower-level conflict |
| mystery | noun | B1 | 3000/9:2225 | lower-level conflict |

**Publisher level distribution:** A2 4, B1 4, B2 2, C1 2. **10/12 word/POS-level conflicts** with draft B2; two matches still need independent exact-sense checks. No word/POS classification alone establishes an individual teaching sense or human approval.

## Four directly opened dictionary sense investigations
- [alongside, preposition](https://www.oxfordlearnersdictionaries.com/definition/english/alongside_2), definition 1: next to something, matching the buildings example. The live dictionary displays an **Oxford 3000 B2** badge while the official Oxford 5000 PDF lists the preposition at **C1**. Both publisher surfaces are retained; do not resolve the discrepancy automatically.
- [formula, noun](https://www.oxfordlearnersdictionaries.com/definition/english/formula), definition 1: mathematical rule represented with symbols, matching the engineer/calculation example; distinguish chemistry, method, and recipe senses. The dictionary displays **Oxford 3000 B2**, but the Oxford 5000 PDF lists **C1**.
- [charity, noun](https://www.oxfordlearnersdictionaries.com/definition/english/charity), definition 1: an organization that helps people in need, matching the meals-for-residents example. The dictionary displays **Oxford 3000 B2**, whereas the Oxford 3000 PDF lists the noun at **A2**; its A2 *social issues* topic label is not an independent CEFR approval.
- [percentage, noun](https://www.oxfordlearnersdictionaries.com/definition/english/percentage), definition 1: an amount/rate out of one hundred, matching returned-product proportion. Oxford's **B1** maths-topic label and PDF word/POS level agree, but *percentage* and *percentage point* are distinct and the precise learner sense remains unapproved.

All four pages were directly opened on **2026-10-30**; source URLs, observed dates, sense locators, draft examples and unresolved publisher-surface conflicts are retained in the JSON packet. The English/ Myanmar wording and original example grammar were checked for editorial risks, **not independently certified**. Human reviewers must confirm precise senses, CEFR teaching suitability, natural Myanmar, original example grammar and British pronunciation.

## Fail-closed staging controls and current counts
Created `tools/audit_cefr_1000_oxford_b2_seventh_twelve.py` to bind all twelve rows to the frozen shortlist Git blob, English/Myanmar/example snapshots, historical provenance, exact publisher URL/PDF page/line/word/POS, reviewer tasks, four sense leads and zero approvals/listening. Its **178 adversarial mutations** are designed to reject forged source, Myanmar, examples, dictionary badge evidence and independent signoffs. Added it to six parallel structural CEFR jobs and the documentary no-deploy gate; updated cross-batch coverage and reviewer handoff expectations.

**Research coverage expected after this packet:** A1 **195/200**, A2 **96/200**, B1 **96/200**, B2 **94/200**, C1 **63/200** = **544/1,000 distinct** across **563 publisher observations**, with **456** lacking direct Oxford word/POS observations. B2 batch-level observations **96**, distinct B2-draft words **94** (two same-level duplicate historical observations); B2 publisher breakdown A1 2, A2 16, B1 21, B2 48, C1 6, unlisted 1. Reviewer queue expected **3 unlisted, 22 publisher-higher, 177 publisher-lower, 342 word/POS-matching but exact-sense-unverified, 456 without direct observations**. These figures are structural expectations / in-memory B2 packet reconciliation, **not a fresh verified GitHub Actions result**.

**CI evidence status:** new GitHub Actions run IDs, actual six-job conclusions and logs are **NOT RETRIEVED / NOT VERIFIED** at this checkpoint. The latest previously verified structural [run 40975080124](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40975080124) and documentary [run 40975084949](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40975084949) were for earlier code and **do not validate this batch**. New workflow or auditor success must not be asserted without real conclusions and logs.

**First-pass written / independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. Final British George/Emma headword/example audio generated and actually listened to: **unverified / 0 real listening signoffs out of 1,000**. Human-independent English, fluent Myanmar, grammar, exact-sense/CEFR, pronunciation and source-backed approval; final dual-voice audio/listening; approved-corpus browser/mobile regression; real physical iPhone Safari; measured GitHub Pages hosting readiness; preserved-production-asset launch diff; and confirmed live deployment are all **BLOCKED / MISSING**. Protect 54 lessons, separate IELTS 1,000-word bank, existing George/Emma production audio and privacy. **Staging only. Never publish or merge before all gates pass.**
