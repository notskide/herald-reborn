---
id: synthetic-data-and-augmentation
title: "Synthetic Data and Data Augmentation"
summary: "Generating or transforming examples to improve coverage while avoiding repeated errors and distorted evaluations."
tags: ["synthetic-data","datasets","training","evaluation"]
related: ["data-quality-and-provenance","evaluation-and-test-sets","neural-networks"]
sources: ["https://huggingface.co/docs/datasets/index","https://developers.google.com/machine-learning/resources/datasets"]
status: draft
updated: 2026-10-14
---

# Synthetic Data and Data Augmentation

Synthetic data is generated rather than directly observed from the target process. Data augmentation creates modified examples meant to preserve the original task label or meaning. Both can improve coverage when real examples are scarce, expensive, or sensitive—but only if the transformations preserve relevant properties.

Synthetic examples may cover rare scenarios, formats, or controlled edge cases. Augmentation can include constrained paraphrases, valid edits, image transformations, or variations in noise and layout.

Risks include copying the teacher model's errors and biases, producing repetitive low-diversity examples, changing labels accidentally, and contaminating evaluation sets with examples too similar to the generation method.

Record whether each example is observed, human-authored, generated, or transformed. Preserve the original example and transformation procedure where permitted. Review samples, test label preservation, deduplicate, and evaluate on independently collected data. Keep training, validation, and test data separated appropriately. Never describe generated examples as real observations.

For a knowledge Dictionary, model-generated prose should not be used as its own factual evidence. Verify factual claims against sources and keep provenance visible.

## Sources

- https://huggingface.co/docs/datasets/index
- https://developers.google.com/machine-learning/resources/datasets

## Sources

- https://huggingface.co/docs/datasets/index
- https://developers.google.com/machine-learning/resources/datasets
