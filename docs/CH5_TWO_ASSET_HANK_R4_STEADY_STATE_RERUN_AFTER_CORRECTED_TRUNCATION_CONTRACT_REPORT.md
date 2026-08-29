# CH5 Two-Asset HANK R4 Steady-State Rerun After Corrected Truncation Contract

## Verdict

`PASS`

Acceptance level:

`R4_FROZEN_STEADY_STATE_FULL_RUN_PASSED_UNDER_CORRECTED_TRUNCATION_CONTRACT__INDEPENDENT_ACCEPTANCE_PENDING`

The frozen fixture `R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1` was invoked exactly once through `run_frozen_r4_steady_state()`. The call returned successfully and reached every authorized R4 steady-state gate. No retry, repair, tuning, or supplemental numerical diagnostic was performed.

## Authority and identity

- Live/base `origin/main`: `a4e5f7c175a8106852aba804fb8374370dd91fce`
- Accepted implementation baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- Isolated execution workspace: `D:\ProjectTemp\ch5-r4-steady-state-rerun-corrected-contract-20260829`
- Source checkout used only as the repository from which live GitHub authority was fetched: `D:\ResearchCode\dissertation-ch5-two-asset-hank`

Before Python execution, `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..a4e5f7c175a8106852aba804fb8374370dd91fce -- src tests` was empty. All relevant scientific and test blobs were therefore byte-identical to the accepted implementation baseline; later differences were governance, task, and report material only.

Verified blob identities:

| Path | Git blob |
|---|---|
| `src/ch5_two_asset_hank/contracts.py` | `c746b616bec38531a7d96da81a54e2899d8aba53` |
| `src/ch5_two_asset_hank/policies.py` | `37bd85c4624bbbafd4ba310805d1c0b8ca08bb24` |
| `src/ch5_two_asset_hank/steady_state.py` | `e773dbdf5eb7641b61d5f5716d04eb9ab103f5c2` |
| `src/ch5_two_asset_hank/hjb.py` | `8b3d67079f13dd5d905e8d472a134a3316b26579` |
| `src/ch5_two_asset_hank/boundaries.py` | `1822089050614cc0fe059096832ab7a57e11cdfa` |
| `src/ch5_two_asset_hank/economics.py` | `fa29c7fcb9ed9ce52657affbb5a94c3b24662bed` |
| `src/ch5_two_asset_hank/derivatives.py` | `5455706a308e000414209ac4f831c6c7327f8263` |
| `src/ch5_two_asset_hank/generator.py` | `9e174df0bca9759c4167efef6b806c60ee451f3a` |
| `src/ch5_two_asset_hank/indexing.py` | `3aee864af5dce5128957896e5d7803c2a815aab6` |
| `src/ch5_two_asset_hank/productivity.py` | `e7714c3440fa3536ab63b0721c83e2f5b32c6bcc` |
| `src/ch5_two_asset_hank/kfe.py` | `1ace478651cf81255fedc80123779f7e33aaacdf` |
| `src/ch5_two_asset_hank/kfe_contract.py` | `f34490906b38144bcdd57b6b3a5be64ac78a4ad2` |
| `tests/test_r4_steady_state.py` | `73b4901b78060cfaa80afa1a0409fa6ad2a7dfa5` |
| `tests/test_r4_truncation_acceptance_contract.py` | `f5defdf92124ccdf878d2649ee20c224a17b0dc9` |

## Files read

- `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT.md`
- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- the accepted correction implementation task and report named by the live task
- the steady-state authorization report named by the live task
- the fourteen scientific/test paths in the identity table above

## Files written

- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT_REPORT.md`

One ephemeral runner script was written outside all tracked repository paths at `D:\ProjectTemp\ch5_r4_single_frozen_run_20260829.py`. It made one runner call, retained the returned result in memory, emitted the reportable fields, and did not alter either Git workspace.

## Pre-run checks

- Static compilation of the relevant scientific modules: `PASS`
- Non-steady-state pytest, with `tests/test_r4_steady_state.py` explicitly excluded: `56 passed in 3.96s`
- `git diff --check`: `PASS`
- Pre-run isolated-workspace status: clean (`## main...origin/main`)

The frozen-run budget was not consumed until all three checks passed.

## Exact execution count

- `run_frozen_r4_steady_state()`: exactly `1`
- Primary 25-point internal HJB solve within that call: exactly `1`
- Upper-buffer 29-point internal HJB solve within that call: exactly `1`
- `tests/test_r4_steady_state.py`: `0`
- Supplemental HJB/KFE/generator diagnostics: `0`

## Reached scientific diagnostics

### HJB, KKT, generator, and truncation

| Diagnostic | Primary 25-point | Buffer 29-point |
|---|---:|---:|
| iterations | 34 | 34 |
| HJB residual | `8.365197423643167e-10` | `8.372715853965929e-10` |
| KKT residual | `9.088497027490715e-15` | `9.423101212153411e-15` |
| generator max absolute row sum | `2.6645352591003757e-15` | `2.6645352591003757e-15` |
| minimum off-diagonal rate | `4.284173835999994e-05` | `4.284173835999994e-05` |
| boundary violation | `7.993605777301127e-15` | `8.43769498715119e-15` |

Both generators passed the accepted generator-validity contract.

All six common-core normalized changes passed the frozen `1e-3` guard:

| Quantity | Normalized change |
|---|---:|
| value | `2.9348475455283523e-09` |
| consumption | `2.165192411731261e-09` |
| transfer | `1.92715998714732e-09` |
| labor | `3.7659760021779296e-09` |
| adjustment cost | `1.0345611728412862e-09` |
| mu_a | `1.92715998714732e-09` |

Canonical candidate mismatch count was `0`. Liquid-drift Z/F/B classification mismatch count was `0`. Boundary/KKT compatibility passed.

There were exactly two raw-ID mismatches, both with bilateral intra-solve alias evidence and a common canonical `BZ` identity:

| State `(a,b,z)` | Raw 25 / 29 | Canonical 25 / 29 | Alias available 25 / 29 | Hamiltonian gap 25 / 29 | Hamiltonian bound 25 / 29 | mu_b 25 / 29 | class 25 / 29 | KKT state residual 25 / 29 |
|---|---|---|---|---|---|---|---|---|
| `(0.5,0.0,0.5)` | `BF / BZ` | `BZ / BZ` | `true / true` | `6.661338147750939e-16 / 1.1102230246251565e-15` | `4.0805675444274515e-15 / 4.080567544427456e-15` | `-5.551115123125783e-16 / 2.1094237467877974e-15` | `Z / Z` | `8.296975767380606e-16 / 4.7411290099317635e-15` |
| `(1.0,0.0,0.5625)` | `BF / BZ` | `BZ / BZ` | `true / true` | `1.1102230246251565e-15 / 1.1102230246251565e-15` | `3.5802429268395466e-15 / 3.5802429268395544e-15` | `-3.219646771412954e-15 / 3.3306690738754696e-15` | `Z / Z` | `3.737930640348919e-15 / 1.8142529359444556e-16` |

For each state and each solve, the Hamiltonian gap was below its solve-local `tau_H` bound. No broad F/Z alias was used.

### Illiquid connectivity

- Upward `a` edges: `134`
- Downward `a` edges: `4`
- Directional `mu_a/h_a` rate consistency: `PASS` through the runner's internal fail-closed gate
- Cross-`a` edges from `G_b`: none
- Cross-`a` edges from `G_z`: none

### Recurrent-class uniqueness

- Closed class count: `1`
- Closed class size: `225`
- Closed-class `a` index support: `(0,1,2)`, corresponding to all three frozen `a` values, including interior `a=0.5`
- Upper-`a`-only absorbing class: excluded
- Left nullity: `1`

### Stationary KFE and mass/density

- `||G^T g||_inf`: `3.885780586188048e-16`
- Normalization error: `4.440892098500626e-16`
- Minimum mass: `1.411264453687144e-17`
- Negative mass count: `0`
- Mass finite: `true`
- Density finite: `true`
- KFE diagnostics finite: `true`
- Sum of mass: `0.9999999999999996`
- Mass conservation error: `2.6645352591003757e-15`
- Mass/density consistency error: `3.3306690738754696e-16`
- KFE closed class count: `1`; unique stationary distribution: `true`
- Forward KFE operator: accepted transpose of the backward generator contract

### Aggregates

- Exact `A_hh`: `0.010765933312087405`
- Exact `B_hh`: `0.015679440387058798`

## Terminal failure

None. The unique authorized full call returned normally.

## Forbidden-operation check

- Frozen runner invoked more than once: no
- `tests/test_r4_steady_state.py` executed: no
- Extra HJB/KFE/generator diagnostic execution: no
- Source, tests, fixture, parameters, equations, grids, or tolerances modified: no
- Repair, tuning, or rerun: no
- MATLAB executed: no
- AR(1), transition, or IRF work entered: no
- Merge, rebase, reset, checkout, clean, stash, broad staging, or force-push: no
- Stale source checkout mutated: no

## Recommended next gate

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP`

This PASS is execution evidence only. Independent acceptance remains pending, and this task does not itself authorize MATLAB/Python parity execution, AR(1), transition, or IRF work.
