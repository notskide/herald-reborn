# Herald Reborn

Herald Reborn is an evolving AI project with a structured knowledge dictionary and examples for connecting applications to the Herald API.

## What this repository contains

- docs: public developer guides and integration examples
- knowledge: curated dictionary entries and a navigation index
- schemas: metadata validation schema
- scripts: dependency-free tools to validate and search the dictionary

## Herald's Dictionary

The knowledge directory is Herald's inspectable knowledge dictionary. It currently covers AI foundations, neural networks, transformers, tokenization, embeddings, retrieval, prompting, evaluation, serving, safety, and data quality. Entries are focused Markdown files with stable IDs, tags, relationships, source URLs, review status, and update dates.

The corpus is an expanding foundation, not a complete encyclopedia. New entries start as drafts and should be reviewed before being marked reviewed. Keep the index synchronized and never invent sources.

Run from the repository root:

    python scripts/validate_knowledge.py
    python scripts/search_knowledge.py --query "How does retrieval-augmented generation work?"

## Connect Herald to your project

Start with the [Connect a script to Herald guide](docs/connecting-to-herald.md). It includes examples for Python, Node.js, and curl, plus request formats, authentication, and troubleshooting.

A developer needs an API base URL and an API key supplied by the API operator. This repository focuses on the dictionary and client-side examples; it does not prescribe where the API must run.

## Model names

Examples use the public model aliases herald-core and herald-sentinel. The aliases identify model options exposed by an API; they do not mean trained model weights are included in this repository.

## Principles

- Structured: use consistent formats and metadata.
- Connected: link related concepts explicitly.
- Traceable: record sources and distinguish evidence from inference.
- Incremental: make small, reviewable improvements.
- Resource-conscious: keep the knowledge layer portable and usable on modest hardware.

## Status

The knowledge corpus and its tools are in active development. Entries remain drafts until they receive deliberate review.

## Contributing

See CONTRIBUTING.md for contribution guidelines.
