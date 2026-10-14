---
id: transformers-and-attention
title: "Transformers and Attention"
summary: "How transformer models use attention and position information to process token sequences."
tags: ["transformers", "attention", "language-models", "architecture"]
related: ["neural-networks", "tokenization-and-context-windows", "embeddings-and-semantic-similarity", "model-parameters-and-decoding"]
sources: ["https://arxiv.org/abs/1706.03762", "https://huggingface.co/docs/transformers/index"]
status: draft
updated: 2026-10-14
---

# Transformers and Attention

The Transformer is a neural-network architecture introduced for sequence processing. It uses attention mechanisms to combine information from different positions, allowing training computations to be more parallelizable than architectures that process each token strictly one after another.

## Attention, in plain language

For each position, an attention operation computes how much information to take from other positions. Queries, keys, and values are learned projections; similarity between queries and keys determines weights used to combine values. Multi-head attention performs several learned attention operations in parallel.

Position information is also needed because attention alone does not tell a model the original order of tokens. Implementations may use positional embeddings, rotary position encodings, or other position-aware methods.

## Common model shapes

- **Encoder-only:** builds contextual representations and is often used for classification or representation tasks.
- **Decoder-only:** predicts subsequent tokens and is widely used for generative language models.
- **Encoder-decoder:** encodes one sequence and generates another, a common design for translation and text transformation.

Attention does not guarantee that every relevant fact receives the right weight. Results depend on training, data, architecture, context length, and inference configuration.

## Sources

- https://arxiv.org/abs/1706.03762
- https://huggingface.co/docs/transformers/index
