#!/usr/bin/env python3
"""Fail-closed structural audit for six UNAPPROVED UK discourse/degree sense leads.
This is documentary integrity only; NEVER human review, CEFR approval or listening.
"""
import argparse
import collections
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-UK-DISCOURSE-DEGREE-SIX-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads("{\"schema\":1,\"scope\":\"USER_APPROVED_1000_TOTAL_STAGING_ONLY\",\"status\":\"UNAPPROVED_UK_DISCOURSE_AND_DEGREE_SENSE_TRIAGE\",\"source_observed_on\":\"2026-11-01\",\"shortlist_blob_sha\":\"475e68ae17ab97bd937e73e5ce4794e0dcd76551\",\"counts_by_level\":{\"A1\":0,\"A2\":4,\"B1\":2,\"B2\":0,\"C1\":0},\"first_pass_written_by_level\":{\"A1\":200,\"A2\":200,\"B1\":200,\"B2\":200,\"C1\":200},\"independently_approved_by_level\":{\"A1\":0,\"A2\":0,\"B1\":0,\"B2\":0,\"C1\":0},\"real_george_emma_listening_signoffs\":0,\"source_scope_notice\":\"Six directly opened Oxford headword pages. Cambridge grammar quite/actually/eventually independently accessible, but Cambridge eventually dictionary direct page returned 403; its indexed B2 classification is a research lead only. Oxford topic labels do not certify exact-sense CEFR. All suggestions unapproved.\",\"production_status\":\"BLOCKED_STAGING_ONLY\",\"supplementary_grammar_sources\":[{\"url\":\"https://dictionary.cambridge.org/grammar/british-grammar/quite\",\"observed_on\":\"2026-11-01\",\"scope\":\"gradable/non-gradable meaning, not CEFR\"},{\"url\":\"https://dictionary.cambridge.org/us/grammar/british-grammar/actually\",\"observed_on\":\"2026-11-01\",\"scope\":\"discourse marker versus temporal false friend, not CEFR\"},{\"url\":\"https://dictionary.cambridge.org/grammar/british-grammar/eventually\",\"observed_on\":\"2026-11-01\",\"scope\":\"process endpoint versus list-final, not CEFR\"}],\"records\":[{\"word\":\"quite\",\"level\":\"A2\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"To a fairly large degree, but not completely.\",\"original_burmese_meaning\":\"အတော်အတန်\",\"original_example_sentence\":\"The journey was quite long.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":751,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"oxford_direct_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/quite\",\"oxford_page_lines\":\"107-115,129-139,158-173\",\"source_access\":\"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01\",\"source_supported_observation\":\"The draft fairly-large-degree sense fits gradable long; British quite with non-gradable adjectives can instead mean completely. Unrelated topic CEFR badges must not be used as exact-sense levels.\",\"risk_class\":\"UK_GRADABLE_VS_ABSOLUTE\",\"suggested_myanmar_UNAPPROVED\":\"အတော်အတန်၊ အတော်လေး (အတိုင်းအတာတစ်ခုအထိ)\",\"suggested_example_UNAPPROVED\":\"The journey was quite long, but we enjoyed it.\",\"source_observed_on\":\"2026-11-01\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"rather\",\"level\":\"A2\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"To a noticeable degree, often more than expected.\",\"original_burmese_meaning\":\"အတော်လေး၊ ထင်ထားသည်ထက်ပို၍\",\"original_example_sentence\":\"The instructions were rather difficult to follow.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":473,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"oxford_direct_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/rather_1\",\"oxford_page_lines\":\"107-132\",\"source_access\":\"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01\",\"source_supported_observation\":\"The draft degree sense is supported; rather can imply surprise, mild criticism or disappointment and is often stronger than quite in British usage. Do not conflate with rather than expressing preference.\",\"risk_class\":\"UK_DEGREE_PRAGMATICS\",\"suggested_myanmar_UNAPPROVED\":\"အတော်လေး၊ ထင်ထားသည်ထက်ပို၍ (တစ်ခါတစ်ရံ မနှစ်သက်မှုသဘောပါ)\",\"suggested_example_UNAPPROVED\":\"The instructions were rather difficult to follow.\",\"source_observed_on\":\"2026-11-01\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"actually\",\"level\":\"A2\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"Used to say what is true, especially when it differs from what someone expected.\",\"original_burmese_meaning\":\"တကယ်တော့၊ အမှန်တကယ်\",\"original_example_sentence\":\"I thought it was Tuesday, but it is actually Wednesday.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":287,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"oxford_direct_url\":\"https://www.oxfordlearnersdictionaries.com/us/definition/english/actually\",\"oxford_page_lines\":\"105-128,139-153\",\"source_access\":\"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01\",\"source_supported_observation\":\"The draft contrasts belief and fact. Actually can politely correct a statement; it does not mean currently or at present. Avoid misleading temporal Myanmar glosses.\",\"risk_class\":\"FACT_VS_CURRENT_TIME\",\"suggested_myanmar_UNAPPROVED\":\"တကယ်တော့၊ အမှန်မှာ (ထင်ထားသည့်အချက်ကို ပြင်ဆင်ဖော်ပြရာတွင်)\",\"suggested_example_UNAPPROVED\":\"I thought the meeting was on Tuesday, but it is actually on Wednesday.\",\"source_observed_on\":\"2026-11-01\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"however\",\"level\":\"A2\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"Used to introduce a fact that contrasts with what was just said.\",\"original_burmese_meaning\":\"သို့သော်၊ ဒါပေမဲ့\",\"original_example_sentence\":\"The room was small; however, it was comfortable.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":285,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"oxford_direct_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/however_1\",\"oxford_page_lines\":\"105-122\",\"source_access\":\"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01\",\"source_supported_observation\":\"The draft contrasts clauses and uses a semicolon correctly. However also has a distinct degree sense meaning to whatever extent. A comma splice with however is not equivalent to a conjunction but.\",\"risk_class\":\"CONTRAST_VS_DEGREE_AND_PUNCTUATION\",\"suggested_myanmar_UNAPPROVED\":\"သို့သော်၊ ဒါပေမဲ့ (ရှေ့ကပြောထားသည့်အချက်နှင့် ဆန့်ကျင်ဘက်ကို ဆက်ပြောရာတွင်)\",\"suggested_example_UNAPPROVED\":\"The room was small; however, it was comfortable.\",\"source_observed_on\":\"2026-11-01\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"therefore\",\"level\":\"B1\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"For that reason; as a result.\",\"original_burmese_meaning\":\"ထို့ကြောင့်၊ အဲဒီအတွက်ကြောင့်\",\"original_example_sentence\":\"The road was closed; therefore, we took another route.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":474,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"oxford_direct_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/therefore\",\"oxford_page_lines\":\"105-114\",\"source_access\":\"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01\",\"source_supported_observation\":\"Therefore introduces a logical consequence, unlike however which signals contrast. The draft semicolon construction is appropriate; avoid treating therefore as a subordinating conjunction.\",\"risk_class\":\"LOGICAL_RESULT_VS_CONTRAST\",\"suggested_myanmar_UNAPPROVED\":\"ထို့ကြောင့်၊ အဲဒီအကြောင်းကြောင့် (အကျိုးဆက်ကို ဖော်ပြရာတွင်)\",\"suggested_example_UNAPPROVED\":\"The road was closed; therefore, we took another route.\",\"source_observed_on\":\"2026-11-01\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"eventually\",\"level\":\"B1\",\"part_of_speech\":\"adverb\",\"original_english_definition\":\"In the end, after a period of time or several difficulties.\",\"original_burmese_meaning\":\"နောက်ဆုံးတွင်၊ အချိန်ကြာပြီးနောက်\",\"original_example_sentence\":\"After several attempts, she eventually solved the problem.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":302,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"oxford_direct_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/eventually\",\"oxford_page_lines\":\"105-119\",\"source_access\":\"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01\",\"source_supported_observation\":\"Eventually marks the end of a period or process, not the last item of a speech or list. Cambridge publisher grammar supports this distinction; Cambridge dictionary indexed B2 conflicts with provisional B1 but direct dictionary page returned 403, so no independently verified CEFR correction.\",\"risk_class\":\"END_OF_PROCESS_VS_LIST_FINAL_AND_LEVEL_CONFLICT\",\"suggested_myanmar_UNAPPROVED\":\"အချိန်ကြာပြီးနောက် နောက်ဆုံးတွင်၊ အခက်အခဲများကျော်ဖြတ်ပြီးမှ\",\"suggested_example_UNAPPROVED\":\"After several attempts, she eventually solved the problem.\",\"source_observed_on\":\"2026-11-01\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"real_george_listening\":false,\"real_emma_listening\":false}]}")


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def validate(packet, shortlist):
    errors = []
    if canonical(packet) != canonical(EXPECTED):
        errors.append("Research packet differs from immutable six-record source/provenance baseline")
    if not isinstance(shortlist, dict):
        return errors + ["Shortlist is not an object"]
    entries = shortlist.get("entries")
    if not isinstance(entries, list) or len(entries) != 1000:
        return errors + ["Frozen shortlist does not have exactly 1000 entries"]
    counts = collections.Counter(e.get("level") for e in entries if isinstance(e, dict))
    if any(counts.get(level) != 200 for level in LEVELS):
        errors.append("Frozen shortlist is not 200 entries per CEFR level")
    if shortlist.get("independently_approved_by_level") != {level: 0 for level in LEVELS}:
        errors.append("Unsubstantiated independent approval counts")
    by_word = collections.defaultdict(list)
    for e in entries:
        if not isinstance(e, dict):
            errors.append("Non-object shortlist row")
            continue
        by_word[e.get("word")].append(e)
        if (e.get("editorial_hold") is not True or
            any(e.get(k) is not False for k in
                ("reviewed_english", "reviewed_burmese", "reviewed_example",
                 "reviewed_level", "reviewed_pronunciation", "release_approved"))):
            errors.append("Shortlist editorial hold or approval flags altered")
    mapping = {
        "level": "level", "part_of_speech": "part_of_speech",
        "original_english_definition": "english_definition",
        "original_burmese_meaning": "burmese_meaning",
        "original_example_sentence": "example_sentence",
        "source_path": "source_path", "source_index": "source_index",
        "source_blob_sha": "source_blob_sha"
    }
    for row in EXPECTED["records"]:
        matches = by_word.get(row["word"], [])
        if len(matches) != 1:
            errors.append("Missing or duplicate held word " + row["word"])
            continue
        for packet_field, shortlist_field in mapping.items():
            if canonical(matches[0].get(shortlist_field)) != canonical(row[packet_field]):
                errors.append("Frozen source mismatch: " + row["word"] + "." + shortlist_field)
    return errors


def self_test(packet, shortlist):
    rejected = 0
    def reject(p, s, label):
        nonlocal rejected
        if not validate(p, s):
            raise AssertionError("FAIL OPEN: " + label)
        rejected += 1
    for i, row in enumerate(packet["records"]):
        for field, value in row.items():
            p = copy.deepcopy(packet)
            p["records"][i][field] = ("FORGED" if value is None else
                (not value if isinstance(value, bool) else
                 value + 1 if type(value) is int else str(value) + " FORGED"))
            reject(p, shortlist, row["word"] + "." + field)
        p = copy.deepcopy(packet)
        p["records"][i]["independent_reviewer_receipt"] = {"result": "PASS"}
        reject(p, shortlist, row["word"] + ".injected_review")
        p = copy.deepcopy(packet)
        p["records"].pop(i)
        reject(p, shortlist, row["word"] + ".deleted")
    for field, value in packet.items():
        if field == "records":
            continue
        p = copy.deepcopy(packet)
        p[field] = "FORGED"
        reject(p, shortlist, "metadata." + field)
    for field in ("reviewed_english", "reviewed_burmese", "reviewed_example",
                  "reviewed_level", "reviewed_pronunciation", "release_approved", "editorial_hold"):
        s = copy.deepcopy(shortlist)
        s["entries"][0][field] = not s["entries"][0][field]
        reject(packet, s, "shortlist." + field)
    s = copy.deepcopy(shortlist)
    s["independently_approved_by_level"]["A1"] = 1
    reject(packet, s, "false_approval_count")
    s = copy.deepcopy(shortlist)
    s["entries"][0]["burmese_meaning"] = "FORGED"
    reject(packet, s, "changed_held_myanmar")
    return rejected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("ALL",) + LEVELS, default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf8"))
    issues = validate(packet, shortlist)
    if issues:
        print(json.dumps({"status": "FAIL", "issues": issues[:15]}, ensure_ascii=False))
        return 1
    mutations = self_test(packet, shortlist) if args.self_test else 0
    count = sum(r["level"] == args.level for r in packet["records"]) if args.level != "ALL" else 6
    print(json.dumps({"status": "PASS_STAGING_RESEARCH_ONLY", "level": args.level,
        "source_bound_records_in_level": count, "total_records": 6,
        "adversarial_mutations_rejected": mutations, "independently_approved": 0,
        "actual_george_emma_listening_signoffs": 0, "production": "BLOCKED_STAGING_ONLY"}))
    return 0

if __name__ == "__main__":
    sys.exit(main())
