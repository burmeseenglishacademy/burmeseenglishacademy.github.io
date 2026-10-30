#!/usr/bin/env python3
"""Source-bound C1 tenth Oxford publisher evidence auditor; NOT independent review."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-OXFORD-C1-TENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
OBS = json.loads(r'''[["preserve","B2",12,3088,"preserve v.",3000,"Museum photograph preservation, not food preservation or preservation of abstract qualities."],["productive","C1",6,1627,"productive adj.",5000,"Useful results from discussion, not farming or industrial production."],["permit","B2",12,3064,"permit v., n.",3000,"Official document noun, not the verb allow; different British stress requires real listening."],["demonstrate","B2",11,2775,"demonstrate v.",3000,"Proving a theory with evidence, not a public protest or a product demonstration."],["nonetheless","C1",6,1512,"nonetheless adv.",5000,"Formal contrast adverb after semicolon, not a causal connector."],["cease","C1",4,888,"cease v.",5000,"Ceasing factory operations, not a brief pause; review formal register."],["adaptation","C1",3,732,"adaptation n.",5000,"Course adjustment to suit learners, not film or biological adaptation."],["evaluate","B2",11,2831,"evaluate v.",3000,"Evidence-based assessment of research results, not merely describing results."],["emphasis","B2",11,2814,"emphasis n.",3000,"Giving workplace safety particular importance, not stress in pronunciation."],["coastal","B2",4,912,"coastal adj.",5000,"Communities near the sea, not necessarily holiday resorts."],["resist","B2",12,3141,"resist v.",3000,"Refusing pressure, not electrical resistance or armed opposition."],["gradually","B2",11,2894,"gradually adv.",3000,"Slow change over time, not repeated or sudden change."]]''')
LEADS = json.loads(r'''[{"word":"preserve","url":"https://www.oxfordlearnersdictionaries.com/definition/english/preserve_1","part_of_speech":"verb","sense_number":2,"page_text_line_start":148,"page_text_line_end":163,"interpretation":"Keeping historic photographs in good condition rather than preserving a quality or food.","observed_on":"2026-10-30","scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},{"word":"productive","url":"https://www.oxfordlearnersdictionaries.com/definition/english/productive","part_of_speech":"adjective","sense_number":2,"page_text_line_start":139,"page_text_line_end":150,"interpretation":"A useful discussion yielding results, not production output.","observed_on":"2026-10-30","scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},{"word":"permit","url":"https://www.oxfordlearnersdictionaries.com/definition/english/permit_2","part_of_speech":"noun","sense_number":1,"page_text_line_start":88,"page_text_line_end":110,"interpretation":"Official document, not the verb permit; noun pronunciation requires listening.","observed_on":"2026-10-30","scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},{"word":"adaptation","url":"https://www.oxfordlearnersdictionaries.com/definition/english/adaptation","part_of_speech":"noun","sense_number":1,"page_text_line_start":115,"page_text_line_end":139,"interpretation":"Course modification, not film adaptation or biological adjustment.","observed_on":"2026-10-30","scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}]''')
SUGGESTIONS = json.loads(r'''[{"word":"preserve","proposed_myanmar":"မူလအခြေအနေ မပျက်စီးစေရန် ထိန်းသိမ်းထားသည်","proposed_example":"The archive uses special storage to preserve old photographs.","status":"EDITORIAL_PROPOSAL_NOT_INDEPENDENTLY_REVIEWED"},{"word":"productive","proposed_myanmar":"ဆွေးနွေးမှုမှ အသုံးဝင်သည့် ရလဒ်များ ထွက်ပေါ်စေသော","proposed_example":"The meeting was productive because the team agreed on a clear plan.","status":"EDITORIAL_PROPOSAL_NOT_INDEPENDENTLY_REVIEWED"},{"word":"permit","proposed_myanmar":"လုပ်ငန်းတစ်ခု ဆောင်ရွက်ရန် ထုတ်ပေးထားသည့် တရားဝင်ခွင့်ပြုလက်မှတ်","proposed_example":"The builder applied for a permit before construction began.","status":"EDITORIAL_PROPOSAL_NOT_INDEPENDENTLY_REVIEWED"},{"word":"adaptation","proposed_myanmar":"အခြေအနေအသစ်နှင့် ကိုက်ညီစေရန် ပြုပြင်ပြောင်းလဲမှု","proposed_example":"The adaptation of the lessons made them easier for beginners to follow.","status":"EDITORIAL_PROPOSAL_NOT_INDEPENDENTLY_REVIEWED"}]''')
TASK = "Independent human reviewer must check dated exact-sense publisher CEFR evidence, English definition, fluent Myanmar meaning, original example grammar and collocation, British pronunciation, cross-level justification and historical Git provenance; issue a content-bound independent receipt. Word/POS PDF and assistant editorial suggestions do not approve the entry."
LIMITATIONS = "Direct Oxford 3000/5000 PDF word/POS evidence observed 2026-10-30 is NOT independently verified exact-sense CEFR approval. Four directly opened dictionary pages are editorial sense leads only. No independent English/Myanmar/example signoff, real George/Emma listening, physical iPhone Safari, hosting readiness or production deployment. Frozen shortlist unchanged."
URLS = json.loads(r'''{"3000":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","5000":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"}''')
LEVELS = ("A1","A2","B1","B2","C1")

def require(condition, message):
    if not condition:
        raise ValueError(message)

def canonical(shortlist):
    entries = shortlist["entries"]
    by = {e["word"]: e for e in entries}
    require(len(entries) == len(by) == 1000, "Duplicate/missing frozen shortlist headwords")
    records = []
    for word, cefr, page, line, excerpt, source_list, risk in OBS:
        require(word in by and by[word]["level"] == "C1", "Wrong source level: " + word)
        e = by[word]
        records.append({
            "word":word,"level":"C1","part_of_speech":e["part_of_speech"],
            "shortlist_snapshot":{"english_definition":e["english_definition"],
                "myanmar_meaning":e["burmese_meaning"],"example_sentence":e["example_sentence"]},
            "shortlist_provenance":{"source_path":e["source_path"],"source_index":e["source_index"],
                "source_blob_sha":e["source_blob_sha"]},
            "publisher_source":{"publisher":"Oxford University Press",
                "title":"The Oxford " + str(source_list) + " by CEFR level",
                "url":URLS[str(source_list)],"observed_on":"2026-10-30",
                "pdf_page":page,"extracted_line":line,"source_excerpt":excerpt,
                "source_cefr_level":cefr,"evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
            "editorial_risk":risk,"independent_reviewer_task":TASK,
            "editorial_hold":True,"independently_reviewed":False,
            "release_approved":False,"independent_reviewer_receipt":None})
    return {"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY",
        "status":"C1_TENTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD",
        "observed_on":"2026-10-30","shortlist_blob_sha":SHORT_SHA,"record_count":12,
        "counts_by_level":{"A1":0,"A2":0,"B1":0,"B2":0,"C1":12},
        "publisher_reference_level_counts":{"B2":8,"C1":4},
        "word_pos_discrepancies":8,"direct_dictionary_sense_leads":LEADS,
        "unapproved_editorial_suggestions":SUGGESTIONS,
        "independently_approved_count":0,"independent_human_review_receipts":[],
        "audio_real_listening_signoffs":[],"release_approved":False,
        "source_limitations":LIMITATIONS,"records":records}

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    actual = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(actual == SHORT_SHA, "Frozen shortlist Git blob drift")
    require(shortlist.get("counts_by_level") == {level:200 for level in LEVELS}
        and shortlist.get("independently_approved_by_level") == {level:0 for level in LEVELS}
        and len(shortlist.get("entries",[])) == 1000, "Scope/independent approval drift")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
        and all(e.get("reviewed_"+k) is False for k in
            ("english","burmese","example","level","pronunciation"))
        for e in shortlist["entries"]), "False shortlist review/approval")
    require(packet == canonical(shortlist),
        "Source/locator, snapshot, provenance, dictionary sense, reviewer or approval drift")
    return {"C1_written":200,"C1_independently_approved":0,
        "new_word_pos_observations":12,"publisher_B2":8,"publisher_C1":4,
        "dictionary_sense_leads":4,"real_listening_signoffs":0,
        "release":"BLOCKED_STAGING_ONLY"}

def leaves(obj, path=()):
    if isinstance(obj,dict):
        for k,v in obj.items():
            yield from leaves(v,path+(k,))
    elif isinstance(obj,list):
        if not obj:
            yield path
        else:
            for i,v in enumerate(obj):
                yield from leaves(v,path+(i,))
    else:
        yield path

def forge(v):
    if v is None: return "FAKE_RECEIPT"
    if isinstance(v,bool): return not v
    if isinstance(v,int): return v+1
    if isinstance(v,str): return v+" [FAKE]"
    return "FAKE"

def self_test(packet,shortlist):
    audit(packet,shortlist)
    n=0
    for path in leaves(packet):
        bad=copy.deepcopy(packet)
        target=bad
        for key in path[:-1]:
            target=target[key]
        key=path[-1]
        if isinstance(target[key],list) and not target[key]:
            target[key].append({"fake":True})
        else:
            target[key]=forge(target[key])
        try:
            audit(bad,shortlist)
        except ValueError:
            n+=1
        else:
            raise ValueError("Fail-open forged path: "+str(path))
    for k in ("records","direct_dictionary_sense_leads",
              "unapproved_editorial_suggestions","independent_human_review_receipts",
              "audio_real_listening_signoffs"):
        bad=copy.deepcopy(packet)
        bad[k].append({"fake":True})
        try:
            audit(bad,shortlist)
        except ValueError:
            n+=1
        else:
            raise ValueError("Fail-open forged append: "+k)
    require(n>=280,"Insufficient mutation cases")
    return n

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    shortlist=json.loads(SHORT.read_text(encoding="utf-8"))
    packet=json.loads(PACKET.read_text(encoding="utf-8"))
    result=audit(packet,shortlist)
    if args.self_test:
        result["adversarial_mutations_rejected"]=self_test(packet,shortlist)
    result["matrix_level"]=args.level
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))
if __name__=="__main__":
    main()
