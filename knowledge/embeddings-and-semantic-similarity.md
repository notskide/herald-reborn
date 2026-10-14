---
id: embeddings-and-semantic-similarity
title: "Embeddings and Semantic Similarity"
summary: "What embeddings represent, how similarity is measured, and why vector closeness is not proof of factual relevance."
tags: ["embeddings", "semantic-search", "vectors", "retrieval"]
related: ["retrieval-and-search", "retrieval-augmented-generation", "vector-search-and-indexes", "evaluation-and-test-sets"]
sources: ["https://arxiv.org/abs/2210.07316", "https://huggingface.co/docs/transformers/index"]
status: draft
updated: 2026-10-14
---

# Embeddings and Semantic Similarity

An embedding is a numeric vector produced from an item such as a sentence, paragraph, image, or other input. Embedding models are designed so that useful relationships between inputs can be reflected in vector geometry.

## Similarity measures

- **Cosine similarity** compares vector directions, often after normalization.
- **Dot product** multiplies corresponding dimensions and sums results; vector magnitude can affect the score.
- **Euclidean distance** measures geometric distance between points.

The correct measure depends on the embedding model and whether vectors are normalized. Scores from different models generally should not be compared directly.

## What embeddings can and cannot do

Embedding search can find paraphrases and conceptually related text that exact keyword matching misses. It may still return text that shares a broad theme but does not answer the question. Rare names, numbers, negation, domain-specific terms, and multilingual queries can be challenging.

An embedding is not a complete symbolic meaning representation, a fact checker, or a probability that a claim is true. Evaluate retrieval against representative questions and judged relevant passages. Store vectors with stable source IDs and metadata.

## Sources

- https://arxiv.org/abs/2210.07316
- https://huggingface.co/docs/transformers/index
