---
id: model-routing-and-fallbacks
title: "Model Routing and Fallbacks"
summary: "Selecting processing paths or models based on task needs, resource limits, and failure conditions."
tags: ["model-routing","reliability","inference","architecture"]
related: ["model-serving-and-api-design","latency-throughput-and-cost","inference-decoding-strategies"]
sources: ["https://cloud.google.com/architecture/ai-ml/llm-serving","https://www.nist.gov/itl/ai-risk-management-framework"]
status: draft
updated: 2026-10-14
---

# Model Routing and Fallbacks

Model routing chooses an execution path for each request. A router may send deterministic lookups to ordinary code, knowledge questions to retrieval, extraction to a specialized model, and difficult open-ended requests to a more capable model. It can also choose a backend based on availability, latency, privacy, and cost.

Define supported task types and a safe default path. Rules or an intent classifier can route requests, but both need tests for ambiguous and adversarial inputs. Do not let users choose privileged internal model identifiers or bypass authorization through route parameters.

Fallbacks must be explicit. If a primary model times out, a validated alternate may respond; if all models fail, return a clear error rather than inventing an answer. If retrieval fails, do not pretend the response is grounded.

Different models vary in instruction following, formatting, safety behavior, context length, latency, and language coverage. Validate every model behind a common interface and keep model-specific settings explicit. Track route, latency, errors, cost, and quality. Limit retries and use backoff to avoid retry storms. Choose a cheaper route only when it meets the task's quality requirements.

## Sources

- https://cloud.google.com/architecture/ai-ml/llm-serving
- https://www.nist.gov/itl/ai-risk-management-framework

## Sources

- https://cloud.google.com/architecture/ai-ml/llm-serving
- https://www.nist.gov/itl/ai-risk-management-framework
