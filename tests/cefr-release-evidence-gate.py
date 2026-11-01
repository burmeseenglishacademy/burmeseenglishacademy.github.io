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

# A syntactically specific publisher URL for the wrong lemma must fail.
# No one may self-approve CEFR by attaching a generic PDF or unrelated entry.
assert module.publisher_headword_url_matches(
    "https://dictionary.cambridge.org/dictionary/english/apple", "apple")
assert module.publisher_headword_url_matches(
    "https://www.oxfordlearnersdictionaries.com/definition/english/apple_1", "apple")
for wrong in (
    "https://dictionary.cambridge.org/dictionary/english/banana",
    "https://www.oxfordlearnersdictionaries.com/definition/english/banana_1",
    "https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000",
    "https://example.net/dictionary/english/apple",
    "https://dictionary.cambridge.org/dictionary/english/apple/extra",
):
    assert not module.publisher_headword_url_matches(wrong, "apple"), wrong

entry["source_burmese"] = "https://dictionary.cambridge.org/dictionary/english/apple"
entry["source_level"] = "https://dictionary.cambridge.org/dictionary/english/apple"
issues = module.validate(data)
assert not any("generic non-word-specific reference" in x for x in issues)
# The validator must reject mismatched publisher URLs even when all
# human-review flags are still false (a distinct, fail-closed provenance error).
for field in ("source_english", "source_burmese", "source_level"):
    old_url = entry[field]
    entry[field] = "https://dictionary.cambridge.org/dictionary/english/banana"
    problems = module.validate(data)
    assert any(field in x and ("does not match headword" in x or "same-headword" in x)
               for x in problems), (field,problems)
    entry[field] = old_url
entry["source_level"] = "https://learnenglish.britishcouncil.org/free-resources/grammar/a1-a2-grammar/articles-a-an-the"
problems = module.validate(data)
assert any("source_level must bind to same-headword" in x for x in problems), problems
entry["source_level"] = "https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000"
problems = module.validate(data)
assert any("generic non-word-specific reference URL in source_level" in x for x in problems), problems
entry["source_level"] = "https://dictionary.cambridge.org/dictionary/english/apple"
with tempfile.TemporaryDirectory() as folder:
    issues = module.validate(data, pathlib.Path(folder), verify_audio=True)
    assert "Audio manifest absent" in issues
assert "Audio verification requested without a root directory" in module.validate(data, verify_audio=True)
# Synthetic fingerprints only: no actual George/Emma recording was generated,
# listened to, approved or released by these tests.
fake_a = "a"*64
fake_b = "b"*64
fake_c = "c"*64
assert module.audio_collision_risks([
    ("apple", "bm_george", fake_a), ("apple", "bf_emma", fake_a)
]) == [(("apple", "bm_george"), ("apple", "bf_emma"))]
assert module.audio_collision_risks([
    ("The apple is red.", "bm_george", fake_b),
    ("The apple is green.", "bm_george", fake_b)
]) == [(("The apple is red.", "bm_george"),
        ("The apple is green.", "bm_george"))]
# Homophones can legitimately have the same waveform for one voice;
# never mechanically claim that all byte-identical short words are bad.
assert module.audio_collision_risks([
    ("two", "bm_george", fake_c), ("too", "bm_george", fake_c)
]) == []
# Regression: the old validator let ANY two unrelated one-word headwords
# reuse identical bytes. Only an explicitly documented homophone exception
# may bypass the same-voice collision rule, pending real listening.
assert module.audio_collision_risks([
    ("apple", "bm_george", fake_a), ("orange", "bm_george", fake_a)
]) == [(("apple", "bm_george"), ("orange", "bm_george"))]
assert module.audio_collision_risks([
    ("two", "bm_george", fake_c), ("too", "bm_george", fake_c),
    ("orange", "bm_george", fake_c)
]) == [(("two", "bm_george"), ("orange", "bm_george")),
      (("too", "bm_george"), ("orange", "bm_george"))]
assert module.audio_collision_risks([
    ("two", "bm_george", fake_c), ("one", "bm_george", fake_c)
]) == [(("two", "bm_george"), ("one", "bm_george"))]
# A third clip must be compared with *every* previous identical-byte clip,
# not just the first (the first two are legitimate same-voice homophones).
# Cross-voice collisions are forbidden even for DIFFERENT headwords.
assert module.audio_collision_risks([
    ("two", "bm_george", fake_c),
    ("too", "bm_george", fake_c),
    ("too", "bf_emma", fake_c),
]) == [(("two", "bm_george"), ("too", "bf_emma")),
      (("too", "bm_george"), ("too", "bf_emma"))]
assert module.audio_collision_risks([
    ("apple", "bm_george", fake_a), ("orange", "bf_emma", fake_a)
]) == [(("apple", "bm_george"), ("orange", "bf_emma"))]
# A two-word example is still a distinct utterance: the previous >=3-word
# threshold let copied "Good morning" / "Good evening" clips pass.
assert module.audio_collision_risks([
    ("Good morning", "bm_george", fake_b),
    ("Good evening", "bm_george", fake_b),
]) == [(("Good morning", "bm_george"), ("Good evening", "bm_george"))]
# Legitimate same-voice one-word homophones remain eligible for listening.
assert module.audio_collision_risks([
    ("two", "bm_george", fake_c), ("too", "bm_george", fake_c)
]) == []
assert module.audio_collision_risks([
    ("apple", "bm_george", fake_a), ("apple", "bf_emma", fake_b)
]) == []
# Do not count be/do inflections, good/bad comparison forms, or irregular
# plurals of existing man/woman/child/foot lemmas as separate lexemes.
# Plural forms may be taught as grammar without inflating a 200-lemma quota.
for form, lemma in (("is","be"),("are","be"),("does","do"),("did","do"),
                    ("better","good"),("worst","bad"),("men","man"),
                    ("women","woman"),("children","child"),("feet","foot")):
    entry["word"] = form
    entry["example_sentence"] = {"is":"She is at home.","are":"They are friends.",
                                 "does":"Does he work here?","did":"Did you eat?",
                                 "better":"This is better.","worst":"That was the worst.",
                                 "men":"The men are here.","women":"The women are here.",
                                 "children":"The children are playing.","feet":"My feet hurt."}[form]
    issues = module.validate(data)
    assert any("grammatical form of " + lemma in x for x in issues), (form,issues)
for lemma in ("be","do","good","bad","man","woman","child","foot"):
    entry["word"] = lemma
    entry["example_sentence"] = {"be":"I want to be a teacher.","do":"I do my homework.",
                                 "good":"That is a good idea.","bad":"The weather is bad.",
                                 "man":"The man is a teacher.","woman":"The woman is a doctor.",
                                 "child":"The child is sleeping.","foot":"My left foot hurts."}[lemma]
    issues = module.validate(data)
    assert not any("grammatical form of " in x for x in issues), (lemma,issues)
for word, example in (("little","I have a little dog."),
                      ("less","Please add less sugar."),
                      ("least","This needs the least effort."),
                      ("person","One person is waiting."),
                      ("people","Many people are waiting.")):
    entry["word"] = word
    entry["example_sentence"] = example
    issues = module.validate(data)
    assert not any("grammatical form of " in x for x in issues), (word,issues)
entry["word"] = "apple"
entry["example_sentence"] = "I eat an apple."
print("PASS: ten be/do/comparison/irregular-plural forms rejected; base lemmas and distinct size/quantity and person/people senses remain eligible for human review.")
print("PASS: mismatched publisher headwords, generic CEFR references, copied cross-voice, multiword and unrelated single-word MP3s rejected; only documented homophones exempt; real listening still mandatory.")
