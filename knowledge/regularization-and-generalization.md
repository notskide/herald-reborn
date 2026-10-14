---
id: regularization-and-generalization
title: "Regularization and Generalization"
summary: "Techniques and evaluation practices that reduce overfitting and help models perform on unseen examples."
tags: ["training","generalization","regularization","neural-networks"]
related: ["neural-networks","data-splitting-and-leakage","optimization-and-learning-rates"]
sources: ["https://www.deeplearningbook.org/","https://arxiv.org/abs/1607.06450"]
status: draft
updated: 2026-10-14
---

# Regularization and Generalization

Generalization is the ability to perform well on relevant unseen examples. Overfitting occurs when a model relies too heavily on patterns specific to training data, including noise or accidental correlations. Underfitting occurs when model capacity or training is insufficient to capture the useful structure.

Common techniques include weight decay, dropout, valid data augmentation, early stopping based on validation performance, and appropriate model selection. No technique works uniformly for every architecture or task. An augmentation must preserve the example's intended meaning and label; otherwise it adds noise rather than useful diversity.

Use validation data for tuning and preserve a separate test set for final assessment. Include slices for rare categories, languages, input lengths, and realistic deployment conditions. Track serious failure cases as well as average metrics. A model can improve overall accuracy while becoming worse for a consequential subgroup.

Regularization cannot compensate for an invalid objective, misleading labels, or unrepresentative data. Inspect task definitions and data quality before increasing model complexity or adding more training steps.

## Sources

- https://www.deeplearningbook.org/
- https://arxiv.org/abs/1607.06450

## Sources

- https://www.deeplearningbook.org/
- https://arxiv.org/abs/1607.06450
