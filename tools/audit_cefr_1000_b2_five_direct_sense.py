#!/usr/bin/env python3
"""Source-bound five B2 Oxford sense observations; staging only, no review approval."""
import argparse
import collections
import copy
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-B2-FIVE-DIRECT-OXFORD-SENSE-AND-MYANMAR-TRIAGE-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_GIT_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("relief", "resistance", "retail", "shame", "somewhat")
EXPECTED = json.loads(r'''{"schema":1,"scope":"USER_APPROVED_CEFR_1000_STAGING_ONLY","status":"UNAPPROVED_B2_FIVE_DIRECT_OXFORD_EXACT_SENSE_TRIAGE","observed_on":"2026-11-01","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","counts_by_level":{"A1":0,"A2":0,"B1":0,"B2":5,"C1":0},"first_pass_written_by_level":{"A1":200,"A2":200,"B1":200,"B2":200,"C1":200},"independently_approved_by_level":{"A1":0,"A2":0,"B1":0,"B2":0,"C1":0},"real_george_emma_listening_signoffs":0,"production_status":"BLOCKED_STAGING_ONLY","publisher_scope_notice":"Five Oxford Advanced Learner's Dictionary pages were directly opened on 2026-11-01. Their sense/POS/grammar observations are research, not independent exact-sense CEFR verification. Oxford topic tags and Cambridge indexed search snippets are NOT direct independent CEFR proof. No human review, British audio listening, physical iPhone QA or release is claimed.","records":[{"word":"relief","level":"B2","part_of_speech":"noun","original_english_definition":"The pleasant feeling when worry, pain or difficulty ends.","original_burmese_meaning":"စိတ်သက်သာရာရမှု","original_example_sentence":"He felt relief when the missing bag was found.","source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":21,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc","risk_class":"DISTINGUISH_EMOTIONAL_RELIEF_FROM_PAIN_REDUCTION_HUMANITARIAN_AID","source_supported_observation":"Oxford directly distinguishes the emotional feeling of relief (sense 1) from pain reduction (sense 2) and humanitarian aid (sense 3). The frozen example demonstrates the emotional sense and is grammatical. Oxford's Feelings b2 topic tag is not independently verified exact-sense CEFR evidence.","oxford_direct_sources":[{"publisher":"Oxford University Press","url":"https://www.oxfordlearnersdictionaries.com/definition/english/relief","observed_on":"2026-11-01","access":"DIRECT_PUBLISHER_PAGE_OPENED","line_locator":"104-139","evidence_scope":"EXACT_EMOTIONAL_RELIEF_SENSE_AND_NOUN_GRAMMAR_NOT_INDEPENDENT_CEFR"}],"suggested_myanmar_UNAPPROVED":"စိုးရိမ်ပူပန်မှု ပျောက်ကင်းသွားသည့်အခါ ခံစားရသော စိတ်သက်သာမှု","suggested_example_UNAPPROVED":"She felt a sense of relief when her brother arrived safely.","independent_reviewer_question":"Confirm that the example, Myanmar gloss and intended emotional sense match; obtain independent exact-sense B2 publisher CEFR evidence.","editorial_hold":true,"independently_checked":false,"release_approved":false,"independent_reviewer_receipt":null,"real_george_listening":false,"real_emma_listening":false},{"word":"resistance","level":"B2","part_of_speech":"noun","original_english_definition":"Refusal to accept or support a change or action.","original_burmese_meaning":"ခုခံဆန့်ကျင်မှု","original_example_sentence":"The proposal met resistance from local residents.","source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":22,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc","risk_class":"B2_DRAFT_VERSUS_OXFORD_C1_TOPIC_TAG_NOT_PROOF_OF_CEFR","source_supported_observation":"Oxford sense 1 explicitly covers opposition to a plan, idea or change. The frozen proposal/residents example is grammatical. Oxford tags Preferences and decisions c1 for this sense; this is a topic label, not direct independently reviewed CEFR proof and should trigger a B2-versus-C1 review rather than automatic releveling.","oxford_direct_sources":[{"publisher":"Oxford University Press","url":"https://www.oxfordlearnersdictionaries.com/definition/english/resistance","observed_on":"2026-11-01","access":"DIRECT_PUBLISHER_PAGE_OPENED","line_locator":"119-129","evidence_scope":"EXACT_OPPOSITION_TO_CHANGE_SENSE_NOT_INDEPENDENT_CEFR"}],"suggested_myanmar_UNAPPROVED":"အစီအစဉ် သို့မဟုတ် အပြောင်းအလဲတစ်ခုကို ဆန့်ကျင်ကန့်ကွက်မှု","suggested_example_UNAPPROVED":"The new policy faced strong resistance from local residents.","independent_reviewer_question":"Independently resolve whether the exact opposition-to-change noun sense is B2 or C1; do not use the different verb resist B2 self-restraint sense as evidence.","editorial_hold":true,"independently_checked":false,"release_approved":false,"independent_reviewer_receipt":null,"real_george_listening":false,"real_emma_listening":false},{"word":"retail","level":"B2","part_of_speech":"noun","original_english_definition":"The business of selling goods directly to customers.","original_burmese_meaning":"လက်လီရောင်းချမှု","original_example_sentence":"She has worked in retail for five years.","source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":23,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc","risk_class":"NOUN_VS_ADVERB_OR_VERB_AND_RETAIL_VS_WHOLESALE","source_supported_observation":"Oxford directly defines retail as an uncountable noun for selling goods to the public, usually through shops, and contrasts it with wholesale. The frozen in-retail employment example is grammatical. Oxford Business b2 and Shopping b2 are topic tags, not independent exact-sense CEFR approval.","oxford_direct_sources":[{"publisher":"Oxford University Press","url":"https://www.oxfordlearnersdictionaries.com/definition/english/retail_1","observed_on":"2026-11-01","access":"DIRECT_PUBLISHER_PAGE_OPENED","line_locator":"88-117","evidence_scope":"EXACT_NOUN_RETAIL_TRADE_SENSE_NOT_INDEPENDENT_CEFR"}],"suggested_myanmar_UNAPPROVED":"စားသုံးသူများထံ ကုန်ပစ္စည်းများကို လက်လီရောင်းချသည့်လုပ်ငန်း","suggested_example_UNAPPROVED":"My sister works in retail at a clothing shop.","independent_reviewer_question":"Check the noun business-sector sense, Burmese idiomatic precision and independent exact-sense CEFR classification.","editorial_hold":true,"independently_checked":false,"release_approved":false,"independent_reviewer_receipt":null,"real_george_listening":false,"real_emma_listening":false},{"word":"shame","level":"B2","part_of_speech":"noun","original_english_definition":"A painful feeling of embarrassment or guilt.","original_burmese_meaning":"အရှက်ကွဲမှု၊ အရှက်ရမှု","original_example_sentence":"He felt shame after lying to his friend.","source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":24,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc","risk_class":"PRIVATE_GUILT_VERSUS_A_SHAME_DISAPPOINTMENT_VERSUS_PUBLIC_HUMILIATION","source_supported_observation":"Oxford sense 1 a shame means something disappointing; sense 2 uncountable shame means embarrassment or guilt about one's action. The frozen lying-to-a-friend example targets sense 2 and is grammatical. The Myanmar word အရှက်ကွဲမှု can imply public loss of face rather than private guilt, so a fluent reviewer should refine it.","oxford_direct_sources":[{"publisher":"Oxford University Press","url":"https://www.oxfordlearnersdictionaries.com/definition/english/shame_1","observed_on":"2026-11-01","access":"DIRECT_PUBLISHER_PAGE_OPENED","line_locator":"107-166","evidence_scope":"EXACT_EMBARRASSMENT_GUILT_NOUN_SENSE_NOT_INDEPENDENT_CEFR"}],"suggested_myanmar_UNAPPROVED":"မိမိလုပ်ရပ်ကြောင့် ရှက်ရွံ့ပြီး အပြစ်ရှိသလို ခံစားရမှု","suggested_example_UNAPPROVED":"She felt ashamed of lying to her friend.","independent_reviewer_question":"Review whether the proposed Myanmar gloss conveys internal shame rather than public disgrace; retain a noun example if POS remains noun.","editorial_hold":true,"independently_checked":false,"release_approved":false,"independent_reviewer_receipt":null,"real_george_listening":false,"real_emma_listening":false},{"word":"somewhat","level":"B2","part_of_speech":"adverb","original_english_definition":"To a limited degree; rather than completely.","original_burmese_meaning":"အတော်အသင့်၊ တစ်စိတ်တစ်ပိုင်း","original_example_sentence":"The second proposal is somewhat more practical.","source_path":"draft/A2-C1-EDITORIAL-STARTER.json","source_index":25,"source_blob_sha":"b04dd85db5cfae131c25aa4c73109778991b6fdc","risk_class":"DEGREE_MODIFIER_NOT_PARTLY_OF_AN_OBJECT_OR_COMPLETELY","source_supported_observation":"Oxford describes somewhat as a rather formal adverb meaning to some degree, with examples modifying adjectives or a situation. The frozen somewhat more practical sentence is grammatical. Burmese တစ်စိတ်တစ်ပိုင်း may suggest an object's physical part instead of the intended degree of practicality.","oxford_direct_sources":[{"publisher":"Oxford University Press","url":"https://www.oxfordlearnersdictionaries.com/definition/english/somewhat","observed_on":"2026-11-01","access":"DIRECT_PUBLISHER_PAGE_OPENED","line_locator":"88-117","evidence_scope":"EXACT_FORMAL_DEGREE_ADVERB_NOT_INDEPENDENT_CEFR"}],"suggested_myanmar_UNAPPROVED":"အတန်အသင့်၊ အနည်းငယ်","suggested_example_UNAPPROVED":"The updated plan is somewhat easier to follow.","independent_reviewer_question":"Confirm degree-modifier sense, formal register, fluent Myanmar and independently sourced exact-sense CEFR.","editorial_hold":true,"independently_checked":false,"release_approved":false,"independent_reviewer_receipt":null,"real_george_listening":false,"real_emma_listening":false}]}''')
REVIEW_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                "reviewed_level", "reviewed_pronunciation", "release_approved")

def check(packet, shortlist, check_git=False):
    issues = []
    def fail(message): issues.append(message)
    if packet != EXPECTED:
        fail("Research packet differs from source-observed immutable baseline")
    if not isinstance(shortlist, dict) or not isinstance(shortlist.get("entries"), list):
        return issues + ["Provisional shortlist missing or invalid"]
    entries = shortlist["entries"]
    if len(entries) != 1000: fail("Shortlist must have exactly 1000 held entries")
    counts = collections.Counter(e.get("level") for e in entries if isinstance(e, dict))
    if counts != collections.Counter({k: 200 for k in LEVELS}):
        fail("200-per-level quotas broken")
    names = [str(e.get("word", "")).casefold() for e in entries if isinstance(e, dict)]
    if len(names) != 1000 or len(set(names)) != 1000:
        fail("Headwords missing or duplicated")
    for e in entries:
        if not isinstance(e, dict):
            fail("Malformed shortlist entry")
            continue
        if e.get("editorial_hold") is not True or any(e.get(k) is not False for k in REVIEW_FLAGS):
            fail("False independent approval or lifted editorial hold")
        if e.get("status") != "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING":
            fail("Shortlist release status changed")
    if not isinstance(packet, dict) or not isinstance(packet.get("records"), list):
        return issues + ["Research packet records missing"]
    if [r.get("word") for r in packet["records"] if isinstance(r, dict)] != list(WORDS):
        fail("B2 research words changed or reordered")
    index = {e.get("word"): e for e in entries if isinstance(e, dict)}
    for r in packet["records"]:
        if not isinstance(r, dict):
            fail("Research record malformed")
            continue
        e = index.get(r.get("word"))
        if e is None:
            fail("Research word missing from shortlist")
            continue
        for old, current in (("word", "word"), ("level", "level"),
                             ("part_of_speech", "part_of_speech"),
                             ("original_english_definition", "english_definition"),
                             ("original_burmese_meaning", "burmese_meaning"),
                             ("original_example_sentence", "example_sentence"),
                             ("source_path", "source_path"), ("source_index", "source_index"),
                             ("source_blob_sha", "source_blob_sha")):
            if r.get(old) != e.get(current):
                fail(f"{r.get('word')}: frozen original {old} changed")
        if r.get("editorial_hold") is not True or r.get("independently_checked") is not False or r.get("release_approved") is not False or r.get("independent_reviewer_receipt") is not None or r.get("real_george_listening") is not False or r.get("real_emma_listening") is not False:
            fail(f"{r.get('word')}: forged human or audio receipt")
        if check_git:
            try:
                raw = subprocess.check_output(["git", "cat-file", "blob", r["source_blob_sha"]], cwd=ROOT)
                source = json.loads(raw.decode("utf8"))["entries"][r["source_index"]]
                for old, current in (("word", "word"), ("level", "level"),
                                     ("part_of_speech", "part_of_speech"),
                                     ("original_english_definition", "english_definition"),
                                     ("original_burmese_meaning", "burmese_meaning"),
                                     ("original_example_sentence", "example_sentence")):
                    if r.get(old) != source.get(current):
                        fail(f"{r.get('word')}: historical source blob/index mismatch {old}")
            except (KeyError, IndexError, ValueError, subprocess.CalledProcessError) as exc:
                fail(f"{r.get('word')}: cannot authenticate historical source provenance: {exc}")
    if check_git:
        try:
            blob = subprocess.check_output(["git", "rev-parse", "HEAD:draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"], cwd=ROOT, text=True).strip()
            if blob != SHORTLIST_GIT_BLOB:
                fail("Frozen shortlist Git blob changed")
        except subprocess.CalledProcessError:
            fail("Cannot verify frozen shortlist Git blob")
    return issues

def self_test(packet, shortlist):
    tested = 0
    def reject(p, s, label):
        nonlocal tested
        tested += 1
        if not check(p, s):
            raise AssertionError("Adversarial mutation escaped: " + label)
    for i, word in enumerate(WORDS):
        for field, bad in (("original_english_definition", "FORGED"),
                           ("original_burmese_meaning", "ဘာသာပြန်အတု"),
                           ("original_example_sentence", "Forged example."),
                           ("source_index", 99999),
                           ("source_blob_sha", "0" * 40),
                           ("source_supported_observation", "Fake publisher evidence"),
                           ("suggested_myanmar_UNAPPROVED", "အတည်ပြုထားသည်"),
                           ("suggested_example_UNAPPROVED", "Wrong teaching example."),
                           ("independent_reviewer_question", "Already approved")):
            p = copy.deepcopy(packet); p["records"][i][field] = bad
            reject(p, shortlist, f"{word}/{field}")
        for flag, bad in (("editorial_hold", False), ("independently_checked", True),
                          ("release_approved", True), ("independent_reviewer_receipt", {"reviewer": "bot"}),
                          ("real_george_listening", True), ("real_emma_listening", True)):
            p = copy.deepcopy(packet); p["records"][i][flag] = bad
            reject(p, shortlist, f"{word}/{flag}")
        p = copy.deepcopy(packet); p["records"][i]["oxford_direct_sources"][0]["url"] = "https://www.oxfordlearnersdictionaries.com/definition/english/other"
        reject(p, shortlist, f"{word}/wrong-source")
        s = copy.deepcopy(shortlist);next(e for e in s["entries"] if e["word"] == word)["reviewed_level"] = True
        reject(packet, s, f"{word}/forged-shortlist-review")
    for field, bad in (("status", "APPROVED"), ("production_status", "LIVE"),
                       ("real_george_emma_listening_signoffs", 1000)):
        p = copy.deepcopy(packet);p[field] = bad;reject(p, shortlist, field)
    s = copy.deepcopy(shortlist);s["entries"].pop();reject(packet, s, "shortlist-count")
    s = copy.deepcopy(shortlist);s["entries"][0]["word"] = s["entries"][1]["word"];reject(packet, s, "duplicate-word")
    print(f"PASS: {tested}/{tested} adversarial source, bilingual, CEFR, provenance, false-human and audio mutations rejected")
    return tested

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text("utf8"))
    shortlist = json.loads(SHORTLIST.read_text("utf8"))
    errors = check(packet, shortlist, check_git=True)
    if errors:
        for err in errors[:20]:print("BLOCK:", err, file=sys.stderr)
        raise SystemExit(1)
    count = sum(r["level"] == args.level for r in packet["records"]) if args.level != "ALL" else len(packet["records"])
    print(f"PASS: {count} B2 publisher sense research records in {args.level}; 0 independent approvals; STAGING ONLY")
    if args.self_test:
        self_test(packet, shortlist)

if __name__ == "__main__":
    main()
