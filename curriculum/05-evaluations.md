# Phase 5 - Evaluations and Research Methodology

This phase is the center of the roadmap.

## Required concepts

- Operationalize vague capabilities into observable success criteria.
- Define the task distribution, edge cases, exclusions, and test-set policy.
- Use deterministic graders where possible; calibrate human or model graders where necessary.
- Measure grader agreement, position bias, verbosity bias, and sensitivity to rubric changes.
- Use seeds, repeated samples, confidence intervals, ablations, effect sizes, and error slices.
- Inspect transcripts and tool trajectories, not only scalar scores.
- Detect contamination, reward hacking, evaluator overfitting, and infrastructure-corrupted runs.

## Minimum valid experiment

1. Research question and falsifiable hypothesis.
2. Fixed dataset version and split.
3. Baseline and treatment.
4. Controlled configuration with recorded model revision.
5. Appropriate metric and uncertainty.
6. Failure analysis and representative examples.
7. Limitations and alternative explanations.
8. Reproduction command.

## Exit questions

- How would you validate an LLM judge?
- Why is a larger eval set not automatically a better eval?
- How can an eval harness create a fake regression?
- What is the difference between benchmark overfitting and training-data contamination?
