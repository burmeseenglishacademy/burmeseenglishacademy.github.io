#!/usr/bin/env python3
"""Fail-closed A1 five-entry morphology / rabbit CEFR research quarantine.

Research observations are NOT independent human CEFR, Myanmar, example,
audio-listening, iPhone, hosting or deployment signoffs. Staging only.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import audit_cefr_1000_oxford_coverage as oxford

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-A1-FIVE-REMAINING-MORPHOLOGY-AND-RABBIT-SENSE-QUARANTINE-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
EXPECTED = json.loads(r'''{"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY","status":"A1_FIVE_REMAINING_UNOBSERVED_HEADWORDS_MORPHOLOGY_AND_CEFR_QUARANTINE","observed_on":"2026-10-30","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","record_count":5,"first_pass_written_by_level":{"A1":200,"A2":200,"B1":200,"B2":200,"C1":200},"independently_approved_by_level":{"A1":0,"A2":0,"B1":0,"B2":0,"C1":0},"oxford_word_pos_distinct_a1":195,"remaining_without_direct_oxford_word_pos":["is","are","does","did","rabbit"],"morphology_variants_count":4,"cambridge_a2_rabbit_sense_count":1,"source_limitations":"Cambridge grammar identifies inflections, not separate Oxford core-list CEFR headwords. Cambridge A2 rabbit is a dictionary exact-sense label and Oxford Animals a2 is a topic label, not independent CEFR approval. No independent review, real listening, physical iPhone QA or production deployment. Frozen shortlist unchanged.","records":[{"word":"is","level":"A1","part_of_speech":"verb","shortlist_snapshot":{"english_definition":"The present form of be used with he, she, it or a singular subject.","myanmar_meaning":"ဖြစ်တယ်၊ ရှိတယ် (အနည်းကိန်းနှင့်တွဲသုံး)","example_sentence":"She is at home."},"shortlist_provenance":{"source_path":"draft/A1-EDITORIAL-STARTER.json","source_index":120,"source_blob_sha":"ff1e93f60828ef2f94c9146522ce94075183b0ae"},"morphology_or_sense":{"canonical_lemma":"be","source_cefr_level":null,"evidence_kind":"INFLECTED_FORM_NOT_INDEPENDENT_LEMMA"},"publisher_observation":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/grammar/british-grammar/be-","observed_on":"2026-10-30","source_excerpt_summary":"Cambridge English Grammar Today: present forms of be include (he/she/it) is and (you/we/they) are.","evidence_scope":"DIRECT_PUBLISHER_GRAMMAR_OR_DICTIONARY_NOT_INDEPENDENT_APPROVAL"},"editorial_risk":"The A1 shortlist counts is as a separate headword although be is already present; grammatical inflection is not an independently CEFR-classified lexical headword. Example She is at home is grammatical; Myanmar sense must distinguish location from identity. Human reviewer must decide grammar card versus lexical item.","independent_reviewer_task":"Independent human reviewer must resolve lexical-lemma versus grammar-form counting, exact sense and CEFR suitability, fluent Myanmar and example grammar, British pronunciation, and record content-bound signoff before any release; automated research is not independent review.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"are","level":"A1","part_of_speech":"verb","shortlist_snapshot":{"english_definition":"The present form of be used with you, we, they or plural subjects.","myanmar_meaning":"ဖြစ်တယ်၊ ရှိတယ် (အများကိန်းနှင့်တွဲသုံး)","example_sentence":"They are friends."},"shortlist_provenance":{"source_path":"draft/A1-EDITORIAL-STARTER.json","source_index":121,"source_blob_sha":"ff1e93f60828ef2f94c9146522ce94075183b0ae"},"morphology_or_sense":{"canonical_lemma":"be","source_cefr_level":null,"evidence_kind":"INFLECTED_FORM_NOT_INDEPENDENT_LEMMA"},"publisher_observation":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/grammar/british-grammar/be-","observed_on":"2026-10-30","source_excerpt_summary":"Cambridge English Grammar Today: present forms of be include (he/she/it) is and (you/we/they) are.","evidence_scope":"DIRECT_PUBLISHER_GRAMMAR_OR_DICTIONARY_NOT_INDEPENDENT_APPROVAL"},"editorial_risk":"The A1 shortlist counts are separately despite existing be and is cards; plural subject agreement is grammar, not a distinct Oxford headword/POS observation. They are friends is grammatical; Myanmar translation must not imply that are always signals plural.","independent_reviewer_task":"Independent human reviewer must resolve lexical-lemma versus grammar-form counting, exact sense and CEFR suitability, fluent Myanmar and example grammar, British pronunciation, and record content-bound signoff before any release; automated research is not independent review.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"does","level":"A1","part_of_speech":"auxiliary verb","shortlist_snapshot":{"english_definition":"The present form of do used with he, she or it in questions and negatives.","myanmar_meaning":"မေးခွန်းနှင့် အငြင်းဝါကျတွင် သုံးသော do ၏ အနည်းကိန်းပုံစံ","example_sentence":"Does he work here?"},"shortlist_provenance":{"source_path":"draft/A1-EDITORIAL-STARTER.json","source_index":123,"source_blob_sha":"ff1e93f60828ef2f94c9146522ce94075183b0ae"},"morphology_or_sense":{"canonical_lemma":"do","source_cefr_level":null,"evidence_kind":"INFLECTED_AUXILIARY_NOT_INDEPENDENT_LEMMA"},"publisher_observation":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/grammar/british-grammar/do","observed_on":"2026-10-30","source_excerpt_summary":"Cambridge English Grammar Today: does is the present simple third-person singular form of do; auxiliary does forms questions and negatives.","evidence_scope":"DIRECT_PUBLISHER_GRAMMAR_OR_DICTIONARY_NOT_INDEPENDENT_APPROVAL"},"editorial_risk":"A1 does is an auxiliary inflection of do already listed in A1, not a distinct Oxford lexical headword. Does he work here? is grammatical; review Burmese description and avoid counting inflection as a new lexical sense.","independent_reviewer_task":"Independent human reviewer must resolve lexical-lemma versus grammar-form counting, exact sense and CEFR suitability, fluent Myanmar and example grammar, British pronunciation, and record content-bound signoff before any release; automated research is not independent review.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"did","level":"A1","part_of_speech":"auxiliary verb","shortlist_snapshot":{"english_definition":"The past form of do used in questions and negatives.","myanmar_meaning":"အတိတ်ကာလ မေးခွန်းတွင် သုံးသော do ၏ ပုံစံ","example_sentence":"Did you eat breakfast?"},"shortlist_provenance":{"source_path":"draft/A1-EDITORIAL-STARTER.json","source_index":124,"source_blob_sha":"ff1e93f60828ef2f94c9146522ce94075183b0ae"},"morphology_or_sense":{"canonical_lemma":"do","source_cefr_level":null,"evidence_kind":"INFLECTED_AUXILIARY_NOT_INDEPENDENT_LEMMA"},"publisher_observation":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/grammar/british-grammar/do","observed_on":"2026-10-30","source_excerpt_summary":"Cambridge English Grammar Today: did is the past form of do, used as auxiliary in questions and negatives.","evidence_scope":"DIRECT_PUBLISHER_GRAMMAR_OR_DICTIONARY_NOT_INDEPENDENT_APPROVAL"},"editorial_risk":"A1 did is the past auxiliary form of do, already present; Did you eat breakfast? is grammatical but the Myanmar meaning omits negative usage. This is a morphology/grammar card, not an independent CEFR lexical headword.","independent_reviewer_task":"Independent human reviewer must resolve lexical-lemma versus grammar-form counting, exact sense and CEFR suitability, fluent Myanmar and example grammar, British pronunciation, and record content-bound signoff before any release; automated research is not independent review.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"rabbit","level":"A1","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"A small animal with long ears.","myanmar_meaning":"ယုန်","example_sentence":"The rabbit is white."},"shortlist_provenance":{"source_path":"draft/A1-EDITORIAL-STARTER.json","source_index":186,"source_blob_sha":"ff1e93f60828ef2f94c9146522ce94075183b0ae"},"morphology_or_sense":{"canonical_lemma":"rabbit","source_cefr_level":"A2","evidence_kind":"DIRECT_DICTIONARY_SENSE_LABEL_NOT_OXFORD_CORE_LIST"},"publisher_observation":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/dictionary/english/rabbit","observed_on":"2026-10-30","source_excerpt_summary":"Cambridge English Dictionary: rabbit noun, A2, animal with long ears; example and intended A1 draft use the animal sense.","evidence_scope":"DIRECT_PUBLISHER_GRAMMAR_OR_DICTIONARY_NOT_INDEPENDENT_APPROVAL"},"editorial_risk":"Provisional A1 rabbit animal sense conflicts with Cambridge's A2 dictionary sense label; Oxford Learner's Dictionary Animals topic is A2, but a topic label is not Oxford core-list word/POS CEFR. Independent reviewer must decide A1 pedagogical rationale or replacement; do not silently retier.","independent_reviewer_task":"Independent human reviewer must resolve lexical-lemma versus grammar-form counting, exact sense and CEFR suitability, fluent Myanmar and example grammar, British pronunciation, and record content-bound signoff before any release; automated research is not independent review.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null}],"independent_human_review_receipts":[],"real_audio_listening_receipts":[],"release_approved":false}''')
LEVELS = ("A1", "A2", "B1", "B2", "C1")
NAMES = ("is", "are", "does", "did", "rabbit")

def need(condition, why):
    if not condition:
        raise ValueError(why)

def audit(packet, shortlist, check_oxford=True):
    # Freeze the original 1000 first-pass entries and all their review holds.
    raw = SHORT.read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()
    need(sha == SHORT_SHA, "Frozen shortlist Git blob SHA changed")
    need(shortlist.get("counts_by_level") == {x:200 for x in LEVELS}
         and shortlist.get("independently_approved_by_level") == {x:0 for x in LEVELS},
         "Scope or independent approvals drift")
    entries = shortlist.get("entries", [])
    need(len(entries) == 1000 and len({x["word"] for x in entries}) == 1000,
         "1000 unique provisional headwords required")
    need(all(x.get("editorial_hold") is True and x.get("release_approved") is False
             and all(x.get("reviewed_" + k) is False for k in
                     ("english", "burmese", "example", "level", "pronunciation"))
             for x in entries), "Forged shortlist approval")
    by_word = {x["word"]: x for x in entries}
    need(packet == EXPECTED, "Immutable publisher research, source or quarantine data drift")
    need(all(by_word[x]["level"] == "A1" for x in ("be","do",*NAMES)),
         "Lemma family is not anchored to A1")
    for row in packet["records"]:
        source = by_word[row["word"]]
        need(row["shortlist_snapshot"] == {
             "english_definition":source["english_definition"],
             "myanmar_meaning":source["burmese_meaning"],
             "example_sentence":source["example_sentence"]},
             "Original bilingual and example snapshot changed")
        need(row["shortlist_provenance"] == {k:source[k] for k in
             ("source_path","source_index","source_blob_sha")},
             "Historical source Git provenance changed")
        need(row["part_of_speech"] == source["part_of_speech"]
             and row["level"] == source["level"], "Part of speech or level drift")
        need(row["editorial_hold"] is True and row["independently_reviewed"] is False
             and row["release_approved"] is False
             and row["independent_reviewer_receipt"] is None,
             "Fake independent review receipt")
    if check_oxford:
        # Oxford core-list observations must not be misreported as five CEFR approvals.
        # Cross-packet auditor separately validates actual publisher locators and excerpts.
        original, packets = oxford.load()
        coverage = oxford.audit(original, packets)
        observed_a1 = {r["word"] for name in oxford.PACKETS["A1"]
                       for r in packets[oxford.PREFIX + name + ".json"]["records"]}
        missing = sorted(set(x["word"] for x in entries if x["level"]=="A1") - observed_a1)
        need(missing == sorted(NAMES) and coverage["by_level"]["A1"]["distinct"] == 195,
             "Oxford A1 five-entry unresolved set changed")
    return {"scope":"STAGING_ONLY_NOT_INDEPENDENT_APPROVAL",
            "A1_first_pass_written":200,"A1_independently_approved":0,
            "Oxford_A1_word_pos_observed":195,
            "A1_without_Oxford_word_pos":5,
            "grammar_inflection_quarantines":4,
            "Cambridge_rabbit_A2_sense_conflicts":1,
            "final_audio_listening_signoffs":0,"release":"BLOCKED_STAGING_ONLY"}

def leaf_paths(obj, path=()):
    if isinstance(obj,dict):
        for k,v in obj.items():
            yield from leaf_paths(v,path+(k,))
    elif isinstance(obj,list):
        for i,v in enumerate(obj):
            yield from leaf_paths(v,path+(i,))
    else:
        yield path

def mutate_leaf(obj,path):
    p=obj
    for k in path[:-1]:
        p=p[k]
    k=path[-1]
    v=p[k]
    p[k] = (not v) if isinstance(v,bool) else (
        999 if isinstance(v,int) else ("FORGED" if v is None or isinstance(v,str) else None))

def self_test(packet,shortlist):
    baseline=audit(packet,shortlist)
    paths=list(leaf_paths(packet))
    # Every scalar source URL, date, exact excerpt summary, lemma mapping, bilingual
    # snapshot, provenance, hold, count and approval must be bound to source.
    for path in paths:
        forged=copy.deepcopy(packet)
        mutate_leaf(forged,path)
        need(forged != packet, "Ineffective mutation")
        try:
            audit(forged,shortlist,check_oxford=False)
        except ValueError:
            continue
        raise AssertionError("Forged source/approval accepted: " + repr(path))
    for label,modify in [
        ("missing row",lambda x:x["records"].pop()),
        ("duplicate row",lambda x:x["records"].append(copy.deepcopy(x["records"][0]))),
        ("false independent approval",lambda x:x.update(release_approved=True)),
        ("false audio receipt",lambda x:x["real_audio_listening_receipts"].append({"fake":True})),
        ("fake human receipt",lambda x:x["independent_human_review_receipts"].append({"fake":True})),
    ]:
        forged=copy.deepcopy(packet)
        modify(forged)
        try:
            audit(forged,shortlist,check_oxford=False)
        except ValueError:
            continue
        raise AssertionError("Forged quarantine accepted: " + label)
    return baseline,len(paths)+5

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    packet=json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist=json.loads(SHORT.read_text(encoding="utf-8"))
    if args.self_test:
        report,n=self_test(packet,shortlist)
        print("PASS: rejected %d/%d A1 morphology, Cambridge, bilingual and fake-signoff mutations" % (n,n))
    else:
        report=audit(packet,shortlist)
    if args.level in ("A1","ALL"):
        print(json.dumps(report,sort_keys=True))
    else:
        print(json.dumps({"level":args.level,"A1_quarantine":True,
                          "release":"BLOCKED_STAGING_ONLY"},sort_keys=True))

if __name__=="__main__":
    main()
