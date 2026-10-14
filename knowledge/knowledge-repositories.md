---
id: knowledge-repositories
title: "Knowledge Repositories"
summary: "How to organize information so it can be searched, checked, linked, and maintained."
tags: ["knowledge", "data-modeling", "foundations"]
related: ["learning-and-memory", "retrieval-and-search", "data-quality-and-provenance", "vector-search-and-indexes"]
sources: ["https://www.w3.org/TR/json-ld11/"]
status: draft
updated: 2026-10-14
---

# Knowledge Repositories

A knowledge repository is an organized collection of information intended for later discovery and use. It can be as simple as a folder of Markdown files or as sophisticated as a graph database with multiple indexes.

## Useful properties

- **Stable identifiers:** each entry has a durable ID independent of its displayed title.
- **Readable content:** humans can review the material without special software.
- **Metadata:** titles, tags, status, timestamps, and provenance support maintenance.
- **Relationships:** explicit links connect concepts and help navigation.
- **Validation:** schemas and automated checks catch malformed records and broken links.
- **Provenance:** source URLs and update history make claims easier to investigate.

## Start simple

Markdown files plus a JSON index are easy to version-control, inspect, diff, and review. A later tool can build full-text or vector indexes from the same source files. This keeps the source of truth portable and avoids committing to a complex database prematurely.

## Keep metadata consistent

Use a stable lowercase hyphenated ID matching the filename. Keep the JSON index synchronized with titles, tags, and relationships. Record source URLs and a review status. Use draft for content that has not received deliberate review; use reviewed only after important claims and sources have been checked; use needs-update for content that may be stale.

## Avoid common failure modes

- Do not store everything in one giant document.
- Do not confuse repeated text with verified knowledge.
- Do not allow links and indexes to drift out of sync.
- Do not discard source URLs or dates when importing material.
- Do not treat a high retrieval score as proof that a claim is correct.
- Do not include private data or secrets in a public corpus.

## Sources

- https://www.w3.org/TR/json-ld11/
