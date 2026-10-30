#!/usr/bin/env python3
"""Fail-closed C1 ninth-twelve Oxford publisher/sense research audit, STAGING ONLY.

Pinned direct Oxford PDF/dictionary locators are cross-checked against the frozen
1000-word bilingual shortlist. Never asserts exact-sense human approval, real
listening, device QA, hosting readiness or deployment.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-OXFORD-C1-NINTH-TWELVE-AND-EIGHT-DIRECT-SENSE-LEADS-2026-10-30.json"
FROZEN = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
OBS = json.loads(r'''[["discipline","B2","The Oxford 3000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf",11,2788,"discipline n.","The draft means self-control in learning, not classroom punishment or an academic discipline. Dictionary sense 3 is uncountable self-control; review Burmese register and whether C1 is justified.",{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/discipline_1","observed_on":"2026-10-30","page_text_line_start":151,"page_text_line_end":175,"editorial_interpretation":"Sense 3 describes personal self-control; distinct from rule enforcement and academic discipline.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}],["furthermore","B2","The Oxford 3000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf",11,2885,"furthermore adv.","Publisher B2 linking adverb versus provisional C1. Semicolon plus furthermore is grammatical, but review discourse-register suitability and Myanmar connector.",null],["transaction","C1","The Oxford 5000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf",7,1926,"transaction n.","The draft refers to a recorded banking transaction, not the formal uncountable transaction of government business. Oxford 5000 PDF C1 but dictionary Oxford 3000 B2 badge: unresolved publisher-surface conflict.",{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/transaction","observed_on":"2026-10-30","page_text_line_start":105,"page_text_line_end":173,"editorial_interpretation":"Countable business/payment transaction; dictionary Oxford 3000 B2 badge conflicts with PDF 5000 C1 noun listing.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}],["unemployment","B1","The Oxford 3000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf",10,2539,"unemployment n.","Publisher B1 word/POS versus C1. Dictionary collective social condition and rate sense differs from an individual's personal spell without work; Myanmar currently conflates situation and rate.",{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/unemployment","observed_on":"2026-10-30","page_text_line_start":117,"page_text_line_end":173,"editorial_interpretation":"Collective number/rate of people without jobs; draft graduates example belongs to population-level sense.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}],["continuous","B1","The Oxford 3000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf",8,1935,"continuous adj.","Publisher B1 word/POS versus C1. Machine monitoring without interruption differs from repeatedly occurring or consecutive; Myanmar needs uninterrupted sense.",null],["vulnerable","C1","The Oxford 5000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf",8,1989,"vulnerable adj.","Publisher C1 adjective and dictionary vulnerable to harm; draft extreme-heat example needs precise environmental vulnerability, not weak-person stereotype.",{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/vulnerable","observed_on":"2026-10-30","page_text_line_start":103,"page_text_line_end":116,"editorial_interpretation":"Vulnerable to harm or danger; extreme heat example aligns with environmental harm susceptibility.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}],["thereby","C1","The Oxford 5000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf",7,1901,"thereby adv.","Formal result marker: the new process reduces waste and consequently costs. Confirm the thereby + -ing participle construction and Burmese causal connector.",{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/thereby","observed_on":"2026-10-30","page_text_line_start":103,"page_text_line_end":142,"editorial_interpretation":"Formal adverb introduces a result of the preceding action; thereby lowering costs matches dictionary sense.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}],["diagnosis","C1","The Oxford 5000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf",4,1081,"diagnosis n.","Publisher C1 noun. Draft early medical diagnosis, not business fault-finding; verify countability and natural Myanmar medical phrasing.",null],["transformation","C1","The Oxford 5000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf",8,1928,"transformation n.","Publisher C1 noun. Town transformation following a railway is broad social change, not mathematical transformation; confirm causation not overstated.",null],["chronic","C1","The Oxford 5000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf",4,897,"chronic adj.","Publisher 5000 PDF C1 but directly opened Oxford dictionary shows Oxford 3000 B2 badge: unresolved publisher-surface disagreement. Draft chronic conditions refers to long-term medical conditions, not informal British very bad.",{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/chronic","observed_on":"2026-10-30","page_text_line_start":105,"page_text_line_end":156,"editorial_interpretation":"Long-term medical condition sense 1, but dictionary Oxford 3000 B2 badge conflicts with official Oxford 5000 C1 PDF.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}],["insight","B2","The Oxford 3000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf",11,2943,"insight n.","Publisher 3000 PDF B2 but directly opened Oxford dictionary shows Oxford 5000 C1 badge: unresolved publisher-surface disagreement. Draft insight into customer needs is understanding gained from survey, not sudden flash of insight.",{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/insight","observed_on":"2026-10-30","page_text_line_start":105,"page_text_line_end":205,"editorial_interpretation":"Insight into something is understanding; dictionary Oxford 5000 C1 badge conflicts with official Oxford 3000 B2 PDF.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}],["slavery","C1","The Oxford 5000 by CEFR level","https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf",7,1784,"slavery n.","Draft discusses the historical institution of forced human ownership and labour, not a metaphorical demanding job. Oxford 5000 PDF C1 but dictionary Oxford 3000 B2 badge: unresolved publisher-surface conflict.",{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/slavery","observed_on":"2026-10-30","page_text_line_start":103,"page_text_line_end":205,"editorial_interpretation":"Uncountable institution/practice of forced ownership and labour, dictionary Oxford 3000 B2 badge conflicts with PDF 5000 C1.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}]]''')
TASK = "Independent human reviewer must check exact-sense publisher CEFR evidence, English definition, fluent Myanmar meaning, original example grammar/collocation, British pronunciation, source provenance and cross-level rationale; provide a content-bound independent receipt. Publisher word/POS listing and automated checks are not independent exact-sense approval."
EXPECTED_META = json.loads(r'''{"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY","status":"C1_NINTH_TWELVE_DIRECT_OXFORD_WORD_POS_AND_EIGHT_DICTIONARY_SENSE_LEADS_EDITORIAL_HOLD","observed_on":"2026-10-30","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","record_count":12,"counts_by_level":{"A1":0,"A2":0,"B1":0,"B2":0,"C1":12},"publisher_reference_level_counts":{"B1":2,"B2":3,"C1":7},"word_pos_discrepancies":5,"direct_dictionary_sense_leads":8,"independently_approved_count":0,"source_limitations":"Oxford 3000 and Oxford 5000 official CEFR PDFs directly inspected 2026-10-30. Publisher levels are word/POS only, not independent exact-sense evidence. Eight directly opened dictionary pages provide editorial leads; chronic, insight, transaction and slavery have conflicting PDF/dictionary badges. No human independent review, real audio listening, physical iPhone test or publication. Frozen shortlist and separate reviewer task flags unchanged."}''')
LEVELS = ("A1", "A2", "B1", "B2", "C1")

def require(ok, why):
    if not ok:
        raise ValueError(why)

def git_blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(packet, shortlist):
    require(git_blob_sha(SHORTLIST) == FROZEN, "Frozen shortlist Git blob changed")
    require(shortlist.get("counts_by_level") == {k: 200 for k in LEVELS},
            "Exactly 200 provisional words per CEFR level required")
    require(shortlist.get("independently_approved_by_level") == {k: 0 for k in LEVELS},
            "Independent approvals cannot be self-attested")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "Exactly 1000 entries")
    by_word = {x["word"]: x for x in entries}
    require(len(by_word) == 1000, "Duplicate frozen shortlist headwords")
    require(set(packet) == set(EXPECTED_META) | {"records"}, "Unknown packet fields")
    for key, expected in EXPECTED_META.items():
        require(packet.get(key) == expected, "Metadata drift: " + key)
    rows = packet.get("records")
    require(isinstance(rows, list) and len(rows) == 12, "Twelve evidence records required")
    require(len({x.get("word") for x in rows}) == 12, "Duplicate packet word")
    keys = {"word", "level", "part_of_speech", "shortlist_snapshot",
            "shortlist_provenance", "publisher_source", "editorial_risk",
            "dictionary_sense_lead", "independent_reviewer_task", "editorial_hold",
            "independently_reviewed", "release_approved", "independent_reviewer_receipt"}
    for i, (word, observed, title, url, page, line, excerpt, risk, sense) in enumerate(OBS):
        row = rows[i]
        original = by_word[word]
        require(set(row) == keys, "Missing/unknown evidence fields: " + word)
        require(row["word"] == word and row["level"] == "C1"
                and original["level"] == "C1"
                and row["part_of_speech"] == original["part_of_speech"],
                "Word/POS or level drift: " + word)
        require(row["shortlist_snapshot"] == {
            "english_definition": original["english_definition"],
            "myanmar_meaning": original["burmese_meaning"],
            "example_sentence": original["example_sentence"]},
            "Frozen bilingual/example mismatch: " + word)
        require(row["shortlist_provenance"] == {
            "source_path": original["source_path"],
            "source_index": original["source_index"],
            "source_blob_sha": original["source_blob_sha"]},
            "Historical Git provenance mismatch: " + word)
        require(row["publisher_source"] == {
            "publisher": "Oxford University Press",
            "title": title,
            "url": url,
            "observed_on": "2026-10-30",
            "pdf_page": page,
            "extracted_line": line,
            "source_excerpt": excerpt,
            "source_cefr_level": observed,
            "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"},
            "Pinned publisher PDF evidence mismatch: " + word)
        require(row["dictionary_sense_lead"] == sense,
                "Direct dictionary sense source mismatch: " + word)
        require(row["editorial_risk"] == risk and
                row["independent_reviewer_task"] == TASK,
                "Editorial/human-review task changed: " + word)
        require(row["editorial_hold"] is True
                and row["independently_reviewed"] is False
                and row["release_approved"] is False
                and row["independent_reviewer_receipt"] is None,
                "Forged independent approval: " + word)
        require(original.get("editorial_hold") is True
                and original.get("release_approved") is False
                and all(original.get("reviewed_" + k) is False
                        for k in ("english", "burmese", "example", "level", "pronunciation")),
                "Frozen shortlist flags not held: " + word)
    return {"level": "C1", "observations": 12, "publisher_B1": 2,
            "publisher_B2": 3, "publisher_C1": 7,
            "direct_dictionary_sense_leads": 8,
            "independently_approved": 0,
            "real_listening_signoffs": 0, "release": "BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist):
    mutations = [
        ("word", lambda r: r.update(word="fake-headword")),
        ("level", lambda r: r.update(level="B2")),
        ("part_of_speech", lambda r: r.update(part_of_speech="fake")),
        ("english", lambda r: r["shortlist_snapshot"].update(english_definition="Forged")),
        ("myanmar", lambda r: r["shortlist_snapshot"].update(myanmar_meaning="အမှား")),
        ("example", lambda r: r["shortlist_snapshot"].update(example_sentence="Forged")),
        ("source_path", lambda r: r["shortlist_provenance"].update(source_path="draft/fake.json")),
        ("source_index", lambda r: r["shortlist_provenance"].update(source_index=-1)),
        ("source_blob", lambda r: r["shortlist_provenance"].update(source_blob_sha="0"*40)),
        ("publisher", lambda r: r["publisher_source"].update(publisher="Fake")),
        ("title", lambda r: r["publisher_source"].update(title="Fake")),
        ("pdf_url", lambda r: r["publisher_source"].update(url="https://example.invalid/fake.pdf")),
        ("observed_on", lambda r: r["publisher_source"].update(observed_on="1900-01-01")),
        ("page", lambda r: r["publisher_source"].update(pdf_page=0)),
        ("line", lambda r: r["publisher_source"].update(extracted_line=-1)),
        ("excerpt", lambda r: r["publisher_source"].update(source_excerpt="fake n.")),
        ("source_level", lambda r: r["publisher_source"].update(source_cefr_level="A1")),
        ("source_scope", lambda r: r["publisher_source"].update(evidence_scope="HUMAN_APPROVED")),
        ("source_access", lambda r: r["publisher_source"].update(access="SEARCH_SNIPPET")),
        ("risk", lambda r: r.update(editorial_risk="Forged")),
        ("review_task", lambda r: r.update(independent_reviewer_task="Approved")),
        ("hold", lambda r: r.update(editorial_hold=False)),
        ("independent_review", lambda r: r.update(independently_reviewed=True)),
        ("approval", lambda r: r.update(release_approved=True)),
        ("receipt", lambda r: r.update(independent_reviewer_receipt={"reviewer": "fake"})),
        ("sense_lead", lambda r: r.update(dictionary_sense_lead={"url": "https://fake.invalid"})),
    ]
    n = 0
    for i in range(12):
        for label, change in mutations:
            forged = copy.deepcopy(packet)
            before = json.dumps(forged["records"][i], ensure_ascii=False, sort_keys=True)
            change(forged["records"][i])
            require(before != json.dumps(forged["records"][i], ensure_ascii=False, sort_keys=True),
                    "Ineffective mutation: " + label)
            try:
                audit(forged, shortlist)
            except ValueError:
                n += 1
            else:
                raise AssertionError("Forged " + label + " accepted for " + OBS[i][0])
    global_mutations = [
        ("count", lambda p: p.update(record_count=11)),
        ("publisher_levels", lambda p: p["publisher_reference_level_counts"].update(B2=7)),
        ("fake_approval", lambda p: p.update(independently_approved_count=1)),
        ("source_date", lambda p: p.update(observed_on="1900-01-01")),
        ("source_limitations", lambda p: p.update(source_limitations="All approved")),
        ("drop_record", lambda p: p["records"].pop()),
        ("extra_field", lambda p: p.update(published=True)),
    ]
    for label, change in global_mutations:
        forged = copy.deepcopy(packet)
        before = json.dumps(forged, ensure_ascii=False, sort_keys=True)
        change(forged)
        require(before != json.dumps(forged, ensure_ascii=False, sort_keys=True),
                "Ineffective global mutation: " + label)
        try:
            audit(forged, shortlist)
        except ValueError:
            n += 1
        else:
            raise AssertionError("Forged global " + label + " accepted")
    require(n == 12*len(mutations)+len(global_mutations), "Negative test count drift")
    return n

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    result = audit(packet, shortlist)
    if args.self_test:
        n = self_test(packet, shortlist)
        print("PASS: %d/%d ninth C1 adversarial mutations rejected" % (n, n))
    print(json.dumps({"requested_level": args.level, **result},
                     ensure_ascii=False, sort_keys=True))

if __name__ == "__main__":
    main()
