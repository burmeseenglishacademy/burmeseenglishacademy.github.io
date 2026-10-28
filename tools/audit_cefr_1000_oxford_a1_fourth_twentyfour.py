#!/usr/bin/env python3
"""Fail-closed provenance QA for 24 direct Oxford A1 word/POS research leads.

This is structural evidence-integrity checking ONLY. It cannot establish
independent exact-sense CEFR, English, Myanmar, audio or release approval.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-FOURTH-TWENTYFOUR-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = ("https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/"
       "oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf")
# Word, 1-based PDF page, 0-based extracted line, verbatim short source excerpt, risk ID.
EXPECTED = [
    ("a", 1, 4, "a, an indefinite article", "ARTICLE_A_VS_AN_SOUND_AND_UNSPECIFIED_REFERENT"),
    ("an", 1, 29, "an indefinite article", "VOWEL_SOUND_NOT_VOWEL_LETTER_DISTINCTION"),
    ("read", 3, 637, "read v.", "PRESENT_READ_VS_PAST_READ_PRONUNCIATION_FOR_AUDIO"),
    ("in", 2, 394, "in prep., adv.", "PREPOSITION_INSIDE_VS_ADVERB_AND_MYANMAR_LOCATION"),
    ("on", 3, 548, "on prep., adv.", "SURFACE_CONTACT_PREPOSITION_VS_ADVERB"),
    ("have", 2, 353, "have v.", "RELATIONSHIP_HAVE_TWO_SISTERS_NOT_LITERAL_OWNERSHIP"),
    ("not", 2, 531, "not adv.", "NEGATION_AND_MYANMAR_PARTICLE_DEPENDS_ON_CLAUSE"),
    ("but", 1, 117, "but conj.", "CONTRAST_JOINING_EXAMPLE_REGISTER"),
    ("or", 3, 557, "or conj.", "CHOICE_VS_INCLUSIVE_ALTERNATIVE"),
    ("all", 1, 25, "all det., pron.", "A1_DETERMINER_VS_OXFORD_A2_ADVERB_HOMOGRAPH"),
    ("me", 2, 470, "me pron.", "OBJECT_PRONOUN_AND_MYANMAR_SPEAKER_GENDER"),
    ("one", 3, 550, "one number/det., pron.", "NUMERAL_VS_PRONOUN_AND_DETERMINER"),
    ("like", 2, 443, "like (find sb/sth pleasant) v.", "VERB_LIKE_VS_PREPOSITION_LIKE_DISTINCT_SENSE"),
    ("time", 3, 801, "time n.", "CLOCK_TIME_VS_DURATION_SENSE"),
    ("people", 3, 582, "people n.", "PLURAL_NOUN_LABEL_VS_OXFORD_NOUN_AND_MYANMAR_COLLOQUIALITY"),
    ("good", 2, 332, "good adj.", "QUALITY_VS_MORAL_GOOD_SENSE"),
    ("know", 2, 422, "know v.", "KNOW_FACT_VS_KNOW_PERSON_SENSE"),
    ("see", 3, 677, "see v.", "VISUAL_PERCEPTION_VS_MEET_UNDERSTAND_SENSE"),
    ("two", 4, 831, "two number", "NUMERAL_VS_QUANTIFIER_EXAMPLE"),
    ("want", 4, 857, "want v.", "WANT_OBJECT_VS_WANT_TO_INFINITIVE_PATTERN"),
    ("go", 2, 331, "go v.", "MOVEMENT_VS_IDIOMATIC_GO_SENSE"),
    ("need", 2, 512, "need v.", "REQUIRE_VS_NEED_TO_MODAL_PATTERN"),
    ("here", 2, 363, "here adv.", "DEICTIC_HERE_LOCATION_DEPENDS_ON_CONTEXT"),
    ("day", 1, 195, "day n.", "TWENTY_FOUR_HOURS_DEFINITION_VS_BUSY_DAY_DAYTIME_SENSE"),
]
LEVELS = ("A1", "A2", "B1", "B2", "C1")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def audit(packet, shortlist, actual_sha):
    require(actual_sha == SHORTLIST_SHA, "Shortlist blob changed; rebind evidence")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "Wrong scope")
    require(packet.get("status") == "A1_TWENTY_FOUR_DIRECT_OXFORD_WORD_POS_LEADS_EDITORIAL_HOLD", "Status drift")
    require(packet.get("observed_on") == "2026-10-29", "Observation date drift")
    require(packet.get("shortlist_blob_sha") == actual_sha, "Wrong shortlist binding")
    require(type(packet.get("record_count")) is int and packet["record_count"] == 24, "Count drift")
    require(packet.get("counts_by_level") == {"A1": 24, "A2": 0, "B1": 0, "B2": 0, "C1": 0}, "Level drift")
    require(packet.get("independently_approved_count") == 0, "Fabricated approval count")
    require("NOT exact-sense CEFR" in packet.get("source_limitations", ""), "Missing source scope caveat")
    require(isinstance(packet.get("editorial_priority"), list) and len(packet["editorial_priority"]) >= 6,
            "Editorial risk summary missing")
    records = packet.get("records")
    require(isinstance(records, list) and len(records) == len(EXPECTED), "Wrong record count")
    entries = {x["word"]: x for x in shortlist.get("entries", []) if x.get("level") == "A1"}
    require(len(entries) == 200, "A1 shortlist quota changed")
    require(len({x["word"] for x in records}) == 24, "Repeated headword")
    for i, (word, page, line, excerpt, risk) in enumerate(EXPECTED):
        row = records[i]
        require(row.get("word") == word and row.get("level") == "A1", f"{word}: identity/level")
        require(word in entries, f"{word}: absent from shortlist")
        source = entries[word]
        require(row.get("part_of_speech") == source.get("part_of_speech"), f"{word}: POS drift")
        require(row.get("shortlist_snapshot") == {
            "english_definition": source.get("english_definition"),
            "myanmar_meaning": source.get("burmese_meaning"),
            "example_sentence": source.get("example_sentence")}, f"{word}: bilingual/example drift")
        require(row.get("shortlist_provenance") == {
            "source_path": source.get("source_path"),
            "source_index": source.get("source_index"),
            "source_blob_sha": source.get("source_blob_sha")}, f"{word}: Git source provenance drift")
        require(row.get("publisher_source") == {
            "publisher": "Oxford University Press",
            "title": "The Oxford 3000 by CEFR level",
            "url": URL, "observed_on": "2026-10-29",
            "pdf_page": page, "extracted_line": line,
            "source_excerpt": excerpt, "source_cefr_level": "A1",
            "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"}, f"{word}: source provenance or CEFR scope drift")
        require(row.get("editorial_risk") == risk, f"{word}: risk suppressed")
        task = row.get("independent_reviewer_task")
        require(isinstance(task, str) and word in task and risk in task
                and "Human-independent" in task and len(task) >= 150, f"{word}: task missing")
        require(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None, f"{word}: false approval")
    return len(records)


def self_test(packet, shortlist, sha):
    count = 0
    for i in range(len(EXPECTED)):
        bad = copy.deepcopy(packet)
        bad["records"][i]["publisher_source"]["source_excerpt"] = "fabricated source text"
        try:
            audit(bad, shortlist, sha)
        except ValueError:
            count += 1
        else:
            raise AssertionError(f"Forgery mutation {i} passed")
    mutations = [
        lambda p: p.update(record_count=25),
        lambda p: p.update(independently_approved_count=24),
        lambda p: p.update(shortlist_blob_sha="0" * 40),
        lambda p: p["records"][0].update(independently_reviewed=True),
        lambda p: p["records"][0].update(release_approved=True),
        lambda p: p["records"][0].update(independent_reviewer_receipt={"reviewer": "bot"}),
        lambda p: p["records"][1]["shortlist_snapshot"].update(myanmar_meaning="အတည်ပြုပြီး"),
        lambda p: p["records"][2]["shortlist_snapshot"].update(example_sentence="Altered example."),
        lambda p: p["records"][3]["shortlist_provenance"].update(source_index=999),
        lambda p: p["records"][4]["publisher_source"].update(url="https://example.org/oxford.pdf"),
        lambda p: p["records"][5]["publisher_source"].update(evidence_scope="EXACT_SENSE"),
        lambda p: p["records"][6]["publisher_source"].update(source_cefr_level="C1"),
        lambda p: p["records"][7].update(editorial_risk=""),
        lambda p: p["records"][8].update(independent_reviewer_task="approved"),
        lambda p: p["records"][9]["publisher_source"].update(observed_on="2026-10-30"),
        lambda p: p["records"][10].update(level="B1"),
        lambda p: p["records"][11].update(part_of_speech="noun"),
        lambda p: p["records"][12]["publisher_source"].update(pdf_page=999),
        lambda p: p["records"][13]["publisher_source"].update(extracted_line=-1),
        lambda p: p["records"][14].update(editorial_hold=False),
        lambda p: p["records"][15]["shortlist_snapshot"].update(english_definition="Invented."),
        lambda p: p["records"].reverse(),
    ]
    for i, mutation in enumerate(mutations):
        bad = copy.deepcopy(packet)
        mutation(bad)
        try:
            audit(bad, shortlist, sha)
        except ValueError:
            count += 1
        else:
            raise AssertionError(f"General mutation {i} passed")
    return count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    sha = blob_sha(SHORTLIST)
    n = audit(packet, shortlist, sha)
    print(f"PASS Oxford A1 fourth batch: {n} dated publisher word/POS leads; "
          f"level={args.level}; 0 independent approvals; NO release")
    if args.self_test:
        m = self_test(packet, shortlist, sha)
        print(f"PASS {m}/{m} negative source, content and false-approval mutations rejected")


if __name__ == "__main__":
    main()
