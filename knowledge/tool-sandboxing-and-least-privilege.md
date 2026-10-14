---
id: tool-sandboxing-and-least-privilege
title: "Tool Sandboxing and Least Privilege"
summary: "Restricting what AI-triggered tools can access or modify so mistakes and manipulative inputs cause limited harm."
tags: ["security","tools","sandboxing","agents"]
related: ["agents-and-tool-use","prompt-injection-and-untrusted-content","adversarial-robustness-and-testing"]
sources: ["https://genai.owasp.org/llm-top-10/","https://owasp.org/www-project-api-security/"]
status: draft
updated: 2026-10-14
---

# Tool Sandboxing and Least Privilege

An assistant that calls tools inherits their capabilities. If a tool can read files, send messages, modify records, run commands, or access networks, model mistakes or prompt injection can trigger real side effects. Least privilege limits each tool to the minimum access needed.

Give tools narrow purposes and explicit schemas. Authorize every sensitive action in application code. Separate read-only operations from mutations. Require confirmation for destructive or irreversible operations. Apply timeouts, output limits, call budgets, and audit logging. Run code or document conversion in isolated environments with minimal filesystem and network access.

A safety instruction in a prompt is not a security boundary. Treat model-generated paths, URLs, and commands as untrusted input. Do not pass arbitrary tool output directly into another privileged interpreter. Keep credentials outside model-visible prompts and outputs.

Retrieved pages, attachments, user text, and tool responses should be treated as data rather than instructions that override application authority. Use distinct identities for development and production, and assume any single safeguard can fail.

Test unauthorized file access, path traversal, secret exfiltration, arbitrary URLs, oversized output, repeated tool calls, and actions without confirmation. Verify that attacks are blocked while legitimate tasks remain usable.

## Sources

- https://genai.owasp.org/llm-top-10/
- https://owasp.org/www-project-api-security/

## Sources

- https://genai.owasp.org/llm-top-10/
- https://owasp.org/www-project-api-security/
