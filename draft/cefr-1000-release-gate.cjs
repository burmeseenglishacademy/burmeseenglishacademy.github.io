#!/usr/bin/env node
// CEFR-1000 fail-closed RELEASE-CANDIDATE preflight. No production writes.
// Usage: node draft/cefr-1000-release-gate.cjs <manifest.json> <evidence.json>
// This is deliberately NOT a provisional-shortlist approval tool.
'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const levels = ['A1','A2','B1','B2','C1'];
const errors = [];
const fail = (s) => errors.push(s);
const hash = (s) => crypto.createHash('sha256').update(s,'utf8').digest('hex');
function load(path) {
  if (!path) { fail('Missing required input path'); return null; }
  try { return JSON.parse(fs.readFileSync(path,'utf8')); }
  catch (e) { fail('Unreadable/invalid JSON: '+path+': '+e.message); return null; }
}
const manifest = load(process.argv[2]);
const evidence = load(process.argv[3]);
const entries = Array.isArray(manifest?.entries) ? manifest.entries : [];
if (entries.length !== 1000) fail('Expected exactly 1000 manifest entries; got '+entries.length);
const counts = Object.fromEntries(levels.map(l=>[l,0]));
const seen = new Set(), repeated = new Map(), senseKeys = new Set(), audioPaths = new Set();
const validDate = (v) => nonempty(v) && /^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z)?$/.test(v) && !Number.isNaN(Date.parse(v));
const evidenceRows = Array.isArray(evidence?.entries) ? evidence.entries : [];
const byId = new Map();
for (const e of evidenceRows) {
  if (!e || typeof e.entry_id !== 'string' || byId.has(e.entry_id)) fail('Missing/duplicate evidence entry_id');
  else byId.set(e.entry_id,e);
}
function nonempty(s) { return typeof s === 'string' && s.trim().length > 0; }
function signed(r, digest, field, id) {
  if (!r || r.verdict !== 'approved' || !nonempty(r.reviewer_id) ||
      !validDate(r.signed_at) || r.content_sha256 !== digest ||
      r.independent !== true || r.revoked === true) fail(id+': invalid independent '+field+' signoff');
}
for (const [i,e] of entries.entries()) {
  const id = e?.entry_id;
  if (!nonempty(id)) { fail('entry '+i+': missing immutable entry_id'); continue; }
  if (seen.has(id)) fail('Duplicate sense identity: '+id);
  seen.add(id);
  if (!levels.includes(e.level)) fail(id+': invalid CEFR level');
  else counts[e.level]++;
  if (![e.headword,e.part_of_speech,e.sense_id,e.english_definition,e.myanmar_meaning,e.original_example].every(nonempty))
    fail(id+': missing final headword/POS/sense/English/Myanmar/example');
  const canonical = JSON.stringify([id,e.level,e.headword,e.part_of_speech,e.sense_id,e.english_definition,e.myanmar_meaning,e.original_example]);
  const digest = hash(canonical);
  const k = String(e.headword||'').normalize('NFKC').trim().toLowerCase();
  if (k) repeated.set(k,(repeated.get(k)||0)+1);
  // A repeated headword is only permissible for a distinct, documented sense.
  const senseKey = [k,String(e.part_of_speech||'').normalize('NFKC').trim().toLowerCase(),String(e.sense_id||'').normalize('NFKC').trim().toLowerCase()].join('|');
  if (senseKeys.has(senseKey)) fail(id+': duplicate normalized headword/POS/sense identity');
  senseKeys.add(senseKey);
  const r = byId.get(id);
  if (!r) { fail(id+': missing evidence row'); continue; }
  if (r.content_sha256 !== digest) fail(id+': stale or mismatched content digest');
  for (const field of ['english','myanmar','example','cefr']) signed(r.reviews?.[field],digest,field,id);
  // Evidence must identify an actual reviewer, not merely assert independence.
  for (const field of ['english','myanmar','example','cefr']) {
    const review = r.reviews?.[field];
    if (review && (!nonempty(review.reviewer_id) || review.reviewer_id === r.author_id))
      fail(id+': reviewer identity absent or identical to content author for '+field);
  }
  const p = r.publisher_evidence;
  if (!p || !nonempty(p.publisher) || !/^https:\/\//.test(p.url||'') ||
      !validDate(p.observed_at) || !nonempty(p.exact_sense_locator) ||
      p.cefr_level !== e.level || p.part_of_speech !== e.part_of_speech)
    fail(id+': missing exact-sense publisher CEFR evidence');
  for (const voice of ['George','Emma']) for (const kind of ['headword','example']) {
    const a = r.audio?.[voice]?.[kind];
    if (!a || !nonempty(a.path) || !/^[a-f0-9]{64}$/.test(a.sha256||'') ||
        !/^[a-f0-9]{64}$/.test(a.spoken_text_sha256||'') ||
        a.spoken_text_sha256 !== hash(kind === 'headword' ? e.headword : e.original_example) ||
        !nonempty(a.voice_provenance) ||
        !(a.duration_seconds > 0) || a.listening?.audio_sha256 !== a.sha256 ||
        a.listening?.verdict !== 'pass' || a.listening?.actually_listened !== true ||
        !nonempty(a.listening?.listener_id) || !validDate(a.listening?.listened_at) ||
        a.listening?.listener_id === r.author_id)
      fail(id+': missing actual '+voice+' '+kind+' audio/listening evidence');
    if (nonempty(a?.path)) {
      const pathKey = a.path.normalize('NFKC').trim().toLowerCase();
      if (audioPaths.has(pathKey)) fail(id+': reused audio artifact path '+a.path);
      audioPaths.add(pathKey);
    }
  }
}
for (const l of levels) if (counts[l] !== 200) fail(l+': expected 200, got '+counts[l]);
if (byId.size !== entries.length) fail('Evidence row count mismatch');
for (const id of byId.keys()) if (!seen.has(id)) fail('Orphan evidence row: '+id);
const gate = evidence?.release_gates;
if (!gate || gate.release_candidate_sha !== manifest?.release_candidate_sha ||
    !/^[a-f0-9]{40}$/.test(gate.release_candidate_sha||'')) fail('Missing matching release candidate SHA');
for (const l of levels) for (const type of ['structural','adversarial']) {
  const j = gate?.ci_jobs?.[l]?.[type];
  if (!j || j.conclusion !== 'success' || j.status !== 'completed' ||
      j.head_sha !== gate.release_candidate_sha || !nonempty(String(j.run_id||'')) ||
      j.logs_inspected !== true) fail('Missing validated current-SHA CI job '+l+'/'+type);
}
for (const field of ['browser_mobile_regression','physical_iphone_safari','github_pages_hosting','production_asset_protection']) {
  const q = gate?.[field];
  if (!q || q.verdict !== 'pass' || q.release_candidate_sha !== gate.release_candidate_sha ||
      !/^https:\/\//.test(q.evidence_url||'') || !validDate(q.observed_at))
    fail('Missing release gate '+field);
}
// Predeployment readiness and postdeployment proof are intentionally separate.
// This script must NEVER authorize publication; it only checks evidence already supplied.
console.log(JSON.stringify({status:errors.length?'BLOCK':'EVIDENCE_PREFLIGHT_PASS_NOT_DEPLOY_AUTHORIZATION',
 counts, repeated_headwords:[...repeated].filter(([,n])=>n>1),
 errors:errors.slice(0,100), total_errors:errors.length},null,2));
process.exit(errors.length ? 1 : 0);
