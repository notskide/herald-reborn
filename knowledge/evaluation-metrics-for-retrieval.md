---
id: evaluation-metrics-for-retrieval
title: "Evaluation Metrics for Retrieval"
summary: "How to measure whether a search or RAG system retrieves relevant evidence near the top of results."
tags: ["retrieval","evaluation","search","metrics"]
related: ["retrieval-and-search","keyword-search-and-ranking","retrieval-augmented-generation","evaluation-and-test-sets"]
sources: ["https://scikit-learn.org/stable/modules/model_evaluation.html","https://arxiv.org/abs/2005.11401"]
status: draft
updated: 2026-10-14
---

# Evaluation Metrics for Retrieval

Retrieval evaluation asks whether a system finds evidence needed for a query, not whether a language model writes fluent text afterward. A test set should contain representative queries and relevant documents or passages.

Recall@k measures how much known relevant evidence appears among the top k results. Precision@k measures the proportion of top-k results that are relevant. Mean reciprocal rank rewards placing the first relevant result near the top; mean average precision summarizes precision over relevant ranks; normalized discounted cumulative gain can represent graded relevance.

Choose metrics for the use case. If one precise passage is needed, early-rank metrics matter. If the task requires broad evidence coverage, recall may matter more. Evaluate generation separately: factual correctness, grounding, citation support, coverage, and abstention. A model may answer from prior knowledge even when retrieval failed, hiding a retrieval defect; a retrieved passage may also be misrepresented.

Include no-answer queries, ambiguous questions, conflicting sources, and cases where the corpus is incomplete. Keep test questions independent of article headings and record the index version and settings for repeatability.

## Sources

- https://scikit-learn.org/stable/modules/model_evaluation.html
- https://arxiv.org/abs/2005.11401

## Sources

- https://scikit-learn.org/stable/modules/model_evaluation.html
- https://arxiv.org/abs/2005.11401
