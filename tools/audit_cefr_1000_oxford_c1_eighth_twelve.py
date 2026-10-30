#!/usr/bin/env python3
"""Fail-closed eighth C1 Oxford word/POS research auditor; NEVER a release approval.

Pinned official PDF locators and frozen shortlist content are compared to the
unapproved evidence packet. No independent linguistic or listening review is done.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-OXFORD-C1-EIGHTH-TWELVE-2026-10-30.json"
FROZEN = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
OBS = json.loads(r'''[["subsequently","B2",3,604,"subsequently adv.","Publisher B2 word/POS versus provisional C1. The adverb means after an earlier event; independently check natural Burmese temporal sequencing and whether C1 has a defensible sense-specific teaching rationale."],["privilege","C1",6,1619,"privilege n.","Distinguish special right/advantage from legal privilege and privileged social status; the members-only library example needs a natural noun sense and fluent Myanmar."],["unity","B2",3,671,"unity n.","Publisher B2 noun versus provisional C1. Verify social solidarity versus physical wholeness; distinguish Burmese စည်းလုံးညီညွတ်မှု from simple agreement."],["usage","B2",3,674,"usage n.","Publisher B2 noun versus provisional C1. The example is linguistic usage, not electricity consumption or ordinary use; require exact-sense publisher evidence and Myanmar register review."],["threshold","C1",7,1904,"threshold n.","Verify quantitative trigger point versus doorway threshold and figurative tolerance. The draft says passes a set threshold; reviewer should check exceeds/crosses collocation and technical Myanmar."],["consecutive","C1",4,966,"consecutive adj.","Verify uninterrupted sequence versus merely frequent occurrence; ensure consecutive months and Burmese ဆက်တိုက် are precise and not misread as continuous duration."],["preliminary","C1",6,1600,"preliminary adj.","Verify early findings before full investigation versus tentative/unconfirmed results; preserve adjective POS and natural Myanmar research register."],["backing","C1",4,815,"backing n.","The intended sense is practical/financial support, not physical backing material or a backing track; verify the gained backing collocation and Burmese."],["respective","C1",7,1712,"respective adj.","Check distributive one-to-one reference in their respective departments; Myanmar should express each manager's own department, not shared ownership."],["scenario","B2",3,551,"scenario n.","Publisher B2 noun versus provisional C1. Draft 'prepared a scenario for a supply shortage' may be awkward; review a realistic planning scenario and fluent Myanmar before independent signoff."],["trace","B2",3,649,"trace v.","Critical POS distinction: Oxford lists trace v. at B2 but trace n. at C1 (page 7 line 1920). Draft C1 uses verb 'trace the source'; do not borrow the noun C1 label."],["bias","B2",1,61,"bias n.","Publisher B2 noun versus provisional C1. Check unfair prejudice in hiring versus statistical bias and the scope of Burmese ဘက်လိုက်သော သဘောထား."]]''')
TASK = "Independent human reviewer must check exact-sense publisher CEFR evidence, English definition, natural Myanmar meaning, original example grammar/collocation, British pronunciation, source provenance and cross-level rationale; provide a content-bound independent receipt. Publisher word/POS listing and automated checks are not independent exact-sense approval."
LEVELS = ("A1", "A2", "B1", "B2", "C1")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def audit(packet, shortlist):
    require(blob_sha(SHORTLIST) == FROZEN, "Frozen shortlist blob changed")
    require(shortlist.get("counts_by_level") == {x: 200 for x in LEVELS}, "Scope changed")
    require(shortlist.get("independently_approved_by_level") == {x: 0 for x in LEVELS},
            "Fabricated independent approval")
    require(len(shortlist.get("entries", [])) == 1000, "Shortlist must have 1000")
    by_word = {x["word"]: x for x in shortlist["entries"]}
    require(len(by_word) == 1000, "Duplicate frozen headword")
    expected_top = {
        "schema": 1,
        "scope": "CEFR_1000_TOTAL_STAGING_ONLY",
        "status": "C1_EIGHTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD",
        "observed_on": "2026-10-30",
        "shortlist_blob_sha": FROZEN,
        "record_count": 12,
        "counts_by_level": {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 12},
        "publisher_reference_level_counts": {"B2": 6, "C1": 6},
        "word_pos_discrepancies": 6,
        "independently_approved_count": 0,
        "source_limitations": "Directly inspected Oxford 5000 PDF word/POS lines on 2026-10-30. Oxford list is not exact-sense CEFR evidence or human approval. All 12 remain on editorial hold; six publisher B2 word/POS levels conflict with provisional C1. The C1 noun trace listing must not be substituted for the B2 verb trace listing. All English/Myanmar/example text remains frozen and unverified.",
    }
    require(set(packet) == set(expected_top) | {"records"}, "Unexpected packet fields")
    for key, value in expected_top.items():
        require(packet.get(key) == value, "Packet metadata drift: " + key)
    rows = packet["records"]
    require(isinstance(rows, list) and len(rows) == 12, "Twelve records required")
    require(len({x.get("word") for x in rows}) == 12, "Repeated research word")
    record_keys = {"word", "level", "part_of_speech", "shortlist_snapshot",
                   "shortlist_provenance", "publisher_source", "editorial_risk",
                   "independent_reviewer_task", "editorial_hold", "independently_reviewed",
                   "release_approved", "independent_reviewer_receipt"}
    for i, (word, observed, page, line, excerpt, risk) in enumerate(OBS):
        row = rows[i]
        original = by_word[word]
        require(set(row) == record_keys, "Unknown or missing record fields: " + word)
        require(row["word"] == word and row["level"] == "C1"
                and original["level"] == "C1"
                and row["part_of_speech"] == original["part_of_speech"],
                "Draft word/POS drift: " + word)
        require(row["shortlist_snapshot"] == {
            "english_definition": original["english_definition"],
            "myanmar_meaning": original["burmese_meaning"],
            "example_sentence": original["example_sentence"],
        }, "Frozen English/Myanmar/example drift: " + word)
        require(row["shortlist_provenance"] == {
            "source_path": original["source_path"],
            "source_index": original["source_index"],
            "source_blob_sha": original["source_blob_sha"],
        }, "Historical Git provenance drift: " + word)
        require(row["publisher_source"] == {
            "publisher": "Oxford University Press",
            "title": "The Oxford 5000 by CEFR level",
            "url": URL,
            "observed_on": "2026-10-30",
            "pdf_page": page,
            "extracted_line": line,
            "source_excerpt": excerpt,
            "source_cefr_level": observed,
            "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT",
        }, "Direct publisher locator/level drift: " + word)
        require(row["editorial_risk"] == risk and row["independent_reviewer_task"] == TASK,
                "Pinned human review handoff changed: " + word)
        require(row["editorial_hold"] is True
                and row["independently_reviewed"] is False
                and row["release_approved"] is False
                and row["independent_reviewer_receipt"] is None,
                "Fabricated human approval: " + word)
        require(original["editorial_hold"] is True and original["release_approved"] is False
                and all(original.get("reviewed_" + field) is False for field in
                        ("english", "burmese", "example", "level", "pronunciation")),
                "Frozen shortlist review flag changed: " + word)
    return {"level": "C1", "observations": 12, "publisher_B2": 6,
            "publisher_C1": 6, "independently_approved": 0,
            "real_listening_signoffs": 0, "release": "BLOCKED_STAGING_ONLY"}


def self_test(packet, shortlist):
    cases = [
        ("word", lambda r: r.update(word="fake-word")),
        ("draft_level", lambda r: r.update(level="B1")),
        ("part_of_speech", lambda r: r.update(part_of_speech="fake")),
        ("english", lambda r: r["shortlist_snapshot"].update(english_definition="Forged.")),
        ("myanmar", lambda r: r["shortlist_snapshot"].update(myanmar_meaning="အမှား")),
        ("example", lambda r: r["shortlist_snapshot"].update(example_sentence="Forged example.")),
        ("historical_path", lambda r: r["shortlist_provenance"].update(source_path="draft/fake.json")),
        ("historical_index", lambda r: r["shortlist_provenance"].update(source_index=-1)),
        ("historical_blob", lambda r: r["shortlist_provenance"].update(source_blob_sha="0"*40)),
        ("publisher", lambda r: r["publisher_source"].update(publisher="Fake publisher")),
        ("pdf_url", lambda r: r["publisher_source"].update(url="https://example.invalid/fake.pdf")),
        ("date", lambda r: r["publisher_source"].update(observed_on="1900-01-01")),
        ("page", lambda r: r["publisher_source"].update(pdf_page=0)),
        ("line", lambda r: r["publisher_source"].update(extracted_line=-1)),
        ("excerpt", lambda r: r["publisher_source"].update(source_excerpt="fabricated n.")),
        ("source_cefr", lambda r: r["publisher_source"].update(source_cefr_level="A1")),
        ("scope", lambda r: r["publisher_source"].update(evidence_scope="EXACT_SENSE_APPROVED")),
        ("access", lambda r: r["publisher_source"].update(access="SEARCH_SNIPPET")),
        ("editorial_risk", lambda r: r.update(editorial_risk="forged")),
        ("human_task", lambda r: r.update(independent_reviewer_task="approved")),
        ("editorial_hold", lambda r: r.update(editorial_hold=False)),
        ("reviewed", lambda r: r.update(independently_reviewed=True)),
        ("release", lambda r: r.update(release_approved=True)),
        ("receipt", lambda r: r.update(independent_reviewer_receipt={"reviewer": "fake"})),
    ]
    n = 0
    for i in range(12):
        for label, change in cases:
            forged = copy.deepcopy(packet)
            before = json.dumps(forged["records"][i], ensure_ascii=False, sort_keys=True)
            change(forged["records"][i])
            require(before != json.dumps(forged["records"][i], ensure_ascii=False, sort_keys=True),
                    "Ineffective negative test: " + label)
            try:
                audit(forged, shortlist)
            except ValueError:
                n += 1
            else:
                raise AssertionError("Forged " + label + " accepted for " + OBS[i][0])
    global_cases = [
        ("count", lambda p: p.update(record_count=11)),
        ("level_count", lambda p: p["publisher_reference_level_counts"].update(B2=7)),
        ("false_approval", lambda p: p.update(independently_approved_count=1)),
        ("source_date", lambda p: p.update(observed_on="1900-01-01")),
        ("remove_record", lambda p: p["records"].pop()),
        ("invent_top_field", lambda p: p.update(approved=True)),
    ]
    for label, change in global_cases:
        forged = copy.deepcopy(packet)
        before = json.dumps(forged, ensure_ascii=False, sort_keys=True)
        change(forged)
        require(before != json.dumps(forged, ensure_ascii=False, sort_keys=True),
                "Ineffective global negative test: " + label)
        try:
            audit(forged, shortlist)
        except ValueError:
            n += 1
        else:
            raise AssertionError("Forged packet " + label + " accepted")
    require(n == 12*len(cases)+len(global_cases), "Negative test count drift")
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    result = audit(packet, shortlist)
    if args.self_test:
        n = self_test(packet, shortlist)
        print("PASS: %d/%d eighth C1 adversarial mutations rejected" % (n, n))
    print(json.dumps({"requested_level": args.level, **result},
                     ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
