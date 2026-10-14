---
id: learning-and-memory
title: Learning and Memory in AI Systems
summary: A practical distinction between changing a model and storing information for later retrieval.
tags: [ai, learning, memory]
related: [knowledge-repositories, retrieval-and-search]
sources:
  - https://arxiv.org/abs/2302.07842
status: draft
updated: 2026-10-14
---

# Learning and Memory in AI Systems

An AI system can appear to learn over time in several different ways. These mechanisms should be distinguished because they have different costs, risks, and maintenance needs.

## Common mechanisms

- **Parameter training:** model weights are changed using a training process. This can be expensive and requires suitable data, evaluation, and compute.
- **External memory:** information is saved outside the model, such as in files, a database, or a vector index, and retrieved when needed.
- **Conversation context:** recent messages are provided to the model during a request. Context is useful but limited and should not be confused with durable storage.
- **Tool-assisted updates:** a system can collect candidate facts from approved sources, then validate and add them to its repository through a controlled workflow.

## Design implications for Herald Reborn

A practical first step is external, inspectable memory. Store facts with stable IDs, provenance, timestamps, and links to related concepts. Retrieval can then select relevant information without retraining a model every time the repository changes.

Updates should not be accepted blindly. Sources can be wrong, stale, or contradictory. A review process should record uncertainty and make changes auditable.

## Open questions

- How should conflicting sources be represented?
- When should old entries expire or be re-checked?
- Which changes can be automated safely, and which require human review?

## Source

- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020): https://arxiv.org/abs/2005.11401