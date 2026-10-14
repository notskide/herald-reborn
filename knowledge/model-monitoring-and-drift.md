---
id: model-monitoring-and-drift
title: "Model Monitoring and Drift"
summary: "Detecting changes in inputs, retrieval behavior, model outputs, and user needs after deployment."
tags: ["monitoring","drift","evaluation","operations"]
related: ["evaluation-and-test-sets","data-quality-and-provenance","model-serving-and-api-design"]
sources: ["https://www.nist.gov/itl/ai-risk-management-framework","https://scikit-learn.org/stable/modules/model_evaluation.html"]
status: draft
updated: 2026-10-14
---

# Model Monitoring and Drift

A deployed AI system can become less useful even when its code has not changed. Input distributions shift, sources become stale, user language evolves, providers update model versions, and workflows introduce new edge cases.

Input drift means requests differ from development data; concept drift means the relationship between inputs and desired outputs changes; retrieval drift means the index or corpus changes what evidence is found; behavior drift means outputs change after a model or prompt update; quality drift means error or correction rates worsen.

Track latency, errors, token counts, retrieval scores, no-result rates, citation support, escalation frequency, and user corrections while respecting privacy. Sample outputs for human review under access controls. Maintain a stable evaluation set and run it before and after model, prompt, and Dictionary updates.

A change in input statistics is a signal to investigate, not proof that quality declined. Conversely, unchanged statistics do not prove the system still performs well. Record model and source versions to connect regressions with deployments.

Do not automatically train on all user feedback: it can be noisy, malicious, unrepresentative, or sensitive. Review and label it under a documented process. Define rollback criteria and an incident owner before a release.

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://scikit-learn.org/stable/modules/model_evaluation.html

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://scikit-learn.org/stable/modules/model_evaluation.html
