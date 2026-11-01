#!/usr/bin/env python3
"""Staging-only source-bound UK spelling / capital-I research audit.

Checks frozen snapshots, dated source observations, and absence of forged
approvals. It does NOT verify linguistics, publisher CEFR, TTS or human listening.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-UK-ORTHOGRAPHY-CAPITAL-I-AND-SPELLING-TEN-2026-11-01.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "e2f9324768a557b96b32f68cd056975fc095467d"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
ORIGINAL = json.loads(r'''{"original_english_definition":"english_definition","original_burmese_meaning":"burmese_meaning","original_example_sentence":"example_sentence","source_path":"source_path","source_index":"source_index","source_blob_sha":"source_blob_sha"}''')
EXPECTED = json.loads(r'''{"i":{"word":"i","level":"A1","part_of_speech":"pronoun","spelling_class":"CAPITAL_I_REQUIRED","source_url":"https://takeielts.britishcouncil.org/blog/capital-letters-in-english-common-errors-and-how-to-fix-them","source_locator":"86-94","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":"https://dictionary.cambridge.org/dictionary/learner-english/i","secondary_access":"CAMBRIDGE_INDEX_ONLY_DIRECT_403","source_supported_observation":"British Council explicitly says the personal pronoun I is always capitalised; Cambridge learner's index shows I pronoun A1. The frozen headword i is lowercase while its example correctly writes I.","editorial_risk":"Display headword I, not i; verify search-key handling and real George/Emma input/listening rather than inferring pronunciation from spelling.","suggested_display_UNAPPROVED":"I","suggested_british_variant_UNAPPROVED":null,"proposed_myanmar_teaching_note_UNAPPROVED":"မိမိကိုယ်ကို ရည်ညွှန်းသော pronoun ကို ဝါကျအလယ်၌ပင် I ဟု အကြီးစာလုံးဖြင့် ရေးရသည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"a":{"word":"a","level":"A1","part_of_speech":"article","spelling_class":"LOWERCASE_CONTROL","source_url":"https://takeielts.britishcouncil.org/blog/capital-letters-in-english-common-errors-and-how-to-fix-them","source_locator":"86-94","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":null,"secondary_access":"NONE","source_supported_observation":"British Council singles out the pronoun I, not the article a, for obligatory mid-sentence capitals; lowercase a is valid as a dictionary headword.","editorial_risk":"Do not blindly uppercase every one-letter headword.","suggested_display_UNAPPROVED":"a","suggested_british_variant_UNAPPROVED":null,"proposed_myanmar_teaching_note_UNAPPROVED":"a သည် article ဖြစ်၍ စာကြောင်းအလယ်တွင် စာလုံးအသေးဖြင့် ရေးနိုင်သည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"me":{"word":"me","level":"A1","part_of_speech":"pronoun","spelling_class":"LOWERCASE_CONTROL","source_url":"https://takeielts.britishcouncil.org/blog/capital-letters-in-english-common-errors-and-how-to-fix-them","source_locator":"86-94","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":null,"secondary_access":"NONE","source_supported_observation":"British Council lists me among ordinary personal pronouns that do not require uppercase except at sentence start.","editorial_risk":"Do not apply the I exception to me.","suggested_display_UNAPPROVED":"me","suggested_british_variant_UNAPPROVED":null,"proposed_myanmar_teaching_note_UNAPPROVED":"me သည် I ကဲ့သို့ အမြဲစာလုံးအကြီးဖြင့် မရေးရသော object pronoun ဖြစ်သည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"realize":{"word":"realize","level":"B1","part_of_speech":"verb","spelling_class":"OXFORD_UK_IZE_VALID","source_url":"https://www.ox.ac.uk/about/the-university/brand/style-guide/words","source_locator":"84-90","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":"https://dictionary.cambridge.org/us/dictionary/english/realize","secondary_access":"CAMBRIDGE_INDEX_ONLY_DIRECT_403","source_supported_observation":"Oxford University notes that its -ise house style differs from OUP's Greek-root -ize preference; Cambridge index says UK usually realise and indexes realize verb B1 (BECOME AWARE).","editorial_risk":"Both realise and realize are valid in British English depending on editorial style; preserve exact sense and obtain independent B1 signoff.","suggested_display_UNAPPROVED":"realize","suggested_british_variant_UNAPPROVED":"realise","proposed_myanmar_teaching_note_UNAPPROVED":"ဗြိတိသျှအင်္ဂလိပ်တွင် realise ကို မကြာခဏ သုံးသော်လည်း Oxford စာလုံးပေါင်းစနစ်၌ realize လည်း မှန်ကန်သည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"recognize":{"word":"recognize","level":"B2","part_of_speech":"verb","spelling_class":"OXFORD_UK_IZE_VALID","source_url":"https://www.ox.ac.uk/about/the-university/brand/style-guide/words","source_locator":"84-90","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":null,"secondary_access":"NONE","source_supported_observation":"Oxford University distinguishes its -ise preference from OUP -ize spelling; recognize is not automatically an American-only error.","editorial_risk":"Human reviewer should select a consistent UK spelling style; no publisher exact-sense CEFR classification is inferred here.","suggested_display_UNAPPROVED":"recognize","suggested_british_variant_UNAPPROVED":"recognise","proposed_myanmar_teaching_note_UNAPPROVED":"recognize နှင့် recognise တို့သည် စာလုံးပေါင်းပုံစံကွဲများဖြစ်ပြီး အသုံးပြုမည့် UK စာလုံးပေါင်းစနစ်ကို တစ်သမတ်တည်း ရွေးရန်လိုသည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"theatre":{"word":"theatre","level":"B2","part_of_speech":"noun","spelling_class":"BRITISH_CONVENTIONAL","source_url":"https://www.ox.ac.uk/about/the-university/brand/style-guide/words","source_locator":"136-149","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":null,"secondary_access":"NONE","source_supported_observation":"Oxford University UK/US style table distinguishes -re from American -er, including theatre/ theater family.","editorial_risk":"Keep the British headword theatre unless independently justified; no automatic CEFR inference.","suggested_display_UNAPPROVED":"theatre","suggested_british_variant_UNAPPROVED":null,"proposed_myanmar_teaching_note_UNAPPROVED":"theatre သည် ဗြိတိသျှစာလုံးပေါင်းဖြစ်ပြီး အမေရိကန်အင်္ဂလိပ်တွင် theater ဟု ရေးလေ့ရှိသည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"defence":{"word":"defence","level":"B2","part_of_speech":"noun","spelling_class":"BRITISH_CONVENTIONAL","source_url":"https://www.ox.ac.uk/about/the-university/brand/style-guide/words","source_locator":"150-158","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":null,"secondary_access":"NONE","source_supported_observation":"Oxford University UK/US table explicitly gives defence as UK noun and defense as US noun.","editorial_risk":"Retain noun/POS distinction; do not mechanically substitute US spelling.","suggested_display_UNAPPROVED":"defence","suggested_british_variant_UNAPPROVED":null,"proposed_myanmar_teaching_note_UNAPPROVED":"defence သည် ဗြိတိသျှအင်္ဂလိပ်တွင် noun အဖြစ် သုံးသော စာလုံးပေါင်းဖြစ်သည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"colour":{"word":"colour","level":"B2","part_of_speech":"noun","spelling_class":"BRITISH_CONVENTIONAL","source_url":"https://www.ox.ac.uk/about/the-university/brand/style-guide/words","source_locator":"136-145","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":null,"secondary_access":"NONE","source_supported_observation":"Oxford University UK/US table explicitly contrasts colour and color.","editorial_risk":"Keep British colour in UK style; spelling choice alone is not a CEFR judgement.","suggested_display_UNAPPROVED":"colour","suggested_british_variant_UNAPPROVED":null,"proposed_myanmar_teaching_note_UNAPPROVED":"colour သည် ဗြိတိသျှစာလုံးပေါင်းဖြစ်ပြီး color သည် အမေရိကန်စာလုံးပေါင်းဖြစ်သည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"galvanize":{"word":"galvanize","level":"C1","part_of_speech":"verb","spelling_class":"OXFORD_UK_IZE_VALID","source_url":"https://www.ox.ac.uk/about/the-university/brand/style-guide/words","source_locator":"84-90","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":"https://dictionary.cambridge.org/dictionary/english/galvanize","secondary_access":"CAMBRIDGE_INDEX_ONLY_DIRECT_403","source_supported_observation":"Oxford University acknowledges OUP -ize; Cambridge indexed dictionary notes UK usually galvanise and gives a motivation-to-action verb sense.","editorial_risk":"Do not falsely label galvanize US-only; independently verify C1 exact sense and British George/Emma pronunciation.","suggested_display_UNAPPROVED":"galvanize","suggested_british_variant_UNAPPROVED":"galvanise","proposed_myanmar_teaching_note_UNAPPROVED":"galvanize နှင့် galvanise တို့သည် စာလုံးပေါင်းကွဲများဖြစ်ပြီး လူများကို လှုပ်ရှားဆောင်ရွက်စေရန် စိတ်အားတက်ကြွစေသည့် အဓိပ္ပာယ်ကို သေချာစစ်ဆေးရန်လိုသည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true},"scrutinize":{"word":"scrutinize","level":"C1","part_of_speech":"verb","spelling_class":"OXFORD_UK_IZE_VALID","source_url":"https://www.ox.ac.uk/about/the-university/brand/style-guide/words","source_locator":"84-90","source_access":"DIRECT_PAGE_OPENED_2026_11_01","secondary_index_url":"https://dictionary.cambridge.org/us/dictionary/english/scrutinize","secondary_access":"CAMBRIDGE_INDEX_ONLY_DIRECT_403","source_supported_observation":"Oxford University acknowledges OUP -ize; Cambridge indexed dictionary notes UK usually scrutinise and describes careful examination.","editorial_risk":"Do not falsely mark scrutinize as American-only; independently verify transitive grammar, C1 sense and final voice audio.","suggested_display_UNAPPROVED":"scrutinize","suggested_british_variant_UNAPPROVED":"scrutinise","proposed_myanmar_teaching_note_UNAPPROVED":"scrutinize နှင့် scrutinise တို့သည် စာလုံးပေါင်းကွဲများဖြစ်ပြီး အရာတစ်ခုကို အသေးစိတ် စစ်ဆေးသည့် အဓိပ္ပာယ်ဖြင့် သုံးသည်။","observed_on":"2026-11-01","independently_checked":false,"release_approved":false,"actual_audio_listened":false,"editorial_hold":true}}''')
META = json.loads(r'''{"schema":1,"scope":"USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY","status":"BRITISH_SPELLING_AND_CAPITAL_I_RESEARCH_UNAPPROVED","observed_on":"2026-11-01","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","source_method":"DIRECT_BRITISH_COUNCIL_AND_OXFORD_UNIVERSITY_STYLE_PAGES_WITH_SEPARATELY_LABELLED_CAMBRIDGE_SEARCH_INDEX_LEADS","counts_by_level":{"A1":3,"A2":0,"B1":1,"B2":4,"C1":2},"independently_approved_by_level":{"A1":0,"A2":0,"B1":0,"B2":0,"C1":0},"real_audio_listening_signoffs":0,"production_status":"BLOCKED_STAGING_ONLY","source_limitations":"Oxford University style guide is not an OUP CEFR word list. Cambridge dictionary pages returned HTTP 403 when opened directly; their search-index snippets are not direct page inspection. British -ize is not inherently US-only. Research is not independent linguistic, exact-sense CEFR, voice listening, physical iPhone or production evidence."}''')

def git_blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def validate(packet, shortlist, level="ALL", check_files=False):
    issues = []
    def need(condition, message):
        if not condition:
            issues.append(message)
    if check_files:
        need(git_blob_sha(PACKET) == PACKET_SHA, "research packet changed without audit rebaseline")
        need(git_blob_sha(SHORT) == SHORT_SHA, "frozen shortlist modified")
    need(set(packet) == set(META) | {"records"}, "top-level schema injection/removal")
    for field, value in META.items():
        need(packet.get(field) == value, "source-bound metadata: " + field)
    entries = shortlist.get("entries", [])
    need(len(entries) == 1000, "exactly 1000 provisional entries")
    need(shortlist.get("counts_by_level") == dict.fromkeys(LEVELS, 200), "200 per level")
    need(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "zero approvals")
    frozen = {e.get("word"): e for e in entries if isinstance(e, dict)}
    need(len(frozen) == 1000, "no duplicate provisional headwords")
    need(all(e.get("editorial_hold") is True and e.get("release_approved") is False
             and all(e.get(k) is False for k in ("reviewed_english","reviewed_burmese",
                 "reviewed_example","reviewed_level","reviewed_pronunciation"))
             for e in entries if isinstance(e, dict)), "shortlist remains fully on hold")
    rows = packet.get("records")
    if not isinstance(rows, list):
        return issues + ["records must be a list"]
    need(len(rows) == 10, "exactly ten research records")
    need(set(r.get("word") for r in rows if isinstance(r, dict)) == set(EXPECTED)
         and len({r.get("word") for r in rows if isinstance(r, dict)}) == 10,
         "ten unique known records")
    need({l: sum(isinstance(r, dict) and r.get("level") == l for r in rows) for l in LEVELS}
         == META["counts_by_level"], "derived per-level counts")
    for r in rows:
        if not isinstance(r, dict) or r.get("word") not in EXPECTED:
            need(False, "malformed or unknown research record")
            continue
        word = r["word"]
        if level != "ALL" and r.get("level") != level:
            continue
        expected = EXPECTED[word]
        need(set(r) == set(expected) | set(ORIGINAL), word + ": exact fields, no hidden approvals")
        for field, value in expected.items():
            need(r.get(field) == value, word + ": publisher/source/hold binding " + field)
        e = frozen.get(word)
        need(e is not None, word + ": shortlist original exists")
        if e:
            for field, orig in ORIGINAL.items():
                need(r.get(field) == e.get(orig), word + ": frozen bilingual/provenance " + field)
            need(r.get("level") == e.get("level") and r.get("part_of_speech") == e.get("part_of_speech"),
                 word + ": frozen level and POS")
    return issues

def self_test(packet, shortlist):
    count = 0
    def reject(bad, label, original=shortlist):
        nonlocal count
        if not validate(bad, original):
            raise AssertionError("forged research accepted: " + label)
        count += 1
    for i, row in enumerate(packet["records"]):
        for field, value in row.items():
            bad = copy.deepcopy(packet)
            if isinstance(value, bool):
                bad["records"][i][field] = not value
            elif isinstance(value, int):
                bad["records"][i][field] = value + 1
            elif value is None:
                bad["records"][i][field] = "FORGED"
            else:
                bad["records"][i][field] = str(value) + " FORGED"
            reject(bad, row["word"] + "." + field)
        bad = copy.deepcopy(packet)
        bad["records"][i]["reviewer_receipt"] = {"result": "PASS"}
        reject(bad, row["word"] + ".fake-reviewer")
        bad = copy.deepcopy(packet)
        bad["records"].pop(i)
        reject(bad, row["word"] + ".deleted")
        bad = copy.deepcopy(packet)
        bad["records"][i] = copy.deepcopy(bad["records"][(i+1) % len(bad["records"])])
        reject(bad, row["word"] + ".duplicate")
    for field, value in META.items():
        bad = copy.deepcopy(packet)
        if isinstance(value, int):
            bad[field] = value + 1
        elif isinstance(value, str):
            bad[field] = value + " FORGED"
        else:
            bad[field] = {}
        reject(bad, "top." + field)
    for field in ("independent_cefr_approved", "audio_listened", "production_deployed"):
        bad = copy.deepcopy(packet)
        bad[field] = True
        reject(bad, "forged." + field)
    for field in ("editorial_hold", "release_approved", "reviewed_english", "reviewed_burmese",
                  "reviewed_example", "reviewed_level", "reviewed_pronunciation"):
        bad_short = copy.deepcopy(shortlist)
        bad_short["entries"][0][field] = not bad_short["entries"][0][field]
        reject(packet, "shortlist." + field, bad_short)
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("ALL",) + LEVELS, default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    shortlist = json.loads(SHORT.read_text(encoding="utf8"))
    issues = validate(packet, shortlist, args.level, check_files=True)
    if issues:
        print(json.dumps({"result":"FAIL", "issues":issues[:25]}, ensure_ascii=False))
        return 1
    mutations = self_test(packet, shortlist) if args.self_test else 0
    print(json.dumps({"result":"PASS_SOURCE_BOUND_UK_ORTHOGRAPHY_RESEARCH_ONLY",
        "level":args.level, "records":len(packet["records"]),
        "per_level":packet["counts_by_level"], "adversarial_mutations_rejected":mutations,
        "independently_approved":0, "real_audio_listening":0,
        "deployment":"BLOCKED_STAGING_ONLY"}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
