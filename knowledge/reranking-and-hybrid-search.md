---
id: reranking-and-hybrid-search
title: "Reranking and Hybrid Search"
summary: "Combining lexical and semantic retrieval, then using a stronger relevance model to order candidates."
tags: ["retrieval","search","ranking","rag"]
related: ["keyword-search-and-ranking","embeddings-and-semantic-similarity","vector-search-and-indexes"]
sources: ["https://arxiv.org/abs/2005.11401","https://huggingface.co/docs/transformers/index"]
status: draft
updated: 2026-10-14
---

# Reranking and Hybrid Search

Lexical search retrieves by matching terms. Dense semantic retrieval compares learned representations and can find related text even without exact word overlap. Hybrid retrieval combines signals from both; reranking then scores a smaller candidate set with a more detailed model.

Lexical methods are strong for exact names, IDs, technical identifiers, and rare terms. Dense methods can help with paraphrases and vocabulary mismatch. Neither dominates every query. Hybrid systems can merge rankings or learn a ranking function from relevance labels.

A reranker often evaluates a query and candidate passage together. This can improve top-rank relevance but adds latency and compute. It is generally cheaper to rerank a limited candidate set than the full corpus. Candidate-generation recall remains a ceiling: a reranker cannot choose evidence retrieval never returned.

Near-duplicates can crowd out distinct evidence. Semantic retrieval may find topical similarity without answering the question. Lexical search may miss synonyms. Evaluate candidate recall first, then rank metrics such as MRR or NDCG, and finally answer grounding. Keep provenance through deduplication.

For a small Dictionary, a well-tuned lexical ranker may be sufficient; add embeddings or reranking when measured misses justify the cost.

## Sources

- https://arxiv.org/abs/2005.11401
- https://huggingface.co/docs/transformers/index

## Sources

- https://arxiv.org/abs/2005.11401
- https://huggingface.co/docs/transformers/index
