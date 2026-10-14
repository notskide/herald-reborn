---
id: hallucinations-and-grounding
title: "Hallucinations and Grounding"
summary: "Why generated answers can contain unsupported claims and how evidence-based response design reduces risk."
tags: ["hallucinations", "grounding", "reliability", "rag"]
related: ["retrieval-augmented-generation", "uncertainty-and-conflicting-evidence", "evaluation-and-test-sets", "data-quality-and-provenance"]
sources: ["https://www.nist.gov/itl/ai-risk-management-framework", "https://arxiv.org/abs/2005.11401"]
status: draft
updated: 2026-10-14
---

# Hallucinations and Grounding

A hallucination is generated content that is false, fabricated, or unsupported in the context where it is presented. An answer may contain a true statement with a fabricated citation, or a plausible explanation that the supplied evidence does not support.

## Why unsupported answers happen

Language models generate outputs from learned patterns and request context. They do not automatically verify every claim against authoritative evidence. Retrieval can fail, evidence can be stale or contradictory, and the model may overstate what a passage supports.

## Grounding practices

- Retrieve relevant, source-bearing entries for knowledge-specific questions.
- Preserve source IDs and URLs when providing claims.
- Distinguish direct evidence from inference or general background.
- Say when the dictionary contains no adequate evidence.
- Do not manufacture citations, statistics, quotations, or source details.
- Evaluate whether citations support the claims they accompany.

A response with citations can still be wrong. A source may be unreliable, misread, outdated, or unrelated to the exact claim. Attribution improves traceability but does not replace checking sources and evaluating answers.

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://arxiv.org/abs/2005.11401
