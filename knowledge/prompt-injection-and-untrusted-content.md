---
id: prompt-injection-and-untrusted-content
title: "Prompt Injection and Untrusted Content"
summary: "How hostile instructions in user input or retrieved documents can manipulate an AI application."
tags: ["prompt-injection", "security", "rag", "untrusted-data"]
related: ["prompt-design-and-instruction-hierarchy", "retrieval-augmented-generation", "agents-and-tool-use", "privacy-and-secrets"]
sources: ["https://genai.owasp.org/llmrisk/llm01-prompt-injection/", "https://www.nist.gov/itl/ai-risk-management-framework"]
status: draft
updated: 2026-10-14
---

# Prompt Injection and Untrusted Content

Prompt injection occurs when crafted input causes a model-driven application to behave in unintended ways. Instructions may be supplied directly by a user or indirectly through a document, webpage, code comment, or retrieved knowledge entry.

## Why it matters

Language models process instructions and ordinary text in a shared context. Delimiting untrusted text and asking a model to ignore embedded instructions can help, but neither method is a complete security boundary. Retrieval-augmented generation does not eliminate this risk.

## Defense in depth

- Treat user-provided and retrieved material as data, not trusted instructions.
- Keep secrets out of prompts whenever possible.
- Enforce authorization in application code, not by asking a model to self-police.
- Give tools narrow permissions and validate every action and argument.
- Require confirmation for sensitive side effects.
- Test direct and indirect injection attempts, including instructions hidden inside otherwise relevant content.
- Monitor unexpected actions and provide a way to stop or revoke access.

A dictionary entry may contain quoted malicious text for educational analysis. That text must never gain authority just because it was retrieved. Mark passages clearly and limit available tools.

## Sources

- https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- https://www.nist.gov/itl/ai-risk-management-framework
