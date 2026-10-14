---
id: privacy-by-design-and-data-retention
title: "Privacy by Design and Data Retention"
summary: "Minimizing personal information throughout collection, retrieval, model calls, logging, storage, and deletion."
tags: ["privacy","data-retention","security","governance"]
related: ["privacy-and-secrets","conversation-state-and-history","memory-design-for-assistants"]
sources: ["https://www.nist.gov/privacy-framework/privacy-framework","https://eur-lex.europa.eu/eli/reg/2016/679/oj"]
status: draft
updated: 2026-10-14
---

# Privacy by Design and Data Retention

Privacy by design considers privacy while a system is specified and built. Data minimization asks whether each field is necessary for a defined purpose. Retention rules specify how long data is kept and how deletion is handled.

Map what the user submits, what the API logs, what the model provider receives, what retrieval indexes store, what tools return, and what backups retain. Include prompts, embeddings, caches, crash dumps, analytics, and evaluation samples where relevant. An embedding should not automatically be considered anonymous or harmless.

Collect only what is needed. Avoid unnecessary sensitive data in prompts. Restrict access to logs and stored conversations. Define retention periods by purpose instead of keeping all data indefinitely. Deletion may need to cover derived stores such as indexes, caches, summaries, exports, and backups. Describe technical limitations honestly.

Document purposes, permissions or lawful basis, vendor terms, user notices, access rights, incident response, and deletion mechanisms as appropriate to the jurisdiction. Legal obligations vary, so this entry is not legal advice.

For Herald, default to not retaining raw conversations unless the feature is necessary and clearly communicated. Store operational metrics without full prompt contents whenever possible.

## Sources

- https://www.nist.gov/privacy-framework/privacy-framework
- https://eur-lex.europa.eu/eli/reg/2016/679/oj

## Sources

- https://www.nist.gov/privacy-framework/privacy-framework
- https://eur-lex.europa.eu/eli/reg/2016/679/oj
