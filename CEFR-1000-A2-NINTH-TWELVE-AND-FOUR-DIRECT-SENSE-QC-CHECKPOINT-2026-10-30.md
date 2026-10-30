# CEFR 1,000 — ninth A2 Oxford PDF twelve + four direct dictionary sense leads (30 October 2026)

**STAGING ONLY — NO INDEPENDENT APPROVAL, NO DEPLOYMENT.** This is the user-approved 1,000-total A1–C1 project (200 per level), not the abandoned 5,000-word target. The provisional shortlist and independent-review task JSON are unchanged.

## Direct publisher observations, 2026-10-30

Directly opened Oxford University Press's official [Oxford 3000 by CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf). These are **word/part-of-speech classifications**, not exact-sense CEFR or human-independent approval. The [source-bound twelve-record packet](draft/CEFR-1000-OXFORD-A2-NINTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json) stores PDF page numbers (1-based), extracted line numbers (0-based), source excerpts, original bilingual/examples, historical source path/index/Git blob, date and editorial holds.

| Draft A2 | Oxford word/POS | Official PDF locator | Specific editorial concern |
|---|---|---|---|
| contact (verb) | **B1** | page 8, line 1932 | Telephone/email communication, not physical contact noun |
| offer (verb) | A2 | page 6, line 1432 | Original example may describe habitual provision rather than willingness to give |
| build (verb) | **A1** | page 1, line 112 | Physical construction, not figurative development |
| culture (noun) | **A1** | page 1, line 183 | Community customs and beliefs, not laboratory cultures |
| safe (adjective) | A2 | page 6, line 1576 | Path safety and natural Myanmar phrasing |
| career (noun) | **A1** | page 1, line 131 | Working-life sequence, not merely one job |
| training (noun) | A2 | page 7, line 1723 | Job instruction versus practice |
| stay (verb) | **A1** | page 3, line 739 | Remaining in place rather than lodging temporarily |
| age (noun) | **A1** | page 1, line 20 | Years lived, not an era |
| deal (noun) | **B1** | page 8, line 1960 | Agreement, not deal verb, unfair treatment, or softwood |
| check (verb) | **A1** | page 1, line 142 | Verify correctness, not cheque or tick mark |
| heart (noun) | A2 | page 5, line 1267 | Blood-pumping organ, not emotion or heart shape |

Publisher counts: **A1 6, A2 4, B1 2**. Therefore **8 of 12 provisional A2 placements differ at publisher word/POS level**. None has been retiered. Source-level discrepancy does not alone prove a particular draft sense belongs at the publisher level.

## Four directly opened dictionary pages

- [contact verb](https://www.oxfordlearnersdictionaries.com/definition/english/contact_2), inspected lines 88–123: communication by telephone, letter or email. Distinct from the contact noun; the draft definition is a plausible match, but publisher PDF B1 conflicts with draft A2.
- [offer verb](https://www.oxfordlearnersdictionaries.com/definition/english/offer_1), lines 88–125: giving or willingness to give. The draft “They offer free lessons every weekend” may imply ongoing service provision rather than a particular offer; request independent sense/example alignment.
- [deal noun](https://www.oxfordlearnersdictionaries.com/definition/english/deal_2), lines 88–121: business or other agreement, consistent with “made a deal”. Distinguish the noun from the separate verb and from the British uncountable wood meaning.
- [heart noun](https://www.oxfordlearnersdictionaries.com/definition/english/heart_1), lines 88–125: the physical organ, distinct from emotional or symbolic meanings. Oxford's **Body a2** topic tag is not an independently verified exact-sense CEFR signoff.

These four are **direct dictionary sense leads only**; no independent human English, Myanmar, example, pronunciation or CEFR signoff was obtained.

## Unapproved original editorial proposals for independent review

| Word | Myanmar candidate (not accepted) | Original English example candidate (not accepted) |
|---|---|---|
| contact | ဖုန်း၊ အီးမေးလ် စသည်ဖြင့် ဆက်သွယ်သည် | Please contact the school if you have any questions. |
| offer | တစ်စုံတစ်ရာ ပေးရန် သို့မဟုတ် လုပ်ပေးရန် ကမ်းလှမ်းသည် | She offered to help me carry the books. |
| deal | နှစ်ဖက်အကြား သဘောတူညီချက် | We made a deal to share the transport costs. |
| heart | ခန္ဓာကိုယ်အနှံ့ သွေးလည်ပတ်စေသော နှလုံး | The doctor checked his heart. |

These alternatives are first-pass suggestions only, not independently checked, not added to the frozen shortlist and not audio-ready.

## Fail-closed audit and documentary readiness

[Staging auditor](tools/audit_cefr_1000_oxford_a2_ninth_twelve.py) pins all twelve publisher URLs, dates, PDF locators, bilingual/example snapshots, upstream Git provenance, dictionary scope, holds and zero independent approvals. Adversarial mutation tests attempt to forge publisher records, Myanmar text, examples, review receipts and listening status. The auditor is invoked by the **six parallel A1/A2/B1/B2/C1/ALL structural jobs** and by the **documentary no-deployment** workflow. CI success, when confirmed from actual run job conclusions and logs, is structural/documentary only, never a linguistic or physical-device signoff.

Expected Oxford direct word/POS coverage after this batch (subject to CI reconciliation): **A1 195/200, A2 120/200, B1 120/200, B2 118/200, C1 99/200 = 652/1,000**; **348** still lack direct Oxford observations. Expected reviewer queue: **3 unlisted, 31 publisher-higher, 225 publisher-lower, 393 matching word/POS but exact-sense-unverified, 348 without observation**. These numbers do not count Cambridge index snippets as Oxford PDF observations.

First-pass written / independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Real final George/Emma headword+example listening signoffs: **0/1,000**. Full independent linguistic/source-backed CEFR approval, final dual-voice audio and listening, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting, privacy/54 lessons/separate IELTS 1,000/production-audio preservation verification and confirmed live deployment remain outstanding.

**No merge, no main modification, no public launch. Release remains BLOCKED / STAGING ONLY.**
