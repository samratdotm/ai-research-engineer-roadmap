# Phase 4 - Transformers and LLMs

## Required concepts

- Text normalization, subword tokenization, vocabulary, token IDs, and attention masks.
- Embedding lookup, positional information, queries, keys, values, scaled dot-product attention, and causal masking.
- Multi-head attention, residual streams, normalization, MLP blocks, and logits.
- Next-token prediction, cross-entropy, teacher forcing, pre-training, SFT, and parameter-efficient tuning.
- Greedy decoding, beam search intuition, temperature, top-k, top-p, stop criteria, and sampling variance.
- Context limits, KV caches, batching, quantization, throughput, latency, and cost.
- Retrieval, tools, agents, and memory as surrounding systems, not properties magically learned by the base model.

## Required explanations

- Trace one sentence from raw text to output token.
- Explain attention with tensor shapes.
- Explain why fine-tuning can improve one distribution and degrade another.
- Explain why an eval set used repeatedly during development becomes part of the training process conceptually.

## Exit questions

- What does self-attention compute?
- Why is the square-root scaling term used?
- What is stored in a KV cache?
- What is the difference between LoRA, quantization, and prompt engineering?
