---
id: prompt-design-and-instruction-hierarchy
title: "Prompt Design and Instruction Hierarchy"
summary: "How to structure model instructions, user requests, examples, retrieved context, and output requirements."
tags: ["prompting", "instructions", "llms", "context"]
related: ["tokenization-and-context-windows", "retrieval-augmented-generation", "agents-and-tool-use", "prompt-injection-and-untrusted-content"]
sources: ["https://ai.google.dev/gemini-api/docs/prompting-strategies", "https://genai.owasp.org/llmrisk/llm01-prompt-injection/"]
status: draft
updated: 2026-10-14
---

# Prompt Design and Instruction Hierarchy

A prompt is the input supplied to a model for a request. Good prompt design makes the task, constraints, evidence, and desired output easier to interpret. A prompt is not a security boundary and cannot guarantee that a model follows every instruction.

## A useful structure

1. Define the role and goal.
2. State constraints, scope, and disallowed actions.
3. Supply relevant evidence with IDs and provenance.
4. Include the user's request.
5. Define the output shape if predictable formatting matters.
6. Describe how to handle missing evidence and uncertainty.

Examples can clarify behavior, but contradictory examples can create ambiguity. Keep instructions short, testable, and consistent.

## Separate data from instructions

Mark user content, webpages, files, and retrieved entries as untrusted data. They may contain text that attempts to control the model. The application should not let text inside a document override trusted instructions or authorize privileged actions.

Test prompts with ambiguous requests, irrelevant context, conflicting sources, injection attempts, and questions that cannot be answered from the dictionary. A prompt that works on a few hand-picked examples may fail in ordinary use.

## Sources

- https://ai.google.dev/gemini-api/docs/prompting-strategies
- https://genai.owasp.org/llmrisk/llm01-prompt-injection/
