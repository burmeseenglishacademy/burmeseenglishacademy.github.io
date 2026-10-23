# Burmese English Academy — CEFR release checkpoint (24 October 2026, SGT)

**Status: STAGING ONLY — NOT RELEASE READY.** **Do not merge this staging branch into `main`.**
Latest production `main` HEAD verified: `dca0db7aa30118ecc18350db8dc406e6cac91554` (v1.2.5).
Latest staging branch snapshot at this checkpoint: `23f8d4bd5be7ebcc320fae1acc2b2c735a3c7e47`.

## Verified work actually completed this session

1. Added `tools/audit_cefr_editorial_evidence.py` and [evidence audit workflow run 40000000330](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40000000330) — **SUCCESS**, report artifact `CEFR-5000-EVIDENCE-AUDIT-UNVERIFIED` (artifact 12521472521, expiring 22 November 2026). This is a work queue, not a semantic or translation sign-off.
2. Harder release validator `tools/validate_cefr_release.py` refuses generic Oxford page URLs, example.org placeholders and some other unspecific URL patterns. This is URL-shape screening, **not proof a URL verifies the claimed meaning**. Negative tests `tests/cefr-release-evidence-gate.py` passed in [workflow 40000388888](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40000388888).
3. New read-only A1 audio overlap inventory `tools/inventory_cefr_a1_audio.py` passed in [workflow 40000653138](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40000653138), report artifact `CEFR-A1-AUDIO-REUSE-UNREVIEWED` (12522375505). None of these recordings was created or published by that test.
4. Integrated [A1 regression 40000819628](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40000819628) **SUCCESS** including evidence checks, existing lessons, 1,000 IELTS words and old audio-manifest regression.
5. New [Chromium and emulated mobile WebKit regression 40000843041](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40000843041) **SUCCESS**. This is **not a physical iPhone Safari test**.

## Measured gaps — do not misrepresent them

- **500 A1 editorial draft records**, each has an initial English definition, Burmese draft meaning and example; **0/500 independently approved**.
- **5,000 frequency/WordNet-derived provisional candidate headwords**; the candidate corpus itself still has **5,000/5,000 blank `burmese_meaning` fields**. The separate 500-entry editorial draft is NOT a verified or published dataset.
- Evidence audit flagged **500/500 A1 generic (non-word-specific) CEFR level source links, 489/500 English source references too generic, and 500/500 lacking independently corroborated Burmese evidence**.
- A1 has **992 unique words/example texts**, requiring **1,984 George/Emma voice file mappings**. The published audio catalogue already contains **22 reusable recordings**; **1,962 missing new recordings**. This is file/manifest verification only, not subjective listening approval.
- New A1 pronunciation pilot 40 files had previously completed with a technical-success artifact, but none has independent auditory approval.
- The remaining **A2–C1 4,500 candidate entries** still need original English/Mynamar editorial content, sense/level review and all new audio.
- Full 5,000 headword + example recordings, independent pronunciation review, final published-site asset size and physical iPhone verification are NOT done.

## Deployment and host constraints

- The existing version 1.2.5 remains on the default branch. No CEFR vocabulary/data/audio has been merged into production.
- Current GitHub repository metadata reported approximately **119 MiB repository size**; this **is not** a measured published Pages site size.
- GitHub's official [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) specify a **1 GiB-class published site cap** (stated as 1 GB) and **100 GB/month soft traffic limit**. Size, total download traffic and deployment behavior still require measuring once new MP3s exist.
- Audio and drafts must remain in staging until source-based semantic approvals, human language review, deterministic audio inventory/decoding, pronunciation spot listening, and cross-device regression pass.
- Neither CI success nor review checkboxes alone certify an English-Myanmar translation or pronounceability.

**No claim of full completion or permission to bypass the release gate is made.**
