#!/usr/bin/env python3
"""Source-bound Oxford A1 exact-sense leads; NOT independent CEFR or bilingual approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
TASK = "Independent human reviewer: Compare the directly observed Oxford dictionary sense with the frozen draft, verify CEFR applicability for this exact sense (a topic label is not a sense CEFR label), check natural Myanmar and original example grammar, record reviewer identity/date/content hash and retain editorial hold until independently signed."
LIMIT = "Four Oxford Advanced Learner's Dictionary pages were directly inspected on 2026-10-30, with zero-based web-extracted line ranges. These are directly observed dictionary-sense research leads, NOT independently verified exact-sense CEFR levels. Oxford topical a1 tags and Oxford 3000 word/POS A1 classification are not automatic exact-sense CEFR approval. English, Myanmar, example, audio and device checks remain on hold."
LEADS = json.loads(r'''[["rice","https://www.oxfordlearnersdictionaries.com/definition/english/rice",103,118,"Uncountable noun. Publisher entry describes rice grain, rice plant and prepared rice dishes; example 'served with rice' supports the draft cooked-rice lunch context.","Draft Myanmar ဆန် denotes uncooked rice and ထမင်း cooked rice; the original example is cooked rice. Human reviewer must choose accurate sense-specific Myanmar or clearly explain both."],["chicken","https://www.oxfordlearnersdictionaries.com/definition/english/chicken_1",107,161,"Publisher noun sense 1 is a countable living bird; sense 2 is uncountable chicken meat. The draft's chicken in the garden is the living animal.","Retain living bird sense only for this example; do not conflate with uncountable meat or figurative coward sense. Myanmar ကြက် needs contextual clarification."],["bread","https://www.oxfordlearnersdictionaries.com/definition/english/bread",103,114,"Publisher lists the common food sense as uncountable; uses a loaf, slice or piece for counted portions. The draft's eat bread is grammatically compatible.","Do not incorrectly introduce countable 'a bread' in A1 example. Distinguish ordinary food sense from old-fashioned money slang."],["walk","https://www.oxfordlearnersdictionaries.com/definition/english/walk_1",103,141,"Publisher verb sense 1 describes moving on foot without running, and directly illustrates walking to school. The draft's We walk to school is consistent.","Oxford A1 PDF lists walk as verb and noun; this source page supports the physical-movement verb sense only. Human reviewer must separately determine exact-sense CEFR and fluent Myanmar."]]''')

def require(condition, why):
    if not condition:
        raise ValueError(why)

def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()

def rebuild():
    require(git_blob_sha(SHORT) == SHA, "Frozen shortlist SHA changed")
    source = json.loads(SHORT.read_text(encoding="utf-8"))
    require(source["counts_by_level"] == {l: 200 for l in LEVELS}, "Scope not 1000")
    require(source["independently_approved_by_level"] == {l: 0 for l in LEVELS}, "Forged approvals")
    require(len(source["entries"]) == 1000, "Incorrect 1000 shortlist")
    lookup = {(e["level"], e["word"]): e for e in source["entries"]}
    require(len(lookup) == 1000, "Duplicate word")
    records = []
    for word, url, start, end, observation, risk in LEADS:
        e = lookup[("A1", word)]
        require(e["editorial_hold"] is True and e["release_approved"] is False, "Lost hold")
        records.append({
            "word": word, "level": "A1", "part_of_speech": e["part_of_speech"],
            "shortlist_snapshot": {"english_definition": e["english_definition"],
                                   "myanmar_meaning": e["burmese_meaning"],
                                   "example_sentence": e["example_sentence"]},
            "shortlist_provenance": {"source_path": e["source_path"],
                                     "source_index": e["source_index"],
                                     "source_blob_sha": e["source_blob_sha"]},
            "publisher_source": {"publisher": "Oxford University Press",
                                 "dictionary": "Oxford Advanced Learner's Dictionary",
                                 "url": url, "observed_on": "2026-10-30",
                                 "web_extracted_line_start": start,
                                 "web_extracted_line_end": end,
                                 "access": "DIRECT_PUBLISHER_DICTIONARY_WEB_TEXT",
                                 "evidence_scope": "DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR",
                                 "oxford_3000_word_pos_reference": "A1",
                                 "exact_sense_cefr_label_observed": None},
            "direct_observation": observation, "editorial_risk": risk,
            "independent_reviewer_task": TASK, "editorial_hold": True,
            "independently_reviewed": False, "release_approved": False,
            "independent_reviewer_receipt": None,
        })
    return {"schema": 1, "scope": "CEFR_1000_STAGING_ONLY",
            "status": "A1_FOUR_DIRECT_DICTIONARY_SENSE_LEADS_UNAPPROVED",
            "observed_on": "2026-10-30", "shortlist_blob_sha": SHA,
            "record_count": 4, "independently_approved_count": 0,
            "source_limitations": LIMIT, "records": records}

def verify(candidate, expected):
    require(candidate == expected, "Direct sense packet changed or forged")
    return True

def self_test(expected):
    cases = [
        lambda x: x.update(record_count=3),
        lambda x: x.update(status="APPROVED"),
        lambda x: x.update(independently_approved_count=1),
        lambda x: x.update(shortlist_blob_sha="0" * 40),
        lambda x: x.update(source_limitations="approved"),
        lambda x: x["records"].reverse(),
        lambda x: x["records"].pop(),
        lambda x: x.update(extra_signoff=True),
    ]
    for i in range(4):
        cases.extend([
            lambda x, i=i: x["records"][i].update(word="fake"),
            lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(english_definition="fake"),
            lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(myanmar_meaning="မှား"),
            lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(example_sentence="Fake."),
            lambda x, i=i: x["records"][i]["shortlist_provenance"].update(source_path="fake"),
            lambda x, i=i: x["records"][i]["shortlist_provenance"].update(source_index=-1),
            lambda x, i=i: x["records"][i]["shortlist_provenance"].update(source_blob_sha="0"*40),
            lambda x, i=i: x["records"][i]["publisher_source"].update(url="https://example.invalid"),
            lambda x, i=i: x["records"][i]["publisher_source"].update(web_extracted_line_start=0),
            lambda x, i=i: x["records"][i]["publisher_source"].update(web_extracted_line_end=0),
            lambda x, i=i: x["records"][i]["publisher_source"].update(observed_on="2099-01-01"),
            lambda x, i=i: x["records"][i]["publisher_source"].update(exact_sense_cefr_label_observed="A1"),
            lambda x, i=i: x["records"][i].update(independently_reviewed=True),
            lambda x, i=i: x["records"][i].update(release_approved=True),
            lambda x, i=i: x["records"][i].update(independent_reviewer_receipt={"fake": True}),
        ])
    n = 0
    for mutate in cases:
        candidate = copy.deepcopy(expected)
        mutate(candidate)
        try:
            verify(candidate, expected)
        except ValueError:
            n += 1
            continue
        raise AssertionError("Forged Oxford exact-sense evidence accepted")
    require(n == 68, "Negative suite count drift")
    return n

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    expected = rebuild()
    verify(json.loads(PACKET.read_text(encoding="utf-8")), expected)
    count = self_test(expected) if args.self_test else 0
    print(json.dumps({"level": args.level, "direct_dictionary_sense_leads": 4,
                      "independent_exact_sense_approvals": 0,
                      "negative_mutations_rejected": count,
                      "release": "BLOCKED_STAGING_ONLY"}, sort_keys=True))

if __name__ == "__main__":
    main()
