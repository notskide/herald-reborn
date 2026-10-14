---
id: retrieval-augmented-generation
title: "Retrieval-Augmented Generation"
summary: "How an assistant retrieves external knowledge and provides it to a language model at answer time."
tags: ["rag", "retrieval", "grounding", "knowledge"]
related: ["knowledge-repositories", "retrieval-and-search", "embeddings-and-semantic-similarity", "hallucinations-and-grounding", "prompt-injection-and-untrusted-content"]
sources: ["https://arxiv.org/abs/2005.11401", "https://www.nist.gov/itl/ai-risk-management-framework"]
status: draft
updated: 2026-10-14
---

# Retrieval-Augmented Generation

Retrieval-augmented generation (RAG) connects a generative model to an external knowledge source. Instead of relying only on information encoded in model parameters, the application searches for relevant records and includes selected evidence in the request.

## Typical flow

1. Receive the user's question.
2. Retrieve candidate passages from a knowledge collection.
3. Rank and filter candidates.
4. Add selected passages, IDs, and sources to model context.
5. Generate an answer guided by that evidence.
6. Return source references and evaluate the result.

## Why RAG is useful

The knowledge store can be updated without retraining the model. Entries can be corrected, removed, cited, and version-controlled independently. This is useful for domain-specific information and changing facts.

## Limitations

RAG does not guarantee correctness. Search may miss a relevant entry, rank a weak passage too highly, or retrieve outdated or malicious content. A model may misunderstand evidence or invent details beyond it. Retrieval and generation therefore need separate evaluation.

For Herald, keep the dictionary inspectable, preserve stable entry IDs and sources, treat retrieved text as evidence rather than instructions, cite sources where possible, and allow an answer to say when evidence is insufficient. Begin with lexical search and add vector retrieval only when evaluation shows a need.

## Sources

- https://arxiv.org/abs/2005.11401
- https://www.nist.gov/itl/ai-risk-management-framework
