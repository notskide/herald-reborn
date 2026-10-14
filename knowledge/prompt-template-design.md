---
id: prompt-template-design
title: "Prompt Template Design"
summary: "How to build reusable prompts with clear instructions, named inputs, bounded context, and testable output expectations."
tags: ["prompting","templates","reliability","llm"]
related: ["prompt-design-and-instruction-hierarchy","tokenization-and-context-windows","retrieval-augmented-generation"]
sources: ["https://platform.openai.com/docs/guides/prompt-engineering","https://huggingface.co/docs/transformers/main_classes/text_generation"]
status: draft
updated: 2026-10-14
---

# Prompt Template Design

A prompt template is a reusable structure into which an application inserts task instructions, user input, retrieved evidence, and constraints. It should make the task and output contract clear without wasting context on repeated or conflicting directions.

Useful components include the task, named input fields, source-grounded evidence with identifiers, constraints, output format, and a fallback for missing or conflicting evidence. Keep trusted instructions separate from user-provided and retrieved text. Delimiters improve clarity but are not a security boundary. Never include secrets or unnecessary personal data.

Version each template and store that version alongside evaluation results. Test realistic inputs, ambiguous requests, empty retrieval, malicious text inside a retrieved page, long conversations, and conflicting instructions. Prefer small controlled edits so a regression can be traced.

Longer prompts are not necessarily better: repetition can increase latency and distract from important instructions. Keep high-priority requirements explicit. For Herald, the template should tell the model when to use Dictionary evidence, how to cite entry IDs or source URLs, how to distinguish inference from evidence, and how to acknowledge missing support.

## Sources

- https://platform.openai.com/docs/guides/prompt-engineering
- https://huggingface.co/docs/transformers/main_classes/text_generation

## Sources

- https://platform.openai.com/docs/guides/prompt-engineering
- https://huggingface.co/docs/transformers/main_classes/text_generation
