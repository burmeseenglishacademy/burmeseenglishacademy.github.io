#!/usr/bin/env python3
"""Read-only provenance guard for CEFR-1000 author-side evidence notes.

This validates documentary completeness only. It never writes review fields,
assigns reviewers, or grants independent approval or release permission.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "draft"
TASKS_PATH = DRAFT / "CEFR-1000-INDEPENDENT-REVIEW-TASKS.json"
NOTE_GLOB = "CEFR-1000-EVIDENCE-*.md"
TASK_ID_RE = re.compile(r"\bCEFR1000-(A1|A2|B1|B2|C1)-(\d{4})\b")
URL_RE = re.compile(r"https?://[^\s<>()\]]+", re.IGNORECASE)
SHA_RE = re.compile(r"\b[0-9a-f]{40}\b", re.IGNORECASE)
DATE_RE = re.compile(
    r"\*\*(?:Observation date|Observed):\*\*\s*(\d{4}-\d{2}-\d{2})",
    re.IGNORECASE,
)
AUTHOR_RE = re.compile(r"author[- ]side", re.IGNORECASE)
NON_INDEPENDENT_RE = re.compile(
    r"(?:not\s+(?:an?\s+)?independent\s+(?:review|signoff|approval|verification)"
    r"|does\s+not\s+constitute\s+(?:an?\s+)?independent"
    r"|no\s+independent\s+(?:review|signoff|approval))",
    re.IGNORECASE,
)


def validate_note_text(text: str, task_by_id: dict, label: str = "<note>") -> list[str]:
    errors: list[str] = []

    date_match = DATE_RE.search(text)
    if not date_match:
        errors.append(f"{label}: missing bold Observed/Observation date (YYYY-MM-DD)")
    else:
        try:
            date.fromisoformat(date_match.group(1))
        except ValueError:
            errors.append(f"{label}: invalid observation date {date_match.group(1)!r}")

    if not AUTHOR_RE.search(text):
        errors.append(f"{label}: missing explicit author-side scope")
    if not NON_INDEPENDENT_RE.search(text):
        errors.append(f"{label}: missing explicit statement that this is not independent signoff")
    if not URL_RE.search(text):
        errors.append(f"{label}: no retained source URL")
    if not SHA_RE.search(text):
        errors.append(f"{label}: no 40-character source/provenance SHA")

    task_ids = set()
    for match in TASK_ID_RE.finditer(text):
        level, serial = match.groups()
        task_id = f"CEFR1000-{level}-{serial}"
        task_ids.add(task_id)
        task = task_by_id.get(task_id)
        if task is None:
            errors.append(f"{label}: unknown review task {task_id}")
        elif task.get("level") != level:
            errors.append(f"{label}: task-level mismatch for {task_id}")

    # A general provenance note may contain no candidate task IDs. Candidate
    # notes with IDs must resolve every ID to the canonical independent task.
    return errors


def main() -> int:
    try:
        tasks_data = json.loads(TASKS_PATH.read_text(encoding="utf-8"))
        tasks = tasks_data.get("tasks")
        if not isinstance(tasks, list) or len(tasks) != 1000:
            raise ValueError("review-task inventory must contain exactly 1000 tasks")
        task_by_id = {task.get("task_id"): task for task in tasks if isinstance(task, dict)}
        if len(task_by_id) != 1000:
            raise ValueError("review-task IDs must be unique and complete")

        notes = sorted(DRAFT.glob(NOTE_GLOB))
        if not notes:
            raise ValueError(f"no {NOTE_GLOB} files found")

        errors: list[str] = []
        referenced = set()
        for path in notes:
            content = path.read_text(encoding="utf-8")
            errors.extend(validate_note_text(content, task_by_id, path.relative_to(ROOT).as_posix()))
            referenced.update(TASK_ID_RE.findall(content))

        if errors:
            for error in errors:
                print("FAIL:", error)
            print(f"BLOCKED: {len(errors)} evidence-note provenance failure(s); no approval inferred")
            return 1

        unique_ids = {
            f"CEFR1000-{level}-{serial}"
            for level, serial in referenced
        }
        print(
            f"PASS: {len(notes)} author-side evidence notes; "
            f"{len(unique_ids)} canonical task IDs referenced; "
            "dates, source URLs, provenance SHAs and non-independent scope present."
        )
        print("READ-ONLY: no shortlist, task, reviewer, approval or release fields changed.")
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"BLOCKED: unable to validate evidence-note inventory: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
