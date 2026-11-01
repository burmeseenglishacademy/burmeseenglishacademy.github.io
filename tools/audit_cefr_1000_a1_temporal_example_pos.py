#!/usr/bin/env python3
"""Fail-closed A1 time-word POS/example research audit. Staging only; NO human signoff."""
import argparse
import collections
import copy
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-A1-TEMPORAL-ADVERB-NOUN-EXAMPLE-POS-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads("{\"schema\":1,\"scope\":\"USER_APPROVED_1000_TOTAL_STAGING_ONLY\",\"status\":\"UNAPPROVED_A1_TEMPORAL_ADVERB_NOUN_EXAMPLE_POS_TRIAGE\",\"observed_on\":\"2026-11-01\",\"shortlist_blob_sha\":\"475e68ae17ab97bd937e73e5ce4794e0dcd76551\",\"counts_by_level\":{\"A1\":3,\"A2\":0,\"B1\":0,\"B2\":0,\"C1\":0},\"first_pass_written_by_level\":{\"A1\":200,\"A2\":200,\"B1\":200,\"B2\":200,\"C1\":200},\"independently_approved_by_level\":{\"A1\":0,\"A2\":0,\"B1\":0,\"B2\":0,\"C1\":0},\"real_george_emma_listening_signoffs\":0,\"production_status\":\"BLOCKED_STAGING_ONLY\",\"source_scope_notice\":\"Five directly opened Oxford noun/adverb headword pages: today and yesterday have noun examples identical to the held A1 adverb cards, while tomorrow is an adverb control. Oxford Time a1 topic tags are NOT independent exact-sense CEFR labels. Publisher research does not constitute independent English/Myanmar/example approval.\",\"records\":[{\"word\":\"today\",\"level\":\"A1\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"On this present day.\",\"original_burmese_meaning\":\"ဒီနေ့၊ ယနေ့\",\"original_example_sentence\":\"Today is Monday.\",\"source_path\":\"draft/A1-EDITORIAL-STARTER.json\",\"source_index\":138,\"source_blob_sha\":\"ff1e93f60828ef2f94c9146522ce94075183b0ae\",\"oxford_direct_sources\":[{\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/today_2\",\"observed_pos\":\"noun\",\"line_locator\":\"88-116\",\"observation\":\"Oxford explicitly labels today as an uncountable noun and gives Today is Monday as a noun example, matching the frozen sentence.\",\"publisher\":\"Oxford University Press\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"observed_on\":\"2026-11-01\",\"cefr_scope\":\"OXFORD_TOPIC_LABEL_NOT_INDEPENDENT_EXACT_SENSE_CEFR\"},{\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/today_1\",\"observed_pos\":\"adverb\",\"line_locator\":\"88-112\",\"observation\":\"Oxford separately labels today an adverb meaning on this day; its examples place today as a time modifier, not as the subject.\",\"publisher\":\"Oxford University Press\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"observed_on\":\"2026-11-01\",\"cefr_scope\":\"OXFORD_TOPIC_LABEL_NOT_INDEPENDENT_EXACT_SENSE_CEFR\"}],\"risk_class\":\"FROZEN_ADVERB_CARD_USES_NOUN_SUBJECT_IN_EXAMPLE\",\"source_supported_observation\":\"Today is Monday is grammatical English but today functions as a noun subject, not the adverb named on the card.\",\"suggested_example_UNAPPROVED\":\"I have an English lesson today.\",\"suggested_myanmar_UNAPPROVED\":\"ဒီနေ့၊ ယနေ့ (အချိန်ပြ ကြိယာဝိသေသနအဖြစ်)\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false,\"independent_reviewer_receipt\":null},{\"word\":\"yesterday\",\"level\":\"A1\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"On the day before today.\",\"original_burmese_meaning\":\"မနေ့က\",\"original_example_sentence\":\"Yesterday was Sunday.\",\"source_path\":\"draft/A1-EDITORIAL-STARTER.json\",\"source_index\":140,\"source_blob_sha\":\"ff1e93f60828ef2f94c9146522ce94075183b0ae\",\"oxford_direct_sources\":[{\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/yesterday_2\",\"observed_pos\":\"noun\",\"line_locator\":\"88-123\",\"observation\":\"Oxford explicitly labels yesterday an uncountable noun and gives Yesterday was Sunday, exactly the frozen sentence.\",\"publisher\":\"Oxford University Press\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"observed_on\":\"2026-11-01\",\"cefr_scope\":\"OXFORD_TOPIC_LABEL_NOT_INDEPENDENT_EXACT_SENSE_CEFR\"},{\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/yesterday_1\",\"observed_pos\":\"adverb\",\"line_locator\":\"88-123\",\"observation\":\"Oxford separately labels yesterday an adverb meaning on the previous day; its examples use yesterday to modify events.\",\"publisher\":\"Oxford University Press\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"observed_on\":\"2026-11-01\",\"cefr_scope\":\"OXFORD_TOPIC_LABEL_NOT_INDEPENDENT_EXACT_SENSE_CEFR\"}],\"risk_class\":\"FROZEN_ADVERB_CARD_USES_NOUN_SUBJECT_IN_EXAMPLE\",\"source_supported_observation\":\"Yesterday was Sunday is grammatical English but yesterday functions as a noun subject, not the adverb named on the card.\",\"suggested_example_UNAPPROVED\":\"I was at home yesterday.\",\"suggested_myanmar_UNAPPROVED\":\"မနေ့က၊ မနေ့တွင် (အချိန်ပြ ကြိယာဝိသေသနအဖြစ်)\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false,\"independent_reviewer_receipt\":null},{\"word\":\"tomorrow\",\"level\":\"A1\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"On the day after today.\",\"original_burmese_meaning\":\"မနက်ဖြန်\",\"original_example_sentence\":\"We have class tomorrow.\",\"source_path\":\"draft/A1-EDITORIAL-STARTER.json\",\"source_index\":139,\"source_blob_sha\":\"ff1e93f60828ef2f94c9146522ce94075183b0ae\",\"oxford_direct_sources\":[{\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/tomorrow_1\",\"observed_pos\":\"adverb\",\"line_locator\":\"88-113\",\"observation\":\"Oxford labels tomorrow an adverb meaning on or during the day after today; the frozen We have class tomorrow is consistent with this usage.\",\"publisher\":\"Oxford University Press\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"observed_on\":\"2026-11-01\",\"cefr_scope\":\"OXFORD_TOPIC_LABEL_NOT_INDEPENDENT_EXACT_SENSE_CEFR\"}],\"risk_class\":\"CORRECT_ADVERB_CONTROL_NO_REWRITE_REQUIRED\",\"source_supported_observation\":\"We have class tomorrow uses tomorrow as a time adverb; retain as a control rather than falsely flagging every temporal headword.\",\"suggested_example_UNAPPROVED\":\"We have class tomorrow.\",\"suggested_myanmar_UNAPPROVED\":\"မနက်ဖြန်\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false,\"independent_reviewer_receipt\":null}]}")
EXPECTED_WORDS = ("today", "yesterday", "tomorrow")


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + bytes([0]) + raw).hexdigest()


def validate(packet, shortlist):
    errors = []
    if canonical(packet) != canonical(EXPECTED):
        errors.append("Research packet differs from frozen direct-Oxford source and bilingual provenance")
    raw = SHORTLIST.read_bytes()
    if git_blob_sha(raw) != EXPECTED["shortlist_blob_sha"]:
        errors.append("Full 1000-word provisional shortlist Git blob changed")
    if not isinstance(shortlist, dict):
        return errors + ["Shortlist is not an object"]
    if canonical(shortlist) != canonical(json.loads(raw.decode("utf8"))):
        errors.append("Injected shortlist differs from on-disk frozen shortlist")
    entries = shortlist.get("entries")
    if not isinstance(entries, list) or len(entries) != 1000:
        return errors + ["Expected exactly 1000 held first-pass entries"]
    if shortlist.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("Provisional release status was altered")
    targets = {k: 200 for k in LEVELS}
    if shortlist.get("scope_target") != targets or shortlist.get("counts_by_level") != targets:
        errors.append("200-per-level first-pass scope altered")
    if shortlist.get("independently_approved_by_level") != {k: 0 for k in LEVELS}:
        errors.append("Unsubstantiated independent approval count")
    counts = collections.Counter()
    lookup = {}
    for row in entries:
        if not isinstance(row, dict):
            errors.append("Non-object shortlist entry")
            continue
        counts[row.get("level")] += 1
        word = row.get("word")
        if not isinstance(word, str) or word.casefold() in lookup:
            errors.append("Missing or duplicated shortlist headword")
        else:
            lookup[word.casefold()] = row
        if (row.get("editorial_hold") is not True or
            any(row.get(field) is not False for field in
                ("reviewed_english", "reviewed_burmese", "reviewed_example",
                 "reviewed_level", "reviewed_pronunciation", "release_approved"))):
            errors.append("Provisional entry editorial hold or independent flags altered")
    if any(counts.get(k) != 200 for k in LEVELS) or len(lookup) != 1000:
        errors.append("Actual per-level counts or headword uniqueness failed")
    if [r["word"] for r in EXPECTED["records"]] != list(EXPECTED_WORDS):
        errors.append("Unexpected baseline headwords")
    fields = {
        "level": "level", "part_of_speech": "part_of_speech",
        "original_english_definition": "english_definition",
        "original_burmese_meaning": "burmese_meaning",
        "original_example_sentence": "example_sentence",
        "source_path": "source_path", "source_index": "source_index",
        "source_blob_sha": "source_blob_sha",
    }
    for frozen in EXPECTED["records"]:
        row = lookup.get(frozen["word"])
        if row is None:
            errors.append("Held A1 headword missing: " + frozen["word"])
            continue
        for packet_field, shortlist_field in fields.items():
            if canonical(row.get(shortlist_field)) != canonical(frozen[packet_field]):
                errors.append(f"Frozen mismatch {frozen['word']}.{shortlist_field}")
        if row.get("level") != "A1" or row.get("part_of_speech") != "adverb":
            errors.append("Time-word POS/level changed")
    return errors


def mutate_leaf(value):
    if value is None:
        return {"forged": "approval"}
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if isinstance(value, str):
        return value + " [FORGED]"
    raise TypeError("Unsupported leaf")


def leaf_paths(value, prefix=()):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from leaf_paths(item, prefix + (key,))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from leaf_paths(item, prefix + (index,))
    else:
        yield prefix


def assign_path(obj, path, value):
    cur = obj
    for part in path[:-1]:
        cur = cur[part]
    cur[path[-1]] = value


def self_test(packet, shortlist):
    rejected = 0
    def reject(p, s, label):
        nonlocal rejected
        if not validate(p, s):
            raise AssertionError("FAIL OPEN: " + label)
        rejected += 1
    for path in leaf_paths(packet):
        p = copy.deepcopy(packet)
        cur = p
        for part in path:
            cur = cur[part]
        assign_path(p, path, mutate_leaf(cur))
        reject(p, shortlist, "packet:" + repr(path))
    for index in range(len(packet["records"])):
        p = copy.deepcopy(packet)
        p["records"].pop(index)
        reject(p, shortlist, "deleted held source row")
        p = copy.deepcopy(packet)
        p["records"][index]["independent_reviewer_receipt"] = {"reviewer": "auto", "result": "PASS"}
        reject(p, shortlist, "forged reviewer")
        p = copy.deepcopy(packet)
        p["records"][index]["oxford_direct_sources"][0]["url"] = "https://example.com/forged"
        reject(p, shortlist, "forged publisher")
    for word in EXPECTED_WORDS:
        for field in ("english_definition", "burmese_meaning", "example_sentence",
                      "part_of_speech", "level", "source_blob_sha", "source_index",
                      "editorial_hold", "release_approved", "reviewed_example"):
            s = copy.deepcopy(shortlist)
            row = next(x for x in s["entries"] if x["word"] == word)
            row[field] = mutate_leaf(row[field])
            reject(packet, s, "shortlist:" + word + "." + field)
    s = copy.deepcopy(shortlist)
    s["entries"][0]["burmese_meaning"] += " FORGED"
    reject(packet, s, "unrelated A1 frozen word")
    s = copy.deepcopy(shortlist)
    s["entries"][-1]["release_approved"] = True
    reject(packet, s, "unrelated C1 false approval")
    s = copy.deepcopy(shortlist)
    s["entries"][10]["word"] = s["entries"][11]["word"]
    reject(packet, s, "duplicate headword")
    for field in ("release_status", "scope_target", "counts_by_level", "independently_approved_by_level"):
        s = copy.deepcopy(shortlist)
        s[field] = "FORGED"
        reject(packet, s, "scope:" + field)
    return rejected


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text("utf8"))
    shortlist = json.loads(SHORTLIST.read_text("utf8"))
    errors = validate(packet, shortlist)
    if errors:
        for issue in errors[:20]:
            print("FAIL:", issue, file=sys.stderr)
        return 1
    count = sum(r["level"] == args.level or args.level == "ALL" for r in packet["records"])
    report = {"scope": "STAGING_ONLY", "level": args.level, "source_bound_records": count,
              "direct_oxford_pages": sum(len(r["oxford_direct_sources"]) for r in packet["records"] if args.level in ("ALL", r["level"])),
              "example_pos_mismatches": sum(r["risk_class"] == "FROZEN_ADVERB_CARD_USES_NOUN_SUBJECT_IN_EXAMPLE" for r in packet["records"] if args.level in ("ALL", r["level"])),
              "independently_approved": 0, "real_audio_listening": 0, "release": "BLOCKED"}
    if args.self_test:
        report["adversarial_mutations_rejected"] = self_test(packet, shortlist)
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
