---
id: privacy-and-secrets
title: "Privacy and Secrets"
summary: "Basic safeguards for user information, API keys, conversation logs, and knowledge ingestion."
tags: ["privacy", "security", "api-keys", "data-handling"]
related: ["data-quality-and-provenance", "model-serving-and-api-design", "prompt-injection-and-untrusted-content", "agents-and-tool-use"]
sources: ["https://owasp.org/API-Security/", "https://www.nist.gov/privacy-framework"]
status: draft
updated: 2026-10-14
---

# Privacy and Secrets

AI applications can process prompts, conversation history, files, retrieved records, tool outputs, and provider credentials. Each data type needs a clear purpose, access policy, retention rule, and deletion process.

## Secrets

API keys and provider credentials are secrets. Keep them in environment variables or a secret manager; never commit them to source control, put them in browser code, or print them in logs. Rotate exposed keys and limit each key's privileges. Client applications should receive only credentials intended for them, not upstream model-provider credentials.

## User data

- Collect only what the product needs.
- Tell users what is stored and why.
- Avoid retaining raw prompts or responses without a clear reason.
- Restrict access to logs and backups.
- Define retention and deletion procedures.
- Remove unnecessary personal or sensitive data from datasets and evaluation cases.
- Review privacy terms of external model providers before sending user content.

Do not add private messages, credentials, personal records, or copyrighted text copied at length to a public dictionary without authorization. Public repository history is durable, so deleting a secret in a later commit does not make exposure harmless; rotate it immediately.

A model's promise to keep information private is not a substitute for access controls, storage protection, minimization, and retention enforcement.

## Sources

- https://owasp.org/API-Security/
- https://www.nist.gov/privacy-framework
