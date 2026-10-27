# Burmese English Academy CEFR 1,000 — Oxford risk triage / release gate hardening
**2026-10-27 · Asia/Singapore · STAGING ONLY · NO INDEPENDENT APPROVAL OR DEPLOYMENT**

## Target and safe staging
The user-approved new target is **1,000 CEFR entries total**: A1/A2/B1/B2/C1 **200 each**, separate from the existing IELTS 1,000-word bank. Previous 5,000-word reports are historical inventory records only. The previously existing hourly automation **BEA 1000 QC & Launch** remains enabled and should work within the existing cadence, not add a second schedule. Publication stays fail-closed; do not notify until all independent reviews, audio listening, physical iPhone Safari, hosting and live deployment are confirmed.

## Substantive editorial risk discovery
Performed a mechanical **word+part-of-speech+CEFR** cross-comparison of the exact **1,000 staged provisional entries** with independently published Oxford 3000/5000 wordlist materials. For bulk comparison, used **community-transcribed** British Oxford 3000 and additional Oxford 5000 CSV mirrors from `winterdl/oxford-5000-vocabulary-audio-definition`, pinned at blob SHAs `0e522eef1b5b770f4b2911373adfc388848cc95e` and `01c721beb00004a11539662823ded2d5136dd848`. Their contents are **secondary/transcribed data**, not automatically independent sense-level CEFR evidence. Opened Oxford University Press's original [Oxford 3000](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf) and [Oxford 5000](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000.pdf) PDFs to spot-check the provenance, including `world n. A1`, `weekend n. A1`, `personality n. A2`, `abortion n. C1` and `veteran n. C1` (the Oxford item is a noun while the current draft proposes adjective). These spot observations are **NOT** 1,000 independent human CEFR approvals. Oxford lists cover major *headwords and POS* and do not prove the level of every chosen sense or usage.

### Exact machine comparison totals
| Proposed level | Provisional selected | Matched Oxford word+POS+level (sense unverified) | Different proposed CEFR for same POS | POS not matched | Not in transcribed core wordlist | Independently approved |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 194 | 0 | 0 | 6 | 0 |
| A2 | 200 | 61 | 118 | 1 | 20 | 0 |
| B1 | 200 | 57 | 142 | 1 | 0 | 0 |
| B2 | 200 | 98 | 100 | 0 | 2 | 0 |
| C1 | 200 | 65 | 47 | 1 | 87 | 0 |
| **TOTAL** | **1,000** | **475** | **407** | **3** | **115** | **0** |

The result is **525 reversible flagged review cases**, including **68** where the same-POS Oxford levels differ by at least two CEFR bands (**A2 1, B1 26, B2 38, C1 3**). Examples of high-priority disagreements: `greenhouse A2 vs B2`, `weekend B1 vs A1`, `personality B2 vs A2`, `prepare B2 vs A1`. A label conflict is **not proof that either exact usage has the wrong level**, and an item absent from a core list (e.g. some inflections, compounds or specialist terms) is **not proof that it is an invalid word**. Independent dictionary/sense/CEFR review is mandatory before retaining, retiering or replacing any item.

**New staging artifacts:** `draft/CEFR-1000-OXFORD-LEVEL-POS-CROSSCHECK.json` includes all 1,000 mechanically compared candidate rows, and `draft/CEFR-1000-OXFORD-DISCREPANCY-QUARANTINE.json` includes 525 reversible held flags, every single one with `independently_approved=false`, pending review. `draft/CEFR-1000-BILINGUAL-DISCREPANCY-REVIEW-PACKETS.json` includes **525 contextual review packets** with each actual English draft definition, actual original Myanmar draft gloss, original English example, observed Oxford alternatives and separated pending independent English-lexical, fluent Myanmar, example, sense-specific CEFR evidence tasks. Priorities: **68 high two-plus bands; 339 one-band CEFR disagreements; 3 POS disagreements; 115 not in transcribed core list**. Each review remains pending and *none* is published.

The prior **120 IELTS / CEFR shared headwords** (A1 1/A2 7/B1 27/B2 48/C1 37) remain separate review tasks, without touching the production IELTS dataset. A shared headword is not inherently a wrong duplicate: independent sense/usefulness review must decide what to retain.

## QA and release integrity improvements
- Created `tools/audit_cefr_1000_oxford_discrepancy.py` to assert the 1,000-row Oxford matrix, 525 flag parity, 525 genuinely pending original bilingual review packets, source provenance, all 200-per-level quotas, zero false human approvals and no release.
- Integrated that auditor into **all six A1/A2/B1/B2/C1/ALL GitHub Actions structural jobs**, alongside protected existing IELTS bank overlap detection and protected-asset git diff. A first test failed on an auditor assumption that wrongly rejected the mathematically correct *zero distance* for aligned words; repaired before re-running. No draft level was changed.
- Fixed a real **future-release-validator false-negative bug**: punctuation-attached words (such as `student.`) and ordinary regular English inflections (such as `managed`, `grabbed`) could be wrongly rejected by a whitespace-only headword checker. The release validator now checks word boundaries and regular English inflections while rejecting substrings inside unrelated words. Added negative tests for punctuation, inflections, unrelated substrings and irregular examples requiring independent override. Not a grammar or linguistic verification.
- Extended `draft/CEFR-1000-RELEASE-EVIDENCE.json` with EMPTY Oxford discrepancy and IELTS overlap human review receipt arrays (no invented identities/observations).
- Hardened `tools/audit_cefr_1000_launch_readiness.py`: a retained Oxford-flagged word and IELTS-overlap case now require independently observed documented resolution linked to the approved final entry's content hash. Audio listening now counts only if the signed record matches the *actual referenced George/Emma MP3 file's SHA-256*, not merely a claimed listening receipt. The script still cannot physically listen or authenticate a person; its evidence integrity pass is never an independent release certification.
- Production assets including 54 lessons, the separate IELTS 1,000 bank, existing George/Emma audio and privacy remain protected. No changes to `main`, no deploy, no release PR.

## Observed actual GitHub Actions runs and commits
- [Six-job Oxford/reviewer-packet staging QA **40456867755**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40456867755) **completed SUCCESS** across A1, A2, B1, B2, C1 and ALL. Inspected actual ALL-job **122032125559** log: 1,000 source-linked provisional draft candidates and 1,000 review tasks; 200 each level; **525** Oxford/POS review flags, **68** high-priority flagged; 120 existing IELTS headword overlap tasks; **zero independent approvals**; production-asset diff `PASS`; no deploy. QA artifact uploaded as **12712274189**.
- [Go-live documentary gate **40456520583**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40456520583) **completed SUCCESS** in **REPORT-ONLY / EXPECTED BLOCKED** mode, not a green light to release. Actual job **122031024322** log: **source-reviewed 0/1,000**, **both-voice real listening 0/1,000**, live deployment **false**. No independently approved manifest, person-specific review, final-corpus audio listening, physical iPhone Safari, measured hosting or released bundle; all still blocking. Gate uploaded blocker artifact **12713225219**.
- [Release evidence negative regression **40456323076**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40456323076) SUCCESS after tokenizer regression tests. [Legacy A1 structural regression **40456323083**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40456323083) SUCCESS. Both are **technical-only**.
- First added-Oxford-auditor workflow **40455968495** failed in the Oxford step because a zero gap was incorrectly asserted invalid; corrected auditor workflow **40456062229** passed, and final full-packet workflow **40456867755** passed.
- Oxford matrix creation `737aff00386b182459d955a55d7a9b1510eea346`; hold file `93444d60ed796d662e019976b6cd29004c52b638`; Oxford auditor fix `60d4961f0b4ea980bad454bc368d64456c724581`; tokenizer validator `5d9e5960c73fd875aa243054a0b19c3e58a61461`; tokenizer tests `be188523541a03008e264b5ad3b64a632d73f3f1`; launch evidence ledger `0e7203d5e6a9db71ee775cc28352691977237c07`; release gate hardening `99712b1e6b39ffff344bee4355b8139bb35ede38`; reviewer packets `0eed0ce7da9a2d8d02e27ad45aed28cebe5a70a0`; packet QA `b4fae0a6e36ba72247eb3ca94809a7f8d8160093`; final six-job workflow `b10af089e8ed107fd46cbdfafcfbc5d30ba88184`.

## Honest readiness / next work
| Level | Actual first-pass bilingual shortlist | English + Myanmar + CEFR + examples independently approved | Both voices real-listening approved | Published |
|---|---:|---:|---:|---:|
| A1 | 200 | 0 | 0 | 0 |
| A2 | 200 | 0 | 0 | 0 |
| B1 | 200 | 0 | 0 | 0 |
| B2 | 200 | 0 | 0 | 0 |
| C1 | 200 | 0 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** | **0** |

Next review the 68 strongest reference conflicts first; then all 525 Oxford/POS cases, the remainder of the 1,000 original bilingual records and the 120 cross-bank overlap cases, with real source-backed human decisions. Substitute or retier material based on the *actual sense* and evidence, never mechanically force an arbitrary quota or claim human signoff. Only after full independent content review should the final corpus be frozen, George/Emma audio prepared and really listened to, desktop/mobile browsers and a **physical iPhone Safari** verified, actual hosting measurements confirmed, and finally a reviewed narrow live release deployed and independently checked.

**No false approvals, audio generation/listening, physical-device QC, hosting confirmation, merge, publication or one-time completion notification were made in this iteration.**
