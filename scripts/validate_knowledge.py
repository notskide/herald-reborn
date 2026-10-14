#!/usr/bin/env python3
"""Validate dictionary entries, index metadata, and related-entry links."""
from __future__ import annotations
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
from knowledge_lib import parse_entry_file, parse_front_matter

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "knowledge"
ALLOWED_STATUS = {"draft", "reviewed", "needs-update"}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED = {"id", "title", "summary", "tags", "related", "sources", "status", "updated"}

def main() -> int:
    errors = []
    try:
        index = json.loads((KNOWLEDGE_DIR / "index.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read knowledge/index.json: {exc}", file=sys.stderr)
        return 1
    if not isinstance(index, dict) or not isinstance(index.get("entries"), list):
        print("FAIL: index.json must contain an entries array", file=sys.stderr)
        return 1
    discovered = {}
    files = sorted(p for p in KNOWLEDGE_DIR.glob("*.md") if p.name != "README.md")
    for path in files:
        try:
            metadata, _ = parse_front_matter(path.read_text(encoding="utf-8"))
            entry = parse_entry_file(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        missing, extra = REQUIRED - set(metadata), set(metadata) - REQUIRED
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing fields: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{path.relative_to(ROOT)} has unknown fields: {', '.join(sorted(extra))}")
        if entry.id != path.stem or not ID_PATTERN.fullmatch(entry.id):
            errors.append(f"{path.relative_to(ROOT)}: ID must be valid and match filename")
        if not entry.title.strip() or not entry.summary.strip():
            errors.append(f"{path.relative_to(ROOT)}: title and summary must be non-empty")
        if entry.status not in ALLOWED_STATUS:
            errors.append(f"{path.relative_to(ROOT)}: invalid status {entry.status!r}")
        try:
            date.fromisoformat(entry.updated)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: updated must be an ISO date")
        for field, values in (("tags", entry.tags), ("related", entry.related), ("sources", entry.sources)):
            if len(values) != len(set(values)):
                errors.append(f"{path.relative_to(ROOT)}: duplicate values in {field}")
        for related_id in entry.related:
            if not ID_PATTERN.fullmatch(related_id):
                errors.append(f"{path.relative_to(ROOT)}: invalid related ID {related_id!r}")
        for source in entry.sources:
            parsed = urlparse(source)
            if parsed.scheme not in {"https", "http"} or not parsed.netloc:
                errors.append(f"{path.relative_to(ROOT)}: source is not an HTTP(S) URL: {source!r}")
        if entry.id in discovered:
            errors.append(f"duplicate entry ID: {entry.id}")
        discovered[entry.id] = entry

    indexed = {}
    for number, record in enumerate(index["entries"], start=1):
        if not isinstance(record, dict):
            errors.append(f"index entry {number} must be an object")
            continue
        entry_id, path_value = record.get("id"), record.get("path")
        if not isinstance(entry_id, str) or not isinstance(path_value, str):
            errors.append(f"index entry {number} needs string id and path")
            continue
        if entry_id in indexed:
            errors.append(f"duplicate index ID: {entry_id}")
        indexed[entry_id] = record
        if path_value != f"{entry_id}.md":
            errors.append(f"index path for {entry_id!r} should be {entry_id}.md")
        relative = Path(path_value)
        if relative.is_absolute() or ".." in relative.parts:
            errors.append(f"unsafe index path: {path_value!r}")
            continue
        target = (KNOWLEDGE_DIR / relative).resolve()
        if not target.is_relative_to(KNOWLEDGE_DIR.resolve()) or not target.is_file():
            errors.append(f"index path missing or unsafe: {path_value!r}")
        parsed_entry = discovered.get(entry_id)
        if parsed_entry:
            if record.get("title") != parsed_entry.title:
                errors.append(f"index title differs from entry {entry_id!r}")
            if record.get("tags") != list(parsed_entry.tags):
                errors.append(f"index tags differ from entry {entry_id!r}")
            if record.get("related") != list(parsed_entry.related):
                errors.append(f"index related list differs from entry {entry_id!r}")

    if set(discovered) - set(indexed):
        errors.append("entries missing from index: " + ", ".join(sorted(set(discovered) - set(indexed))))
    if set(indexed) - set(discovered):
        errors.append("index IDs missing files: " + ", ".join(sorted(set(indexed) - set(discovered))))
    for entry_id, entry in discovered.items():
        for related_id in entry.related:
            if related_id not in discovered:
                errors.append(f"{entry_id}: related entry does not exist: {related_id}")
    if errors:
        print("Knowledge validation failed:", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1
    print(f"Knowledge validation passed: {len(discovered)} entries; index and relationships are consistent.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
