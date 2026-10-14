---
id: chunking-and-document-ingestion
title: "Chunking and Document Ingestion"
summary: "How to transform source documents into searchable, traceable units for retrieval-augmented generation."
tags: ["rag","chunking","documents","retrieval"]
related: ["retrieval-augmented-generation","retrieval-and-search","knowledge-repositories"]
sources: ["https://arxiv.org/abs/2005.11401","https://huggingface.co/docs/datasets/index"]
status: draft
updated: 2026-10-14
---

# Chunking and Document Ingestion

Document ingestion converts raw sources into units that can be indexed and retrieved. A pipeline commonly extracts text, removes irrelevant boilerplate where appropriate, preserves metadata, splits content into chunks, and records each source's identity and version.

## Chunking choices

- Fixed-size chunks are simple but may split a definition or argument.
- Structure-aware chunks follow headings, paragraphs, lists, or document sections.
- Semantic chunks aim to split when meaning changes, but can be more expensive and less predictable.
- Parent-child retrieval finds a small relevant passage while providing its larger section as context.
- Overlapping chunks repeat boundary text to preserve context, at the cost of duplicated material.

There is no universally best chunk size. Small chunks can improve pinpoint relevance but omit context; large chunks preserve context but dilute ranking and consume more prompt tokens. Tune chunking on real queries.

Preserve stable document IDs, source URLs, titles, headings, page numbers or offsets when available, retrieval timestamps, and access-control metadata. Treat extracted text as untrusted; enforce file-size and format limits and do not execute embedded content. Deduplicate near-identical versions so copied content does not dominate search.

## Sources

- https://arxiv.org/abs/2005.11401
- https://huggingface.co/docs/datasets/index

## Sources

- https://arxiv.org/abs/2005.11401
- https://huggingface.co/docs/datasets/index
