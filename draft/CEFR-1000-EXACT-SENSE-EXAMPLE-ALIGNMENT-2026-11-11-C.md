# CEFR-1000 exact-sense/example alignment review queue — 2026-11-11 C

**Scope and authority.** AI-assisted editorial analysis only, not independent review, not publisher CEFR verification, and not release approval. Read directly from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`) on `cefr-5000-bilingual-qa-staging` on **2026-11-11**. All shortlist entries remain untouched, held, and unapproved. The proposed examples below are editorial alternatives, **not** signed-off or imported into the shortlist.

## High-priority exact-sense conflicts

| Entry / original provenance | Observed first-pass text | Risk and proposed correction for independent review |
| --- | --- | --- |
| **C1 anachronism**, noun; `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json`, index **9**, blob `7eaf88b9ed7687b26ccde713262f10fb209743a8` | Definition: “Something that seems to belong to a different historical period.” Example: “The old payment machine looked like an anachronism in the modern shop.” | The example illustrates an *outdated object in a contemporary setting*, not necessarily a **historical-period error**. Do not transfer Oxford's **History C2** topic tag for the historical sense to this example, or infer C1 from the generic definition. Decide which sense is intended and seek exact-sense CEFR evidence; otherwise replace with an independently reviewed C1 candidate. Myanmar currently describes belonging to a different era, but an idiomatic rendering of *outmoded relic* may differ. |
| **B2 portion**, noun; `draft/A2-C1-EDITORIAL-STARTER.json`, index **177**, blob `b04dd85db5cfae131c25aa4c73109778991b6fdc` | Definition: “A part or amount of something larger.” Myanmar: “အစိတ်အပိုင်း၊ အစားအစာတစ်ပွဲစာပမာဏ”. Example: “The waiter brought a small portion of rice.” | Definition and translation combine **part/share** with **serving of food**; the example selects the serving sense. For this example, a narrower candidate definition is “An amount of food served to one person.” Myanmar candidate “တစ်ယောက်စာ စားစရာပမာဏ” requires native review. Independently check CEFR for the food-serving sense specifically; do not borrow a level from the abstract part/share sense. |
| **A2 maybe**, adverb; `draft/A2-C1-EDITORIAL-STARTER.json`, index **292**, same blob | Definition: “Possibly; used when something is not certain.” Myanmar: “ဖြစ်နိုင်သည်၊ ဖြစ်ကောင်းဖြစ်မည်”. Example: “Maybe we can visit the museum on Sunday.” | This sentence can express a **tentative suggestion**, not merely probability. A context-specific Myanmar candidate is “တနင်္ဂနွေနေ့မှာ ပြတိုက်ကို သွားကြည့်လို့ရမလား မသိဘူး” (conversational, not necessarily literal); native reviewer must choose appropriate register. Verify Cambridge/Collins A2 *suggestion* use versus Oxford's lower topic tag; distinguish one-word **maybe** from **may be**. |
| **B1 doubt**, noun; `draft/A2-C1-EDITORIAL-STARTER.json`, index **212**, same blob | Example: “I have some doubt about the figures.” | Grammatically possible, but the mass-noun construction may sound less idiomatic than “I have doubts about the figures.” Alternative changes singular to plural; verify whether the headword example policy permits inflection and confirm exact sense. Do not mark a grammatical failure solely because of stylistic preference. |
| **C1 integrity**, noun; `draft/A2-C1-EDITORIAL-STARTER.json`, index **330**, same blob | Definition: “The quality of being honest and following strong moral principles.” Example: “A leader's integrity matters when difficult decisions arise.” | Meaning and example appear semantically aligned, but **C1** is not demonstrated by the shortlist itself. Must source-check the moral-honesty sense rather than structural-wholeness sense; Myanmar “ဖြောင့်မတ်ရိုးသားမှု၊ ကိုယ်ကျင့်တရားခိုင်မာမှု” requires independent fluency review. |

## Source reconciliation references (not new publisher observations)

Prior staging evidence report `draft/CEFR-1000-PUBLISHER-EVIDENCE-RECONCILIATION-2026-11-11.md` records publisher pages observed **2026-11-11**:
- Cambridge **maybe**: https://dictionary.cambridge.org/dictionary/learner-english/maybe
- Collins **maybe**: https://www.collinsdictionary.com/dictionary/english/maybe
- Oxford **maybe**: https://www.oxfordlearnersdictionaries.com/us/definition/english/maybe_1
- Oxford **anachronism**: https://www.oxfordlearnersdictionaries.com/us/definition/english/anachronism
- Cambridge **anachronism**: https://dictionary.cambridge.org/de/worterbuch/englisch/anachronism
- Collins **anachronism**: https://www.collinsdictionary.com/dictionary/english/anachronism

These links support **reopening and checking** exact senses; no new live publisher verification was performed in this review. Topic tags and CEFR entry labels must not be conflated.

## Human-independent task specification

For each row, an independent English reviewer should record exact lemma/POS/sense, whether definition and original example match, a corrected original example where needed, source URL, publisher label or explicit “no CEFR evidence”, observation date and reviewer identity. A separate fluent Myanmar reviewer must judge the **same sense and context** for meaning and example translation; reviewers must be independent of the content author. Preserve immutable original provenance and record changes without rewriting the original source. Do not approve a level when only a different sense is labeled. Any replacement must preserve 200 entries per level and cross-level sense uniqueness, and must pass independent review before release.

## Counts and release gates

| CEFR | Provisional written | Independently checked/approved |
| --- | ---: | ---: |
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

Historical GitHub Actions run [42953145166](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42953145166) for SHA `882e6a62859df59c7644b50d431f4da0d131a01e` had seven jobs reported `success` by jobs API (rechecked **2026-11-11**); this does not validate this new documentation commit. Full raw logs and current-commit results are not established here. Final 4,000 George/Emma headword/example audio assets, genuine listening, browser/mobile regression, physical iPhone Safari evidence, hosting, independent reviews, deployment and production asset preservation remain blocking. **Staging only. Do not publish or alter main.**
