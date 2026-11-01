# CEFR 1,000 — Six source-supported alternatives for non-independent inflection slots (2 November 2026)

**STAGING ONLY — all alternatives are UNAPPROVED. No frozen shortlist edit, merge or publication.** The user-approved target is 1,000 TOTAL, **200 each** at A1, A2, B1, B2 and C1; not the superseded 5,000. Frozen shortlist Git blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

## Why this matters

The provisional 1,000 includes six held inflectional/comparative forms that the existing release validator does not allow to inflate a distinct-lexeme quota: **is, are, does, did** (A1), **better** (A2) and **worst** (B1). These can still be taught in grammar, but their slots need independently reviewed lexical replacements before the 200/level release quota can be met. The table below pairs **quota slots**, not synonyms. **No replacement decision is made.**

| Held original / slot | Candidate / proposed POS | Direct Oxford 3000 word/POS level | Oxford dictionary exact-sense observation | Proposed original example / Myanmar gloss (NOT independently reviewed) |
|---|---|---|---|---|
| is / A1 | **afraid**, adjective | [Oxford CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), extracted line **17**, A1 section | [Oxford afraid](https://www.oxfordlearnersdictionaries.com/definition/english/afraid), lines **88–115**; predicative adjective, *afraid of* | The child is afraid of the dark. — ကြောက်ရွံ့နေသော၊ ကြောက်သော |
| are / A1 | **angry**, adjective | Same Oxford PDF, line **31**, A1 | [Oxford angry](https://www.oxfordlearnersdictionaries.com/definition/english/angry), lines **88–121**; angry *about* something | She was angry about the delay. — စိတ်ဆိုးသော၊ ဒေါသထွက်သော |
| does / A1 | **answer**, noun | Same Oxford PDF, line **34**, A1; noun and verb both listed | [Oxford answer noun](https://www.oxfordlearnersdictionaries.com/definition/english/answer_1), lines **88–115**; response to a question | Please write your answer below. — အဖြေ၊ ပြန်လည်ဖြေကြားချက် |
| did / A1 | **airport**, noun | Same Oxford PDF, line **25**, A1 | [Oxford airport](https://www.oxfordlearnersdictionaries.com/definition/english/airport), lines **88–121**; transport facility | We arrived at the airport early. — လေဆိပ် |
| better / A2 | **ability**, noun | Same Oxford PDF, line **920**, A2 section | [Oxford ability](https://www.oxfordlearnersdictionaries.com/definition/english/ability_1), lines **88–123**; ability *to do* something | She has the ability to learn quickly. — လုပ်ဆောင်နိုင်စွမ်း၊ စွမ်းရည် |
| worst / B1 | **achievement**, noun | Same Oxford PDF, line **1803**, B1 section | [Oxford achievement](https://www.oxfordlearnersdictionaries.com/definition/english/achievement), lines **88–112**; countable successful accomplishment | Finishing the course was a big achievement for her. — ကြိုးစားအားထုတ်မှုဖြင့် ရရှိသည့် အောင်မြင်မှု |

**Source observation date:** 2026-11-02. The official Oxford CEFR PDF was directly inspected, as were the six linked dictionary entries. PDF lines are the web-extracted text locator, **not printed PDF page numbers**. The PDF supplies a **word + POS level**, not independent verification that a particular proposed definition/example is at that CEFR level. Dictionary senses and original examples still require an independent reviewer to confirm precise meaning, fluent Myanmar, grammar and pronunciation. Neither these publisher observations nor this audit constitute human-independent signoff.

## Integrity and scope

The [six-record research packet](draft/CEFR-1000-SIX-INFLECTION-SLOT-REPLACEMENT-CANDIDATES-2026-11-02.json) retains each held original's exact English definition, Myanmar meaning, example, original file path/index, historical source Git blob and all false review flags. It also retains the candidate's direct publisher URLs, extracted line locators, observation date, proposed bilingual content and unresolved sense risk. The candidates were checked as **absent from all 1,000 frozen headwords**, preventing obvious cross-level duplicates. Their actual suitability and any overlap with the separate IELTS bank are **not independently checked**.

The [fail-closed auditor](tools/audit_cefr_1000_six_inflection_slot_candidates.py) pins the packet Git blob `e2a3545e05f5f61c1c2f3c1bb734d8a73d33cc72` and shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; verifies six pair identities, original English/Myanmar/example/provenance, source URLs/lines, absence of candidates in the frozen shortlist, editorial hold and zero approvals. It includes **150 programmed synthetic tamper mutations**, not human linguistic reviews. The [staging six-lane GitHub Actions workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) now invokes the auditor in A1/A2/B1/B2/C1/ALL and its negative tests in ALL. **New CI job conclusions/logs are not yet independently retrievable; do not claim the 150 tests passed.** Earlier baseline structural run [41330436098](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436098) was SUCCESS for all six lanes, but predates these changes.

## Release-readiness blockers

| Level | First-pass written | Independently approved | Held slots considered here |
|---|---:|---:|---:|
| A1 | 200 | 0 | 4 |
| A2 | 200 | 0 | 1 |
| B1 | 200 | 0 | 1 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |

All 1,000 remain on editorial hold. There is **no approved release manifest**, no independent English/Myanmar/example/exact-sense CEFR review, no completed final George/Emma voice recordings with **real listening signoff**, no browser/mobile regression receipts, no **physical iPhone Safari** review, no measured GitHub Pages hosting approval, no final protected-assets preservation signoff and no confirmed production deployment. The existing 54 lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy protections were **not edited**. The user authorised eventual launch only when every gate is genuinely verified. **RELEASE BLOCKED — STAGING ONLY.**
