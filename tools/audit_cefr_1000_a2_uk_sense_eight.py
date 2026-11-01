#!/usr/bin/env python3
"""Fail-closed research-only A2 UK exact-sense triage audit. Never grants approval."""
import argparse
import copy
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-A2-EIGHT-DIRECT-UK-SENSE-AND-CEFR-TRIAGE-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_BLOB = "0429e393cf17355866926806f9b74b74ea1747e9"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
ORIGINAL = {
    "original_english_definition": "english_definition",
    "original_burmese_meaning": "burmese_meaning",
    "original_example_sentence": "example_sentence",
    "source_path": "source_path",
    "source_index": "source_index",
    "source_blob_sha": "source_blob_sha",
}
EXPECTED_META = json.loads(r'''{"schema":1,"scope":"USER_APPROVED_1000_TOTAL_STAGING_ONLY","status":"UNAPPROVED_A2_DIRECT_OXFORD_SENSE_TRIAGE","source_observed_on":"2026-11-01","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","counts_by_level":{"A1":0,"A2":8,"B1":0,"B2":0,"C1":0},"first_pass_written_by_level":{"A1":200,"A2":200,"B1":200,"B2":200,"C1":200},"independently_approved_by_level":{"A1":0,"A2":0,"B1":0,"B2":0,"C1":0},"real_george_emma_listening_signoffs":0,"source_scope_notice":"Oxford topic badges are NOT independent exact-sense CEFR signoff. Cambridge indexed snippets for pretty, due, worth suggest B1 but direct Cambridge page opens returned HTTP 403. All suggested Myanmar and examples are editorial proposals, not independent approvals.","production_status":"BLOCKED_STAGING_ONLY"}''')
EXPECTED = json.loads(r'''{"program":{"word":"program","level":"A2","part_of_speech":"noun","oxford_direct_url":"https://www.oxfordlearnersdictionaries.com/us/definition/english/program_1","oxford_page_lines":"103-123","source_access":"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01","source_supported_observation":"The computer-instruction sense is British program; programme applies to other senses. Oxford computer-topic badge a2 is contextual, not an authenticated independent CEFR review.","risk_class":"UK_COMPUTER_SPELLING_VALID","suggested_myanmar_UNAPPROVED":"ကွန်ပျူတာက လုပ်ဆောင်ရမည့် အမိန့်ညွှန်ကြားချက်များပါဝင်သော ပရိုဂရမ်","suggested_example_UNAPPROVED":"The program checks the files for errors.","publisher_cefr_conflict_status":"NO_CONFLICT_ESTABLISHED","cambridge_index_url":null,"cambridge_access":"NOT_USED","source_observed_on":"2026-11-01","editorial_hold":true,"independently_checked":false,"release_approved":false,"real_george_listening":false,"real_emma_listening":false},"public":{"word":"public","level":"A2","part_of_speech":"noun","oxford_direct_url":"https://www.oxfordlearnersdictionaries.com/definition/english/public_2","oxford_page_lines":"103-124","source_access":"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01","source_supported_observation":"The public is a collective noun referring to ordinary people, normally with the article the; Oxford permits singular or plural verb agreement. The a2 badge is a topic label.","risk_class":"COLLECTIVE_NOUN_AGREEMENT","suggested_myanmar_UNAPPROVED":"အများပြည်သူ၊ ပြည်သူလူထု (the public ဟု သုံးလေ့ရှိ)","suggested_example_UNAPPROVED":"The library is open to the public.","publisher_cefr_conflict_status":"NO_CONFLICT_ESTABLISHED","cambridge_index_url":null,"cambridge_access":"NOT_USED","source_observed_on":"2026-11-01","editorial_hold":true,"independently_checked":false,"release_approved":false,"real_george_listening":false,"real_emma_listening":false},"college":{"word":"college","level":"A2","part_of_speech":"noun","oxford_direct_url":"https://www.oxfordlearnersdictionaries.com/definition/english/college","oxford_page_lines":"103-159","source_access":"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01","source_supported_observation":"Oxford separates UK post-school further education and training from US college meaning a university-level degree institution. The draft definition is broad and the example is ambiguous.","risk_class":"UK_US_EDUCATION_SENSE","suggested_myanmar_UNAPPROVED":"ကျောင်းပြီးနောက် ဆက်လက်ပညာသင်ကြားနိုင်သော ကောလိပ်၊ သက်မွေးပညာသင်တန်းကျောင်း","suggested_example_UNAPPROVED":"My sister is starting a course at a local college next month.","publisher_cefr_conflict_status":"NO_CONFLICT_ESTABLISHED","cambridge_index_url":null,"cambridge_access":"NOT_USED","source_observed_on":"2026-11-01","editorial_hold":true,"independently_checked":false,"release_approved":false,"real_george_listening":false,"real_emma_listening":false},"post":{"word":"post","level":"A2","part_of_speech":"noun","oxford_direct_url":"https://www.oxfordlearnersdictionaries.com/definition/english/post_2","oxford_page_lines":"186-224","source_access":"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01","source_supported_observation":"Oxford distinguishes countable internet/blog post from uncountable British postal mail and from job post. The draft example fits internet sense. a2 appears as a topic label.","risk_class":"INTERNET_VS_MAIL_JOB","suggested_myanmar_UNAPPROVED":"အင်တာနက် သို့မဟုတ် လူမှုကွန်ရက်တွင် တင်ထားသော ပို့စ်၊ စာတင်ချက်","suggested_example_UNAPPROVED":"Her online post explained the new class schedule.","publisher_cefr_conflict_status":"NO_CONFLICT_ESTABLISHED","cambridge_index_url":null,"cambridge_access":"NOT_USED","source_observed_on":"2026-11-01","editorial_hold":true,"independently_checked":false,"release_approved":false,"real_george_listening":false,"real_emma_listening":false},"term":{"word":"term","level":"A2","part_of_speech":"noun","oxford_direct_url":"https://www.oxfordlearnersdictionaries.com/definition/english/term_1","oxford_page_lines":"107-139,180-188","source_access":"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01","source_supported_observation":"Oxford sense 1 is a word/expression used as a name, often technical; sense 2 is a school term. A b1 education-topic badge occurs on school-term sense, not evidence for the draft terminology sense.","risk_class":"TERMINOLOGY_VS_SCHOOL_PERIOD","suggested_myanmar_UNAPPROVED":"သီးခြားအဓိပ္ပာယ်ဖြင့် သုံးသော ဝေါဟာရ၊ အသုံးအနှုန်း","suggested_example_UNAPPROVED":"Our teacher explained the scientific term in simple English.","publisher_cefr_conflict_status":"SENSE_SPECIFIC_CEFR_UNRESOLVED","cambridge_index_url":null,"cambridge_access":"NOT_USED","source_observed_on":"2026-11-01","editorial_hold":true,"independently_checked":false,"release_approved":false,"real_george_listening":false,"real_emma_listening":false},"pretty":{"word":"pretty","level":"A2","part_of_speech":"adverb","oxford_direct_url":"https://www.oxfordlearnersdictionaries.com/us/definition/english/pretty_1","oxford_page_lines":"103-127","source_access":"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01","source_supported_observation":"Oxford adverb is rather informal and means fairly/to some extent, distinct from pretty adjective (attractive). Cambridge publisher-indexed adverb B1 versus draft A2 is a review lead; Cambridge direct open returned HTTP 403.","risk_class":"ADVERB_VS_ADJECTIVE_REGISTER","suggested_myanmar_UNAPPROVED":"အတော်အတန်၊ တော်တော်လေး (စကားပြောသုံး၊ အလွတ်သဘော)","suggested_example_UNAPPROVED":"The instructions are pretty clear, but I still have one question.","publisher_cefr_conflict_status":"CAMBRIDGE_INDEX_B1_VS_DRAFT_A2","cambridge_index_url":"https://dictionary.cambridge.org/dictionary/english/pretty","cambridge_access":"INDEX_ONLY_DIRECT_403","source_observed_on":"2026-11-01","editorial_hold":true,"independently_checked":false,"release_approved":false,"real_george_listening":false,"real_emma_listening":false},"due":{"word":"due","level":"A2","part_of_speech":"adjective","oxford_direct_url":"https://www.oxfordlearnersdictionaries.com/definition/english/due_1","oxford_page_lines":"150-165","source_access":"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01","source_supported_observation":"Oxford expected/arranged sense is predicative, as in the next train is due; separate from due to meaning caused by, payment due and in due course. Cambridge publisher-indexed expected sense B1 versus draft A2 is a review lead; direct Cambridge returned HTTP 403.","risk_class":"EXPECTED_VS_CAUSE_PAYMENT","suggested_myanmar_UNAPPROVED":"သတ်မှတ်ထားသော အချိန်တွင် ရောက်ရန်၊ ဖြစ်ရန် မျှော်မှန်းထားသော","suggested_example_UNAPPROVED":"The next bus is due in ten minutes.","publisher_cefr_conflict_status":"CAMBRIDGE_INDEX_B1_VS_DRAFT_A2","cambridge_index_url":"https://dictionary.cambridge.org/dictionary/english/due","cambridge_access":"INDEX_ONLY_DIRECT_403","source_observed_on":"2026-11-01","editorial_hold":true,"independently_checked":false,"release_approved":false,"real_george_listening":false,"real_emma_listening":false},"worth":{"word":"worth","level":"A2","part_of_speech":"adjective","oxford_direct_url":"https://www.oxfordlearnersdictionaries.com/us/definition/english/worth_1","oxford_page_lines":"103-115,132-165","source_access":"DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01","source_supported_observation":"Oxford worth adjective is predicative and preposition-like, followed by value, noun or -ing; monetary value differs from worthwhile-action sense. Cambridge publisher-indexed money sense B1 versus draft A2 is a review lead; Cambridge direct returned HTTP 403.","risk_class":"PREDICATIVE_ADJECTIVE_MONEY_VS_ACTION","suggested_myanmar_UNAPPROVED":"ငွေကြေးတန်ဖိုးရှိသော၊ တန်ဖိုးအားဖြင့် ... ဖြစ်သော","suggested_example_UNAPPROVED":"This old coin is worth ten dollars.","publisher_cefr_conflict_status":"CAMBRIDGE_INDEX_B1_VS_DRAFT_A2","cambridge_index_url":"https://dictionary.cambridge.org/dictionary/english/worth","cambridge_access":"INDEX_ONLY_DIRECT_403","source_observed_on":"2026-11-01","editorial_hold":true,"independently_checked":false,"release_approved":false,"real_george_listening":false,"real_emma_listening":false}}''')


def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()


def validate(packet, shortlist, level="ALL", check_files=False):
    errors = []
    if check_files:
        if git_blob_sha(PACKET) != PACKET_BLOB:
            errors.append("packet Git blob changed")
        if git_blob_sha(SHORTLIST) != SHORTLIST_BLOB:
            errors.append("frozen shortlist Git blob changed")
    if not isinstance(packet, dict) or set(packet) != set(EXPECTED_META) | {"records"}:
        return errors + ["packet keys/schema changed"]
    for key, value in EXPECTED_META.items():
        if packet.get(key) != value or type(packet.get(key)) is not type(value):
            errors.append("packet metadata mismatch: " + key)
    records = packet.get("records")
    if not isinstance(records, list) or len(records) != 8:
        return errors + ["must have exactly eight source-bound records"]
    if not isinstance(shortlist, dict) or not isinstance(shortlist.get("entries"), list):
        return errors + ["missing shortlist"]
    entries = shortlist["entries"]
    if len(entries) != 1000:
        errors.append("shortlist not exactly 1000")
    counts = {k: 0 for k in LEVELS}
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("invalid shortlist entry")
            continue
        w, lev = entry.get("word"), entry.get("level")
        if lev not in counts or not isinstance(w, str):
            errors.append("invalid word/level")
            continue
        counts[lev] += 1
        key = w.casefold().strip()
        if key in seen:
            errors.append("cross-level duplicate: " + key)
        seen.add(key)
        if (entry.get("editorial_hold") is not True or
            any(entry.get(f) is not False for f in
                ("release_approved", "reviewed_english", "reviewed_burmese",
                 "reviewed_example", "reviewed_level", "reviewed_pronunciation"))):
            errors.append("false shortlist approval: " + w)
    if any(counts[k] != 200 for k in LEVELS):
        errors.append("not 200 provisional entries per level")
    byword = {e.get("word"): e for e in entries if isinstance(e, dict)}
    observed = set()
    for record in records:
        if not isinstance(record, dict):
            errors.append("non-object research record")
            continue
        word = record.get("word")
        if word in observed or word not in EXPECTED:
            errors.append("duplicate/unknown research word: " + str(word))
            continue
        observed.add(word)
        expected = EXPECTED[word]
        if set(record) != set(expected) | set(ORIGINAL):
            errors.append("unexpected research fields: " + word)
            continue
        for key, value in expected.items():
            if record.get(key) != value or type(record.get(key)) is not type(value):
                errors.append(word + ": mismatched " + key)
        original = byword.get(word)
        if not original:
            errors.append("research word missing from shortlist: " + word)
            continue
        for field, source_field in ORIGINAL.items():
            if record.get(field) != original.get(source_field):
                errors.append(word + ": original snapshot mismatch " + field)
        if original.get("level") != "A2" or original.get("part_of_speech") != record.get("part_of_speech"):
            errors.append(word + ": level/POS mismatch")
        if (record.get("editorial_hold") is not True or
            record.get("independently_checked") is not False or
            record.get("release_approved") is not False or
            record.get("real_george_listening") is not False or
            record.get("real_emma_listening") is not False):
            errors.append(word + ": forged approval/listening")
        if not str(record.get("oxford_direct_url", "")).startswith(
                "https://www.oxfordlearnersdictionaries.com/"):
            errors.append(word + ": untrusted publisher URL")
        if record.get("source_access") != "DIRECT_OXFORD_DICTIONARY_PAGE_OPENED_2026_11_01":
            errors.append(word + ": unsupported source access")
        if record.get("cambridge_access") == "INDEX_ONLY_DIRECT_403" and record.get("publisher_cefr_conflict_status") == "NO_CONFLICT_ESTABLISHED":
            errors.append(word + ": indexed CEFR mismatch hidden")
    if observed != set(EXPECTED):
        errors.append("missing source-bound words")
    return errors


def self_test(packet, shortlist):
    rejected = 0
    def reject(p, s, tag):
        nonlocal rejected
        problems = validate(p, s)
        if not problems:
            raise AssertionError("FAIL OPEN: " + tag)
        rejected += 1
    for i, row in enumerate(packet["records"]):
        for field, value in row.items():
            p = copy.deepcopy(packet)
            if isinstance(value, bool):
                p["records"][i][field] = not value
            elif isinstance(value, int):
                p["records"][i][field] = value + 1
            elif value is None:
                p["records"][i][field] = "FORGED"
            else:
                p["records"][i][field] = value + " FORGED"
            reject(p, shortlist, row["word"] + "." + field)
        p = copy.deepcopy(packet)
        p["records"][i]["independent_reviewer_receipt"] = {"result": "PASS"}
        reject(p, shortlist, row["word"] + ".injected-receipt")
        p = copy.deepcopy(packet)
        p["records"].pop(i)
        reject(p, shortlist, row["word"] + ".deleted")
    for field, value in EXPECTED_META.items():
        p = copy.deepcopy(packet)
        if isinstance(value, bool):
            p[field] = not value
        elif isinstance(value, int):
            p[field] = value + 1
        elif isinstance(value, str):
            p[field] = value + " FORGED"
        else:
            p[field] = {"FORGED": True}
        reject(p, shortlist, "metadata." + field)
    for field in ("independent_cefr_approved", "audio_listened", "production_deployed"):
        p = copy.deepcopy(packet)
        p[field] = True
        reject(p, shortlist, "top-injection." + field)
    for field in ("editorial_hold", "release_approved", "reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation"):
        s = copy.deepcopy(shortlist)
        s["entries"][0][field] = not s["entries"][0][field]
        reject(packet, s, "shortlist." + field)
    return rejected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("ALL",) + LEVELS, default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf8"))
    problems = validate(packet, shortlist, args.level, check_files=True)
    if problems:
        print(json.dumps({"result": "FAIL", "issues": problems[:20]}, ensure_ascii=False))
        return 1
    mutations = self_test(packet, shortlist) if args.self_test else 0
    print(json.dumps({"result": "PASS_STAGING_RESEARCH_ONLY",
        "level": args.level, "source_bound_records": 8,
        "adversarial_mutations_rejected": mutations,
        "first_pass_written": 1000, "independently_approved": 0,
        "george_emma_listened": 0, "production": "BLOCKED_STAGING_ONLY"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
