# CEFR 1,000 — A1 tenth twelve Oxford word/POS and grammatical-role QC (staging only)

**Observed:** 2026-10-29. **Branch:** `cefr-5000-bilingual-qa-staging`. **Scope:** approved project size **1,000 total** (A1/A2/B1/B2/C1 **200 each**), not the superseded 5,000. **Release status: BLOCKED / STAGING ONLY.**

## Direct source-backed work (not human signoff)

Inspected the official [Oxford University Press Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-29**, directly locating **12 previously unobserved A1 draft words**. Preserved the exact short word/POS excerpt, publisher URL, observation date, **one-based PDF page / zero-based web extracted line**, original English definition, Myanmar meaning, original example, historical source-path/index/Git blob provenance and pending independent-review task in [the immutable-source-bound research packet](draft/CEFR-1000-OXFORD-A1-TENTH-TWELVE-2026-10-29.json). No publisher PDF entry proves the exact intended sense or that a Burmese translation/example is independently correct.

| A1 draft | PDF page / extracted line | Oxford A1 POS | Human reviewer must resolve |
|---|---|---|---|
| where | 4 / 875 | adv., conj. | Draft generic question-word POS; example uses interrogative adverb. |
| when | 4 / 874 | adv., pron., conj. | Interrogative time adverb in example; exclude conjunction use. |
| why | 4 / 879 | adv. | Interrogative reason adverb, not a formal 'question word' POS. |
| what | 4 / 873 | pron./det. | Example uses interrogative pronoun; distinguish determiner. |
| who | 4 / 878 | pron. | Interrogative person pronoun; distinguish relative use. |
| which | 4 / 876 | pron./det. | Example 'Which book' uses determiner. |
| yellow | 4 / 901 | adj., n. | Example uses adjective; distinguish noun. |
| pink | 3 / 596 | adj., n. | Example uses adjective. |
| orange | 3 / 558 | n., adj. | Example uses colour adjective, not fruit noun. |
| brown | 1 / 111 | adj., n. | Example uses adjective. |
| grey | 2 / 339 | adj., n. | British spelling grey; adjective in example. |
| purple | 3 / 627 | adj., n. | Example uses adjective. |

**Six formal POS discrepancies:** `where`, `when`, `why`, `what`, `who` and `which` are labelled only `question word` in the draft. Oxford gives adverb, pronoun, determiner and/or conjunction labels. The actual example usage must be analysed before editing the final shortlist. The six colour words have Oxford A1 adjective labels but still require sense, translation and example review. The draft's `is`, `are`, `does` and `did` are also inflected-form/headword-policy risks: Oxford lists base headwords `be` and `do` (PDF pages 1 and 1, extracted lines 66 and 216), so reviewers must decide whether those draft forms belong as distinct headwords without automatic replacement. All proposed editorial work remains **unapplied**.

## Verified fail-closed tests and provenance

Added [tenth-batch auditor](tools/audit_cefr_1000_oxford_a1_tenth_twelve.py) to reconstruct all 12 records from the frozen 1,000-entry shortlist and fixed directly observed publisher page/line/POS anchors, with strict field equality. It rejects count-preserving duplicates, invented human receipts, altered English/Myanmar/examples, false levels, changed source URLs/locators, historical Git provenance drift, editorial risk tampering and forged release flags.

- [Structural GitHub Actions run **40878191825**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40878191825), head `f70d290776231f590c32ea212d9e2f5d4e09cf1f`: **SUCCESS**, all six A1/A2/B1/B2/C1/ALL jobs individually concluded **success**. Actual ALL-job logs confirm **238/238** new negative mutations rejected, **145/145** full reviewer-handoff mutations rejected, source-coverage reconciliation and protected production assets unchanged.
- [Documentary no-deployment run **40878209627**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40878209627), head `b94994c4603b8b06c689d6994eda2dd2d9757794`: **SUCCESS AS REPORT-ONLY**. Logs confirm 238/238 new mutations rejected, all release blockers retained, and no production publication.
- Compared previous staging checkpoint `8098c6024c9b10261efc35cc8cba575fdef11013` against verified code head `b94994c4603b8b06c689d6994eda2dd2d9757794`: **six staging-only files changed** (research packet, auditor, two existing auditors and two no-deploy workflows); no protected production file changed. The prior CI runs on intermediate commits were not used to assert final success.

## Exact counts and mandatory release blockers

| Level | First-pass written | Direct Oxford word/POS observed | Human-independent approved |
|---|---:|---:|---:|
| A1 | 200 | 148 | 0 |
| A2 | 200 | 72 | 0 |
| B1 | 200 | 84 | 0 |
| B2 | 200 | 70 | 0 |
| C1 | 200 | 51 | 0 |
| **Total** | **1,000** | **425** | **0** |

There are **444 recorded Oxford source observations** across **425 distinct headwords**; repeated observations do not inflate coverage. **575** have no direct Oxford word/POS observation in audited packets. The review queue has **152 publisher-lower**, **13 publisher-higher**, **3 unlisted**, **257 matching word/POS but exact-sense-unverified**, and **575 without direct observations**. The 12 new entries are Oxford A1 word/POS matches only, **not** independent English, Myanmar, example, sense, pronunciation or CEFR approvals.

**Final George/Emma real listening signoffs: 0/1,000.** No independently approved 1,000-entry release manifest, no final British George/Emma headword+example audio with real listening attestations, no approved-corpus desktop/mobile regression, no physical iPhone Safari review, no measured GitHub Pages hosting gate, and no confirmed production deployment. Existing 54 lessons, separate IELTS 1,000-word bank, George/Emma production audio and privacy remain protected. **No merge, main change or publication. Release BLOCKED / STAGING ONLY.**
