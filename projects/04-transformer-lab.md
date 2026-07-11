# Project 4 - Mini Transformer and Fine-Tuned LLM

## Question

How does a transformer learn and generate tokens, and what behavior changes after fine-tuning?

## Part A - Mini transformer

- Tokenizer or character vocabulary.
- Embeddings and positional information.
- Causal multi-head self-attention.
- Transformer blocks and language-model head.
- Training and generation scripts.

## Part B - Small-model fine-tuning

- Curated dataset with frozen train/eval split.
- Base-model evaluation.
- SFT with LoRA or equivalent parameter-efficient tuning.
- Post-training evaluation and model card.

## Experiments

- Context-length or model-size comparison.
- Decoding-strategy analysis.
- Data-quality ablation.
- Base vs. fine-tuned regressions by slice.

## Acceptance criteria

- Attention implementation has shape and masking tests.
- The training run records model/data revisions and configuration.
- Results include failure examples, not only successful generations.
- Explain the path from raw text to next-token distribution without notes.
