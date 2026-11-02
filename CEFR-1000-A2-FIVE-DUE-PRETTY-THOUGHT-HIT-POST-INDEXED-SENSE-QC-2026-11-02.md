# CEFR 1000 — A2 five exact-sense / POS source conflicts (STAGING ONLY)

**Observed:** 2026-11-02. **Scope:** user-approved **1,000 TOTAL**, A1/A2/B1/B2/C1 **200 each**; not the superseded 5,000-word plan. Branch `cefr-5000-bilingual-qa-staging` only. **Research leads, not independently verified CEFR approvals.**

## Source-supported findings and Myanmar/grammar handoff

| Frozen A2 headword/POS | Cambridge publisher-indexed evidence | Exact-sense risk |
|---|---|---|
| **due**, adjective | [Cambridge due](https://dictionary.cambridge.org/dictionary/english/due): **B1 EXPECTED** arrival/event sense | Original bus-due-in-ten-minutes example is the B1 expected-arrival sense; do not confuse `due to` causation, C2 owed payment, or B2 `in due course`. |
| **pretty**, adverb | [Cambridge pretty](https://dictionary.cambridge.org/us/dictionary/english/pretty): **B1 informal adverb** quite/not extremely | Frozen `pretty clear` is the B1 degree adverb; **A2** is a separate attractive **adjective** sense, not support for the frozen adverb. |
| **thought**, noun | [Cambridge thought](https://dictionary.cambridge.org/dictionary/english/thought): **B1 noun** idea/opinion | Frozen `One thought` example is the B1 countable noun; `thought` as past tense of `think` is a different POS, and careful-thinking noun use has a separate B2 learner-dictionary lead. |
| **hit**, verb | [Cambridge hit](https://dictionary.cambridge.org/dictionary/english/hit): **A2 hand/hand-held object strike**, **B1 sudden-force collision** in Advanced Learner's Dictionary | Frozen `The ball hit the window` is a moving-object collision. Cambridge Essential British English offers a broader A2 hit example with a ball; retain this **cross-dictionary edition conflict** for human adjudication, not auto-retiering. |
| **post**, noun | [Cambridge post](https://dictionary.cambridge.org/dictionary/english/post): **internet-message noun unlabelled in observed index**; internet-publication **verb B1** | Frozen `Her post explained...` is a noun. Do not copy the B1 verb badge onto the noun or confuse UK postal meanings. |

**Source access:** Publisher-owned public search-index snippets inspected on **2026-11-02**; direct Cambridge headword page opens returned **HTTP 403**. These are observed indexed labels and sense leads, **not** directly rechecked full publisher pages, and **not** independent English, Myanmar, example, pronunciation or CEFR signoff. Oxford/Cambridge dictionary edition and sense granularity can differ. The publisher URLs and this access limitation are preserved in the [five-card research packet](draft/CEFR-1000-A2-FIVE-DUE-PRETTY-THOUGHT-HIT-POST-INDEXED-SENSE-2026-11-02.json). The packet contains the original English/Myanmar/examples, original source path/index/blob, five unapproved English/Myanmar/example alternatives, exact-sense warnings and four independent reviewer tasks per entry.

**Editorial decisions:** No automatic retiering or changes to the frozen shortlist. A2 placement of `due`, `pretty`, `thought` requires independent source-backed justification or separately approved replacements; `hit` requires a genuine sense/edition and example reconciliation; `post` requires an independently observed noun-sense CEFR source. Myanmar fluency, example grammar, UK pronunciation and voice-specific example audio require human review.

## Mechanical safeguards, not approval

[Auditor](tools/audit_cefr_1000_a2_five_due_pretty_thought.py) pins research packet blob `14afa1b1ac982a6ad19a29eb16502f889dcc172e` and frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; checks **200/level**, 1,000 globally casefold-deduplicated headwords, frozen original fields and historical provenance, source URLs, exact POS/CEFR distinction, publisher HTTP 403 access caveat, and rejects false reviewer/listening/device/deployment flags. Synthetic mutation self-tests target each card's publisher evidence, Myanmar/example alternatives, provenance, all human review flags, and top-level release metadata. A passing auditor is only evidence of mechanical consistency, **not** a genuine independent language review.

Wired into **six parallel structural A1/A2/B1/B2/C1/ALL** lanes and the documentary **NO DEPLOY** QC gate. Commits: [research `3fec22c`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/3fec22c74f23324c2872e63171b2ca2a666c4b57), [auditor `511e02e`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/511e02eaa16b83112412711e0402d9a4501d4712), [structural workflow `42d4a38`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/42d4a38f3b357997a9ecb4a138a083533590fab3), [documentary workflow `adae2e7`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/adae2e7bcd6c8d0b83e754fe555b2e50fafd8358).

New push-triggered [structural run 41422143280](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41422143280) (SHA `42d4a38f3b357997a9ecb4a138a083533590fab3`) and [documentary run 41422157118](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41422157118) (SHA `adae2e7bcd6c8d0b83e754fe555b2e50fafd8358`) were **in progress when first inspected**. No new CI success is claimed until actual job conclusions and logs are checked.

## Release blockers (truthful)

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

All 1,000 remain **editorial hold**. Missing: genuine independently signed English/Myanmar/example and source-backed exact-sense CEFR review, approved 1,000-entry manifest, British George/Emma headword **and** example audio generation with real recording-by-recording listening receipts, desktop/browser/mobile regression, **physical iPhone Safari** evidence, measured GitHub Pages hosting clearance, protected production asset signoff and confirmed production deployment. Preserve 54 lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy assets. **RELEASE BLOCKED — STAGING ONLY; no main change, merge or publication.**
