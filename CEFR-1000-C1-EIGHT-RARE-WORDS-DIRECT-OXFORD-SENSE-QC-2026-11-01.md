# CEFR-1000 C1 eight rare-word Oxford exact-sense research — 2026-11-01

**Scope:** User-approved **1,000 total**, A1/A2/B1/B2/C1 **200 each**; `cefr-5000-bilingual-qa-staging` only. The 5,000-word proposal is superseded. **All eight records remain unapproved, and all 1,000 remain on editorial hold.** This is source-supported research, not independent CEFR verification or a release approval.

## Directly observed publisher sources (Oxford Advanced Learner's Dictionary)

The following Oxford **English dictionary pages were opened directly on 2026-11-01**. Each source URL, observed date, line locator, original bilingual fields, source path/index/blob SHA and proposed unapproved alternative are preserved in [the eight-card research packet](draft/CEFR-1000-C1-EIGHT-DIRECT-OXFORD-RARE-SENSE-TRIAGE-2026-11-01.json).

| C1 provisional word | Direct Oxford URL | Lines | Exact-sense editorial finding |
|---|---|---|---|
| ambivalence | https://www.oxfordlearnersdictionaries.com/definition/english/ambivalence | 101–107 | Mixed positive **and** negative feelings, not simple indifference |
| anachronism | https://www.oxfordlearnersdictionaries.com/definition/english/anachronism | 101–109 | Old-fashioned object/person versus historically misplaced detail are different senses; the frozen payment-machine example is the former |
| antipathy | https://www.oxfordlearnersdictionaries.com/definition/english/antipathy | 101–110 | Formal strong dislike, not merely disagreement; `towards` is a supported complement |
| arbitrate | https://www.oxfordlearnersdictionaries.com/definition/english/arbitrate | 101–118 | Formal settling of a dispute between parties, not merely giving an opinion |
| belligerent | https://www.oxfordlearnersdictionaries.com/definition/english/belligerent_1 | 101–110 | Hostile person versus war-fighting country; frozen passenger example uses the former |
| benevolent | https://www.oxfordlearnersdictionaries.com/definition/english/benevolent | 101–119 | Kind, generous person versus use in a charitable organisation's name |
| brevity | https://www.oxfordlearnersdictionaries.com/definition/english/brevity | 101–115 | **Actionable issue:** frozen definition and Myanmar gloss combine concise expression and short duration, while frozen report example teaches concise expression only |
| circumspect | https://www.oxfordlearnersdictionaries.com/definition/english/circumspect | 101–106 | Careful risk assessment before action, not simply secrecy |

**Important evidence boundary:** Oxford's `c2` topic tags appear near anachronism's historical sense, arbitrate's discussion sense, belligerent's senses and benevolent's personal-quality sense. A topic tag is **not** independent, publisher-verified exact-sense CEFR classification of the provisional C1 word. No automatic move to C2 or approval is warranted. For the remaining entries no exact-sense CEFR rating was established. An independent reviewer must confirm the word/POS/sense/level, fluent Myanmar, example grammar and provenance. The frozen shortlist was **not edited**.

## Fail-closed integrity and CI wiring

Added [the eight-card source/provenance auditor](tools/audit_cefr_1000_c1_rare_eight_direct_oxford.py). It pins the research packet's Git blob `fd87b46061fc7240ff297ea4e117d497a7c00913` and frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; compares the eight original bilingual/example/POS/provenance fields against the frozen shortlist; requires publisher URL, observation date, source locator and explicit editorial holds; and rejects synthetic forged source, translation, CEFR, approval and audio claims. The self-test defines **135 adversarial mutations** (16 per card, six root and one deletion), but **no actual CI pass is claimed until run logs are inspected**.

Wired the auditor to the existing parallel A1/A2/B1/B2/C1/ALL structural workflow (one audit per lane, adversarial self-test in ALL) and the documentary no-deployment workflow. Staging code/research commits: packet `b5dab447ccf2e1db1f3f84bd153cc51b7773788f`, auditor `1243a670b0b5ce41d5364244cc662a9a17cce257`, structural wiring `cbbee67223beb5dbcda2613585ae5d7798917603`, documentary wiring `3a22f8ac421c53d997e2ebaa3bcd2f92b1caabf6`. GitHub commit workflow-run lookup currently returns no pull-request-triggered runs and combined statuses are empty; **new push-triggered job IDs/conclusions/logs have not been independently retrieved**. These checks are **structural, not linguistic approval**.

## Exact release blockers

| Level | Provisional written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Missing: independent exact-sense English/Myanmar/example/CEFR signoffs for all 1,000, an approved deduplicated manifest, actual final George and Emma headword/example audio generation and **human listening** receipts, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting readiness, final preservation/privacy signoff for the existing 54 lessons, separate IELTS 1,000-word bank and established production voices, and confirmed production deployment. **STAGING ONLY / RELEASE BLOCKED. No merge, main edit or publication.**

## Verified GitHub Actions conclusions and actual logs — 2026-11-01

The previously unverified runs were subsequently retrieved through the GitHub Actions API and their job logs inspected. [Structural run **41323587535**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41323587535) **completed SUCCESS** at test SHA `cbbee67223beb5dbcda2613585ae5d7798917603`; all six jobs A1/A2/B1/B2/C1/ALL concluded success. ALL job `124898762102` log explicitly recorded **135/135** synthetic eight-card mutations rejected, **0** independent approvals and unchanged protected production assets; ALL artifact ID `13090307267`. [Documentary no-deploy run **41323592372**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41323592372) **completed SUCCESS as report-only** at test SHA `3a22f8ac421c53d997e2ebaa3bcd2f92b1caabf6`, job `124898777498`; its log separately confirmed 135/135 synthetic rejections, 0/1,000 independent word reviews, absent George/Emma listening receipts, physical iPhone, browser/mobile, hosting, approved manifest and production signoffs. Blocker artifact ID `13090540999`. Documentary SUCCESS means that reporting/protection checks passed, **not** that release gates passed. The staging research remains held; no main modification, merge or publication.
