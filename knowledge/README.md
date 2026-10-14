# Knowledge directory

This directory stores small, human-readable knowledge entries. Keep content portable and easy to inspect without special tooling.

## Entry format

Each entry is a Markdown file with YAML front matter:

```yaml
---
id: example-topic
 title: Example topic
summary: A one-sentence summary.
tags: [example, foundations]
related: [another-topic]
sources:
  - https://example.com/source
status: draft
updated: 2026-10-14
---

# Example topic

Write the explanation here.
```

Use a stable, lowercase, hyphenated `id` matching the filename (without `.md`). Allowed status values for now: `draft`, `reviewed`, `needs-update`. Use an empty list when there are no known related entries or sources. Never invent citations; when no reliable source is available, say so.

The index in `index.json` is the navigation layer. Keep it synchronized with entries as the repository grows.