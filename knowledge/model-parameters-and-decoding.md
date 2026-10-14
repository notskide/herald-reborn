---
id: model-parameters-and-decoding
title: "Model Parameters and Decoding"
summary: "How learned weights differ from generation settings such as temperature, top-p, and output-token limits."
tags: ["parameters", "decoding", "inference", "generation"]
related: ["neural-networks", "transformers-and-attention", "tokenization-and-context-windows", "quantization-and-inference"]
sources: ["https://huggingface.co/docs/transformers/main/en/main_classes/text_generation", "https://arxiv.org/abs/1706.03762"]
status: draft
updated: 2026-10-14
---

# Model Parameters and Decoding

The word parameter can refer to two different things in language-model discussions. Model parameters are learned weights inside the network. Decoding parameters are settings that control how outputs are selected at inference time.

## Model weights

Training changes model weights to optimize an objective. These weights are part of the model artifact and are not normally changed by adjusting a request's temperature or token limit.

## Decoding settings

- **Temperature:** rescales token-selection probabilities. Lower values generally make selection more concentrated; higher values increase variation. It does not guarantee correctness.
- **Top-p sampling:** considers candidate tokens whose cumulative probability reaches a selected threshold, then samples within that group.
- **Maximum output tokens:** limits generation length; hitting the limit can cut off an answer.
- **Stop sequences:** can tell some runtimes to stop when a specified sequence appears.
- **Seed:** some runtimes allow a seed for repeatable sampling, but identical outputs are not guaranteed across hardware, runtime versions, or implementations.

Supported settings depend on the API and model provider. Keep defaults until there is an evaluation set, change one setting at a time, and measure answer quality as well as style. Low temperature cannot turn unsupported information into verified facts.

## Sources

- https://huggingface.co/docs/transformers/main/en/main_classes/text_generation
- https://arxiv.org/abs/1706.03762
