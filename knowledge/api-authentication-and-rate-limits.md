---
id: api-authentication-and-rate-limits
title: "API Authentication and Rate Limits"
summary: "Practical controls for identifying clients, protecting credentials, and keeping API usage within safe resource limits."
tags: ["api","security","authentication","operations"]
related: ["model-serving-and-api-design","privacy-and-secrets","quantization-and-inference"]
sources: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication","https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429","https://owasp.org/www-project-api-security/"]
status: draft
updated: 2026-10-14
---

# API Authentication and Rate Limits

Authentication asks who or what is making a request. Authorization asks what that identity may do. Rate limiting controls how often a client can consume a service. These are related but distinct protections.

## Credential handling

Use high-entropy API keys or a suitable identity mechanism. Store secrets in environment variables or a dedicated secret manager, never in public source code, browser bundles, logs, or error messages. Support rotation and revocation. Never treat a user-supplied account identifier as proof of identity.

## Rate-limit design

Limits may apply to requests per minute, concurrent requests, tokens per minute, daily usage, or estimated compute cost. Apply limits per identity and, where appropriate, per IP address. Return HTTP 429 when a limit is exceeded and provide a retry hint when useful. Include expensive request properties such as input length, output tokens, tool calls, and retrieval fan-out.

Authenticate before expensive work. Validate request size and model names. Use timeouts and bounded queues so a flood of requests cannot create unbounded memory use. Monitor denial rates and unusual traffic. Document limits for developers and ensure one client cannot exhaust shared capacity.

A rate limiter is not a substitute for authorization, and API keys should not be embedded in public client-side code where users can extract them.

## Sources

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
- https://owasp.org/www-project-api-security/

## Sources

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
- https://owasp.org/www-project-api-security/
