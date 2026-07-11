# 52-Week Roadmap

This roadmap uses a spiral: first understand a mechanism, then implement it, then measure it, then revisit it at model and systems scale.

## Phase 0 - Orientation and baseline

**Week 1 | July 13-19, 2026**

Learn the vocabulary connecting the systems already used at work to the underlying ML lifecycle: data, parameters, loss, optimization, training, inference, evaluation, deployment, and monitoring.

### Outcomes

- Explain AI vs. ML vs. deep learning vs. generative AI.
- Distinguish model training from prompt/application engineering.
- Trace data through training and inference lifecycles.
- Complete the initial concept and interview baseline.

### Artifact

Diagnostic notebook, two-page gap assessment, and a ten-minute recorded explanation.

---

## Phase 1 - Math, probability, statistics, and NumPy

**Weeks 2-6 | July 20-August 23, 2026**

### Concepts

- Vectors, matrices, shapes, broadcasting, matrix multiplication, dot products, norms, and projections.
- Functions, derivatives, partial derivatives, gradients, chain rule, and computational graphs.
- Random variables, distributions, expectation, variance, covariance, conditional probability, and Bayes' rule.
- Sampling, estimators, uncertainty, confidence intervals, and hypothesis tests.
- Loss functions, gradient descent, learning rates, and numerical stability.

### Outcomes

- Derive and implement linear and logistic regression.
- Explain what a gradient represents geometrically and computationally.
- Quantify uncertainty rather than treating one number as truth.
- Perform numerical gradient checks.

### Project

[ML From Scratch](projects/01-ml-from-scratch.md)

---

## Phase 2 - Classical machine learning and data

**Weeks 7-12 | August 24-October 4, 2026**

### Concepts

- Regression, classification, trees, ensembles, clustering, PCA, and feature engineering.
- Train/validation/test splits, cross-validation, overfitting, regularization, and hyperparameter selection.
- Data leakage, imbalance, missing values, distribution shift, and reproducible preprocessing.
- Accuracy, precision, recall, F1, ROC-AUC, PR-AUC, ranking metrics, and calibration.
- Baselines, error slices, and practical vs. statistical significance.

### Outcomes

- Match a metric to the real cost of errors.
- Identify leakage and invalid experimental comparisons.
- Build a reproducible data-to-model pipeline.
- Explain why a more complex model is not automatically better.

### Project

[Reproducible ML Workbench](projects/02-classical-ml-workbench.md)

---

## Phase 3 - Deep learning and PyTorch

**Weeks 13-20 | October 5-November 29, 2026**

### Concepts

- Tensors, modules, datasets, data loaders, forward pass, backpropagation, and autograd.
- Activations, initialization, loss functions, SGD, momentum, Adam, and learning-rate schedules.
- Batch normalization, dropout, regularization, checkpointing, gradient clipping, and mixed precision.
- CNNs and sequence modeling as examples of representation learning.
- Debugging exploding gradients, dead activations, overfitting, underfitting, and data problems.

### Outcomes

- Write and debug a complete PyTorch training loop.
- Interpret loss and metric curves.
- Reproduce runs with seeds and saved configurations.
- Diagnose whether the problem is code, data, optimization, or model capacity.

### Project

[PyTorch Training Laboratory](projects/03-pytorch-training-lab.md)

---

## Phase 4 - Transformers and LLM training

**Weeks 21-28 | November 30, 2026-January 24, 2027**

### Concepts

- Tokenization, embeddings, positional information, attention, masking, residual connections, and normalization.
- Encoder, decoder, and encoder-decoder architectures.
- Causal language-model loss, pre-training, instruction tuning, and parameter-efficient fine-tuning.
- Decoding, temperature, top-k, top-p, repetition, and calibration.
- Context windows, KV cache, batching, quantization, latency, throughput, and cost.
- Data curation, deduplication, contamination, and model cards.

### Outcomes

- Implement a small decoder-only transformer.
- Fine-tune a small open model using a correct data split.
- Compare base and fine-tuned behavior with more than one metric.
- Explain the complete path from raw text to generated token.

### Project

[Mini Transformer and Fine-Tuned LLM](projects/04-transformer-lab.md)

---

## Phase 5 - Evaluations and research methodology

**Weeks 29-34 | January 25-March 7, 2027**

### Concepts

- Research questions, hypotheses, variables, controls, baselines, confounders, and experiment validity.
- Task construction, coverage, difficulty, contamination, edge cases, and out-of-distribution testing.
- Deterministic, human, and model-based grading.
- Judge calibration, agreement, position bias, verbosity bias, and rubric design.
- Multiple seeds, bootstrap confidence intervals, ablations, power, effect sizes, and error taxonomies.
- Agent trajectory evaluation, tool-use correctness, reward hacking, and regression detection.

### Outcomes

- Turn an ambiguous capability into measurable tasks.
- Validate a grader rather than assuming it is correct.
- Distinguish model regression from harness or infrastructure failure.
- Write a defensible experimental conclusion with limitations.

### Project

[Agent EvalLab](projects/05-agent-eval-lab.md)

---

## Phase 6 - Reinforcement learning, alignment, and post-training

**Weeks 35-41 | March 8-April 25, 2027**

### Concepts

- Markov decision processes, states, actions, rewards, policies, trajectories, returns, and discounting.
- Value functions, Q-learning, temporal-difference learning, policy gradients, actor-critic, and PPO.
- SFT, reward models, RLHF, RLAIF, DPO, GRPO, KL control, and on-policy vs. off-policy learning.
- Reward shaping, sparse rewards, reward variance, credit assignment, and reward hacking.
- Training/evaluation isolation, reproducibility, checkpoint selection, and post-training data pipelines.

### Outcomes

- Explain where SFT, preference optimization, and online RL differ.
- Implement one small classical RL agent and one LLM post-training workflow.
- Inspect trajectories and reward distributions, not only mean reward.
- Defend whether an observed gain generalized.

### Project

[Agent Inc. Research Edition](projects/06-agent-inc-research.md)

---

## Phase 7 - ML systems and distributed execution

**Weeks 42-46 | April 26-May 30, 2027**

### Concepts

- GPU memory, compute, bandwidth, kernels, profiling, and arithmetic intensity at an intuitive level.
- Data parallelism, DDP, sharding/FSDP, tensor parallelism, and pipeline parallelism.
- Fault recovery, checkpointing, job orchestration, data lineage, and experiment tracking.
- Model serving, continuous batching, KV-cache management, quantization, and autoscaling.
- Throughput vs. latency, p50/p95/p99, utilization, cost, and reliability.

### Outcomes

- Choose an appropriate scaling strategy.
- Benchmark serving without making invalid comparisons.
- Build resilient distributed evaluation execution.
- Diagnose model, data, infrastructure, and provider failures separately.

### Project

[Distributed Eval and Serving Platform](projects/07-distributed-eval-platform.md)

---

## Phase 8 - Research Engineer capstone and interviews

**Weeks 47-52 | May 31-July 11, 2027**

### Work

- Complete one polished capstone with a reproducible public release.
- Submit at least one meaningful contribution to an established evaluation, post-training, or ML-systems project.
- Publish two technical articles and one six-to-eight-page research-style report.
- Rewrite resume and portfolio around evidence, not tool names.
- Practice Python coding, ML fundamentals, experiment design, system design, and project deep dives.

### Exit outcomes

- Interview-ready for Applied AI, AI Evals, Research Tools, RL Environment, and AI Reliability roles.
- Credible for Research Engineer roles in model evaluations and agent environments.
- A clear gap assessment for post-training roles that require larger-scale model-training experience.

### Project

[Research Engineer Capstone](projects/08-capstone.md)
