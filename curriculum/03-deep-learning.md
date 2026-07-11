# Phase 3 - Deep Learning and PyTorch

## Required concepts

- Tensor shape discipline, batching, datasets, data loaders, devices, dtypes, and reproducibility.
- Linear layers, activations, compositions, logits, softmax, and cross-entropy.
- Forward pass, computational graph, reverse-mode automatic differentiation, and optimizer step.
- Initialization, normalization, dropout, weight decay, gradient clipping, and schedules.
- CNN building blocks and enough sequence modeling history to understand why transformers mattered.
- Checkpoints, mixed precision, gradient accumulation, and memory/performance tradeoffs.

## Debugging ladder

1. Can the model overfit a single batch?
2. Are input, label, and output shapes correct?
3. Is the loss appropriate for the output representation?
4. Are gradients present and finite?
5. Is the learning rate plausible?
6. Is the data pipeline correct?
7. Does a simple baseline work?
8. Only then increase model complexity.

## Exit questions

- What exactly happens during `loss.backward()`?
- Why do training and validation loss diverge?
- What changes between `model.train()` and `model.eval()`?
- When should gradient accumulation or mixed precision be used?
