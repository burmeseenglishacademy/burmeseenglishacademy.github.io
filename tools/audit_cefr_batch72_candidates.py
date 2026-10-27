#!/usr/bin/env python3
"""Candidate-only screening. Never infer CEFR approval from structural clearance."""
import argparse,collections,json,re
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'draft'
def load(n):return json.loads((D/n).read_text(encoding='utf-8'))
def main(level):
    proposed=load('BATCH72-EXTRA-CANDIDATES.json')['proposed_by_level']
    files=[D/'A1-EDITORIAL-STARTER.json',*sorted(D.glob('A1-EXPANSION-BATCH*.json')),D/'A2-C1-EDITORIAL-STARTER.json',*sorted(D.glob('A2-C1-EDITORIAL-BATCH*.json')),*sorted(D.glob('A2-C1-RETIER-EDITORIAL-BATCH*.json')),*[p for p in sorted(D.glob('A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json')) if 'BATCH72' not in p.name]]
    prior=collections.defaultdict(list)
    for f in files:
        for r in json.loads(f.read_text(encoding='utf-8'))['entries']:prior[r['word'].casefold()].append(f.name)
    pool={r['word'].casefold():r for r in load('UNVERIFIED_CEFR_CANDIDATES.json')['entries']}
    out=[]
    for lvl,words in proposed.items():
        if level not in ('ALL',lvl):continue
        for w in words:
            flags=[]
            if not re.fullmatch('[a-z]{3,}',w):flags.append('INVALID_HEADWORD')
            if w.casefold() in prior:flags.append('PRIOR_AUTHORED_COLLISION')
            p=pool.get(w.casefold())
            if p and p.get('level')!=lvl:flags.append('UNVERIFIED_POOL_TIER_DISAGREEMENT')
            if p and re.search(r'\\b(?:surname|given name|capital of|city in|genus|species|trademark)\\b',str(p.get('english_definition_draft','')),re.I):flags.append('SUSPECT_WORDNET_SEED_SENSE')
            out.append({'level':lvl,'word':w,'mechanical_status':'QUARANTINE' if flags else 'CLEAR_ONLY_NOT_APPROVED','risk_flags':flags,'independently_checked':False})
    clear=[x for x in out if not x['risk_flags']]
    held=[x for x in out if x['risk_flags']]
    print('BATCH72 PREFLIGHT',level,'screened',len(out),'clear-only',len(clear),'quarantined',len(held))
    print('CLEAR_ONLY_WORDS',json.dumps([x['word'] for x in clear]))
    print('HELD_WORDS',json.dumps([{k:v for k,v in x.items() if k in ('word','risk_flags')} for x in held]))
    if level=='ALL':
        (D/'BATCH72-EXTRA-CANDIDATE-TRIAGE.json').write_text(json.dumps({'schema':1,'batch':72,'source':'GitHub Actions candidate-only screen','stage':'MECHANICAL_ONLY_NO_CEFR_APPROVAL','screened':len(out),'clear_only':len(clear),'quarantined':len(held),'records':out},ensure_ascii=False,indent=2)+'\\n',encoding='utf-8')
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--level',choices=['A2','B1','B2','C1','ALL'],required=True);main(a.parse_args().level)
