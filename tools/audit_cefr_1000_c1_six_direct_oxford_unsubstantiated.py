#!/usr/bin/env python3
"""Fail-closed staging-only integrity check for six directly opened Oxford C1 leads.
Oxford dictionary definitions do not themselves establish exact-sense CEFR C1.
No self-test or successful CI job is an independent linguistic/audio signoff.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-C1-SIX-DIRECT-OXFORD-RARE-SENSE-AND-CEFR-UNSUBSTANTIATED-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json"
PACKET_SHA = "6a3d6fed0a03c228dec417ac96d83638ed25e039"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_SHA = "7eaf88b9ed7687b26ccde713262f10fb209743a8"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")
EXPECTED = {
    "coercion": (16, "noun", 88, 112, "/kəʊˈɜːʃn/", "PRESSURE_VS_THREATENED_FORCE_SCOPE"),
    "conundrum": (18, "noun", 88, 109, "/kəˈnʌndrəm/", "DIFFICULT_PROBLEM_VS_WORD_RIDDLE"),
    "corroborate": (19, "verb", 88, 119, "/kəˈrɒbəreɪt/", "SUPPORTING_EVIDENCE_NOT_CONCLUSIVE_PROOF"),
    "credence": (20, "noun", 88, 110, "/ˈkriːdns/", "LEND_CREDENCE_CREDIBILITY_VS_GIVE_CREDENCE_BELIEF"),
    "deference": (21, "noun", 88, 125, "/ˈdefərəns/", "RESPECT_SHOWN_NOT_NECESSARILY_ACCEPTING_JUDGEMENT"),
    "delineate": (22, "verb", 88, 114, "/dɪˈlɪnieɪt/", "DETAILED_DESCRIPTION_VS_LITERAL_BOUNDARY_MARKING"),
}
REVIEW_NEEDED = [
    "independent English exact-sense and grammar",
    "fluent Myanmar semantic equivalence",
    "original example naturalness and sense",
    "publisher-backed exact-sense CEFR level, not topic footer",
    "British George/Emma headword and example generation with actual listening",
]

def sha(path):
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def require(ok, message):
    if not ok:
        raise ValueError(message)

def held(record, label):
    require(record.get("editorial_hold") is True, label + " editorial hold")
    require(record.get("independently_approved", False) is False, label + " forged independent approval")
    for flag in FLAGS:
        require(record.get(flag, False) is False, label + " forged " + flag)

def validate(packet, shortlist, source):
    quotas = {level: 200 for level in LEVELS}
    zeros = {level: 0 for level in LEVELS}
    require(packet.get("schema") == 1 and packet.get("created_on") == "2026-11-02", "packet schema/date")
    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_NOT_5000", "scope")
    require(packet.get("branch") == "cefr-5000-bilingual-qa-staging", "branch")
    require(packet.get("release_status") == "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH", "release status")
    require(packet.get("shortlist_path") == "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json", "shortlist path")
    require(packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "shortlist provenance")
    require(packet.get("source_path") == "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json", "historical path")
    require(packet.get("source_blob_sha") == SOURCE_SHA, "historical provenance")
    require(packet.get("counts_by_level") == quotas and packet.get("independently_approved_by_level") == zeros, "packet quota and approvals")
    require(packet.get("research_record_count") == 6, "record count")
    require(packet.get("independent_human_review_receipts") == [], "forged human receipts")
    require(packet.get("real_audio_listening_receipts") == [], "forged listening receipts")
    require(packet.get("release_approved") is False, "forged release approval")
    limits = packet.get("source_limitations", "")
    for phrase in ("Oxford", "topic footer", "exact-sense C1", "HTTP 403", "unapproved", "No audio", "physical iPhone", "production deployment"):
        require(phrase in limits, "source-access or release caveat missing: " + phrase)

    require(shortlist.get("counts_by_level") == quotas and shortlist.get("independently_approved_by_level") == zeros, "shortlist quotas")
    entries = shortlist.get("entries", [])
    require(len(entries) == 1000, "shortlist not 1000")
    require(dict(collections.Counter(x.get("level") for x in entries)) == quotas, "200 per level")
    require(len({x.get("word", "").casefold() for x in entries}) == 1000, "duplicate headwords")
    require(all(x.get("editorial_hold") is True and all(x.get(f) is False for f in FLAGS) for x in entries), "shortlist has unapproved edits or forged flags")
    byword = {x["word"]: x for x in entries}

    records = packet.get("records", [])
    require(isinstance(records, list) and len(records) == 6, "six records")
    require([r.get("word") for r in records] == list(EXPECTED), "missing, duplicate or reordered research words")
    source_entries = source.get("entries", [])
    require(len(source_entries) > 22, "historical source incomplete")
    for r in records:
        w = r["word"]
        index, pos, first, last, ipa, risk = EXPECTED[w]
        require(r.get("level") == "C1" and r.get("part_of_speech") == pos, w + " level/POS")
        require(r.get("source_index") == index and r.get("source_blob_sha") == SOURCE_SHA, w + " historical index/blob")
        require(r.get("status") == "RESEARCH_LEAD_NOT_HUMAN_REVIEWED", w + " false review status")
        held(r, w + " research")
        original = r.get("frozen_original")
        require(original == byword[w], w + " original card drift")
        held(original, w + " frozen")
        historical = source_entries[index]
        require(historical.get("word") == w and historical.get("proposed_level") == "C1", w + " historical word/level")
        for f in ("word", "part_of_speech", "english_definition", "burmese_meaning", "example_sentence"):
            require(historical.get(f) == original.get(f), w + " historical bilingual drift " + f)
        require(r.get("review_needed") == REVIEW_NEEDED, w + " review tasks")
        require(r.get("exact_sense_risk") == risk, w + " exact-sense risk")

        ox = r.get("oxford", {})
        require(ox.get("publisher") == "Oxford Advanced Learner's Dictionary", w + " Oxford publisher")
        require(ox.get("url") == "https://www.oxfordlearnersdictionaries.com/definition/english/" + w, w + " Oxford URL")
        require(urlparse(ox["url"]).hostname == "www.oxfordlearnersdictionaries.com", w + " Oxford domain")
        require(ox.get("observed_on") == "2026-11-02" and ox.get("access") == "DIRECT_HEADWORD_ENTRY", w + " Oxford access")
        require(ox.get("line_start") == first and ox.get("line_end") == last, w + " Oxford line locator")
        require(ox.get("british_ipa") == ipa, w + " British IPA source")
        require(isinstance(ox.get("source_sense_summary"), str) and len(ox["source_sense_summary"]) > 80, w + " source sense missing")
        require(ox.get("exact_sense_cefr_badge") is None, w + " invented Oxford CEFR badge")
        require(ox.get("topic_footer_not_headword_cefr") is True, w + " footer misattribution")

        cam = r.get("cambridge", {})
        require(cam.get("url") == "https://dictionary.cambridge.org/dictionary/english/" + w, w + " Cambridge URL")
        require(cam.get("observed_on") == "2026-11-02", w + " Cambridge date")
        require(cam.get("access") == "DIRECT_HTTP_403_NO_CEFR_LEVEL_CLAIM", w + " forged Cambridge access")
        require(cam.get("indexed_cefr") is None, w + " invented Cambridge CEFR label")

        alt = r.get("unapproved_teaching_alternative", {})
        for field in ("english_definition", "burmese_meaning", "example_sentence"):
            require(isinstance(alt.get(field), str) and len(alt[field].strip()) >= 16, w + " missing alternative " + field)
        require(w in alt["example_sentence"].casefold(), w + " example omits target")
    return True

def expect_reject(packet, shortlist, source):
    try:
        validate(packet, shortlist, source)
    except (ValueError, KeyError, IndexError, TypeError, AttributeError):
        return
    raise AssertionError("FAIL-OPEN: forged evidence accepted")

def self_test(packet, shortlist, source):
    tested = 0
    def reject_variant(p, s=shortlist, src=source):
        nonlocal tested
        expect_reject(p, s, src)
        tested += 1

    for i, r in enumerate(packet["records"]):
        for field, value in (
            ("level", "B2"), ("part_of_speech", "adverb"),
            ("source_index", -1), ("source_blob_sha", "forged"),
            ("frozen_original", {}), ("status", "APPROVED"),
            ("editorial_hold", False), ("independently_approved", True),
            ("release_approved", True), ("review_needed", []),
            ("exact_sense_risk", "NO_RISK"),
        ):
            p = copy.deepcopy(packet)
            p["records"][i][field] = value
            reject_variant(p)
        for flag in FLAGS:
            p = copy.deepcopy(packet)
            p["records"][i][flag] = True
            reject_variant(p)
        for field, value in (
            ("publisher", "Unverified website"),
            ("url", "https://evil.example/forged"),
            ("observed_on", "2025-01-01"),
            ("access", "SEARCH_INDEX_ONLY"),
            ("line_start", 0), ("line_end", 0),
            ("british_ipa", "/fake/"),
            ("source_sense_summary", ""),
            ("exact_sense_cefr_badge", "C1"),
            ("topic_footer_not_headword_cefr", False),
        ):
            p = copy.deepcopy(packet)
            p["records"][i]["oxford"][field] = value
            reject_variant(p)
        for field, value in (
            ("url", "https://evil.example/forged"),
            ("observed_on", "2025-01-01"),
            ("access", "DIRECT_PUBLISHER_VERIFIED"),
            ("indexed_cefr", "C1"),
        ):
            p = copy.deepcopy(packet)
            p["records"][i]["cambridge"][field] = value
            reject_variant(p)
        for field in ("english_definition", "burmese_meaning", "example_sentence"):
            p = copy.deepcopy(packet)
            p["records"][i]["unapproved_teaching_alternative"][field] = ""
            reject_variant(p)

    for field, value in (
        ("scope", "CEFR_5000"), ("branch", "main"),
        ("release_status", "LIVE"), ("shortlist_blob_sha", "fake"),
        ("source_blob_sha", "fake"), ("source_limitations", ""),
        ("research_record_count", 5),
        ("independent_human_review_receipts", [{"fake": True}]),
        ("real_audio_listening_receipts", [{"fake": True}]),
        ("release_approved", True),
        ("independently_approved_by_level", {x: 200 for x in LEVELS}),
    ):
        p = copy.deepcopy(packet)
        p[field] = value
        reject_variant(p)
    p = copy.deepcopy(packet)
    p["records"][1] = copy.deepcopy(p["records"][0])
    reject_variant(p)
    s = copy.deepcopy(shortlist)
    s["entries"][0]["release_approved"] = True
    reject_variant(packet, s)
    s = copy.deepcopy(shortlist)
    s["entries"][0]["word"] = s["entries"][1]["word"]
    reject_variant(packet, s)
    src = copy.deepcopy(source)
    src["entries"][16]["burmese_meaning"] = "forged"
    reject_variant(packet, shortlist, src)
    print(f"PASS: {tested}/{tested} synthetic negative mutations rejected; ZERO independent approvals implied")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    require(sha(PACKET) == PACKET_SHA, "research packet Git blob integrity")
    require(sha(SHORTLIST) == SHORTLIST_SHA, "frozen shortlist Git blob integrity")
    require(sha(SOURCE) == SOURCE_SHA, "historical source Git blob integrity")
    packet, shortlist, source = load(PACKET), load(SHORTLIST), load(SOURCE)
    validate(packet, shortlist, source)
    print(f"PASS: six held C1 direct Oxford exact-sense leads, {args.level}; zero Oxford/Cambridge exact-sense CEFR badges claimed")
    if args.self_test:
        self_test(packet, shortlist, source)

if __name__ == "__main__":
    main()
