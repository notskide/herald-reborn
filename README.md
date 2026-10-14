# Herald Reborn

Herald Reborn is an evolving AI project built around a structured, source-linked knowledge dictionary and public examples for connecting applications to the Herald API.

## What this repository contains

- `knowledge/`: the expanding Dictionary of AI concepts, implementation practices, evaluation, safety, and deployment.
- `scripts/`: dependency-free tools for validation and keyword-based retrieval.
- `schemas/`: the metadata schema for knowledge entries.
- `docs/`: public developer guides and the project roadmap.
- `.github/workflows/`: automated checks for Dictionary consistency and search smoke tests.

## Herald's Dictionary

The Dictionary contains **82 indexed topics** spanning AI foundations and model architecture, training and optimization, prompting, retrieval and RAG, inference, serving, agents and tools, multimodal tasks, software integration, evaluation, privacy, safety, and governance. Each entry is a focused Markdown file with a stable ID, summary, tags, related entries, source links, review status, and update date.

This is a growing reference collection, not a complete encyclopedia. New and expanded material starts as `draft` until source relevance and important claims have been deliberately reviewed. An entry does not train a model or prove a claim simply because it exists.

Run from the repository root:

    python scripts/validate_knowledge.py
    python scripts/search_knowledge.py --query "How does retrieval-augmented generation work?"
    python scripts/search_knowledge.py --query "quantization memory" --limit 5
    python scripts/search_knowledge.py --query "privacy" --tag security

## Build bounded context for a model

The context builder selects the best Dictionary matches, includes entry IDs and source URLs, flags draft-only evidence, and enforces a character budget. It has no model dependency and treats retrieved text as untrusted reference material rather than executable instructions.

Run from the repository root:

    python scripts/context_builder.py --query "How does retrieval-augmented generation work?" --limit 4 --max-chars 6000
    python -m unittest discover -s scripts -p "test_*.py" -v

The context builder prepares evidence; it does not generate an answer. A real model inference endpoint is still required for chat generation.

## Connect Herald to your project

Start with [Connect a script to Herald](docs/connecting-to-herald.md). It includes Python, Node.js, and curl examples, request formats, authentication, and troubleshooting.

A developer needs an API base URL and an API key supplied by the API operator. This repository focuses on the Dictionary and developer integration examples; it does not prescribe where the API must run.

## Model names

Examples use the public model aliases `herald-core` and `herald-sentinel`. These aliases identify model options exposed by an API; they do not mean trained model weights are included in this repository.

## Principles

- **Structured:** use consistent formats and metadata.
- **Traceable:** record sources and distinguish evidence from inference.
- **Connected:** link related concepts explicitly.
- **Incremental:** make small, reviewable improvements.
- **Resource-conscious:** keep retrieval portable and usable on modest hardware.
- **Honest:** document limitations and never invent data, sources, model weights, or evaluation results.

## Status

The knowledge corpus and its tools are in active development. Entries remain drafts until reviewed. The goal is a useful, searchable, auditable knowledge source that supports Herald's runtime without requiring the entire corpus to be loaded into the model prompt.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
