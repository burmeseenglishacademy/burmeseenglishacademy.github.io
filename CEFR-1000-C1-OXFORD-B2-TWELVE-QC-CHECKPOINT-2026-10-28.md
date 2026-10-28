# CEFR 1,000 — twelve additional C1-draft / Oxford B2 word-POS conflicts (2026-10-28)

**Decision: BLOCKED / STAGING ONLY.** This is the user-approved **1,000-total** vocabulary scope: A1/A2/B1/B2/C1 **200 each**, not the superseded 5,000-word plan. No change to main, no merge, no publication and no independent review signoff.

## Direct Oxford University Press evidence

On **2026-10-28**, inspected the official [Oxford 5000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf), which lists additional B2–C1 words by headword/part of speech. Twelve **provisional C1** words below appear in its **B2** section at the indicated word/POS. This is **not exact-sense CEFR evidence**, and is not a human-independent editorial judgement. Source page numbers are 1-based PDF pages; line references are 0-based extracted PDF text lines.

| Provisional C1 word | Oxford 5000 word/POS | PDF page / line | Specific editorial risk |
| --- | --- | --- | --- |
| additionally | B2 adverb | 1 / 17 | Ordinary discourse connector; formal register alone does not prove C1 |
| disability | B2 noun | 1 / 172 | Independently check respectful disability terminology and fluent Myanmar |
| dominant | B2 adjective | 1 / 188 | Ordinary market-power sense, not demonstrated C1 |
| evaluation | B2 noun | 1 / 222 | Ordinary programme assessment; process versus result in Myanmar |
| identical | B2 adjective | 2 / 316 | Example says documents *looked* identical but one lacks a signature; fails to demonstrate actual exact identity |
| implement | B2 verb | 2 / 320 | Ordinary plan-implementation sense |
| inevitable | B2 adjective | 2 / 328 | Ordinary unavoidable-delay sense |
| interpretation | B2 noun | 2 / 348 | Explanation of data versus language interpreting |
| invasion | B2 noun | 2 / 351 | Ordinary forceful-entry sense |
| precisely | B2 adverb | 2 / 475 | Ordinary accuracy sense |
| probability | B2 noun | 2 / 483 | Everyday likelihood versus technical probability |
| sustainable | B2 adjective | 3 / 613 | Environmental resource sense; packaging context alone does not establish C1 |

Machine-readable [source packet](draft/CEFR-1000-OXFORD-C1-B2-CONFLICT-TWELVE-2026-10-28.json) retains **all twelve original English definitions, Myanmar meanings, example sentences, shortlist source paths/indexes/blob SHAs, official publisher URL, observation date, PDF locators, risks and independent review tasks**. Canonical provisional shortlist Git blob remains `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; no provisional words or approval flags were changed.

## Release-readiness safeguards and execution honesty

- Added [fail-closed provenance auditor](tools/audit_cefr_1000_oxford_c1_b2_conflict_twelve.py) with **26 authored negative mutations** (publisher/CEFR/POS/page/line forgery, changed English/Myanmar/example/provenance, duplicate/missing rows, false signoff, and erased risk). Authored tests are **not claimed passed** until their actual CI conclusions and logs are inspected.
- Integrated the auditor into **six parallel GitHub Actions structural matrix jobs** (A1/A2/B1/B2/C1/ALL); the ALL job additionally runs negative mutations. Integrated the same self-test into the documentary **no-deploy** workflow.
- Added an **empty** `oxford_c1_b2_conflict_twelve_review_receipts` collection to release evidence, and a new launch blocker requiring separate independent, content-hash-bound **C1 exact-sense** reconciliation for every retained flagged entry, with a substantive explanation of the Oxford B2 discrepancy and revised definition/example. No receipts were manufactured.
- New staging commits include packet `3bb23fdb85defecabc5cee06e57a60662daada58`, auditor `6c9c67491c48e21adffb9782cbe89bce4fe32632`, workflows `64c2e83ec2775c3765539443899518dfac2cd4fb` and `b885dd7fa0695c3dc217cdb4557cd0dc4445fa94`, ledger `e69a27c71ee83a96d2abd7799152b36215abdeb4`, and release-gate wording fix `111e02075cff93f6f238956fe509874d409acb6d`.
- **New GitHub Actions run IDs, conclusions and logs have not been retrieved; do not mark this new code as CI PASS.** Previously verified structural run [40658480451](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40658480451) and documentary no-deploy run [40658480572](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40658480572) **predate these changes**.
- Direct main-versus-staging Git blob SHA comparison found **seven named protected production files identical**: `content.js`, `ielts-vocabulary-data.js`, `audio-manifest.js`, `audio-player.js`, `audio-integration.js`, `privacy-tools.js`, `site-config.js`. This does **not** exhaustively verify the entire `audio/` tree or prove production device/browser behavior.

## Exact counts and release blockers

| Level | First-pass English/Myanmar/example written | Independently approved | Final both-voice George/Emma listening signoffs |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

Missing: human-independent exact-sense CEFR/English/Myanmar/example review, approved 1,000-word release manifest, complete British George/Emma headword and example audio with **actual listening signoff**, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting constraints, complete production asset verification, and confirmed public deployment. Preserve the **54 existing lessons**, separate **IELTS 1,000-word bank**, established production George/Emma audio and privacy. **Do not publish.**
