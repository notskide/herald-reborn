---
id: evaluation-and-test-sets
title: "AI Evaluation and Test Sets"
summary: "How to evaluate retrieval and generation with representative cases, measurable criteria, and regression checks."
tags: ["evaluation", "testing", "metrics", "quality"]
related: ["data-quality-and-provenance", "retrieval-augmented-generation", "hallucinations-and-grounding", "fine-tuning-versus-retrieval"]
sources: ["https://arxiv.org/abs/2211.09110", "https://github.com/EleutherAI/lm-evaluation-harness"]
status: draft
updated: 2026-10-14
---

# AI Evaluation and Test Sets

Evaluation asks whether a system performs its intended tasks reliably. A few impressive demonstrations are not enough; evaluation needs representative inputs, explicit criteria, and repeatable procedures.

## Test-set design

Include questions clearly answered by the dictionary, paraphrased questions, unanswerable questions, ambiguous requests, stale or conflicting sources, prompt-injection attempts, long requests, and expected behavior when a backend is unavailable. Keep evaluation examples separate from training or tuning data.

## Measure components separately

- **Retrieval recall:** how often relevant evidence appears among selected results.
- **Ranking quality:** whether the best evidence appears near the top.
- **Groundedness:** whether answer claims are supported by evidence.
- **Answer quality:** correctness, completeness, relevance, and clarity.
- **Citation quality:** whether cited entries support the claims.
- **Operational behavior:** latency, error rate, resource use, and cost.

No single score captures all dimensions. Automated graders can scale review but may share biases or mistakes with the system under evaluation. Human review remains useful for nuanced cases.

Record model identifier, prompt version, dictionary version, and evaluation setup. Re-run tests when the corpus, retrieval, prompt, or model changes.

## Sources

- https://arxiv.org/abs/2211.09110
- https://github.com/EleutherAI/lm-evaluation-harness
