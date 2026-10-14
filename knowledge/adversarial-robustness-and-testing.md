---
id: adversarial-robustness-and-testing
title: "Adversarial Robustness and Testing"
summary: "How to test AI systems against confusing, manipulative, malformed, or distribution-shifted inputs."
tags: ["robustness","security","evaluation","testing"]
related: ["prompt-injection-and-untrusted-content","evaluation-and-test-sets","hallucinations-and-grounding"]
sources: ["https://genai.owasp.org/llm-top-10/","https://www.nist.gov/itl/ai-risk-management-framework"]
status: draft
updated: 2026-10-14
---

# Adversarial Robustness and Testing

Robustness is an AI system's ability to behave acceptably when inputs are unusual, ambiguous, misleading, or intentionally hostile. An adversarial test is a controlled attempt to expose a failure mode, not merely a difficult question.

## What to test

- Input variation: misspellings, punctuation changes, long messages, mixed languages, and irrelevant content.
- Instruction conflicts: attempts to override system rules or reveal hidden configuration.
- Data attacks: poisoned documents, misleading retrieved pages, fabricated citations, and duplicated content.
- Resource attacks: very long prompts, repeated requests, and inputs designed to consume excessive compute.
- Boundary cases: empty input, unsupported formats, missing context, contradictory sources, and out-of-scope requests.

Define each test with an input, expected behavior, failure mode, and severity. Run the same suite after changes to prompts, retrieval, models, or tools. Track whether the target failure occurred and whether the system remains useful for legitimate requests.

No finite test suite proves that a system is secure. Combine repeatable tests with input limits, least-privilege tools, retrieval trust boundaries, output validation, rate limits, monitoring, and human review for high-impact actions. Avoid judging robustness from a few impressive demonstrations.

## Sources

- https://genai.owasp.org/llm-top-10/
- https://www.nist.gov/itl/ai-risk-management-framework

## Sources

- https://genai.owasp.org/llm-top-10/
- https://www.nist.gov/itl/ai-risk-management-framework
