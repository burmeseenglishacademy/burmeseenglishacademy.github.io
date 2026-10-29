# CEFR 1,000 staging-only checkpoint — B1 sixth Oxford twelve and retired legacy 5,000 generator
**Observed:** 2026-10-29 (Singapore). **Scope:** user-approved **1,000 total**, A1/A2/B1/B2/C1 **200 each**. **Branch:** `cefr-5000-bilingual-qa-staging` (name retained). **Release:** **BLOCKED — STAGING ONLY**.

## Primary-source observations (NOT independent exact-sense review)
Directly inspected Oxford University Press's [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on 2026-10-29. New immutable-provisional-snapshot research packet: [B1 sixth twelve](draft/CEFR-1000-OXFORD-B1-SIXTH-TWELVE-2026-10-29.json). PDF page is **one-based**; extracted text line is **zero-based**. The publisher supplies word/part-of-speech list levels, **not independent verification of the precise draft sense or B1 curriculum placement**.

| B1-draft headword | Oxford word/POS level | PDF page / extracted line | Oxford PDF excerpt |
|---|---|---|---|
| flight | A1 | 2 / 297 | `flight n.` |
| primary | B1 | 9 / 2320 | `primary adj.` |
| activity | A1 | 1 / 9 | `activity n.` |
| application | B1 | 7 / 1821 | `application n.` |
| complex | B1 | 7 / 1919 | `complex adj.` |
| condition | A2 | 4 / 1072 | `condition n.` |
| freedom | B2 | 11 / 2877 | `freedom n.` |
| interview | A1 | 2 / 401 | `interview n., v.` |
| location | B1 | 8 / 2197 | `location n.` |
| accept | A2 | 4 / 912 | `accept v.` |
| attempt | B2 | 10 / 2645 | `attempt n., v.` |
| distance | A2 | 5 / 1137 | `distance n.` |

**Twelve distinct, previously unobserved B1-draft entries:** three publisher A1, three A2, four B1, two B2. Eight word/POS level discrepancies require genuine human exact-sense reconciliation. The packet preserves the **frozen** English definition, fluent-Myanmar candidate, original example, historical source path/index/blob SHA, publisher URL/date/page/line, explicit editorial risks and unapproved reviewer tasks. Examples of open issues: `application` formal request vs software, `condition` physical state vs requirement/medical condition, `freedom` personal rights vs ability, `interview` job vs media, `attempt` noun countability and `location` natural British example wording. These are editorial tasks, not silent corrections or approvals.

## Verified consolidated research coverage
| Draft level | First-pass written | Independently approved | Distinct Oxford word/POS observations |
|---|---:|---:|---:|
| A1 | 200 | 0 | 112 |
| A2 | 200 | 0 | 72 |
| B1 | 200 | 0 | 84 |
| B2 | 200 | 0 | 70 |
| C1 | 200 | 0 | 51 |
| **Total** | **1,000** | **0** | **389** |

The audited 28 Oxford research packets have **408 observations for 389 distinct provisional headwords**, including 19 repeated observations that do **not** increase coverage. **611** remain without direct observations in the audited packets. Review handoff priorities: **152** publisher-lower, **13** publisher-higher, **3** not found in the inspected core lists (**not a CEFR classification**), **221** word/POS matches still exact-sense unverified, and **611** no-direct-observation entries. All **1,000** remain on editorial hold.

## Fail-closed source and release safety
- Added [B1 sixth-twelve source-integrity auditor](tools/audit_cefr_1000_oxford_b1_sixth_twelve.py), cryptographically bound to the frozen shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. **144/144** negative mutations (source, CEFR, English/Myanmar/example, historical provenance, fake review) rejected in actual CI logs.
- Updated cross-batch auditor and the content-bound 1,000-entry human reviewer handoff to require **389** distinct observations and **611** remaining research gaps. Existing **145/145** reviewer-handoff adversarial mutations still rejected; **36** historical locator-only excerpts remain cross-referenced, not double-counted.
- Integrated new checks in six parallel A1/A2/B1/B2/C1/ALL structural lanes and documentary no-deployment gate.
- Retired the superseded **5,000-candidate generation workflow** in `.github/workflows/cefr-source-audit.yml`: it is now a **read-only, no-deployment, 1,000-only scope guard**. It no longer downloads WordNet to generate 5,000 candidates, persists old candidates, commits from Actions or holds `contents: write`. The historical branch name remains unchanged.

### Actual GitHub Actions verification
- [Structural six-lane run 40845329395](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40845329395) — commit `7c314b5a481945db97fb3607c3f5157eb9891993`; **SUCCESS**, all **six job conclusions SUCCESS**, including **144/144** new mutations, 145 content-bound handoff mutations and protected production diff **PASS**. B1 sixth-twelve auditor was present in this run.
- [Documentary report-only run 40845341773](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40845341773) — commit `11456dfe00abdba2da3b6bb9f79dc9d42693a3ff`; **SUCCESS** as a *test of the fail-closed documentary gate*, **not** release readiness. Logs confirm 144/144 rejected mutations, 0 independent approvals, 0 final audio listening and protected production diff **PASS**.
- [Legacy workflow replacement scope-guard run 40845400849](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40845400849) — commit `4278563e16fdb2030023c5a98a7d91b3dfd73403`; **SUCCESS**. Logs confirm exactly 1,000 frozen provisional candidates, 200 per level, 0 independent approvals, 20/20 cross-batch negative tests and no legacy 5,000-generation/repository-write/deploy step.

Earlier intermediate runs on partial commits failed while coverage/handoff counts were not yet reconciled; the three completed final runs above are the verified repaired results. **CI success validates structure and safeguards, never human linguistic accuracy or production release.**

## Remaining non-negotiable release blockers
- Human-independent English definition, fluent Myanmar, original example grammar and source-backed **exact-sense CEFR** signoff: **0/1,000**; no fabricated reviewer receipts.
- Final British George **and** Emma headword **and** example audio generation, matching digests and **real listening signoff**: **0/1,000 final verified**; do not infer this from existing production audio.
- Approved-corpus desktop/browser and mobile regression: **not verified**. Physical iPhone Safari and real on-device audio review: **no evidence**.
- GitHub Pages hosting size/bandwidth measurements for the approved release: **no verified evidence**.
- Final independent privacy/production-asset verification and confirmed production deployment: **not completed**. Staging GitHub Actions diff confirms protected 54 lessons, separate IELTS 1,000 bank, established George/Emma production audio and privacy assets were **not changed** in this staging work.

**NO MERGE, MAIN MODIFICATION, PUBLICATION OR DEPLOYMENT. Release BLOCKED / STAGING ONLY.**
