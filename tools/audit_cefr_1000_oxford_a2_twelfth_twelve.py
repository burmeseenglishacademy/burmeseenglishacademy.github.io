#!/usr/bin/env python3
"""Fail-closed A2 twelfth Oxford source-bound staging audit; never approves human review."""
import argparse, copy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-TWELFTH-TWELVE-AND-FOUR-SENSE-LEADS-2026-10-31.json"
SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
ANCHORS = json.loads(r'''[["fire",2,292,"fire n.","A1","Fire in the camping example is controlled flames; distinguish a destructive blaze."],["fun",2,320,"fun n.","A1","Have fun is natural, fun noun is uncountable in the example; distinguish adjective fun."],["art",1,45,"art n.","A1","Art as creative practice, not an individual artwork; Myanmar translation should preserve this sense."],["building",1,113,"building n.","A1","Countable physical structure, not the process of building."],["education",5,1154,"education n.","A2","Educational process rather than institution; a good education is idiomatic and can be countable."],["front",2,317,"front n., adj.","A1","Forward side of a house, not cardinal east; in front of and at the front of differ."],["list",2,446,"list n., v.","A1","Countable written inventory, not verb to list; made a list is natural."],["college",1,161,"college n.","A1","British further-education college versus US degree college; Myanmar needs context."],["town",4,815,"town n.","A1","Settlement smaller than a city; some city/town distinctions vary by country."],["date",1,193,"date n.","A1","Calendar date, not a romantic meeting or fruit; apostrophe in today's is correct."],["land",2,423,"land n.","A1","Dry land as opposed to sea, not land ownership or verb to land."],["space",3,726,"space n.","A1","Available room in example is uncountable, not outer space or countable parking space."]]''')
DICTIONARY = json.loads(r'''{"college":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/college","heading":"UK post-school study or training, distinct from US college-as-university","lines":[105,164],"grammar":"countable or uncountable","note":"British college may provide further education or vocational training; US college often denotes degree study. Myanmar should not imply every college is a university.","proposal":{"myanmar_meaning":"ကျောင်းပြီးနောက် ပညာဆက်လက်သင်ယူရန် သို့မဟုတ် သက်မွေးပညာသင်ယူရန် ကောလိပ်","original_example":"She plans to study nursing at a local college next year."}},"front":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/front_1","heading":"forward part or position of an object or building","lines":[106,140],"grammar":"countable, usually singular; often the front","note":"Front is the forward side, not east. Distinguish at the front of from in front of and avoid Myanmar အရှေ့ ambiguity.","proposal":{"myanmar_meaning":"အရာဝတ္ထုတစ်ခု၏ ရှေ့ဘက်ပိုင်း","original_example":"There is a small garden at the front of our house."}},"education":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/education","heading":"teaching, training and learning process","lines":[105,115],"grammar":"uncountable or countable in a specific education","note":"The original a good education is grammatical; education is not always an uncountable-only noun.","proposal":{"myanmar_meaning":"ပညာသင်ကြားခြင်းနှင့် သင်ယူလေ့လာခြင်း လုပ်ငန်းစဉ်","original_example":"Every child should have access to education."}},"space":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/space_1","heading":"available room or area for use, not outer space","lines":[203,216],"grammar":"uncountable for available room; countable for an individual empty place","note":"Original example enough space for another chair specifically illustrates uncountable available room (dictionary sense 3), not merely countable an empty space (sense 2).","proposal":{"myanmar_meaning":"အသုံးပြုရန် ရရှိနိုင်သော နေရာလွတ်","original_example":"There is enough space for another chair in this room."}}}''')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def expected_packet():
    require(blob_sha(SHORT) == SHA, "Frozen shortlist blob changed")
    short = json.loads(SHORT.read_text(encoding="utf-8"))
    require(short["counts_by_level"] == dict.fromkeys(("A1","A2","B1","B2","C1"),200), "Wrong 1000 scope")
    require(short["independently_approved_by_level"] == dict.fromkeys(("A1","A2","B1","B2","C1"),0), "False independent approvals")
    require(len(short["entries"]) == 1000, "Shortlist length changed")
    by_word = {r["word"]: r for r in short["entries"]}
    require(len(by_word) == 1000, "Duplicate shortlist headwords")
    records = []
    for word, page, line, excerpt, pub_level, risk in ANCHORS:
        e = by_word[word]
        require(e["level"] == "A2" and e["editorial_hold"] is True
                and e["release_approved"] is False and all(e["reviewed_"+k] is False for k in
                ("english","burmese","example","level","pronunciation")), "A2 editorial hold lost: "+word)
        row = {
          "word":word, "level":"A2", "part_of_speech":e["part_of_speech"],
          "shortlist_snapshot":{"english_definition":e["english_definition"],
                                "myanmar_meaning":e["burmese_meaning"],
                                "example_sentence":e["example_sentence"]},
          "shortlist_provenance":{k:e[k] for k in ("source_path","source_index","source_blob_sha")},
          "publisher_source":{"publisher":"Oxford University Press",
                              "title":"The Oxford 3000 by CEFR level","url":URL,
                              "observed_on":"2026-10-31","pdf_page":page,
                              "extracted_line":line,"source_excerpt":excerpt,
                              "source_cefr_level":pub_level,
                              "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                              "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
          "editorial_risk":risk,
          "original_example_grammar_note":"First-pass sentence reviewed as an editorial lead only; independent native-English and fluent Myanmar signoff not completed.",
          "independent_reviewer_task":"Independent human: reconcile Oxford word/POS label with intended exact sense, confirm English definition, fluent Myanmar, original-example grammar, British pronunciation and level placement; retier/replace if necessary.",
          "editorial_hold":True,"independently_reviewed":False,
          "release_approved":False,"independent_reviewer_receipt":None
        }
        if word in DICTIONARY:
            d=DICTIONARY[word]
            row["dictionary_sense_lead"] = {
              "publisher":"Oxford University Press","url":d["url"],"observed_on":"2026-10-31",
              "sense_heading_paraphrase":d["heading"],"page_text_line_start":d["lines"][0],
              "page_text_line_end":d["lines"][1],"grammar":d["grammar"],
              "editorial_note":d["note"],"source_scope":"DIRECT_DICTIONARY_SENSE_NOT_INDEPENDENT_CEFR_APPROVAL",
              "site_footer_word_of_day_cefr_not_attributed_to_headword":True,
              "unapproved_proposal":d["proposal"]
            }
        records.append(row)
    require(len({r["word"] for r in records}) == 12, "Duplicate new A2 word")
    return {
      "schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY",
      "status":"A2_TWELFTH_TWELVE_OXFORD_DIRECT_WORD_POS_FOUR_DICTIONARY_SENSE_LEADS_HELD",
      "observed_on":"2026-10-31","shortlist_blob_sha":SHA,
      "record_count":12,"counts_by_level":{"A1":0,"A2":12,"B1":0,"B2":0,"C1":0},
      "publisher_reference_level_counts":{"A1":11,"A2":1,"B1":0,"B2":0,"C1":0},
      "dictionary_sense_lead_count":4,"independently_approved_count":0,
      "real_george_emma_listening_signoffs":0,
      "source_limitations":"Direct Oxford 3000 CEFR PDF word/POS labels are not independently validated exact-sense CEFR ratings. Four dictionary sense leads were opened and paraphrased; dictionary topic badges and site-wide Word of the Day footer are NOT headword CEFR labels. Original Myanmar and example remain unreviewed; no independent reviewer or audio/device/deployment evidence.",
      "records":records
    }

def verify(candidate, expected):
    require(candidate == expected, "A2 twelfth packet differs from source-anchored frozen shortlist")
    return True

def self_test(expected):
    n=0
    global_cases=[
      lambda x:x.update(status="READY"),
      lambda x:x.update(independently_approved_count=12),
      lambda x:x.update(real_george_emma_listening_signoffs=12),
      lambda x:x.update(record_count=11),
      lambda x:x.update(shortlist_blob_sha="0"*40),
      lambda x:x["records"].reverse(),
      lambda x:x["records"].append(copy.deepcopy(x["records"][0])),
      lambda x:x.update(unreviewed_extra=True)
    ]
    for mutate in global_cases:
        bad=copy.deepcopy(expected);mutate(bad)
        try:verify(bad,expected)
        except ValueError:n+=1
        else:raise AssertionError("Global forged A2 packet accepted")
    for i in range(12):
        mutations=[
          lambda r:r.update(word="forged"),
          lambda r:r.update(part_of_speech="forged"),
          lambda r:r["shortlist_snapshot"].update(english_definition="forged"),
          lambda r:r["shortlist_snapshot"].update(myanmar_meaning="အမှား"),
          lambda r:r["shortlist_snapshot"].update(example_sentence="Forged."),
          lambda r:r["shortlist_provenance"].update(source_blob_sha="0"*40),
          lambda r:r["publisher_source"].update(source_cefr_level="C1"),
          lambda r:r["publisher_source"].update(source_excerpt="fabricated"),
          lambda r:r["publisher_source"].update(extracted_line=999),
          lambda r:r["publisher_source"].update(url="https://example.invalid"),
          lambda r:r.update(independently_reviewed=True),
          lambda r:r.update(release_approved=True),
          lambda r:r.update(independent_reviewer_receipt={"reviewer":"AI"}),
          lambda r:r.update(editorial_hold=False),
        ]
        if expected["records"][i].get("dictionary_sense_lead"):
            mutations.extend([
              lambda r:r["dictionary_sense_lead"].update(page_text_line_start=999),
              lambda r:r["dictionary_sense_lead"].update(site_footer_word_of_day_cefr_not_attributed_to_headword=False),
              lambda r:r["dictionary_sense_lead"]["unapproved_proposal"].update(myanmar_meaning="forged")
            ])
        for mutate in mutations:
            bad=copy.deepcopy(expected);mutate(bad["records"][i])
            try:verify(bad,expected)
            except ValueError:n+=1
            else:raise AssertionError("Forged A2 record accepted: "+str(i))
    return n

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=("A1","A2","B1","B2","C1","ALL"),default="ALL")
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    expected=expected_packet()
    candidate=json.loads(PACKET.read_text(encoding="utf-8"))
    verify(candidate,expected)
    n=self_test(expected) if a.self_test else 0
    print(json.dumps({"level":a.level,"new_a2_draft_oxford_word_pos_observations":12 if a.level in ("A2","ALL") else 0,
      "publisher_A1":11,"publisher_A2":1,"direct_dictionary_sense_leads":4,
      "adversarial_mutations_rejected":n,"independently_approved":0,
      "real_listening_signoffs":0,"release":"BLOCKED_STAGING_ONLY"},sort_keys=True))

if __name__=="__main__":
    main()
