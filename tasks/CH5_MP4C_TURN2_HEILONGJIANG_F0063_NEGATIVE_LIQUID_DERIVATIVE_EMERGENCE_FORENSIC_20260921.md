# Task — turn-2 黑龙江 F0063 negative liquid-derivative emergence zero-science forensic

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_LIQUID_DERIVATIVE_EMERGENCE_FORENSIC_20260921`

Status: `ACTIVE`

Results eligibility: `FALSE`

## Roles and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer / scientific-route authority. Codex is bounded Builder / scientific numerical analyst. GitHub live main is repository-state authority.

Absolutely do not enter, read, search, use or modify:

`zcx369658780/deep-learning-hank`.

## Required reads

Fresh-fetch live main, then read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_ACCEPTANCE_20260921.md`
6. `docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NONPOSITIVE_BACKWARD_LIQUID_SHADOW_FORENSIC_ACCEPTANCE_20260921.md`
7. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`
8. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`
9. current `option_a_step.py` derivative construction, nonlinear continuation and turn2 integration source, read-only
10. this exact task.

## Purpose

This is a zero-science attribution task.

The current selector law is not under review. The one-sided extrapolation design has been scientifically rejected.

Determine **when, where and by what accepted numerical transition** the first nonpositive liquid derivative appears in the 黑龙江 turn-2 HJB iterate.

The task must distinguish:

1. already present in the source-native initialization;
2. introduced before checkpoint 1;
3. introduced by a later accepted direct solve/update;
4. floating-point / serialization artifact;
5. exact transient non-monotonicity of the persisted value iterate;
6. evidence insufficient to attribute further.

Do not redesign or repair the iteration.

## Accepted evidence root

Use only accepted run004 evidence:

`reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921/`

Target province:

`household/p07_黑龙江/`

Available accepted objects include:

- `native_initialization_arrays.npz`
- checkpoints 000, 001, 002 complete map/update artifacts
- checkpoint 003 persisted failed-map prefix and derivative receipt
- checkpoint 000/001/002 `checkpoint_arrays.npz`
- checkpoint 000/001/002 `direct_update_arrays.npz`
- checkpoint 000/001/002 direct-solve receipts
- checkpoint 003 cell JSON through flat 63.

## Exact derivative law to reconstruct independently

The current source defines raw liquid finite differences on the 20-point b grid:

`p_b^F[i]=(V[i+1]-V[i])/(b[i+1]-b[i])`

`p_b^B[i]=(V[i]-V[i-1])/(b[i]-b[i-1])`

with the existing boundary duplicate-carrier convention.

For this forensic only, independent arithmetic reconstruction of raw derivatives from **persisted V arrays** is explicitly authorized.

This authorization is diagnostic only. Do not import or call the production derivative helper.

## Required analysis

### A. Artifact and identity chain

Bind:

- native initialization V identity;
- checkpoint 0/1/2 V identities;
- direct-update next-value identities 0->1, 1->2, 2->3;
- checkpoint3 derivative receipt V identity;
- exact grid identity and F-order shape.

Prove the checkpoint-to-checkpoint SHA chain.

### B. Full 黑龙江 derivative census by iterate

Independently reconstruct raw p_b backward/forward arrays from persisted V at:

- native initialization / checkpoint0;
- checkpoint1;
- checkpoint2;
- checkpoint3 next-value state.

For each iterate, report separately for:

- interior b cells;
- lower-b boundary;
- upper-b boundary.

Count sign patterns:

- (+,+)
- (<=0,+)
- (+,<=0)
- (<=0,<=0)

Also report:

- minimum p_b^B and location;
- minimum p_b^F and location;
- first F-order flat with any nonpositive liquid derivative;
- count and maximum magnitude of negative derivatives.

For checkpoint3, require exact parity at persisted F0062/F0063 values.

### C. Local trajectory around F0062/F0063

For flats 62 and 63 and the directly relevant neighboring b-grid points, persist at each iterate:

- V levels used by the finite difference;
- p_b^B and p_b^F;
- selected-policy identity if available at completed checkpoints;
- g_b and q_b from selected policy if available;
- whether the derivative sign changed from the previous iterate.

Identify the exact update at which each mixed-sign pattern first appears.

### D. Direct-solve attribution

For update 2->3, inspect only persisted artifacts:

- checkpoint2 `checkpoint_arrays.npz`;
- checkpoint2 `q_generator.npz`;
- checkpoint2 `selected_policy_arrays.npz`;
- checkpoint2 `direct_update_arrays.npz`;
- checkpoint2 direct-solve receipt.

Verify independently:

1. persisted direct-update `next_value` identity equals checkpoint3 V identity;
2. the direct-solve residual/backward-error evidence is consistent with the persisted arrays;
3. the negative finite difference at F0063 follows directly from exact neighboring entries in that persisted `next_value`.

If feasible without model calls, reconstruct the two local sparse-system rows affecting the neighboring V entries and decompose the persisted matrix/rhs equality.

Do not call `spsolve` or solve a new linear system.

The goal is to distinguish a correct linear solve that creates a transient non-monotone iterate from a corrupted/incorrectly serialized solve.

### E. Earlier-update comparison

Perform the same local finite-difference before/after comparison for:

- native/checkpoint0 -> checkpoint1;
- checkpoint1 -> checkpoint2;
- checkpoint2 -> checkpoint3.

Determine whether the negative slope emerges gradually or appears discontinuously in the final accepted update.

### F. Scientific classification

End with exactly one:

#### 1. Exact direct-solve transient confirmed

`PASS__TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_FORENSIC__EXACT_DIRECT_SOLVE_TRANSIENT_NONMONOTONICITY_CONFIRMED__NO_CODE_CHANGE`

Use only if persisted identities and arithmetic prove the accepted direct solve exactly creates the negative derivative, with no evidence of serialization/arithmetic corruption.

#### 2. Nonpositive derivative predates the final update

`PASS__TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_FORENSIC__NONPOSITIVE_DERIVATIVE_PREEXISTED_FINAL_UPDATE__NO_CODE_CHANGE`

#### 3. Evidence/identity inconsistency

`BLOCKED__TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_FORENSIC__PERSISTED_EVIDENCE_OR_IDENTITY_INCONSISTENT`

#### 4. Attribution remains unresolved

`BLOCKED__TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_FORENSIC__NUMERICAL_ATTRIBUTION_UNRESOLVED__NO_CODE_CHANGE`

## Zero-science boundary

Allowed diagnostic arithmetic:

- loading persisted NPZ/JSON;
- independent finite differences from persisted V;
- SHA/hash verification;
- sparse matrix-row multiplication using persisted matrix arrays;
- residual recomputation using persisted matrix/rhs/next_value;
- scalar summaries.

Forbidden:

- production derivative helper calls;
- production selector calls;
- production root-helper calls;
- HJB/direct update execution;
- `spsolve` or any new linear solve;
- D2/Q reconstruction from policies;
- KFE/SVD;
- aggregate/integration;
- turn2 replay/rerun;
- turn3;
- MATLAB;
- tuning/retry;
- any production source change.

Scientific/model calls must remain zero.

## No scientific repair

Do not modify:

`src/ch5_two_asset_hank/**`

Do not change Delta, initialization, convergence law, matrix equation, derivative law or damping.

Do not propose an implementation fix inside this task.

If the forensic shows exact transient non-monotonicity, stop and return evidence. Any decision to alter the HJB numerical iteration is a later scientific-design question.

## Allowed paths

Validator:

`validators/multi_province/turn2_heilongjiang_f0063_negative_derivative_emergence_forensic/**`

Optional test:

`tests/test_mp4c_turn2_heilongjiang_f0063_negative_derivative_emergence_forensic.py`

Fresh evidence:

`reports/ch5_mp4c_turn2_heilongjiang_f0063_negative_derivative_emergence_forensic_20260921_run001/`

Report:

`docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_EMERGENCE_FORENSIC_REPORT.md`

Do not modify CURRENT.

Do not publish a successor task.

## Required evidence

Persist at minimum:

- authority/source binding;
- accepted artifact SHA chain;
- reconstructed derivative parity receipt;
- four-iterate sign census;
- F0062/F0063 local V/derivative trajectory;
- direct-update identity receipt;
- local sparse-row/residual attribution if feasible;
- numerical-artifact vs exact-transient classification;
- zero-science ledger;
- focused tests;
- sealed manifest/readback;
- report.

Commit + ordinary non-force push, then STOP.
