#!/usr/bin/env python3
"""Source-integrity audit only; Oxford dictionary observations are NOT CEFR approval."""
import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "draft/CEFR-1000-OXFORD-DICTIONARY-C1-SENSE-TRIAGE-2026-10-27.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
WORDS = {"affable", "conscientious", "alacrity", "abstruse", "equivocate",
         "obfuscate", "equanimity", "catharsis"}
EXPECTED_SCOPE = {"affable": "TOPIC_PERSONAL_QUALITIES_C2",
                  "conscientious": "TOPIC_PERSONAL_QUALITIES_C1"}
HOLD_FIELDS = ("independent_english_review", "independent_myanmar_review",
               "independent_example_review", "independent_cefr_sense_review",
               "release_approved")

def check(packet, shortlist, level):
    errors = []
    rows = packet.get("records", [])
    if (packet.get("status") != "OXFORD_DIRECT_DICTIONARY_C1_SENSE_TRIAGE_STAGING_HOLD"
            or packet.get("observed_on") != "2026-10-27"
            or packet.get("shortlist_blob_sha") != "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
            or packet.get("record_count") != 8
            or packet.get("independently_approved_count") != 0
            or not isinstance(rows, list) or len(rows) != 8):
        errors.append("Packet scope, source snapshot, or hold counts changed")
        return errors
    if {r.get("word") for r in rows if isinstance(r, dict)} != WORDS:
        errors.append("Wrong, duplicate or missing Oxford source headword")
    source = {(x["word"], x["level"]): x for x in shortlist["entries"]}
    for r in rows:
        if not isinstance(r, dict):
            errors.append("Non-object source record")
            continue
        if level not in ("ALL", r.get("shortlist_level")):
            continue
        word = r.get("word")
        original = source.get((word, "C1"))
        if original is None:
            errors.append(str(word) + ": no C1 shortlist entry")
            continue
        for a, b in (("shortlist_english_definition", "english_definition"),
                     ("shortlist_myanmar_meaning", "burmese_meaning"),
                     ("shortlist_example", "example_sentence"),
                     ("shortlist_part_of_speech", "part_of_speech")):
            if r.get(a) != original.get(b):
                errors.append(str(word) + ": shortlist snapshot changed " + a)
        if (r.get("source_url") != "https://www.oxfordlearnersdictionaries.com/definition/english/" + word
                or r.get("publisher") != "Oxford University Press"
                or r.get("source_access") != "DIRECT_PUBLISHER_DICTIONARY_PAGE_WEB_TEXT"
                or r.get("observed_on") != "2026-10-27"
                or r.get("source_word_pos") != original.get("part_of_speech")):
            errors.append(str(word) + ": publisher source provenance or POS changed")
        span = r.get("source_line_range_0_based")
        if (not isinstance(span, list) or len(span) != 2
                or any(type(v) is not int for v in span)
                or span[0] < 85 or span[1] < span[0] or span[1] > 140):
            errors.append(str(word) + ": missing direct-page text locator")
        if r.get("source_cefr_evidence_scope") != EXPECTED_SCOPE.get(word, "NO_ENTRY_LEVEL_OBSERVED"):
            errors.append(str(word) + ": invented or changed publisher CEFR scope")
        if any(r.get(flag) is not False for flag in HOLD_FIELDS) or r.get("editorial_hold") is not True or r.get("independent_reviewer_receipt") is not None:
            errors.append(str(word) + ": independent approval or hold forged")
        if not isinstance(r.get("editorial_risk"), str) or len(r["editorial_risk"]) < 40:
            errors.append(str(word) + ": editorial risk rationale missing")
    return errors

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=["A1", "A2", "B1", "B2", "C1", "ALL"], default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(SOURCE.read_text(encoding="utf8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf8"))
    issues = check(packet, shortlist, args.level)
    if args.self_test:
        assert args.level == "ALL", "negative tests only for ALL"
        for change in (
            lambda p: p["records"][0].update(release_approved=True),
            lambda p: p["records"][0].update(independent_reviewer_receipt={"reviewer": "FAKE"}),
            lambda p: p["records"][0].update(source_url="https://dictionary.cambridge.org/dictionary/english/affable"),
            lambda p: p["records"][0].update(source_cefr_evidence_scope="CORE_OXFORD_5000_C1"),
            lambda p: p["records"][0].update(shortlist_example="A fabricated sentence."),
            lambda p: p["records"][0].update(source_line_range_0_based=[0, 1]),
            lambda p: p["records"].__setitem__(1, copy.deepcopy(p["records"][0])),
        ):
            fake = copy.deepcopy(packet)
            change(fake)
            assert check(fake, shortlist, "ALL"), "Tampered source packet accepted"
        print("PASS: seven mock tamper cases rejected; no independent approvals")
    report = {"level": args.level, "direct_oxford_dictionary_observations":
              sum(x.get("shortlist_level") == args.level or args.level == "ALL" for x in packet["records"]),
              "independently_approved": 0, "errors": issues,
              "status": "SOURCE_TRIAGE_STAGING_HOLD_NOT_RELEASE"}
    Path(f"cefr-1000-oxford-dictionary-{args.level}.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf8")
    print(json.dumps(report))
    if issues:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
