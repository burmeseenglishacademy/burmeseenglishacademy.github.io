# Burmese English Academy — batch25 staging checkpoint (25 October 2026, Singapore)

**HOLD: UNVERIFIED BILINGUAL DRAFTS. NO MERGE, NO CEFR AUDIO RELEASE, NO PRODUCTION DEPLOYMENT.**

## Substantive changes made in this iteration

1. **50 original first-pass bilingual vocabulary drafts** written in `draft/A2-C1-EDITORIAL-BATCH25.json`: A2 **14**, B1 **14**, B2 **16**, C1 **6**. Each contains a learner-facing English definition, provisional POS and level, original Myanmar meaning and original grammatical usage example. These are human-readable AI-assisted *drafts*, **not** independently validated senses, translations, examples or CEFR assignments.
2. **50 separate source-evidence review packets** in `draft/A2-C1-REVIEW-TASKS-BATCH25.json`. English dictionary sense/POS, independent Myanmar translation, example/collocation, sense-specific CEFR evidence and George/Emma listening + real-device iPhone Safari are **five separate pending stages**. Cambridge dictionary links are **unvisited lookup leads**, not observed source findings. Reviewer identities, evidence and dates are blank.
3. **12 reversible candidate quarantines** in `draft/A2-C1-QUARANTINE-BATCH25.json`: A2 `recent`, `centre`, `active`; B1 `dating`, `tech`, `express`; B2 `alexander`, `mac`, `min`; C1 `hiv`, `forty`, `sheep`. These hold wrong/rare WordNet senses, names, acronyms or implausible tiers for later independent adjudication. They are **not** source-verified rejections.
4. Added `tools/audit_cefr_batch25_review_tasks.py` and `.github/workflows/cefr-batch25-review-qa.yml`: five parallel A2/B1/B2/C1/ALL **read-only structural checks**, scoped to staging paths, with no publishing steps. Checks enforce candidate POS/level alignment, unique new headwords, no draft/quarantine collisions, pending five-stage flags, empty observed evidence, zero approvals and empty staging release entries.

## Exact unique written inventory — all UNVERIFIED

| Provisional level | Target | Unique first-pass drafts | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 446 | 0 | 254 |
| B1 | 1,000 | 446 | 0 | 554 |
| B2 | 1,300 | 441 | 0 | 859 |
| C1 | 1,500 | 332 | 0 | 1,168 |
| **Total** | **5,000** | **2,165** | **0** | **2,835** |

A2–C1 unique written = **1,665**; A1 unique written = **500**; 182 historical duplicate rows in older A2–C1 draft files are excluded from unique totals. A2–C1 distinct held candidates = **387**. These totals were asserted by the real batch25 ALL job log at the commit below; they **do not** indicate linguistic accuracy.

## GitHub commits, actual CI and test logs

- Bilingual 50-entry draft: `807913bce6dc9bb01e3fca76b1fa0bcc6e066028`.
- Five-stage independent review packets: `d64314b9524b16d022bf2cb22fcf85b63cf12356`.
- Candidate quarantine: `dfa5b7452e47dfa5e1b302c8ffad2f1db0d5b5a7`.
- New structural auditor: `324b4d38522766ef996ca3bb0d5560838ecbf9c8`.
- Parallel workflow: `175a2312a8d1ee89e1eb0500e77190a6ad1e01a7`.
- Fixes made **after inspecting real failing job logs**: `4eb55196d0c2ff58dae9e3475aa6cfffe0a018c6` (B2 expected 16), `606b6dd362d3abb76315d8f332e05e2bfdbb5ea1` (review task map expected 50).
- First real batch25 run [40153581063](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40153581063) **failed** due to stale B2 count assertion; second [40153600018](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40153600018) **failed** due to stale review packet count assertion. These failures were not concealed.
- **Latest inspected real run [40153625371](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40153625371)** at `606b6dd362d3abb76315d8f332e05e2bfdbb5ea1`: **completed/success**. Inspected all five actual job statuses and decoded their job logs: A2 `121050169360`, B1 `121050169273`, B2 `121050169198`, C1 `121050169287`, ALL `121050169306` — all **completed/success**. ALL log: `A2=446 B1=446 B2=441 C1=332 total=1665; independent approvals=0`; `A1-C1 written=2165; first drafts outstanding=2835; legacy duplicate rows=182`; `50 drafts, 12 holds, zero approvals; no audio/deploy`.
- Compared staging base `0f6b423e1cd3972df31dd162ac048d2b63cb7281` to `4eb55196d0c2ff58dae9e3475aa6cfffe0a018c6`: six staging commits, only five added files in `draft/`, `tools/`, `.github/workflows/` (the last auditor fix and this checkpoint are subsequent). Production `main` head independently read as `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged at that inspection.

## Editorial integrity and release blockers

- All English senses, Myanmar meanings, examples and CEFR tiers remain **unreviewed by an independent source-based linguist**. The C1 words `inter`, `exhibit`, `marathon`, `ion`, `par`, `podcast` especially require sense-specific level evidence. A2 `nature`, `global`; B1 plural `relations`; B2 `sudden`, `enterprise` also require level/lemma scrutiny and possible re-tiering. No source pages were consulted for this batch; a green CI cannot certify these editorial decisions.
- The existing 54 lessons, 1,000 IELTS vocabulary bank, production George/Emma audio, UI and privacy remain untouched by the batch25 staging change set. `cefr-vocabulary-data.js` retains `entries:[]`.
- **No** new CEFR George/Emma audio was generated, listened to, or validated. **No** browser/mobile end-to-end, physical iPhone Safari, or hosting bandwidth/storage release verification was performed. **No** production publication occurred.
- **Release remains HOLD:** **2,835** first-pass entries unwritten; **0/5,000** independently approved; full CEFR pronunciation generation/listening and real-device QA incomplete; hosting clearance and production deployment unconfirmed. Do not merge or notify project completion.
