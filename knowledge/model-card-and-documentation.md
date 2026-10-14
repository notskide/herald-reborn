---
id: model-card-and-documentation
title: "Model Cards and AI System Documentation"
summary: "Documenting model purpose, evaluations, intended users, limitations, and deployment conditions transparently."
tags: ["documentation","governance","model-evaluation","transparency"]
related: ["evaluation-and-test-sets","model-serving-and-api-design","privacy-and-secrets"]
sources: ["https://arxiv.org/abs/1810.03993","https://www.nist.gov/itl/ai-risk-management-framework"]
status: draft
updated: 2026-10-14
---

# Model Cards and AI System Documentation

A model card describes a model's intended use, evaluation, limitations, and relevant design information. Application documentation must also cover the surrounding system, because behavior changes with prompts, tools, retrieval sources, and permissions.

Useful sections include model identity and version, intended and out-of-scope use, training information where known, data constraints, evaluated languages and tasks, metrics, failure modes, safety tests, privacy, licensing, and deployment needs. Separate measured results from estimates and unknowns.

For the application, document architecture, data sources and freshness, access controls, prompt versions, supported tools, latency and memory measurements, fallbacks, monitoring, and incident handling. State whether evaluations were independent and which configurations were tested.

Avoid claims such as “safe,” “unbiased,” or “fully accurate” without defined evidence. A benchmark score applies only to its task, set, metric, and conditions. English-only testing does not demonstrate equal quality in every language.

Tie documentation to version identifiers and update it after material changes. Record known limitations and provide a route for reporting issues. If training details or weights are unavailable, say so rather than inventing them.

## Sources

- https://arxiv.org/abs/1810.03993
- https://www.nist.gov/itl/ai-risk-management-framework

## Sources

- https://arxiv.org/abs/1810.03993
- https://www.nist.gov/itl/ai-risk-management-framework
