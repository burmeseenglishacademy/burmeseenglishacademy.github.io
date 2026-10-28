#!/usr/bin/env python3
"""Fail-closed staging-only source/snapshot audit for 12 Oxford A2 follow-up observations.

Oxford PDF word/POS levels do NOT constitute independent exact-sense CEFR,
Myanmar, English, example, pronunciation or listening approval.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-FOLLOWUP-TWELVE-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
STATUS = "DIRECT_OXFORD_A2_FOLLOWUP_WORD_POS_TRIAGE_NOT_INDEPENDENT_APPROVAL"
SCOPE = "OXFORD_3000_WORD_POS_LEVEL_ONLY_NOT_EXACT_SENSE"
EXPECTED = {
    "case": ("A2", "n.", 4, 1027),
    "person": ("A1", "n.", 3, 586),
    "change": ("A1", "v., n.", 1, 139),
    "enough": ("A1", "det., pron., adv.", 1, 245),
    "believe": ("A1", "v.", 1, 79),
    "job": ("A1", "n.", 2, 410),
    "later": ("A1", "adv.", 2, 428),
    "line": ("A1", "n.", 2, 444),
    "order": ("A1", "n., v.", 3, 559),
    "service": ("A2", "n.", 6, 1602),
    "season": ("A2", "n.", 6, 1590),
    "area": ("A1", "n.", 1, 41),
}
ROW_FIELDS = {
    "word", "level", "part_of_speech", "source_cefr", "source_pos",
    "source_entry", "source_scope", "source_url", "source_authority",
    "source_document", "pdf_page_1_based", "pdf_extracted_line_0_based",
    "observed_on", "source_access", "shortlist_english_definition",
    "shortlist_myanmar_meaning", "shortlist_example", "shortlist_source_path",
    "shortlist_source_index", "shortlist_source_blob_sha", "editorial_risk",
    "independent_review_task", "editorial_hold", "independently_reviewed",
    "release_approved", "reviewer_receipt"
}
TOP_FIELDS = {
    "schema", "scope", "status", "observed_on", "shortlist_blob_sha",
    "source_url", "record_count", "counts_by_level",
    "publisher_reference_level_counts", "word_pos_discrepancies",
    "independently_approved_count", "provenance_note", "records"
}

def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def audit(packet, shortlist, raw):
    errors = []
    if not isinstance(packet, dict):
        return ["packet must be an object"]
    if set(packet) != TOP_FIELDS:
        errors.append("packet top-level schema drift")
    expected_top = {
        "schema": 1, "scope": "CEFR_1000_TOTAL_STAGING_ONLY",
        "status": STATUS, "observed_on": "2026-10-28",
        "source_url": URL, "record_count": 12,
        "counts_by_level": {"A1": 0, "A2": 12, "B1": 0, "B2": 0, "C1": 0},
        "publisher_reference_level_counts": {"A1": 9, "A2": 3},
        "word_pos_discrepancies": 9, "independently_approved_count": 0,
        "shortlist_blob_sha": blob_sha(raw),
    }
    for key, value in expected_top.items():
        if packet.get(key) != value:
            errors.append("packet " + key + " drift")
    note = packet.get("provenance_note")
    if not isinstance(note, str) or not all(
        phrase in note.lower() for phrase in
        ("direct official oxford", "word/pos", "not independent", "zero human")
    ):
        errors.append("publisher scope caveat missing")
    entries = shortlist.get("entries", [])
    if (len(entries) != 1000 or shortlist.get("counts_by_level") !=
            {x: 200 for x in ("A1", "A2", "B1", "B2", "C1")}):
        errors.append("canonical shortlist 1000/level counts drift")
    lookup = {(x.get("word"), x.get("level")): x for x in entries}
    rows = packet.get("records")
    if not isinstance(rows, list):
        return errors + ["records not a list"]
    if len(rows) != 12 or {r.get("word") for r in rows if isinstance(r, dict)} != set(EXPECTED):
        errors.append("missing, extra or duplicate source headwords")
    for row in rows:
        if not isinstance(row, dict):
            errors.append("malformed record")
            continue
        word = row.get("word")
        if word not in EXPECTED:
            errors.append("unexpected word " + str(word))
            continue
        cefr, pos, page, line = EXPECTED[word]
        if set(row) != ROW_FIELDS:
            errors.append(word + ": row schema drift")
        expected_values = {
            "level": "A2", "source_cefr": cefr, "source_pos": pos,
            "source_entry": word + " " + pos, "source_scope": SCOPE,
            "source_url": URL, "source_authority": "Oxford University Press",
            "source_document": "The Oxford 3000 by CEFR level",
            "pdf_page_1_based": page, "pdf_extracted_line_0_based": line,
            "observed_on": "2026-10-28",
            "source_access": "DIRECT_OFFICIAL_OUP_PDF_TEXT",
            "editorial_hold": True, "independently_reviewed": False,
            "release_approved": False, "reviewer_receipt": None,
        }
        for key, value in expected_values.items():
            if row.get(key) != value:
                errors.append(word + ": source/hold drift " + key)
        entry = lookup.get((word, "A2"))
        if not entry:
            errors.append(word + ": canonical A2 entry missing")
            continue
        snapshots = {
            "part_of_speech": "part_of_speech",
            "shortlist_english_definition": "english_definition",
            "shortlist_myanmar_meaning": "burmese_meaning",
            "shortlist_example": "example_sentence",
            "shortlist_source_path": "source_path",
            "shortlist_source_index": "source_index",
            "shortlist_source_blob_sha": "source_blob_sha",
        }
        for field, canonical in snapshots.items():
            if row.get(field) != entry.get(canonical):
                errors.append(word + ": snapshot drift " + field)
        if not all(entry.get(k) is False for k in
                   ("reviewed_english", "reviewed_burmese", "reviewed_example",
                    "reviewed_level", "reviewed_pronunciation", "release_approved")):
            errors.append(word + ": canonical false approval")
        if entry.get("editorial_hold") is not True:
            errors.append(word + ": canonical hold removed")
        risk = row.get("editorial_risk")
        task = row.get("independent_review_task")
        if not isinstance(risk, str) or len(risk) < 90:
            errors.append(word + ": substantive editorial risk missing")
        if (not isinstance(task, str) or len(task) < 250 or
                word not in task or "Oxford 3000 lists " + word + " at " + cefr not in task or
                "independent human" not in task or "content SHA256" not in task):
            errors.append(word + ": human independent-review task missing")
    return errors

def negative_cases(packet):
    tests = []
    def changed(label, fn):
        obj = copy.deepcopy(packet)
        fn(obj)
        tests.append((label, obj))
    changed("false approved total", lambda x: x.update(independently_approved_count=12))
    changed("hide conflicts", lambda x: x.update(word_pos_discrepancies=0))
    changed("forge publisher counts", lambda x: x.update(publisher_reference_level_counts={"A1": 0, "A2": 12}))
    changed("wrong shortlist hash", lambda x: x.update(shortlist_blob_sha="0" * 40))
    changed("wrong source URL", lambda x: x.update(source_url="https://example.com/pdf"))
    changed("wrong observation date", lambda x: x.update(observed_on="2026-10-29"))
    changed("missing record", lambda x: x["records"].pop())
    changed("duplicate record", lambda x: x["records"].append(copy.deepcopy(x["records"][0])))
    changed("fake row approval", lambda x: x["records"][0].update(release_approved=True))
    changed("fake reviewer receipt", lambda x: x["records"][0].update(reviewer_receipt={"reviewer_id": "bot"}))
    changed("fake independent review", lambda x: x["records"][0].update(independently_reviewed=True))
    changed("remove editorial hold", lambda x: x["records"][0].update(editorial_hold=False))
    changed("change Myanmar", lambda x: x["records"][0].update(shortlist_myanmar_meaning="မှားနေသော"))
    changed("change English", lambda x: x["records"][0].update(shortlist_english_definition="different"))
    changed("change example", lambda x: x["records"][0].update(shortlist_example="Different example."))
    changed("change source POS", lambda x: x["records"][0].update(source_pos="v."))
    changed("change source CEFR", lambda x: x["records"][0].update(source_cefr="C1"))
    changed("change PDF page", lambda x: x["records"][0].update(pdf_page_1_based=12))
    changed("change PDF line", lambda x: x["records"][0].update(pdf_extracted_line_0_based=999))
    changed("change upstream blob", lambda x: x["records"][0].update(shortlist_source_blob_sha="0" * 40))
    changed("remove task", lambda x: x["records"][0].update(independent_review_task=""))
    changed("remove risk", lambda x: x["records"][0].update(editorial_risk=""))
    changed("replace publisher", lambda x: x["records"][0].update(source_authority="Wikipedia"))
    changed("source scope fraud", lambda x: x["records"][0].update(source_scope="INDEPENDENT_EXACT_SENSE_CEFR_APPROVED"))
    return tests

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=["A1", "A2", "B1", "B2", "C1", "ALL"], default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    errors = audit(packet, shortlist, raw)
    rejected = 0
    if args.self_test and not errors:
        for label, mutation in negative_cases(packet):
            if not audit(mutation, shortlist, raw):
                errors.append("accepted forged mutation: " + label)
            else:
                rejected += 1
    print(json.dumps({
        "level": args.level, "a2_followup_observations": 12,
        "oxford_a1_word_pos_conflicts": 9, "oxford_a2_word_pos_matches": 3,
        "independently_approved": 0, "negative_mutations_rejected": rejected,
        "errors": errors, "status": "PASS_STRUCTURE_STILL_HOLD" if not errors else "FAIL"
    }, ensure_ascii=False))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
