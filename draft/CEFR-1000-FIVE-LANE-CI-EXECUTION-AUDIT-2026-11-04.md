# CEFR-1000 CI execution audit — 2026-11-04

Staging-only. The approved scope remains 1,000 words, 200 per A1/A2/B1/B2/C1, not 5,000.

GitHub Actions [run 41771552059](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41771552059) completed **success** on 2026-11-04, testing commit `059c6547c31d487044bbd93f28a7c0a00354a6ef`. Directly inspected [run](https://api.github.com/repos/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41771552059) and [job](https://api.github.com/repos/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41771552059/jobs) records. A1 job 126382164337, A2 126382164309, B1 126382164346, B2 126382164538 and C1 126382164007 all concluded success. Every listed step in each job, including the synthetic mutation suite and empty-evidence rejection, concluded success. Raw test logs were not fetched; individual assertion output is not independently quoted.

**Coverage gap:** All five matrix jobs execute the exact same ten synthetic tests, without passing their CEFR matrix level to the tests. Five green jobs do **not** mean five distinct level-specific test suites. Next engineering task: parameterise adversarial tests by level and assert that the selected lane is tested; preserve a full-inventory cross-level check. The validator checks evidence fields and flags but does not authenticate reviewers, real listening, devices, or source provenance.

Inventory (previously inspected frozen shortlist, not re-counted this run): A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0 (first-pass/independently approved). All 1,000 remain editorial hold. Publisher-supported exact-sense CEFR and independent bilingual/example reviews, 4,000 George/Emma recordings and actual listening signoff, browser/mobile/physical iPhone QA, GitHub Pages limits, preservation/privacy and production deployment remain blocked or unverified.

No merge, approval flags, production write or publication. This report's new commit is not certified by the earlier run.
