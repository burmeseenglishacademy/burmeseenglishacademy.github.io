#!/usr/bin/env python3
"""Fail-closed nine-card morphology/sense handoff; research only, NEVER human approval."""
import argparse
import collections
import copy
import hashlib
import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CROSSLEVEL-IRREGULAR-COMPARATIVES-AND-QUANTIFIERS-NINE-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads("{\"schema\":1,\"scope\":\"USER_APPROVED_CEFR_1000_STAGING_ONLY\",\"status\":\"UNAPPROVED_CROSS_LEVEL_IRREGULAR_FORMS_AND_QUANTIFIER_SENSE_TRIAGE\",\"observed_on\":\"2026-11-01\",\"shortlist_blob_sha\":\"475e68ae17ab97bd937e73e5ce4794e0dcd76551\",\"counts_by_level\":{\"A1\":3,\"A2\":5,\"B1\":1,\"B2\":0,\"C1\":0},\"first_pass_written_by_level\":{\"A1\":200,\"A2\":200,\"B1\":200,\"B2\":200,\"C1\":200},\"independently_approved_by_level\":{\"A1\":0,\"A2\":0,\"B1\":0,\"B2\":0,\"C1\":0},\"real_george_emma_listening_signoffs\":0,\"production_status\":\"BLOCKED_STAGING_ONLY\",\"publisher_scope_notice\":\"Nine directly inspected Oxford entries document inflection and exact-sense/POS distinctions. Dictionary form tables and topic badges are NOT independent exact-sense CEFR classification, and this packet is NOT independent English/Myanmar/example approval. The earlier four A1 be/do inflection risks are already separately quarantined; this packet targets additional comparative/superlative and cross-level noun/quantifier families.\",\"records\":[{\"word\":\"people\",\"level\":\"A1\",\"part_of_speech\":\"plural noun\",\"original_english_definition\":\"More than one person.\",\"original_burmese_meaning\":\"လူတွေ၊ လူများ\",\"original_example_sentence\":\"Many people are here.\",\"source_path\":\"draft/A1-EDITORIAL-STARTER.json\",\"source_index\":43,\"source_blob_sha\":\"ff1e93f60828ef2f94c9146522ce94075183b0ae\",\"family\":\"person/people\",\"morphology_class\":\"IRREGULAR_PLURAL_CROSS_LEVEL\",\"related_lemma\":\"person\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/people_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"107-115\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"},{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/person\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"103-115\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"Oxford explicitly says people is the usual plural of person in ordinary contexts. The A1 people card has only this plural meaning, while singular person is separately counted at A2; human must resolve whether two pedagogical forms count as separate vocabulary senses.\",\"risk_class\":\"INDEPENDENT_CROSS_LEVEL_LEXEME_COUNT_AND_PLURAL_AGREEMENT_REVIEW\",\"suggested_myanmar_UNAPPROVED\":\"လူများ (person ၏ ပုံမှန်အများကိန်း); အများကိန်းကြိယာနှင့် တွဲသုံးသည်\",\"suggested_example_UNAPPROVED\":\"Many people are waiting outside.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"good\",\"level\":\"A1\",\"part_of_speech\":\"adjective\",\"original_english_definition\":\"Of a high quality or pleasant.\",\"original_burmese_meaning\":\"ကောင်းသော\",\"original_example_sentence\":\"That is a good idea.\",\"source_path\":\"draft/A1-EDITORIAL-STARTER.json\",\"source_index\":44,\"source_blob_sha\":\"ff1e93f60828ef2f94c9146522ce94075183b0ae\",\"family\":\"good/better\",\"morphology_class\":\"BASE_ADJECTIVE\",\"related_lemma\":\"good\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/good_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-135\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"Oxford lists better as the comparative form of good. The A1 good example is grammatical and illustrates quality; do not mark it defective.\",\"risk_class\":\"BASE_FORM_CONTROL\",\"suggested_myanmar_UNAPPROVED\":\"ကောင်းသော (အရည်အသွေးကောင်းမွန်မှုကို ဖော်ပြသည်)\",\"suggested_example_UNAPPROVED\":\"That is a good idea.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"little\",\"level\":\"A1\",\"part_of_speech\":\"adjective\",\"original_english_definition\":\"Small in size or amount.\",\"original_burmese_meaning\":\"သေးငယ်သော၊ နည်းသော\",\"original_example_sentence\":\"I have a little dog.\",\"source_path\":\"draft/A1-EDITORIAL-STARTER.json\",\"source_index\":61,\"source_blob_sha\":\"ff1e93f60828ef2f94c9146522ce94075183b0ae\",\"family\":\"little/less/least\",\"morphology_class\":\"SIZE_ADJECTIVE_NOT_QUANTITY_DETERMINER\",\"related_lemma\":\"little\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/little_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-134\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"},{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/less_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-110\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"The held little card illustrates physical size in 'a little dog'. Oxford notes that the adjective's size comparison usually uses smaller/smallest, whereas less is a determiner for smaller quantities of uncountable nouns. Do not incorrectly treat less as the ordinary size-comparative of this card.\",\"risk_class\":\"DISTINCT_SIZE_VS_UNCOUNTABLE_QUANTITY_SENSE\",\"suggested_myanmar_UNAPPROVED\":\"သေးငယ်သော (အရွယ်အစား); ပမာဏကို ဖော်ပြသော a little နှင့် မရောထွေးရန်\",\"suggested_example_UNAPPROVED\":\"She lives in a little house.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"better\",\"level\":\"A2\",\"part_of_speech\":\"adjective\",\"original_english_definition\":\"Of a higher quality or more suitable than something else.\",\"original_burmese_meaning\":\"ပိုကောင်းသော\",\"original_example_sentence\":\"The second plan is better for our budget.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":86,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"family\":\"good/better\",\"morphology_class\":\"COMPARATIVE_FORM_OF_GOOD\",\"related_lemma\":\"good\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/better_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-113\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"},{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/good_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"103-123\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"Oxford labels better adjective explicitly as comparative of good; the held A2 better card teaches precisely that comparative quality sense, not a new lexical lemma. It must not inflate a 200-distinct-lexeme quota.\",\"risk_class\":\"NON_INDEPENDENT_COMPARATIVE_LEXEME_QUOTA\",\"suggested_myanmar_UNAPPROVED\":\"ပိုကောင်းသော (good ၏ comparative ပုံစံ; နှိုင်းယှဉ်ရာတွင် သုံးသည်)\",\"suggested_example_UNAPPROVED\":\"The second plan is better than the first one.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"person\",\"level\":\"A2\",\"part_of_speech\":\"noun\",\"original_english_definition\":\"One human being considered as an individual.\",\"original_burmese_meaning\":\"လူတစ်ဦး\",\"original_example_sentence\":\"Only one person can enter at a time.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":191,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"family\":\"person/people\",\"morphology_class\":\"SINGULAR_BASE_NOUN_CROSS_LEVEL\",\"related_lemma\":\"person\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/person\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-115\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"},{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/people_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"107-115\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"Oxford explicitly gives people as the ordinary plural of person and persons as a formal plural. The singular person card is A2 while the plural people card is A1; this is not automatically a CEFR error but needs a cross-level pedagogical rationale.\",\"risk_class\":\"CROSS_LEVEL_PLURAL_SINGULAR_PEDAGOGICAL_RATIONALE\",\"suggested_myanmar_UNAPPROVED\":\"လူတစ်ဦး၊ လူတစ်ယောက် (အနည်းကိန်း); အများကိန်းမှာ ပုံမှန်အားဖြင့် people\",\"suggested_example_UNAPPROVED\":\"One person is waiting outside.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"less\",\"level\":\"A2\",\"part_of_speech\":\"determiner\",\"original_english_definition\":\"A smaller amount of something that cannot usually be counted.\",\"original_burmese_meaning\":\"ပိုနည်းသော၊ လျော့နည်းသော\",\"original_example_sentence\":\"Please add less sugar to my tea.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":288,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"family\":\"little/less/least\",\"morphology_class\":\"UNCOUNTABLE_QUANTITY_DETERMINER\",\"related_lemma\":\"little_quantity\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/less_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-110\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"},{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/little_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"103-128\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"Oxford identifies less as a determiner/pronoun used with uncountable nouns for a smaller amount. The held less sugar example is grammatical and illustrates this meaning; it is not the comparative of little meaning physically small.\",\"risk_class\":\"DISTINCT_QUANTITY_FUNCTION_REVIEW_NOT_AUTOMATIC_BAN\",\"suggested_myanmar_UNAPPROVED\":\"ပိုနည်းသော (ရေတွက်မရသောနာမ်များနှင့် ပမာဏနှိုင်းယှဉ်ရာတွင်)\",\"suggested_example_UNAPPROVED\":\"Please use less sugar in the tea.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"bad\",\"level\":\"A2\",\"part_of_speech\":\"adjective\",\"original_english_definition\":\"Not good in quality or unpleasant.\",\"original_burmese_meaning\":\"မကောင်းသော၊ ညံ့သော\",\"original_example_sentence\":\"The bad weather delayed our trip.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":507,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"family\":\"bad/worst\",\"morphology_class\":\"BASE_ADJECTIVE\",\"related_lemma\":\"bad\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/bad_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-137\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"Oxford lists worse and worst as comparative and superlative forms of bad. The held bad weather example illustrates an ordinary quality sense.\",\"risk_class\":\"BASE_FORM_CONTROL\",\"suggested_myanmar_UNAPPROVED\":\"မကောင်းသော၊ ညံ့သော (အရည်အသွေး၊ အခြေအနေ)\",\"suggested_example_UNAPPROVED\":\"The weather was bad yesterday.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"least\",\"level\":\"A2\",\"part_of_speech\":\"determiner\",\"original_english_definition\":\"The smallest amount or number compared with others.\",\"original_burmese_meaning\":\"အနည်းဆုံးသော\",\"original_example_sentence\":\"This option requires the least effort.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":510,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"family\":\"little/less/least\",\"morphology_class\":\"MINIMUM_QUANTITY_DETERMINER\",\"related_lemma\":\"little_quantity\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/least_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-113\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"},{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/less_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-110\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"Oxford labels least a determiner/pronoun indicating the smallest amount, size or degree; the held 'least effort' is a valid quantity construction. It should not be automatically merged with the A1 little physical-size adjective.\",\"risk_class\":\"DISTINCT_QUANTITY_FUNCTION_REVIEW_NOT_AUTOMATIC_BAN\",\"suggested_myanmar_UNAPPROVED\":\"အနည်းဆုံးသော (ပမာဏ၊ အတိုင်းအတာ၊ ကြိုးစားအားထုတ်မှု)\",\"suggested_example_UNAPPROVED\":\"This option needs the least effort.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false},{\"word\":\"worst\",\"level\":\"B1\",\"part_of_speech\":\"adjective\",\"original_english_definition\":\"The least good or most unpleasant of a group.\",\"original_burmese_meaning\":\"အဆိုးဆုံး\",\"original_example_sentence\":\"That was the worst storm of the year.\",\"source_path\":\"draft/A2-C1-EDITORIAL-STARTER.json\",\"source_index\":57,\"source_blob_sha\":\"b04dd85db5cfae131c25aa4c73109778991b6fdc\",\"family\":\"bad/worst\",\"morphology_class\":\"SUPERLATIVE_FORM_OF_BAD\",\"related_lemma\":\"bad\",\"oxford_direct_sources\":[{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/worst_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"88-111\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"},{\"publisher\":\"Oxford University Press\",\"url\":\"https://www.oxfordlearnersdictionaries.com/definition/english/bad_1\",\"observed_on\":\"2026-11-01\",\"access\":\"DIRECT_PUBLISHER_PAGE_OPENED\",\"line_locator\":\"103-123\",\"evidence_scope\":\"GRAMMATICAL_FORM_OR_EXACT_SENSE_NOT_INDEPENDENT_CEFR\"}],\"source_supported_observation\":\"Oxford labels worst adjective explicitly as superlative of bad. The held B1 worst card teaches that exact superlative meaning; it is not a new lexical lemma for a distinct-lexeme quota.\",\"risk_class\":\"NON_INDEPENDENT_SUPERLATIVE_LEXEME_QUOTA\",\"suggested_myanmar_UNAPPROVED\":\"အဆိုးဆုံး (bad ၏ superlative ပုံစံ)\",\"suggested_example_UNAPPROVED\":\"That was the worst storm of the year.\",\"editorial_hold\":true,\"independently_checked\":false,\"release_approved\":false,\"independent_reviewer_receipt\":null,\"real_george_listening\":false,\"real_emma_listening\":false}]}")
EXPECTED_WORDS = ("people", "good", "little", "better", "person", "less", "bad", "least", "worst")
REQUIRED_NON_LEXICAL_FORMS = {"is": "be", "are": "be", "does": "do",
                              "did": "do", "better": "good", "worst": "bad"}
SENSE_DISTINCTIONS = ("less", "least", "little", "people", "person")
_spec = importlib.util.spec_from_file_location("cefr_final_manifest_gate", ROOT / "tools/validate_cefr_release.py")
release_gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(release_gate)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + bytes([0]) + raw).hexdigest()


def release_guard_errors():
    errors = []
    rules = getattr(release_gate, "NON_LEXICAL_INFLECTIONS", {})
    for form, lemma in REQUIRED_NON_LEXICAL_FORMS.items():
        if rules.get(form) != lemma:
            errors.append("Final manifest quota guard missing for " + form + " -> " + lemma)
    for word in SENSE_DISTINCTIONS:
        if word in rules:
            errors.append("Over-broad automatic inflection ban for " + word)
    # The synthetic manifest is intentionally NOT releasable. We test only
    # whether the target non-lexical-form defect is rejected by the real gate.
    for form, lemma in REQUIRED_NON_LEXICAL_FORMS.items():
        row = {"word": form, "level": "A1", "part_of_speech": "adjective",
               "english_definition": "Synthetic non-approved test",
               "burmese_meaning": "စမ်းသပ်ချက်",
               "example_sentence": "This is a synthetic test."}
        synthetic = {"targets": release_gate.TARGETS, "release_status": "UNVERIFIED_DO_NOT_PUBLISH",
                     "entries": [row]}
        defects = release_gate.validate(synthetic)
        if not any("grammatical form of " + lemma in x for x in defects):
            errors.append("Release validator failed open for synthetic " + form)
    return errors


def validate(packet, shortlist):
    errors = []
    if canonical(packet) != canonical(EXPECTED):
        errors.append("Nine-record source-bound research packet changed")
    raw = SHORTLIST.read_bytes()
    if git_blob_sha(raw) != EXPECTED["shortlist_blob_sha"]:
        errors.append("Full 1000-word held shortlist Git blob changed")
    if not isinstance(shortlist, dict):
        return errors + ["Shortlist must be a JSON object"]
    if canonical(shortlist) != canonical(json.loads(raw.decode("utf8"))):
        errors.append("Injected shortlist differs from frozen on-disk source")
    entries = shortlist.get("entries")
    if not isinstance(entries, list) or len(entries) != 1000:
        return errors + ["Exactly 1000 provisional entries required"]
    targets = {level: 200 for level in LEVELS}
    if shortlist.get("scope_target") != targets or shortlist.get("counts_by_level") != targets:
        errors.append("First-pass 200-per-level scope altered")
    if shortlist.get("independently_approved_by_level") != {level: 0 for level in LEVELS}:
        errors.append("Unsubstantiated independent review count")
    if shortlist.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("Frozen editorial-hold release status changed")
    counts = collections.Counter()
    lookup = {}
    for row in entries:
        if not isinstance(row, dict):
            errors.append("Non-object shortlist entry")
            continue
        counts[row.get("level")] += 1
        word = row.get("word")
        if not isinstance(word, str) or word.casefold() in lookup:
            errors.append("Missing or duplicated provisional headword")
        else:
            lookup[word.casefold()] = row
        if row.get("editorial_hold") is not True or any(
            row.get(field) is not False for field in
            ("reviewed_english", "reviewed_burmese", "reviewed_example",
             "reviewed_level", "reviewed_pronunciation", "release_approved")
        ):
            errors.append("Held shortlist row has false independent approval")
    if counts != collections.Counter(targets) or len(lookup) != 1000:
        errors.append("Per-level count or headword uniqueness failure")
    if tuple(r["word"] for r in EXPECTED["records"]) != EXPECTED_WORDS:
        errors.append("Research baseline headword sequence changed")
    fields = {"level": "level", "part_of_speech": "part_of_speech",
              "original_english_definition": "english_definition",
              "original_burmese_meaning": "burmese_meaning",
              "original_example_sentence": "example_sentence",
              "source_path": "source_path", "source_index": "source_index",
              "source_blob_sha": "source_blob_sha"}
    for frozen in EXPECTED["records"]:
        row = lookup.get(frozen["word"])
        if row is None:
            errors.append("Missing held word: " + frozen["word"])
            continue
        for left, right in fields.items():
            if canonical(frozen[left]) != canonical(row.get(right)):
                errors.append("Source snapshot mismatch: " + frozen["word"] + "." + right)
    errors.extend(release_guard_errors())
    return errors


def leaf_paths(value, prefix=()):
    if isinstance(value, dict):
        for k, v in value.items():
            yield from leaf_paths(v, prefix + (k,))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from leaf_paths(v, prefix + (i,))
    else:
        yield prefix


def mutate(value):
    if value is None:
        return {"forged": "human_approval"}
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if isinstance(value, str):
        return value + " [FORGED]"
    raise TypeError(type(value))


def replace_path(value, path):
    current = value
    for k in path[:-1]:
        current = current[k]
    k = path[-1]
    current[k] = mutate(current[k])


def self_test(packet, shortlist):
    rejected = 0
    def reject(p, s, label):
        nonlocal rejected
        if not validate(p, s):
            raise AssertionError("FAIL OPEN: " + label)
        rejected += 1
    for path in leaf_paths(packet):
        forged = copy.deepcopy(packet)
        replace_path(forged, path)
        reject(forged, shortlist, "packet " + repr(path))
    for word in EXPECTED_WORDS:
        for field in ("english_definition", "burmese_meaning", "example_sentence",
                      "part_of_speech", "level", "source_blob_sha", "source_index",
                      "editorial_hold", "reviewed_english", "release_approved"):
            forged = copy.deepcopy(shortlist)
            row = next(r for r in forged["entries"] if r["word"] == word)
            row[field] = mutate(row[field])
            reject(packet, forged, "held " + word + "." + field)
    for index in (0, 999):
        forged = copy.deepcopy(shortlist)
        forged["entries"][index]["release_approved"] = True
        reject(packet, forged, "false approval outside source-bound records")
    forged = copy.deepcopy(shortlist)
    forged["entries"][0]["word"] = forged["entries"][1]["word"]
    reject(packet, forged, "duplicate headword")
    for field in ("release_status", "scope_target", "counts_by_level",
                  "independently_approved_by_level"):
        forged = copy.deepcopy(shortlist)
        forged[field] = "FORGED"
        reject(packet, forged, "scope " + field)
    return rejected


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text("utf8"))
    shortlist = json.loads(SHORTLIST.read_text("utf8"))
    errors = validate(packet, shortlist)
    if errors:
        for issue in errors[:20]:
            print("FAIL:", issue, file=sys.stderr)
        return 1
    rows = [r for r in packet["records"] if args.level in ("ALL", r["level"])]
    report = {"scope": "STAGING_ONLY", "level": args.level,
              "source_bound_entries": len(rows),
              "direct_oxford_page_observations": sum(len(r["oxford_direct_sources"]) for r in rows),
              "new_comparative_superlative_lexeme_quota_risks": sum(
                  r["word"] in ("better", "worst") for r in rows),
              "independently_approved": 0, "real_listening_receipts": 0,
              "release": "BLOCKED"}
    if args.self_test:
        report["adversarial_mutations_rejected"] = self_test(packet, shortlist)
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
