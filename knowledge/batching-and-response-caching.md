---
id: batching-and-response-caching
title: "Batching and Response Caching"
summary: "Ways to reduce repeated computation and improve throughput without changing the meaning of an answer."
tags: ["performance","caching","inference","serving"]
related: ["model-serving-and-api-design","retrieval-and-search","tokenization-and-context-windows"]
sources: ["https://huggingface.co/docs/transformers/main_classes/text_generation","https://cloud.google.com/architecture/ai-ml/llm-serving"]
status: draft
updated: 2026-10-14
---

# Batching and Response Caching

Batching groups compatible requests so a model or accelerator can process them together. It may improve throughput, but waiting to fill a batch can increase latency. Dynamic batching therefore needs a maximum batch size and a maximum waiting time.

## Cache types

- Exact response cache: reuses an answer for an identical normalized request.
- Retrieval cache: stores search results for a query and filter set.
- Embedding cache: avoids recomputing an embedding for unchanged text.
- Prompt-prefix cache: reuses computation for common prompt prefixes when the runtime supports it.
- Semantic cache: reuses results for questions considered similar; this is riskier because similar wording can hide material differences.

Cache keys must include every factor that affects correctness, such as model and prompt version, language, relevant parameters, access permissions, and knowledge-corpus version. Never serve a private result to another user because their prompt looks similar. Personalized or sensitive results may be unsuitable for caching.

Invalidate or version entries when the Dictionary, model, instructions, or permissions change. Use shorter lifetimes for volatile facts. Cache validated results, not transient failures. Measure cache hit rate, latency saved, memory use, stale answers, and isolation mistakes. Caching is an optimization, not a replacement for access control or evaluation.

## Sources

- https://huggingface.co/docs/transformers/main_classes/text_generation
- https://cloud.google.com/architecture/ai-ml/llm-serving

## Sources

- https://huggingface.co/docs/transformers/main_classes/text_generation
- https://cloud.google.com/architecture/ai-ml/llm-serving
