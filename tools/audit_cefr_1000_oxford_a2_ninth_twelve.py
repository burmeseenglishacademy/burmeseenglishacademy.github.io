#!/usr/bin/env python3
"""Fail-closed, staging-only Oxford A2 ninth-twelve source/snapshot auditor.

Direct publisher PDF word/POS and four dictionary sense leads are research,
NOT independently reviewed exact-sense CEFR, Myanmar, grammar or audio evidence.
No release or deployment action exists in this script.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-NINTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_BLOB_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads(r'''{"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY","status":"A2_NINTH_TWELVE_OXFORD_PDF_FOUR_DIRECT_DICTIONARY_SENSE_LEADS_EDITORIAL_HOLD","observed_on":"2026-10-30","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","record_count":12,"counts_by_level":{"A1":0,"A2":12,"B1":0,"B2":0,"C1":0},"publisher_reference_level_counts":{"A1":6,"A2":4,"B1":2},"word_pos_discrepancies":8,"direct_dictionary_sense_leads":4,"independently_approved_count":0,"independent_human_review_receipts":[],"audio_real_listening_signoffs":0,"release_approved":false,"source_limitations":"Direct Oxford 3000 CEFR PDF and four Oxford dictionary pages inspected 2026-10-30. Six A1 and two B1 publisher word/POS labels conflict with provisional A2. Dictionary sense leads and Oxford topic labels are not independent exact-sense CEFR, fluent Myanmar, example, pronunciation, listening or physical-device approval. Frozen shortlist, reviewer flags and production remain unchanged.","records":[{"word":"contact","level":"A2","part_of_speech":"verb","shortlist_snapshot":{"english_definition":"To communicate with someone by phone, email, or another method.","myanmar_meaning":"ဆက်သွယ်သည်","example_sentence":"Please contact the office before Friday."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":596,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":8,"extracted_line":1932,"source_excerpt":"contact n., v.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/contact_2","page_text_line_start":88,"page_text_line_end":123,"editorial_interpretation":"Verb sense 1 is communication with somebody, including phone, letter or email; directly aligns with the draft, distinct from noun physical contact.","observed_on":"2026-10-30","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"editorial_risk":"Communication by telephone/email; distinguish verb from physical contact noun; publisher B1, provisional A2.","unapproved_myanmar_proposal":"ဖုန်း၊ အီးမေးလ် စသည်ဖြင့် ဆက်သွယ်သည်","unapproved_original_example_proposal":"Please contact the school if you have any questions.","independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"offer","level":"A2","part_of_speech":"verb","shortlist_snapshot":{"english_definition":"To say that you are willing to give or do something.","myanmar_meaning":"ကမ်းလှမ်းသည်","example_sentence":"They offer free lessons every weekend."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":597,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":6,"extracted_line":1432,"source_excerpt":"offer v., n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/offer_1","page_text_line_start":88,"page_text_line_end":125,"editorial_interpretation":"Verb sense 1 concerns willingness to give; draft example 'They offer free lessons' may describe regular provision, so definition/example alignment needs human judgement.","observed_on":"2026-10-30","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"editorial_risk":"Definition says willingness to give/do, but example 'They offer free lessons' describes habitual provision; independent reviewer must reconcile sense.","unapproved_myanmar_proposal":"တစ်စုံတစ်ရာ ပေးရန် သို့မဟုတ် လုပ်ပေးရန် ကမ်းလှမ်းသည်","unapproved_original_example_proposal":"She offered to help me carry the books.","independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"build","level":"A2","part_of_speech":"verb","shortlist_snapshot":{"english_definition":"To make something by putting materials or parts together.","myanmar_meaning":"ဆောက်လုပ်သည်၊ တည်ဆောက်သည်","example_sentence":"They will build a new bridge next year."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":598,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":1,"extracted_line":112,"source_excerpt":"build v.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":null,"editorial_risk":"Construction sense matches, but provisional A2 is above publisher A1 word/POS; distinguish physical construction from building confidence.","unapproved_myanmar_proposal":null,"unapproved_original_example_proposal":null,"independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"culture","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"The customs, beliefs, and ways of life of a group of people.","myanmar_meaning":"ယဉ်ကျေးမှု","example_sentence":"Food is an important part of local culture."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":599,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":1,"extracted_line":183,"source_excerpt":"culture n.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":null,"editorial_risk":"Customs/beliefs meaning is plausible; distinguish group culture from arts and laboratory cultures; provisional A2 above A1.","unapproved_myanmar_proposal":null,"unapproved_original_example_proposal":null,"independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"safe","level":"A2","part_of_speech":"adjective","shortlist_snapshot":{"english_definition":"Not likely to cause harm or danger.","myanmar_meaning":"ဘေးကင်းသော","example_sentence":"This path is safe for children to use."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":600,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":6,"extracted_line":1576,"source_excerpt":"safe adj.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":null,"editorial_risk":"Physical safety of a path versus safety from risk; exact-sense and natural Myanmar require independent review.","unapproved_myanmar_proposal":null,"unapproved_original_example_proposal":null,"independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"career","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"The series of jobs a person has during their working life.","myanmar_meaning":"အလုပ်အကိုင်ဘဝ","example_sentence":"She hopes to start a career in engineering."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":601,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":1,"extracted_line":131,"source_excerpt":"career n.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":null,"editorial_risk":"Series of jobs over working life versus first job; provisional A2 above A1.","unapproved_myanmar_proposal":null,"unapproved_original_example_proposal":null,"independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"training","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"The process of learning skills needed for a job or activity.","myanmar_meaning":"လေ့ကျင့်သင်ကြားမှု","example_sentence":"New workers receive safety training."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":603,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":7,"extracted_line":1723,"source_excerpt":"training n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":null,"editorial_risk":"Job skills instruction, not a train as vehicle; confirm Myanmar distinction between teaching and practice.","unapproved_myanmar_proposal":null,"unapproved_original_example_proposal":null,"independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"stay","level":"A2","part_of_speech":"verb","shortlist_snapshot":{"english_definition":"To remain in a place instead of leaving.","myanmar_meaning":"တစ်နေရာတွင် ဆက်နေသည်","example_sentence":"Please stay here until the bus arrives."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":664,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":739,"source_excerpt":"stay v.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":null,"editorial_risk":"Remain in a place, not a temporary hotel visit; provisional A2 above A1.","unapproved_myanmar_proposal":null,"unapproved_original_example_proposal":null,"independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"age","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"The number of years a person has lived.","myanmar_meaning":"အသက်အရွယ်","example_sentence":"The form asks for your age."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":665,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":1,"extracted_line":20,"source_excerpt":"age n.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":null,"editorial_risk":"Numerical age of person rather than historical era; provisional A2 above A1.","unapproved_myanmar_proposal":null,"unapproved_original_example_proposal":null,"independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"deal","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"An agreement between two people or groups.","myanmar_meaning":"သဘောတူညီချက်","example_sentence":"They made a deal to share the costs."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":666,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":8,"extracted_line":1960,"source_excerpt":"deal n.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/deal_2","page_text_line_start":88,"page_text_line_end":121,"editorial_interpretation":"Noun sense 1 is an agreement, particularly in business; distinguish deal verb and noun senses for treatment or softwood.","observed_on":"2026-10-30","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"editorial_risk":"Agreement noun vs verb deal and uncountable softwood 'deal'; provisional A2 below B1.","unapproved_myanmar_proposal":"နှစ်ဖက်အကြား သဘောတူညီချက်","unapproved_original_example_proposal":"We made a deal to share the transport costs.","independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"check","level":"A2","part_of_speech":"verb","shortlist_snapshot":{"english_definition":"To examine something to make sure it is correct.","myanmar_meaning":"မှန်ကန်မှုရှိမရှိ စစ်ဆေးသည်","example_sentence":"Please check your answers before you leave."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":667,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":1,"extracted_line":142,"source_excerpt":"check v.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":null,"editorial_risk":"Examine for correctness; not a bank cheque or mark; provisional A2 above A1.","unapproved_myanmar_proposal":null,"unapproved_original_example_proposal":null,"independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"heart","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"The organ in your chest that pumps blood.","myanmar_meaning":"နှလုံး","example_sentence":"Regular exercise can help keep your heart healthy."},"shortlist_provenance":{"source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":668,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc"},"publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":5,"extracted_line":1267,"source_excerpt":"heart n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/heart_1","page_text_line_start":88,"page_text_line_end":125,"editorial_interpretation":"Noun sense 1 is the blood-pumping organ, distinct from emotion and heart shape; Body a2 topic tag is not a separately verified exact-sense CEFR label.","observed_on":"2026-10-30","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"editorial_risk":"Physical organ sense rather than emotional centre or symbol; topic Body a2 is not independent exact-sense CEFR approval.","unapproved_myanmar_proposal":"ခန္ဓာကိုယ်အနှံ့ သွေးလည်ပတ်စေသော နှလုံး","unapproved_original_example_proposal":"The doctor checked his heart.","independent_reviewer_task":"An independent human must review exact-sense source-backed CEFR level, English definition, natural fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. PDF word/POS and dictionary/topic observations are not independent approval.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null}]}''')
REVIEW_FIELDS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                 "reviewed_level", "reviewed_pronunciation", "release_approved")

def require(ok, reason):
    if not ok:
        raise ValueError(reason)

def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def audit(packet, shortlist, check_file_sha=True):
    require(isinstance(packet, dict) and packet == EXPECTED,
            "Publisher PDF, dictionary, bilingual snapshot, provenance, holds or metadata drift")
    require(len(packet["records"]) == 12 and len({r["word"] for r in packet["records"]}) == 12,
            "Exactly twelve distinct A2 research records required")
    require(collections.Counter(r["publisher_source"]["source_cefr_level"]
                                for r in packet["records"]) == {"A1": 6, "A2": 4, "B1": 2},
            "Source level discrepancy counts changed")
    require(sum(r["dictionary_sense_lead"] is not None for r in packet["records"]) == 4,
            "Four direct dictionary sense leads required")
    require(packet["independently_approved_count"] == 0
            and packet["independent_human_review_receipts"] == []
            and packet["audio_real_listening_signoffs"] == 0
            and packet["release_approved"] is False, "Forged approval/listening receipt")
    if check_file_sha:
        require(git_blob_sha(SHORTLIST) == SHORTLIST_BLOB_SHA,
                "Frozen shortlist content Git blob SHA changed")
    require(shortlist.get("release_status") ==
            "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH",
            "Provisional shortlist release status changed")
    require(shortlist.get("counts_by_level") == dict.fromkeys(LEVELS, 200)
            and shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "Scope or independent approval counts changed")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000,
            "Shortlist must remain exactly 1000 provisional entries")
    byword = {(r.get("level"), r.get("word")): r for r in entries}
    require(len(byword) == 1000, "Duplicate provisional headwords or levels")
    for record in packet["records"]:
        source = byword.get(("A2", record["word"]))
        require(source is not None and source.get("part_of_speech") == record["part_of_speech"],
                "Shortlist headword or part-of-speech mismatch")
        for k, v in record["shortlist_snapshot"].items():
            actual_key = "burmese_meaning" if k == "myanmar_meaning" else k
            require(source.get(actual_key) == v, "Frozen bilingual/example drift: " + record["word"])
        for k, v in record["shortlist_provenance"].items():
            require(source.get(k) == v, "Historical Git provenance drift: " + record["word"])
        require(source.get("editorial_hold") is True
                and all(source.get(f) is False for f in REVIEW_FIELDS),
                "Fabricated human review or release approval: " + record["word"])
        require(record["publisher_source"]["evidence_scope"] ==
                "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE"
                and record["publisher_source"]["access"] == "DIRECT_OFFICIAL_PDF_WEB_TEXT",
                "Oxford PDF word/POS research cannot be called exact-sense approval")
        if record["dictionary_sense_lead"] is not None:
            require(record["dictionary_sense_lead"]["evidence_scope"] ==
                    "DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF",
                    "Dictionary page research cannot be called human-independent approval")
    return True

def negative_tests(packet, shortlist):
    rejected = 0
    def reject(p, s):
        nonlocal rejected
        try:
            audit(p, s, check_file_sha=False)
        except (ValueError, TypeError, KeyError):
            rejected += 1
        else:
            raise AssertionError("Forged research or human signoff accepted")
    for key in packet:
        if key == "records":
            continue
        p = copy.deepcopy(packet)
        p[key] = "FORGED"
        reject(p, shortlist)
    for i, record in enumerate(packet["records"]):
        for key, val in record.items():
            if isinstance(val, dict):
                for inner in val:
                    p = copy.deepcopy(packet)
                    p["records"][i][key][inner] = "FORGED"
                    reject(p, shortlist)
            else:
                p = copy.deepcopy(packet)
                p["records"][i][key] = "FORGED"
                reject(p, shortlist)
    for word in [r["word"] for r in packet["records"]]:
        for field in ("english_definition", "burmese_meaning", "example_sentence",
                      "source_path", "source_index", "source_blob_sha",
                      "editorial_hold", "reviewed_english", "reviewed_burmese",
                      "reviewed_example", "reviewed_level",
                      "reviewed_pronunciation", "release_approved"):
            s = copy.deepcopy(shortlist)
            entry = next(r for r in s["entries"] if r["word"] == word and r["level"] == "A2")
            entry[field] = False if field == "editorial_hold" else (True if field in REVIEW_FIELDS else "FORGED")
            reject(packet, s)
    s = copy.deepcopy(shortlist)
    s["independently_approved_by_level"]["A2"] = 1
    reject(packet, s)
    s = copy.deepcopy(shortlist)
    s["entries"].pop()
    reject(packet, s)
    return rejected

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    audit(packet, shortlist)
    if args.self_test:
        n = negative_tests(packet, shortlist)
        print(f"PASS: {n}/{n} forged source, bilingual, provenance, review and listening mutations rejected")
    print(json.dumps({"level": args.level, "records": 12, "source_cefr": {"A1": 6, "A2": 4, "B1": 2},
                      "direct_dictionary_sense_leads": 4, "independent_approvals": 0,
                      "release": "BLOCKED_STAGING_ONLY"}, sort_keys=True))

if __name__ == "__main__":
    main()
