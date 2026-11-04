#!/usr/bin/env python3
"""Read-only checks that protected BEA production learning/audio/privacy assets
remain identical on staging. This is a *pre-deployment preservation check*,
not user-experience, publishing, or post-release verification.
"""
import json
import pathlib
import subprocess
import sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
ASSETS=(
    "content.js",
    "ielts-vocabulary-data.js",
    "audio-manifest.js",
    "audio-player.js",
    "audio-integration.js",
    "privacy-tools.js",
    "privacy.html",
    "site-config.js",
    "audio",
)

def git(*args):
    result=subprocess.run(["git",*args],cwd=ROOT,check=True,capture_output=True,text=True)
    return result.stdout.strip()

def main():
    baseline="refs/remotes/origin/main"
    try:
        baseline_sha=git("rev-parse",baseline)
        stage_sha=git("rev-parse","HEAD")
        statuses=[]
        for path in ASSETS:
            base=git("rev-parse",baseline+":"+path)
            stage=git("rev-parse","HEAD:"+path)
            statuses.append({"path":path,"main_git_sha":base,"staging_git_sha":stage,
                             "identical":base==stage})
    except subprocess.CalledProcessError as err:
        print("BLOCKED: Could not inspect both Git branches",err.stderr,file=sys.stderr)
        return 2
    safe=all(x["identical"] for x in statuses)
    report={"status":"STAGING_PROTECTED_ASSET_COMPARISON_PASS" if safe else "BLOCKED_STAGING_ASSET_DIFF",
            "baseline_ref":baseline,"baseline_sha":baseline_sha,
            "staging_sha":stage_sha,"protected_paths_checked":len(statuses),
            "paths":statuses,
            "note":"Pre-deployment read-only comparison; does NOT prove production deployment or real-device QA."}
    out=ROOT/"scratch/cefr1000-preservation"
    out.mkdir(parents=True,exist_ok=True)
    (out/"report.json").write_text(json.dumps(report,indent=2)+"\n","utf-8")
    for item in statuses:
        print(("PASS" if item["identical"] else "FAIL"),item["path"])
    return 0 if safe else 1

if __name__=="__main__":
    raise SystemExit(main())
