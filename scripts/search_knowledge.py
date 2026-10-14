#!/usr/bin/env python3
"""Search Herald's knowledge dictionary without third-party packages."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
from knowledge_lib import load_entries, search_entries

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KNOWLEDGE_DIR = ROOT / "knowledge"

def main() -> int:
    parser = argparse.ArgumentParser(description="Search the Herald Reborn knowledge dictionary.")
    parser.add_argument("--query", required=True, help="question or keywords to search for")
    parser.add_argument("--limit", type=int, default=5, help="maximum results to print")
    parser.add_argument("--tag", help="only return entries carrying this tag")
    parser.add_argument("--status", choices=("draft", "reviewed", "needs-update"), help="filter by review status")
    parser.add_argument("--knowledge-dir", type=Path, default=DEFAULT_KNOWLEDGE_DIR, help="path to knowledge directory")
    args = parser.parse_args()
    try:
        entries = load_entries(args.knowledge_dir)
        results = search_entries(entries, args.query, limit=args.limit, tag=args.tag, status=args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"herald-search: {exc}", file=sys.stderr)
        return 2
    if not results:
        print("No matching entries. Try different words or remove the filters.")
        return 0
    for rank, (entry, score) in enumerate(results, start=1):
        print(f"{rank}. {entry.title} [id={entry.id}; score={score:.3f}; status={entry.status}]")
        print(f"   {entry.summary}")
        print(f"   File: knowledge/{entry.path}")
        for source in entry.sources:
            print(f"   Source: {source}")
        if entry.related:
            print("   Related: " + ", ".join(entry.related))
        print()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
