---
id: ai-systems-and-models
title: "AI Systems and Models"
summary: "A practical map of AI, machine learning, training, inference, and the components around a deployed model."
tags: ["ai", "models", "machine-learning", "foundations"]
related: ["neural-networks", "transformers-and-attention", "learning-and-memory", "model-serving-and-api-design"]
sources: ["https://www.nist.gov/itl/ai-risk-management-framework", "https://developers.google.com/machine-learning/glossary"]
status: draft
updated: 2026-10-14
---

# AI Systems and Models

An AI system is more than a model. It may include the model, instructions, application code, data, external tools, storage, monitoring, and the people who operate it.

## Core terms

- **Artificial intelligence (AI):** a broad field concerned with systems that perform tasks associated with perception, language, prediction, planning, or decision support.
- **Machine learning (ML):** methods that infer patterns from data rather than relying only on rules written by a person.
- **Deep learning:** ML methods built around neural networks with multiple layers.
- **Model:** a learned or programmed function that maps inputs to outputs.
- **Parameters:** values inside a learned model adjusted during training.
- **Training:** optimizing a model using data and an objective.
- **Inference:** running a model to produce outputs for new inputs.
- **Application layer:** software that prepares prompts, retrieves knowledge, calls tools, checks results, and presents responses.

## Why the distinction matters

Adding a document to a knowledge repository changes what an application can retrieve. It does not automatically change model parameters. Fine-tuning can change parameters; retrieval-augmented generation supplies external information at request time. These approaches solve different problems.

A model name or API route is an identifier and interface, not evidence that trained weights exist. When describing an AI capability, state which component provides it, what data it uses, how it was evaluated, and what limitations remain.

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://developers.google.com/machine-learning/glossary
