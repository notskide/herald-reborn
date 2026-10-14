---
id: neural-networks
title: "Neural Networks"
summary: "The building blocks of neural networks, including layers, activations, loss functions, gradients, and generalization."
tags: ["ai", "neural-networks", "training", "machine-learning"]
related: ["ai-systems-and-models", "transformers-and-attention", "model-parameters-and-decoding", "evaluation-and-test-sets"]
sources: ["https://www.deeplearningbook.org/", "https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html"]
status: draft
updated: 2026-10-14
---

# Neural Networks

A neural network is a parameterized function built from connected computational units. During training, an optimization procedure adjusts parameters to reduce a chosen loss on examples.

## Building blocks

- **Layer:** a stage that transforms a representation.
- **Weight and bias:** learned parameters used by a layer.
- **Activation function:** a nonlinear transformation that lets stacked layers represent more than a single linear mapping.
- **Loss function:** a numerical measure of how poorly predictions match a target or objective.
- **Gradient:** information about how a loss changes as parameters change.
- **Backpropagation:** an efficient way to compute gradients through a computational graph.
- **Optimizer:** a procedure that uses gradients to update parameters.
- **Generalization:** performance on examples not used to fit the model.

## Overfitting and underfitting

A model overfits when it learns accidental patterns in training data and performs poorly on new examples. It underfits when its capacity or training is insufficient to capture useful patterns. Validation data, regularization, suitable model capacity, and careful data selection help diagnose these problems.

Language models commonly learn statistical patterns in token sequences. Their outputs still need evaluation; low training loss alone does not prove factual accuracy or reliable reasoning.

## Sources

- https://www.deeplearningbook.org/
- https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
