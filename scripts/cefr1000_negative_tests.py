#!/usr/bin/env python3
"""Mutation tests: provisional structural gate must fail closed on corrupt evidence."""
import copy
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = ("CEFR-1000-PROVISIONAL-SHORTLIST.json", "CEFR-1000-INDEPENDENT-REVIEW-TASKS.json")

def run_gate(root):
    return subprocess.run([sys.executable, str(root / "scripts/cefr1000_staging_gate.py"), "--level", "A1"],
                          cwd=root, capture_output=True, text=True)

def main():
    with tempfile.TemporaryDirectory() as folder:
        root = pathlib.Path(folder)
        (root / "draft").mkdir()
        (root / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/cefr1000_staging_gate.py", root / "scripts")
        originals = {}
        for name in FILES:
            originals[name] = json.loads((ROOT / "draft" / name).read_text(encoding="utf-8"))
        def check(label, mutate):
            docs = copy.deepcopy(originals)
            mutate(docs[FILES[0]], docs[FILES[1]])
            for name, doc in docs.items():
                (root / "draft" / name).write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
            result = run_gate(root)
            if result.returncode == 0:
                raise AssertionError(f"{label}: corrupt provisional data passed gate")
            print(f"PASS rejected: {label}")
        # First establish that the unmodified provisional inventory passes structural checks.
        for name, doc in originals.items():
            (root / "draft" / name).write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        baseline = run_gate(root)
        if baseline.returncode != 0:
            raise AssertionError("Baseline failed structural gate: " + baseline.stdout + baseline.stderr)
        check("missing entry", lambda s,t: s["entries"].pop())
        check("cross-level duplicate", lambda s,t: s["entries"][-1].update(
            word=s["entries"][0]["word"], part_of_speech=s["entries"][0]["part_of_speech"]))
        check("fabricated approval", lambda s,t: s["entries"][0].update(reviewed_english=True))
        check("fake reviewer", lambda s,t: t["tasks"][0].update(reviewer_identity="Unverified Person"))
        check("wrong source provenance", lambda s,t: t["tasks"][0].update(source_blob_sha="invalid"))
        check("relabelled task", lambda s,t: t["tasks"][0].update(task_id="CEFR1000-A1-9999"))
        check("altered source shortlist SHA", lambda s,t: t.update(source_shortlist_blob_sha="invalid"))
        check("false release status", lambda s,t: t.update(release_status="APPROVED"))
        print("All eight negative cases rejected; no independent review inferred.")

if __name__ == "__main__":
    main()
