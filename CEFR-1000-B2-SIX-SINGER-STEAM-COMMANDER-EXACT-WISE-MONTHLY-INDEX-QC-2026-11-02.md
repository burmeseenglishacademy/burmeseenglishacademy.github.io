# CEFR 1,000 — six B2 Cambridge-indexed exact-sense checks (2 November 2026)

**Scope:** user-approved 1,000 TOTAL, exactly A1/A2/B1/B2/C1 = 200 each; staging branch `cefr-5000-bilingual-qa-staging` only. **Release blocked; no approvals, listening, iPhone test or deployment.**

## Publisher-indexed research leads, not human verification

On **2026-11-02**, Cambridge Dictionary English headword search-index results displayed these POS/sense/CEFR labels. Attempts to open each direct Cambridge headword page returned **HTTP 403**. Therefore these are **publisher-indexed leads**, NOT directly opened publisher pages, independently checked CEFR classifications or reviewer signoffs. An independent reviewer must confirm the precise sense and British usage, the Myanmar gloss, example grammar, and any placement change.

| Frozen B2 headword | Indexed CEFR | Exact-sense interpretation and action |
| --- | --- | --- |
| [singer](https://dictionary.cambridge.org/dictionary/english/singer) | **A2** noun [C] | General person who sings. Frozen professional qualifier does not substantiate B2. **Conflict**. |
| [steam](https://dictionary.cambridge.org/dictionary/english/steam) | **B2** noun [U] | Hot vapour produced when water boils. **Alignment lead**; distinguish steam noun, steam verb, visible condensed mist and STEAM acronym. |
| [commander](https://dictionary.cambridge.org/dictionary/english/commander) | **C2** noun [C] | Military operation officer or naval rank. **Conflict with B2**; frozen group-leader wording partly broader than naval rank. |
| [exact](https://dictionary.cambridge.org/dictionary/english/exact) | **B1** adjective, ACCURATE | Completely correct in detail. **Conflict**; the separate formal verb *exact* must not be borrowed to justify B2 adjective. |
| [wise](https://dictionary.cambridge.org/dictionary/english/wise) | **B2** adjective | Good judgement grounded in knowledge and experience. **Alignment lead**. |
| [monthly](https://dictionary.cambridge.org/dictionary/english/monthly) | **B1** adjective/adverb | Once each month. **Conflict**; frozen item is adjective and must not be conflated with the adverb. |

Source-access limitations are recorded **per entry** in [the six-record research packet](draft/CEFR-1000-B2-SIX-SINGER-STEAM-COMMANDER-EXACT-WISE-MONTHLY-INDEXED-2026-11-02.json). That packet preserves all six original English definitions, Myanmar meanings and example sentences, source indexes 545/546/548/549/553/556, historical blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`, publisher URLs, observation dates, UK IPA leads and **unapproved** bilingual/example alternatives. No frozen record or review flag was edited.

## Fail-closed QA and evidence status

[New auditor](tools/audit_cefr_1000_b2_six_singer_commander_indexed.py) validates frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, the original source blob, exactly 200 held headwords per level, global deduplication, per-card exact-sense labels, source URL and access provenance, and absence of forged independent, audio-listening, iPhone and production signoffs. Its mock-only adversarial suite is wired into **A1/A2/B1/B2/C1/ALL** structural GitHub Actions lanes and the separate documentary **NO DEPLOY** workflow. A passing mechanical test is not linguistic or release approval.

**Counts:** first-pass written/independently approved = A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. All 1,000 remain on editorial hold. Independent English/Myanmar/example/sense-specific CEFR reviews, approved manifest, full British George/Emma headword+example audio with real listening, browser/mobile regression, physical iPhone Safari evidence, GitHub Pages hosting measurements and confirmed production deployment are missing. Existing 54 lessons, separate IELTS bank, established George/Emma production audio and privacy assets are protected. **No merge, publication or main-branch changes authorised until every gate passes.**

**CI note:** do not claim new runs passed until their actual IDs, job conclusions and logs are inspected. Last previously verified six-lane structural run: [41437145678](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41437145678); documentary run: [41437150894](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41437150894), both predate this packet.
