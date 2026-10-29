#!/usr/bin/env python3
"""Fail-closed audit of 11 new A1 Oxford PDF word/POS observations; NEVER approves review.

All publisher excerpts and line locators are fixed from direct inspection of
Oxford 3000 official PDF on 2026-10-30. This is not independent exact-sense QA.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-FOURTEENTH-ELEVEN-2026-10-30.json"
SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LIMIT = "Official Oxford 3000 by CEFR level PDF directly inspected 2026-10-30. Eleven A1 lemma/number/verb word-POS observations, not independent exact-sense CEFR approval. Inflected is/are/does/did are NOT independent Oxford headword observations; rabbit remains unlisted in inspected core lists and unresolved. Number versus clock-time uses, lexical do versus auxiliary do, wake/wake up and sleep example grammar require independent bilingual/editorial review. No final audio listening, physical iPhone, hosting or deployment verification."
TASK = "Independent human reviewer: verify Oxford word/POS against intended A1 exact sense and CEFR applicability; check fluent Myanmar meaning, number/classifier or verb grammar, original example alignment, British usage, pronunciation and frozen Git provenance. Publisher wordlist observation alone is not approval."
ANCHORS = json.loads(r'''[["do",1,216,"do1 v., auxiliary v.","Publisher lists lemma do (verb/auxiliary), not does/did as separate headwords. Draft uses lexical do homework; distinguish auxiliary usage."],["four",2,309,"four number","Cardinal four is A1; example counts chairs. Review Burmese classifier usage and numeral headword policy."],["five",2,295,"five number","Cardinal five is A1; example counts books. Myanmar ငါး also denotes fish, so require context-sensitive bilingual review."],["six",3,703,"six number","Cardinal six is A1; example counts students. Check numeral pronunciation and Myanmar classifier."],["seven",3,682,"seven number","Cardinal seven is A1; seven days in a week is grammatical, but exact example and translation need independent review."],["eight",1,236,"eight number","Cardinal eight is A1; example at eight refers to eight o'clock, not a quantity of eight objects. Sense/context mismatch requires review."],["nine",2,523,"nine number","Cardinal nine is A1; shop opens at nine refers to clock time, not counting objects. Independent exact-context check required."],["ten",3,773,"ten number","Cardinal ten is A1; example counts pencils. Check Myanmar quantity/classifier and British pronunciation."],["sleep",3,708,"sleep v.","Oxford A1 lists verb sleep; draft I sleep eight hours may be less idiomatic than I sleep for eight hours/I get eight hours' sleep. Human grammar review required."],["wake",4,854,"wake v.","Oxford A1 lists wake verb; draft I wake at seven omits up and can mean wake from sleep. Check wake/wake up usage and Myanmar နိုး vs အိပ်ရာထ."],["speak",3,727,"speak v.","Oxford A1 lists speak verb; example I speak English at school uses language ability/use, not simply saying words aloud. Definition-example sense alignment needs review."]]''')


def require(ok, why):
    if not ok:
        raise ValueError(why)


def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def rebuild():
    require(git_blob_sha(SHORT) == SHA, "Frozen shortlist blob changed")
    source = json.loads(SHORT.read_text(encoding="utf-8"))
    require(source["counts_by_level"] == {l: 200 for l in LEVELS}, "Wrong 1000 scope")
    require(source["independently_approved_by_level"] == {l: 0 for l in LEVELS}, "Forged approvals")
    require(len(source["entries"]) == 1000, "Wrong number of first-pass words")
    lookup = {(r["level"], r["word"]): r for r in source["entries"]}
    require(len(lookup) == 1000, "Duplicate shortlist words")
    records = []
    for word, page, line, excerpt, discrepancy in ANCHORS:
        e = lookup[("A1", word)]
        require(e["editorial_hold"] is True and e["release_approved"] is False,
                "A1 editorial hold lost: " + word)
        records.append({
            "word": word,
            "level": "A1",
            "part_of_speech": e["part_of_speech"],
            "shortlist_snapshot": {
                "english_definition": e["english_definition"],
                "myanmar_meaning": e["burmese_meaning"],
                "example_sentence": e["example_sentence"],
            },
            "shortlist_provenance": {
                "source_path": e["source_path"],
                "source_index": e["source_index"],
                "source_blob_sha": e["source_blob_sha"],
            },
            "publisher_source": {
                "publisher": "Oxford University Press",
                "title": "The Oxford 3000 by CEFR level",
                "url": URL,
                "observed_on": "2026-10-30",
                "pdf_page": page,
                "extracted_line": line,
                "source_excerpt": excerpt,
                "source_cefr_level": "A1",
                "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT",
            },
            "editorial_discrepancy": discrepancy,
            "editorial_risk": "A1_FOURTEENTH_ELEVEN_" + word.upper() + "_EXACT_SENSE_POS_REVIEW",
            "independent_reviewer_task": TASK,
            "editorial_hold": True,
            "independently_reviewed": False,
            "release_approved": False,
            "independent_reviewer_receipt": None,
        })
    require(len({r["word"] for r in records}) == 11, "Duplicate fourteenth-batch word")
    return {
        "schema": 1,
        "scope": "CEFR_1000_TOTAL_STAGING_ONLY",
        "status": "A1_FOURTEENTH_ELEVEN_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD",
        "observed_on": "2026-10-30",
        "shortlist_blob_sha": SHA,
        "record_count": 11,
        "counts_by_level": {"A1": 11, "A2": 0, "B1": 0, "B2": 0, "C1": 0},
        "publisher_reference_level_counts": {"A1": 11, "A2": 0, "B1": 0, "B2": 0, "C1": 0},
        "draft_pos_reconciliation_count": 0,
        "independently_approved_count": 0,
        "source_limitations": LIMIT,
        "records": records,
    }


def verify(candidate, expected):
    # Strict deep equality rejects extra fields, count-preserving tampering,
    # invented receipts and any changes to original Myanmar/example/provenance.
    require(candidate == expected, "Fourteenth A1 packet differs from frozen source anchors")
    return True


def self_test(expected):
    n = 0
    mutations = [
        lambda x: x.update(record_count=10),
        lambda x: x.update(independently_approved_count=1),
        lambda x: x.update(draft_pos_reconciliation_count=1),
        lambda x: x.update(status="READY"),
        lambda x: x.update(shortlist_blob_sha="0" * 40),
        lambda x: x.update(extra_approval=True),
        lambda x: x["records"].reverse(),
        lambda x: x["records"].pop(),
        lambda x: x["records"].append(copy.deepcopy(x["records"][0])),
        lambda x: x["counts_by_level"].update(A1=10),
    ]
    for i in range(11):
        mutations.extend([
            lambda x, i=i: x["records"][i].update(word="fake"),
            lambda x, i=i: x["records"][i].update(level="A2"),
            lambda x, i=i: x["records"][i].update(part_of_speech="fake"),
            lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(english_definition="fake"),
            lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(myanmar_meaning="မှား"),
            lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(example_sentence="Fake."),
            lambda x, i=i: x["records"][i]["shortlist_provenance"].update(source_blob_sha="0" * 40),
            lambda x, i=i: x["records"][i]["publisher_source"].update(url="https://example.invalid/fake"),
            lambda x, i=i: x["records"][i]["publisher_source"].update(source_excerpt="fake n."),
            lambda x, i=i: x["records"][i]["publisher_source"].update(pdf_page=99),
            lambda x, i=i: x["records"][i]["publisher_source"].update(extracted_line=999),
            lambda x, i=i: x["records"][i]["publisher_source"].update(source_cefr_level="C1"),
            lambda x, i=i: x["records"][i].update(editorial_discrepancy="none"),
            lambda x, i=i: x["records"][i].update(editorial_risk="none"),
            lambda x, i=i: x["records"][i].update(independent_reviewer_task="approved"),
            lambda x, i=i: x["records"][i].update(editorial_hold=False),
            lambda x, i=i: x["records"][i].update(independently_reviewed=True),
            lambda x, i=i: x["records"][i].update(release_approved=True),
            lambda x, i=i: x["records"][i].update(independent_reviewer_receipt={"fake": True}),
        ])
    for mutation in mutations:
        test = copy.deepcopy(expected)
        mutation(test)
        require(test != expected, "Ineffective adversarial mutation")
        try:
            verify(test, expected)
        except ValueError:
            n += 1
            continue
        raise AssertionError("Fourteenth A1 forged evidence accepted")
    require(n == 219, "Fourteenth A1 adversarial suite count drift")
    return n


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    expected = rebuild()
    actual = json.loads(PACKET.read_text(encoding="utf-8"))
    verify(actual, expected)
    n = self_test(expected) if args.self_test else 0
    print(json.dumps({
        "level": args.level,
        "a1_observations": 11,
        "draft_pos_reconciliation_count": 0,
        "independently_approved": 0,
        "forged_mutations_rejected": n,
        "release": "BLOCKED_STAGING_ONLY",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
