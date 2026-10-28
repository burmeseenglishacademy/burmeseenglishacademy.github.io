#!/usr/bin/env python3
"""Fail-closed audit of 12 publisher-indexed A2 source-recovery editorial leads.

This is NOT independent human review or a release validator. It binds research
leads to the immutable provisional 1,000-word shortlist and rejects fake signoff.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "draft/CEFR-1000-CAMBRIDGE-A2-RECOVERY-TWELVE-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
WORDS = ("raincoat", "toothache", "bookshelf", "postcard", "saucepan",
         "dustbin", "washcloth", "shoelace", "lunchbox", "doormat",
         "bathrobe", "sunscreen")
LABELS = dict(zip(WORDS, ("A2", "A2", "A2", "A2", "B1", "B1",
                           None, None, None, None, None, None)))
URLS = {w: "https://dictionary.cambridge.org/dictionary/" + section + "/" + w
        for w, section in zip(WORDS,
            ("essential-british-english", "english", "learner-english",
             "english", "english", "english", "english", "english",
             "english", "english", "english", "learner-english"))}
SNAPSHOT_KEYS = ("english_definition", "myanmar_meaning", "example_sentence")


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def audit(packet, shortlist, source_bytes):
    issues = []
    expected = {e["word"]: e for e in shortlist.get("entries", [])
                if isinstance(e, dict) and e.get("word") in WORDS and e.get("level") == "A2"}
    if (packet.get("scope") != "USER_APPROVED_CEFR_1000_TOTAL_STAGING_ONLY"
            or packet.get("status") != "A2_RECOVERY_TWELVE_SOURCE_LEADS_EDITORIAL_HOLD"
            or packet.get("observed_on") != "2026-10-28"
            or packet.get("record_count") != 12
            or packet.get("independently_approved_count") != 0
            or packet.get("counts_by_level") != {"A1": 0, "A2": 12, "B1": 0, "B2": 0, "C1": 0}
            or packet.get("shortlist_blob_sha") != git_blob_sha(source_bytes)):
        issues.append("Packet scope, count, hold, or immutable shortlist SHA invalid")
    records = packet.get("records")
    if not isinstance(records, list) or len(records) != 12 or len(expected) != 12:
        return issues + ["Missing or excess records / canonical shortlist entries"]
    seen = set()
    for rec in records:
        if not isinstance(rec, dict):
            issues.append("Malformed record")
            continue
        w = rec.get("word")
        if w not in LABELS or w in seen:
            issues.append("Unknown or duplicate headword")
            continue
        seen.add(w)
        canonical = expected[w]
        if (rec.get("level") != "A2"
                or rec.get("part_of_speech") != canonical.get("part_of_speech")
                or rec.get("source_path") != canonical.get("source_path")):
            issues.append(w + ": canonical level/POS/source mismatch")
        snapshot = rec.get("shortlist_snapshot", {})
        if not isinstance(snapshot, dict) or any(
                snapshot.get(k) != canonical.get(
                    "burmese_meaning" if k == "myanmar_meaning" else k)
                for k in SNAPSHOT_KEYS):
            issues.append(w + ": English/Myanmar/example snapshot drift")
        source = rec.get("publisher_evidence", {})
        if (not isinstance(source, dict)
                or source.get("publisher") != "Cambridge University Press & Assessment"
                or source.get("url") != URLS[w]
                or source.get("observed_on") != "2026-10-28"
                or source.get("cefr_label") != LABELS[w]
                or source.get("access") != "PUBLISHER_WEB_SEARCH_RESULT_NOT_HUMAN_INDEPENDENT_REVIEW"
                or source.get("evidence_scope") != "PUBLISHER_INDEXED_SENSE_LEAD_ONLY"
                or not isinstance(source.get("sense_identifier"), str)
                or len(source["sense_identifier"]) < 8):
            issues.append(w + ": publisher evidence drift or fabricated CEFR label")
        if (rec.get("editorial_hold") is not True
                or rec.get("independently_reviewed") is not False
                or rec.get("release_approved") is not False
                or rec.get("reviewer_receipt") is not None
                or not isinstance(rec.get("editorial_risk"), str)
                or len(rec["editorial_risk"]) < 7
                or not isinstance(rec.get("independent_reviewer_task"), str)
                or len(rec["independent_reviewer_task"]) < 80):
            issues.append(w + ": false approval or insufficient editorial task")
        if w == "sunscreen":
            extra = rec.get("additional_publisher_evidence", {})
            if (not isinstance(extra, dict)
                    or extra.get("publisher") != "HarperCollins Publishers"
                    or extra.get("url") != "https://www.collinsdictionary.com/de/worterbuch/englisch/sunscreen"
                    or extra.get("cefr_label") != "B2"
                    or extra.get("observed_on") != "2026-10-28"):
                issues.append("sunscreen: Collins provenance or B2 lead altered")
        elif rec.get("additional_publisher_evidence") is not None:
            issues.append(w + ": unexpected second publisher")
    if seen != set(WORDS):
        issues.append("Headword coverage incomplete")
    return issues


def self_test(packet, shortlist, raw):
    changes = [
        lambda d: d.update(independently_approved_count=12),
        lambda d: d.update(shortlist_blob_sha="0" * 40),
        lambda d: d["records"][0]["shortlist_snapshot"].update(myanmar_meaning="အတည်ပြုပြီး"),
        lambda d: d["records"][1]["shortlist_snapshot"].update(example_sentence="False example."),
        lambda d: d["records"][2]["publisher_evidence"].update(cefr_label="B2"),
        lambda d: d["records"][3]["publisher_evidence"].update(url="https://example.org/forged"),
        lambda d: d["records"][4].update(independently_reviewed=True),
        lambda d: d["records"][5].update(release_approved=True),
        lambda d: d["records"][6].update(reviewer_receipt={"reviewer": "fake"}),
        lambda d: d["records"][7].update(editorial_hold=False),
        lambda d: d["records"][8].update(part_of_speech="verb"),
        lambda d: d["records"][11]["additional_publisher_evidence"].update(cefr_label="A2"),
        lambda d: d["records"].append(copy.deepcopy(d["records"][0])),
        lambda d: d["records"][9]["publisher_evidence"].update(access="DIRECT_HUMAN_VERIFIED"),
        lambda d: d["records"][0].update(editorial_risk=""),
    ]
    for i, mutate in enumerate(changes, 1):
        altered = copy.deepcopy(packet)
        mutate(altered)
        if not audit(altered, shortlist, raw):
            raise AssertionError("Mutation %d bypassed audit" % i)
    print("PASS: 15/15 forged source, Myanmar, example, level and approval mutations rejected")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=["A1", "A2", "B1", "B2", "C1", "ALL"], default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = load(SOURCE)
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw.decode("utf-8"))
    issues = audit(packet, shortlist, raw)
    if issues:
        for issue in issues:
            print("FAIL:", issue)
        return 1
    print("PASS: 12 A2 publisher-indexed leads bound to original bilingual snapshots; 0 independent approvals")
    print("NOTE: 4 Cambridge A2, 2 Cambridge B1 conflicts, 6 Cambridge unlabelled; Collins B2 sunscreen lead")
    if args.self_test:
        self_test(packet, shortlist, raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
