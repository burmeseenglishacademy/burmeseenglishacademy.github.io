#!/usr/bin/env python3
"""Fail-closed six-card Cambridge indexed CEFR triage integrity audit.

Search-index labels are research leads, never direct publisher inspection or
independent CEFR approval. The frozen shortlist and production are untouched.
"""
import argparse
import collections
import copy
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-C1-B2-CAMBRIDGE-INDEXED-SIX-SENSE-TRIAGE-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_GIT_BLOB = "d05cb4ec1f6985603c90283f8599c97fa2e834fb"
SHORTLIST_GIT_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "signature": ("C1", "B1"),
    "upgrade": ("C1", "B2"),
    "diverse": ("C1", "B2"),
    "closely": ("B2", "C1"),
    "neutral": ("C1", "C1"),
    "asset": ("C1", "C1"),
}
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()


def verify(packet, shortlist, baseline, level="ALL", historical=True):
    issues = []
    def fail(message):
        issues.append(message)
    if level not in (*LEVELS, "ALL"):
        return ["Invalid CEFR lane"]
    if packet != baseline:
        fail("Indexed research packet changed from frozen source observation")
    if not isinstance(packet, dict) or not isinstance(packet.get("records"), list):
        return issues + ["Research packet missing records"]
    if packet.get("status") != "UNAPPROVED_SIX_CAMBRIDGE_INDEXED_EXACT_SENSE_TRIAGE":
        fail("Research packet status is not unapproved")
    if packet.get("shortlist_blob_sha") != SHORTLIST_GIT_BLOB:
        fail("Research packet no longer pins frozen shortlist")
    if packet.get("counts_by_level") != dict(A1=0, A2=0, B1=0, B2=1, C1=5):
        fail("Six-record level counts differ")
    if packet.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
        fail("False independent approval count")
    if packet.get("real_george_emma_listening_signoffs") != 0:
        fail("False listening signoff")
    if packet.get("production_status") != "BLOCKED_STAGING_ONLY":
        fail("Release status changed")
    if not isinstance(shortlist, dict) or not isinstance(shortlist.get("entries"), list):
        return issues + ["Shortlist missing or invalid"]
    entries = shortlist["entries"]
    if len(entries) != 1000:
        fail("Shortlist must contain exactly 1000 cards")
    counts = collections.Counter(x.get("level") for x in entries if isinstance(x, dict))
    if counts != collections.Counter(dict.fromkeys(LEVELS, 200)):
        fail("Shortlist does not have exactly 200 per level")
    names = [str(x.get("word", "")).casefold() for x in entries if isinstance(x, dict)]
    if len(names) != 1000 or len(set(names)) != 1000:
        fail("Shortlist headwords duplicated or malformed")
    for entry in entries:
        if not isinstance(entry, dict):
            fail("Malformed shortlist entry")
            continue
        if entry.get("editorial_hold") is not True or any(entry.get(k) is not False for k in FLAGS):
            fail("Shortlist contains false review approval or lifted editorial hold")
        if entry.get("status") != "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING":
            fail("Shortlist status changed")
    records = packet["records"]
    if [x.get("word") for x in records if isinstance(x, dict)] != list(EXPECTED):
        fail("Research records missing or reordered")
    by_word = {x.get("word"): x for x in entries if isinstance(x, dict)}
    for row in records:
        if not isinstance(row, dict):
            fail("Malformed research row")
            continue
        word = row.get("word")
        if word not in EXPECTED:
            fail("Unexpected research word")
            continue
        frozen = by_word.get(word)
        if frozen is None:
            fail("Research word missing from shortlist")
            continue
        for original, source in (
            ("word", "word"), ("level", "level"),
            ("part_of_speech", "part_of_speech"),
            ("original_english_definition", "english_definition"),
            ("original_burmese_meaning", "burmese_meaning"),
            ("original_example_sentence", "example_sentence"),
            ("source_path", "source_path"),
            ("source_index", "source_index"),
            ("source_blob_sha", "source_blob_sha"),
        ):
            if row.get(original) != frozen.get(source):
                fail(f"{word}: frozen {original} mismatch")
        source = row.get("cambridge_index_observation", {})
        expected_level, indexed_level = EXPECTED[word]
        if row.get("level") != expected_level or source.get("index_cefr_label") != indexed_level:
            fail(f"{word}: CEFR observation or draft level changed")
        if source.get("url") != f"https://dictionary.cambridge.org/dictionary/english/{word}":
            fail(f"{word}: wrong publisher headword URL")
        if source.get("observed_on") != "2026-11-01" or source.get("access") != "SEARCH_INDEX_EXCERPT_ONLY_DIRECT_PAGE_HTTP_403":
            fail(f"{word}: indexed evidence misrepresented as direct inspection")
        if row.get("editorial_hold") is not True or row.get("independently_checked") is not False or row.get("release_approved") is not False or row.get("independent_reviewer_receipt") is not None or row.get("real_george_listening") is not False or row.get("real_emma_listening") is not False:
            fail(f"{word}: fabricated review or audio listening receipt")
        if historical:
            try:
                raw = subprocess.check_output(["git", "cat-file", "blob", row["source_blob_sha"]], cwd=ROOT)
                old = json.loads(raw.decode("utf8"))["entries"][row["source_index"]]
                for original, field in (("word", "word"), ("level", "level"),
                    ("part_of_speech", "part_of_speech"),
                    ("original_english_definition", "english_definition"),
                    ("original_burmese_meaning", "burmese_meaning"),
                    ("original_example_sentence", "example_sentence")):
                    if row.get(original) != old.get(field):
                        fail(f"{word}: historical Git provenance differs at {original}")
            except (KeyError, IndexError, ValueError, subprocess.CalledProcessError) as exc:
                fail(f"{word}: historical provenance inaccessible: {exc}")
    return issues


def negative_tests(packet, shortlist):
    count = 0
    for i, row in enumerate(packet["records"]):
        for field, bad in (
            ("original_english_definition", "FORGED"),
            ("original_burmese_meaning", "အတု"),
            ("original_example_sentence", "Forged example."),
            ("source_index", 99999),
            ("source_blob_sha", "0" * 40),
            ("suggested_myanmar_UNAPPROVED", "ပြင်ပြီး"),
            ("independent_reviewer_question", "Already approved"),
            ("independently_checked", True),
            ("release_approved", True),
            ("editorial_hold", False),
            ("independent_reviewer_receipt", {"reviewer": "bot"}),
            ("real_george_listening", True),
            ("real_emma_listening", True),
        ):
            altered = copy.deepcopy(packet)
            altered["records"][i][field] = bad
            count += 1
            if not verify(altered, shortlist, packet, historical=False):
                raise AssertionError(f"Mutation escaped: {row['word']}/{field}")
        for field, bad in (("index_cefr_label", "A1"), ("url", "https://dictionary.cambridge.org/dictionary/english/other"),
                           ("access", "DIRECT_PUBLISHER_PAGE_OPENED")):
            altered = copy.deepcopy(packet)
            altered["records"][i]["cambridge_index_observation"][field] = bad
            count += 1
            if not verify(altered, shortlist, packet, historical=False):
                raise AssertionError(f"Source mutation escaped: {row['word']}/{field}")
        altered = copy.deepcopy(shortlist)
        next(x for x in altered["entries"] if x["word"] == row["word"])["reviewed_level"] = True
        count += 1
        if not verify(packet, altered, packet, historical=False):
            raise AssertionError(f"False shortlist approval escaped: {row['word']}")
    for field, bad in (("production_status", "LIVE"), ("real_george_emma_listening_signoffs", 1000),
                       ("counts_by_level", dict(A1=0, A2=0, B1=0, B2=0, C1=6))):
        altered = copy.deepcopy(packet)
        altered[field] = bad
        count += 1
        if not verify(altered, shortlist, packet, historical=False):
            raise AssertionError("Packet status mutation escaped: " + field)
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet_bytes = PACKET.read_bytes()
    shortlist_bytes = SHORTLIST.read_bytes()
    if git_blob(packet_bytes) != PACKET_GIT_BLOB:
        sys.exit("FAIL: six-record packet Git blob differs from observed baseline")
    if git_blob(shortlist_bytes) != SHORTLIST_GIT_BLOB:
        sys.exit("FAIL: original 1000-word shortlist changed")
    packet = json.loads(packet_bytes)
    shortlist = json.loads(shortlist_bytes)
    issues = verify(packet, shortlist, packet, level=args.level)
    if issues:
        sys.exit("FAIL: " + "; ".join(issues[:20]))
    n = sum(x["level"] == args.level for x in packet["records"]) if args.level != "ALL" else len(packet["records"])
    print(f"PASS: {args.level} indexed research cards={n}; 1000 frozen held; independent approvals=0; publisher direct opens=403; no release")
    if args.self_test:
        count = negative_tests(packet, shortlist)
        print(f"PASS: {count}/{count} synthetic adversarial mutations rejected (not independent review)")


if __name__ == "__main__":
    main()
