#!/usr/bin/env python3
"""Show next unreviewed A2–C1 candidate headwords for editorial drafting.
Never treats frequency tiers or WordNet first senses as verified CEFR content.
"""
import collections
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
source=json.loads((root/'draft/UNVERIFIED_CEFR_CANDIDATES.json').read_text('utf8'))
drafts=json.loads((root/'draft/A2-C1-EDITORIAL-STARTER.json').read_text('utf8'))
assert source['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
assert drafts['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
assert len(source['entries'])==5000
seen={r['word'] for r in drafts['entries']}
assert len(seen)==len(drafts['entries'])
tiers={'A2':700,'B1':1000,'B2':1300,'C1':1500}
for level, quota in tiers.items():
    group=[r for r in source['entries'] if r['level']==level]
    assert len(group)==quota
    remaining=[r for r in group if r['word'] not in seen]
    print(f'{level} next 30 unreviewed candidates ({len(remaining)} un-drafted):')
    for row in remaining[:30]:
        print(f"  {row['word']:17} | provisional POS: {row.get('part_of_speech','')} | lexical clue: {row.get('english_definition_draft','')[:105]}")
print('NOTE: NO levels, senses, meanings, translations, or audio approved')
