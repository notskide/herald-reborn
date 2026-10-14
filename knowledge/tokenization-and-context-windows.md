---
id: tokenization-and-context-windows
title: "Tokenization and Context Windows"
summary: "How text becomes model tokens and why context capacity affects prompts, retrieval, and generated responses."
tags: ["tokens", "context-window", "language-models", "prompting"]
related: ["transformers-and-attention", "prompt-design-and-instruction-hierarchy", "retrieval-augmented-generation", "model-parameters-and-decoding"]
sources: ["https://huggingface.co/docs/transformers/main_classes/tokenizer", "https://huggingface.co/docs/tokenizers/index"]
status: draft
updated: 2026-10-14
---

# Tokenization and Context Windows

A tokenizer converts text into tokens that a model can process. A token may represent a word, part of a word, punctuation, whitespace, or another text unit. Tokens are not the same as words, and token counts vary with language, spelling, formatting, and tokenizer choice.

## Why tokenization matters

The tokenizer used with a model should match that model's requirements. Special tokens may mark message boundaries, roles, tool calls, or task-specific information. When exact token counts matter, use the matching tokenizer instead of estimating from characters or words.

## Context window

A context window is the amount of tokenized input and output a model can handle in one request. Depending on the model, instructions, conversation history, retrieved documents, tool output, and the response may share the same limit.

When context is too long, applications may summarize old messages, retrieve only relevant passages, remove low-value history, or reject oversized requests. Truncation should be explicit because it may discard a critical fact or instruction.

Keep retrieved passages focused, preserve IDs and sources, reserve room for the answer, and never assume every model has the same context limit.

## Sources

- https://huggingface.co/docs/transformers/main_classes/tokenizer
- https://huggingface.co/docs/tokenizers/index
