#!/usr/bin/env python3
"""Fail-closed, staging-only audit of 12 source-bound countability/number risks.

Grammar evidence is NOT an independent English/Myanmar/exact-sense CEFR review,
human listening, an approved manifest, or permission to publish.
"""
import argparse
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-NOUN-COUNTABILITY-AND-AGREEMENT-TWELVE-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FROZEN_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
EXPECTED = json.loads("{\"bread\":{\"level\":\"A1\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"UNCOUNTABLE_FOOD\",\"source_supported_grammar_observation\":\"Bread is a mass noun in this food sense; count loaves or slices, not breads for ordinary portions.\",\"grammar_source_url\":\"https://www.oxfordonlineenglish.com/uncountable-nouns\",\"grammar_source_locator\":\"583-586\",\"proposed_original_example_UNAPPROVED\":\"We bought two loaves of bread for the picnic.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"ပေါင်မုန့်ကို အရေအတွက်ဖော်ပြရာတွင် a loaf of bread သို့မဟုတ် a slice of bread ဟု သုံးနိုင်သည်။\"},\"information\":{\"level\":\"A2\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"UNCOUNTABLE_INFORMATION\",\"source_supported_grammar_observation\":\"Information is uncountable; not an information or informations. A piece of information is countable.\",\"grammar_source_url\":\"https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/uncount-nouns\",\"grammar_source_locator\":\"23-29,39-46\",\"proposed_original_example_UNAPPROVED\":\"The receptionist gave us a piece of information about the bus timetable.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"information ကို uncountable noun အဖြစ် သုံးပြီး အချက်တစ်ချက်ကို a piece of information ဟု ဖော်ပြနိုင်သည်။\"},\"data\":{\"level\":\"A2\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"MASS_OR_TECHNICAL_PLURAL\",\"source_supported_grammar_observation\":\"Oxford records uncountable and plural use: in technical English data can take plural agreement; avoid rigid singular-only or plural-only rule.\",\"grammar_source_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/data\",\"grammar_source_locator\":\"111-128,163-175\",\"proposed_original_example_UNAPPROVED\":\"The researchers compared the data from two surveys.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"data ကို ယေဘုယျသုံးစွဲမှုတွင် uncountable အဖြစ်လည်း၊ နည်းပညာစာရေးသားမှုတွင် plural အဖြစ်လည်း သုံးနိုင်သည်။\"},\"police\":{\"level\":\"A2\",\"part_of_speech\":\"plural noun\",\"grammar_risk\":\"PLURAL_ONLY_AGREEMENT\",\"source_supported_grammar_observation\":\"Police referring to the organisation/officers is grammatically plural; the police are, not the police is.\",\"grammar_source_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/police_1\",\"grammar_source_locator\":\"103-113\",\"proposed_original_example_UNAPPROVED\":\"The police are investigating the reported theft.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"the police ကို ရဲတပ်ဖွဲ့/ရဲအရာရှိများအဖြစ် သုံးလျှင် plural verb နှင့်တွဲသုံးသည်။\"},\"news\":{\"level\":\"A2\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"UNCOUNTABLE_SINGULAR_AGREEMENT\",\"source_supported_grammar_observation\":\"News is uncountable and takes a singular verb despite final -s; not the news are.\",\"grammar_source_url\":\"https://www.oxfordonlineenglish.com/uncountable-nouns\",\"grammar_source_locator\":\"491-520\",\"proposed_original_example_UNAPPROVED\":\"The news is encouraging this morning.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"news သည် -s ဖြင့်ဆုံးသော်လည်း singular verb နှင့်တွဲသုံးရသော uncountable noun ဖြစ်သည်။\"},\"experience\":{\"level\":\"A2\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"UNCOUNTABLE_SKILL_VS_COUNTABLE_EVENT\",\"source_supported_grammar_observation\":\"The frozen skill/knowledge sense is uncountable; a particular event is countable. Do not substitute event meaning.\",\"grammar_source_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/experience_1\",\"grammar_source_locator\":\"107-115,187-202\",\"proposed_original_example_UNAPPROVED\":\"She has several years of experience in warehouse operations.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"အလုပ်လုပ်ကိုင်၍ရရှိသည့် အတွေ့အကြုံသည် uncountable ဖြစ်ပြီး သီးခြားကြုံတွေ့မှုတစ်ခုကို an experience ဟု သုံးနိုင်သည်။\"},\"analysis\":{\"level\":\"B1\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"COUNTABLE_OR_UNCOUNTABLE_IRREGULAR_PLURAL\",\"source_supported_grammar_observation\":\"Oxford marks the study/result sense both countable and uncountable; plural is analyses, not analysises; do not treat topic badge as headword CEFR.\",\"grammar_source_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/analysis\",\"grammar_source_locator\":\"103-124,138-138\",\"proposed_original_example_UNAPPROVED\":\"The report includes an analysis of the results.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"analysis ကို ရေတွက်နိုင်/မရေတွက်နိုင် နှစ်မျိုးသုံးနိုင်ပြီး plural သည် analyses ဖြစ်သည်။\"},\"advice\":{\"level\":\"B1\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"UNCOUNTABLE_ADVICE\",\"source_supported_grammar_observation\":\"Advice is uncountable; some advice or a piece of advice, not an advice.\",\"grammar_source_url\":\"https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/uncount-nouns\",\"grammar_source_locator\":\"13-16,23-46\",\"proposed_original_example_UNAPPROVED\":\"The trainer offered some practical advice.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"advice ကို uncountable noun အဖြစ် သုံးပြီး အကြံပြုချက်တစ်ခုကို a piece of advice ဟု ဖော်ပြနိုင်သည်။\"},\"equipment\":{\"level\":\"B1\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"UNCOUNTABLE_EQUIPMENT\",\"source_supported_grammar_observation\":\"Equipment is uncountable; count items or pieces, not equipments.\",\"grammar_source_url\":\"https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/uncount-nouns\",\"grammar_source_locator\":\"23-46\",\"proposed_original_example_UNAPPROVED\":\"The laboratory needs two new pieces of equipment.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"equipment ကို uncountable noun အဖြစ် သုံးပြီး ပစ္စည်းအရေအတွက်ကို pieces of equipment ဟု ဖော်ပြနိုင်သည်။\"},\"traffic\":{\"level\":\"B1\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"UNCOUNTABLE_TRAFFIC\",\"source_supported_grammar_observation\":\"Traffic in road-vehicle sense is uncountable; a traffic is not idiomatic, and traffic jams count separate events.\",\"grammar_source_url\":\"https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/uncount-nouns\",\"grammar_source_locator\":\"23-29,48-51\",\"proposed_original_example_UNAPPROVED\":\"Heavy traffic is slowing the delivery vehicles.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"ယာဉ်အသွားအလာအဓိပ္ပာယ်ရှိသော traffic သည် uncountable ဖြစ်ပြီး ပိတ်ဆို့မှုတစ်ခုကို a traffic jam ဟု ခွဲဖော်ပြသည်။\"},\"progress\":{\"level\":\"B1\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"UNCOUNTABLE_IMPROVEMENT\",\"source_supported_grammar_observation\":\"Progress meaning advancement is normally uncountable; make progress, not a progress or progresses for ordinary improvement.\",\"grammar_source_url\":\"https://dictionaryblog.cambridge.org/2018/03/21/countable-or-uncountable-and-why-it-matters/\",\"grammar_source_locator\":\"11-25\",\"proposed_original_example_UNAPPROVED\":\"The students have made steady progress.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"တိုးတက်မှုအဓိပ္ပာယ်ရှိသော progress ကို uncountable noun အဖြစ် သုံးပြီး make progress ဟု တွဲသုံးသည်။\"},\"diagnosis\":{\"level\":\"C1\",\"part_of_speech\":\"noun\",\"grammar_risk\":\"COUNTABLE_OR_UNCOUNTABLE_IRREGULAR_PLURAL\",\"source_supported_grammar_observation\":\"Oxford marks the illness/problem identification sense countable and uncountable; plural diagnoses, not diagnosises; healthcare c1 is a topic badge, not independent exact-sense CEFR evidence.\",\"grammar_source_url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/diagnosis\",\"grammar_source_locator\":\"103-132\",\"proposed_original_example_UNAPPROVED\":\"The doctor confirmed the diagnosis after further tests.\",\"proposed_myanmar_teaching_note_UNAPPROVED\":\"diagnosis ကို countable/uncountable နှစ်မျိုးသုံးနိုင်ပြီး plural သည် diagnoses ဖြစ်သည်။\"}}")
ORIGINAL = {
    "original_english_definition": "english_definition",
    "original_burmese_meaning": "burmese_meaning",
    "original_example_sentence": "example_sentence",
    "source_path": "source_path",
    "source_index": "source_index",
    "source_blob_sha": "source_blob_sha",
}
SOURCE_FIELDS = (
    "level", "part_of_speech", "grammar_risk",
    "source_supported_grammar_observation", "grammar_source_url",
    "grammar_source_locator", "proposed_original_example_UNAPPROVED",
    "proposed_myanmar_teaching_note_UNAPPROVED",
)
EXPECTED_KEYS = set(ORIGINAL) | set(SOURCE_FIELDS) | {
    "word", "grammar_source_access", "observed_on",
    "example_assessment", "cefr_evidence_scope",
    "independently_checked", "release_approved",
    "actual_audio_listened", "editorial_hold",
}

def validate(packet, shortlist, level="ALL"):
    issues = []
    def need(condition, reason):
        if not condition:
            issues.append(reason)
    need(packet.get("schema") == 1, "schema")
    need(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY", "scope")
    need(packet.get("status") == "SOURCE_BOUND_NOUN_COUNTABILITY_AND_AGREEMENT_TRIAGE_UNAPPROVED", "status")
    need(packet.get("observed_on") == "2026-11-01", "observation date")
    need(packet.get("shortlist_blob_sha") == FROZEN_SHA, "frozen shortlist blob")
    need(packet.get("source_method") == "DIRECTLY_OPENED_GRAMMAR_OR_DICTIONARY_PAGES_NO_EXACT_SENSE_CEFR_INFERENCE", "source method")
    need(packet.get("counts_by_level") == {"A1": 1, "A2": 5, "B1": 5, "B2": 0, "C1": 1}, "level counts")
    need(type(packet.get("independent_approvals")) is int and packet["independent_approvals"] == 0, "false independent approval")
    need(type(packet.get("real_audio_listening_signoffs")) is int and packet["real_audio_listening_signoffs"] == 0, "false listening")
    need(packet.get("production_status") == "BLOCKED_STAGING_ONLY", "production status")
    entries = shortlist.get("entries", [])
    need(len(entries) == 1000, "frozen 1000 total")
    need(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "frozen approval counts")
    frozen = {r["word"]: r for r in entries if isinstance(r, dict) and "word" in r}
    records = packet.get("records", [])
    if not isinstance(records, list):
        return issues + ["records must be a list"]
    need(len(records) == 12, "exact 12 records")
    words = [r.get("word") for r in records if isinstance(r, dict)]
    need(len(words) == len(set(words)) and set(words) == set(EXPECTED), "deduplicated exact record set")
    need({l: sum(1 for r in records if isinstance(r, dict) and r.get("level") == l) for l in LEVELS}
         == {"A1": 1, "A2": 5, "B1": 5, "B2": 0, "C1": 1}, "derived level counts")
    for r in records:
        if not isinstance(r, dict) or r.get("word") not in EXPECTED:
            need(False, "unknown or malformed record")
            continue
        word = r["word"]
        if level != "ALL" and r.get("level") != level:
            continue
        need(set(r) == EXPECTED_KEYS, word + ": exact field set (no hidden approval/CEFR fields)")
        for field in SOURCE_FIELDS:
            need(r.get(field) == EXPECTED[word][field], word + ": source-bound " + field)
        original = frozen.get(word)
        need(original is not None, word + ": frozen shortlist entry exists")
        if original is not None:
            for field, original_field in ORIGINAL.items():
                need(r.get(field) == original.get(original_field), word + ": frozen " + field)
            need(r.get("part_of_speech") == original.get("part_of_speech"), word + ": original POS")
            need(r.get("level") == original.get("level"), word + ": original level")
            need(original.get("editorial_hold") is True and original.get("release_approved") is False,
                 word + ": shortlist remains on editorial hold")
        need(r.get("grammar_source_access") == "DIRECT_PAGE_OPENED", word + ": direct access")
        need(r.get("observed_on") == "2026-11-01", word + ": observed date")
        need(r.get("example_assessment") == "NO_DEMONSTRATED_ERROR_IN_FROZEN_EXAMPLE_REVIEW_STILL_REQUIRED",
             word + ": no invented example error")
        need(r.get("cefr_evidence_scope") == "GRAMMAR_ONLY_NOT_EXACT_SENSE_CEFR",
             word + ": grammar is not CEFR")
        need(r.get("independently_checked") is False and r.get("release_approved") is False
             and r.get("actual_audio_listened") is False and r.get("editorial_hold") is True,
             word + ": no forged signoff")
        need(r.get("grammar_source_url", "").startswith("https://"), word + ": source URL")
    return issues

def self_test(packet, shortlist):
    n = 0
    def reject(bad, label):
        nonlocal n
        if not validate(bad, shortlist):
            raise AssertionError("forged mutation accepted: " + label)
        n += 1
    for i, record in enumerate(packet["records"]):
        for field in record:
            bad = copy.deepcopy(packet)
            value = bad["records"][i][field]
            if type(value) is bool:
                bad["records"][i][field] = not value
            elif type(value) is int:
                bad["records"][i][field] = value + 1
            else:
                bad["records"][i][field] = str(value) + " FORGED"
            reject(bad, record["word"] + "." + field)
        bad = copy.deepcopy(packet)
        bad["records"][i]["reviewer_receipt"] = {"result": "PASS"}
        reject(bad, record["word"] + ".forged-extra-approval")
        bad = copy.deepcopy(packet)
        del bad["records"][i]
        reject(bad, record["word"] + ".deleted")
        bad = copy.deepcopy(packet)
        bad["records"][i] = copy.deepcopy(bad["records"][(i + 1) % len(bad["records"])])
        reject(bad, record["word"] + ".duplicated")
    for field in packet:
        if field == "records":
            continue
        bad = copy.deepcopy(packet)
        v = bad[field]
        if type(v) is int:
            bad[field] = v + 1
        elif type(v) is str:
            bad[field] = v + " FORGED"
        elif isinstance(v, dict):
            bad[field] = {}
        reject(bad, "top-level." + field)
    bad = copy.deepcopy(packet)
    bad["source_cefr_level"] = "C1"
    reject(bad, "forged-top-level-CEFR")
    return n

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("ALL",) + LEVELS, default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    issues = validate(packet, shortlist, args.level)
    if issues:
        print(json.dumps({"result": "FAIL", "issues": issues[:30]}, ensure_ascii=False))
        return 1
    mutations = self_test(packet, shortlist) if args.self_test else 0
    print(json.dumps({
        "result": "PASS_SOURCE_BOUND_GRAMMAR_RESEARCH_ONLY",
        "level": args.level, "records": 12, "counts_by_level": packet["counts_by_level"],
        "adversarial_mutations_rejected": mutations,
        "independently_approved": 0, "actual_audio_listening": 0,
        "deployment": "BLOCKED_STAGING_ONLY"
    }, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
