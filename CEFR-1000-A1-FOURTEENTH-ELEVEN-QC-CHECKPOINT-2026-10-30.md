# CEFR 1000 A1 fourteenth direct Oxford packet — 30 October 2026

**STAGING ONLY.** Exactly 1,000 provisional words, A1–C1 200 each; zero independently approved. Branch remains `cefr-5000-bilingual-qa-staging`; neither main nor production assets are modified.

## Official Oxford source observations

On **2026-10-30**, the [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) was directly inspected. One-based PDF pages and zero-based extracted lines follow. Publisher **word/POS** A1 evidence does not independently prove exact-sense A1 or translation/example quality.

| Draft | Oxford PDF page | Extracted line | Publisher excerpt | Human-review risk |
|---|---:|---:|---|---|
| do | 1 | 216 | `do1 v., auxiliary v.` | Publisher lists lemma do (verb/auxiliary), not does/did as separate headwords. Draft uses lexical do homework; distinguish auxiliary usage. |
| four | 2 | 309 | `four number` | Cardinal four is A1; example counts chairs. Review Burmese classifier usage and numeral headword policy. |
| five | 2 | 295 | `five number` | Cardinal five is A1; example counts books. Myanmar ငါး also denotes fish, so require context-sensitive bilingual review. |
| six | 3 | 703 | `six number` | Cardinal six is A1; example counts students. Check numeral pronunciation and Myanmar classifier. |
| seven | 3 | 682 | `seven number` | Cardinal seven is A1; seven days in a week is grammatical, but exact example and translation need independent review. |
| eight | 1 | 236 | `eight number` | Cardinal eight is A1; example at eight refers to eight o'clock, not a quantity of eight objects. Sense/context mismatch requires review. |
| nine | 2 | 523 | `nine number` | Cardinal nine is A1; shop opens at nine refers to clock time, not counting objects. Independent exact-context check required. |
| ten | 3 | 773 | `ten number` | Cardinal ten is A1; example counts pencils. Check Myanmar quantity/classifier and British pronunciation. |
| sleep | 3 | 708 | `sleep v.` | Oxford A1 lists verb sleep; draft I sleep eight hours may be less idiomatic than I sleep for eight hours/I get eight hours' sleep. Human grammar review required. |
| wake | 4 | 854 | `wake v.` | Oxford A1 lists wake verb; draft I wake at seven omits up and can mean wake from sleep. Check wake/wake up usage and Myanmar နိုး vs အိပ်ရာထ. |
| speak | 3 | 727 | `speak v.` | Oxford A1 lists speak verb; example I speak English at school uses language ability/use, not simply saying words aloud. Definition-example sense alignment needs review. |

All 11 research records preserve the original frozen English/Myanmar/example, historical source path/index/blob SHA, publisher URL, observation date and independent human reviewer task. They remain on editorial hold; no automatic rewrites or approvals.

**Remaining five A1 source gaps:** `is`, `are`, `does`, `did` are inflected forms of Oxford-listed `be`/`do`, not independent Oxford headwords; `rabbit` was not located in the inspected Oxford 3000/5000 core lists and cannot be inferred as a CEFR level from that absence. A human reviewer must decide the learner-facing lemma policy, whether inflected forms deserve separate teaching entries under the 200 unique headword/sense rule, and what to do with rabbit. Oxford lists `be v., auxiliary v.` on PDF page 1 extracted line 66 and `do1 v., auxiliary v.` on page 1 line 216; these lemma observations do **not** count as observations for the four inflected draft headwords.

**Grammar and bilingual risks:** `five` (ငါး) has a fish homograph in Myanmar; `eight`/`nine` examples refer to time rather than object quantity; `sleep eight hours` may need a preposition; `wake at seven` vs `wake up/get up`; `speak English` is not equivalent to merely saying words aloud. All remain unresolved pending independent review.

## Staging structural/release readiness

Added fail-closed source-bound packet auditor with **219 negative mutations** (10 general plus 19 per record), and wired it into six parallel CEFR structural lanes and documentary no-deployment gate. Coverage expected after this packet: **A1 195/200, A2 84/200, B1 84/200, B2 70/200, C1 51/200 = 484/1,000 distinct**; **503 total Oxford observations**; **516 without direct word/POS observations**. Reviewer priority counts expected: 3 unlisted, 15 publisher-higher, 157 publisher-lower, 309 matching word/POS but exact-sense unverified, 516 without observations. These are source-research counts, not independent review.

Written/independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Real George/Emma listening signoffs **0/1,000**. Final audio generation/listening, independent exact-sense/English/Myanmar/example review, browser/mobile regression, physical iPhone Safari, measured GitHub Pages limits, protected production asset verification and production deployment remain unverified. **No merge or deployment permitted.**

CI runs and job conclusions are not asserted until retrieved from GitHub Actions.
