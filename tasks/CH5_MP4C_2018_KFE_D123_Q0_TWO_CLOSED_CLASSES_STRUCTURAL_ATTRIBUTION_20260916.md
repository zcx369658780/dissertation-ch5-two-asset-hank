# CH5 MP4C 2018 KFE D1-D3 Q0 two closed communicating classes structural attribution

Date: 2026-09-16
Status: ACTIVE

## Objective

Attribute the two accepted closed communicating classes of Q0 to exact grid states, accepted policies and directed-flow basins. This is a structural diagnostic only. Do not change Q0 or any scientific law, and do not solve for stationary mass.

## Required startup authority

Read, in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_FAIL_CLOSED_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_RERUN_REPORT.md`
7. accepted Q0 artifact, manifest and all 800 accepted cell receipts
8. exact corrected generator / selector source needed only for interpretation of persisted receipts.

## Frozen object

Use the exact accepted Q0 only:

- SHA-256 `093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`
- CSR `(800,800)`
- state shape `(b,a,z)=(20,20,2)`
- F-order, b fastest
- exact-positive graph rule: off-diagonal `Q0[i,j] > 0` only; no edge tolerance.

The previously accepted SCC result is authority evidence: 400 SCCs of size 2, exactly two closed classes of size 2, 796 transient states. The task may recompute one SCC decomposition solely to recover/persist exact membership and condensation-graph attribution because the previous receipt did not persist node membership.

## Required outputs

Persist and explain all of the following:

1. Exact member flat indices, `(i_b,i_a,i_z)` coordinates and physical `(b,a,z)` values for both closed classes.
2. For each closed-class member, bind the corresponding accepted `cell_XXXX.json` receipt and report selected policy branch, active constraints, transfer branch, derivative branches, Z marker if any, `q_b,q_a,c,l,d,cost,g_b,g_a`, and all outgoing Q0 rates.
3. Determine whether each class has zero asset outgoing rates because both selected consumed asset drifts are exactly zero, or whether closure arises from another directed topology. Productivity switching within each size-2 class must be reported explicitly.
4. Build the SCC condensation DAG and, for every SCC, identify which closed class(es) are reachable. Report counts of states/SCCs in basin A only, basin B only, and states with paths to both classes. Do not convert this into probabilistic absorption weights.
5. Identify the first directed split/separatrix structure in asset-grid coordinates: report neighboring SCCs/cells whose downstream reachability differs, using exact graph connectivity only.
6. Compare the two recurrent asset coordinates with persisted Option-A selected policy types and with raw V0/V1 diagnostics where exact same coordinates exist. Do not run a V1 selector.
7. State whether the structural multiplicity is directly caused by accepted exact-zero Z/zero-kink policies, by state-constraint boundary behavior, by deterministic upwind asset drift producing multiple sink nodes, or whether causality remains unresolved.
8. Explain the scientific implication narrowly: Q0 invariant stationary mass is nonunique structurally. Do not label this as economic multiple equilibria or corrected HJB fixed-point multiplicity.

## Runtime ceilings

Allowed:

- accepted Q0 artifact load: <=1
- structural graph audit: <=1
- SCC decomposition: <=1
- condensation/reachability analysis: <=1
- accepted cell receipt reads: <=800

Forbidden / exactly zero:

- GESVD/SVD/eigendecomposition/nullspace solve
- normalized stationary mass construction
- `Q0.T @ p` KFE residual evaluation
- row replacement, pin, RHS/source injection
- iterative eigensolver
- selector evaluations, scalar roots, policy maps
- D2 reassembly, HJB solve, V1 remap
- MATLAB, outer, firm, wage-return, GE, annual, shock, IRF, Results
- retries, edge tolerance, graph repair, artificial diffusion.

## Fail closed

Stop if Q0/hash/order differs, previous two-class SCC result cannot be reproduced exactly, any membership cannot be bound to the accepted receipts, or any requested attribution would require modifying scientific code/Q0 or making a new economic law.

## Deliverable

Write:

`docs/CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_REPORT.md`

Allowed terminal classifications:

- `ATTRIBUTED__TWO_RECURRENT_CLASSES_FROM_EXACT_POLICY_FLOW_TOPOLOGY`
- `ATTRIBUTED__TWO_RECURRENT_CLASSES_FROM_EXACT_ZERO_ASSET_DRIFT_SINKS`
- `ATTRIBUTED__MIXED_POLICY_TOPOLOGY_MECHANISM`
- `BLOCKED__MEMBERSHIP_OR_CAUSAL_ATTRIBUTION_INSUFFICIENT`
- `BLOCKED__OTHER_AUTHORITY_CONFLICT`

Commit + non-force push task branch. Do not merge main. Do not publish successor task.
