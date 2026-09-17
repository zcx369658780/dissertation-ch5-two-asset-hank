# Task — V2 cell100 NO_ADMISSIBLE_POLICY zero-science attribution

Date: 2026-09-17

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID: `CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_20260917`

## Governance

This is a zero-science forensic task. Fresh-fetch live `origin/main`; read `AGENTS.md`, rule index, current status/handoff, the nonlinear continuation fail-closed acceptance, the Builder continuation report, the exact cell-100 receipt, frozen selector/D1/D3/Z/KKT authority, and only the persisted evidence needed for attribution.

Never enter or use `zcx369658780/deep-learning-hank`.

No scientific runtime is authorized.

## Frozen failing object

Accepted V2 field SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`

First failing V2 cell:

- flat F index `100`
- zero-based `(i_b,i_a,i_z)=(0,5,0)`
- physical `(b,a,z)=(-2.0,2.6315789473684212,0.8)`
- cell ID `v002_f0100_b000_a005_z000`
- `p_b_backward = p_b_forward = 0.012333311206716577`
- `p_a_backward = 0.00903315440190679`
- `p_a_forward = 0.008957007194295222`
- selector outcome `NO_ADMISSIBLE_POLICY`
- admissible comparisons `0`.

## Required attribution

Using only persisted receipts, static source inspection and algebraic reasoning:

1. Enumerate every candidate/active-set/derivative/transfer branch that the frozen selector actually considered at flat 100.
2. For every considered candidate, map each rejection reason to the exact frozen inequality/equality/KKT requirement and persisted raw value.
3. Reconstruct the lower-b state-constraint logic explicitly because `b=-2` is the lower liquid boundary.
4. Audit transfer negative/zero-kink/positive regimes and any active lower-b multiplier branch.
5. Audit whether interior-Z is legally applicable at this boundary cell; do not invent a Z branch if the frozen contract excludes it.
6. Inspect any `ROOT_FAILURE_NO_UNIQUE_BRACKET`: identify the exact frozen root equation, interval, endpoint signs/values if persisted, and whether failure means no legal root or only an implementation omission.
7. Prove whether all legal frozen branches were represented. Compare against accepted selector authority and prior boundary branches; do not infer completeness merely from implementation enumeration.
8. If useful, inspect persisted neighboring cells and the prior accepted V1 receipt for the same coordinate, but do not call selectors or recompute roots.
9. Identify the **minimal causal obstruction**: one or more mutually incompatible primal/KKT/direction conditions, omitted legal branch, or insufficient authority.

## Allowed classification

Return exactly one:

- `ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`
- `ATTRIBUTED__SELECTOR_OMITS_AUTHORITY_BACKED_LEGAL_BRANCH`
- `ATTRIBUTED__ROOT_IMPLEMENTATION_OMISSION_WITHIN_AUTHORIZED_BRANCH`
- `BLOCKED__OWNER_SCIENTIFIC_DECISION_REQUIRED`
- `BLOCKED__INSUFFICIENT_PERSISTED_EVIDENCE`

Do not repair or rerun.

## Zero-call ledger

All must remain exactly zero:

- selector evaluations
- scalar roots / Z roots
- policy maps
- D2 assemblies
- HJB solves/updates
- graph/SCC
- KFE/SVD/eigen/nullspace/`Q.T@p`
- MATLAB
- outer/firm/wage-return/GE/annual/shock/IRF/Results
- scientific retries.

Allowed operations are static source/evidence reads, hashing, text/JSON parsing and algebraic derivation only.

## Deliverable

Write:
`docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_REPORT.md`

Commit and ordinary non-force push a task branch. Do not merge main and do not publish a successor task.
