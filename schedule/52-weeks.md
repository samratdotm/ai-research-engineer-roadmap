# 52-Week Execution Plan

The **core** column fits the 10-hour commitment. Stretch work is optional.

| Week | Core focus | Required evidence | Optional stretch |
|---:|---|---|---|
| 1 | Vocabulary, lifecycle, baseline assessment | Diagnostic notebook, gap assessment, recorded explanation | Map an ADP agent request to the lifecycle |
| 2 | Vectors, matrices, shapes, broadcasting | NumPy shape exercises with tests | Visualize linear transformations |
| 3 | Dot products, matrix multiplication, norms, projections | Linear-regression forward pass | Least-squares derivation |
| 4 | Derivatives, gradients, chain rule | Finite-difference gradient checker | Tiny autodiff graph visualization |
| 5 | Probability, expectation, variance, sampling | Sampling simulation notebook | Bayes-rule simulation |
| 6 | Confidence intervals and gradient descent | Complete ML From Scratch report and phase interview | Implement momentum |
| 7 | Problem framing, targets, split design, baseline | Dataset card and frozen split | Add schema validation |
| 8 | Linear/logistic models and regularization | Baseline training pipeline | Implement regularization from scratch |
| 9 | Trees and ensembles | Model comparison with fixed protocol | Inspect feature importance pitfalls |
| 10 | Metrics, thresholds, imbalance | Metric/threshold decision memo | Cost-sensitive learning |
| 11 | Cross-validation, tuning, calibration | Calibrated model and reliability plot | Nested cross-validation |
| 12 | Leakage, shift, failure slices | ML Workbench report and phase interview | Synthetic shift experiment |
| 13 | PyTorch tensors, datasets, loaders, modules | End-to-end beginner training loop | Custom Dataset implementation |
| 14 | Forward pass, loss, autograd | Manual vs. PyTorch gradient comparison | Implement a custom autograd function |
| 15 | MLPs, activations, initialization | MLP experiment matrix | Initialization ablation |
| 16 | Optimizers and learning-rate schedules | SGD vs. Adam controlled comparison | Momentum visualization |
| 17 | Overfitting, dropout, weight decay | Deliberate overfit and mitigation report | Label-noise experiment |
| 18 | CNN or text classifier | Working model with baseline | Architecture comparison |
| 19 | Checkpoints, seeds, mixed precision | Reproducible multi-seed runs | Profile CPU/GPU pipeline |
| 20 | Debugging and consolidation | PyTorch Lab report and phase interview | Reproduce a small paper result |
| 21 | Tokenization and embeddings | Tokenizer analysis notebook | Compare tokenizers across languages |
| 22 | Attention with tensor shapes | Scaled dot-product attention implementation | Attention visualization |
| 23 | Causal masking and multi-head attention | Tested attention module | Efficient attention reading note |
| 24 | Transformer block and residual stream | Trainable decoder block | Pre-norm vs. post-norm comparison |
| 25 | Causal LM training | Mini transformer learns a corpus | Scaling-loss experiment |
| 26 | Decoding and sampling | Temperature/top-k/top-p comparison | Calibration analysis |
| 27 | SFT and LoRA on a small model | Base vs. tuned eval | Full fine-tune on a tiny model |
| 28 | Data quality, model card, limitations | Transformer project report and phase interview | Quantize and benchmark |
| 29 | Research questions, hypotheses, controls | Pre-registered Agent EvalLab plan | Critique an existing benchmark |
| 30 | Task datasets and deterministic graders | Versioned tasks and code graders | Difficulty calibration |
| 31 | LLM judges and rubric design | Human-labeled calibration subset | Pairwise vs. pointwise study |
| 32 | Agreement, bias, confidence intervals | Judge validation and bootstrap analysis | Position-bias experiment |
| 33 | Agent trajectories, tool-use metrics, OOD cases | Multi-turn/tool evaluation suite | Adversarial task generation |
| 34 | Regression and infrastructure failure diagnosis | Agent EvalLab release and phase interview | Contribute an Inspect eval |
| 35 | MDPs, returns, Bellman intuition | Tabular environment and value calculations | Bandit comparison |
| 36 | Q-learning and exploration | Trained Q-learning agent | Sensitivity to exploration schedule |
| 37 | Policy gradients and actor-critic intuition | Policy-gradient notebook | Variance-reduction comparison |
| 38 | PPO, KL control, trajectory inspection | PPO experiment | Reward/advantage visualization |
| 39 | SFT, reward modeling, DPO | Small preference-optimization comparison | Train a reward model |
| 40 | GRPO, verifiable rewards, reward hacking | Agent Inc. baselines and attack suite | Alternative reward design |
| 41 | Seeds, ablations, held-out/OOD evaluation | Agent Inc. research report and phase interview | Second model-size study |
| 42 | GPU and memory accounting, profiling | Memory/compute budget for one model | Kernel profiling note |
| 43 | DDP and distributed execution | Multi-process training/eval example | Run on two GPUs |
| 44 | FSDP/sharding and fault recovery | Scaling design memo and recovery test | Checkpoint-sharding experiment |
| 45 | vLLM serving, batching, KV cache, quantization | Serving benchmark | Quantization quality/perf tradeoff |
| 46 | Distributed eval orchestration and observability | Platform release and phase interview | Add autoscaling simulation |
| 47 | Select capstone question and pre-register study | Approved capstone proposal | External mentor review |
| 48 | Build baselines and freeze evaluation | Reproducible baseline results | Additional baseline |
| 49 | Run main experiments | Valid run set with lineage | Scale experiment |
| 50 | Ablations, OOD, failures, limitations | Analysis notebook and failure taxonomy | Reviewer-style critique |
| 51 | Report, demo, open-source contribution | Draft report and submitted contribution | Recorded technical talk |
| 52 | Resume, portfolio, full mock loop, retrospective | Public release and final readiness assessment | Application sprint |

## Monthly checkpoint

On the final Sunday of every month:

1. Update [tracking/progress.md](../tracking/progress.md).
2. Select five concepts at random from [tracking/concept-checklist.md](../tracking/concept-checklist.md) and explain them aloud.
3. Verify that every reported result has a reproducible command and stored configuration.
4. Remove low-value stretch tasks before adding new work.
