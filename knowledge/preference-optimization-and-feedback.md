---
id: preference-optimization-and-feedback
title: "Preference Optimization and Human Feedback"
summary: "How preference comparisons and feedback can shape model behavior and the limits of preference-based objectives."
tags: ["alignment","training","feedback","evaluation"]
related: ["fine-tuning-versus-retrieval","data-quality-and-provenance","evaluation-and-test-sets"]
sources: ["https://arxiv.org/abs/2203.02155","https://arxiv.org/abs/2305.18290"]
status: draft
updated: 2026-10-14
---

# Preference Optimization and Human Feedback

Preference data records which of two or more responses a reviewer prefers under stated criteria. It can shape model behavior through training approaches such as reinforcement learning from human feedback and direct preference optimization.

A preference is not universal truth. It depends on the prompt, criteria, reviewer instructions, context, and trade-offs. A response may be preferred because it sounds confident even when it is less accurate. Reviewers may disagree, and their preferences may be unrepresentative.

Define whether reviewers should prioritize factual support, relevance, helpfulness, safety, or completeness. Keep evaluation examples separate from training data. Use diverse examples and examine the cases where reviewers disagree.

Optimizing a proxy can cause the system to exploit superficial patterns rather than achieve the underlying goal. Reward models can be fooled, and feedback can be noisy, biased, manipulated, or sensitive. After training, test factuality, calibration, refusals, language coverage, and instruction-following for regressions.

Preference optimization changes model behavior through training. Adding trusted facts to a Dictionary is a different operation: retrieval makes external information available at runtime. Systems may use both, but each requires its own evaluation.

## Sources

- https://arxiv.org/abs/2203.02155
- https://arxiv.org/abs/2305.18290

## Sources

- https://arxiv.org/abs/2203.02155
- https://arxiv.org/abs/2305.18290
