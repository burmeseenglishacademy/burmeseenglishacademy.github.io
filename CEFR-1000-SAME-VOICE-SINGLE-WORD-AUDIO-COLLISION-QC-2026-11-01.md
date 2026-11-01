# CEFR 1,000 — same-voice single-word audio-copy release regression (1 November 2026)

**Scope:** user-approved **1,000 total** CEFR vocabulary cards (A1/A2/B1/B2/C1 exactly **200 each**). Branch `cefr-5000-bilingual-qa-staging` only. **RELEASE BLOCKED / NO DEPLOYMENT.**

## Actual defect and repair

The previous `tools/validate_cefr_release.py::audio_collision_risks` rejected byte-identical MP3s between George and Emma and distinct multiword examples, but **accepted identical MP3 bytes for any two different same-voice single-word headwords**. This permitted a copied George `apple` clip to masquerade as George `orange`, even though the words are not homophones. An existing legitimate `two`/`too` synthetic homophone control masked this gap.

The corrected release validator **rejects all same-voice distinct-headword byte collisions by default**, with a narrowly explicit `two`/`too` exception. Other potential homophones are **not** silently approved: add any exception only after source-supported phonetic assessment and real independent listening. Every cross-voice identical-byte collision remains blocked, even between different words; all distinct multiword utterance collisions remain blocked. This is only a file-byte integrity safeguard, **not a proof that speech is correct or that any person listened**.

- Validator code commit: [`e1c0f24374f2647e54929f6d3febc9b6e3d6c0fd`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/e1c0f24374f2647e54929f6d3febc9b6e3d6c0fd).
- Adversarial test commit: [`c6c48779e5b5868ab007d047c9e763cdd7689d84`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/c6c48779e5b5868ab007d047c9e763cdd7689d84).
- New synthetic cases: `apple/orange` same voice must fail, `two/one` must fail, `two/too/orange` transitive collision must detect both unrelated pairs, `two/too` same voice may remain mechanically exempt, and all George/Emma cross-voice and multiword cases still fail.
- [Release evidence regression run 41318645107](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41318645107) **SUCCESS** on test commit `c6c48779`; job `124883969096` log confirms the new unrelated-single-word collision cases passed.
- [A1 integrated regression run 41318645081](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41318645081) **SUCCESS** on the same test commit.
- Six-lane structural run [41318645132](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41318645132) and documentary no-deployment run [41318645110](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41318645110) were **in progress at initial report creation**; their actual conclusions/logs must be checked before claiming full CI success. Earlier six-lane [41313788683](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41313788683) succeeded on previous SHA `ac492855`, including 123/123 six-card adversarial source mutations; it does not verify this new audio fix.

## Publisher pronunciation corroboration and evidence limit

On **2026-11-01**, Cambridge publisher search-index results for [two](https://dictionary.cambridge.org/pronunciation/english/two) and [too](https://dictionary.cambridge.org/pronunciation/english/too) both displayed British **/tuː/**. Direct publisher-page opens returned **HTTP 403**. These are **indexed pronunciation leads only**, not a direct inspected-page receipt, independent pronunciation approval, generated George/Emma audio, or human listening. The narrowly documented mechanical homophone exception is still subject to actual voice-specific listening and independent reviewer signoff. All other same-voice different-headword byte collisions fail closed until a separately evidenced exception is explicitly added.

## Final verified CI readback (2026-11-01)

Both previously in-progress runs subsequently completed **SUCCESS**, testing the actual regression SHA `c6c48779e5b5868ab007d047c9e763cdd7689d84`:

- [Six-lane structural run 41318645132](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41318645132): **A1, A2, B1, B2, C1, ALL all SUCCESS**. ALL job `124883969497`, artifact `13087724299`; logs explicitly show **123/123** indexed six-card source mutations rejected and 1,000 held/zero independently approved. These are structural research tests, not human signoffs.
- [Documentary no-deployment run 41318645110](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41318645110): **SUCCESS as report-only**; job `124883969461`, blocker artifact `13088422350`. Logs explicitly report **missing approved manifest**, **missing independent stage signoffs**, and **no final protected-assets preservation signoff**; staging production-protection check passed.
- [Release regression 41318645107](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41318645107): **SUCCESS**, job `124883969096` explicitly confirms the unrelated single-word MP3 copy test and documented-homophone controls. [Integrated A1 regression 41318645081](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41318645081): **SUCCESS**.

**Important:** Passing CI only confirms the code's automated negative tests and staging research structure. It cannot certify any actual George/Emma audio generation, listening, human linguistic review, iPhone testing, hosting measurements or deployment. Release remains blocked.

## Counts and non-negotiable blockers

| Level | First-pass written | Independently approved | Final George/Emma listening |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |

The 1,000-word frozen shortlist is **still on editorial hold**, with **zero independent human receipts**. No approved deduplicated release manifest, complete real George/Emma headword/example recordings and human listening receipts, browser/mobile regression receipts, physical iPhone Safari evidence, measured GitHub Pages hosting signoff, production preservation signoff or confirmed live deployment. Existing 54 lessons, separate IELTS bank, production George/Emma audio and privacy must remain protected. **No merge, main modification or publication.**
