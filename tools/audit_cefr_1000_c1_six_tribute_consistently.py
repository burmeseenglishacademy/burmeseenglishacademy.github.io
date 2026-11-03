#!/usr/bin/env python3
"""Fail-closed staging audit: six Cambridge exact-sense C1 editorial holds.
Publisher CEFR badges are research evidence, NOT independent human approval.
No production write, merge, deploy, reviewer signoff, or audio/device claim.
"""
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-C1-SIX-TRIBUTE-CONSISTENTLY-CAMBRIDGE-SENSE-2026-11-03.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
HISTORICAL = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
EXPECTED_BLOBS = {
    PACKET: "1a4b91e0239045309119e74dea478f1951f9ccb9",
    SHORTLIST: "475e68ae17ab97bd937e73e5ce4794e0dcd76551",
    HISTORICAL: "b04dd85db5cfae131c25aa4c73109778991b6fdc",
}
LEVELS = ("A1", "A2", "B1", "B2", "C1")
QUOTAS = {x: 200 for x in LEVELS}
EXPECTED = {
    "tribute": ("C2", "CONFLICT_C1_VS_C2", 31, "english/tribute"),
    "trigger": ("C1", "SENSE_MATCH_C1_LEAD", 32, "english/trigger"),
    "racism": ("B2", "CONFLICT_C1_VS_B2", 71, "english/racism"),
    "signature": ("B1", "CONFLICT_C1_VS_B1", 75, "english/signature"),
    "abortion": ("C1", "SENSE_MATCH_C1_LEAD", 78, "english/abortion"),
    "consistently": ("C2", "CONFLICT_C1_VS_C2", 110, "english/consistently"),
}
FROZEN = ("english_definition", "burmese_meaning", "example_sentence",
          "part_of_speech", "source_path", "source_index", "source_blob_sha")
SOURCE_FIELDS = ("word", "level", "part_of_speech", "english_definition",
                 "burmese_meaning", "example_sentence")
REVIEW_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                "reviewed_level", "reviewed_pronunciation", "release_approved")
CARD_FALSE = ("independent_english_review", "independent_myanmar_review",
              "independent_example_review", "independent_cefr_review",
              "real_george_emma_audio_listening_signed_off",
              "physical_iphone_safari_signed_off", "release_approved")

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def audit(packet, shortlist, historical):
    errors = []
    def check(ok, description):
        if not ok:
            errors.append(description)
    check(packet.get("project") == "Burmese English Academy CEFR 1000 (not superseded 5000)", "1000 scope")
    check(packet.get("branch") == "cefr-5000-bilingual-qa-staging", "branch")
    check(packet.get("source_shortlist_blob_sha") == EXPECTED_BLOBS[SHORTLIST], "shortlist binding")
    check(packet.get("observation_date") == "2026-11-03", "observation date")
    check(packet.get("status") == "RESEARCH_ONLY_ALL_SIX_EDITORIAL_HOLD_NOT_INDEPENDENTLY_APPROVED", "hold status")
    check(packet.get("scope_counts") == QUOTAS, "packet quotas")
    check(packet.get("independently_approved") == dict.fromkeys(LEVELS, 0), "packet approvals")
    check("not human review" in packet.get("evidence_method", ""), "publisher not human")
    check(packet.get("risk_summary") == {"conflicts": 4, "aligned_leads": 2, "unverified_signoffs": 6}, "risk summary")
    check(shortlist.get("release_status") == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH", "frozen hold")
    check(shortlist.get("counts_by_level") == QUOTAS, "frozen quotas")
    check(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "frozen approvals")
    rows = shortlist.get("entries", [])
    check(len(rows) == 1000, "1000 rows")
    check(dict(collections.Counter(x.get("level") for x in rows)) == QUOTAS, "200 per level")
    check(len({x.get("word", "").casefold() for x in rows}) == 1000, "unique written headwords")
    check(all(x.get("editorial_hold") is True and all(x.get(k) is False for k in REVIEW_FLAGS) for x in rows), "frozen reviewer flags")
    cards = packet.get("entries", [])
    check(len(cards) == 6 and {x.get("word") for x in cards} == set(EXPECTED), "six cards")
    originals = {x["word"]: x for x in rows}
    historical_rows = historical.get("entries", [])
    check(len(historical_rows) > 110, "historical source length")
    for card in cards:
        word = card.get("word")
        if word not in EXPECTED or word not in originals:
            continue
        indexed, alignment, index, suffix = EXPECTED[word]
        orig = originals[word]
        historic = historical_rows[index]
        check(card.get("level") == "C1" and orig.get("level") == "C1", word + " C1 slot")
        check(card.get("frozen_definition") == orig.get("english_definition"), word + " English frozen")
        check(card.get("frozen_myanmar") == orig.get("burmese_meaning"), word + " Myanmar frozen")
        check(card.get("frozen_example") == orig.get("example_sentence"), word + " example frozen")
        check(all(card.get(k) == orig.get(k) for k in
                  ("part_of_speech", "source_path", "source_index", "source_blob_sha")), word + " source binding")
        check(all(historic.get(k) == orig.get(k) for k in SOURCE_FIELDS), word + " historical source")
        check(orig.get("source_index") == index and orig.get("source_blob_sha") == EXPECTED_BLOBS[HISTORICAL], word + " provenance")
        check(card.get("publisher") == "Cambridge Dictionary / Cambridge Advanced Learner's Dictionary", word + " publisher")
        check(card.get("publisher_url", "").startswith("https://dictionary.cambridge.org/") and
              card.get("publisher_url", "").endswith(suffix), word + " publisher URL")
        check(card.get("observed_on") == "2026-11-03", word + " date")
        check(card.get("access_mode") == "web search engine publisher page text (indexed/crawled), not independent reviewer", word + " access honesty")
        check(card.get("publisher_cefr") == indexed and card.get("alignment") == alignment, word + " exact sense level")
        check(bool(card.get("publisher_sense")) and bool(card.get("evidence_interpretation")) and
              bool(card.get("british_ipa_reference")), word + " sense and IPA")
        check(all(isinstance(card.get(k), str) and card[k].strip() for k in
                  ("unapproved_myanmar_candidate", "unapproved_original_example_candidate", "independent_reviewer_task")), word + " candidate handoff")
        check(all(card.get(k) is False for k in CARD_FALSE), word + " forged approval/audio/device")
    return errors

def main():
    for path, expected in EXPECTED_BLOBS.items():
        assert git_blob(path) == expected, "Frozen Git blob mismatch: " + str(path)
    packet, shortlist, historical = map(read, (PACKET, SHORTLIST, HISTORICAL))
    failures = audit(packet, shortlist, historical)
    assert not failures, "; ".join(failures)
    mutations = 0
    for i in range(len(packet["entries"])):
        for key in CARD_FALSE:
            forged = copy.deepcopy(packet)
            forged["entries"][i][key] = True
            assert audit(forged, shortlist, historical), "forged flag accepted " + key
            mutations += 1
        for key, value in (("publisher_cefr", "A1"), ("alignment", "INDEPENDENT_APPROVAL"),
                           ("observed_on", "2020-01-01"), ("publisher_url", "https://untrusted.example"),
                           ("access_mode", "INDEPENDENT_VERIFIED"), ("frozen_myanmar", "spoofed")):
            forged = copy.deepcopy(packet)
            forged["entries"][i][key] = value
            assert audit(forged, shortlist, historical), "forged source accepted " + key
            mutations += 1
    for level in LEVELS:
        forged = copy.deepcopy(packet)
        forged["independently_approved"][level] = 1
        assert audit(forged, shortlist, historical), "forged level approval accepted"
        mutations += 1
    print(f"PASS: six C1 research cards source-bound; {mutations}/{mutations} adversarial forgeries rejected; 200 each A1-C1; 0 independently approved; NO DEPLOY")

if __name__ == "__main__":
    main()
