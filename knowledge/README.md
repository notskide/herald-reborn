# Herald's Knowledge Dictionary

This directory is the human-readable source of knowledge for Herald Reborn. Think of it as a version-controlled dictionary of concepts, definitions, practical rules, and source references. It is not a trained model and is not automatically correct just because an entry exists.

## Entry format

Each entry is a Markdown file with YAML front matter. Keep values in this simple form so the standard-library validator can parse them:

    ---
    id: example-topic
    title: "Example topic"
    summary: "A one-sentence summary."
    tags: ["example", "foundations"]
    related: ["another-topic"]
    sources: ["https://example.com/source"]
    status: draft
    updated: 2026-10-14
    ---

The id must be stable, lowercase, and hyphenated, and must match the filename without .md. Allowed statuses are draft, reviewed, and needs-update. Use an empty array when a field has no known values. Never invent source URLs; if no reliable source is available, say so in the entry and leave the sources list empty.

## Writing guidelines

- Keep one entry focused on one topic.
- Define unfamiliar terms the first time they appear.
- Separate established information from examples, interpretation, and open questions.
- Prefer primary papers, official documentation, standards, and reputable technical references.
- Summarize in original wording; do not copy source material at length.
- Link related entries by their IDs, not display titles.
- Use draft until source relevance and important claims have been reviewed.
- Use needs-update when an entry may be stale.
- Do not add secrets, private messages, or personal data.

## Index and tools

index.json is the navigation layer. Each entry's path is relative to this directory. Keep its title, tags, and relationships synchronized with the file.

Run from the repository root:

    python scripts/validate_knowledge.py
    python scripts/search_knowledge.py --query "semantic search"
    python scripts/search_knowledge.py --query "privacy" --tag security

The tools use Python's standard library and need no extra packages.
