# CEFR 1,000 — publisher headword URL binding hardening (1 November 2026)

**Scope:** user-approved 1,000 total (A1/A2/B1/B2/C1 = 200 each), **staging only**. Do not merge, publish, change main, or treat structural URL checks as independent language review.

## Concrete vulnerability and repair

The future release structural validator previously checked only that each `source_english`, `source_burmese`, and `source_level` URL looked sufficiently specific. A URL such as `https://dictionary.cambridge.org/dictionary/english/banana` could be attached to a card for `apple` and pass the URL-shape test. Likewise a general grammar page could be entered as `source_level` without being an exact-headword dictionary source. This is not adequate evidence for a source-backed exact-sense CEFR release.

Staging repair in `tools/validate_cefr_release.py` introduces `publisher_headword_url_matches(url,word)`. It recognises only exact publisher dictionary hosts and headword paths for Cambridge English Dictionary and Oxford Learner's Dictionaries (including Oxford numbered homograph suffixes), rejects unrelated headwords and generic publisher lists, and requires the future `source_level` URL to match the reviewed word. Other source fields still permit legitimate non-dictionary explanatory resources, but if a publisher dictionary URL is used it must match the headword. This checks URL structure **only**; the separate release-evidence ledger still requires independently attested direct-publisher **exact-sense** CEFR, English, fluent Myanmar, example and pronunciation review. A dictionary page's mere existence or a word/POS topic tag is **not** a CEFR signoff.

## Negative-test additions

`tests/cefr-release-evidence-gate.py` now checks positive Cambridge apple and Oxford apple_1 URLs; negative Cambridge/Oxford banana URLs for an apple card, a fake host, an extra path segment, a generic Oxford wordlist, a generic British Council grammar page as CEFR level evidence, and wrong-headword URLs in all three source fields. The test keeps all mock reviewer flags false. No independent review receipt was created.

**Commits:** validator `0ca75554f782f1c3e87a681475c9cf51ac079351`; negative tests `b177de2ec3d0cbbeafa2a874dec4ef79af3aa639`. GitHub Actions run IDs/conclusions/logs for these commits are **not yet independently verified**; no CI success claim is made. The source-binding function was sanity-checked separately for two positive and two negative URL patterns, but this is not a full repository test.

## Release ledger — unchanged

| CEFR | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

All 1,000 provisional entries remain on editorial hold. Approved manifest: absent. Genuine independent review receipts: 0. Final George/Emma actual listening signoffs: 0/1,000. Browser/mobile automated evidence: 0. Physical iPhone Safari, hosting measurements and confirmed production deployment: absent. Protect 54 lessons, separate IELTS 1,000-word bank, established production voice audio and privacy. **RELEASE BLOCKED / STAGING ONLY.**
