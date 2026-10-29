#!/usr/bin/env python3
"""Audit four directly opened Oxford B2 sense leads; no independent human or CEFR signoff."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-SIXTH-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
WORD_POS = ROOT / "draft/CEFR-1000-OXFORD-B2-SIXTH-TWELVE-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
EXPECTED = json.loads(r'''[["principal","https://www.oxfordlearnersdictionaries.com/definition/english/principal_1","88-112","The intended adjective is used only before a noun; draft principal reason fits this construction. Distinguish principal noun and principle noun; dictionary displays Oxford 3000 B2 while 5000 PDF also lists B2, so list membership metadata differs without a level disagreement.","Adjective main/most important, pre-nominal; not school head noun or principle."],["monthly","https://www.oxfordlearnersdictionaries.com/definition/english/monthly_1","88-120","The first adjective sense is recurring every month and aligns with monthly meeting. Second adjective sense concerns monthly payments or calculation; do not conflate. Dictionary displays Oxford 3000 B2 while Oxford 5000 PDF also lists B2.","Recurring frequency adjective, not monthly salary/payment sense, adverb or noun."],["barely","https://www.oxfordlearnersdictionaries.com/definition/english/barely","88-147","Draft could barely hear aligns with first sense: hearing was only just possible with difficulty. Publisher separately lists approximate quantities and temporal barely; avoid double negatives and review Myanmar gloss for naturalness.","Only just able to hear; not barely 50% or barely started when."],["steam","https://www.oxfordlearnersdictionaries.com/definition/english/steam_1","88-174","Publisher distinguishes hot gaseous water, power produced from steam and condensed droplets on cold surfaces. Visible steam rising from soup can involve condensed droplets; reviewer should choose a precise learner-friendly definition and Burmese gloss.","Soup vapour/mist context; avoid conflating invisible water vapour, condensed droplets, steam power and idioms."]]''')
LEVELS = ("A1","A2","B1","B2","C1")

def need(ok, why):
    if not ok:
        raise ValueError(why)

def audit(packet, shortlist, wordpos):
    raw = SHORT.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    need(blob == SHORT_SHA, "Frozen shortlist Git blob changed")
    need(shortlist.get("counts_by_level") == {k:200 for k in LEVELS}
         and shortlist.get("independently_approved_by_level") == {k:0 for k in LEVELS}
         and len(shortlist.get("entries",[])) == 1000, "Scope or approval drift")
    need(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet.get("status") == "B2_SIXTH_FOUR_DIRECT_DICTIONARY_SENSE_LEADS_EDITORIAL_HOLD"
         and packet.get("observed_on") == "2026-10-30"
         and packet.get("shortlist_blob_sha") == SHORT_SHA
         and packet.get("linked_word_pos_packet") == "draft/CEFR-1000-OXFORD-B2-SIXTH-TWELVE-2026-10-30.json"
         and packet.get("record_count") == 4 and len(packet.get("records",[])) == 4
         and packet.get("independently_approved_count") == 0, "Packet scope/count/approval drift")
    need("not independently verified" in packet.get("source_limitations",""),
         "Source limitations incorrectly elevated to human approval")
    by_word = {r["word"]:r for r in shortlist["entries"]}
    by_wordpos = {r["word"]:r for r in wordpos["records"]}
    need(len(by_word)==1000 and len(by_wordpos)==12, "Frozen word/POS binding invalid")
    for row,(word,url,lines,finding,task) in zip(packet["records"],EXPECTED):
        original = by_word[word]
        need(row.get("word")==word and row.get("level")=="B2"
             and row.get("part_of_speech")==original["part_of_speech"],
             "Word/level/POS drift")
        snapshot = {"english_definition": original["english_definition"],
                    "myanmar_meaning": original["burmese_meaning"],
                    "example_sentence": original["example_sentence"]}
        provenance = {k:original[k] for k in ("source_path","source_index","source_blob_sha")}
        need(row.get("shortlist_snapshot")==snapshot,
             "Bilingual/example snapshot drift for " + word)
        need(row.get("shortlist_provenance")==provenance,
             "Historical provenance drift for " + word)
        need(by_wordpos[word]["shortlist_snapshot"]==snapshot
             and by_wordpos[word]["shortlist_provenance"]==provenance,
             "Sense lead not bound to Oxford word/POS packet")
        need(row.get("source")=={
             "publisher":"Oxford University Press","url":url,"observed_on":"2026-10-30",
             "web_text_lines":lines,"access":"DIRECT_OFFICIAL_DICTIONARY_WEB_PAGE",
             "evidence_scope":"SENSE_DISTINCTION_NOT_INDEPENDENT_CEFR_SIGNOFF"},
             "Dictionary URL/observation/line/scope changed")
        need(row.get("finding")==finding and row.get("independent_reviewer_task")==task,
             "Source-backed editorial finding/task changed")
        need(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
             and row.get("release_approved") is False
             and row.get("independent_reviewer_receipt") is None,
             "False independent approval")
    return True

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    packet=json.loads(PACKET.read_text("utf8"))
    shortlist=json.loads(SHORT.read_text("utf8"))
    wordpos=json.loads(WORD_POS.read_text("utf8"))
    audit(packet,shortlist,wordpos)
    rejected=0
    if args.self_test:
        cases=[
            ("word","fake"),("level","C1"),("part_of_speech","fake"),
            ("shortlist_snapshot",{"english_definition":"fake"}),
            ("shortlist_provenance",{"source_index":-1}),
            ("source",{"url":"https://example.org/forged"}),
            ("finding","fake"),("independent_reviewer_task","fake"),
            ("editorial_hold",False),("independently_reviewed",True),
            ("release_approved",True),("independent_reviewer_receipt",{"fake":True}),
        ]
        for i in range(4):
            for field,value in cases:
                test=copy.deepcopy(packet)
                need(test["records"][i][field]!=value,"Ineffective negative test")
                test["records"][i][field]=value
                try:
                    audit(test,shortlist,wordpos)
                except (ValueError,KeyError,TypeError):
                    rejected+=1
                else:
                    raise AssertionError("Forged sense source or approval accepted")
        for field,value in [
            ("record_count",3),("independently_approved_count",1),
            ("shortlist_blob_sha","0"*40),("observed_on","2026-10-29"),
            ("source_limitations","human approved")
        ]:
            test=copy.deepcopy(packet)
            need(test[field]!=value,"Ineffective metadata mutation")
            test[field]=value
            try:
                audit(test,shortlist,wordpos)
            except (ValueError,KeyError,TypeError):
                rejected+=1
            else:
                raise AssertionError("Forged sense metadata accepted")
        need(rejected==53,"Adversarial test count drift")
        print("PASS: rejected 53/53 forged direct sense source, Myanmar and approval mutations")
    print(json.dumps({"level":args.level,"direct_dictionary_sense_leads":4,
                      "independent_exact_sense_cefr_approvals":0,
                      "adversarial_mutations_rejected":rejected,
                      "release":"BLOCKED_STAGING_ONLY"},sort_keys=True))

if __name__=="__main__":
    main()
