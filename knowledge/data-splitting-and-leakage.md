---
id: data-splitting-and-leakage
title: "Data Splitting and Leakage"
summary: "How to separate training, validation, and test information so reported performance reflects generalization."
tags: ["training","evaluation","datasets","statistics"]
related: ["data-quality-and-provenance","evaluation-and-test-sets","learning-and-memory"]
sources: ["https://scikit-learn.org/stable/modules/cross_validation.html","https://developers.google.com/machine-learning/crash-course"]
status: draft
updated: 2026-10-14
---

# Data Splitting and Leakage

Training data updates model parameters. Validation data supports choices such as hyperparameters and thresholds. A held-out test set estimates performance after those choices are made. Repeatedly tuning against the test set turns it into validation data and can make the final score optimistic.

Leakage occurs when information unavailable in the intended use becomes visible during training or evaluation. Examples include near-duplicate records in separate partitions, related records from the same entity split across sets, future facts used to predict the past, labels encoded in metadata, or benchmark answers present in training examples.

Random splitting is not always appropriate. Time-sensitive data may need chronological splits; repeated entities may require group splits; source-based datasets may need source-level separation.

Decide the split strategy before training. Record partition IDs and deduplication rules. Fit learned preprocessing only on training data. For retrieval, test whether the relevant answer source is present and accessible, and create some test questions independently of indexed text.

A clean split does not guarantee a representative test set. Review coverage, label quality, and similarity to deployment conditions alongside leakage checks.

## Sources

- https://scikit-learn.org/stable/modules/cross_validation.html
- https://developers.google.com/machine-learning/crash-course

## Sources

- https://scikit-learn.org/stable/modules/cross_validation.html
- https://developers.google.com/machine-learning/crash-course
