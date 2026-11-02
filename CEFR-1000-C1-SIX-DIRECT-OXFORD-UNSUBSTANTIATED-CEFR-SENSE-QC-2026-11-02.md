# CEFR 1,000 — six held C1 direct-Oxford exact-sense investigations (2 November 2026)

**Scope:** user-approved **1,000 total** (A1/A2/B1/B2/C1: 200 each), **not** the superseded 5,000-word plan. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED, staging only; zero independently approved.

## Publisher evidence observed directly on 2026-11-02

Six Oxford Advanced Learner's Dictionary English headword pages were opened directly and inspected. Source-line locators refer to the page text observed on this date. **None of these six Oxford entries supplied an observed headword/exact-sense CEFR C1 badge.** The unrelated Oxford *Topics* and *Word of the Day* footer badges must never be promoted into headword CEFR evidence. Direct Cambridge Dictionary English page requests for all six returned **HTTP 403**; no Cambridge exact-sense CEFR classification is asserted.

| Frozen C1 word | Oxford entry and inspected lines | Exact-sense / bilingual / grammar risk requiring independent resolution |
| --- | --- | --- |
| [coercion](https://www.oxfordlearnersdictionaries.com/definition/english/coercion) | 88–112; uncountable, formal noun | Oxford describes compulsion using force or threats; frozen English says *threats or pressure*. Ordinary social pressure must not automatically be equated with coercion. Frozen signed-agreement example is plausible but its legal conclusion is context-dependent. |
| [conundrum](https://www.oxfordlearnersdictionaries.com/definition/english/conundrum) | 88–109; noun | Oxford separates a difficult confusing problem from a playful word-riddle sense. Frozen housing/transport example is the problem sense, not the riddle sense. A B2 footer belongs to an unrelated Word-of-the-Day/topic item, **not** this word. |
| [corroborate](https://www.oxfordlearnersdictionaries.com/definition/english/corroborate) | 88–119; formal verb, often passive | Supporting a witness's account with photographs does not prove it conclusively. Oxford's *Scientific research c2* is a topic label, **not** a CEFR C2 headword classification. British headword IPA was observed; no George/Emma audio has been listened to. |
| [credence](https://www.oxfordlearnersdictionaries.com/definition/english/credence) | 88–110; uncountable, formal noun | **Priority definition/example mismatch:** Oxford distinguishes a claim's credibility from the act of believing it. Frozen *gave credence to* example concerns enhanced credibility; frozen definition/ Myanmar primarily teach belief or acceptance. |
| [deference](https://www.oxfordlearnersdictionaries.com/definition/english/deference) | 88–125; uncountable noun | Oxford describes behaviour showing respect. Frozen definition over-narrows this to accepting someone's judgement or status; waiting for elders' opinion may show respect without accepting it. |
| [delineate](https://www.oxfordlearnersdictionaries.com/definition/english/delineate) | 88–114; formal verb | Oxford includes describing, drawing or explaining in detail. Frozen contract example is detailed specification of responsibilities, not necessarily literal boundary marking. |

The [six-card source-bound research packet](draft/CEFR-1000-C1-SIX-DIRECT-OXFORD-RARE-SENSE-AND-CEFR-UNSUBSTANTIATED-2026-11-02.json) preserves original English definitions, Myanmar glosses, examples, exact historical `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json` indices **16, 18, 19, 20, 21, 22**, source Git blob `7eaf88b9ed7687b26ccde713262f10fb209743a8`, frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, dated publisher URLs, British IPA as transcribed from Oxford, original examples, risk notes, and six **unapproved** fluent-Myanmar/English/example alternatives. All remain on editorial hold; no independent review flags were changed.

## Mechanical safeguards, not linguistic approval

The [fail-closed six-card auditor](tools/audit_cefr_1000_c1_six_direct_oxford_unsubstantiated.py) checks exact 200-per-level quotas, 1,000 unique casefolded headwords, frozen source and packet Git blobs, historical bilingual identity, publisher host/access/line locators, absent exact-sense CEFR labels, all review holds, missing real audio and human receipts, and forged footer CEFR claims. Its synthetic mutation self-test is invoked only by the **ALL** structural lane and documentary no-deployment workflow; ordinary audit runs in parallel **A1/A2/B1/B2/C1/ALL** lanes. A passing job proves structural consistency only, not that any source is independently human-verified or any audio was heard.

**Current first-pass written / independently checked and approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**; total **1,000/0**. Final George/Emma audio generation and actual listening signoffs, independent English/Myanmar/example/exact-sense CEFR approval, deduplicated approved manifest, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages limits, protected production asset signoff and confirmed production deployment remain missing.

**RELEASE BLOCKED — STAGING ONLY.** No merge, main edit, publication, or change to the protected 54 lessons, separate IELTS 1,000-word bank, established production audio or privacy code.


## Verified GitHub Actions conclusions and logs (2026-11-02)

**Actually verified** [six-lane structural run 41371171713](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41371171713), testing commit `f0f51f8a34485efee690c9b4dd3389faf0422ca5`: **SUCCESS** across **A1, A2, B1, B2, C1 and ALL**. ALL job `125041755619` logs explicitly confirmed **219/219 synthetic negative mutations rejected** for this six-card Oxford source packet and **zero independent approvals implied**; ALL artifact ID `13109158685`.

**Actually verified** [documentary no-deployment run 41371171657](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41371171657) at the **same SHA**: **SUCCESS as report-only**, documentary job `125041755437` logs independently confirmed **219/219** mutations rejected. The readiness report explicitly **BLOCKED** missing 1,000 independent reviewer receipts, final approved manifest, real George/Emma listening, matched desktop/mobile Chromium and WebKit evidence, physical iPhone Safari, measured Pages hosting and final protected-asset signoff. Its production-file diff check passed for protected lessons, IELTS, established audio and privacy paths; blocker artifact ID `13109059136`.

**These successful CI jobs do not establish human-independent CEFR or Myanmar approval, actual listening, physical device testing, measured hosting or deployment. RELEASE BLOCKED — STAGING ONLY.**
