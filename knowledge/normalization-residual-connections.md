---
id: normalization-residual-connections
title: "Normalization and Residual Connections"
summary: "Transformer components that can stabilize optimization and help information and gradients pass through deep networks."
tags: ["transformers","architecture","training","neural-networks"]
related: ["transformers-and-attention","neural-networks","optimization-and-learning-rates"]
sources: ["https://arxiv.org/abs/1706.03762","https://arxiv.org/abs/1512.03385"]
status: draft
updated: 2026-10-14
---

# Normalization and Residual Connections

Deep networks pass signals and gradients through many layers. Normalization and residual connections are architectural tools that can help stabilize and improve training, although their exact behavior depends on placement and model design.

Layer normalization rescales and shifts a representation using statistics across features for each example. It can make optimization less sensitive to some activation-scale changes. Transformer variants differ in whether normalization is applied before or after a sublayer and in the exact normalization operation.

A residual connection adds a sublayer's transformed signal to its input, creating a path for information and gradients to flow across the network. Instead of learning an entirely new representation at each layer, a block can learn a change to the current representation. Transformer blocks commonly apply residual paths around attention and feed-forward components.

Pre-normalization and post-normalization can differ in training stability. Epsilon values, initialization, precision, dropout, and architecture variant also matter. Implementations should match the configuration associated with pretrained weights rather than mixing components casually.

These mechanisms do not guarantee generalization, factual accuracy, or safe output. Evaluate architecture alongside data, objectives, training, and downstream behavior.

## Sources

- https://arxiv.org/abs/1706.03762
- https://arxiv.org/abs/1512.03385

## Sources

- https://arxiv.org/abs/1706.03762
- https://arxiv.org/abs/1512.03385
