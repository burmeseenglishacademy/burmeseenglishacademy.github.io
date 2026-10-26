#!/usr/bin/env python3
"""Batch69 level-parallel structural quarantine and cross-corpus audit. Never approves content."""
import argparse, collections, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'draft'
COUNTS={"A2":12,"B1":10,"B2":16,"C1":22}
def load(name): return json.loads((D/name).read_text(encoding="utf-8"))
def prior_index():
    files=[D/'A1-EDITORIAL-STARTER.json',*sorted(D.glob('A1-EXPANSION-BATCH*.json')),D/'A2-C1-EDITORIAL-STARTER.json',*sorted(D.glob('A2-C1-EDITORIAL-BATCH*.json')),*sorted(D.glob('A2-C1-RETIER-EDITORIAL-BATCH*.json')),*[p for p in sorted(D.glob('A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json')) if 'BATCH69' not in p.name]]
    prior=collections.defaultdict(list)
    for p in files:
        for r in json.loads(p.read_text(encoding='utf-8'))['entries']: prior[r['word'].casefold()].append(p.name)
    return prior
def run(level):
    d=load('A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH69.json')
    t=load('A2-C1-SOURCE-RECOVERY-REVIEW-TASKS-BATCH69.json')
    q=load('A2-C1-SOURCE-RECOVERY-QUARANTINE-BATCH69.json')
    E,T,Q=d['entries'],t['entries'],q['records']
    assert d['release_status']=='UNVERIFIED_SOURCE_RECOVERY_DO_NOT_PUBLISH'
    assert t['release_status']=='UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH' and t['source_pages_not_yet_checked'] is True
    assert q['release_status']=='REVERSIBLE_EDITORIAL_QUARANTINE_NOT_APPROVED_DO_NOT_PUBLISH'
    assert len(E)==len(T)==len(Q)==60
    assert collections.Counter(e['proposed_level'] for e in E)==COUNTS
    assert d['counts_by_proposed_level']==COUNTS
    assert len({e['word'].casefold() for e in E})==60
    assert {e['word'] for e in E}=={x['word'] for x in T}=={x['word'] for x in Q}
    task={x['word']:x for x in T};hold={x['word']:x for x in Q}
    prior=prior_index()
    pool={x['word'].casefold():x for x in load('UNVERIFIED_CEFR_CANDIDATES.json')['entries']}
    problems=[];selected=0
    for e in E:
        if level!='ALL' and e['proposed_level']!=level: continue
        selected+=1;w=e['word']; x=task[w];h=hold[w]
        assert re.fullmatch('[a-z]{3,}',w),w
        assert e['part_of_speech'] in ('noun','verb','adjective','adverb'),w
        assert len(e['english_definition'])>=30,w
        assert re.search('[\\u1000-\\u109f]',e['burmese_meaning']),w
        s=e['example_sentence']
        assert len(s)>=35 and s[0].isupper() and s[-1] in '.?!',w
        assert re.search(r'(?<![a-z])'+re.escape(w)+r'(?![a-z])',s.casefold()),w
        assert e['editorial_hold'] is True and e['release_approved'] is False,w
        assert e['status']=='REVERSIBLE_QUARANTINE_PENDING_INDEPENDENT_EVIDENCE',w
        assert len(e['editorial_hold_reasons'])==3,w
        assert all(e[k] is False for k in ('reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation')),w
        assert all(e[k]=='' for k in ('source_english','source_burmese','source_level')),w
        assert x['editorial_hold'] is True and x['release_approved'] is False,w
        assert x['editorial_hold_reasons']==e['editorial_hold_reasons'],w
        for k in ('english_definition_review','burmese_review','example_review','cefr_review'):
            assert x[k]['completed'] is False and x[k]['reviewer'] is None and x[k]['observed_evidence'] is None,w
        assert x['english_definition_review']['source_observed'] is False,w
        assert all(v is False for v in x['audio_review'].values()),w
        assert h['reason_codes']==e['editorial_hold_reasons'] and h['hold_reversible'] is True,w
        assert h['independently_approved'] is False and h['release_approved'] is False,w
        if w in prior: problems.append({'word':w,'issue':'PRIOR_AUTHORED_COLLISION','files':prior[w]})
        p=pool.get(w)
        if p and p.get('level')!=e['proposed_level']: problems.append({'word':w,'issue':'UNVERIFIED_POOL_TIER_DISAGREEMENT','pool_level':p.get('level')})
        if p and re.search(r'\\b(?:surname|given name|capital of|city in|genus|species|trademark)\\b',str(p.get('english_definition_draft','')),re.I): problems.append({'word':w,'issue':'SUSPECT_WORDNET_SENSE'})
    if level=='ALL':
        assert 'UNVERIFIED_DRAFT_DO_NOT_PUBLISH' in (ROOT/'cefr-vocabulary-data.js').read_text(encoding='utf-8')
        assert re.search(r'entries:\\s*\\[\\s*\\]',(ROOT/'cefr-vocabulary-data.js').read_text(encoding='utf-8'))
        (ROOT/'batch69-triage-results.json').write_text(json.dumps({'batch':69,'drafts':60,'by_level':COUNTS,'independently_approved':0,'audio_generated':0,'problems':problems},ensure_ascii=False,indent=2)+'\\n',encoding='utf-8')
    print('BATCH69',level,'structurally checked',selected,'cross-corpus problems',json.dumps(problems,ensure_ascii=False))
    assert not problems,'Cross-corpus problems: quarantine and repair before considering structural-clear'
    print('PASS: structural-only. All held. No independent approval, no audio, no publication.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--level',choices=[*COUNTS,'ALL'],required=True)
    run(p.parse_args().level)
