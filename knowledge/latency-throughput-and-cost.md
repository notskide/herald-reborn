---
id: latency-throughput-and-cost
title: "Latency, Throughput, and Inference Cost"
summary: "How to measure response speed, request capacity, and resource consumption for AI services."
tags: ["latency","throughput","performance","serving"]
related: ["model-serving-and-api-design","quantization-and-inference","retrieval-and-search"]
sources: ["https://cloud.google.com/architecture/ai-ml/llm-serving","https://platform.openai.com/docs/guides/latency-optimization"]
status: draft
updated: 2026-10-14
---

# Latency, Throughput, and Inference Cost

Latency is how long a request takes to complete. Throughput is the amount of work completed per unit time, such as requests or generated tokens per second. Cost can include compute, provider charges, storage, network transfer, and operational effort.

For a RAG assistant, latency may come from network transit, authentication, history loading, query normalization, retrieval, reranking, prompt construction, model queueing, token generation, post-processing, and response transfer. Total latency alone hides the slow stage.

Measure p50/p95/p99 latency, time to first token, generation speed, queue length, failure rate, memory peak, and cost per successful answer. A fast but wrong or incomplete answer is not necessarily efficient.

Larger models and longer contexts often cost more but may improve capability. Batching can increase throughput while adding wait time. Caching saves repeated work but may serve stale results. Retrieving too few passages can remove necessary evidence.

Set timeouts, bound concurrency, limit output length, and profile realistic simultaneous requests. Compare changes using the same evaluation set and report quality beside speed and cost. For Herald, establish a retrieval-only baseline before adding model inference.

## Sources

- https://cloud.google.com/architecture/ai-ml/llm-serving
- https://platform.openai.com/docs/guides/latency-optimization

## Sources

- https://cloud.google.com/architecture/ai-ml/llm-serving
- https://platform.openai.com/docs/guides/latency-optimization
