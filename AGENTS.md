# Repository Governance Boundary

## Repository Identity

Repository:
`zcx369658780/dissertation-ch5-two-asset-hank`

Purpose:
Python reconstruction of the Dissertation Chapter 5 two-asset HA/HANK household model.

This repository is a model repository, not the governance repository.

## Authority Boundary

- GitHub main is the source of repository state.
- Tasks authorize bounded work.
- Scientific direction requires owner/reviewer approval.
- Do not infer authority from previous repositories or conversations.

## Repository Separation

This repository is independent from:

- `zcx369658780/dissertation-ch5-r5-python-model`
- `zcx369658780/deep-learning-hank`
- governance repositories

External materials may be used as evidence only.
They do not automatically authorize code migration.

## Scientific Boundary

Before implementation:

- freeze economic object;
- define state variables;
- define controls;
- define HJB/KFE formulation;
- establish parity criteria.

Engineering success does not imply economic model validity.

## Forbidden Without Explicit Task Authority

Do not:

- claim Results evidence;
- modify calibration for convenience;
- run full experiments without authorization;
- treat legacy output as numerical oracle without review;
- claim MATLAB/Python equivalence without parity evidence.

## Reconstruction Principle

The goal is an auditable two-asset HA/HANK reconstruction, not a line-by-line translation of legacy code.
