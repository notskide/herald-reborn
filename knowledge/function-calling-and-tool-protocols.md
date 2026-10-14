---
id: function-calling-and-tool-protocols
title: "Function Calling and Tool Protocols"
summary: "How models request structured operations and how applications safely execute and return results."
tags: ["tools","agents","api","structured-output"]
related: ["agents-and-tool-use","model-serving-and-api-design","prompt-injection-and-untrusted-content"]
sources: ["https://platform.openai.com/docs/guides/function-calling","https://modelcontextprotocol.io/introduction"]
status: draft
updated: 2026-10-14
---

# Function Calling and Tool Protocols

Function calling lets a model request an operation through a structured interface instead of merely describing what it would do. The application defines tool names, descriptions, parameter schemas, and execution behavior. The model proposes a call; the application validates and executes it.

A safe cycle is: expose only appropriate tools, receive a candidate call, validate its name and arguments, check identity and authorization, require confirmation when needed, execute the operation, return bounded results, then validate the final answer.

Valid JSON does not prove a request is authorized. Reject unknown tools and malformed arguments. Separate read-only operations from side effects, and use idempotency keys for operations that may be retried. A tool protocol can standardize discovery and invocation, but interoperability does not make a tool trusted.

Treat tool results and retrieved pages as untrusted content. They cannot override the application's permission model. Never let a model decide its own permissions or retrieve secrets merely because a prompt asks. Audit high-impact calls and rely on the tool result—not the model's claim—to determine whether an operation succeeded.

## Sources

- https://platform.openai.com/docs/guides/function-calling
- https://modelcontextprotocol.io/introduction

## Sources

- https://platform.openai.com/docs/guides/function-calling
- https://modelcontextprotocol.io/introduction
