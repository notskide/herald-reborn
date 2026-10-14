---
id: encoder-decoder-and-sequence-models
title: "Encoder-Decoder and Sequence Models"
summary: "How sequence-to-sequence architectures transform an input sequence into an output sequence."
tags: ["architecture","transformers","sequence-models","translation"]
related: ["transformers-and-attention","tokenization-and-context-windows","ai-systems-and-models"]
sources: ["https://arxiv.org/abs/1409.0473","https://arxiv.org/abs/1706.03762"]
status: draft
updated: 2026-10-14
---

# Encoder-Decoder and Sequence Models

Sequence-to-sequence systems map an input sequence to an output sequence. Examples include translation, summarization, transcription, and structured transformation. An encoder processes the input into representations; a decoder generates output conditioned on those representations.

Earlier recurrent systems processed tokens sequentially while passing hidden state forward. Transformer-based encoder-decoder systems use attention and can process many input positions in parallel during encoding. A decoder usually applies causal masking during output generation to prevent access to future output tokens.

Encoder-only models are useful for classification and representation tasks; decoder-only models predict the next token and are common for dialogue; encoder-decoder models separate input processing from output generation. These are tendencies, not absolute rules. Data, objectives, parameters, context handling, and evaluation also matter.

For transforming a supplied document, an encoder-decoder model may be suitable. For open-ended continuation or dialogue, a decoder-only model may be convenient. Compare options on the actual workload, languages, input limits, latency, and deployment constraints. Architecture does not guarantee factual fidelity: evaluate which details are preserved, omitted, or invented.

## Sources

- https://arxiv.org/abs/1409.0473
- https://arxiv.org/abs/1706.03762

## Sources

- https://arxiv.org/abs/1409.0473
- https://arxiv.org/abs/1706.03762
