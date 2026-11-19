# CEFR-1000 cross-level exact-sense editorial triage — 2026-11-20

**Scope:** Approved 1,000-total shortlist only; staging editorial investigation, **not** independent review or a release approval. Observation date: 2026-11-20 (UTC+08). Source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; paired pending task file blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`. These are internal provenance, **not external CEFR citations**.

## Inventory-wide mechanical inspection

Parsed all 1,000 provisional entries (A1/A2/B1/B2/C1: 200 each). All 1,000 provisional Myanmar meaning strings contain at least one Myanmar Unicode codepoint; this is only a script-presence test, **not** evidence of fluency, semantic correctness or reviewer signoff. No duplicate case-folded headword was found in this snapshot, even across different parts of speech. No headwords in the snapshot contain spaces, underscores, digits or all-uppercase acronyms. These narrow checks do not prove canonical lexical identity, exact-sense uniqueness, named-entity exclusion or CEFR suitability. Independent approvals remain 0/200 at every level.

## Priority independent-review queue

| Task | Provisional entry and sense | Specific risk / question | Original replacement example proposed for review |
|---|---|---|---|
| CEFR1000-A1-0004 | A1 **i**, pronoun, first person | Headword is lower-case `i`, but standard standalone English pronoun is **I**; case-fold dedup hides this canonical-spelling error. Do not silently rewrite shortlist without coordinated task/provenance update. | **I live near the school.** |
| CEFR1000-A1-0005 | A1 **you**, pronoun, addressee | Myanmar equivalents `သင်၊ မင်း၊ ရှင်` vary in relationship, register and social context; reviewer should check examples and teaching notes, not choose one as universally interchangeable. | **Are you ready?** |
| CEFR1000-A2-0203 | A2 **through**, preposition, movement from one side to another | Verify exact movement sense rather than duration, completion, or means; source must label this sense at A2. | **The train goes through a tunnel.** |
| CEFR1000-A2-0204 | A2 **while**, conjunction, simultaneous events | Distinguish temporal conjunction from contrastive `while`; verify exact sense and example tense. | **I read while my brother cooked.** |
| CEFR1000-B1-0402 | B1 **independent**, adjective, not controlled | Political independence, financial independence and personal self-reliance are not interchangeable; verify the actual labelled sense. | **The committee made an independent decision.** |
| CEFR1000-B1-0404 | B1 **wonder**, verb, wish to know | Distinguish the verb from noun `wonder` and the `wonder if` polite-request construction. | **I wonder where the keys are.** |
| CEFR1000-B2-0602 | B2 **relief**, noun, easing of worry/pain | Separate emotion from financial aid and geographical relief; current Myanmar `စိတ်သက်သာရာရမှု` may cover only emotional relief. | **We felt relief when everyone arrived safely.** |
| CEFR1000-B2-0604 | B2 **retail**, noun, selling to consumers | Verify distinction between noun `retail` and adjective/adverb uses; source level must match the noun business sense. | **She works in retail.** |
| CEFR1000-C1-0802 | C1 **trigger**, verb, cause event | Verify C1 for the exact causal verb sense; do not substitute evidence for psychological triggers or firearm noun. | **The announcement triggered a public debate.** |
| CEFR1000-C1-0804 | C1 **signature**, noun, handwritten name | **High-priority possible mislevel:** common form-signing sense may be below C1. Check exact-sense labelled learner dictionaries; do not transfer a C1 label from `signature` meaning a distinctive characteristic or style. | **Please put your signature here.** |

**Task-ID caveat:** IDs in the table are provisional lookup hypotheses based on global ordinals, and **must be reconciled against the actual independent task JSON before use**. Do not use them as authoritative review assignments until confirmed.

## Independent evidence still required

For each item: record a directly accessible authoritative learner-dictionary or curriculum URL, observation date, exact quoted/identified sense and part of speech, displayed CEFR label (or explicitly state none), page version/archival provenance where possible, independently reviewed natural Myanmar definition, example grammaticality, reviewer identity and timestamp. A teaching example or a generic CEFR wordlist **cannot by itself** substantiate an exact-sense level. Do not set any reviewed or approved flag on the basis of this note.

**Release state:** staging-only. No new audio, real listening, physical iPhone Safari test, browser regression, hosting clearance or production deployment evidenced by this document. Protect the 54 lessons, separate IELTS 1,000 bank, existing George/Emma audio and privacy configuration.
