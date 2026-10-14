---
id: uncertainty-and-conflicting-evidence
title: "Uncertainty and Conflicting Evidence"
summary: "How to represent unknowns, outdated claims, and source disagreements without hiding uncertainty."
tags: ["uncertainty", "sources", "facts", "reliability"]
related: ["data-quality-and-provenance", "hallucinations-and-grounding", "knowledge-repositories", "evaluation-and-test-sets"]
sources: ["https://www.nist.gov/itl/ai-risk-management-framework", "https://arxiv.org/abs/2005.11401"]
status: draft
updated: 2026-10-14
---

# Uncertainty and Conflicting Evidence

A knowledge system should distinguish what is known, what is inferred, what is disputed, and what is unknown. Fluent writing can sound certain even when available evidence is weak.

## Useful distinctions

- **Supported claim:** backed by a credible source relevant to the statement.
- **Inference:** derived from evidence but not stated by the source itself.
- **Unverified claim:** adequate supporting evidence has not been recorded.
- **Conflicting evidence:** sources disagree, perhaps because of different definitions, dates, or errors.
- **Stale evidence:** a source may once have been correct but no longer reflect the current state.

## Handling disagreements

Record the source for each claim, compare dates and definitions, and explain the exact point of disagreement. If the conflict cannot be resolved, preserve it and state what evidence might settle it. Do not silently discard an inconvenient source.

The assistant should calibrate its language to the strength of evidence. It can answer the supported part, identify missing information, and ask a clarifying question when ambiguity matters. A retrieval score indicates estimated relevance, not probability that a claim is true.

Use draft while an entry is being prepared, reviewed only after a human checks important claims and source relevance, and needs-update when content may be stale.

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://arxiv.org/abs/2005.11401
