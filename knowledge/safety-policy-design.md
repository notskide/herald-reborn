---
id: safety-policy-design
title: "AI Safety Policy Design"
summary: "Turning intended assistant behavior into clear rules, escalation paths, tests, and operational controls."
tags: ["safety","policy","governance","evaluation"]
related: ["prompt-design-and-instruction-hierarchy","prompt-injection-and-untrusted-content","evaluation-and-test-sets"]
sources: ["https://www.nist.gov/itl/ai-risk-management-framework","https://genai.owasp.org/llm-top-10/"]
status: draft
updated: 2026-10-14
---

# AI Safety Policy Design

A safety policy states what an assistant should do, what it must not do, and how it responds when requests are ambiguous, unsafe, unsupported, or outside its role. Policies are useful when translated into observable tests and application controls.

For each rule, define the situation, expected behavior, permitted alternatives, escalation path, and examples of correct and incorrect handling. Separate mandatory constraints from style preferences. Avoid vague instructions such as “be safe” without operational examples.

System instructions can guide behavior, but are not a security boundary by themselves. Enforce permissions, input limits, output schemas, tool authorization, and data controls in application code. Use retrieval filters for access restrictions and require confirmation for irreversible actions.

Avoid harmful overblocking. Test allowed and disallowed neighboring cases, track false refusals and unsafe completions, and refine the policy when it blocks legitimate uses unnecessarily. When a refusal is appropriate, explain it briefly and offer a safe alternative where possible.

Document policy ownership, versions, exceptions, review cadence, and incident handling. Re-test after changing models, prompts, tools, or retrieval sources. A policy cannot make a model perfectly reliable; boundaries and monitoring reduce risk but require ongoing validation.

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://genai.owasp.org/llm-top-10/

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://genai.owasp.org/llm-top-10/
