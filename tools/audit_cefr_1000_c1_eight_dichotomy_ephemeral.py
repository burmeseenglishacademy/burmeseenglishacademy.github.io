#!/usr/bin/env python3
"""Fail-closed integrity audit for eight UNAPPROVED C1 Oxford research cards.
Mechanical checks never constitute independent linguistic/CEFR or audio approval.
"""
import argparse
import copy
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-C1-EIGHT-DIRECT-OXFORD-DICHOTOMY-EPHEMERAL-SENSE-TRIAGE-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "54935a003fec14108490a91f17253c5018a88714"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("dichotomy", "disseminate", "eclectic", "efficacy",
         "embellish", "endemic", "enigma", "ephemeral")
LOCATORS = ("101-107", "101-116", "101-113", "93-109",
            "101-117", "101-112", "101-109", "101-108")
IPAS = ("/daɪˈkɒtəmi/", "/dɪˈsemɪneɪt/", "/ɪˈklektɪk/",
        "/ˈefɪkəsi/", "/ɪmˈbelɪʃ/", "/enˈdemɪk/",
        "/ɪˈnɪɡmə/", "/ɪˈfemərəl/")
URL_PREFIX = "https://www.oxfordlearnersdictionaries.com/definition/english/"
FALSE_FLAGS = ("independent_english_review", "independent_myanmar_review",
               "independent_example_review", "independent_exact_sense_cefr_review",
               "independent_pronunciation_review", "independent_approval",
               "george_emma_listened")
ORIGINAL = ("english_definition", "burmese_meaning", "example_sentence",
            "source_path", "source_index", "source_blob_sha")
EXPECTED_NOTE = ("Eight Oxford English dictionary entries directly opened; no exact-sense C1 CEFR badge observed. "
                 "Cambridge direct access HTTP 403; no Cambridge CEFR assertion. "
                 "Research alternatives are self-drafted, not human-independent signoffs.")

def git_sha(path):
    return subprocess.run(["git", "hash-object", str(path)], cwd=ROOT,
                          check=True, capture_output=True, text=True).stdout.strip()

def validate(packet, shortlist):
    errors = []
    if not isinstance(packet, dict) or not isinstance(shortlist, dict):
        return ["JSON root must be an object"]
    root_expected = {
        "schema": 1, "scope": "USER_APPROVED_CEFR_1000_STAGING_ONLY",
        "status": "RESEARCH_ONLY_NO_INDEPENDENT_APPROVAL",
        "observed_on": "2026-11-02",
        "shortlist_path": "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json",
        "shortlist_blob_sha": SHORTLIST_SHA,
        "counts_by_level": dict.fromkeys(LEVELS, 200),
        "independently_approved_by_level": dict.fromkeys(LEVELS, 0),
        "source_access_note": EXPECTED_NOTE,
        "reviewer_signoffs": 0, "real_audio_listening_signoffs": 0,
        "physical_iphone_safari_signoffs": 0, "production_deployed": False,
    }
    for k, v in root_expected.items():
        if packet.get(k) != v: errors.append("packet root: " + k)
    for k in ("counts_by_level", "scope_target"):
        if k in shortlist and shortlist[k] != dict.fromkeys(LEVELS, 200):
            errors.append("shortlist quota: " + k)
    if shortlist.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
        errors.append("shortlist independent approvals must remain zero")
    frozen = shortlist.get("entries")
    rows = packet.get("entries")
    if not isinstance(frozen, list) or len(frozen) != 1000:
        return errors + ["shortlist must have exactly 1000 entries"]
    if not isinstance(rows, list) or len(rows) != 8:
        return errors + ["research must have exactly eight entries"]
    counts = {level: 0 for level in LEVELS}
    unique = set()
    for entry in frozen:
        if not isinstance(entry, dict):
            errors.append("shortlist non-object entry"); continue
        level, word = entry.get("level"), entry.get("word")
        if level not in counts or not isinstance(word, str):
            errors.append("shortlist invalid identity"); continue
        counts[level] += 1
        normalized = word.strip().casefold()
        if normalized in unique: errors.append("shortlist duplicate headword " + normalized)
        unique.add(normalized)
        if entry.get("editorial_hold") is not True or entry.get("release_approved") is not False:
            errors.append("shortlist release hold bypass " + word)
        for key in ("reviewed_english", "reviewed_burmese", "reviewed_example",
                    "reviewed_level", "reviewed_pronunciation"):
            if entry.get(key) is not False: errors.append("shortlist forged review " + word + ":" + key)
    if counts != dict.fromkeys(LEVELS, 200):
        errors.append("shortlist level counts incorrect")
    lookup = {entry.get("word"): entry for entry in frozen if isinstance(entry, dict)}
    for i, word in enumerate(WORDS):
        row = rows[i]
        if not isinstance(row, dict):
            errors.append("non-object research row"); continue
        frozen_entry = lookup.get(word)
        if frozen_entry is None or frozen_entry.get("level") != "C1":
            errors.append("missing frozen C1 " + word); continue
        if row.get("word") != word or row.get("level") != "C1":
            errors.append("research identity " + word)
        if row.get("part_of_speech") != frozen_entry.get("part_of_speech"):
            errors.append("research POS " + word)
        original = row.get("original")
        if not isinstance(original, dict):
            errors.append("missing original " + word)
        else:
            for field in ORIGINAL:
                if original.get(field) != frozen_entry.get(field):
                    errors.append("frozen original mismatch " + word + ":" + field)
        if row.get("editorial_hold") is not True:
            errors.append("research hold bypass " + word)
        for field in FALSE_FLAGS:
            if row.get(field) is not False:
                errors.append("forged human/audio approval " + word + ":" + field)
        evidence = row.get("publisher_evidence")
        if not isinstance(evidence, dict):
            errors.append("missing publisher evidence " + word); continue
        expected = {
            "publisher": "Oxford Advanced Learner's Dictionary",
            "access": "DIRECT_PAGE_OPENED",
            "url": URL_PREFIX + word,
            "observed_on": "2026-11-02",
            "line_locator": LOCATORS[i],
            "uk_ipa": IPAS[i],
            "exact_sense_cefr_badge_observed": False,
            "cefr_level_supported_by_this_page": "NOT_ESTABLISHED",
            "note": "Oxford headword definition, POS and pronunciation inspected; footer topic/Word-of-the-Day labels are not exact-sense CEFR evidence.",
        }
        if evidence != expected:
            errors.append("publisher URL, access, line, IPA or false CEFR " + word)
        if not isinstance(row.get("editorial_risk"), str) or len(row["editorial_risk"]) < 8:
            errors.append("missing risk " + word)
        if not isinstance(row.get("editorial_finding"), str) or len(row["editorial_finding"]) < 35:
            errors.append("missing substantive finding " + word)
        proposed = row.get("unapproved_teaching_alternative")
        if not isinstance(proposed, dict):
            errors.append("missing unapproved candidate " + word); continue
        for key in ("english_definition", "burmese_meaning", "example_sentence"):
            if not isinstance(proposed.get(key), str) or len(proposed[key].strip()) < 12:
                errors.append("missing proposed " + word + ":" + key)
        if not re.search(r"[\u1000-\u109f]", proposed.get("burmese_meaning", "")):
            errors.append("Myanmar script missing " + word)
        if not re.search(r"\b" + re.escape(word) + r"\b", proposed.get("example_sentence", ""), re.I):
            errors.append("example does not contain headword " + word)
    return errors

def adversarial_test(packet, shortlist):
    total = 0
    def reject(bad_packet, bad_shortlist, label):
        nonlocal total
        errors = validate(bad_packet, bad_shortlist)
        if not errors: raise AssertionError("missed synthetic forgery: " + label)
        total += 1
    for i, word in enumerate(WORDS):
        for field, value in (
            ("word", "fakeword"), ("level", "B2"),
            ("part_of_speech", "adverb"), ("editorial_hold", False),
            ("independent_english_review", True), ("independent_myanmar_review", True),
            ("independent_example_review", True), ("independent_exact_sense_cefr_review", True),
            ("independent_pronunciation_review", True), ("independent_approval", True),
            ("george_emma_listened", True), ("editorial_finding", "x"),
        ):
            bad = copy.deepcopy(packet); bad["entries"][i][field] = value
            reject(bad, shortlist, word + ":" + field)
        for field, value in (
            ("english_definition", "wrong"),
            ("burmese_meaning", "wrong"),
            ("example_sentence", "wrong"),
            ("source_index", -1),
            ("source_path", "draft/fake.json"),
            ("source_blob_sha", "0"*40),
        ):
            bad = copy.deepcopy(packet); bad["entries"][i]["original"][field] = value
            reject(bad, shortlist, word + ":original:" + field)
        for field, value in (
            ("url", "https://www.oxfordlearnersdictionaries.com/definition/english/" + word + "-fake"),
            ("access", "SEARCH_SNIPPET_ONLY"),
            ("line_locator", "0-0"), ("observed_on", "2020-01-01"),
            ("uk_ipa", "/fake/"), ("exact_sense_cefr_badge_observed", True),
            ("cefr_level_supported_by_this_page", "C1"),
        ):
            bad = copy.deepcopy(packet); bad["entries"][i]["publisher_evidence"][field] = value
            reject(bad, shortlist, word + ":publisher:" + field)
        for field, value in (
            ("english_definition", ""), ("burmese_meaning", "No Burmese"),
            ("example_sentence", "A sentence without the target word."),
        ):
            bad = copy.deepcopy(packet); bad["entries"][i]["unapproved_teaching_alternative"][field] = value
            reject(bad, shortlist, word + ":candidate:" + field)
    for field, value in (
        ("status", "APPROVED"), ("source_access_note", "independently verified"),
        ("shortlist_blob_sha", "0"*40), ("counts_by_level", {"C1": 1000}),
        ("independently_approved_by_level", {"C1": 8}), ("reviewer_signoffs", 8),
        ("real_audio_listening_signoffs", 16), ("physical_iphone_safari_signoffs", 1),
        ("production_deployed", True),
    ):
        bad = copy.deepcopy(packet); bad[field] = value
        reject(bad, shortlist, "root:" + field)
    bad = copy.deepcopy(packet); bad["entries"].pop()
    reject(bad, shortlist, "removed card")
    bad = copy.deepcopy(shortlist); bad["entries"][0]["reviewed_level"] = True
    reject(packet, bad, "forged frozen review")
    bad = copy.deepcopy(shortlist); bad["entries"][1]["word"] = bad["entries"][0]["word"]
    reject(packet, bad, "duplicate frozen headword")
    print(f"PASS: {total}/{total} synthetic source, Myanmar, grammar, CEFR, approval and release mutations rejected; NOT human review")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    for path, expected in ((PACKET, PACKET_SHA), (SHORTLIST, SHORTLIST_SHA)):
        if not path.is_file() or git_sha(path) != expected:
            raise SystemExit("BLOCK: frozen source blob mismatch " + str(path))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    errors = validate(packet, shortlist)
    if errors:
        print("\n".join("BLOCK: " + x for x in errors[:30]), file=sys.stderr)
        raise SystemExit(1)
    if args.self_test: adversarial_test(packet, shortlist)
    print("PASS: eight source-bound C1 Oxford research cards; 200 per level, 0 independent approvals; STAGING ONLY; " + args.level)

if __name__ == "__main__":
    main()
