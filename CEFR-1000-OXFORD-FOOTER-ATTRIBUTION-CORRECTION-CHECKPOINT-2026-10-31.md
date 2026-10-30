# CEFR 1,000 — Oxford dictionary Word-of-the-Day attribution correction (2026-10-31)

**STAGING ONLY — release blocked.** This checkpoint corrects five previously recorded apparent Oxford publisher conflicts. It does not independently verify CEFR senses, English, fluent Myanmar, examples, or audio, and it does not approve any word.

## Important publisher-source correction

On 2026-10-31, directly reopened the Oxford Advanced Learner's Dictionary pages for **historic, graduate (verb), appointment, contemporary (adjective), and raw (adjective)**. The five earlier research packets identified a **C1 Oxford 5000 footer** on each page as though it belonged to the page's headword. The nearby footer actually names **"applicable" (adjective)** and is the **site-wide "Oxford Learner's Dictionaries Word of the Day" widget**. Thus the five apparent *C1 dictionary footer versus B1/B2 Oxford 3000 PDF* conflicts were **false attributions** and must not be used as evidence of the target headword's CEFR level.

| Target, provisional level | Actual Oxford 3000 PDF word/POS label | Dictionary URL, rechecked 2026-10-31 | Page text: target sense / separate Word of Day |
| --- | --- | --- | --- |
| historic (B2) | B1 adjective | [historic](https://www.oxfordlearnersdictionaries.com/definition/english/historic) | 107–124 / 157–171 |
| graduate (B2) | B1 verb | [graduate verb](https://www.oxfordlearnersdictionaries.com/definition/english/graduate_2) | 112–125 / 233–247 |
| appointment (B2) | B1 noun | [appointment](https://www.oxfordlearnersdictionaries.com/definition/english/appointment) | 105–125 / 242–256 |
| contemporary (B2) | B2 adjective | [contemporary adjective](https://www.oxfordlearnersdictionaries.com/definition/english/contemporary_1) | 129–141 / 173–187 |
| raw (B2) | B2 adjective | [raw adjective](https://www.oxfordlearnersdictionaries.com/definition/english/raw_1) | 107–115 / 228–242 |

Source: [Oxford 3000 by CEFR level official PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), and the [Oxford 3000/5000 publisher wordlist](https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&list=ox5000). The PDF and publisher wordlist indicate **word/part-of-speech levels, not independently signed-off exact senses**. Oxford dictionary **topic badges** likewise are not equivalent to core-list or independent exact-sense ratings.

**Remaining real issue:** historic, graduate and appointment are provisionally B2 but appear at B1 in the official Oxford 3000 word/POS list; they still need independent human exact-sense and placement review. Contemporary and raw have B2 publisher word/POS matches but still need human exact-sense and bilingual review. No automatic retiering. The dictionary sense leads remain useful; only the misattributed C1-footer interpretation is retracted.

The historical source packets are retained intact for audit provenance. The [five-record corrective source packet](draft/CEFR-1000-OXFORD-FOOTER-WORD-OF-DAY-FIVE-CORRECTION-2026-10-31.json) supersedes **only** the original `publisher_surface_conflict.dictionary_footer_label = "C1"` *interpretation*. The [fail-closed correction auditor](tools/audit_cefr_1000_oxford_footer_attribution.py) binds original packet records and held shortlist snapshots, rejects false Word-of-Day attribution, and runs across the six A1/A2/B1/B2/C1/ALL structural lanes plus documentary no-deployment QC. These automated checks do not independently inspect Oxford's live page at CI time or confer linguistic approval.


## Bilingual and example-sense editorial handoff (proposals only)

These are original candidate improvements, **not independent approvals**. The frozen shortlist and review tasks have not been changed. Human reviewers must assess natural Myanmar, exact English sense, original example grammar and publisher-backed CEFR for each retained item.

| Word | Proposed English example / Myanmar wording | Review concern |
| --- | --- | --- |
| **historic** | *The signing of the agreement was a historic moment for the town.* — **သမိုင်းတွင် အရေးပါသော၊ သမိုင်းဝင်သော** | Current “The agreement was a historic moment” conflates an agreement with the moment of signing; distinguish *historic* (historically important) from *historical* (related to the past). B1 publisher word/POS versus B2 draft still unresolved. |
| **graduate** (verb) | *She hopes to graduate from university next year.* — **တက္ကသိုလ်မှ ဘွဲ့ရသည်** | Prefer degree completion over vague “finishing a course”; British *graduate from* versus North American *graduate college*; verb /ˈɡrædʒueɪt/ distinct from noun /ˈɡrædʒuət/. B1 publisher word/POS versus B2 draft still unresolved. |
| **appointment** (noun) | *I made a dental appointment for Friday morning.* — **သွားဆရာဝန်နှင့် ကြိုတင်ချိန်းဆိုထားသော အချိန်** | Countable scheduled consultation, not appointment to a job; B1 publisher word/POS versus B2 draft still unresolved. |
| **contemporary** (adjective) | *The museum displays contemporary art by local artists.* — **ယနေ့ခေတ်နှင့် သက်ဆိုင်သော၊ ခေတ်ပြိုင်ဖြစ်သော** | *By* more directly credits artists; distinguish modern-day art from people who lived in the same historical period. Publisher B2 word/POS match does not approve exact sense. |
| **raw** (adjective) | *Wash your hands after handling raw chicken.* — **မချက်ပြုတ်ရသေးသော၊ အစိမ်းဖြစ်သော** | Food sense (uncooked), not unprocessed data/materials or uncontrolled emotion; publisher B2 word/POS match does not approve exact sense. |

The proposals are editorial first-pass suggestions only. A genuine independent reviewer must explicitly accept or revise each and provide content-bound signoff before any release manifest or audio can be considered ready.

## Frozen staging counts and blockers

| CEFR level | First-pass written | Independently approved | Direct Oxford word/POS observed (last verified prior run) |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 195 |
| A2 | 200 | 0 | 120 |
| B1 | 200 | 0 | 144 |
| B2 | 200 | 0 | 142 |
| C1 | 200 | 0 | 111 |
| **Total** | **1,000** | **0** | **712** |

No new distinct Oxford word/POS observation was added in this correction; 288 remain without direct Oxford observations. All 1,000 remain on editorial hold. Actual final George/Emma headword/example listening signoffs: **0/1,000**. Independent English/Myanmar/example and exact-sense CEFR receipts, complete dual-voice audio generation and listening, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting, privacy/production preservation release signoff and confirmed production deployment remain missing. The 54 lessons, separate IELTS 1,000 bank, established George/Emma production audio and privacy assets must remain untouched.

**Release: BLOCKED / STAGING ONLY.** No merge, main-branch change or publication. GitHub Actions job conclusions must be inspected separately; this document itself is not a CI pass receipt.

## Verified GitHub Actions results (actual job logs)

- [Structural run 41099832672](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41099832672): **SUCCESS** for all six A1/A2/B1/B2/C1/ALL jobs; code SHA `1b06c352aee8b72f20881004b39140288751e9c9`. Actual ALL log: **five false Oxford footer claims corrected; 53/53 adversarial attribution, source and signoff mutations rejected**; 712 distinct Oxford word/POS headwords across 731 observations; protected production assets unchanged. Structural ALL artifact ID `12996989403`.
- [Documentary no-deployment run 41099839880](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41099839880): **SUCCESS, report-only**, code SHA `e3f8051b42b44de7f0b7c1ac87466d799221a803`. Actual log confirms 53/53 correction mutations rejected and enumerates the missing independent review, real audio listening, browser/mobile, physical iPhone Safari, hosting and production evidence. Blocker artifact ID `12997497371`.

These are **structural/documentary CI conclusions only**; no independent reviewer, physical-device test, real listening, hosting measurement, merge or deployment has been completed.
