# CEFR 1,000 staging research — six held C1 exact-sense investigations (2 November 2026)

**Scope:** user-approved **1,000 total** (A1/A2/B1/B2/C1 = 200 each), **not** the superseded 5,000-word plan. **Staging branch only:** `cefr-5000-bilingual-qa-staging`. No production change, merge, or launch permission bypass.

## Source and access limitations

On **2026-11-02**, public search-index extracts of Cambridge Dictionary headword pages were inspected for **spy, popularity, neutral, sacred, signature, copyright**. Attempts to open Cambridge headword pages directly returned **HTTP 403**. Accordingly, the labels below are **publisher-indexed research leads, not direct-page verification and not independent human CEFR signoff**. Do not infer a level from a different part of speech, a different sense, a translation page, or the Cambridge Business/Academic dictionary subsections.

| Frozen C1 headword/POS | Cambridge indexed exact-sense lead | Editorial disposition (not approval) | Publisher URL |
| --- | --- | --- | --- |
| spy (noun) | **B1 noun** person secretly collecting/reporting information; **C1 verb** is a distinct entry | **High-priority C1/B1 conflict; POS collision** | https://dictionary.cambridge.org/dictionary/english/spy |
| popularity (uncountable noun) | **B2 noun** being liked/supported by many people | **High-priority C1/B2 conflict**; frozen definition/example align with indexed B2 sense | https://dictionary.cambridge.org/us/dictionary/english/popularity |
| neutral (adjective) | **C1** not taking sides in an argument or war | Indexed C1 alignment lead; distinguish unobtrusive-colour and specialist scientific senses | https://dictionary.cambridge.org/us/dictionary/english/neutral |
| sacred (adjective) | **C1** holy/religious; separate **C2** figurative too-important-to-change sense | Indexed C1 alignment lead for frozen temple example; keep figurative sense separate | https://dictionary.cambridge.org/dictionary/english/sacred |
| signature (noun) | Handwritten-name sense observed, **exact-sense CEFR not established** | **C1 unsubstantiated**; the separate verb `sign` cannot prove the level of `signature` | https://dictionary.cambridge.org/dictionary/english/signature |
| copyright (noun) | Legal right to control use/copying observed, **exact-sense CEFR not established** | **C1 unsubstantiated**; Business English/Law labels are not CEFR badges | https://dictionary.cambridge.org/us/dictionary/english/copyright |

## Bilingual and example review handoff

The six-card [research packet](draft/CEFR-1000-C1-SIX-SPY-POPULARITY-NEUTRAL-SACRED-SIGNATURE-COPYRIGHT-INDEX-2026-11-02.json) preserves **original frozen English definition, Myanmar meaning, original example, source path/index/blob SHA**, dated publisher URLs, exact-sense/POS warnings and six **self-drafted, unapproved** English/Myanmar/example alternatives. Human-independent reviewers must separately check the English sense, natural Myanmar wording, grammar/originality, level-specific publisher evidence and British pronunciation. The original shortlist remains unchanged.

**Source integrity:** `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` Git blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; six-card research packet blob SHA `26c52a26f541c65ede562c89e5d9ee9754722e87`.

## Mechanical safeguard and verification limits

Added [fail-closed auditor](tools/audit_cefr_1000_c1_six_spy_popularity_index.py) with frozen blob checks, 200-per-level quotas, global headword deduplication, source-provenance equality, publisher-access/CEFR/POS controls, and rejection of forged independent-review, audio, physical iPhone and deployment claims. Added synthetic adversarial mutation self-tests; the auditor is wired into **all six parallel A1/A2/B1/B2/C1/ALL** structural lanes and the documentary **NO DEPLOY** gate. A connector-side readback on 2026-11-02 independently confirmed 200/level, 1,000 unique headwords, original fields preserved, all review flags false and all entries held. **This is not a claim that the new Python auditor or CI jobs have passed.**

Previous baseline [structural run 41394722700](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41394722700) showed six SUCCESS jobs; [documentary run 41394736038](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41394736038) showed documentary SUCCESS. **Both predate these commits**. The connector's commit-workflow-run endpoint returned no new runs (it only exposes PR-triggered runs); current push-triggered run IDs, job conclusions and logs are **unverified**. Next run must retrieve actual new run/job IDs and logs, repair failures and record the result before asserting CI pass.

## Truthful release status

| CEFR level | First-pass written | Independently approved |
| --- | ---: | ---: |
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

All 1,000 remain on **editorial hold**. No approved manifest. Final George/Emma headword + example audio generation and **actual human listening signoffs** are missing; browser/mobile regression, **physical iPhone Safari** evidence, measured GitHub Pages hosting limits and confirmed production deployment are also missing. Preserve 54 lessons, the separate IELTS 1,000-word bank, existing production George/Emma audio and privacy protections. **RELEASE BLOCKED — STAGING ONLY.**


## 2026-11-02 staging CI baseline repair

The previous six-card auditor failed closed in both the 06:07 UTC and 07:05 UTC push-triggered CI cycles. Actual [structural run 41403993216](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41403993216) failed all six A1/A2/B1/B2/C1/ALL jobs; [documentary run 41404006448](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41404006448) also failed. Logs identified the same root cause: `BLOCK: publisher exact-sense context missing: popularity`. The research packet's `other_sense_warning` had been only `B2 noun`, shorter than the auditor's required 12 characters. This was a **genuine fail-closed baseline failure**, not evidence of independent linguistic review or a reason to weaken the gate.

Replaced the ambiguous warning with an explicit statement that the indexed B2 label applies to the uncountable noun and that the indexed result did not establish a C1 label for the matching sense. The Cambridge direct-page HTTP 403 caveat and 2026-11-02 observation date remain unchanged. Re-pinned the auditor to research blob `26c52a26f541c65ede562c89e5d9ee9754722e87` and added 24 negative mutations (empty or truncated exact-sense context across all six records). Repair commits: [`0eb5b7f`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/0eb5b7fc40c4cb14207ac393557faea0df3b20e6) and [`4f8b38d`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/4f8b38d02246c5f909a46bc6a2ed1d614528740f). The frozen 1,000-word shortlist remains unchanged. These repairs are mechanical research integrity work, not independent approval.

Fresh push-triggered [structural run 41418285519](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41418285519) and [documentary run 41418285338](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41418285338) were initiated for commit `4f8b38d02246c5f909a46bc6a2ed1d614528740f`. Both runs subsequently completed **SUCCESS** for tested SHA `4f8b38d02246c5f909a46bc6a2ed1d614528740f`. The structural run's six actual jobs A1/A2/B1/B2/C1/ALL all concluded success (ALL job `125187390430`; C1 job `125187390565`). The documentary run's job `125187388159` concluded success; its actual log reports **115/115 synthetic adversarial mutations rejected** and explicitly **zero human approvals**. These checks verify the repaired research-integrity baseline only; they are not independent linguistic, pronunciation, listening, device or release verification. All 1,000 remain on editorial hold with 0 independent approvals. **NO DEPLOYMENT.**
