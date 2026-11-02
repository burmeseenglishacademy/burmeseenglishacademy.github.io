#!/usr/bin/env python3
"""Mechanical fail-closed audit of five held A2 Cambridge search-index sense leads.
This is not independent linguistic, CEFR, listening, mobile, or deployment approval.
"""
import argparse
import copy
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-A2-FIVE-DUE-PRETTY-THOUGHT-HIT-POST-INDEXED-SENSE-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "14afa1b1ac982a6ad19a29eb16502f889dcc172e"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
 "due": ("B1", "A2_VS_B1_EXPECTED_TIME", "https://dictionary.cambridge.org/dictionary/english/due"),
 "pretty": ("B1", "A2_VS_B1_INFORMAL_DEGREE_ADVERB", "https://dictionary.cambridge.org/us/dictionary/english/pretty"),
 "thought": ("B1", "A2_VS_B1_IDEA_NOUN", "https://dictionary.cambridge.org/dictionary/english/thought"),
 "hit": ("MIXED_A2_B1", "A2_HAND_ACTION_VS_B1_OBJECT_COLLISION", "https://dictionary.cambridge.org/dictionary/english/hit"),
 "post": ("NOT_OBSERVED_NOUN", "A2_UNLABELLED_INTERNET_NOUN_VS_B1_VERB", "https://dictionary.cambridge.org/dictionary/english/post"),
}
ORIGINAL = ("english_definition", "burmese_meaning", "example_sentence",
            "source_path", "source_index", "source_blob_sha")
FLAGS = ("independent_english_review", "independent_myanmar_review",
         "independent_example_review", "independent_exact_sense_cefr_review",
         "independent_pronunciation_review", "independent_approval", "george_emma_listened")
SOURCE_NOTE = ("Cambridge Dictionary publisher-owned search-index snippets inspected 2026-11-02; "
 "direct Cambridge headword page opens returned HTTP 403. Indexed labels are leads only, "
 "not independently verified direct publisher-page CEFR observations. No human-independent "
 "linguistic review, real listening, iPhone test or deployment was performed.")
ACCESS = "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_PAGE_HTTP_403"

def sha(path):
 return subprocess.run(["git", "hash-object", str(path)], cwd=ROOT,
                       check=True, text=True, capture_output=True).stdout.strip()

def audit(packet, shortlist):
 errors = []
 if not isinstance(packet, dict) or not isinstance(shortlist, dict):
  return ["research packet and shortlist must be objects"]
 meta = {"schema": 1, "scope": "USER_APPROVED_CEFR_1000_STAGING_ONLY",
         "status": "RESEARCH_ONLY_NO_INDEPENDENT_APPROVAL",
         "observed_on": "2026-11-02", "shortlist_path": "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json",
         "shortlist_blob_sha": SHORTLIST_SHA, "source_access_note": SOURCE_NOTE,
         "reviewer_signoffs": 0, "real_audio_listening_signoffs": 0,
         "physical_iphone_safari_signoffs": 0, "production_deployed": False}
 for k, v in meta.items():
  if type(packet.get(k)) is not type(v) or packet.get(k) != v: errors.append("packet metadata " + k)
 target = dict.fromkeys(LEVELS, 200)
 zero = dict.fromkeys(LEVELS, 0)
 for k, wanted in (("counts_by_level", target), ("independently_approved_by_level", zero)):
  if packet.get(k) != wanted or shortlist.get(k) != wanted: errors.append("quota/review counts " + k)
 entries = shortlist.get("entries")
 if not isinstance(entries, list) or len(entries) != 1000:
  return errors + ["exactly 1000 frozen source entries required"]
 byword, counts = {}, dict.fromkeys(LEVELS, 0)
 for e in entries:
  if not isinstance(e, dict): errors.append("malformed frozen entry"); continue
  w, lev = e.get("word"), e.get("level")
  if not isinstance(w, str) or lev not in counts: errors.append("invalid source word/level"); continue
  counts[lev] += 1
  if w.casefold() in byword: errors.append("duplicate cross-level headword " + w)
  byword[w.casefold()] = e
  if e.get("editorial_hold") is not True or e.get("release_approved") is not False:
   errors.append("frozen source release flag " + w)
  for f in ("reviewed_english", "reviewed_burmese", "reviewed_example",
            "reviewed_level", "reviewed_pronunciation"):
   if e.get(f) is not False: errors.append("frozen source reviewer flag " + w + "/" + f)
 if counts != target: errors.append("frozen source per-level quotas")
 cards = packet.get("entries")
 if not isinstance(cards, list) or len(cards) != 5:
  return errors + ["exactly five research cards required"]
 seen = set()
 for card in cards:
  if not isinstance(card, dict): errors.append("malformed research card"); continue
  w = card.get("word")
  if w not in EXPECTED or w in seen: errors.append("unexpected/duplicate research word"); continue
  seen.add(w)
  src = byword.get(w)
  if not src or src.get("level") != "A2" or card.get("level") != "A2" or card.get("part_of_speech") != src.get("part_of_speech"):
   errors.append("source level/POS mismatch " + w); continue
  orig = card.get("original")
  if not isinstance(orig, dict): errors.append("missing original " + w); continue
  for k in ORIGINAL:
   if orig.get(k) != src.get(k): errors.append("original provenance mismatch " + w + "/" + k)
  pub = card.get("publisher_evidence")
  if not isinstance(pub, dict): errors.append("missing publisher evidence " + w); continue
  lev, risk, url = EXPECTED[w]
  for k, v in {"publisher": "Cambridge Dictionary", "access": ACCESS, "url": url,
               "observed_on": "2026-11-02", "indexed_cefr": lev,
               "publisher_page_directly_verified": False,
               "independent_exact_sense_cefr_review": False}.items():
   if type(pub.get(k)) is not type(v) or pub.get(k) != v: errors.append("publisher evidence mismatch " + w + "/" + k)
  for k in ("indexed_exact_sense", "other_sense_warning"):
   if not isinstance(pub.get(k), str) or len(pub[k]) < 50:
    errors.append("publisher exact-sense warning absent " + w + "/" + k)
  if card.get("editorial_risk") != risk: errors.append("risk category mismatch " + w)
  if not isinstance(card.get("editorial_finding"), str) or len(card["editorial_finding"]) < 80:
   errors.append("editorial finding missing " + w)
  alt = card.get("unapproved_teaching_alternative")
  if not isinstance(alt, dict): errors.append("teaching alternative absent " + w)
  else:
   for k in ("english_definition", "burmese_meaning", "example_sentence"):
    if not isinstance(alt.get(k), str) or len(alt[k]) < 18:
     errors.append("bilingual teaching alternative absent " + w + "/" + k)
  if not isinstance(card.get("reviewer_actions"), list) or len(card["reviewer_actions"]) != 4:
   errors.append("human reviewer handoff absent " + w)
  if card.get("editorial_hold") is not True: errors.append("research hold forged " + w)
  for f in FLAGS:
   if card.get(f) is not False: errors.append("human/audio approval forged " + w + "/" + f)
 if seen != set(EXPECTED): errors.append("missing expected research card")
 return errors

def self_test(packet, shortlist):
 cases = 0
 def must_reject(p, s, name):
  nonlocal cases
  cases += 1
  if not audit(p, s): raise AssertionError("FAIL OPEN: " + name)
 for i, card in enumerate(packet["entries"]):
  for field, value in (("level", "B1"), ("part_of_speech", "noun" if card["part_of_speech"] == "verb" else "verb"),
                       ("editorial_risk", "SAFE"), ("editorial_hold", False),
                       ("independent_approval", True), ("george_emma_listened", True),
                       ("independent_english_review", True),
                       ("independent_myanmar_review", True),
                       ("independent_example_review", True),
                       ("independent_exact_sense_cefr_review", True),
                       ("independent_pronunciation_review", True),
                       ("reviewer_actions", [])):
   p = copy.deepcopy(packet); p["entries"][i][field] = value
   must_reject(p, shortlist, card["word"] + "/" + field)
  for field, value in (("url", "https://dictionary.cambridge.org/dictionary/english/other"),
                       ("publisher", "Oxford"), ("access", "DIRECT_PAGE_VERIFIED"),
                       ("observed_on", "2026-11-03"), ("indexed_cefr", "A2"),
                       ("publisher_page_directly_verified", True),
                       ("independent_exact_sense_cefr_review", True),
                       ("other_sense_warning", ""), ("indexed_exact_sense", "")):
   p = copy.deepcopy(packet); p["entries"][i]["publisher_evidence"][field] = value
   must_reject(p, shortlist, card["word"] + "/publisher/" + field)
  for field in ORIGINAL:
   p = copy.deepcopy(packet); p["entries"][i]["original"][field] = "FORGED"
   must_reject(p, shortlist, card["word"] + "/original/" + field)
  for field in ("english_definition", "burmese_meaning", "example_sentence"):
   p = copy.deepcopy(packet); p["entries"][i]["unapproved_teaching_alternative"][field] = ""
   must_reject(p, shortlist, card["word"] + "/alternative/" + field)
 for field, value in (("reviewer_signoffs", 1), ("real_audio_listening_signoffs", 1),
                      ("physical_iphone_safari_signoffs", 1), ("production_deployed", True),
                      ("status", "APPROVED"), ("shortlist_blob_sha", "FAKE"),
                      ("source_access_note", "DIRECT VERIFIED")):
  p = copy.deepcopy(packet); p[field] = value; must_reject(p, shortlist, "metadata/" + field)
 for field, value in (("reviewed_level", True), ("editorial_hold", False),
                      ("release_approved", True), ("level", "B2")):
  s = copy.deepcopy(shortlist); s["entries"][0][field] = value
  must_reject(packet, s, "frozen/" + field)
 p = copy.deepcopy(packet); p["entries"].pop(); must_reject(p, shortlist, "missing card")
 p = copy.deepcopy(packet); p["entries"][1] = copy.deepcopy(p["entries"][0])
 must_reject(p, shortlist, "duplicate card")
 print(f"PASS: {cases}/{cases} synthetic forged source, POS, CEFR, bilingual, provenance, review and listening mutations rejected")
 return cases

def main():
 parser = argparse.ArgumentParser()
 parser.add_argument("--level", choices=[*LEVELS, "ALL"], default="ALL")
 parser.add_argument("--self-test", action="store_true")
 args = parser.parse_args()
 if sha(PACKET) != PACKET_SHA: raise SystemExit("FAIL CLOSED: research packet blob drift")
 if sha(SHORTLIST) != SHORTLIST_SHA: raise SystemExit("FAIL CLOSED: frozen shortlist blob drift")
 packet = json.loads(PACKET.read_text(encoding="utf-8"))
 shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
 errors = audit(packet, shortlist)
 if errors: raise SystemExit("FAIL CLOSED: " + "; ".join(errors[:20]))
 if args.self_test: self_test(packet, shortlist)
 print("PASS: held A2 source-index research only; no independent review, voice listening, iPhone or deployment approval (" + args.level + ")")

if __name__ == "__main__":
 main()
