# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`F0063_NEGATIVE_SLOPE_EXACT_DIRECT_SOLVE_TRANSIENT_ACCEPTED__MONOTONICITY_PRESERVING_HJB_RELAXATION_DESIGN_GATE_ACTIVE`

Results eligibility=`FALSE`。

## Latest accepted forensic

Accepted candidate:

`892b3ca9a40bb97b2390dedcab5d7bcd99ca0c21`

Acceptance:

`docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_EMERGENCE_FORENSIC_ACCEPTANCE_20260921.md`

The accepted checkpoint2→3 implicit direct solve exactly creates the first negative liquid finite-difference slopes.

This is not a serialization, finite-difference or linear-solve-accuracy defect.

## Scientific implication

The upstream numerical iteration law is now the unresolved object.

The current Owner-adopted law freezes full implicit updates at Delta=1000 and explicitly forbids damping, relaxation, adaptive Delta and line search.

Any monotonicity-preserving update safeguard therefore requires a new scientific/numerical design and later Owner adoption before implementation.

## Active task

`tasks/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_SCIENTIFIC_DESIGN_GATE_20260921.md`

This is zero-science design only.

It will test whether a global convex relaxation of the existing solved candidate can preserve strict positive raw liquid slopes while keeping the same fixed-point equations.

No production change, new linear solve or turn2 rerun is authorized.
