---
id: knowledge-repositories
title: Knowledge Repositories
summary: How to organize information so it can be searched, checked, linked, and maintained.
tags: [knowledge, data-modeling, foundations]
related: [learning-and-memory, retrieval-and-search]
sources:
  - https://www.w3.org/TR/json-ld11/
status: draft
updated: 2026-10-14
---

# Knowledge Repositories

A knowledge repository is an organized collection of information intended for later discovery and use. It can be as simple as a folder of Markdown files or as sophisticated as a graph database with multiple indexes.

## Useful properties

- **Stable identifiers:** each concept or entry has a durable ID.
- **Readable content:** humans can review the source material without special software.
- **Metadata:** titles, tags, status, timestamps, and provenance make entries easier to manage.
- **Relationships:** explicit links connect concepts and allow navigation across topics.
- **Validation:** schemas and automated checks catch malformed records and broken links.
- **Provenance:** sources and update history make claims easier to verify.

## Start simple

For an early project, Markdown files plus a JSON index are easy to version-control and review. A later tool can build full-text or vector search indexes from the same source files. This keeps the source of truth portable and avoids committing to a complex database too early.

## Avoid common failure modes

- Do not store everything in one giant document.
- Do not confuse repeated text with verified knowledge.
- Do not allow links and indexes to silently drift out of sync.
- Do not discard source URLs or dates when importing material.
- Do not treat an entry's presence as proof that it is correct.

## Source

- W3C, *JSON-LD 1.1*: https://www.w3.org/TR/json-ld11/