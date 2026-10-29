#!/usr/bin/env python3
"""Fail-closed Cambridge indexed-sense / Oxford word-POS A1 cross-publisher hold auditor.

Publisher search-indexed text is not a complete direct dictionary page review,
independent human signoff, a CEFR promotion, or authority to publish.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_PATH = ROOT / "draft/CEFR-1000-CAMBRIDGE-A1-FAMILY-AND-EVERYDAY-TWELVE-2026-10-29.json"
OXFORD_PATH = ROOT / "draft/CEFR-1000-OXFORD-A1-NINTH-TWELVE-2026-10-29.json"
SHORTLIST_PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
LABELS = {
  "sister": "A1",
  "son": "A1",
  "daughter": "A1",
  "grandmother": "A2",
  "grandfather": "A2",
  "uncle": "A2",
  "aunt": "A2",
  "phone": "A1",
  "computer": "A1",
  "picture": "A1",
  "bag": "A1",
  "money": "A1"
}
URLS = {
  "sister": "https://dictionary.cambridge.org/dictionary/english/sister",
  "son": "https://dictionary.cambridge.org/dictionary/english/son",
  "daughter": "https://dictionary.cambridge.org/dictionary/english/daughter",
  "grandmother": "https://dictionary.cambridge.org/dictionary/english/grandmother",
  "grandfather": "https://dictionary.cambridge.org/dictionary/english/grandfather",
  "uncle": "https://dictionary.cambridge.org/dictionary/learner-english/uncle",
  "aunt": "https://dictionary.cambridge.org/dictionary/english/aunt",
  "phone": "https://dictionary.cambridge.org/dictionary/english/phone",
  "computer": "https://dictionary.cambridge.org/dictionary/english/computer",
  "picture": "https://dictionary.cambridge.org/dictionary/english/picture",
  "bag": "https://dictionary.cambridge.org/dictionary/english/bag",
  "money": "https://dictionary.cambridge.org/dictionary/english/money"
}
NOTES = {
  "sister": "Sibling sense; Myanmar အစ်မ/ညီမ distinguishes older and younger sisters. Exclude nun and ward nurse senses.",
  "son": "Male child relative to a parent; exclude forms of address and figurative 'son of' uses.",
  "daughter": "Female child relative to a parent; do not confuse with stepdaughter or daughter-in-law.",
  "grandmother": "Cambridge explicitly labels the same parental-mother sense A2, whereas Oxford word/POS list has A1. Preserve conflict, do not automatically retier. Myanmar အဘွား/အဖွား spelling and maternal/paternal nuance need native review.",
  "grandfather": "Cambridge explicitly labels parental-father sense A2 versus Oxford A1 word/POS. Preserve conflict; review Myanmar kinship and family-side phrasing.",
  "uncle": "Cambridge A2 kinship sense versus Oxford A1 word/POS. Check parent sibling vs marriage and Myanmar relative distinctions; no automatic retiering.",
  "aunt": "Cambridge A2 kinship sense versus Oxford A1 word/POS. Check parent sibling vs marriage and Myanmar relative distinctions; no automatic retiering.",
  "phone": "Cambridge A1 communication device noun; distinct from verb phone and specialized phonetics noun. The original example fits device noun.",
  "computer": "Cambridge A1 information-processing machine noun; ensure definition does not overgeneralize all electronic devices.",
  "picture": "Cambridge A1 drawing/painting/photo image noun; distinct from B2 screen image and C1 imagine verb. Example is ambiguous without context.",
  "bag": "Cambridge A1 carrying-container noun; review bag versus suitcase/handbag and whether Myanmar အိတ် is sufficiently natural.",
  "money": "Cambridge A1 uncountable noun including an amount of funds, not exclusively physical cash; original definition coins and notes may be too narrow. Keep rewrite proposal on hold."
}
REVIEW_TASK = ("Independent human reviewer must access the actual publisher sense, reconcile Oxford word/POS and Cambridge sense labels, check original English definition, fluent Myanmar meaning, example grammar, British usage and source provenance; document identity and signed evidence. No automatic approval or retiering.")
SCOPE = "PUBLISHER_OWNED_SEARCH_INDEXED_EXACT_SENSE_LEAD_NOT_HUMAN_VERIFICATION"
ACCESS = "SEARCH_INDEXED_PUBLISHER_PAGE_TEXT_DIRECT_PAGE_HTTP_403"

def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()

def audit(packet, oxford, shortlist, oxford_sha, shortlist_sha):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "scope/schema")
    require(packet.get("status") == "A1_TWELVE_CAMBRIDGE_INDEXED_SENSE_LEADS_EDITORIAL_HOLD", "status/hold")
    require(packet.get("observed_on") == "2026-10-29", "observation date")
    require(packet.get("shortlist_blob_sha") == shortlist_sha and packet.get("oxford_packet_blob_sha") == oxford_sha, "source blob binding")
    require(packet.get("record_count") == 12 and packet.get("counts_by_level") == {"A1": 12, "A2": 0, "B1": 0, "B2": 0, "C1": 0}, "counts")
    require(packet.get("cambridge_sense_label_counts") == {"A1": 8, "A2": 4}, "sense counts")
    require(packet.get("independently_approved_count") == 0, "false approval count")
    require("403" in str(packet.get("limitations")) and "NOT" in str(packet.get("limitations")), "access limitations")
    require(len(shortlist.get("entries", [])) == 1000 and shortlist.get("counts_by_level") == {x: 200 for x in LEVELS}, "shortlist scope")
    require(shortlist.get("independently_approved_by_level") == {x: 0 for x in LEVELS}, "shortlist approvals")
    require(all(x.get("editorial_hold") is True and x.get("release_approved") is False and all(x.get(k) is False for k in ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation")) for x in shortlist.get("entries", [])), "shortlist independent hold")
    rows = packet.get("records")
    if not isinstance(rows, list) or len(rows) != 12:
        return errors + ["exactly 12 records required"]
    oxford_map = {x["word"]: x for x in oxford["records"]}
    canonical = {(x["word"], x["level"]): x for x in shortlist["entries"]}
    seen = set()
    for r in rows:
        if not isinstance(r, dict):
            errors.append("malformed record")
            continue
        word = r.get("word")
        if word not in LABELS or word in seen:
            errors.append("unknown/duplicate word " + str(word))
            continue
        seen.add(word)
        o, c = oxford_map.get(word), canonical.get((word, "A1"))
        if o is None or c is None:
            errors.append("missing canonical/Oxford word " + word)
            continue
        expected_snapshot = {"english_definition": c.get("english_definition"), "myanmar_meaning": c.get("burmese_meaning"), "example_sentence": c.get("example_sentence")}
        expected_provenance = {"source_path": c.get("source_path"), "source_index": c.get("source_index"), "source_blob_sha": c.get("source_blob_sha")}
        for field, expected in (
            ("level", "A1"), ("part_of_speech", c.get("part_of_speech")),
            ("shortlist_snapshot", expected_snapshot), ("shortlist_provenance", expected_provenance),
            ("oxford_packet_path", "draft/CEFR-1000-OXFORD-A1-NINTH-TWELVE-2026-10-29.json"),
            ("oxford_packet_blob_sha", oxford_sha),
            ("oxford_word_pos_level", o["publisher_source"]["source_cefr_level"]),
            ("oxford_pdf_page", o["publisher_source"]["pdf_page"]),
            ("oxford_extracted_line", o["publisher_source"]["extracted_line"]),
            ("oxford_source_excerpt", o["publisher_source"]["source_excerpt"]),
            ("editorial_discrepancy", NOTES[word]),
            ("independent_reviewer_task", REVIEW_TASK),
            ("editorial_hold", True), ("independently_reviewed", False),
            ("release_approved", False), ("independent_reviewer_receipt", None),
        ):
            if r.get(field) != expected:
                errors.append(word + ": " + field + " drift")
        s = r.get("cambridge_source")
        expected_source = {
            "publisher": "Cambridge University Press & Assessment",
            "url": URLS[word], "observed_on": "2026-10-29",
            "cefr_label": LABELS[word], "part_of_speech": "noun",
            "evidence_scope": SCOPE, "access": ACCESS, "source_excerpt": None,
        }
        if s != expected_source:
            errors.append(word + ": Cambridge source URL, label, access, or scope drift")
        if o.get("shortlist_snapshot") != expected_snapshot or o.get("shortlist_provenance") != expected_provenance:
            errors.append(word + ": upstream Oxford / frozen shortlist mismatch")
        if o.get("editorial_hold") is not True or o.get("independently_reviewed") is not False or o.get("release_approved") is not False:
            errors.append(word + ": upstream Oxford approval drift")
    require(seen == set(LABELS), "missing required words")
    require(sum(LABELS[x] == "A2" for x in seen) == 4, "four unresolved cross-publisher conflicts")
    return errors

def negative_tests(packet, oxford, shortlist, oxford_sha, shortlist_sha):
    mutations = 0
    for i in range(12):
        for path, value in [
            (("word",), "forged"), (("level",), "A2"),
            (("shortlist_snapshot", "english_definition"), "forged definition"),
            (("shortlist_snapshot", "myanmar_meaning"), "အတည်ပြုပြီး"),
            (("shortlist_snapshot", "example_sentence"), "Fake example."),
            (("shortlist_provenance", "source_blob_sha"), "0" * 40),
            (("oxford_pdf_page",), 999), (("oxford_source_excerpt",), "fake n."),
            (("cambridge_source", "url"), "https://example.com"),
            (("cambridge_source", "cefr_label"), "C1"),
            (("cambridge_source", "observed_on"), "2026-10-30"),
            (("cambridge_source", "access"), "DIRECT_PUBLISHER_FULL_PAGE"),
            (("cambridge_source", "source_excerpt"), "fabricated quotation"),
            (("editorial_discrepancy",), "resolved"),
            (("independent_reviewer_task",), "auto-approved"),
            (("editorial_hold",), False), (("independently_reviewed",), True),
            (("release_approved",), True), (("independent_reviewer_receipt",), {"reviewer": "fake"}),
        ]:
            obj = copy.deepcopy(packet)
            cur = obj["records"][i]
            for key in path[:-1]:
                cur = cur[key]
            cur[path[-1]] = value
            if not audit(obj, oxford, shortlist, oxford_sha, shortlist_sha):
                raise AssertionError("mutant escaped: " + str(i) + " " + "/".join(path))
            mutations += 1
    for field, value in [
        ("record_count", 13), ("independently_approved_count", 1),
        ("status", "APPROVED"), ("shortlist_blob_sha", "0" * 40),
        ("cambridge_sense_label_counts", {"A1": 12, "A2": 0}),
    ]:
        obj = copy.deepcopy(packet)
        obj[field] = value
        if not audit(obj, oxford, shortlist, oxford_sha, shortlist_sha):
            raise AssertionError("header mutant escaped: " + field)
        mutations += 1
    obj = copy.deepcopy(packet)
    obj["records"][1] = copy.deepcopy(obj["records"][0])
    if not audit(obj, oxford, shortlist, oxford_sha, shortlist_sha):
        raise AssertionError("duplicate mutant escaped")
    return mutations + 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    raw_oxford, raw_shortlist = OXFORD_PATH.read_bytes(), SHORTLIST_PATH.read_bytes()
    oxford, shortlist = json.loads(raw_oxford), json.loads(raw_shortlist)
    packet = json.loads(PACKET_PATH.read_text(encoding="utf-8"))
    oxford_sha, shortlist_sha = blob_sha(raw_oxford), blob_sha(raw_shortlist)
    issues = audit(packet, oxford, shortlist, oxford_sha, shortlist_sha)
    tested = negative_tests(packet, oxford, shortlist, oxford_sha, shortlist_sha) if args.self_test and not issues else 0
    count = sum(r["level"] == args.level or args.level == "ALL" for r in packet["records"])
    report = {"level": args.level, "cambridge_indexed_sense_leads": count,
              "cross_publisher_A1_vs_A2_conflicts": 4 if args.level in ("A1", "ALL") else 0,
              "independently_approved": 0, "negative_mutations_rejected": tested,
              "status": "PASS_STRUCTURE_EDITORIAL_HOLD_ONLY" if not issues else "FAIL",
              "errors": issues}
    print(json.dumps(report, ensure_ascii=False))
    if issues:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
