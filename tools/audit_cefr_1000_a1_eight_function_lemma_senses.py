#!/usr/bin/env python3
"""Fail-closed staging-only audit of eight held A1 grammatical/CEFR research cards.

Search-index observations are NOT direct publisher verification or human review.
This tool does not generate audio, approve entries, or deploy anything.
"""
import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A1-EDITORIAL-STARTER.json"
PACKET = ROOT / "draft/CEFR-1000-A1-EIGHT-THANK-BE-DO-I-WAKE-LEMMA-SENSE-2026-11-02.json"
FROZEN_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_SHA = "ff1e93f60828ef2f94c9146522ce94075183b0ae"
PACKET_SHA = "dc2e4ff1f83758e77fe704684781f743eccf7c15"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("thank", "is", "are", "do", "does", "did", "i", "wake")
EXPECTED = {
    "thank": ("LEVEL_CONFLICT", "A2", "/dictionary/english/thank"),
    "is": ("INFLECTED_FORM_LEMMA_COLLISION", "A1_FOR_BE_SENSE_NOT_INDEPENDENT_IS_LEMMA", "/grammar/british-grammar/be-"),
    "are": ("INFLECTED_FORM_LEMMA_COLLISION", "A1_FOR_BE_SENSE_NOT_INDEPENDENT_ARE_LEMMA", "/grammar/british-grammar/be-"),
    "do": ("A1_SENSE_ALIGNMENT_LEAD", "A1", "/dictionary/learner-english/do"),
    "does": ("INFLECTED_FORM_LEMMA_COLLISION", "A1_FOR_DO_AUXILIARY_NOT_INDEPENDENT_DOES_LEMMA", "/grammar/british-grammar/do"),
    "did": ("INFLECTED_FORM_LEMMA_COLLISION", "A1_FOR_DO_AUXILIARY_NOT_INDEPENDENT_DID_LEMMA", "/grammar/british-grammar/do"),
    "i": ("A1_ALIGNMENT_WITH_CASE_RISK", "A1", "/dictionary/essential-british-english/i"),
    "wake": ("A1_SENSE_ALIGNMENT_LEAD", "A1", "/dictionary/essential-british-english/wake"),
}
FALSE_FLAGS = ("independently_reviewed", "release_approved",
               "headword_george_listened", "headword_emma_listened",
               "example_george_listened", "example_emma_listened",
               "physical_iphone_safari_tested")
ROW_KEYS = {"word", "level", "part_of_speech", "shortlist_snapshot",
            "shortlist_provenance", "publisher_observation", "triage_status",
            "unapproved_teaching_alternative", "independent_reviewer_task",
            "editorial_hold", *FALSE_FLAGS}
PUB_KEYS = {"publisher", "source_url", "related_source_url", "observed_on",
            "access", "evidence_scope", "indexed_cefr_or_qualification",
            "indexed_part_of_speech_and_sense", "observation_paraphrase",
            "exact_sense_independently_verified"}
ALTERNATIVE_KEYS = {"english_definition", "burmese_meaning", "example_sentence"}

def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load():
    raw = SHORTLIST.read_bytes()
    original = SOURCE.read_bytes()
    packet_raw = PACKET.read_bytes()
    if blob_sha(raw) != FROZEN_SHA:
        raise ValueError("Frozen shortlist SHA mismatch")
    if blob_sha(original) != SOURCE_SHA:
        raise ValueError("Frozen A1 source SHA mismatch")
    if blob_sha(packet_raw) != PACKET_SHA:
        raise ValueError("Research packet changed without reviewed auditor re-pin")
    return json.loads(packet_raw), json.loads(raw), json.loads(original)

def validate(packet, shortlist, original, level="ALL"):
    errors = []
    def require(condition, reason):
        if not condition:
            errors.append(reason)

    require(level in (*LEVELS, "ALL"), "invalid CEFR lane")
    require(packet.get("schema") == 1, "schema")
    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY", "scope")
    require(packet.get("created_on") == "2026-11-02", "observation date")
    require(packet.get("status") == "A1_EIGHT_FUNCTION_WORD_LEMMA_AND_SENSE_TRIAGE_HUMAN_REVIEW_REQUIRED", "status")
    require(packet.get("frozen_shortlist_blob_sha") == FROZEN_SHA, "source binding")
    caveat = packet.get("source_access_limitations", "")
    require(isinstance(caveat, str) and all(s in caveat for s in
            ("search-index", "HTTP 403", "not direct", "not independent")), "source access limitation")
    require(packet.get("count") == 8 and packet.get("level") == "A1", "eight A1 records")
    require(packet.get("production_deployed") is False, "no production deployment")
    for k in ("headword_audio_listening_signoffs", "example_audio_listening_signoffs",
              "physical_iphone_safari_signoffs"):
        require(type(packet.get(k)) is int and packet[k] == 0, "no fabricated signoffs: " + k)
    counts = dict.fromkeys(LEVELS, 200)
    require(packet.get("first_pass_written_by_level") == counts, "first-pass totals")
    require(packet.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "approval totals")
    entries = shortlist.get("entries", [])
    require(len(entries) == 1000, "exactly 1000 entries")
    require(Counter(e.get("level") for e in entries) == Counter(counts), "200 per level")
    require(shortlist.get("counts_by_level") == counts, "frozen declared level counts")
    require(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "frozen approvals")
    require(len({e.get("word", "").casefold() for e in entries}) == 1000, "unique casefold headwords")
    for e in entries:
        require(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                ("reviewed_english", "reviewed_burmese", "reviewed_example",
                 "reviewed_level", "reviewed_pronunciation")),
                "frozen editorial hold: " + str(e.get("word")))
    index = {e["word"]: e for e in entries}
    source_entries = original.get("entries", [])
    rows = packet.get("records")
    if not isinstance(rows, list):
        return errors + ["records must be list"]
    require(len(rows) == 8, "exactly eight cards")
    seen = set()
    for pos, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append("non-object row")
            continue
        word = row.get("word")
        require(set(row) == ROW_KEYS, "row keys at " + str(pos))
        require(word in WORDS and word not in seen, "unexpected or duplicate word: " + str(word))
        seen.add(word)
        if word not in EXPECTED or word not in index:
            continue
        frozen = index[word]
        expected_status, expected_cefr, expected_path = EXPECTED[word]
        require(row.get("level") == "A1" == frozen["level"], word + " level")
        require(row.get("part_of_speech") == frozen["part_of_speech"], word + " POS")
        snapshot = {k: frozen[k] for k in ALTERNATIVE_KEYS}
        require(row.get("shortlist_snapshot") == snapshot, word + " frozen bilingual/example")
        provenance = {k: frozen[k] for k in ("source_path", "source_index", "source_blob_sha")}
        require(row.get("shortlist_provenance") == provenance, word + " provenance")
        idx = frozen["source_index"]
        require(frozen["source_path"] == "draft/A1-EDITORIAL-STARTER.json"
                and frozen["source_blob_sha"] == SOURCE_SHA, word + " source path/hash")
        require(type(idx) is int and 0 <= idx < len(source_entries)
                and all(source_entries[idx].get(k) == frozen[k] for k in
                        ("word", "level", "part_of_speech", "english_definition",
                         "burmese_meaning", "example_sentence")), word + " source row")
        require(row.get("triage_status") == expected_status, word + " triage")
        pub = row.get("publisher_observation")
        if not isinstance(pub, dict):
            errors.append(word + " missing publisher observation")
            continue
        require(set(pub) == PUB_KEYS, word + " publisher schema")
        require(pub.get("publisher") == "Cambridge Dictionary / Cambridge English Grammar Today",
                word + " publisher")
        url = pub.get("source_url", "")
        related = pub.get("related_source_url", "")
        require(isinstance(url, str) and urlparse(url).scheme == "https"
                and urlparse(url).netloc == "dictionary.cambridge.org"
                and urlparse(url).path == expected_path, word + " exact source URL")
        require(isinstance(related, str) and urlparse(related).scheme == "https"
                and urlparse(related).netloc == "dictionary.cambridge.org", word + " related URL")
        require(pub.get("observed_on") == "2026-11-02", word + " date")
        require(pub.get("access") == "PUBLISHER_SEARCH_INDEX_VISIBLE_DIRECT_OPEN_403",
                word + " publisher access honesty")
        require(pub.get("evidence_scope") == "INDEXED_OR_GRAMMAR_RESEARCH_LEAD_NOT_DIRECT_OR_INDEPENDENT",
                word + " source scope")
        require(pub.get("indexed_cefr_or_qualification") == expected_cefr, word + " CEFR scope")
        require(isinstance(pub.get("indexed_part_of_speech_and_sense"), str)
                and len(pub["indexed_part_of_speech_and_sense"]) >= 18, word + " exact sense")
        note = pub.get("observation_paraphrase")
        require(isinstance(note, str) and len(note) >= 90, word + " note specificity")
        require(pub.get("exact_sense_independently_verified") is False,
                word + " forged independent verification")
        alt = row.get("unapproved_teaching_alternative")
        require(isinstance(alt, dict) and set(alt) == ALTERNATIVE_KEYS,
                word + " alternative schema")
        if isinstance(alt, dict):
            for k in ALTERNATIVE_KEYS:
                value = alt.get(k)
                require(isinstance(value, str) and len(value.strip()) >= 10,
                        word + " alternative " + k)
            require(alt != snapshot, word + " copied frozen alternative")
            require(any("\u1000" <= ch <= "\u109f" for ch in alt.get("burmese_meaning", "")),
                    word + " Myanmar script missing")
        task = row.get("independent_reviewer_task")
        require(isinstance(task, str) and "Independently" in task
                and "Do not alter" in task, word + " independent reviewer task")
        require(row.get("editorial_hold") is True, word + " editorial hold")
        for flag in FALSE_FLAGS:
            require(row.get(flag) is False, word + " forged " + flag)
    require(seen == set(WORDS), "missing A1 cards")
    return errors

def self_test(packet, shortlist, original):
    cases = []
    def add(label, mutated, short=shortlist):
        cases.append((label, mutated, short))
    for i, word in enumerate(WORDS):
        for key, value in (
            ("level", "C1"), ("triage_status", "APPROVED"),
            ("part_of_speech", "noun"), ("editorial_hold", False),
            ("release_approved", True), ("independently_reviewed", True),
            ("headword_george_listened", True), ("headword_emma_listened", True),
            ("example_george_listened", True), ("example_emma_listened", True),
            ("physical_iphone_safari_tested", True)):
            m = copy.deepcopy(packet)
            m["records"][i][key] = value
            add(word + " " + key, m)
        for key, value in (
            ("source_url", "https://attacker.example/dictionary/english/" + word),
            ("access", "DIRECT_PUBLISHER_PAGE_VERIFIED"),
            ("evidence_scope", "INDEPENDENT_CEFR_APPROVED"),
            ("observed_on", "2020-01-01"),
            ("exact_sense_independently_verified", True),
            ("indexed_cefr_or_qualification", "C2"),
            ("observation_paraphrase", "A1")):
            m = copy.deepcopy(packet)
            m["records"][i]["publisher_observation"][key] = value
            add(word + " publisher " + key, m)
        for key in ALTERNATIVE_KEYS:
            m = copy.deepcopy(packet)
            m["records"][i]["shortlist_snapshot"][key] = "FORGED SOURCE"
            add(word + " snapshot " + key, m)
        m = copy.deepcopy(packet)
        m["records"][i]["shortlist_provenance"]["source_index"] = 0
        add(word + " provenance", m)
    for key, value in (("production_deployed", True),
                       ("headword_audio_listening_signoffs", 1),
                       ("example_audio_listening_signoffs", 1),
                       ("physical_iphone_safari_signoffs", 1),
                       ("count", 9), ("level", "C1")):
        m = copy.deepcopy(packet)
        m[key] = value
        add("packet " + key, m)
    m = copy.deepcopy(packet)
    m["records"].append(copy.deepcopy(m["records"][0]))
    add("duplicate card", m)
    m = copy.deepcopy(packet)
    m["records"][0].pop("independent_reviewer_task")
    add("missing reviewer task", m)
    m = copy.deepcopy(packet)
    m["independently_approved_by_level"]["A1"] = 1
    add("forged independent totals", m)
    m = copy.deepcopy(shortlist)
    m["entries"][0]["editorial_hold"] = False
    add("frozen hold tampering", packet, m)
    m = copy.deepcopy(shortlist)
    m["entries"][0]["word"] = m["entries"][1]["word"]
    add("frozen dedup tampering", packet, m)
    rejected = 0
    for label, altered_packet, altered_shortlist in cases:
        if validate(altered_packet, altered_shortlist, original):
            rejected += 1
        else:
            raise AssertionError("Mutation escaped fail-closed audit: " + label)
    print("PASS: " + str(rejected) + "/" + str(len(cases)) +
          " synthetic adversarial mutations rejected (mock-only; no independent approval)")
    return rejected

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet, shortlist, original = load()
    errors = validate(packet, shortlist, original, args.level)
    if errors:
        raise SystemExit("FAIL: " + "; ".join(errors[:25]))
    print("PASS: held A1 eight-card source/lemma/sense integrity, lane " + args.level +
          "; 200 first-pass each level; 0 independent approvals; no release")
    if args.self_test:
        self_test(packet, shortlist, original)

if __name__ == "__main__":
    main()
