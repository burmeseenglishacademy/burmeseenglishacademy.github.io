# CEFR 1,000 — six B2 foundational exact-sense conflicts and controls (2 November 2026)

**Scope:** user-approved 1,000 total, A1/A2/B1/B2/C1 200 each, NOT superseded 5,000. **Branch:** `cefr-5000-bilingual-qa-staging`. **Status:** EDITORIAL HOLD / STAGING ONLY / NEVER DEPLOY without all gates.

## Publisher-index evidence, not independent review

On 2 November 2026, public web search-index excerpts for Cambridge Dictionary entries showed the following CEFR sense labels. Direct Cambridge English headword requests returned **HTTP 403**, so the labels are recorded as *indexed research leads*, not personally opened publisher-page evidence or independent human signoff.

| Frozen B2 word / exact provisional sense | Cambridge indexed lead | Assessment |
|---|---|---|
| [colour](https://dictionary.cambridge.org/dictionary/english/colour) — ordinary visible colour (noun) | **A1**, APPEARANCE | Three-band conflict; avoid confusing with C2 INTEREST or RACE senses |
| [repeat](https://dictionary.cambridge.org/dictionary/english/repeat) — say instruction again (verb) | **A2**, say/do again | Two-band conflict; ordinary imperative, not advanced technical sense |
| [speaker](https://dictionary.cambridge.org/dictionary/english/speaker) — guest public speaker (noun) | **B1**, FORMAL TALK | One-band conflict; separate B1 language speaker and A2 electrical speaker |
| [appointment](https://dictionary.cambridge.org/dictionary/english/appointment) — dental meeting (noun) | **A2**, ARRANGEMENT | Two-band conflict; not C2 JOB appointment |
| [package](https://dictionary.cambridge.org/dictionary/english/package) — services offered as a unit (noun) | **B2**, OFFERED TOGETHER | Indexed B2 alignment control, distinct from wrapped parcel |
| [graduate](https://dictionary.cambridge.org/dictionary/english/graduate) — finish a university degree (verb) | **B2**, UK verb | Weaker alignment lead: label was found on [Cambridge's Traditional Chinese-to-English university index](https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94-%E8%8B%B1%E8%AA%9E/%E5%A4%A7%E5%AD%B8), **not** directly on English headword page |

The [research packet](draft/CEFR-1000-B2-SIX-FOUNDATIONAL-SENSE-CAMBRIDGE-INDEXED-TRIAGE-2026-11-02.json) retains each **unchanged frozen bilingual record**, historical starter path/index/blob, publisher URL, dated access method, observed exact-sense heading, original example and unapproved alternative English/Myanmar/example. Four provisional B2 placements conflict with indexed lower levels; two are controls. **No retiering or shortlist edits.**

## Mechanical evidence guard

The [fail-closed six-card auditor](tools/audit_cefr_1000_b2_six_foundational_senses.py) checks pinned Git blobs, 1,000 unique headwords, five 200-word quotas, 0 approvals, source index provenance, exact Cambridge entry paths, indexed-versus-direct-access distinctions, Myanmar script, target-word examples, and absence of fabricated independent review or listening claims. A synthetic mutation suite is wired into the six parallel A1/A2/B1/B2/C1/ALL structural lanes and the documentary **NO DEPLOY** gate. The auditor is a mechanical safeguard; it cannot validate the semantic correctness of Myanmar or replace an independent reviewer.

**Latest staging changes (read-back pending CI):** packet commit `f4b45745398540e75acd699cbe5ab89a54ddbba4`; auditor correction `ce4298cf250994151a53dfc1a06f9ed4c51d385d`; parallel workflow `17e60bbccfe1125ebd5f294d6fc982b00166e4d5`; documentary workflow `f0ab4fbff5e1b353cb0108daf5aecbc3e932982e`. Previous [structural run 41375278000](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41375278000) and [documentary run 41375278050](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41375278050) were verified successful **before** these new changes. **No new CI run ID, job conclusion or log is yet retrievable; do not claim this new auditor CI-passed.**

## Honest release gate

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**Blocked:** independently reviewed English, fluent Myanmar, examples and exact-sense CEFR evidence; approved manifest; final British George/Emma headword/example audio and real listening receipts; browser/mobile regression; physical iPhone Safari; measured GitHub Pages hosting; production deployment and protected-asset verification. Production 54 lessons, separate IELTS 1,000-word bank, established George/Emma audio and privacy were not edited. No merge, publication, listening or device-test claim.
