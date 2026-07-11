# Project 6 - Agent Inc. Research Edition

## Primary question

Does reinforcement post-training teach a small open model a general business-operation policy, or does it exploit the reward and training scenarios?

## Required baselines

- Base model with fixed scaffold.
- Improved prompting/scaffold without weight updates.
- SFT or behavior-cloning baseline.
- GRPO treatment.

## Required rigor

- At least three seeds where compute permits; otherwise repeated evaluation samples with an explicit limitation.
- Larger held-out set and explicit out-of-distribution scenarios.
- Confidence intervals and effect sizes.
- Ablation of reward components.
- Deterministic-only vs. hybrid-judge reward.
- Reward-hacking attack suite.
- Training/evaluation data audit.
- Cost, compute, and failure accounting.

## Acceptance criteria

- No result is selected because it looks best.
- Training and held-out curves are reported separately.
- Invalid infrastructure runs remain visible in quarantine logs.
- Six-to-eight-page report includes abstract, related work, methods, results, failures, limitations, and future work.
- One-command reproduction is provided for the affordable subset.
