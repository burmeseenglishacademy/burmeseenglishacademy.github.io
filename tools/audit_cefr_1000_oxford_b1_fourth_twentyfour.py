#!/usr/bin/env python3
"""Audit fourth B1 Oxford 24-word packet (staging research only, NEVER approval)."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-FOURTH-TWENTYFOUR-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_URL = ("https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/"
              "oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf")
EXPECTED = json.loads(r'''[["worst","A2",7,1776,"worst adj.","SUPERLATIVE_A2_VS_B1","The superlative adjective appears at A2 in Oxford; determine whether the storm example or definition justifies a different exact-sense level."],["anyway","A2",4,947,"anyway adv.","CONCESSION_A2_VS_B1","Oxford gives the adverb A2; review whether the concessive use after but matches the intended sense and Myanmar discourse register."],["direct","B1",8,1977,"direct v., adv.","DIRECT_VERB_GUIDE_VS_ADVERB","Oxford combines verb and adverb in one B1 entry; verify the theatre-production verb sense rather than direction or adverb usage."],["dream","A2",5,1145,"dream n., v.","DREAM_SLEEP_VS_ASPIRATION","The sleep-image noun differs from an ambition or aspiration noun; independently check which sense the example and Myanmar gloss express."],["easily","A2",5,1153,"easily adv.","EASILY_WITHOUT_DIFFICULTY_A2","Oxford lists easily at A2, not the provisional B1; confirm the ability/puzzle example and avoid inferring exact-sense CEFR from the wordlist."],["luck","A2",6,1374,"luck n.","LUCK_CHANCE_VS_GOOD_FORTUNE","The draft defines both favourable and unfavourable chance while the example specifically describes good luck; check Myanmar nuance."],["marriage","B1",9,2208,"marriage n.","MARRIAGE_LEGAL_STATE_VS_MARRIED_LIFE","The legal relationship and the duration of married life may not be identical dictionary senses; verify Myanmar distinctions."],["fighting","B1",8,2060,"fighting n.","FIGHTING_PHYSICAL_CONFLICT_VS_OPPOSITION","The definition combines physical fighting with opposing an adversary; the example is non-specific and requires exact-sense review."],["rich","A1",3,653,"rich adj.","RICH_WEALTH_A1_VS_B1","Oxford gives rich adjective A1; the wealth sense in the example is ordinary, so provisional B1 needs independent justification."],["skin","A2",6,1624,"skin n.","SKIN_BODY_COVERING_A2_VS_B1","Oxford gives skin noun A2; distinguish human skin from fruit or animal hide senses before deciding the intended level."],["damage","B1",8,1959,"damage n., v.","DAMAGE_NOUN_VS_VERB","Oxford lists damage as noun and verb at B1; verify the uncountable harm noun, Myanmar translation and roof example."],["directly","B1",8,1978,"directly adv.","DIRECTLY_WITHOUT_INTERMEDIARY_VS_IMMEDIATELY","The supplier-contact example means without an intermediary, not immediately; verify the exact dictionary sense and Myanmar wording."],["doubt","B1",8,1989,"doubt n., v.","DOUBT_NOUN_COLLOCATION","The example 'some doubt about the figures' is grammatical but may be less idiomatic than 'some doubts'; independent grammar review required."],["crime","A2",5,1093,"crime n.","CRIME_GENERAL_VS_SPECIFIC_OFFENCE","Oxford lists crime noun at A2; distinguish crime as a general activity from an individual offence under investigation."],["fully","B2",11,2880,"fully adv.","FULLY_COMPLETELY_B2_VS_B1","Oxford labels fully adverb B2, higher than provisional B1; verify the fully charged collocation and whether exact-sense CEFR supports B1."],["male","A2",6,1378,"male adj., n.","MALE_ADJECTIVE_VS_NOUN_MYANMAR","Oxford combines adjective and noun at A2; the Myanmar gloss includes a noun-like 'အမျိုးသား', so review the adjective sense and register."],["plant","A1",3,601,"plant n.","PLANT_LIVING_ORGANISM_VS_FACTORY","Oxford lists plant noun at A1; ensure the living organism sense rather than industrial plant, and check example against the definition."],["reality","B1",9,2355,"reality n.","REALITY_FACT_VS_ACTUAL_CONDITIONS","The example contrasts a plan with actual conditions; verify the noun's exact sense and whether the Myanmar gloss fits that contrast."],["spot","B1",9,2458,"spot n.","SPOT_MARK_VS_PLACE","The dark mark sense differs from a location or place; Oxford word/POS level cannot establish the precise marked-surface sense."],["agreement","B1",7,1800,"agreement n.","AGREEMENT_DOCUMENT_VS_MUTUAL_ASSENT","The definition describes an accepted arrangement while the example may refer to a signed document; independent sense alignment needed."],["award","A2",4,974,"award n.","AWARD_NOUN_A2_VS_VERB_B1","Oxford lists award noun at A2 and separately award verb at B1; the provisional noun must not inherit the verb's B1 label."],["eventually","B1",8,2031,"eventually adv.","EVENTUALLY_AFTER_TIME_VS_FINAL_RESULT","Oxford lists eventually adverb B1; verify delayed successful outcome, original example grammar and natural Myanmar translation."],["challenge","B1",7,1885,"challenge n.","CHALLENGE_DIFFICULT_TASK_VS_CONTEST","The difficult-task noun differs from a challenge to authority or a contest; confirm exact sense and the learner's original example."],["comment","A2",4,1065,"comment n.","COMMENT_NOUN_A2_VS_VERB_B1","Oxford lists comment noun at A2 and comment verb at B1; do not transfer the B1 verb label to the draft noun."]]''')
COUNTS = {"A1": 2, "A2": 10, "B1": 11, "B2": 1, "C1": 0}

def require(ok, reason):
    if not ok:
        raise ValueError(reason)

def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()

def audit(p, shortlist, sha):
    require(sha == SHORTLIST_SHA and p.get("shortlist_blob_sha") == sha,
            "shortlist SHA/provenance drift")
    require(p.get("schema") == 1 and p.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY",
            "scope drift")
    require(p.get("status") == "B1_FOURTH_TWENTYFOUR_DIRECT_OXFORD_WORD_POS_TRIAGE_EDITORIAL_HOLD",
            "research hold status drift")
    require(p.get("observed_on") == "2026-10-29", "date drift")
    require(type(p.get("record_count")) is int and p["record_count"] == 24, "count drift")
    require(p.get("counts_by_level") == {"A1":0,"A2":0,"B1":24,"B2":0,"C1":0},
            "draft level quota drift")
    require(p.get("publisher_reference_level_counts") == COUNTS,
            "publisher level counts drift")
    require(type(p.get("word_pos_discrepancies")) is int
            and p["word_pos_discrepancies"] == 13, "conflict count drift")
    require(p.get("independently_approved_count") == 0,
            "fabricated independent approval")
    require("NOT exact-sense CEFR" in p.get("source_limitations", ""),
            "missing word/POS-only caveat")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "shortlist quota drift")
    b1 = [e for e in entries if e.get("level") == "B1"]
    require(len(b1) == 200 and len({e.get("word") for e in b1}) == 200,
            "B1 uniqueness/quota drift")
    byword = {e["word"]:e for e in b1}
    records = p.get("records")
    require(isinstance(records, list) and len(records) == 24, "packet length drift")
    require(len({r.get("word") for r in records if isinstance(r, dict)}) == 24,
            "duplicate packet word")
    for i, (word, ox, page, line, excerpt, risk_id, risk) in enumerate(EXPECTED):
        r = records[i]
        require(isinstance(r, dict) and r.get("word") == word and
                r.get("level") == "B1", f"{word}: identity drift")
        e = byword[word]
        require(r.get("part_of_speech") == e.get("part_of_speech"),
                f"{word}: POS drift")
        require(r.get("shortlist_snapshot") == {
            "english_definition":e.get("english_definition"),
            "myanmar_meaning":e.get("burmese_meaning"),
            "example_sentence":e.get("example_sentence")}, f"{word}: bilingual snapshot drift")
        require(r.get("shortlist_provenance") == {
            "source_path":e.get("source_path"),
            "source_index":e.get("source_index"),
            "source_blob_sha":e.get("source_blob_sha")}, f"{word}: original Git provenance drift")
        require(r.get("publisher_source") == {
            "publisher":"Oxford University Press",
            "title":"The Oxford 3000 by CEFR level",
            "url":SOURCE_URL,
            "observed_on":"2026-10-29",
            "pdf_page":page,
            "extracted_line":line,
            "source_excerpt":excerpt,
            "source_cefr_level":ox,
            "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, f"{word}: publisher evidence drift")
        require(r.get("editorial_risk_id") == risk_id and
                r.get("editorial_risk") == risk, f"{word}: editorial risk drift")
        task = ("Independent human bilingual and exact-sense review required for "
                f"{word} ({risk_id}). Verify original English definition, fluent Myanmar meaning, "
                "grammatical example, British pronunciation and exact-sense CEFR using directly "
                "observed publisher dictionary sense/label with dated URL and locator. Oxford "
                f"word/POS level {ox} is not exact-sense approval. Preserve signed independent "
                "reviewer receipt bound to final content hash.")
        require(r.get("independent_reviewer_task") == task,
                f"{word}: independent review task altered")
        require(r.get("editorial_hold") is True and
                r.get("independently_reviewed") is False and
                r.get("release_approved") is False and
                r.get("independent_reviewer_receipt") is None,
                f"{word}: false independent approval")
    return len(records)

def negative_tests(p, shortlist, sha):
    count = 0
    for i in range(24):
        for mutation in ("publisher", "myanmar", "review", "risk"):
            changed = copy.deepcopy(p)
            r = changed["records"][i]
            if mutation == "publisher":
                r["publisher_source"]["source_excerpt"] = "invented B1 exact-sense label"
            elif mutation == "myanmar":
                r["shortlist_snapshot"]["myanmar_meaning"] = "မမှန်ကန်သော ဘာသာပြန်"
            elif mutation == "review":
                r["independent_reviewer_receipt"] = {"reviewer_id":"fake"}
            else:
                r["editorial_risk"] = "No editorial risks; release immediately."
            try:
                audit(changed, shortlist, sha)
            except ValueError:
                count += 1
            else:
                raise AssertionError(f"forged {mutation} for {i} was accepted")
    for field, value in (
        ("record_count",25), ("word_pos_discrepancies",0),
        ("independently_approved_count",24), ("shortlist_blob_sha","0"*40),
        ("source_limitations","Independent review done"),
        ("status","RELEASE_APPROVED"), ("observed_on","2027-01-01")):
        changed = copy.deepcopy(p)
        changed[field] = value
        try:
            audit(changed, shortlist, sha)
        except ValueError:
            count += 1
        else:
            raise AssertionError(f"forged packet field {field} was accepted")
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("A1","A2","B1","B2","C1","ALL"),
                        default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.level not in ("B1","ALL"):
        print(f"SKIP: {args.level} not B1 packet; no approval granted")
        return
    p = json.loads(PACKET.read_text("utf8"))
    s = json.loads(SHORTLIST.read_text("utf8"))
    sha = blob_sha(SHORTLIST)
    print(f"PASS: {audit(p,s,sha)}/24 Oxford B1 draft word/POS source snapshots "
          "bound to provisional shortlist; 13 discrepancies; 0 approvals")
    if args.self_test:
        print(f"PASS: {negative_tests(p,s,sha)}/103 forged publisher, Myanmar, "
              "risk, review and metadata mutations rejected")

if __name__ == "__main__":
    main()
