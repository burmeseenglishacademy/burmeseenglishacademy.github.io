# CEFR 1,000 — C1 twelfth 12-word source-bound editorial triage (2026-10-31)

**Staging only.** Branch `cefr-5000-bilingual-qa-staging`; never merge, publish or modify `main`. The user-approved scope is **1,000 TOTAL**: A1/A2/B1/B2/C1 exactly 200 each. This packet is research, **not** an approved release manifest.

## Direct publisher observations

The [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) were inspected directly on **2026-10-31** for these exact headwords/parts of speech.

- **unexpected (adjective): B2**, Oxford 3000 PDF, **page 12, extracted line 3274**, publisher excerpt `unexpected adj.`. Provisional draft C1 is **not independently substantiated** by that publisher word/POS label; exact-sense and CEFR placement require independent review.
- **Not found in either inspected Oxford core list**: actively, imperial, bearing, repeatedly, advisory, deference, delineate, dichotomy, disseminate, eclectic, efficacy. **Absence is not a CEFR label** and must not be converted into C1, C2 or any other classification. This is an evidence-gap finding, not proof the words are unsuitable.

Four directly opened Oxford dictionary sense leads, also inspected **2026-10-31**, document lexical/grammar details but do **not** establish independently reviewed exact-sense CEFR:

| Draft word | Official publisher dictionary | Direct page lines | Specific reviewer risk |
|---|---|---|---|
| bearing | [Oxford noun](https://www.oxfordlearnersdictionaries.com/definition/english/bearing) | 88–123 | Sense 1 `bearing on` (uncountable/singular, relevance/influence); the Engineering c2 topic badge belongs to a **different mechanical sense** |
| delineate | [Oxford verb](https://www.oxfordlearnersdictionaries.com/definition/english/delineate) | 88–115 | Formal transitive verb describing/drawing/explaining in detail; draft may overrestrict to exact limits |
| dichotomy | [Oxford noun](https://www.oxfordlearnersdictionaries.com/definition/english/dichotomy) | 88–109 | Formal, usually singular, two strongly opposed groups or things; not merely any division |
| efficacy | [Oxford noun](https://www.oxfordlearnersdictionaries.com/definition/english/efficacy) | 88–110 | Formal uncountable effectiveness; distinguish from efficiency; OPAL W is not a CEFR level |

The [12-record immutable shortlist-bound research packet](draft/CEFR-1000-OXFORD-C1-TWELFTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json) preserves exact original English/Myanmar/example snapshots, historical source paths, indices and Git blobs, publisher URLs, observation dates, Oxford page/line locators and separate unapproved Myanmar/example proposals for four words. No frozen shortlist content or review flags changed.

The [fail-closed auditor](tools/audit_cefr_1000_oxford_c1_twelfth_twelve.py) checks source/shortlist Git blobs, historical original source rows, exact Oxford B2 locator, explicit two-list absence semantics, dictionary URLs/sense numbers, Burmese/example provenance, editorial holds and no fabricated human receipts. It defines **173** adversarial in-memory mutations (12 × 13, 4 × 3, plus 5 packet-level). **CI conclusions and logs, not a code commit, determine whether these tests passed.** Wired to six parallel A1/A2/B1/B2/C1/ALL structural lanes and the documentary no-deploy gate.

## Coverage and release status

After successful CI reconciliation, expected direct Oxford word/POS **research observations** are A1 **195/200**, A2 **200/200**, B1 **200/200**, B2 **200/200**, C1 **123/200**, totaling **918/1,000 distinct** across **937** research observations; **82** without an audited direct Oxford observation. C1 contains 13 unlisted observations (including the 11 new absences). Reviewer-priority totals expected: **35 unlisted**, **61 publisher higher**, **352 publisher lower**, **470 word/POS matching but exact-sense unverified**, **82 unobserved**. These counts must be checked against actual CI logs; they do **not** mean independent verification.

First-pass written / independently checked: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Real George/Emma final headword and example listening signoffs: **0/1,000**. No independent English, fluent Myanmar, original example, exact-sense CEFR, pronunciation or human reviewer receipts; no final approved-manifest dedup, dual-voice audio generation/listening, browser/mobile regression, physical iPhone Safari evidence, measured Pages deployment artifact, or confirmed live production release.

Protect existing **54 lessons**, separate **IELTS 1,000-word bank**, established production George/Emma audio, and privacy controls. No release or production changes are authorised until **every** evidence gate passes. **RELEASE BLOCKED — STAGING ONLY.**


## Actual CI verification — 2026-10-31 16:02 UTC (2026-11-01 00:02 Singapore)

**Verified from GitHub Actions run conclusions, job steps and decoded logs**, not inferred from code commits:

- [Parallel structural run 41217633979](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41217633979): **completed SUCCESS**, all six jobs A1/A2/B1/B2/C1/ALL **SUCCESS**; code SHA `e2cd864aa1a288ed95a3ad066c55ad9b9625ef0d`. ALL job ID `124585382306`, structural ALL artifact ID `13048975582`.
- [Documentary no-deployment run 41217633931](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41217633931): **completed SUCCESS**, documentary job `124585382050`, same code SHA; blocker artifact ID `13048003194`. **SUCCESS means the documentary gate correctly reports blockers, not that launch gates passed.**
- Actual ALL and documentary logs each confirm **173/173** forged Oxford source, Myanmar, historical provenance and fabricated review mutations rejected; new 12-word packet shows 11 unlisted, one Oxford B2 word/POS and four direct dictionary leads, **zero independent approvals**.
- Actual ALL logs confirm cross-batch Oxford reconciliation **A1 195, A2 200, B1 200, B2 200, C1 123 = 918/1,000 distinct** and 937 observations; 82 not directly observed. Documentary logs confirm protected production assets unchanged and explicitly block independent review, final voice listening, physical iPhone and measured hosting/deployment evidence.

Earlier intermediate workflow runs failed while the reviewer-handoff validator still expected 94 unobserved entries; this was repaired to **82** before the successful final runs. This checkpoint remains **STAGING ONLY / RELEASE BLOCKED**.
