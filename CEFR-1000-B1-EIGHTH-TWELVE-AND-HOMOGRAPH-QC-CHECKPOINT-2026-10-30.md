# CEFR 1,000 — B1 eighth twelve and exact-sense homograph review (30 October 2026)

**Scope:** USER-APPROVED 1,000 TOTAL (A1/A2/B1/B2/C1 = 200 each). **Branch:** `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED / STAGING ONLY. This is publisher word/POS research, **not** independent English/Myanmar/example/CEFR approval.

## Direct publisher observations

Official Oxford University Press [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), opened and inspected on **2026-10-30**. The [12-record evidence packet](draft/CEFR-1000-OXFORD-B1-EIGHTH-TWELVE-AND-FOUR-SENSE-LEADS-2026-10-30.json) retains each word's exact PDF page/line, excerpt, original English definition, Myanmar meaning, original example, source blob SHA/index, and editorial hold.

| B1-draft entry | Oxford word/POS | PDF page (1-based), extracted line (0-based) | Review risk |
|---|---|---|---|
| channel (noun) | B1 | 7, 1887 | TV channel versus waterway/communication |
| fat (adjective) | A1 | 2, 275 | animal body-fat sense; avoid stigmatizing person examples |
| royal (adjective) | B1 | 9, 2401 | monarchy/institution versus narrower family-only Myanmar |
| serve (verb) | A2 | 6, 1601 | serving breakfast versus military/legal/sports |
| wonderful (adjective) | A1 | 4, 889 | intensity and natural Myanmar emotional nuance |
| bottom (noun) | A2 | 4, 1008 | lowest part inside a bag versus other meanings |
| lie2 (verb, knowingly say falsehood) | B1 | 8, 2186 | **HOMOGRAPH:** not A1 lie1 (recline) |
| square (noun) | A2 | 7, 1651 | geometric shape versus public square/adjective |
| surface (noun) | B1 | 10, 2488 | physical tabletop versus land/water or verb |
| supply (noun) | B1 | 9, 2485 | available quantity versus emergency supplies or provision |
| waste (verb) | B1 | 10, 2564 | wasting water versus refuse noun/adjective |
| strength (noun) | B1 | 9, 2472 | physical power versus material/moral strength |

Publisher distribution: **A1 2, A2 3, B1 7**. Five B1-draft word/POS level discrepancies require independent human exact-sense decisions; matching word/POS labels also require independent sense review.

## Four directly opened dictionary sense leads

- [lie2, knowingly say falsehood](https://www.oxfordlearnersdictionaries.com/definition/english/lie2_1), page text lines 88–122: past tense **lied**, participle **lied**, example grammar `lie about something`. Distinct from [lie1, recline](https://www.oxfordlearnersdictionaries.com/definition/english/lie1_1), whose past is **lay** and participle **lain**. **Oxford PDF lists lie2 B1, dictionary badge displays B2**: unresolved publisher-surface conflict; do not automatically retier.
- [channel noun](https://www.oxfordlearnersdictionaries.com/definition/english/channel_1), lines 103–154: TV station sense aligns with draft documentary example, not waterway.
- [supply noun](https://www.oxfordlearnersdictionaries.com/definition/english/supply_1), lines 109–133: available quantity (e.g., water) aligns with draft, but draft Myanmar `ထောက်ပံ့ပစ္စည်း` can imply material supplies; independent reviewer should consider context-specific `ရရှိနိုင်သော သန့်ရှင်းသည့်ရေပမာဏ` (unapproved editorial suggestion).
- [waste verb](https://www.oxfordlearnersdictionaries.com/definition/english/waste_2), lines 112–122: using more than necessary aligns with the draft's water example; not the noun meaning refuse.

These are direct publisher dictionary *sense leads*, not independently signed exact-sense CEFR evidence. The alternative Myanmar suggestion is **unapproved**, not an edit to the frozen shortlist.

## Structural QC and release safeguards

Added `tools/audit_cefr_1000_oxford_b1_eighth_twelve.py` to verify immutable publisher PDF locators, dates, excerpts, dictionary anchors, original source blob and bilingual snapshots, zero independent approvals, and editorial holds. It performs adversarial source, provenance, bilingual, homograph, reviewer-receipt and release-flag mutation tests. Wired into **six parallel CEFR level jobs** and the documentary no-deployment workflow; GitHub Actions run conclusions and logs must be checked separately before calling CI successful.

Cross-batch **expected** direct Oxford word/POS coverage: A1 **195/200**, A2 **96/200**, B1 **108/200**, B2 **94/200**, C1 **75/200** = **568/1,000** distinct, **587** source observations, **432** unobserved. Expected independent reviewer priorities: **3 unlisted**, **22 publisher higher**, **188 publisher lower**, **355 word/POS matches requiring exact-sense review**, **432 unobserved**. These are source-research counts, not independently approved entries, and remain subject to actual CI confirmation.

| Level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

**Release blockers:** human-independent exact-sense CEFR, English, fluent Myanmar and example reviews; final British George/Emma headword and example audio plus **real listening** signoff (0/1,000); approved-corpus browser/mobile regression; physical iPhone Safari review; measured GitHub Pages hosting limits; final protected-production asset comparison and confirmed live deployment. Existing 54 lessons, separate IELTS 1,000-word bank, production George/Emma audio and privacy must remain intact. **No merge, main change or publication is authorised by this checkpoint.**

## Verified GitHub Actions results

- [Structural run 40988041949](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40988041949) at code SHA `f248ce0d60cd7ebf9e4b597d88db351dade1ea47`: **SUCCESS**, all six A1/A2/B1/B2/C1/ALL jobs independently checked as successful. Actual ALL-job logs show **386/386** new eighth-B1 forged-source/bilingual/homograph/receipt mutations and **145/145** reviewer-handoff mutations rejected. Source coverage and reviewer priority reconciled to **568 distinct / 587 observations / 432 unobserved**, with **3 unlisted / 22 higher / 188 lower / 355 word-POS matching but exact-sense unverified / 432 unobserved**.
- [Documentary no-deployment run 40988050201](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40988050201) at code SHA `bf1af0f3fb5f860101129bee172d58b24d72ae72`: **SUCCESS as report-only**, with **386/386** new mutations rejected; actual logs state **0/1,000** independent source reviews, **0/1,000** dual-voice listening receipts, **production confirmed false**, and **protected production assets untouched**.
- Compared staging changes against prior verified staging SHA `7fbb027a030ef2baac8465c2295ce6715a6b607b`: only the research packet, auditor, two cross-batch audit scripts, two staging CI workflows and this checkpoint were modified at comparison time. No existing 54-lesson, IELTS, George/Emma audio, privacy or main-branch assets changed. These structural/documentary CI passes **do not** clear any real human, physical-device, audio-listening, hosting or deployment gate.
