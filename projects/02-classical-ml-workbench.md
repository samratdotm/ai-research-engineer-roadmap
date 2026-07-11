# Project 2 - Reproducible ML Workbench

## Question

Which model and decision threshold best serve the real error costs of a public tabular problem?

## Build

- Dataset card and fixed split policy.
- Schema/data-quality checks.
- Preprocessing pipeline.
- Naive, linear, tree, and ensemble baselines.
- Cross-validation, tuning, calibration, and slice analysis.
- Reproducible CLI for training and evaluation.

## Experiments

- Metric/threshold tradeoff.
- Calibration before/after a calibration method.
- Artificial distribution-shift test.
- Leakage demonstration and correction.

## Acceptance criteria

- Test data is untouched until final evaluation.
- Pipeline prevents preprocessing leakage.
- Model choice is justified by evidence and operational costs.
- Model card reports limitations and unsafe uses.
