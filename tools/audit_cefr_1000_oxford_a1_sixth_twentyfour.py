#!/usr/bin/env python3
"""Staging-only fail-closed A1 sixth Oxford batch integrity and disjoint-coverage audit.
Publisher PDF word/POS evidence is NOT exact-sense CEFR or human-independent signoff.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-SIXTH-TWENTYFOUR-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
PREVIOUS = ["CEFR-1000-OXFORD-A1-TWELVE-DIRECT-PDF-2026-10-28.json","CEFR-1000-OXFORD-A1-SECOND-TWELVE-2026-10-28.json","CEFR-1000-OXFORD-A1-THIRD-TWELVE-2026-10-28.json","CEFR-1000-OXFORD-A1-FOURTH-TWENTYFOUR-2026-10-29.json","CEFR-1000-OXFORD-A1-FIFTH-TWENTYFOUR-2026-10-29.json"]
EXPECTED = json.loads(r'''[["friend",2,314,"friend n.","FRIEND_PERSON_VS_FRIENDLY_ADJECTIVE"],["name",2,509,"name n., v.","NAME_PEOPLE_VS_OBJECT_OR_PLACE_AND_VERB"],["red",3,644,"red adj., n.","RED_COLOUR_ADJECTIVE_VS_NOUN"],["blue",1,93,"blue adj., n.","BLUE_COLOUR_ADJECTIVE_VS_MOOD"],["green",2,338,"green adj., n.","GREEN_COLOUR_VS_ENVIRONMENTAL_SENSE"],["black",1,90,"black adj., n.","BLACK_COLOUR_VS_NOUN"],["white",4,877,"white adj., n.","WHITE_COLOUR_VS_NOUN"],["girl",2,327,"girl n.","GIRL_CHILD_VS_ADULT_INFORMAL_USE"],["boy",1,104,"boy n.","BOY_CHILD_VS_ADULT_INFORMAL_USE"],["woman",4,888,"woman n.","WOMAN_ADULT_VS_GIRL_CHILD"],["child",1,145,"child n.","CHILD_PERSON_VS_CHILD_OF_PARENT"],["car",1,129,"car n.","CAR_ROAD_VEHICLE_VS_RAILWAY_CARRIAGE"],["bus",1,114,"bus n.","BUS_PASSENGER_VEHICLE_VS_VERB"],["train",4,817,"train n.","TRAIN_RAIL_VEHICLE_VS_TRAIN_VERB"],["city",1,149,"city n.","CITY_VS_TOWN_CONTEXT"],["country",1,177,"country n.","COUNTRY_NATION_VS_RURAL_AREA"],["street",3,743,"street n.","STREET_ROAD_VS_ADDRESS_NAME"],["table",3,760,"table n.","TABLE_FURNITURE_VS_DATA_TABLE"],["chair",1,138,"chair n.","CHAIR_SEAT_VS_MEETING_CHAIRPERSON"],["door",1,220,"door n.","DOOR_PANEL_VS_ENTRANCE"],["window",4,883,"window n.","WINDOW_BUILDING_VS_COMPUTER_INTERFACE"],["pen",3,580,"pen n.","PEN_WRITING_INSTRUMENT_VS_ANIMAL_ENCLOSURE"],["apple",1,39,"apple n.","APPLE_FRUIT_VS_BRAND_NAMED_ENTITY"],["and",1,30,"and conj.","AND_COORDINATING_CONJUNCTION_VS_SEQUENCE"]]''')
EXPECTED_PROPOSALS = json.loads(r'''[{"word":"name","issue":"Draft definition covers a person only, but names also identify places and things.","suggested_english_definition":"The word or words by which a person, place or thing is known.","suggested_myanmar_meaning":"လူ၊ နေရာ သို့မဟုတ် အရာတစ်ခုကို ခေါ်ဝေါ်သည့် အမည်","suggested_example_sentence":"Please write your name here.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false},{"word":"red","issue":"Definition by tomato colour is understandable but should be a learner-friendly colour gloss.","suggested_english_definition":"Having the colour of blood or a ripe tomato.","suggested_myanmar_meaning":"အနီရောင်ရှိသော","suggested_example_sentence":"She has a red bag.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false},{"word":"woman","issue":"Adult female sense must not be confused with girl or informal address.","suggested_english_definition":"An adult female person.","suggested_myanmar_meaning":"အရွယ်ရောက်ပြီးသော အမျိုးသမီး","suggested_example_sentence":"The woman is waiting for the bus.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false},{"word":"city","issue":"City versus town can be jurisdiction-specific; draft gloss should not be presented as a strict population threshold.","suggested_english_definition":"A large and important town where many people live and work.","suggested_myanmar_meaning":"လူဦးရေများပြီး အလုပ်အကိုင်နှင့် အဆောက်အအုံများစွာရှိသော မြို့ကြီး","suggested_example_sentence":"We live in a big city.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false},{"word":"train","issue":"Draft railway definition should be clear for passenger and goods trains without confusing verb train.","suggested_english_definition":"A railway vehicle made up of connected carriages that carries people or goods.","suggested_myanmar_meaning":"သံလမ်းပေါ်တွင် ပြေးဆွဲသည့် ရထား","suggested_example_sentence":"We travel to the city by train.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false},{"word":"and","issue":"Draft mentions words or ideas but does not explain phrase and clause coordination.","suggested_english_definition":"Used to join words, phrases or parts of sentences.","suggested_myanmar_meaning":"စကားလုံး၊ စကားစု သို့မဟုတ် ဝါကျအစိတ်အပိုင်းများကို ဆက်ရန် သုံးသည့် ‘နှင့်၊ ပြီးတော့’","suggested_example_sentence":"My brother and sister are here.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false}]''')

def require(condition, message):
    if not condition:
        raise ValueError(message)

def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(packet, shortlist, sha, check_upstream=False):
    require(sha == SHORTLIST_SHA, "Shortlist blob changed")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "Wrong scope")
    require(packet.get("status") == "A1_SIXTH_TWENTYFOUR_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD", "Status drift")
    require(packet.get("observed_on") == "2026-10-29" and packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "Provenance drift")
    require(type(packet.get("record_count")) is int and packet["record_count"] == 24, "Count drift")
    require(packet.get("counts_by_level") == {"A1":24,"A2":0,"B1":0,"B2":0,"C1":0}, "Level count drift")
    require(packet.get("independently_approved_count") == 0, "False independent approvals")
    require(packet.get("distinct_A1_oxford_word_pos_coverage_after_batch") == 100, "Coverage claim drift")
    limitations = packet.get("source_limitations", "")
    require("NOT exact-sense CEFR" in limitations and "No human-independent approvals" in limitations and "not 100 reviewed words" in limitations, "Caveat lost")
    require(packet.get("editorial_priority") == [row[4] for row in EXPECTED], "Risk priority drift")
    entries = shortlist.get("entries", [])
    require(len(entries) == 1000 and shortlist.get("counts_by_level") == {k:200 for k in LEVELS}, "1,000 scope or quotas drift")
    require(shortlist.get("independently_approved_by_level") == {k:0 for k in LEVELS}, "False shortlist approval")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False for e in entries), "Hold lost")
    selected = {e["word"]:e for e in entries if e.get("level") == "A1"}
    require(len(selected) == 200, "A1 quota drift")
    records = packet.get("records")
    require(isinstance(records,list) and len(records) == 24, "24 records required")
    require(len(set(r.get("word") for r in records)) == 24, "Duplicate new headword")
    earlier = []
    for filename in PREVIOUS:
        p = ROOT / "draft" / filename
        require(p.is_file(), "Prior source packet missing: " + filename)
        previous = json.loads(p.read_text(encoding="utf-8"))
        earlier.extend(r["word"] for r in previous["records"])
    require(len(set(earlier)) == 76, "Prior distinct A1 coverage no longer 76")
    require(not (set(earlier) & {r["word"] for r in records}), "Previously covered word repeated")
    require(len(set(earlier) | {r["word"] for r in records}) == 100, "Coverage not exactly 100")
    for row, (word,page,line,excerpt,risk) in zip(records, EXPECTED):
        require(row.get("word") == word and row.get("level") == "A1", word + ": identity")
        require(word in selected, word + ": missing from shortlist")
        source = selected[word]
        require(row.get("part_of_speech") == source.get("part_of_speech"), word + ": POS drift")
        require(row.get("shortlist_snapshot") == {"english_definition":source["english_definition"],"myanmar_meaning":source["burmese_meaning"],"example_sentence":source["example_sentence"]}, word + ": original bilingual/example drift")
        provenance = {k:source[k] for k in ("source_path","source_index","source_blob_sha")}
        require(row.get("shortlist_provenance") == provenance, word + ": historical Git provenance drift")
        expected_pub = {"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":URL,"observed_on":"2026-10-29","pdf_page":page,"extracted_line":line,"source_excerpt":excerpt,"source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}
        require(row.get("publisher_source") == expected_pub, word + ": publisher evidence drift")
        require(row.get("editorial_risk") == risk, word + ": editorial risk drift")
        task = ("Human-independent reviewer must check " + word + " as A1 in the exact intended sense, distinguish " + risk +
            ", independently evaluate the original English definition, fluent Myanmar meaning, example grammar and British pronunciation, and retain dated direct dictionary source evidence with content-bound human attestation. The Oxford list alone is word/POS evidence, not exact-sense approval.")
        require(row.get("independent_reviewer_task") == task, word + ": independent task drift")
        require(row.get("editorial_hold") is True and row.get("independently_reviewed") is False and row.get("release_approved") is False and row.get("independent_reviewer_receipt") is None, word + ": fabricated signoff")
        if check_upstream:
            upstream = ROOT / provenance["source_path"]
            require(upstream.is_file() and blob_sha(upstream) == provenance["source_blob_sha"], word + ": historical source blob drift")
            origin = json.loads(upstream.read_text(encoding="utf-8"))["entries"][provenance["source_index"]]
            require(all(origin.get(k) == source.get(k) for k in ("word","level","part_of_speech","english_definition","burmese_meaning","example_sentence")), word + ": historical original mismatch")
    require(packet.get("unreviewed_editorial_proposals") == EXPECTED_PROPOSALS, "Unreviewed bilingual rewrite drift or false approval")
    return len(records)

def self_test(packet, shortlist, sha):
    mutations = []
    for i in range(24):
        mutations += [
            lambda p,i=i: p["records"][i]["publisher_source"].update(extracted_line=-1),
            lambda p,i=i: p["records"][i]["publisher_source"].update(source_excerpt="forged"),
            lambda p,i=i: p["records"][i]["shortlist_snapshot"].update(myanmar_meaning="forged"),
            lambda p,i=i: p["records"][i]["shortlist_snapshot"].update(example_sentence="forged"),
            lambda p,i=i: p["records"][i]["shortlist_provenance"].update(source_index=-1),
            lambda p,i=i: p["records"][i].update(independently_reviewed=True),
            lambda p,i=i: p["records"][i].update(independent_reviewer_receipt={"reviewer":"fabricated"}),
            lambda p,i=i: p["records"][i].update(editorial_risk=""),
        ]
    for i in range(6):
        mutations += [
            lambda p,i=i: p["unreviewed_editorial_proposals"][i].update(human_independent_approval=True),
            lambda p,i=i: p["unreviewed_editorial_proposals"][i].update(suggested_myanmar_meaning="forged")
        ]
    mutations += [
        lambda p:p.update(record_count=25),
        lambda p:p.update(independently_approved_count=24),
        lambda p:p.update(distinct_A1_oxford_word_pos_coverage_after_batch=200),
        lambda p:p.update(shortlist_blob_sha="0"*40),
        lambda p:p.update(source_limitations="approved"),
        lambda p:p["records"].reverse(),
        lambda p:p["records"][0].update(release_approved=True),
        lambda p:p["records"][1]["publisher_source"].update(source_cefr_level="C1")
    ]
    for i,change in enumerate(mutations):
        altered = copy.deepcopy(packet)
        change(altered)
        try:
            audit(altered,shortlist,sha)
        except ValueError:
            continue
        raise AssertionError(f"Negative mutation {i} escaped")
    return len(mutations)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    packet=json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist=json.loads(SHORTLIST.read_text(encoding="utf-8"))
    n=audit(packet,shortlist,blob_sha(SHORTLIST),check_upstream=True)
    print(f"PASS A1 sixth Oxford packet: {n} word/POS observations; distinct coverage 100/200; level={args.level}; independent approvals 0; STAGING ONLY")
    if args.self_test:
        count=self_test(packet,shortlist,blob_sha(SHORTLIST))
        print(f"PASS {count}/{count} source, bilingual, provenance, proposal and false-review mutations rejected")

if __name__=="__main__":
    main()
