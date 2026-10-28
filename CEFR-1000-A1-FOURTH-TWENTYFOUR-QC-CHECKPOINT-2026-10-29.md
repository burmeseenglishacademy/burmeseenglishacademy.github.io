# CEFR 1,000 — Oxford A1 24-word source/grammar checkpoint (29 October 2026)

**Scope:** USER-APPROVED 1,000 TOTAL, A1/A2/B1/B2/C1 **200 each**. Staging branch `cefr-5000-bilingual-qa-staging` only. **BLOCKED / STAGING ONLY.** This is not a review signoff, audio listening record, production QA or deployment record.

## Work actually performed

Opened the **official Oxford 3000 by CEFR level PDF** directly on 29 October 2026, then reconciled 24 A1 shortlist headwords and parts of speech against the publisher's A1 list. The new source-bound packet is [`draft/CEFR-1000-OXFORD-A1-FOURTH-TWENTYFOUR-2026-10-29.json`](draft/CEFR-1000-OXFORD-A1-FOURTH-TWENTYFOUR-2026-10-29.json). It preserves each original English definition, fluent-Myanmar first-pass gloss as written, original example, shortlist Git source path/index/blob SHA, Oxford publisher URL, dated observation, one-based PDF page, zero-based extracted line and the exact short word/POS source excerpt.

**Official primary source:** https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf (directly viewed 2026-10-29). **24 A1 word/POS matches**: a, an, read, in, on, have, not, but, or, all, me, one, like, time, people, good, know, see, two, want, go, need, here, day. These are **not** publisher exact-sense CEFR certifications or independent linguistic reviews.

Two further directly observed **contrasting word/POS entries** were preserved separately rather than silently conflated with the selected A1 senses:

- `all` A1 determiner/pronoun (PDF p.1, extracted line 25) versus A2 adverb (p.4, line 931); the A1 example *All students are here* uses the determiner.
- `like` A1 enjoyment verb (p.2, line 443) versus A1 similarity preposition (p.2, line 442); the A1 example *I like this song* uses the verb.

## Prioritised editorial action proposals — NOT applied to the provisional shortlist

1. **have** — current definition *to own or possess* conflicts with *I have two sisters*, where *have* describes family relationships, not ownership. Independent reviewer should either use an original ownership example such as *I have a blue bag* or separately define and teach the family-relationship sense; confirm fluent Myanmar.
2. **read** — *I read a book every night* is habitual present /riːd/, not past /red/. Final British George and Emma headword/example recordings must be listened to for the intended pronunciation.
3. **all** — preserve determiner usage at A1; separately distinguish the Oxford A2 adverb. A broad headword match is not an exact-sense signoff.
4. **like** — keep enjoyment-verb example separate from the similarity-preposition homograph; do not infer either sense's approval from a word-only lookup.
5. **day** — a *24-hour period* gloss versus *Today is a busy day* may conflate calendar day and daytime/activity context; independent reviewer should choose one clear sense and example.
6. **a/an** — the learner rule depends on **vowel/consonant sound**, not just the next written letter. Confirm a natural Myanmar explanation and British audio.

The remaining entries also carry per-word human-review tasks covering sense, POS, original-example grammar, fluent Myanmar and pronunciation. No machine self-review was converted to independent approval. No final shortlist content or flags changed.

## Fail-closed CI safeguards

Added `tools/audit_cefr_1000_oxford_a1_fourth_twentyfour.py` to bind the 24 records to the exact provisional shortlist blob, original English/Myanmar/examples, original source Git paths/indices/SHAs, dated official Oxford PDF URL and locators, specific editorial risks and zero-review hold flags. The auditor includes **48 negative mutation cases** (24 per-record forged publisher excerpts plus 24 forged source, translation, example, provenance, homograph, or review/approval mutations). Structural QA executes the audit in six parallel A1/A2/B1/B2/C1/ALL jobs; documentary no-deploy QC runs the full negative suite.

**Verified actual new CI:** [parallel structural run 40727475721](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40727475721) completed **SUCCESS**, with all six A1/A2/B1/B2/C1/ALL jobs individually concluded **success** at head commit `1dc62485c837a058aa29c451eb094d2c2cfa7549`. The ALL job log (job `122954515746`) explicitly records **48/48 negative source/content/false-approval mutations rejected** and `PASS: protected production assets unchanged; no deploy`. [Documentary no-deployment run 40727459320](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40727459320) completed **SUCCESS** at `064e95005fcce5b155fb91ca78cb0370fe3475d9`; job `122954454359` logs **48/48** mutations rejected and `PASS: protected production assets untouched by staging migration`. The full release-enforcement step was **skipped by design** because this was a report-only run; no evidence of final approval, audio listening, iPhone testing or deployment is implied.

## Current evidence counts and hard blockers

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Final George/Emma headword-and-example listening receipts: **0/1,000** complete per-word receipts; no assertion that final 4,000 voice clips were generated or listened to. Human-independent English, Myanmar, example and exact-sense CEFR reviews are missing. Full desktop/mobile regression, **real physical iPhone Safari**, measured GitHub Pages hosting and bandwidth checks, preserved-production full audio verification and confirmed public deployment are also missing.

**Protect production:** all new edits are confined to staging research packets, staging-only auditors/workflows and staging reports. No `main` write, merge or publish. The 54 production lessons, separate IELTS 1,000 bank, established George/Emma production audio and privacy paths must remain unchanged and are checked by CI; a successful diff check is not a full listening test.
