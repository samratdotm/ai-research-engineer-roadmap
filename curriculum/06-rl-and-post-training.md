# Phase 6 - RL and Post-Training

## Learning sequence

1. Multi-armed bandits and exploration/exploitation intuition.
2. Markov decision processes, returns, value functions, and Bellman equations.
3. Tabular Q-learning.
4. Policy gradients and actor-critic intuition.
5. PPO and KL constraints.
6. SFT and preference datasets.
7. Reward modeling, RLHF/RLAIF, DPO, and GRPO.
8. Agent environments, tool trajectories, verifiable rewards, and reward hacking.

## Required distinctions

- Online vs. offline and on-policy vs. off-policy.
- Behavior cloning/SFT vs. preference optimization vs. reinforcement learning.
- Outcome reward vs. process reward.
- Reward signal vs. ground-truth answer.
- Training reward vs. held-out capability evaluation.

## Exit questions

- Why does on-policy training need trajectories from the current policy?
- Why can a rising training reward coincide with worse real behavior?
- What problem does KL regularization address?
- When would DPO be more appropriate than GRPO?
