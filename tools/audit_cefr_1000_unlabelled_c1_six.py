#!/usr/bin/env python3
"""Fail-closed integrity audit of six unlabelled Cambridge C1 editorial leads.

These publisher-indexed observations have NO visible Cambridge CEFR label.
No source triage, automated tests or reviewer-like JSON field is independent
human signoff. This script never publishes or approves curriculum content.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "draft/CEFR-1000-CAMBRIDGE-UNLABELLED-C1-SIX-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
STATUS = "UNLABELLED_CAMBRIDGE_C1_FORMAL_SENSE_TRIAGE_NOT_APPROVAL"
TRIAGE = "UNLABELLED_FORMAL_PUBLISHER_SENSE_REQUIRES_INDEPENDENT_C1_PROOF"
EXPECTED = {
    "abstruse": {
        "sense_heading": "adjective (complex or hard to understand)",
        "source_observation": "Cambridge describes a difficult-to-understand adjective, marked formal; no CEFR label visible in publisher-indexed excerpt.",
        "editorial_risk": "Cambridge meaning is compatible with the draft; neither the index nor a generic advanced-register label establishes C1. Independently verify source-specific C1 classification or replace.",
        "myanmar_review_prompt": "Review whether 'အယူအဆများ အလွန်ရှုပ်ထွေး၍' unnecessarily restricts abstruse to ideas; original example grammar and teaching suitability require external signoff."
    },
    "equivocate": {
        "sense_heading": "verb [I] (intentionally evasive speech)",
        "source_observation": "Cambridge marks an intransitive formal verb for deliberately unclear speech, often to conceal truth; no CEFR label visible.",
        "editorial_risk": "Draft defines evasion of a direct answer but omits the possible concealment-of-truth nuance. Verify grammar of 'began to equivocate' and source-backed C1 label.",
        "myanmar_review_prompt": "Review Myanmar 'တိုက်ရိုက်အဖြေမပေးလိုသဖြင့်' as an overly narrow motive; distinguish equivocating from simply being uncertain."
    },
    "obfuscate": {
        "sense_heading": "verb [T or I] (make meaning unclear)",
        "source_observation": "Cambridge formal sense covers making an issue harder to understand, often intentionally; also separately lists online-data and source-code senses; no CEFR label visible.",
        "editorial_risk": "Draft definition asserts deliberate action while example 'jargon can obfuscate' does not imply intent; align exact sense, agency and example before approval.",
        "myanmar_review_prompt": "Review whether 'ရည်ရွယ်ချက်ရှိရှိ' misrepresents accidental obscurity in example; do not conflate technical obfuscation with general unclear communication."
    },
    "fortitude": {
        "sense_heading": "noun [U] (enduring hardship courage)",
        "source_observation": "Cambridge marks an uncountable formal noun for sustained courage when facing difficulty; no CEFR label visible.",
        "editorial_risk": "Draft adds patience; review whether patience is a necessary component of the sense. Original example is plausible but not independently checked.",
        "myanmar_review_prompt": "Myanmar gloss 'သတ္တိနှင့် ခံနိုင်ရည်' may be reasonable; confirm natural wording and distinction from mere endurance."
    },
    "alacrity": {
        "sense_heading": "noun [U] (eager speed)",
        "source_observation": "Cambridge marks an uncountable formal noun combining readiness or eagerness with quick action; no CEFR label visible.",
        "editorial_risk": "Draft adds cheerfulness; review whether this extra emotional quality is necessary and whether 'responded with alacrity' is idiomatic.",
        "myanmar_review_prompt": "Myanmar gloss includes 'ပျော်ရွှင်စွာ' which may overstate happiness; independently assess willingness and speed without overtranslation."
    },
    "salience": {
        "sense_heading": "noun [U] (contextual importance/relevance)",
        "source_observation": "Cambridge marks an uncountable formal noun for relevance or importance to the matter under discussion; no CEFR label visible.",
        "editorial_risk": "Draft blends noticeable prominence with importance. Distinguish discourse relevance from perceptual salience; verify 'salience of safety concerns' collocation.",
        "myanmar_review_prompt": "Myanmar 'အထူးထင်ရှားပြီး အရေးပါနေမှု' may conflate prominence and relevance; check against chosen publisher sense."
    }
}


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def audit(data, shortlist, raw, level="ALL"):
    errors = []
    if not isinstance(data, dict):
        return ["evidence must be object"]
    rows = data.get("records")
    if not isinstance(rows, list):
        return ["records must be array"]
    if data.get("schema") != 1 or data.get("status") != STATUS:
        errors.append("evidence schema/status drift")
    if data.get("scope") != "CEFR_1000_TOTAL_A1_TO_C1_STAGING_ONLY":
        errors.append("scope drift")
    if data.get("observed_on") != "2026-10-28":
        errors.append("observation date drift")
    if data.get("shortlist_blob_sha") != blob_sha(raw):
        errors.append("pinned shortlist blob mismatch")
    if data.get("record_count") != 6 or len(rows) != 6:
        errors.append("expected exactly six source observations")
    if data.get("counts_by_level") != dict(A1=0, A2=0, B1=0, B2=0, C1=6):
        errors.append("per-level source counts drift")
    if data.get("independently_approved_count") != 0:
        errors.append("false independent approvals")
    if "No visible Cambridge CEFR level" not in str(data.get("provenance_note", "")):
        errors.append("unlabelled-source caveat removed")
    entries = shortlist.get("entries", [])
    if len(entries) != 1000 or shortlist.get("counts_by_level") != {k:200 for k in LEVELS}:
        errors.append("canonical shortlist count drift")
    lookup = {(x.get("word"), x.get("level")): x for x in entries}
    words = [r.get("word") for r in rows if isinstance(r, dict)]
    if len(words) != 6 or len(set(words)) != 6 or set(words) != set(EXPECTED):
        errors.append("duplicate, missing or extra source headwords")
    for rec in rows:
        if not isinstance(rec, dict):
            errors.append("malformed source record")
            continue
        word = rec.get("word")
        if level != "ALL" and rec.get("level") != level:
            continue
        original = lookup.get((word, "C1"))
        if word not in EXPECTED or original is None:
            errors.append(str(word) + ": absent from canonical C1")
            continue
        if rec.get("level") != "C1" or rec.get("part_of_speech") != original.get("part_of_speech"):
            errors.append(word + ": CEFR/POS drift")
        if rec.get("source_cefr") is not None or rec.get("source_evidence_scope") != "SENSE_DESCRIPTION_NOT_CEFR_LEVEL":
            errors.append(word + ": invented CEFR classification")
        if rec.get("triage") != TRIAGE:
            errors.append(word + ": triage drift")
        for field, expected in EXPECTED[word].items():
            if rec.get(field) != expected:
                errors.append(word + ": pinned publisher lead/editorial task drift: " + field)
        for field, original_field in (
            ("shortlist_english_definition", "english_definition"),
            ("shortlist_myanmar_meaning", "burmese_meaning"),
            ("shortlist_example", "example_sentence"),
            ("shortlist_source_path", "source_path"),
            ("shortlist_source_index", "source_index"),
            ("shortlist_source_blob_sha", "source_blob_sha"),
        ):
            if rec.get(field) != original.get(original_field):
                errors.append(word + ": original shortlist provenance drift: " + field)
        url = rec.get("source_url")
        parsed = urlparse(url) if isinstance(url, str) else urlparse("")
        if (parsed.scheme != "https" or parsed.hostname != "dictionary.cambridge.org"
                or parsed.path != "/dictionary/english/" + word or parsed.query or parsed.fragment):
            errors.append(word + ": invalid publisher headword URL")
        if (rec.get("source_authority") != "Cambridge University Press & Assessment"
                or rec.get("source_access") != "PUBLISHER_OWNED_SEARCH_INDEXED_SNIPPET_DIRECT_PAGE_403"
                or rec.get("observed_on") != "2026-10-28"):
            errors.append(word + ": source access/date/authority provenance drift")
        if (rec.get("editorial_hold") is not True
                or rec.get("independently_reviewed") is not False
                or rec.get("release_approved") is not False
                or rec.get("reviewer_receipt") is not None):
            errors.append(word + ": fabricated independent approval")
        if (original.get("editorial_hold") is not True
                or original.get("release_approved") is not False):
            errors.append(word + ": source shortlist unexpectedly released")
    return errors


def negative_tests(data, shortlist, raw):
    cases = [
        ("fake approval", lambda d: d["records"][0].update(release_approved=True)),
        ("fake reviewer", lambda d: d["records"][0].update(reviewer_receipt={"reviewer_id":"human"})),
        ("invented C1 source label", lambda d: d["records"][0].update(source_cefr="C1")),
        ("source scope misrepresentation", lambda d: d["records"][0].update(source_evidence_scope="EXACT_SENSE_CEFR")),
        ("false direct page", lambda d: d["records"][0].update(source_access="DIRECT_PUBLISHER_DICTIONARY_PAGE")),
        ("fake publisher URL", lambda d: d["records"][0].update(source_url="https://example.org/dictionary/english/abstruse")),
        ("Burmese snapshot altered", lambda d: d["records"][0].update(shortlist_myanmar_meaning="wrong")),
        ("English snapshot altered", lambda d: d["records"][0].update(shortlist_english_definition="wrong")),
        ("example snapshot altered", lambda d: d["records"][0].update(shortlist_example="wrong")),
        ("historical source blob changed", lambda d: d["records"][0].update(shortlist_source_blob_sha="0"*40)),
        ("source index changed", lambda d: d["records"][0].update(shortlist_source_index=-1)),
        ("publisher observation altered", lambda d: d["records"][0].update(source_observation="Invented C1 classification")),
        ("editorial risk altered", lambda d: d["records"][0].update(editorial_risk="")),
        ("duplicate record", lambda d: d["records"].__setitem__(1, copy.deepcopy(d["records"][0]))),
        ("fake per-level counts", lambda d: d.update(counts_by_level={"C1":6})),
        ("fake approved count", lambda d: d.update(independently_approved_count=6)),
        ("changed date", lambda d: d["records"][0].update(observed_on="2026-10-29")),
        ("lost CEFR caveat", lambda d: d.update(provenance_note="publisher confirmed C1")),
        ("removed hold", lambda d: d["records"][0].update(editorial_hold=False)),
        ("wrong POS", lambda d: d["records"][0].update(part_of_speech="noun")),
    ]
    for label, change in cases:
        altered = copy.deepcopy(data)
        change(altered)
        if not audit(altered, shortlist, raw, "ALL"):
            raise AssertionError("FAIL OPEN: " + label)
    return len(cases)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    data = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    issues = audit(data, shortlist, raw, args.level)
    negatives = negative_tests(data, shortlist, raw) if args.self_test and not issues else 0
    result = {"level":args.level, "observations":sum(
        r.get("level") == args.level or args.level == "ALL"
        for r in data["records"]), "independently_approved":0,
        "publisher_cefr_labels_observed":0, "negative_mutations_rejected":negatives,
        "status":"PASS_STRUCTURE_NOT_CEFR_APPROVAL" if not issues else "FAIL",
        "errors":issues}
    output = ROOT / ("cefr-1000-unlabelled-c1-six-" + args.level + ".json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    if issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
