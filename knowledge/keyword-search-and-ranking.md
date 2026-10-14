---
id: keyword-search-and-ranking
title: "Keyword Search and Ranking"
summary: "How lexical search finds and ranks text using normalized terms, field boosts, and BM25-style scoring."
tags: ["search", "keywords", "bm25", "retrieval"]
related: ["retrieval-and-search", "knowledge-repositories", "retrieval-augmented-generation", "evaluation-and-test-sets"]
sources: ["https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html", "https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html"]
status: draft
updated: 2026-10-14
---

# Keyword Search and Ranking

Keyword search retrieves records based on overlapping terms. It is a strong first step for a small, human-readable dictionary because it is easy to run, inspect, test, and maintain without an embedding model.

## Basic pipeline

- **Normalization:** case-fold text and apply a consistent tokenizer.
- **Indexing:** record terms in documents and optionally in title, tags, and summary fields.
- **Candidate matching:** find documents containing query terms.
- **Ranking:** score candidates so likely useful entries appear first.
- **Filtering:** limit results by tags, status, or access policy.

## BM25 in brief

BM25 is a widely used lexical ranking function. It considers how often a query term appears in a document, how rare that term is across the collection, and document length. Term-frequency saturation prevents repeated occurrences from increasing scores without limit; length normalization reduces bias toward long documents.

Field boosts can add weight to title or tag matches. Phrase bonuses can help exact names. These are heuristics and should be evaluated on representative queries.

## Known weaknesses

Keyword search may miss synonyms, paraphrases, spelling variations, or semantically related text with few overlapping tokens. It may also rank documents that mention words without answering the question. Start with transparent scoring, return entry IDs and sources, then improve based on observed failures.

## Sources

- https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html
- https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html
