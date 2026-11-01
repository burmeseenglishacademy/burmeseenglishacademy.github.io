# CEFR 1000 — GitHub Pages hosting limits and evidence gate (1 November 2026)

**STAGING ONLY.** Official [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) were directly checked on **2026-11-01** (usage limits, page lines 31–49). This is a policy check, **not a measurement of this site's actual deployed size, throughput, or runtime**.

| Official rule | Conservative staging validator requirement |
| --- | --- |
| Source repository recommended limit **1 GB** | Source repository measured bytes must be positive and no greater than **1,000,000,000** |
| Published Pages site maximum **1 GB** | Published site artifact measured bytes must be positive and no greater than **1,000,000,000** |
| Pages deployment timeout **10 minutes** | Independently documented actual deployment duration must be **1–600 seconds** |
| Pages soft bandwidth limit **100 GB/month** | Documented monthly traffic estimate must be positive and no greater than **100,000,000,000 bytes** |
| Pages soft limit **10 builds/hour** | For **native Pages builds**, observed build count in the last hour must be **0–10** |
| **Custom GitHub Actions** site builds | Exempt from native **10 builds/hour** limit; **not exempt** from site size, bandwidth review or deployment timeout |
| Pages is not a commercial SaaS host | Preserve the Academy's free educational, noncommercial and privacy-first scope |

The [staging release-readiness auditor](tools/audit_cefr_1000_launch_readiness.py) now fails closed when the hosting receipt lacks an actual positive deployment duration, an explicit native/custom build method, an observed hourly build count, or a specific GitHub Actions run URL. It rejects 601-second deployments, 11 native builds in an hour, fabricated non-GitHub run URLs, and missing fields; a synthetic custom Actions case confirms the documented exemption without waiving the 600-second timeout. This validator checks **documentary shape only**. A supplied run URL is **not** proof that the actual GitHub job succeeded. A human reviewer must inspect real run/job conclusions and logs, and separately confirm the published site measurements and asset integrity.

The evidence ledger still has `hosting_limits_check: null`. No actual final approved corpus/site build, published artifact measurement, production run-duration evidence, traffic estimate, or hosting signoff has been supplied. **Hosting gate remains BLOCKED.** No main-branch edit, production asset modification, merge or publication is authorised until every release gate, including 1,000 independent reviews, actual George/Emma listening, browser/mobile/physical iPhone Safari and protected assets, is verified.

## Verified staging documentary QC (2026-11-01)

[Documentary run 41266448123](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41266448123) completed **SUCCESS (report-only)** on code SHA `402ccbb8675cf83441e32bc5e9e3624b5f891fbc`. Its actual job log confirmed that synthetic hosting tests rejected over-600-second deployments, native build counts over 10/hour, missing evidence and invalid run URLs, while preserving the custom GitHub Actions native-build-rate exception. Documentary blocker artifact `13067785722` records **no measured hosting evidence**. This is **not** a real deployment test or hosting signoff.
