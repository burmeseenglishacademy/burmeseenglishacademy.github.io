#!/usr/bin/env python3
"""Prioritize 100 undrafted headwords per CEFR tier for human editorial selection.

This is a *queue*, not proof of sense, translation or CEFR correctness.
The first WordNet sense may be unrelated to the word's ordinary meaning.
"""
import json
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
pool=json.loads((root/'draft/UNVERIFIED_CEFR_CANDIDATES.json').read_text('utf8'))
drafts=json.loads((root/'draft/A2-C1-EDITORIAL-STARTER.json').read_text('utf8'))
evidence=json.loads((root/'draft/A2-C1-SOURCE-EVIDENCE-REVIEW.json').read_text('utf8'))
assert pool['release_status']==drafts['release_status']==evidence['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
assert len(pool['entries'])==5000
seen={x['word'] for x in drafts['entries']}
conflicts={x['word'] for x in evidence['records'] if x['provisional_level_conflicts_with_source']}
exclude={'trump','pussy','bible','congress','democrat','soviet','indian','irish','gay'}
named=re.compile(r'(?:United States|English (?:actor|actress|admiral|writer|engineer)|American (?:actor|actress|writer|politician)|a (?:city|town|state|country|republic|continent|university) (?:in|of)|the largest .* city|named after)',re.I)
for level, quota in [('A2',700),('B1',1000),('B2',1300),('C1',1500)]:
    rows=[x for x in pool['entries'] if x['level']==level]
    assert len(rows)==quota
    safe=[]
    deferred=[]
    for row in rows:
        w=row['word']
        if w in seen: continue
        clue=row.get('english_definition_draft','')
        reasons=[]
        if w in conflicts: reasons.append('SOURCE_LEVEL_CONFLICT')
        if w in exclude: reasons.append('REGISTER_OR_NAMED_ENTITY')
        if not re.fullmatch(r'[a-z]{3,}',w): reasons.append('FORM_OR_ABBREVIATION')
        if re.search(r'(ing|ed|s)$',w) and len(w)>5: reasons.append('MORPHOLOGICAL_FORM')
        if named.search(clue): reasons.append('POSSIBLE_PROPER_NOUN_FIRST_SENSE')
        if reasons: deferred.append((w,reasons))
        else: safe.append(w)
    print(f'{level} SHORTLIST {len(safe)} candidates after heuristic deferrals; first 100:')
    for i in range(0,min(100,len(safe)),10):
        print('  '+', '.join(safe[i:i+10]))
    print(f'{level} deferred {len(deferred)} candidate forms for extra sense review (not rejected).')
print('DISCLAIMER: ALL words and provisional CEFR levels remain unverified. No automatic publication.')
