---
id: calibration-and-confidence
title: "Calibration and Confidence"
summary: "The difference between a model's expressed confidence and the measured reliability of its predictions."
tags: ["uncertainty","evaluation","probability","reliability"]
related: ["uncertainty-and-conflicting-evidence","hallucinations-and-grounding","evaluation-and-test-sets"]
sources: ["https://scikit-learn.org/stable/modules/calibration.html","https://www.nist.gov/itl/ai-risk-management-framework"]
status: draft
updated: 2026-10-14
---

# Calibration and Confidence

A predictor is calibrated when stated probabilities correspond reasonably well to observed frequencies over a suitable evaluation population. For example, among predictions assigned confidence near 0.8, roughly 80% should be correct under the measurement setup. This is a population-level property, not a guarantee for one case.

Language models can use confident wording without having a calibrated probability that a complete factual answer is true. Token probabilities measure aspects of next-token prediction; they are not automatically a probability of factual correctness.

## How to evaluate

For classifiers, reliability diagrams compare predicted probabilities with observed outcomes. Brier score and log loss assess probabilistic predictions, but should be interpreted alongside task-specific error costs. Calibration methods must be fitted on appropriate data separate from the model's training examples.

For retrieval-grounded assistants, evaluate retrieval relevance, source quality, claim support, contradiction handling, and abstention separately. Good retrieval does not prove that the generated response used the evidence correctly.

Do not invent numeric confidence percentages for generated prose unless a validated method supports them. Prefer meaningful statements such as “the sources agree,” “evidence is limited,” or “I could not verify this.” Re-check behavior after model, prompt, corpus, or user-population changes.

## Sources

- https://scikit-learn.org/stable/modules/calibration.html
- https://www.nist.gov/itl/ai-risk-management-framework

## Sources

- https://scikit-learn.org/stable/modules/calibration.html
- https://www.nist.gov/itl/ai-risk-management-framework
