# CH5 Two-Asset HANK Pre-P5 True Same-Input Aggregate Parity

## Terminal classification

`TRUE_SAME_INPUT_AGGREGATE_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT`

The task stopped at the pre-scientific compatibility gate. No HJB, KFE, policy, generator-based household solve, MATLAB model, or Python model was executed.

Two independent accepted-production interface conflicts prevent the task's frozen common fixture from being supplied unchanged to both implementations:

1. Accepted Python `GridSpec` rejects the task-frozen illiquid grid because it requires `a[0] == 0`, while the task requires `a=[0.5,1.0,1.5,2.0,2.5]`.
2. Accepted original MATLAB `HANK_2ASSETS_HJB.m` hard-codes a two-state productivity block and cannot consume `Nz=9` with an arbitrary exact `9x9 Q_z_common` through its existing interface without production-source modification.

Changing either frozen grid or either production interface is forbidden. The common productivity operator was therefore not constructed, no harness was frozen for scientific execution, and all four scientific execution counts remain zero.

## Live authority and identities

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched task/base `origin/main`: `472fb4b96f4087952b5983b83bd2c08d5861ddfa`
- task: `CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY`
- accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- accepted P1-P4 evidence: `daa3e60ff97828ec80fb2e83bee863eb4aa632a4`
- latest completed native-robustness report: `e5271f3e218244fa77ec080b3e4a7005cfb1447d`
- isolated repository workspace: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`
- external preflight root: `D:\ProjectTemp\ch5-pre-p5-true-same-input-parity-artifacts-20260829`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..472fb4b96f4087952b5983b83bd2c08d5861ddfa -- src tests`: empty

Python scientific source and tests remain unchanged from the accepted baseline.

Accepted MATLAB identities all passed:

| Source | SHA-256 | Result |
|---|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS |

## Frozen common manifest

The task-frozen object was read and preserved without substitution:

| Object | Frozen value |
|---|---|
| `rho` | `0.05` |
| `gamma_c` | `1.0` |
| `phi` | `1.0` |
| `chi_0` | `0.05` |
| `chi_1` | `1.0` |
| `a_bar` | `0.5` |
| `r_b` | `0.03` |
| `w` | `1.0` |
| `tau` | `0.0` |
| migration cost | `0.0` |
| labor weight | `1.0` |
| `mu_z` | `0.2` |
| `sigma_z` | `0.1` |
| baseline/perturbation `r_a` | `0.040 / 0.041` |
| `a` | `[0.5,1.0,1.5,2.0,2.5]` |
| `b` | `[0.0,1.25,2.5,3.75,5.0]` |
| `z` | `linspace(0.5,1.5,9)` |
| required state count | `5*5*9=225` |
| `da`, `db`, finite-state cell weight | `0.5`, `1.25`, `0.625` |
| max iterations / pseudo-time | `500 / 10` |
| change / HJB residual tolerance | `1e-8 / 1e-7` |
| generator / drift tolerance | `1e-11 / 1e-12` |
| KKT tolerance | `1e-7` |
| KFE stationarity/normalization | `1e-10` |
| nonnegative mass tolerance | `1e-12` |

All common `a` points satisfy `a>=a_bar`, as designed. The Jiangsu 2016 cache was not read or used as the scientific input object.

## First blocker: accepted Python grid contract

The preflight attempted to construct the exact frozen Python common grid through the accepted production `GridSpec` before calling `build_z_generator`:

```python
a = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
b = np.array([0.0, 1.25, 2.5, 3.75, 5.0])
z = np.linspace(0.5, 1.5, 9)
grid = GridSpec(a, b, z, 0.0)
```

Accepted `contracts.py:22-49` contains the immutable production contract:

```python
if not np.isclose(self.a[0], 0.0):
    raise ValueError("the frozen illiquid lower bound requires a[0] == 0")
```

The exact runtime result was:

```text
ValueError: the frozen illiquid lower bound requires a[0] == 0
```

This occurred before the sole planned `build_z_generator(grid, params)` statement. Consequently:

- `build_z_generator` invocation count: `0`;
- `Q_z_common` construction count: `0`;
- `Q_z_common.npy` exists: no;
- `common_q_manifest.json` exists: no.

The failed preflight script is 2111 bytes, SHA-256 `489445C83618177FB47F5A0A643504645D500BF4A7E9EA78B2E31CDD83E1414D`. It was not edited or retried after the gate failed. Modifying Python `GridSpec`, inserting a forbidden `a=0`, or changing the task-frozen `a` grid would exceed authority.

Blocker: `BLOCKED_TRUE_SAME_INPUT_AGGREGATE_PYTHON_FROZEN_GRID_INTERFACE_INCOMPATIBLE`.

## Independent MATLAB productivity-interface audit

The accepted original MATLAB function reads these fields:

- `param`: `ga`, `alphap`, `alphal`, `rho`, `frisch_l`;
- `grid`: `I`, `bmin`, `bmax`, `J`, `amin`, `amax`, `Nz`, `zmin`, `zmax`, `z`, `la_mat`;
- `num`: `maxit`, `crit`, `Delta`, `maxiter`, `homecrit`;
- `CHIh`: passed to `HANK3_FOC` and `HANK3_cost`, which require `chi0`, `chi1`, `fixcost`, `fixcost2`, `a_bar`;
- `results`: `rb`, `rah`, `w`, `rb_gap`, `tau`, `Tt`, `Ct`, `At`, `Bt`, `Lt`; additional province/display fields are referenced only when `show_result==1`.

The economic scalar fields could be mapped unambiguously from the frozen task with `show_result=0`, `rb_gap=0`, `Tt=0`, and domestic adjustment-cost fields. The productivity interface cannot be mapped:

```matlab
Bswitch = [
  speye(I*J)*la_mat(1,1), speye(I*J)*la_mat(1,2);
  speye(I*J)*la_mat(2,1), speye(I*J)*la_mat(2,2)];
```

During both HJB construction and final generator reconstruction it further hard-codes:

```matlab
BB = [BBi{1}, sparse(I*J,I*J); sparse(I*J,I*J), BBi{2}];
AAH = [AAHi{1}, sparse(I*J,I*J); sparse(I*J,I*J), AAHi{2}];
```

The stationary distribution is likewise restricted to two slices:

```matlab
g(:,:,1) = reshape(g_stacked(1:I*J),[I,J]);
g(:,:,2) = reshape(g_stacked(I*J+1:I*J*2),[I,J]);
```

Although `grid.Nz` controls array allocation and loops, the actual productivity generator and combined operator dimensions are fixed at `2*I*J`. Supplying `Nz=9` and a `9x9 la_mat/Q_z_common` would still index only states 1 and 2 and would create matrices incompatible with `M=I*J*Nz=225`. The interface cannot consume the task's exact productivity object without changing production source.

Named blocker: `BLOCKED_TRUE_SAME_INPUT_AGGREGATE_MATLAB_PRODUCTIVITY_INTERFACE_INCOMPATIBLE`.

## Measure, orientation, and labor semantics

The requested common definitions are internally clear:

- mass uses finite-state productivity with constant asset cell weight `da*db=0.625` and no continuous-`z` quadrature;
- Python canonical shape is `[a,b,z]`;
- MATLAB storage is `[b,a,z]`, requiring the accepted first-two-axis orientation adapter;
- raw hours are `H_hh=sum(mass*l)`;
- effective labor is `L_hh=sum(mass*z*l)`;
- MATLAB native `Lt` is effective labor because it uses `zzz.*l`.

However, the source-interface blockers occur before a common 225-state grid/operator can exist in both implementations. No synthetic orientation or persistence preflight can establish scientific compatibility in their absence, so those later gates were not run.

## Exact execution counts and unavailable result tables

| Action | Count |
|---|---:|
| Python `build_z_generator` | 0 |
| MATLAB HJB/KFE scientific solve, `r_a=0.040` | 0 |
| Python HJB/KFE scientific solve, `r_a=0.040` | 0 |
| MATLAB HJB/KFE scientific solve, `r_a=0.041` | 0 |
| Python HJB/KFE scientific solve, `r_a=0.041` | 0 |
| P1-P4 rerun | 0 |

### Levels

| implementation | r_a | C_hh | H_hh | L_hh | A_hh | B_hh |
|---|---:|---:|---:|---:|---:|---:|
| MATLAB | 0.040 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Python | 0.040 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| MATLAB | 0.041 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Python | 0.041 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

Response deltas, pointwise policy differences, mass differences, aggregate tolerance evaluations, and validity diagnostics are unavailable because no scientific solve was authorized past the failed preflight.

## Forbidden-operation check

- MATLAB executed: no
- Python HJB/KFE/policy/generator scientific solve executed: no
- P1-P4 rerun: no
- MATLAB/Python production source or tests modified: no
- frozen grid, parameters, measure, productivity object, or tolerances altered: no
- Jiangsu native snapshot used as scientific input: no
- preflight repaired or retried after failure: no
- consumed scientific solve rerun: no
- P5 acceptance issued: no
- AR(1), transition, IRF, calibration extension, dynamics, or Results entered: no
- merge, rebase, reset, or force-push: no

## Recommended successor

P5 remains blocked. The smallest evidence-based successor is a pre-execution design-resolution task that must resolve both source-interface conflicts without silently changing the scientific object:

1. decide whether the accepted Python grid contract may be explicitly extended to support a positive illiquid lower bound, with production changes and tests separately authorized; and
2. decide whether MATLAB requires an externally authorized adapter/new accepted source capable of arbitrary `Nz` and exact `Q_z_common`, or whether a different truly common fixture must be specified that both unchanged accepted implementations can consume.

No new parity execution should be authorized until one exact common fixture passes both production interfaces. This report does not recommend Owner P5 acceptance.
