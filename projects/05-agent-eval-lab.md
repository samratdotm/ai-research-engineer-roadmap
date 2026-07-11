# Project 5 - Agent EvalLab

## Question

How can an agent capability be measured reliably enough to guide a release or training decision?

## Build

- Versioned task dataset covering normal, edge, adversarial, and OOD cases.
- Deterministic scorers for verifiable outcomes.
- Model-based grader with explicit rubric.
- Human-labeled calibration subset.
- Tool-trajectory and multi-turn metrics.
- Bootstrap confidence intervals and slice analysis.
- CLI, structured logs, and regression dashboard.

## Experiments

- Model judge vs. human agreement.
- Position/order bias.
- Rubric-change sensitivity.
- Prompt/scaffold ablation.
- Injected infrastructure failure vs. model regression.

## Acceptance criteria

- Research question and protocol are written before main runs.
- Judge limitations are measured.
- Invalid runs are quarantined.
- Each aggregate score links to inspectable examples or trajectories.
- A new contributor can reproduce the evaluation.
