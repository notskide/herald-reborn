---
id: source-attribution-and-provenance
title: "Source Attribution and Provenance"
summary: "Tracking where claims originated, how information was transformed, and which sources support an answer."
tags: ["sources","provenance","citations","trust"]
related: ["data-quality-and-provenance","knowledge-repositories","hallucinations-and-grounding","retrieval-augmented-generation"]
sources: ["https://www.w3.org/TR/prov-overview/","https://www.nist.gov/itl/ai-risk-management-framework"]
status: draft
updated: 2026-10-14
---

# Source Attribution and Provenance

Provenance records the origin and history of information. Attribution identifies which sources support a claim. Together, they help readers inspect evidence, detect stale material, and distinguish direct statements from interpretation.

For each knowledge item, store a stable identifier, source title, URL or archival reference, publisher or author where known, publication or update date, access date, and relevant license notes. Keep the Dictionary entry revision separate from the source revision. One source may support one part of an entry but not another.

When sources conflict, record the conflict and context instead of choosing silently. A citation is useful only when it resolves to relevant evidence and actually supports the statement nearby. Primary documentation and research papers are often useful for technical claims, but authority depends on the subject.

Generated citations need verification against retrieved source identifiers or checked URLs. Models can invent plausible titles, authors, page numbers, and links. Never claim a source was checked if it was not.

For Herald, maintain stable entry IDs and keep the index synchronized. Responses should identify the entry used and link to recorded sources where possible. If a source changes or becomes stale, re-review the dependent claims.

## Sources

- https://www.w3.org/TR/prov-overview/
- https://www.nist.gov/itl/ai-risk-management-framework

## Sources

- https://www.w3.org/TR/prov-overview/
- https://www.nist.gov/itl/ai-risk-management-framework
