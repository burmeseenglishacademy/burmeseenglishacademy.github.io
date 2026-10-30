#!/usr/bin/env python3
"""Fail-closed six Cambridge A2 compound research leads. Staging ONLY, no approvals."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-CAMBRIDGE-A2-SIX-COMPOUND-INDEXED-SENSE-TRIAGE-2026-10-31.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
EXPECTED = json.loads(r'''{"saucepan":{"publisher_evidence":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/us/dictionary/english/saucepan","observed_on":"2026-10-31","access":"WEB_SEARCH_INDEXED_PUBLISHER_ENTRY_DIRECT_FETCH_403","cefr_badge_observed":"B1","scope":"HEADWORD_SENSE_NOT_INDEPENDENT_CEFR_REVIEW","grammar":"countable noun","sense_paraphrase":"Deep cooking pan with straight sides, normally a handle and lid."},"editorial_risk":"A2 draft is below the observed B1 publisher badge; avoid automatically re-tiering without exact-sense human signoff.","unapproved_proposal":{"burmese_meaning":"လက်ကိုင်ပါ အနက်ရှိသော ချက်ပြုတ်အိုးငယ်","original_example":"She warmed the soup in a saucepan."}},"postcard":{"publisher_evidence":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/dictionary/english/postcard","observed_on":"2026-10-31","access":"WEB_SEARCH_INDEXED_PUBLISHER_ENTRY_DIRECT_FETCH_403","cefr_badge_observed":"A2","scope":"HEADWORD_SENSE_NOT_INDEPENDENT_CEFR_REVIEW","grammar":"countable noun","sense_paraphrase":"Card sent by post without an envelope, often with a picture."},"editorial_risk":"A2 badge aligns with draft word/POS; confirm picture is optional and Myanmar definition does not imply every postcard has one.","unapproved_proposal":{"burmese_meaning":"စာအိတ်မပါဘဲ စာတိုက်က ပို့နိုင်သော ပုံပါလေ့ရှိသည့် ကတ်ပြား","original_example":"I sent my aunt a postcard from Bagan."}},"toothbrush":{"publisher_evidence":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/dictionary/english/toothbrush","observed_on":"2026-10-31","access":"WEB_SEARCH_INDEXED_PUBLISHER_ENTRY_DIRECT_FETCH_403","cefr_badge_observed":"A2","scope":"HEADWORD_SENSE_NOT_INDEPENDENT_CEFR_REVIEW","grammar":"countable noun","sense_paraphrase":"Small long-handled brush for cleaning teeth."},"editorial_risk":"A2 badge aligns; toothpaste is usual but not a necessary component of the noun definition.","unapproved_proposal":{"burmese_meaning":"သွားသန့်ရှင်းရေးအတွက် အသုံးပြုသော သွားတိုက်တံ","original_example":"He put a new toothbrush in his travel bag."}},"dustbin":{"publisher_evidence":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/dictionary/english/dustbin","observed_on":"2026-10-31","access":"WEB_SEARCH_INDEXED_PUBLISHER_ENTRY_DIRECT_FETCH_403","cefr_badge_observed":"B1","scope":"HEADWORD_SENSE_NOT_INDEPENDENT_CEFR_REVIEW","grammar":"countable noun; mainly British English","sense_paraphrase":"Large container for household rubbish, typically kept outside; American equivalents garbage can or trash can."},"editorial_risk":"A2 draft below B1 publisher badge. Original example near kitchen door could suggest an indoor kitchen bin, whereas the cited sense typically refers to an outdoor container.","unapproved_proposal":{"burmese_meaning":"အိမ်အပြင်ဘက်တွင် ထားလေ့ရှိသော အမှိုက်ပုံးကြီး","original_example":"The dustbin outside the house was full."}},"crossroads":{"publisher_evidence":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/dictionary/english/crossroads","observed_on":"2026-10-31","access":"WEB_SEARCH_INDEXED_PUBLISHER_ENTRY_DIRECT_FETCH_403","cefr_badge_observed":"B2","scope":"HEADWORD_SENSE_NOT_INDEPENDENT_CEFR_REVIEW","grammar":"countable noun; singular and plural form crossroads","sense_paraphrase":"Road junction where two roads cross; separate figurative decision-point use."},"editorial_risk":"A2 draft below B2 publisher badge. Do not confuse literal road junction with figurative be at a crossroads; singular and plural both crossroads.","unapproved_proposal":{"burmese_meaning":"လမ်းနှစ်လမ်း ဖြတ်ဆုံရာ လမ်းဆုံ","original_example":"Turn right at the crossroads beside the petrol station."}},"doormat":{"publisher_evidence":{"publisher":"Cambridge University Press","url":"https://dictionary.cambridge.org/dictionary/english/doormat","observed_on":"2026-10-31","access":"WEB_SEARCH_INDEXED_PUBLISHER_ENTRY_DIRECT_FETCH_403","cefr_badge_observed":"NOT_OBSERVED","scope":"HEADWORD_SENSE_NOT_INDEPENDENT_CEFR_REVIEW","grammar":"countable noun","sense_paraphrase":"Mat at a doorway for wiping shoes; separate informal figurative sense means a person accepting poor treatment."},"editorial_risk":"No Cambridge CEFR badge visible in indexed entry; do not infer A2. Literal mat sense must not be confused with figurative person sense.","unapproved_proposal":{"burmese_meaning":"တံခါးဝတွင် ဖိနပ်သုတ်ရန် ခင်းထားသော ဖျာငယ်","original_example":"A wet doormat lay outside the front door."}}}''')
LEVELS = ("A1", "A2", "B1", "B2", "C1")
RECORD_KEYS = {"word", "draft_level", "part_of_speech", "shortlist_snapshot",
               "original_git_provenance", "publisher_evidence", "editorial_risk",
               "unapproved_proposal", "editorial_hold", "independent_reviewed",
               "release_approved"}

def blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()

def validate(packet=None, shortlist=None):
    errors = []
    if blob_sha(SHORT) != SHORT_SHA:
        errors.append("Frozen shortlist blob changed; no evidence can be trusted")
    data = shortlist if shortlist is not None else json.loads(SHORT.read_text("utf-8"))
    doc = packet if packet is not None else json.loads(PACKET.read_text("utf-8"))
    if len(data.get("entries", [])) != 1000:
        errors.append("Shortlist no longer has 1000 entries")
    if data.get("counts_by_level") != dict.fromkeys(LEVELS, 200):
        errors.append("Incorrect 200 per level")
    if data.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
        errors.append("Unverified independent approvals")
    if doc.get("schema") != 1 or doc.get("created_on") != "2026-10-31":
        errors.append("Research schema or observation date changed")
    if doc.get("status") != "STAGING_SOURCE_RESEARCH_ONLY_NO_INDEPENDENT_REVIEW":
        errors.append("Research packet falsely marked approved")
    if doc.get("frozen_shortlist_blob_sha") != SHORT_SHA:
        errors.append("Shortlist provenance SHA mismatch")
    if "never assert independently approved" not in doc.get("scope", ""):
        errors.append("Research limitation removed")
    records = doc.get("records")
    if not isinstance(records, list) or len(records) != len(EXPECTED):
        return errors + ["Research packet must contain exactly six records"]
    by_word = {e.get("word"): e for e in data["entries"]}
    if len(by_word) != 1000:
        errors.append("Duplicate shortlist word")
    seen = set()
    for row in records:
        if not isinstance(row, dict):
            errors.append("Non-object record")
            continue
        word = row.get("word")
        if word not in EXPECTED or word in seen:
            errors.append("Unexpected/duplicate word: " + str(word))
            continue
        seen.add(word)
        original = by_word.get(word)
        if original is None:
            errors.append("Missing frozen shortlist row: " + word)
            continue
        if set(row) != RECORD_KEYS:
            errors.append(word + ": altered record keys")
        if row.get("draft_level") != "A2" or row.get("part_of_speech") != "noun":
            errors.append(word + ": wrong draft level/POS")
        if original.get("level") != "A2" or original.get("part_of_speech") != "noun":
            errors.append(word + ": shortlist level/POS drift")
        snapshot = {k: original.get(k) for k in ("english_definition","burmese_meaning","example_sentence")}
        provenance = {k: original.get(k) for k in ("source_path","source_index","source_blob_sha")}
        if row.get("shortlist_snapshot") != snapshot:
            errors.append(word + ": changed English/Myanmar/example snapshot")
        if row.get("original_git_provenance") != provenance:
            errors.append(word + ": changed original Git provenance")
        for k,v in EXPECTED[word].items():
            if row.get(k) != v:
                errors.append(word + ": ungrounded change to " + k)
        if row.get("editorial_hold") is not True or row.get("independent_reviewed") is not False or row.get("release_approved") is not False:
            errors.append(word + ": forged independent review or removed hold")
        if original.get("editorial_hold") is not True or original.get("release_approved") is not False or any(original.get("reviewed_"+f) is not False for f in ("english","burmese","example","level","pronunciation")):
            errors.append(word + ": frozen shortlist false approval")
        if row.get("publisher_evidence",{}).get("access") != "WEB_SEARCH_INDEXED_PUBLISHER_ENTRY_DIRECT_FETCH_403":
            errors.append(word + ": direct access falsely claimed")
    if seen != set(EXPECTED):
        errors.append("Missing expected source words")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    errors = validate()
    if errors:
        raise SystemExit("BLOCK: " + "; ".join(errors[:15]))
    if args.self_test:
        original = json.loads(PACKET.read_text("utf-8"))
        mutations = 0
        for idx in range(6):
            for path, value in (
                (("publisher_evidence","cefr_badge_observed"),"C1"),
                (("publisher_evidence","url"),"https://example.org/forged"),
                (("publisher_evidence","observed_on"),"2026-11-01"),
                (("publisher_evidence","access"),"DIRECT_LIVE_PAGE"),
                (("publisher_evidence","sense_paraphrase"),"unverified new sense"),
                (("publisher_evidence","grammar"),"unverified grammar"),
                (("original_git_provenance","source_blob_sha"),"0"*40),
                (("original_git_provenance","source_index"),999),
                (("shortlist_snapshot","burmese_meaning"),"အမှား"),
                (("shortlist_snapshot","example_sentence"),"Incorrect example."),
                (("unapproved_proposal","burmese_meaning"),"အတည်ပြုပြီး"),
                (("editorial_risk",),"no risk"),
                (("independent_reviewed",),True),
                (("release_approved",),True),
                (("editorial_hold",),False),
            ):
                forged = copy.deepcopy(original)
                target = forged["records"][idx]
                for key in path[:-1]:
                    target = target[key]
                target[path[-1]] = value
                if not validate(forged):
                    raise SystemExit("BLOCK: mutation escaped: " + str((idx,path)))
                mutations += 1
        print(f"PASS: {mutations}/{mutations} adversarial source, bilingual, provenance and false-signoff mutations rejected")
    counts = {l: 0 for l in LEVELS}
    counts["A2"] = 6
    print(f"PASS: {args.level} six Cambridge search-index sense leads; A2=6; B1=2 B2=1 A2=2 unlabelled=1; 0 independent approvals; NO DEPLOY")
if __name__ == "__main__":
    main()
