# Phase 2 - Classical Machine Learning

## Learning order

1. Problem framing and target definition.
2. Data inspection and split strategy.
3. Simple baseline.
4. Linear and tree models.
5. Metrics and threshold selection.
6. Cross-validation and tuning.
7. Error slices, calibration, and shift.
8. Reproducible report.

## Required concepts

- Linear/logistic regression, regularization, decision trees, random forests, and gradient boosting.
- K-nearest neighbors, clustering, PCA, and when not to use them.
- Numerical/categorical preprocessing, missing data, class imbalance, and feature leakage.
- Accuracy, precision, recall, specificity, F1, ROC-AUC, PR-AUC, log loss, Brier score, and calibration.
- Cross-validation, hyperparameter search, early stopping, and nested evaluation intuition.

## Research habits introduced

- State a hypothesis before running a model.
- Fix the test split before tuning.
- Compare to a naive baseline.
- Track dataset version and random seed.
- Inspect examples behind every aggregate metric.

## Exit questions

- When is accuracy misleading?
- Why can ROC-AUC look good on a severely imbalanced problem?
- How can preprocessing leak test information?
- How would you detect a model that is accurate but poorly calibrated?
