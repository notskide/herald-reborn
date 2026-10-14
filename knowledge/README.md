# Herald's Knowledge Dictionary

This directory is the human-readable, version-controlled knowledge base for Herald Reborn. It currently contains **82 indexed topics** covering AI foundations, model training, retrieval and RAG, runtime architecture, applications, multimodal systems, evaluation, security, and responsible deployment.

**Important:** a larger Dictionary is not a trained model. Entries provide retrievable information for a runtime to use; a language model is still needed to generate flexible natural-language responses. Entries marked `draft` have not completed deliberate source and claim review.

## Entry format

Each entry is a Markdown file with front matter:

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

The ID must be stable, lowercase, hyphenated, and match the filename without `.md`. Allowed statuses are `draft`, `reviewed`, and `needs-update`. Use empty arrays where no known values exist. Never invent source URLs. Prefer primary research, official documentation, standards, and reputable technical references.

## Writing and maintenance rules

- Keep one entry focused on one concept; define terms before relying on them.
- Write original explanations instead of copying long source passages.
- Separate established claims from examples, recommendations, and unknowns.
- Link related entries by stable IDs and keep every relationship valid.
- New or substantially expanded entries start as `draft`. Mark `reviewed` only after checking key claims and source relevance.
- Update dates when content is checked or changed.
- Treat fast-changing model details, security guidance, and law as context-dependent.
- Do not put secrets, private conversations, personal records, or copyrighted source dumps in this public repository.

## Index and tools

The `index.json` file drives navigation and retrieval. Each record's title, tags, related links, and path must stay synchronized with its Markdown file. The validator checks metadata, duplicate IDs, source URL shape, indexed files, and relationships.

Run from the repository root:

    python scripts/validate_knowledge.py
    python scripts/search_knowledge.py --query "How does retrieval-augmented generation work?"
    python scripts/search_knowledge.py --query "quantization memory" --limit 5
    python scripts/search_knowledge.py --query "privacy" --tag security

The tools use Python's standard library and need no extra packages.
