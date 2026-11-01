# CEFR 1000 — UK pronunciation heteronyms and audio-sense preflight (1 November 2026)

**Scope:** USER-APPROVED **1,000 TOTAL** only (A1/A2/B1/B2/C1: 200 each). Research and structural checks exclusively on `cefr-5000-bilingual-qa-staging`. The previous 5,000-word plan is superseded. No release or production edit is authorised until ALL independent QC gates pass.

## Substantive findings and publisher provenance

A fresh complete scan of the 1,000 frozen provisional entries selected 14 high-value British-English headword pronunciation/sense cases: **A1 3, A2 1, B1 4, B2 4, C1 2**. Their complete frozen English/Myanmar/example snapshots, source paths/indices/blob SHAs, indexed publisher UK IPA variants, observation date and reviewer handoff are stored in [the 14-record research packet](draft/CEFR-1000-BRITISH-PRONUNCIATION-HETERONYMS-FOURTEEN-2026-11-01.json).

| Draft CEFR and intended POS | UK draft pronunciation lead | Contrast that must not replace it |
| --- | --- | --- |
| A1 read (present/habitual verb) | /riːd/ | Past-tense *read* /red/ |
| A1 use (verb) | /juːz/ | Noun /juːs/ |
| A1 minute (time noun) | /ˈmɪn.ɪt/ | Adjective 'tiny' /maɪˈnjuːt/ |
| A2 project (noun) | /ˈprɒdʒ.ekt/ | Verb /prəˈdʒekt/ |
| B1 progress (noun) | /ˈprəʊ.ɡres/ | Verb /prəˈɡres/ |
| B1 produce (verb) | /prəˈdʒuːs/ | Agricultural noun /ˈprɒdʒ.uːs/ |
| B1 address (noun) | /əˈdres/ | **UK verb is also /əˈdres/**: negative control, no invented stress conflict |
| B1 separate (adjective) | /ˈsep.ə.rət/ | Verb /ˈsep.ə.reɪt/ |
| B2 conduct (verb) | /kənˈdʌkt/ | Noun /ˈkɒn.dʌkt/ |
| B2 suspect (verb) | /səˈspekt/ | Noun/adjective /ˈsʌs.pekt/ |
| B2 graduate (verb) | /ˈɡrædʒ.u.eɪt/ | Noun /ˈɡrædʒ.u.ət/ |
| B2 contrast (noun) | /ˈkɒn.trɑːst/ | Verb /kənˈtrɑːst/ |
| C1 advocate (verb) | /ˈæd.və.keɪt/ | Noun /ˈæd.və.kət/ |
| C1 permit (noun) | /ˈpɜː.mɪt/ | Verb /pəˈmɪt/ |

**Source status:** The Cambridge Dictionary search index exposed these UK IPA/POS distinctions on **2026-11-01**, but direct page-opening attempts returned **HTTP 403**. The packet therefore records `SEARCH_INDEX_VISIBLE_DIRECT_PAGE_403` and **does not** label the research as directly inspected publisher pages, independently verified pronunciation, real human listening, or CEFR approval. Publisher URL pattern: `https://dictionary.cambridge.org/pronunciation/english/<headword>`. Examples include [permit](https://dictionary.cambridge.org/pronunciation/english/permit), [advocate](https://dictionary.cambridge.org/pronunciation/english/advocate), [read](https://dictionary.cambridge.org/pronunciation/english/read), [produce](https://dictionary.cambridge.org/pronunciation/english/produce), [minute](https://dictionary.cambridge.org/dictionary/english/minute) and [address](https://dictionary.cambridge.org/pronunciation/english/address).

**Exact-sense/CEFR reviewer warnings:** The Cambridge indexed dictionary distinguishes *minute* A1 time-unit sense from A2 'wait a minute' short-wait usage; the draft example could be read either way. It identifies *produce* B1 manufacturing verb versus C2 agricultural noun. It labels *advocate* as a C2 verb, conflicting with the provisional C1 placement. These are **publisher-indexed review leads, not final classifications or human-independent decisions**. UK noun and verb *address* share the indexed /əˈdres/ pronunciation, so treating every noun/verb homograph as a stress contrast would be an error.

## Fail-closed safeguards

Created [`tools/audit_cefr_1000_uk_heteronym_audio_risks.py`](tools/audit_cefr_1000_uk_heteronym_audio_risks.py). It binds all 14 cases to the frozen shortlist's exact English/Myanmar/example and historical source provenance; enforces the dated publisher access limitation and observed UK IPA/POS pairs; checks the deliberately same-pronunciation *address* control; rejects any manufactured independent approval, reviewer receipt, George/Emma headword or example listening claim. Its negative self-test is designed to reject **356 forged mutations** (14 × 25 plus 6 top-level changes). This is structural documentary validation only, never human review or actual listening.

Added the auditor to all **six parallel A1/A2/B1/B2/C1/ALL structural GitHub Actions lanes** and the documentary no-deployment workflow, including both trigger-path lists. Actual run IDs for the new workflow changes: structural [41261594641](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41261594641) and documentary [41261597262](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41261597262). **Actual GitHub Actions verified:** structural run **SUCCESS** in all six A1/A2/B1/B2/C1/ALL jobs, code SHA `4c2002c78ee4ac26af200d1d574050c9809be259`; documentary run **SUCCESS**, report-only, code SHA `fba4b030df932a7dc3c7672683cf0d438b33bd1f`. Actual ALL and documentary job logs confirmed **356/356 forged source, UK IPA, historical provenance, false-approval and false-listening mutations rejected**. Structural ALL artifact ID `13065402420`; documentary blocker artifact ID `13065776142`. The documentary job's production-protection step reported existing lessons, IELTS, George/Emma and privacy assets unchanged. **CI success is only structural/documentary and does not independently verify pronunciation or listening.**

## Truthful release inventory

| Level | First-pass written | Independently checked and approved | Publisher Oxford core-list observations | Final George/Emma headword + example listening |
| --- | ---: | ---: | ---: | ---: |
| A1 | 200 | 0 | 195/200 | 0/200 |
| A2 | 200 | 0 | 200/200 | 0/200 |
| B1 | 200 | 0 | 200/200 | 0/200 |
| B2 | 200 | 0 | 200/200 | 0/200 |
| C1 | 200 | 0 | 200/200 | 0/200 |
| **Total** | **1,000** | **0** | **995/1,000** | **0/1,000** |

The five A1 Oxford observation exceptions are separately documented inflected forms and a rabbit sense. **995 observations do not mean 995 CEFR approvals.** The new pronunciation packet is an additional independent-review handoff, not a change to the frozen 1,000.

**Release remains BLOCKED / STAGING ONLY.** Required: independently authenticated English/Myanmar/example/exact-sense CEFR and pronunciation signoff for all 1,000, approved 200-per-level deduplicated manifest, real British George/Emma audio generation and actual human listening of both headword and example for every entry, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages limits, protected 54 lessons + separate IELTS 1,000 + existing George/Emma production audio/privacy integrity, and confirmed live production deployment. No merge or publication.
