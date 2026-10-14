---
id: memory-design-for-assistants
title: "Memory Design for Assistants"
summary: "Separating transient context, durable preferences, factual knowledge, and task state in a memory-enabled assistant."
tags: ["memory","personalization","conversation","privacy"]
related: ["learning-and-memory","conversation-state-and-history","privacy-and-secrets"]
sources: ["https://www.nist.gov/privacy-framework/privacy-framework","https://huggingface.co/docs/transformers/main_classes/text_generation"]
status: draft
updated: 2026-10-14
---

# Memory Design for Assistants

An assistant's memory is application-managed information available across turns or sessions. Memory can improve continuity, but it should not be one undifferentiated store of everything a user has said.

Useful categories include working context (recent turns), task state (intermediate results), explicit user preferences, general knowledge, and activity history retained under an operational policy. Each category has different freshness, privacy, and deletion requirements. Temporary task state should expire when the task ends; durable preferences should be based on actual statements rather than guesses.

Define how information is created, reviewed, updated, retrieved, and deleted. Store provenance and timestamps for facts that may change. A recent explicit correction should override an old assumption. Avoid inferring sensitive traits or saving speculative details as facts.

Only retrieve memory relevant to the current request. Scope records to the correct user and tenant. Keep private memories out of shared caches and public logs. Give users a way to inspect or correct durable memory when the product promises that capability.

More memory is not always better: irrelevant or stale records can confuse answers, increase context cost, and raise privacy risk. Measure whether each memory type improves real tasks before adding it.

## Sources

- https://www.nist.gov/privacy-framework/privacy-framework
- https://huggingface.co/docs/transformers/main_classes/text_generation

## Sources

- https://www.nist.gov/privacy-framework/privacy-framework
- https://huggingface.co/docs/transformers/main_classes/text_generation
