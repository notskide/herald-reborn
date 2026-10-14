---
id: query-rewriting-and-expansion
title: "Query Rewriting and Expansion"
summary: "Transforming a user's question into better search queries while preserving its intent and constraints."
tags: ["retrieval","query-processing","search","rag"]
related: ["retrieval-and-search","keyword-search-and-ranking","vector-search-and-indexes"]
sources: ["https://arxiv.org/abs/2005.11401","https://scikit-learn.org/stable/modules/model_evaluation.html"]
status: draft
updated: 2026-10-14
---

# Query Rewriting and Expansion

A user's phrasing may differ from the language used in the documents that answer the question. Query rewriting normalizes or reformulates a question for search. Query expansion adds verified synonyms, aliases, or alternative terms to improve recall.

Preserve the user's goal, timeframe, entities, language, and constraints. Expanding an abbreviation can help; substituting a different product or jurisdiction can mislead. Keep the original request available and treat a rewrite as a search aid rather than a replacement for user intent.

Possible techniques include normalizing whitespace and punctuation, adding Dictionary aliases, extracting dates and entities, generating a small number of alternate phrasings, or splitting multi-part questions into sub-queries.

Expansion can hurt by adding common terms that overwhelm specific terms or by injecting a wrong assumption. Limit rewrites, merge result sets with deduplication, and preserve source provenance. Compare recall and precision before and after rewriting on a fixed test set with misspellings, ambiguous terms, multilingual requests, and strict constraints.

For a low-resource runtime, begin with deterministic normalization and a curated alias map before paying for model-based query expansion.

## Sources

- https://arxiv.org/abs/2005.11401
- https://scikit-learn.org/stable/modules/model_evaluation.html

## Sources

- https://arxiv.org/abs/2005.11401
- https://scikit-learn.org/stable/modules/model_evaluation.html
