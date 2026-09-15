# Freeze — J160 cross-state finalizer common-support repair

Date: 2026-09-15

## Purpose

Close the post-science finalization blocker from the bounded J160 cross-state confirmation **without rerunning science**.

## Frozen science

No scientific input, model equation, solver, parameter, grid, or previously completed science call may change.

The completed raw execution to be finalized is expected at:

`D:\ProjectTemp\ch5-mp4c-k1-j160-cross-state-evidence-20260915-001`

with the Builder worktree context at:

`D:\ProjectTemp\ch5-mp4c-k1-j160-bounded-cross-state-confirmation-20260915-001`

The successor must independently verify raw evidence integrity before trusting it.

## Zero-science-runtime rule

Authorized new science calls:

- HJB=0
- KFE=0
- J20 rerun=0
- J160 rerun=0
- J320/J640/J1280=0
- global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0

Scientific retries=0.

## Common-support CDF repair

The accepted same-support marginal distance is based on cumulative node mass, deterministic piecewise-linear CDF interpolation, and integral absolute CDF difference divided by common support width.

The repair must preserve that behavior exactly when supports are identical.

For different supports only, define comparison on the union interval:

`[min(x_old.min,x_new.min), max(x_old.max,x_new.max)]`.

For each raw signed marginal separately:

- below its minimum support, CDF=0;
- at/within its own support, use the existing cumulative-node-mass / piecewise-linear interpolation convention;
- above its maximum support, CDF=its raw total marginal mass;
- do not clip negative node mass;
- do not renormalize scientific mass to force total=1;
- do not smooth or rebin scientific marginals.

Integrate absolute CDF difference over the union interval and divide by union-support width.

This metric must be labeled:

`DOMAIN_PLUS_GRID_CDF_DISTANCE`

for J20→J160 comparisons because both domain and discretization change. It must not be described as a pure precision metric.

## Regression requirement

Focused tests must prove that for same-support fixtures the repaired function reproduces the prior accepted distance exactly (up to deterministic floating representation), and that different-support fixtures produce finite deterministic results with the exterior-extension rule above.

## Raw evidence integrity gate

Before finalization, verify at minimum:

- evidence path exists;
- any raw manifest/seal present validates;
- exactly four new authorized J160 HJB calls are represented;
- exactly four corresponding KFE completions are represented;
- scientific retries=0;
- center J160 and all J20 references were reuse-only;
- frozen `(ra,w)` corner set is exact;
- frozen `rb=.02, a=[0,100], b=[-2,20], I=20, J=160, h=1, Nz=2` is exact;
- no forbidden runtime appears.

If this gate fails, stop with an evidence-integrity blocker and do not fabricate compact evidence.

## Finalization authority

If integrity and repair tests pass, the task may generate:

- the formal J160 bounded cross-state confirmation report;
- compact evidence;
- sealed manifest;
- truthful CURRENT closeout docs;
- one coherent Builder candidate commit.

No successor task may be published by Builder.

Results eligibility remains `FALSE`.
