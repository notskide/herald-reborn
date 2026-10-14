---
id: edge-and-low-resource-inference
title: "Edge and Low-Resource Inference"
summary: "Design choices for running AI with limited RAM, CPU, storage, power, or network availability."
tags: ["edge-ai","inference","memory","quantization"]
related: ["quantization-and-inference","model-serving-and-api-design","model-parameters-and-decoding"]
sources: ["https://huggingface.co/docs/transformers/quantization/bitsandbytes","https://pytorch.org/tutorials/"]
status: draft
updated: 2026-10-14
---

# Edge and Low-Resource Inference

Low-resource inference runs a model under strict memory, compute, power, or storage limits. The goal is not simply the smallest model; it is the smallest reliable system that completes its task within acceptable latency.

Memory includes model weights, temporary activations, attention key/value cache, tokenizer and runtime data, loaded documents, request buffers, and the application. Parallel requests and long contexts increase peak usage. Quantization reduces some weight-memory requirements but does not remove runtime overhead.

Reduce footprint by choosing a compact model for the target task, using supported quantization, limiting input and output length, keeping only relevant conversation history, bounding concurrency, and avoiding dependencies that do not serve the request path. Measure peak resident memory with the API and retrieval running together.

CPU-only inference may work for tiny models and low traffic, but speed depends on processor, quantization kernel, context length, and runtime. A model file fitting on disk does not prove the model fits in RAM or runs fast enough.

For Herald, benchmark retrieval alone, then the chosen model, then both under realistic traffic. This reveals whether the limiting factor is application code, model weights, context cache, or concurrency.

## Sources

- https://huggingface.co/docs/transformers/quantization/bitsandbytes
- https://pytorch.org/tutorials/

## Sources

- https://huggingface.co/docs/transformers/quantization/bitsandbytes
- https://pytorch.org/tutorials/
