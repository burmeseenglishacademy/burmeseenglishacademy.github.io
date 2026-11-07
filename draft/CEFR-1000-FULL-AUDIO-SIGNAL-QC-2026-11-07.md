# BEA CEFR-1000: complete provisional George/Emma audio signal audit

**Date:** 7 November 2026. **Status:** TECHNICAL PASS ONLY — **unreviewed**, **not deployed**, **not a human listening signoff**.

## Exact inputs and reproducibility

- GitHub Actions [full audio candidate run #41807100296](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41807100296), commit `71e1834eea5e8841205a03dcd34530a02c0089d7`, completed **success**.
- Actual complete candidate artifact: `cefr1000-COMPLETE-GEORGE-EMMA-CANDIDATE-UNREVIEWED`, artifact ID **13310534630**. Downloaded and read the ZIP archive directly for this audit; no production MP3 was changed.
- Scanned every `audio/{bm_george,bf_emma}/*.mp3` via libsndfile/soundfile to floating-point PCM and NumPy, and compared against SHA-256 digests, sample rates and durations in the 16 shard JSON reports. This is an *additional, post-build* check, beyond GitHub Actions' ffprobe/ffmpeg integrity gate.

## Verified technical inventory

| Metric | Observed |
|---|---:|
| Approved CEFR scope | 1,000 provisional entries (A1/A2/B1/B2/C1 × 200) |
| Distinct spoken passages | 1,996 |
| MP3s actually scanned | **3,992/3,992** |
| George | 1,996 |
| Emma | 1,996 |
| New provisional Kokoro audio | 3,716 |
| Byte-for-byte reused existing website recordings | 276 |
| New MP3 payload (before metadata and site packaging) | 71,458,096 bytes |
| Total candidate MP3 payload | 74,706,292 bytes |
| MP3 payloads with an incorrect recorded SHA-256 | **0** |
| Invalid sample-rate/mono/duration versus shard manifest | **0** |
| Near-silent decoded clips (RMS below 0.005) | **0** |
| Clips with decoded PCM peak at or above 0.999 | **0** |
| George/Emma same-text duration ratio over 2× | **0** |
| Other signal errors / clipping above 0.01% sample fraction | **0** |

Recorded duration range: **headwords 0.475–2.05 sec** (median 1.15 sec); **examples 1.60–6.95 sec** (median 3.35 sec). Maximum observed normalized amplitude 0.90; minimum individual clip peak 0.21995.

GitHub Pages [official limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) include 1 GB published-site cap and 100 GB/month soft bandwidth. Using the **previously reported production build size** of 124,894,352 bytes (October 23) and the 71,458,096 bytes of *new* candidate MP3 payload yields a **provisional ~196,352,448 byte subtotal**, before new vocabulary JS, manifest growth, site packaging and current build verification. **This is not a live usage/bandwidth measurement or final hosting clearance.** The unreviewed candidate audio should remain in staging GitHub Actions artifacts and must not be uploaded to the public Pages site yet.

## Boundaries and next tasks

1. **Human listening signoffs: 0**. Audio PCM signal and codec tests cannot verify word stress, voice naturalness, English lexical sense, accent fidelity or whether a heteronym is pronounced as the intended part of speech.
2. **Independent word approvals: 0/1,000**. Editorial first-pass and external dictionary leads do not constitute independent review. The frozen audio mapping becomes stale if any headword/example changes; regenerate changed clips and cryptographic manifests after approved corrections.
3. **Physical iPhone Safari QA: not verified**. WebKit browser emulation is not a physical iPhone test.
4. **Production release remains BLOCKED**. No approval flags, production branch, published site, release-evidence receipts or production MP3 assets are modified here.

This file records an actual all-file technical scan only; it is not a verified final listening certificate.
