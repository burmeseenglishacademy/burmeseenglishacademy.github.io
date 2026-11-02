#!/usr/bin/env python3
"""Fail-closed mechanical audit of six held C1 Cambridge-indexed research leads.
This does NOT approve English, Myanmar, CEFR, audio, devices, or release.
"""
import argparse
import copy
import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-C1-SIX-SPY-POPULARITY-NEUTRAL-SACRED-SIGNATURE-COPYRIGHT-INDEX-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "26c52a26f541c65ede562c89e5d9ee9754722e87"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
 "spy": ("B1", "POS_COLLISION_C1_VERB_VS_B1_NOUN"),
 "popularity": ("B2", "C1_VS_B2_EXACT_SENSE"),
 "neutral": ("C1", "C1_SENSE_ALIGNMENT_CONTROL"),
 "sacred": ("C1", "C1_VS_C2_SENSE_BOUNDARY"),
 "signature": ("NOT_OBSERVED", "UNSUBSTANTIATED_C1"),
 "copyright": ("NOT_OBSERVED", "UNSUBSTANTIATED_C1"),
}
FALSE_FLAGS = ("independent_english_review", "independent_myanmar_review",
 "independent_example_review", "independent_exact_sense_cefr_review",
 "independent_pronunciation_review", "independent_approval", "george_emma_listened")
ORIGINAL = ("english_definition", "burmese_meaning", "example_sentence",
 "source_path", "source_index", "source_blob_sha")
ACCESS = "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_PAGE_HTTP_403"
SOURCE_NOTE = ("Public Cambridge search-index snippets inspected 2026-11-02; direct Cambridge page open returned HTTP 403. "
 "Indexed exact-sense labels are research leads only, not independently verified publisher page observations or human review. "
 "No independent approvals or listening/device/deployment evidence.")

def blob_sha(path):
 return subprocess.run(["git", "hash-object", str(path)], cwd=ROOT,
                       check=True, capture_output=True, text=True).stdout.strip()

def audit(packet, shortlist):
 errors = []
 if not isinstance(packet, dict) or not isinstance(shortlist, dict):
  return ["root must be object"]
 for key, value in {
  "schema": 1, "scope": "USER_APPROVED_CEFR_1000_STAGING_ONLY",
  "status": "RESEARCH_ONLY_NO_INDEPENDENT_APPROVAL", "observed_on": "2026-11-02",
  "shortlist_path": "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json",
  "shortlist_blob_sha": SHORTLIST_SHA, "source_access_note": SOURCE_NOTE,
  "reviewer_signoffs": 0, "real_audio_listening_signoffs": 0,
  "physical_iphone_safari_signoffs": 0, "production_deployed": False
 }.items():
  if packet.get(key) != value: errors.append("packet metadata: " + key)
 for key in ("counts_by_level", "independently_approved_by_level"):
  wanted = dict.fromkeys(LEVELS, 200 if key == "counts_by_level" else 0)
  if packet.get(key) != wanted: errors.append("packet quota/review: " + key)
 if shortlist.get("counts_by_level") != dict.fromkeys(LEVELS, 200):
  errors.append("frozen shortlist quota")
 if shortlist.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
  errors.append("frozen shortlist independent counts")
 source_entries = shortlist.get("entries")
 if not isinstance(source_entries, list) or len(source_entries) != 1000:
  return errors + ["frozen shortlist must contain exactly 1000"]
 byword = {}
 counts = dict.fromkeys(LEVELS, 0)
 for e in source_entries:
  if not isinstance(e, dict): errors.append("malformed shortlist entry"); continue
  w, level = e.get("word"), e.get("level")
  if level not in counts or not isinstance(w, str): errors.append("invalid level/headword"); continue
  counts[level] += 1
  if w.casefold() in byword: errors.append("duplicate cross-level headword: " + w)
  byword[w.casefold()] = e
  if e.get("editorial_hold") is not True or e.get("release_approved") is not False:
   errors.append("frozen entry release flag: " + w)
  for flag in ("reviewed_english", "reviewed_burmese", "reviewed_example",
               "reviewed_level", "reviewed_pronunciation"):
   if e.get(flag) is not False: errors.append("frozen entry reviewer flag: " + w + "/" + flag)
 if counts != dict.fromkeys(LEVELS, 200): errors.append("per-level 200 quota")
 entries = packet.get("entries")
 if not isinstance(entries, list) or len(entries) != len(EXPECTED):
  return errors + ["six research cards required"]
 seen = set()
 for item in entries:
  if not isinstance(item, dict): errors.append("malformed card"); continue
  w = item.get("word")
  if w not in EXPECTED or w in seen: errors.append("missing/duplicate unexpected card"); continue
  seen.add(w)
  source = byword.get(w)
  if not source or item.get("level") != "C1" or item.get("part_of_speech") != source.get("part_of_speech"):
   errors.append("headword/POS/level mismatch: " + w); continue
  original = item.get("original")
  if not isinstance(original, dict): errors.append("original missing: " + w); continue
  for key in ORIGINAL:
   if original.get(key) != source.get(key): errors.append("frozen original mismatch: " + w + "/" + key)
  pub = item.get("publisher_evidence")
  if not isinstance(pub, dict): errors.append("publisher evidence missing: " + w); continue
  if pub.get("publisher") != "Cambridge Dictionary" or pub.get("access") != ACCESS:
   errors.append("publisher/access forged: " + w)
  if pub.get("observed_on") != "2026-11-02" or pub.get("publisher_page_directly_verified") is not False:
   errors.append("observation/direct access forged: " + w)
  if pub.get("independent_exact_sense_cefr_review") is not False:
   errors.append("publisher review forged: " + w)
  if pub.get("indexed_cefr") != EXPECTED[w][0] or item.get("editorial_risk") != EXPECTED[w][1]:
   errors.append("indexed level or risk changed: " + w)
  url = pub.get("url")
  if url != "https://dictionary.cambridge.org/" + ("us/" if w in ("popularity","neutral","copyright") else "") + "dictionary/english/" + w:
   errors.append("canonical dictionary URL mismatch: " + w)
  for key in ("indexed_exact_sense", "other_sense_warning"):
   if not isinstance(pub.get(key), str) or len(pub[key]) < 12: errors.append("publisher exact-sense context missing: " + w)
  for key in ("editorial_finding",):
   if not isinstance(item.get(key), str) or len(item[key]) < 30: errors.append("editorial rationale missing: " + w)
  alt = item.get("unapproved_teaching_alternative")
  if not isinstance(alt, dict) or any(not isinstance(alt.get(k), str) or len(alt[k]) < 15 for k in ("english_definition","burmese_meaning","example_sentence")):
   errors.append("bilingual/example alternative missing: " + w)
  if not isinstance(item.get("reviewer_actions"), list) or len(item["reviewer_actions"]) != 4:
   errors.append("human review handoff missing: " + w)
  if item.get("editorial_hold") is not True: errors.append("editorial hold forged: " + w)
  for flag in FALSE_FLAGS:
   if item.get(flag) is not False: errors.append("independent/listening flag forged: " + w + "/" + flag)
 if seen != set(EXPECTED): errors.append("missing expected research headwords")
 return errors

def selftest(packet, shortlist):
 total = 0
 def reject(p, s, label):
  nonlocal total
  total += 1
  if not audit(p, s): raise AssertionError("fail-open synthetic mutation: " + label)
 for index, item in enumerate(packet["entries"]):
  for flag in FALSE_FLAGS:
   p = copy.deepcopy(packet); p["entries"][index][flag] = True
   reject(p, shortlist, item["word"] + "/" + flag)
  for field, value in (("indexed_cefr", "C1"), ("access", "DIRECT_PAGE_OPENED"),
                       ("publisher_page_directly_verified", True),
                       ("independent_exact_sense_cefr_review", True),
                       ("url", "https://dictionary.cambridge.org/dictionary/english/other")):
   p = copy.deepcopy(packet); p["entries"][index]["publisher_evidence"][field] = value
   if field == "indexed_cefr" and item["word"] in ("neutral","sacred"):
    p["entries"][index]["publisher_evidence"][field] = "B2"
   reject(p, shortlist, item["word"] + "/" + field)
  for context_key in ("indexed_exact_sense", "other_sense_warning"):
   for bad_value in ("", "B2 noun"):
    p = copy.deepcopy(packet)
    p["entries"][index]["publisher_evidence"][context_key] = bad_value
    reject(p, shortlist, item["word"] + "/" + context_key + "/missing_or_truncated")
  p = copy.deepcopy(packet); p["entries"][index]["original"]["burmese_meaning"] = "မမှန်ကန်"
  reject(p, shortlist, item["word"] + "/original")
  p = copy.deepcopy(packet); p["entries"][index]["editorial_hold"] = False
  reject(p, shortlist, item["word"] + "/hold")
 for field, value in (("production_deployed", True), ("reviewer_signoffs", 6),
                      ("real_audio_listening_signoffs", 1),
                      ("physical_iphone_safari_signoffs", 1),
                      ("source_access_note", "Direct publisher pages independently verified")):
  p = copy.deepcopy(packet); p[field] = value; reject(p, shortlist, field)
 s = copy.deepcopy(shortlist); s["entries"][0]["release_approved"] = True
 reject(packet, s, "frozen release")
 s = copy.deepcopy(shortlist); s["entries"][0]["word"] = s["entries"][1]["word"]
 reject(packet, s, "cross-level duplicate")
 print(f"PASS: {total}/{total} synthetic provenance, CEFR, Myanmar, approval and release mutations rejected; no human approval")

def main():
 parser = argparse.ArgumentParser()
 parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
 parser.add_argument("--self-test", action="store_true")
 args = parser.parse_args()
 for path, sha in ((PACKET, PACKET_SHA), (SHORTLIST, SHORTLIST_SHA)):
  if not path.is_file() or blob_sha(path) != sha:
   raise SystemExit("BLOCK: frozen blob changed " + str(path))
 packet = json.loads(PACKET.read_text(encoding="utf-8"))
 shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
 errors = audit(packet, shortlist)
 if errors: raise SystemExit("BLOCK: " + "; ".join(errors[:30]))
 if args.self_test: selftest(packet, shortlist)
 print("PASS: six source-bound, unapproved C1 Cambridge indexed leads; 200/level, 0 independent approvals; STAGING ONLY; " + args.level)

if __name__ == "__main__":
 main()
