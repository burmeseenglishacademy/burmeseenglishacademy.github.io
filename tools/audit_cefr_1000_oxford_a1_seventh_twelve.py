#!/usr/bin/env python3
"""Fail-closed A1 seventh-twelve Oxford publisher-word/POS research auditor.

Official publisher word/POS list is not a sense-level CEFR dictionary.
All records and editorial rewrites remain unreviewed, unapplied, staging only.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-SEVENTH-TWELVE-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PREVIOUS = ["A1-TWELVE-DIRECT-PDF-2026-10-28","A1-SECOND-TWELVE-2026-10-28","A1-THIRD-TWELVE-2026-10-28","A1-FOURTH-TWENTYFOUR-2026-10-29","A1-FIFTH-TWENTYFOUR-2026-10-29","A1-SIXTH-TWENTYFOUR-2026-10-29"]
EXPECTED_HEADER = json.loads(r'''{"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY","status":"A1_SEVENTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD","observed_on":"2026-10-29","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","record_count":12,"counts_by_level":{"A1":12,"A2":0,"B1":0,"B2":0,"C1":0},"publisher_reference_level_counts":{"A1":12,"A2":0,"B1":0,"B2":0,"C1":0},"word_pos_discrepancies":0,"part_of_speech_taxonomy_flags":["how"],"independently_approved_count":0,"distinct_A1_oxford_word_pos_coverage_after_batch":112,"source_limitations":"Official Oxford 3000 PDF word/POS labels only, NOT exact-sense CEFR or independent Myanmar/English/example approval. No human-independent approvals, no real audio listening, no physical iPhone QA, no deployment. Twelve observations are not twelve independently reviewed words."}''')
EXPECTED_FIXED = json.loads(r'''[{"word":"to","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":3,"extracted_line":804,"source_excerpt":"to prep., infinitive marker","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"TO_DESTINATION_VS_INFINITIVE","editorial_risk":"Destination use in the draft example must not be confused with the infinitive marker; verify grammatical function and Myanmar destination particle.","independent_reviewer_task":"Separate independent human review for to: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"from","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":2,"extracted_line":316,"source_excerpt":"from prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"FROM_ORIGIN_VS_START_TIME","editorial_risk":"The example expresses place of origin; independently verify country-origin use rather than a time or material source.","independent_reviewer_task":"Separate independent human review for from: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"with","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":4,"extracted_line":886,"source_excerpt":"with prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"WITH_ACCOMPANIMENT_VS_INSTRUMENT","editorial_risk":"The example expresses living together with family, not use of an instrument; distinguish the intended Myanmar accompaniment meaning.","independent_reviewer_task":"Separate independent human review for with: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"for","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":2,"extracted_line":305,"source_excerpt":"for prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"FOR_BENEFICIARY_VS_PURPOSE","editorial_risk":"The gift example marks the intended recipient, not duration or purpose; verify recipient-focused Myanmar.","independent_reviewer_task":"Separate independent human review for for: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"of","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":3,"extracted_line":541,"source_excerpt":"of prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"OF_POSSESSION_VS_PARTITIVE","editorial_risk":"The draft combines possession and part-whole meanings; the door-of-the-room example needs an exact-sense check for naturalness and Myanmar phrasing.","independent_reviewer_task":"Separate independent human review for of: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"at","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":1,"extracted_line":50,"source_excerpt":"at prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"AT_TIME_VS_LOCATION","editorial_risk":"The definition covers time and location but the example uses time only; require one coherent exact sense before release.","independent_reviewer_task":"Separate independent human review for at: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"as","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":1,"extracted_line":48,"source_excerpt":"as prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"AS_ROLE_VS_COMPARISON","editorial_risk":"The job-role preposition in works as a teacher must be distinguished from as-conjunction and similarity uses.","independent_reviewer_task":"Separate independent human review for as: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"by","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":1,"extracted_line":120,"source_excerpt":"by prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"BY_TRANSPORT_VS_PASSIVE_AGENT","editorial_risk":"The example uses a means of transport, whereas the gloss also refers to an agent; align English and Myanmar to one exact sense.","independent_reviewer_task":"Separate independent human review for by: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"about","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":1,"extracted_line":5,"source_excerpt":"about prep., adv.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"ABOUT_TOPIC_VS_APPROXIMATION","editorial_risk":"The example uses topic preposition; Oxford combines preposition and adverb, so do not import approximate-quantity sense.","independent_reviewer_task":"Separate independent human review for about: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"after","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":1,"extracted_line":17,"source_excerpt":"after prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"AFTER_TIME_PREP_VS_A2_CONJ_ADV","editorial_risk":"Oxford places after preposition at A1 but after conjunction/adverb at A2; verify the example's prepositional object.","independent_reviewer_task":"Separate independent human review for after: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"before","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":1,"extracted_line":75,"source_excerpt":"before prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"BEFORE_TIME_PREP_VS_A2_CONJ_ADV","editorial_risk":"Oxford places before preposition at A1 but before conjunction/adverb at A2; the example must remain prepositional.","independent_reviewer_task":"Separate independent human review for before: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."},{"word":"how","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":2,"extracted_line":381,"source_excerpt":"how adv.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk_id":"HOW_QUESTION_WORD_VS_ADVERB_TAXONOMY","editorial_risk":"The shortlist labels a question word, while Oxford labels the item adverb; verify pedagogical POS mapping and greeting formula versus method.","independent_reviewer_task":"Separate independent human review for how: verify exact-sense CEFR from a directly inspected sense-specific dictionary entry with URL, date and locator; check fluent Myanmar, English definition, original example grammar and British pronunciation. Oxford A1 word/POS alone is NOT exact-sense proof. Bind any real reviewer receipt to final content hash."}]''')
EXPECTED_PROPOSALS = json.loads(r'''[{"word":"at","issue":"Draft definition spans both place and time while the example uses time.","suggested_english_definition":"Used before a particular time.","suggested_myanmar_meaning":"အချိန်တစ်ခုကို ဖော်ပြရာတွင် သုံးသော 'မှာ၊ တွင်'","suggested_example_sentence":"We meet at six o'clock.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false},{"word":"by","issue":"Draft combines passive agent and transport method.","suggested_english_definition":"Used to show the means of transport.","suggested_myanmar_meaning":"ယာဉ်တစ်မျိုးမျိုးဖြင့် သွားလာကြောင်း ဖော်ပြရာတွင် သုံးသော 'ဖြင့်'","suggested_example_sentence":"She goes to work by bus.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false},{"word":"of","issue":"Possession and part-whole senses overlap in draft and example.","suggested_english_definition":"Used to show that something is part of a larger thing.","suggested_myanmar_meaning":"တစ်ခုခု၏ အစိတ်အပိုင်းဖြစ်ကြောင်း ဖော်ပြရာတွင် သုံးသော '၏၊ ရဲ့'","suggested_example_sentence":"The roof of the house is red.","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false},{"word":"how","issue":"Question-word classroom label differs from Oxford's adverb taxonomy.","suggested_english_definition":"Used to ask about someone's condition.","suggested_myanmar_meaning":"အခြေအနေကို မေးရာတွင် သုံးသော 'ဘယ်လို'","suggested_example_sentence":"How is your mother today?","review_status":"UNREVIEWED_UNAPPLIED_PROPOSAL","human_independent_approval":false}]''')
ROW_KEYS = {"word", "level", "part_of_speech", "shortlist_snapshot",
            "shortlist_provenance", "publisher_source", "editorial_risk_id",
            "editorial_risk", "independent_reviewer_task", "editorial_hold",
            "independently_reviewed", "release_approved", "independent_reviewer_receipt"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git_blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load():
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    return packet, shortlist


def audit(packet, shortlist, verify_upstream=True):
    require(git_blob(SHORTLIST) == SHORTLIST_SHA, "Frozen shortlist blob changed")
    require(shortlist.get("counts_by_level") == {x: 200 for x in ("A1","A2","B1","B2","C1")}
            and shortlist.get("independently_approved_by_level") == {x: 0 for x in ("A1","A2","B1","B2","C1")},
            "Frozen 1000 scope or human approval flags drift")
    require(isinstance(shortlist.get("entries"), list) and len(shortlist["entries"]) == 1000,
            "Shortlist must have 1000 entries")
    require(set(packet) == set(EXPECTED_HEADER) | {"records","editorial_rewrite_proposals"},
            "Packet unknown or missing field")
    for key, expected in EXPECTED_HEADER.items():
        require(packet.get(key) == expected, "Packet header drift: " + key)
    require(packet.get("editorial_rewrite_proposals") == EXPECTED_PROPOSALS,
            "Unreviewed editorial proposals drifted or falsely approved")
    rows = packet.get("records")
    require(isinstance(rows, list) and len(rows) == len(EXPECTED_FIXED) == 12,
            "Expected exactly twelve direct observations")
    by_word = {r["word"]: r for r in shortlist["entries"]}
    require(len(by_word) == 1000, "Shortlist contains duplicate headwords")
    seen = set()
    for i, (row, fixed) in enumerate(zip(rows, EXPECTED_FIXED)):
        word = fixed["word"]
        require(isinstance(row, dict) and set(row) == ROW_KEYS, "Unknown/missing row field")
        require(row["word"] == word and word not in seen, "Wrong or duplicate source word")
        seen.add(word)
        original = by_word.get(word)
        require(original is not None and original["level"] == "A1"
                and original["editorial_hold"] is True
                and original["release_approved"] is False, "Wrong A1 editorial hold")
        require(row["level"] == "A1" and row["part_of_speech"] == original["part_of_speech"],
                "Provisional word/POS changed")
        require(row["shortlist_snapshot"] == {
            "english_definition": original["english_definition"],
            "myanmar_meaning": original["burmese_meaning"],
            "example_sentence": original["example_sentence"]}, "English/Myanmar/example drift: " + word)
        require(row["shortlist_provenance"] == {k: original[k] for k in
                ("source_path", "source_index", "source_blob_sha")},
                "Historical Git provenance drift: " + word)
        for key in ("publisher_source", "editorial_risk_id", "editorial_risk", "independent_reviewer_task"):
            require(row.get(key) == fixed[key], "Publisher/locator/risk/task drift: " + word + ":" + key)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None,
                "Fabricated human approval/receipt: " + word)
    if verify_upstream:
        prior = set()
        for name in PREVIOUS:
            path = ROOT / ("draft/CEFR-1000-OXFORD-" + name + ".json")
            obj = json.loads(path.read_text(encoding="utf-8"))
            prior.update(r["word"] for r in obj["records"])
        require(not (seen & prior), "Repeated A1 source observation inflates coverage")
        require(len(prior) == 100 and len(prior | seen) == 112,
                "Previous A1 coverage or new distinct count drift")
    return {"source_observations": 12, "new_distinct_A1_word_pos": 12,
            "A1_distinct_oxford_word_pos_total": 112, "human_approvals": 0,
            "real_george_emma_listening": 0, "release": "BLOCKED_STAGING_ONLY"}


def self_test(packet, shortlist):
    cases = [
        ("word", lambda r: r.update(word="forged")),
        ("POS", lambda r: r.update(part_of_speech="noun")),
        ("English", lambda r: r["shortlist_snapshot"].update(english_definition="forged")),
        ("Myanmar", lambda r: r["shortlist_snapshot"].update(myanmar_meaning="အတု")),
        ("example", lambda r: r["shortlist_snapshot"].update(example_sentence="forged")),
        ("source index", lambda r: r["shortlist_provenance"].update(source_index=-1)),
        ("source SHA", lambda r: r["shortlist_provenance"].update(source_blob_sha="0" * 40)),
        ("source URL", lambda r: r["publisher_source"].update(url="https://example.invalid/fake.pdf")),
        ("source page", lambda r: r["publisher_source"].update(pdf_page=999)),
        ("source line", lambda r: r["publisher_source"].update(extracted_line=9999)),
        ("source excerpt", lambda r: r["publisher_source"].update(source_excerpt="forged n.")),
        ("publisher CEFR", lambda r: r["publisher_source"].update(source_cefr_level="C1")),
        ("source date", lambda r: r["publisher_source"].update(observed_on="2099-01-01")),
        ("scope escalation", lambda r: r["publisher_source"].update(evidence_scope="INDEPENDENT_SENSE_APPROVAL")),
        ("risk deletion", lambda r: r.update(editorial_risk="")),
        ("risk code", lambda r: r.update(editorial_risk_id="forged")),
        ("reviewer task", lambda r: r.update(independent_reviewer_task="forged")),
        ("review flag", lambda r: r.update(independently_reviewed=True)),
        ("release flag", lambda r: r.update(release_approved=True)),
        ("fabricated receipt", lambda r: r.update(independent_reviewer_receipt={"name":"forged"})),
    ]
    tested = 0
    for i in range(12):
        for label, change in cases:
            forged = copy.deepcopy(packet)
            change(forged["records"][i])
            try:
                audit(forged, shortlist, verify_upstream=False)
            except ValueError:
                tested += 1
            else:
                raise AssertionError("Mutation accepted: %s / %s" % (i, label))
    for label, change in [
        ("record count", lambda x: x.update(record_count=11)),
        ("coverage claim", lambda x: x.update(distinct_A1_oxford_word_pos_coverage_after_batch=200)),
        ("independent approvals", lambda x: x.update(independently_approved_count=12)),
        ("status", lambda x: x.update(status="PUBLISHED")),
        ("observed date", lambda x: x.update(observed_on="2099-01-01")),
        ("source limitations", lambda x: x.update(source_limitations="Independently approved")),
        ("proposal forged approval", lambda x: x["editorial_rewrite_proposals"][0].update(human_independent_approval=True)),
        ("proposal translation", lambda x: x["editorial_rewrite_proposals"][1].update(suggested_myanmar_meaning="အတု")),
        ("proposal removed", lambda x: x["editorial_rewrite_proposals"].pop()),
        ("row removed", lambda x: x["records"].pop()),
    ]:
        forged = copy.deepcopy(packet)
        change(forged)
        try:
            audit(forged, shortlist, verify_upstream=False)
        except ValueError:
            tested += 1
        else:
            raise AssertionError("Header/proposal mutation accepted: " + label)
    return tested


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("A1","A2","B1","B2","C1","ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet, shortlist = load()
    result = audit(packet, shortlist)
    if args.self_test:
        result["negative_mutations_rejected"] = self_test(packet, shortlist)
    print(json.dumps({"requested_level":args.level, **result}, sort_keys=True))


if __name__ == "__main__":
    main()
