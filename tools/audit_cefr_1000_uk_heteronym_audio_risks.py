#!/usr/bin/env python3
"""Staging-only, fail-closed UK pronunciation heteronym research packet auditor.

Publisher-indexed IPA is NOT a direct publisher page, a listening test, a
human linguistic approval, or proof that final George/Emma audio exists.
"""
import argparse
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-BRITISH-PRONUNCIATION-HETERONYMS-FOURTEEN-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FROZEN_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
# Exact observed UK-IPA/POS pairs. The address control MUST NOT be misclassified.
EXPECTED = {
    "read": ("riːd", "past-tense verb", "red", "PRESENT_VS_PAST", None),
    "use": ("juːz", "noun", "juːs", "POS_CONTRAST", None),
    "minute": ("ˈmɪn.ɪt", "adjective", "maɪˈnjuːt", "POS_AND_SENSE_CONTRAST", "A1_TIME_NOUN_VS_A2_SHORT_WAIT"),
    "project": ("ˈprɒdʒ.ekt", "verb", "prəˈdʒekt", "STRESS_SHIFT", None),
    "progress": ("ˈprəʊ.ɡres", "verb", "prəˈɡres", "STRESS_SHIFT", None),
    "produce": ("prəˈdʒuːs", "noun", "ˈprɒdʒ.uːs", "STRESS_AND_VOWEL_SHIFT", "B1_MAKE_VERB_VS_C2_FARM_NOUN"),
    "conduct": ("kənˈdʌkt", "noun", "ˈkɒn.dʌkt", "STRESS_SHIFT", None),
    "suspect": ("səˈspekt", "noun/adjective", "ˈsʌs.pekt", "STRESS_SHIFT", None),
    "separate": ("ˈsep.ə.rət", "verb", "ˈsep.ə.reɪt", "ENDING_VOWEL_SHIFT", None),
    "graduate": ("ˈɡrædʒ.u.eɪt", "noun", "ˈɡrædʒ.u.ət", "ENDING_VOWEL_SHIFT", None),
    "contrast": ("ˈkɒn.trɑːst", "verb", "kənˈtrɑːst", "STRESS_SHIFT", None),
    "advocate": ("ˈæd.və.keɪt", "noun", "ˈæd.və.kət", "ENDING_VOWEL_SHIFT", "CAMBRIDGE_INDEX_C2_VS_DRAFT_C1"),
    "permit": ("ˈpɜː.mɪt", "verb", "pəˈmɪt", "STRESS_SHIFT", None),
    "address": ("əˈdres", "verb", "əˈdres", "NEGATIVE_CONTROL_UK_SAME", None),
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(packet, shortlist, level="ALL"):
    errors = []
    def need(ok, reason):
        if not ok:
            errors.append(reason)
    need(packet.get("schema") == 1, "schema")
    need(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY", "scope")
    need(packet.get("observed_on") == "2026-11-01", "observation date")
    need(packet.get("status") == "PRONUNCIATION_POS_HETERONYM_RESEARCH_LEADS_UNAPPROVED", "status")
    need(packet.get("shortlist_blob_sha") == FROZEN_SHA, "frozen shortlist blob")
    need(packet.get("record_count") == 14, "record count")
    need(packet.get("independently_approved_count") == 0, "no independent approvals")
    need(packet.get("headword_audio_listening_signoffs") == 0, "no headword listening")
    need(packet.get("example_audio_listening_signoffs") == 0, "no example listening")
    limitations = packet.get("source_limitations", "")
    need(isinstance(limitations, str) and all(x in limitations for x in ("403", "search-index", "not directly opened", "not actual listening")) if False else
         isinstance(limitations, str) and "403" in limitations and "search-index" in limitations and "not directly opened" in limitations, "source access limitation")
    rows = packet.get("records")
    if not isinstance(rows, list):
        return errors + ["records not a list"]
    need(len(rows) == 14, "14 records required")
    source = shortlist.get("entries", [])
    index = {e["word"]: e for e in source}
    need(len(source) == 1000, "frozen shortlist must be 1000")
    need(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "shortlist approval still zero")
    seen = set()
    counts = dict.fromkeys(LEVELS, 0)
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            errors.append(f"record {i} not object")
            continue
        word = r.get("word")
        need(word in EXPECTED, f"record {i} unknown word")
        need(word not in seen, f"record {i} duplicate word")
        seen.add(word)
        if word not in EXPECTED or word not in index:
            continue
        e = index[word]
        if e["level"] in counts:
            counts[e["level"]] += 1
        for k in ("level", "part_of_speech"):
            need(r.get(k) == e[k], f"{word} frozen {k}")
        snap = r.get("shortlist_snapshot", {})
        need(isinstance(snap, dict), f"{word} snapshot type")
        if isinstance(snap, dict):
            for k, source_k in (("english_definition", "english_definition"),
                                ("myanmar_meaning", "burmese_meaning"),
                                ("example_sentence", "example_sentence")):
                need(snap.get(k) == e[source_k], f"{word} frozen {k}")
        prov = r.get("shortlist_provenance", {})
        need(isinstance(prov, dict), f"{word} provenance type")
        if isinstance(prov, dict):
            for k in ("source_path", "source_index", "source_blob_sha"):
                need(prov.get(k) == e[k], f"{word} provenance {k}")
        p = r.get("publisher_observation", {})
        need(isinstance(p, dict), f"{word} publisher type")
        if isinstance(p, dict):
            ipa, other_pos, other_ipa, risk, cefr = EXPECTED[word]
            expected = {
                "publisher": "Cambridge University Press",
                "url": f"https://dictionary.cambridge.org/pronunciation/english/{word}",
                "observed_on": "2026-11-01",
                "access": "SEARCH_INDEX_VISIBLE_DIRECT_PAGE_403",
                "evidence_scope": "UK_IPA_BY_PART_OF_SPEECH_ONLY_NOT_LISTENING_SIGNOFF",
                "draft_uk_ipa": f"/{ipa}/",
                "contrast_part_of_speech": other_pos,
                "contrast_uk_ipa": f"/{other_ipa}/",
                "risk_kind": risk,
                "cefr_conflict_lead": cefr,
            }
            for k, value in expected.items():
                need(p.get(k) == value, f"{word} publisher {k}")
            need((p.get("draft_uk_ipa") == p.get("contrast_uk_ipa")) == (word == "address"),
                 f"{word} UK pronunciation false-positive control")
        note = r.get("editorial_note", "")
        need(isinstance(note, str) and len(note) >= 35, f"{word} editorial note")
        task = r.get("independent_reviewer_task", "")
        need(isinstance(task, str) and all(s in task for s in ("Independently", "George", "Emma", "HEADWORD", "EXAMPLE")),
             f"{word} human listening reviewer task")
        for k, expected in (("editorial_hold", True), ("independently_reviewed", False),
                            ("release_approved", False), ("headword_george_listened", False),
                            ("headword_emma_listened", False), ("example_george_listened", False),
                            ("example_emma_listened", False), ("independent_reviewer_receipt", None)):
            need(r.get(k) is expected, f"{word} false signoff {k}")
    need(seen == set(EXPECTED), "complete expected word set")
    need(packet.get("counts_by_level") == counts, "per-level counts")
    if level != "ALL":
        need(level in LEVELS, "valid level")
        need(sum(1 for r in rows if r.get("level") == level) == counts.get(level), "level subset")
    return errors


def self_test(packet, shortlist):
    baseline = validate(packet, shortlist)
    if baseline:
        raise AssertionError(f"baseline failed: {baseline[:8]}")
    n = 0
    for i, row in enumerate(packet["records"]):
        cases = [
            (("word",), row["word"] + "-fake"),
            (("level",), "C2"),
            (("part_of_speech",), "fiction"),
            (("shortlist_snapshot", "english_definition"), "Forged definition"),
            (("shortlist_snapshot", "myanmar_meaning"), "အတု"),
            (("shortlist_snapshot", "example_sentence"), "Fake sentence."),
            (("shortlist_provenance", "source_path"), "fake.json"),
            (("shortlist_provenance", "source_index"), -1),
            (("shortlist_provenance", "source_blob_sha"), "0" * 40),
            (("publisher_observation", "url"), "https://example.org/fake"),
            (("publisher_observation", "observed_on"), "2099-01-01"),
            (("publisher_observation", "access"), "DIRECT_PUBLISHER_PAGE"),
            (("publisher_observation", "evidence_scope"), "EXACT_SENSE_CEFR_APPROVED"),
            (("publisher_observation", "draft_uk_ipa"), "/wrong/"),
            (("publisher_observation", "contrast_uk_ipa"), "/wrong/"),
            (("publisher_observation", "risk_kind"), "NO_RISK"),
            (("publisher_observation", "cefr_conflict_lead"), "VERIFIED"),
            (("editorial_hold",), False),
            (("independently_reviewed",), True),
            (("release_approved",), True),
            (("headword_george_listened",), True),
            (("headword_emma_listened",), True),
            (("example_george_listened",), True),
            (("example_emma_listened",), True),
            (("independent_reviewer_receipt",), {"reviewer": "fake"}),
        ]
        for path, value in cases:
            bad = copy.deepcopy(packet)
            target = bad["records"][i]
            for k in path[:-1]:
                target = target[k]
            target[path[-1]] = value
            if not validate(bad, shortlist):
                raise AssertionError(f"forged evidence accepted: {row['word']} {path}")
            n += 1
    for key, value in (("record_count", 15), ("independently_approved_count", 1),
                       ("headword_audio_listening_signoffs", 1),
                       ("example_audio_listening_signoffs", 1),
                       ("source_limitations", "Publisher page directly verified"),
                       ("status", "APPROVED")):
        bad = copy.deepcopy(packet)
        bad[key] = value
        if not validate(bad, shortlist):
            raise AssertionError(f"forged top-level {key} accepted")
        n += 1
    return n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("ALL",) + LEVELS, default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet, shortlist = load(PACKET), load(SHORTLIST)
    errors = validate(packet, shortlist, args.level)
    if errors:
        print(json.dumps({"result": "FAIL", "errors": errors[:40]}, ensure_ascii=False))
        return 1
    rejected = self_test(packet, shortlist) if args.self_test else 0
    print(json.dumps({"result": "PASS_STRUCTURAL_RESEARCH_ONLY_NOT_AUDIO_OR_HUMAN_SIGNOFF",
                      "level": args.level, "source_access": "SEARCH_INDEX_DIRECT_403",
                      "records": 14, "counts_by_level": packet["counts_by_level"],
                      "adversarial_mutations_rejected": rejected,
                      "independently_approved": 0, "actually_listened": 0,
                      "deployment": "BLOCKED_STAGING_ONLY"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
