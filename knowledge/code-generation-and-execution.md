---
id: code-generation-and-execution
title: "Code Generation and Execution"
summary: "Practices for generating code with AI while treating generated programs as untrusted until reviewed and tested."
tags: ["coding","tools","security","evaluation"]
related: ["agents-and-tool-use","prompt-injection-and-untrusted-content","model-serving-and-api-design"]
sources: ["https://genai.owasp.org/llm-top-10/","https://docs.python.org/3/library/"]
status: draft
updated: 2026-10-14
---

# Code Generation and Execution

A code-generating model predicts a plausible program from requirements and context. Generated code may be syntactically valid yet logically wrong, insecure, incompatible with dependencies, or unsuitable for its runtime. Treat it as an untrusted proposal, not proof of correctness.

## Safer workflow

1. Specify inputs, outputs, constraints, expected errors, and supported environments.
2. Generate the smallest implementation that meets the specification.
3. Run syntax checks, tests, and relevant static analysis.
4. Review filesystem access, network access, subprocesses, dependencies, and secret handling.
5. Test invalid input, edge cases, concurrency, and resource limits.
6. Review the diff and maintain a rollback path.

Never execute unreviewed generated code with broad host privileges. Use a disposable sandbox with filesystem and network restrictions, resource quotas, and a timeout. Do not pass production credentials into a code-execution environment unless a narrowly scoped need has been justified. Dependency installation can execute code too.

Test behavior rather than copying the generated implementation's assumptions. Explanations from the same model are not independent verification. Code affecting money, identity, security, health, or irreversible actions requires appropriate human review.

## Sources

- https://genai.owasp.org/llm-top-10/
- https://docs.python.org/3/library/

## Sources

- https://genai.owasp.org/llm-top-10/
- https://docs.python.org/3/library/
