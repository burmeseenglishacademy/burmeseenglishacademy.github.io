#!/usr/bin/env node
// CEFR-1000 release gate. Fail closed; never changes data or grants approvals.
// Usage: node scripts/cefr1000-release-gate.cjs path/to/approved-manifest.json
const fs = require('node:fs');
const crypto = require('node:crypto');
const levels = ['A1','A2','B1','B2','C1'];
const errors = [];
const fail = (msg) => errors.push(msg);
const nonempty = (x) => typeof x === 'string' && x.trim().length > 0;
const validURL = (x) => { try { return /^https:$/.test(new URL(x).protocol); } catch { return false; } };
// Dates must be real, non-future calendar dates; arbitrary strings are not evidence.
const validDate = (x) => {
  if (typeof x !== 'string') return false;
  const d = /^\d{4}-\d{2}-\d{2}$/.test(x) ? x+'T00:00:00Z' : x;
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$/.test(d)) return false;
  const t = Date.parse(d);
  if (!Number.isFinite(t) || t > Date.now()) return false;
  // Date.parse may normalize invalid calendar days; require a round trip for date-only values.
  if (/^\d{4}-\d{2}-\d{2}$/.test(x) && new Date(t).toISOString().slice(0,10)!==x) return false;
  return true;
};
const path = process.argv[2];
if (!path) { console.error('BLOCKED: explicit approved manifest path required'); process.exit(1); }
let m;
try { m = JSON.parse(fs.readFileSync(path,'utf8')); }
catch(e) { console.error('BLOCKED: cannot read manifest:',e.message); process.exit(1); }
const entries = m.entries;
if (!Array.isArray(entries)) fail('entries array missing');
else {
  if (entries.length !== 1000) fail('expected exactly 1000 entries, got '+entries.length);
  const globalKeys = new Set();
  for (const level of levels) {
    const group = entries.filter(e=>e && e.level===level);
    if (group.length!==200) fail(level+': expected 200, got '+group.length);
    for (const [i,e] of group.entries()) {
      const tag=level+'['+i+'] '+String(e.word||'?');
      for (const field of ['word','part_of_speech','sense_id','english_definition','burmese_meaning','example_sentence']) {
        if (!nonempty(e[field])) fail(tag+': missing '+field);
      }
      const key=[e.word,e.part_of_speech,e.sense_id].map(s=>String(s||'').normalize('NFKC').trim().toLocaleLowerCase('en')).join('|');
      if(globalKeys.has(key)) fail(tag+': duplicate lexical sense '+key);
      globalKeys.add(key);
      if(e.editorial_hold!==false || e.release_approved!==true) fail(tag+': editorial hold/approval not cleared');
      for(const field of ['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation'])
        if(e[field]!==true) fail(tag+': '+field+' not independently approved');
      // A flag alone is insufficient: attributable independent reviewer, dated evidence, and exact sense source.
      const reviews=e.independent_reviews;
      for(const domain of ['english','burmese','example','cefr','pronunciation']) {
        const r=reviews?.[domain];
        if(!r || !nonempty(r.reviewer_id) || !validDate(r.signed_at) || !nonempty(r.evidence_url) || !validURL(r.evidence_url) || r.decision!=='approved')
          fail(tag+': independently signed '+domain+' evidence absent');
      }
      const sources=e.cefr_sources;
      if(!Array.isArray(sources)||!sources.some(s=>validURL(s.url)&&validDate(s.observed_on)&&nonempty(s.exact_sense)&&s.level===level))
        fail(tag+': source-backed exact-sense CEFR evidence absent');
      for(const voice of ['George','Emma']) for(const kind of ['headword','example']) {
        const a=e.audio?.[voice]?.[kind];
        if(!a || !nonempty(a.path)||!nonempty(a.sha256)||!(/^[0-9a-f]{64}$/i.test(a.sha256))||!nonempty(a.listening_reviewer)||!validDate(a.listened_at)||a.listening_result!=='pass')
          fail(tag+': real audio asset and listening signoff absent: '+voice+'/'+kind);
        else if(!fs.existsSync(a.path)) fail(tag+': audio file not present '+a.path);
        else if(crypto.createHash('sha256').update(fs.readFileSync(a.path)).digest('hex')!==a.sha256.toLowerCase())
          fail(tag+': audio checksum mismatch '+a.path);
      }
    }
  }
  for(const e of entries) if(!levels.includes(e?.level)) fail('unknown CEFR level');
}
for(const field of ['browser_regression','mobile_regression','physical_iphone_safari','github_pages_hosting','production_deployment','production_asset_preservation']) {
  const gate=m.release_evidence?.[field];
  if(!gate || gate.result!=='pass'||!nonempty(gate.evidence_url)||!validURL(gate.evidence_url)||!validDate(gate.checked_at))
    fail('release evidence missing: '+field);
}
if(m.release_evidence?.production_deployment?.result==='pass' && !nonempty(m.release_evidence?.production_deployment?.deployed_commit_sha))
  fail('production deployed SHA missing');
const summary={result:errors.length?'BLOCKED':'PASS',entries:Array.isArray(entries)?entries.length:null,counts:Object.fromEntries(levels.map(l=>[l,Array.isArray(entries)?entries.filter(e=>e?.level===l).length:0])),blocker_count:errors.length,blockers:errors.slice(0,30),structural_blockers:errors.filter(x=>/expected exactly 1000|expected 200|unknown CEFR level|duplicate lexical sense/.test(x)).slice(0,30)};
console.log(JSON.stringify(summary,null,2));
process.exit(errors.length?1:0);
