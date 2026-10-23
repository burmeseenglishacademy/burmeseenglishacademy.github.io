#!/usr/bin/env python3
"""Negative tests for CEFR publication-reference guard; no real content approved."""
import importlib.util
import pathlib
import tempfile

root = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("release_gate", root / "tools/validate_cefr_release.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.source_url_is_specific("https://dictionary.cambridge.org/dictionary/english/apple")
assert module.source_url_is_specific("https://learnenglish.britishcouncil.org/free-resources/grammar/a1-a2-grammar/articles-a-an-the")
for url in (
    "http://dictionary.cambridge.org/dictionary/english/apple",
    "https://dictionary.cambridge.org/",
    "https://dictionary.cambridge.org/dictionary",
    "https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000",
    "https://example.org/dictionary/english/apple",
    "https://example.com/checked/word/apple",
    "https://www.oxfordlearnersdictionaries.com/",
    "",
):
    assert not module.source_url_is_specific(url), url

entry = {
    "word": "apple", "level": "A1", "part_of_speech": "noun",
    "english_definition": "A common round fruit.", "burmese_meaning": "ပန်းသီး",
    "example_sentence": "I eat an apple.",
    "source_english": "https://dictionary.cambridge.org/dictionary/english/apple",
    "source_burmese": "https://example.org/meaning/apple",
    "source_level": "https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000",
    "reviewed_english": False, "reviewed_burmese": False,
    "reviewed_example": False, "reviewed_level": False,
    "reviewed_pronunciation": False,
}
data = {"release_status": "UNVERIFIED_DRAFT_DO_NOT_PUBLISH",
        "targets": module.TARGETS, "entries": [entry]}
issues = module.validate(data)
assert any("generic non-word-specific reference" in x for x in issues), issues
assert any("reviewed_burmese not independently verified" in x for x in issues), issues
assert any("Exactly 5000 entries required" in x for x in issues), issues
assert any("Release status" in x for x in issues), issues
entry["source_burmese"] = "https://dictionary.cambridge.org/dictionary/english/apple"
entry["source_level"] = "https://dictionary.cambridge.org/dictionary/english/apple"
issues = module.validate(data)
assert not any("generic non-word-specific reference" in x for x in issues)
with tempfile.TemporaryDirectory() as folder:
    issues = module.validate(data, pathlib.Path(folder), verify_audio=True)
    assert "Audio manifest absent" in issues
print("PASS: generic/placeholder references rejected; review flags and incomplete audio block publication.")
