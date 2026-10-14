---
id: agents-and-tool-use
title: "AI Agents and Tool Use"
summary: "How a model can propose tool calls in a controlled loop and why permissions must remain in application code."
tags: ["agents", "tools", "automation", "security"]
related: ["prompt-design-and-instruction-hierarchy", "model-serving-and-api-design", "prompt-injection-and-untrusted-content", "evaluation-and-test-sets"]
sources: ["https://arxiv.org/abs/2210.03629", "https://platform.openai.com/docs/guides/function-calling"]
status: draft
updated: 2026-10-14
---

# AI Agents and Tool Use

An AI agent is often a model-driven application that repeatedly observes information, selects an action, receives a result, and continues toward a goal. The term is broad, so describe actual capabilities rather than relying on the label.

## A controlled tool loop

1. The application sends the request and the tools the model may request.
2. The model proposes a tool and structured arguments.
3. Application code validates the tool name, arguments, permissions, and limits.
4. The application runs the tool and returns its result.
5. The model uses the result for another step or a final answer.
6. The application checks whether further actions are permitted.

A model's tool call is a proposal, not authorization. Application code must enforce access controls and validate arguments independently.

Use least privilege, timeouts, budgets, audit trails, and clear failure handling. Require human confirmation for consequential or irreversible actions where appropriate. Tool results are untrusted inputs. Start with read-only search before adding actions that change external systems.

## Sources

- https://arxiv.org/abs/2210.03629
- https://platform.openai.com/docs/guides/function-calling
