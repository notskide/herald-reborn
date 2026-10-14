---
id: vector-search-and-indexes
title: "Vector Search and Indexes"
summary: "How vector indexes retrieve embedding neighbors and what trade-offs appear as a corpus grows."
tags: ["vector-search", "embeddings", "indexes", "retrieval"]
related: ["embeddings-and-semantic-similarity", "retrieval-augmented-generation", "knowledge-repositories", "evaluation-and-test-sets"]
sources: ["https://github.com/facebookresearch/faiss", "https://github.com/pgvector/pgvector"]
status: draft
updated: 2026-10-14
---

# Vector Search and Indexes

A vector index organizes embeddings so a system can retrieve items similar to a query vector. For small collections, comparing a query against every vector may be simple enough. Larger collections may use approximate-nearest-neighbor structures to reduce search time.

## Exact and approximate search

- **Exact search** checks all candidates under a chosen metric and can return the true nearest neighbors in the indexed set, at potentially higher cost.
- **Approximate search** explores a subset of candidates to improve speed or memory use, with some risk of missing exact neighbors.

Index choice affects latency, memory, insert and update cost, filtering, and recall. Benchmark a configuration on the target workload.

## Metadata matters

Store vector records with stable document IDs, chunk IDs, source URLs, timestamps, access restrictions, and tags. A vector without source metadata is hard to cite or refresh. When documents change, ensure associated embeddings are updated or removed.

Nearest-neighbor distance is not a factuality guarantee. A close result may be outdated, tangential, or contradicted by another entry. Herald's initial dictionary is small enough to start with keyword search; add vectors when evaluation shows they are worth the extra complexity.

## Sources

- https://github.com/facebookresearch/faiss
- https://github.com/pgvector/pgvector
