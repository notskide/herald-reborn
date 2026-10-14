---
id: learning-and-memory
title: "Learning and Memory in AI Systems"
summary: "Differentiate parameter training, external knowledge memory, conversation context, and controlled updates."
tags: ["ai", "learning", "memory"]
related: ["ai-systems-and-models", "knowledge-repositories", "retrieval-and-search", "retrieval-augmented-generation", "data-quality-and-provenance"]
sources: ["https://arxiv.org/abs/2005.11401"]
status: draft
updated: 2026-10-14
---

# Learning and Memory in AI Systems

An AI system can appear to learn over time in several different ways. These mechanisms have different costs, risks, and maintenance needs.

## Common mechanisms

- **Parameter training:** model weights are changed using a training process. This can be expensive and requires appropriate data, evaluation, and compute.
- **External memory:** information is saved outside the model, such as in Markdown files, a database, or a search index, and retrieved when needed.
- **Conversation context:** recent messages are sent with a request. Context is useful but limited and is not durable storage by itself.
- **Tool-assisted updates:** a system can propose facts from approved sources and send them through a controlled review workflow.
- **Fine-tuning:** a pretrained model is further trained to adapt behavior or performance on a target task; it does not guarantee exact recall of individual facts.

## Design implications for Herald Reborn

Start with external, inspectable memory. Store facts with stable IDs, source URLs, timestamps, status, and links to related concepts. Retrieval can select relevant information without retraining a model every time the repository changes.

Treat the dictionary as an evidence store, not an infallible truth database. Sources can be wrong, stale, incomplete, or contradictory. Review should record uncertainty and make changes auditable.

## A simple lifecycle

1. Collect a candidate fact from a permitted source.
2. Write a focused entry with provenance.
3. Validate metadata, links, and relationships.
4. Review claims and source relevance.
5. Publish the entry and update the index.
6. Evaluate whether search retrieves it for representative questions.
7. Mark stale content for re-checking.

## Open questions

- How should conflicting sources be represented?
- When should old entries expire or be re-checked?
- Which changes can be automated safely, and which require human review?

## Sources

- https://arxiv.org/abs/2005.11401
