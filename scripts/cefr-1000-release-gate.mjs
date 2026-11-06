#!/usr/bin/env node
/**
 * CEFR-1000 release gate (staging only). Fail closed.
 * Usage: node scripts/cefr-1000-release-gate.mjs <approved-manifest.json>
 * This does not approve content, synthesize audio, or certify human review.
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';

const levels = ['A1','A2','B1','B2','C1'];
const errors = [];
const fail = (message) => errors.push(message);
const nonempty = (v) => typeof v === 'string' && v.trim().length > 0;
const validDate = (s) => {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(s ?? '')) return false;
  const d = new Date(s + 'T00:00:00Z');
  return !Number.isNaN(d.valueOf()) && d.toISOString().slice(0,10) === s &&
    d <= new Date();
};
const validUrl = (s) => {
  try { const u = new URL(s); return u.protocol === 'https:' && !!u.hostname; }
  catch { return false; }
};
const verified = (record, fields, label) => {
  if (!record || typeof record !== 'object') { fail(label + ': evidence missing'); return; }
  for (const f of fields) if (!nonempty(record[f])) fail(label + ': missing ' + f);
  if (!validDate(record.observed_on)) fail(label + ': invalid observation date');
  if (!validUrl(record.url)) fail(label + ': invalid evidence URL');
};
const signoff = (r, label) => {
  if (!r || typeof r !== 'object') { fail(label + ': independent signoff missing'); return; }
  for (const f of ['reviewer_id','signed_on','evidence_id','decision']) {
    if (!nonempty(r[f])) fail(label + ': missing ' + f);
  }
  if (r.decision !== 'approved') fail(label + ': not approved');
  if (!validDate(r.signed_on)) fail(label + ': invalid signoff date');
  if (r.independent !== true) fail(label + ': independent reviewer confirmation absent');
};
const manifestRoot = path.dirname(path.resolve(process.argv[2] || '.'));
const artifactPaths = new Set();
const artifact = (a, label) => {
  if (!a || typeof a !== 'object') { fail(label + ': artifact missing'); return; }
  if (!nonempty(a.path) || !nonempty(a.sha256) || !/^[a-f0-9]{64}$/i.test(a.sha256 ?? ''))
    fail(label + ': file path or sha256 missing/invalid');
  // Evidence metadata alone cannot prove that an audio file exists or matches its digest.
  // Reject path traversal, missing files, empty files and mismatched hashes.
  if (nonempty(a.path)) {
    const absolute = path.resolve(manifestRoot, a.path);
    const relative = path.relative(manifestRoot, absolute);
    if (path.isAbsolute(a.path) || relative.startsWith('..' + path.sep) || relative === '..') {
      fail(label + ': unsafe artifact path');
    } else {
      if (artifactPaths.has(absolute)) fail(label + ': reused audio artifact path');
      artifactPaths.add(absolute);
      try {
        const stat = fs.statSync(absolute);
        if (!stat.isFile() || stat.size === 0) fail(label + ': audio artifact empty or not a file');
        else {
          const actual = crypto.createHash('sha256').update(fs.readFileSync(absolute)).digest('hex');
          if (actual.toLowerCase() !== String(a.sha256 ?? '').toLowerCase())
            fail(label + ': audio artifact SHA256 mismatch');
        }
      } catch { fail(label + ': audio artifact inaccessible'); }
    }
  }
  if (!nonempty(a.listened_by) || !validDate(a.listened_on) ||
      a.listening_result !== 'pass' || !nonempty(a.listening_evidence_id))
    fail(label + ': real listening signoff missing');
};
const input = process.argv[2];
if (!input) { console.error('Usage: node scripts/cefr-1000-release-gate.mjs <approved-manifest.json>'); process.exit(2); }
let manifest;
try { manifest = JSON.parse(fs.readFileSync(input,'utf8')); }
catch (e) { console.error('FAIL: cannot parse manifest: ' + e.message); process.exit(1); }
if (manifest.release_status !== 'APPROVED_FOR_RELEASE') fail('release status not explicitly approved');
if (!Array.isArray(manifest.entries)) fail('entries array missing');
const entries = Array.isArray(manifest.entries) ? manifest.entries : [];
if (entries.length !== 1000) fail('expected exactly 1000 entries, found ' + entries.length);
const keys = new Set();
for (const level of levels) {
  const group = entries.filter(e => e?.level === level);
  if (group.length !== 200) fail(level + ': expected 200, found ' + group.length);
}
entries.forEach((e,i) => {
  const tag = 'entry['+i+']';
  if (!e || typeof e !== 'object') { fail(tag+': invalid entry'); return; }
  if (!levels.includes(e.level)) fail(tag+': invalid CEFR level');
  for (const field of ['word','part_of_speech','sense_id','english_definition','burmese_meaning','example_sentence']) {
    if (!nonempty(e[field])) fail(tag+': missing '+field);
  }
  // Global sense identity: same word/POS/sense may not be double-counted across levels.
  const key = [e.word,e.part_of_speech,e.sense_id].map(v=>String(v??'').normalize('NFKC').trim().toLocaleLowerCase('en')).join('|');
  if (keys.has(key)) fail(tag+': duplicate lexical sense '+key);
  keys.add(key);
  for (const aspect of ['english','burmese','example','level','pronunciation']) {
    signoff(e.independent_reviews?.[aspect],tag+' '+aspect);
  }
  verified(e.cefr_source,['publisher','exact_sense','cefr_level','observed_on','url','source_reference'],tag+' CEFR source');
  if (e.cefr_source?.url && !/^https:\/\//.test(e.cefr_source.url)) fail(tag+': invalid CEFR source scheme');
  if (e.cefr_source?.cefr_level !== e.level) fail(tag+': source CEFR mismatch');
  if (e.cefr_source?.exact_sense && e.sense_id && e.cefr_source.exact_sense !== e.sense_id)
    fail(tag+': source exact-sense mismatch');
  for (const voice of ['george','emma']) for (const kind of ['headword','example']) {
    artifact(e.audio?.[voice]?.[kind],tag+' '+voice+' '+kind);
  }
});
const gates = manifest.release_gates ?? {};
for (const name of ['desktop_browser','mobile_browser','physical_iphone_safari','github_pages_hosting','production_deployment','production_assets_preserved']) {
  const g = gates[name];
  if (!g || g.result !== 'pass' || !nonempty(g.evidence_id) || !validDate(g.checked_on))
    fail('release gate '+name+': pass with dated evidence required');
}
if (manifest.protection?.lessons_54_preserved !== true ||
    manifest.protection?.ielts_1000_preserved !== true ||
    manifest.protection?.existing_george_emma_audio_preserved !== true ||
    manifest.protection?.privacy_preserved !== true)
  fail('production preservation attestations incomplete');
if (errors.length) {
  console.error('CEFR-1000 RELEASE BLOCKED: '+errors.length+' failure(s)');
  for (const e of errors.slice(0,80)) console.error('- '+e);
  if (errors.length > 80) console.error('... '+(errors.length-80)+' further failures');
  process.exit(1);
}
console.log('CEFR-1000 manifest evidence structurally complete. Independent evidence must still be authenticated externally.');
