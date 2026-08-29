# CH5 Two-Asset HANK Pre-P5 Same-Input Parity Adapter Design and Conformance

## Terminal classification

`SAME_INPUT_PARITY_ADAPTER_BLOCKED_MATLAB`

The two expressly authorized test-only adapters are technically isolatable and passed static/synthetic conformance checks:

- MATLAB O1 is a one-line domestic FOC scale correction from `a` to `max(a,a_bar)` outside the production tree.
- Python O2 rebinds only `ch5_two_asset_hank.hjb.build_operator`, retains production asset generators, and injects the exact frozen two-state `Q_z_common`.

However, the frozen common fixture requires `gamma_c/ga=1.0`, while accepted original MATLAB `HANK_2ASSETS_HJB.m` evaluates CRRA utility as `C^(1-ga)/(1-ga)` in both initialization and iteration without a `ga==1` logarithmic branch. At `ga=1`, this is non-finite. Correcting it would require a scientifically material main-HJB utility adapter or production-source change beyond the task's authorized O1/O2 adapters. Therefore the package is not ready for scientific execution, and no HJB/KFE/model solve occurred.

## Live authority and source identities

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched task/base `origin/main`: `4c0afddfa93aeb082b55b3612a522fe25f4a0301`
- task: `CH5_TWO_ASSET_HANK_PRE_P5_SAME_INPUT_PARITY_ADAPTER_DESIGN_AND_CONFORMANCE`
- accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- accepted P1-P4 evidence: `daa3e60ff97828ec80fb2e83bee863eb4aa632a4`
- failed unchanged-native preflight report: `1435176971de0bee1b7426482d8cfc18452dc130`
- external artifact root: `D:\ProjectTemp\ch5-pre-p5-same-input-adapter-design-artifacts-20260829`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..4c0afddfa93aeb082b55b3612a522fe25f4a0301 -- src tests`: empty

Accepted MATLAB source identities:

| Source | SHA-256 | Result |
|---|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS |

No production file or test was written.

## Why unchanged-native execution was impossible

The predecessor preflight established two interface incompatibilities rather than parity failures:

1. the earlier common grid began at `a=0.5`, but accepted Python `GridSpec` requires `a[0]==0`;
2. accepted MATLAB main hard-codes a two-state productivity block and cannot accept arbitrary `Nz=9`.

The current fixture resolves those interface shapes by using `a[0]=0` and `Nz=2`. The accepted structural O1/O2 decisions then authorize a test-only low-`a` FOC helper and a test-only common-productivity operator injection. The later `ga=1` audit exposes a separate main-HJB utility incompatibility not covered by either decision.

## Frozen 50-state common manifest

| Object | Frozen value |
|---|---|
| `rho` | `0.05` |
| `gamma_c / ga` | `1.0` |
| `phi / frisch_l` | `1.0 / 1.0` |
| `chi_0`, `chi_1`, `a_bar` | `0.05`, `1.0`, `0.5` |
| `r_b`, `w`, `tau` | `0.03`, `1.0`, `0.0` |
| migration cost / labor weight | `0.0 / 1.0` |
| external transfer / `rb_gap` | `0.0 / 0.0` |
| `r_a / rah` pair | `0.040 / 0.041` |
| `a` | `[0.0,0.5,1.0,1.5,2.0]` |
| `b` | `[0.0,1.25,2.5,3.75,5.0]` |
| `z` | `[0.8,1.3]` |
| state count | `5*5*2=50` |
| `Q_z_common` | `[[-0.4,0.4],[0.3,-0.3]]` |
| `da`, `db`, cell weight | `0.5`, `1.25`, `0.625` |

The persisted conformance manifest is 3024 bytes, SHA-256 `E5069AD58FDF89C747B170526F5C3297663289F835C3AA230BE94780F329F45C`.

## Adapter A: MATLAB O1 test-only helper

The external helper is:

`D:\ProjectTemp\ch5-pre-p5-same-input-adapter-design-artifacts-20260829\matlab_o1\HANK3_FOC.m`

It is 577 bytes, SHA-256 `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315`. Production `HANK3_FOC.m` remains byte-identical.

Complete substantive diff:

```diff
 if foreign == 1
     d = (min(pa./pb - 1 + chi0*price,0) + max(pa./pb - 1 - chi0*price,0)).*a/chi1;
 else
-    d = (min(pa./pb - 1 + chi0,0) + max(pa./pb - 1 - chi0,0)).*a/chi1;
+    d = (min(pa./pb - 1 + chi0,0) + max(pa./pb - 1 - chi0,0)).*max(a,a_bar)/chi1;
 end
```

The foreign branch, signature, parameters, thresholds, price treatment, and all unrelated formulas are unchanged. A final newline is the only non-substantive byte difference outside the displayed line.

Synthetic conformance covered `a=0`, `a=0.25`, `a=a_bar=0.5`, and `a=1.0`, each with positive-transfer, negative-transfer, and zero-transfer derivative pairs. All 12 corrected MATLAB values exactly matched accepted Python `transfer_candidate`. Representative results:

| `a` | `v_a/v_b` | corrected MATLAB | Python |
|---:|---:|---:|---:|
| 0.0 | 1.2 | 0.075 | 0.075 |
| 0.25 | 0.8 | -0.075 | -0.075 |
| 0.5 | 1.02 | 0 | 0 |
| 1.0 | 1.2 | 0.15 | 0.15 |

MATLAB conformance JSON: 1542 bytes, SHA-256 `C70CC664EC5E27A92B4A55F54A11411A3425AD539A455B4D47E891A989479FC2`.

### Future path-resolution proof

The static MATLAB path test used:

```matlab
addpath(original_root,'-end');
addpath(temporary_root,'-begin');
```

`which` resolved:

- `HANK_2ASSETS_HJB` -> accepted original main;
- `HANK3_cost` -> accepted original cost helper;
- `HANK3_FOC` -> external O1-corrected helper.

No HJB was invoked during this check.

## Adapter B: Python O2 common-Q operator injection

External adapter: `python_common_q_adapter.py`, 1556 bytes, SHA-256 `D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225`.

The exact runtime name rebound is:

`ch5_two_asset_hank.hjb.build_operator`

The successor would install the binding only immediately around a production `solve_hjb` call and restore the original binding in `finally`. No repository module is written.

The adapter:

1. requires the exact frozen `z=[0.8,1.3]`;
2. calls production `_asset_generator(grid,policy.mu_a,0,tolerance)`;
3. calls production `_asset_generator(grid,policy.mu_b,1,tolerance)`;
4. constructs `G_z=kron(Q_z_common,I_25)` in accepted canonical `[a,b,z]` flattening;
5. returns the unchanged production `OperatorBundle` fields and diagnostics.

It does not call production `build_z_generator`. It does not replace `compute_derivatives`, `select_policy`, any policy/KKT formula, the implicit solve, `hjb_residual`, convergence logic, or production KFE.

Synthetic conformance results:

- `G_a` sparse nonzero difference from direct production `_asset_generator`: `0`;
- `G_b` sparse nonzero difference: `0`;
- `G_z` exact dense/sparse equality with `kron([[-0.4,0.4],[0.3,-0.3]],I_25)`: PASS;
- sampled canonical low/high-z transitions: `0.4` upward and `0.3` downward: PASS;
- total maximum row sum: `5.551115123125783e-17`;
- minimum off-diagonal: `0.016`;
- runtime binding installation: PASS;
- restoration of original production binding: PASS.

The conformance used only synthetic drift arrays; it did not call policy selection or a model solve.

## Common measure and aggregate semantics

Productivity is a finite Markov state, so no continuous-z quadrature factor is permitted. A density converts to probability mass as:

`mass = density * da * db = density * 0.625`, followed by required `sum(mass)=1`.

Frozen aggregates:

- `C_hh=sum(mass*c)`;
- raw hours `H_hh=sum(mass*l)`;
- effective labor `L_hh=sum(mass*z*l)`;
- `A_hh=sum(mass*a)`;
- `B_hh=sum(mass*b)`.

MATLAB `Lt` uses `zzz.*l` and is effective labor. It must later be compared with Python `sum(mass*z*l)`, never Python raw hours.

The orientation adapter is MATLAB `[b,a,z]` to Python `[a,b,z]`; within each z block the Python canonical asset index maps by transposing the first two logical axes. `G_z=kron(Q_z_common,I_25)` preserves the already accepted P3 z-block orientation.

## Required-field mapping audit

### MATLAB

| Structure | Required fields and mapping |
|---|---|
| `param` | `ga=1`, `rho=0.05`, `alphal=1`, `frisch_l=1`; `alphap` is read but not used by the accepted main |
| `grid` | `I=5` liquid points, `J=5` illiquid points, `bmin=0`, `bmax=5`, `amin=0`, `amax=2`, `Nz=2`, `zmin=0.8`, `zmax=1.3`, exact `z`, exact `la_mat=Q_z_common` |
| `num` | `maxit=500`, `crit=1e-8`, `Delta=10`, `homecrit=1e-11`; `maxiter` is read but unused |
| `CHIh` | `chi0=0.05`, `chi1=1`, `a_bar=0.5`; domestic `fixcost/fixcost2` are loaded but unused and must be explicitly frozen at neutral zero by any successor authority |
| `results` | `rb=0.03`, `rah` pair, `w=1`, `rb_gap=0`, `tau=0`, `Tt=0`; prior `Ct/At/Bt/Lt` affect reported deltas but not the solve and require explicit neutral initialization; display-only province fields are not reached with `show_result=0` |

### Python

`GridSpec`, `EconomicParams`, `HouseholdInputs`, caller-supplied `initial_value`, and `HJBNumerics` can represent the frozen grid, scalar parameters, two `r_a` values, and numerical tolerances. O2 changes only the runtime operator binding. Production KFE accepts explicit constant `cell_weights=0.625` through its existing contract.

The neutral MATLAB bookkeeping fields and unused loaded fields are documentable, but they do not cure the material `ga=1` utility problem.

## Initialization and numerical mapping audit

MATLAB does not accept an external initial value. It computes `l0` by `fzero`, then constructs:

```matlab
c0 = (1-tau).*w.*zzz.*l0 + Rb.*bbb + Tt;
v02 = (c0.^(1-ga)./(1-ga) - l0.^(1+1/frisch_l)./(1+1/frisch_l))./rho;
v = v02;
```

Python accepts an arbitrary logical `initial_value` directly. If the MATLAB initialization were finite, its mapped array could be reproduced externally for Python, though byte-identical iterative initialization is not required for a converged fixed-point comparison.

At the frozen `ga=1`, MATLAB's consumption term divides by zero. The same expression is used for per-iteration utility:

```matlab
u = C.^(1-ga)./(1-ga) - ...;
```

A static allowed test at `C=[0.5,1,2]` returned three non-finite values; JSON encoded them as `null`, and `all_finite=false`. Evidence SHA-256: `E0CDAE97963FA8C525CD4F0D859FEB01AD57132CAC91C3EEA99DCAA62821B4FE`.

This is not an initialization-only detail: it affects the HJB flow utility itself. A log-utility branch such as `log(C)` would be a scientifically material main-HJB correction not authorized here.

Mapped numerical settings otherwise are:

| Setting | MATLAB | Python |
|---|---:|---:|
| max iterations | `maxit=500` | `500` |
| change tolerance | `crit=1e-8` | `1e-8` |
| pseudo-time | `Delta=10` | `pseudo_time_step=10` |
| HJB residual | not exposed as stopping rule | acceptance audit `1e-7` |
| generator | `homecrit=1e-11` | `1e-11` |
| drift zero | hard-coded directional thresholds near `1e-12` | `1e-12` |
| KKT | not exposed | `1e-7` |
| KFE residual/normalization | not exposed as explicit tolerance | `1e-10` |
| nonnegative mass | not exposed | `1e-12` |

No value was tuned.

## Persistence and no-solve proof

`conformance_preflight.py` is 5545 bytes, SHA-256 `32212CD65191A58836B5DA17342910D90F71392425C9400D145F6AD6DE3B12F2`. It wrote JSON with `allow_nan=False`, read it back, and verified exact logical/numeric structure. MATLAB O1 JSON was likewise written and decoded. The initial Code Analyzer assertion was rejected because the copied legacy helper retains two analyzer warnings; subsequent inspection confirmed the path identities, and direct helper conformance completed without invoking HJB.

Exact execution counts:

| Action | Count |
|---|---:|
| MATLAB `HANK_2ASSETS_HJB` | 0 |
| Python `solve_hjb` | 0 |
| KFE solve | 0 |
| P1-P4 rerun | 0 |

## Forbidden-operation check

- accepted MATLAB main/helper modified: no
- Python `src/tests` modified: no
- MATLAB HJB called: no
- Python `solve_hjb` called: no
- KFE called: no
- production `build_z_generator` used for common fixture: no
- P1-P4 rerun: no
- test-only adapters presented as production changes: no
- frozen fixture or tolerances tuned: no
- P5 acceptance issued: no
- dynamics or Results entered: no
- merge, rebase, reset, or force-push: no

## Required successor before execution

The four-run parity task must not be issued yet. The smallest next gate is a MATLAB utility-interface design decision that explicitly chooses one of:

1. authorize a test-only main-HJB adapter adding the mathematically correct `ga==1` log-utility branch in both initialization and flow utility, with a complete one-purpose diff and static conformance; or
2. publish a new scientifically justified common curvature that the unchanged accepted MATLAB CRRA implementation can represent, while recognizing that this changes the currently frozen fixture.

That decision must also freeze neutral values for MATLAB's domestic-unused/bookkeeping fields. Only after a new live task resolves this blocker may a successor reconsider the exact four one-shot execution contract. This report does not authorize those runs or Owner P5 acceptance.
