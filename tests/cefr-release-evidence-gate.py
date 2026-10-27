#!/usr/bin/env python3
"""Negative tests for CEFR publication-reference guard; no real content approved."""
import importlib.util
import pathlib
import tempfile

root = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("release_gate", root / "tools/validate_cefr_release.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.TARGETS == {level: 200 for level in ("A1","A2","B1","B2","C1")}
# Punctuation and ordinary inflections must not cause false release failures.
assert module.example_has_headword_or_regular_form("student", "I am a student.")
assert module.example_has_headword_or_regular_form("however", "However, the room was small.")
assert module.example_has_headword_or_regular_form("manage", "We managed to finish the work.")
assert module.example_has_headword_or_regular_form("grab", "She grabbed her bag.")
assert module.example_has_headword_or_regular_form("hand", "Please wash your hands.")
assert not module.example_has_headword_or_regular_form("cat", "The catalogue is on a shelf.")
assert not module.example_has_headword_or_regular_form("go", "They went to school.")

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
assert any("Exactly 1000 entries required" in x for x in issues), issues
assert any("Release status" in x for x in issues), issues
# The provisional A1 'i' spelling is not acceptable in a future approved
# manifest even though all word matching is case-insensitive.
entry["word"] = "i"
entry["example_sentence"] = "I am ready."
issues = module.validate(data)
assert any("first-person singular pronoun must be displayed as capital I" in x for x in issues), issues
entry["word"] = "I"
issues = module.validate(data)
assert not any("first-person singular pronoun must be displayed as capital I" in x for x in issues), issues
entry["word"] = "apple"
entry["example_sentence"] = "I eat an apple."

entry["source_burmese"] = "https://dictionary.cambridge.org/dictionary/english/apple"
entry["source_level"] = "https://dictionary.cambridge.org/dictionary/english/apple"
issues = module.validate(data)
assert not any("generic non-word-specific reference" in x for x in issues)
with tempfile.TemporaryDirectory() as folder:
    issues = module.validate(data, pathlib.Path(folder), verify_audio=True)
    assert "Audio manifest absent" in issues
assert "Audio verification requested without a root directory" in module.validate(data, verify_audio=True)
print("PASS: generic/placeholder references rejected; review flags and incomplete audio block publication.")
