# Audio provenance and licences

Verified 22 October 2026 against upstream sources.

Kokoro-82M is published by hexgrad under Apache License 2.0, as is the Kokoro
inference library. `bm_george` and `bf_emma` are listed in its British English
voice catalogue. No separate paid licence or API subscription is specified for
these voices. We generate speech locally from the Academy's existing texts.
The website serves generated recordings, not model weights or a hosted API.

The upstream Apache-2.0 licence is retained in `licenses/Kokoro-Apache-2.0.txt`.
If redistributing the library/model, retain licence and attribution notices,
identify modifications, and retain applicable upstream NOTICE material. This
notice does not relabel the Academy's existing lessons or website under Apache.
Model licensing is not a guarantee of error-free speech or exclusive copyright
in generated audio. George and Emma are synthetic voice identifiers, not a
claim of personal endorsement.

Sources:
- https://huggingface.co/hexgrad/Kokoro-82M
- https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
- https://github.com/hexgrad/kokoro/blob/main/LICENSE

Installed build-time dependencies (PyTorch, Misaki, spaCy, ffmpeg, etc.) retain
their own licences and are not bundled in the website or source delivery.
The optional local ASR check uses faster-whisper and the small.en Whisper model;
these are also build-time tools, not website dependencies, and are not shipped.
No learner audio or text is sent to a transcription service.
