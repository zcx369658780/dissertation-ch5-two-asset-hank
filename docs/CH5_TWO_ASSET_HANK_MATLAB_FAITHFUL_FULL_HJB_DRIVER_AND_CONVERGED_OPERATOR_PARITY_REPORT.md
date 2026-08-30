# Chapter 5 Two-Asset HANK MATLAB-Faithful Full HJB Driver and Converged Operator Parity Report

Date: 2026-08-30

## Terminal classification

`MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_BLOCKED`

The frozen MATLAB HJB-only batch produced a valid converged 50-state HJB object, but the one authorized Python batch failed during its first faithful operator construction and produced no comparable HJB object. The frozen Python operator rejected a negative MATLAB component rate. The scientific budget was therefore consumed at MATLAB/Python/comparator counts `1/1/0`; no repair, rerun, tuning, or comparison was performed. This is BLOCKED rather than MATERIAL MISMATCH because two valid comparable HJB objects do not exist.

## Live authority and identities

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Worktree: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Fresh-fetched live start `origin/main`: `90542c972d7a2eb692789f4ecc9ef996a243ffd0`.
- Pre-publication final `origin/main`: `90542c972d7a2eb692789f4ecc9ef996a243ffd0`; publication commit/read-back is recorded in the executor handoff.
- Start worktree: clean after fast-forward.
- Primary authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Accepted faithful bare-`a`, taper/drift, and local-policy chain was present and unchanged.

All required MATLAB hashes matched exactly:

| Source | SHA-256 |
|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` |

## Full pre-KFE MATLAB source map

The mandatory source audit closed before implementation:

| MATLAB source | Exact role |
|---|---|
| `HANK_2ASSETS_HJB.m:2-35` | Household/HJB parameter, numerical, rate, wage, tax, transfer, and prior-result extraction. |
| lines 46-63 | Uniform `b`, `ah`, and `z` grids; arrays have logical order `(i,j,nz)=(b,a,z)`. MATLAB column-major flatten index is `i+(j-1)I+(nz-1)IJ`. |
| lines 64-66 | `Bswitch=[I*la11,I*la12;I*la21,I*la22]`, equivalent to `kron(la_mat,speye(I*J))`; productivity blocks are outermost in the flattened vector. |
| lines 79-88 | `rb_neg=rb+rb_gap`; state-dependent `Rb`; `raah=rah*(1-0.1*(ahmax/ah)^(-9))`; broadcast to `Rah`. |
| lines 90-113 and `lab_solve2.m:1-11` | `tempMat=Rah.*raah+Rb.*bbb+Tt`; cellwise `fzero` baseline labor; `c0=(1-tau)wzl0+Rb*b+Tt`; initial value is baseline flow utility divided by `rho`. |
| lines 114-123 | Iteration begins; `VbF/VbB` and `VahF/VahB` finite differences; liquid endpoints use baseline-resource marginal utility; illiquid forward derivative is zero at `a_max`, backward derivative zero at `a=0`. |
| lines 124-136 | `1e-6` derivative floors; `C_B/C_F`, `l_B/l_F`, `sc_B/sc_F`; strict `1e-12` `Ic_B/Ic_F/Ic_0`; selected flow utility. |
| lines 137-154 | Four bare-`a` `HANK3_FOC` calls; lower/upper-`a` transfer overrides; `sdh=-d-cost`; `Idh_F/Idh_B/Idh_0`; lower/upper-`b` overrides. |
| lines 155-188 | Iteration `BB` uses separate component sums: backward `-(Ic_B*sc_B+Idh_B*sdh_B)/db`, forward `(Ic_F*sc_F+Idh_F*sdh_F)/db`, then diagonal closure. The components are not netted through final `mu_b`. |
| lines 190-229 | Iteration `AAH` uses derivative-side `dhB/dhF`, `MhB=min(dhB,0)`, `MhF=max(dhF,0)+Rah*a`, plus the upper-`a` override. It is not constructed from `sign(mu_a)`. |
| lines 232-245 | `A=BB+AAH+Bswitch`; implicit matrix `(1/Delta+rho)I-A`; RHS `u+V/Delta`; MATLAB direct sparse solve and reshape. |
| lines 246-261 | Convergence statistic `max(abs(V_new-v),[],'all')`; accept only if strictly below `crit`; maximum `maxit`. Designated caller uses `Delta=1000`, `crit=1e-7`, `maxit=100`. |
| lines 262-332 | After the loop, selected `d`, final net liquid drift `s`, and tapered illiquid drift `mh` are formed; a separate post-convergence `BB/AAH/A` is reconstructed from signs of these net drifts immediately before KFE. |
| line 333 onward | Stationary KFE begins and was not executed by the external HJB-only evaluator. |

The audit proved that backward and forward component contributions can coexist in one HJB row before diagonal closure. It also proved that the iteration operator and the post-convergence pre-KFE net-drift reconstruction are distinct source objects. Corrected/reference `generator.py` is not the faithful iteration-operator oracle.

## Faithful architecture attempted and reverted

Before freeze, an isolated candidate architecture was implemented only in faithful-route paths:

- temporary extension of `matlab_faithful_policy.py` to expose separate iteration `BB` component rates;
- new candidate `matlab_faithful_operator.py` with MATLAB `(b,a,z)` ordering, component-rate `BB/AAH`, and finite-state `Bswitch`;
- new candidate `matlab_faithful_hjb.py` with source initialization, derivative updates, faithful local selection, implicit solve, source convergence rule, and separate iteration/post-convergence operators;
- targeted candidate test `test_matlab_faithful_full_hjb.py`.

Corrected/reference `policies.py`, `hjb.py`, and `generator.py` were never modified or repurposed. No KKT, multiplier, corrected-candidate, or Bellman-residual veto was introduced.

Because the frozen Python scientific call failed before a valid HJB object existed, all unaccepted candidate production/test changes were reverted during fail-closed closeout. The accepted local-policy file returned to its predecessor SHA-256:

`95D74893BAD22082FB1C731AD4E35E19A69039DFC30B477F7AAACC54ED3F446E`

Final repository mutation is therefore only this BLOCKED report.

## `Bswitch`, initialization, and engineering preflights

The frozen fixture used the designated two-state finite switch:

```text
[[-1/3, 1/3],
 [ 1/3,-1/3]]
```

The faithful candidate used `kron(switch_matrix,I_(I*J))`, not the corrected reflected-diffusion productivity generator.

An initialization-only external MATLAB extraction generated shared `l0`, `c0`, and `v0` using exact `tempMat`, `lab_solve2`, and baseline formulas. It did not solve the HJB and did not consume the scientific HJB budget. Initialization artifact SHA-256:

`C6662095D14CB83D820FACFB4779CA188BE23958BE162B943BDD2F3959522A9F`

Independent Python source-initialization preflight versus that artifact produced:

- `l0` maximum absolute difference: `2.6645352591003757e-15`;
- `c0` maximum absolute difference: `3.1086244689504383e-15`;
- `v0` maximum absolute difference: `7.105427357601002e-15`.

Pre-freeze targeted engineering checks covered MATLAB ordering, coexisting component rates, exact `Bswitch`, initialization, one synthetic implicit step, and predecessor primitives:

`21 passed in 0.74s`

These preflights exposed no failure because their synthetic component rates were nonnegative. They did not evaluate the frozen converged HJB fixture.

## Frozen fixture and identities

Artifact root:

`D:\ProjectTemp\ch5-matlab-faithful-full-hjb-parity-20260830-001`

The fixture had `5 b × 5 a × 2 z = 50` states:

- `b=linspace(-0.5,0.5,5)`, covering lower/interior/upper and borrowing states;
- `a=linspace(0,2,5)`, covering taper lower/interior/upper states;
- `z=[0.8,1.3]`, both designated productivity states;
- source numerics `Delta=1000`, `maxit=100`, `crit=1e-7`;
- source cost/FOC values `chi0=0.1`, `chi1=2`, `a_bar=1e-6`.

All identities were frozen before either scientific HJB call:

| Frozen object | SHA-256 |
|---|---|
| parameter/grid manifest | `784ADA4834A3FD8CFBCE7C3B5BC652DE63C2A986802603799CE3670860EF6C7A` |
| ordering adapter | `52EB994358F07767AD8859D737C3D7A89BC7FB04DC063754027CA80386F2926D` |
| initialization artifact | `C6662095D14CB83D820FACFB4779CA188BE23958BE162B943BDD2F3959522A9F` |
| MATLAB HJB-only evaluator | `E81AB34611E3C31DAF2400ED6A34B58F91C4FA0E0FBCCEE843828F5A6588DCBA` |
| Python runner | `CE3C320DC6D7014A692FE0B71165854236FECD0D23C0A8026C1BCD152D5FF2AC` |
| comparator | `4471CCC837A66245DCB8D2CA1D45F1BD79CBEE5EAE80874B14933E06C75F9A92` |
| tolerances | `915B3539828F42099182A9145E64B4A353D0D049AF1674549C1031C923CEF72D` |
| pre-execution ledger | `4E027B68F537C458958DA7F76363B41A07877E1C0E0A1B902CDD3AE934ED8158` |
| frozen policy candidate | `58CD63AC847E7D241B39CE687D25BCA9DB82E515007F205AC4E01B37D7ED53AF` |
| frozen operator candidate | `D946C8DEB251DA06C1859FBFD7E6BEE12B53F3891BE55F79D66DD7E8B50367A7` |
| frozen HJB candidate | `D96231B44C5BA45C694C0A943C308EF0CF5CFAFE93E0DE6C8E0ED736278F35DA` |

The solver-derived value bound was frozen at absolute `1e-7`, exactly the designated source convergence scale. Explicit scalar/rate/operator values used the frozen `128*eps64*max(1,abs(x),abs(y))` rule. No tolerance was changed after output.

## Scientific execution ledger and blocker

| Action | Calls/budget | Outcome |
|---|---:|---|
| MATLAB source-extracted converged HJB batch | `1/1` | Valid: converged in 9 iterations; statistic `3.882012578060312e-08`; 50-state output SHA `3457F51AC0F910EA40FC35A832518B9068456E22DEA4E4783F487976432DDC0A`. |
| Python faithful HJB batch | `1/1` | Failed before first valid HJB object: `ValueError: MATLAB HJB component rates must be non-negative`. No Python output artifact exists. |
| Comparator | `0/1` | Not run because comparable MATLAB and Python objects did not both exist. |

The failure was at frozen `matlab_faithful_operator.py` component validation while constructing the first iteration `BB`.

Read-only inspection of the valid frozen MATLAB output established the smallest exact blocker:

| Operator | NNZ | Minimum off-diagonal | Maximum absolute row sum |
|---|---:|---:|---:|
| iteration `BB` | 108 | `-0.45465503938313373` | `0` |
| iteration `AAH` | 110 | `0.03601822162356304` | `2.7755575615628914e-17` |
| `Bswitch` | 100 | `0.3333333333333333` | `0` |
| iteration full `A` | 230 | `-0.45465503938313373` | `2.7755575615628914e-16` |
| post-convergence `BB` | 88 | `0.19141418136524457` | `0` |
| post-convergence `AAH` | 80 | `0.0017675480456268225` | `0` |
| post-convergence full `A` | 184 | `0.0017675480456268225` | `1.3877787807814457e-16` |

Thus the designated source-extracted iteration `BB` itself contains a negative off-diagonal component for this frozen source-valid fixture, while its rows still close exactly. This invalidates the frozen Python assumption that every MATLAB iteration component rate must be nonnegative. It does not authorize removing that guard or accepting negative rates after observing output; doing so would be an in-task scientific repair and would require a replacement Python/parity budget under new live authority.

## Required comparisons not reached

Because no Python HJB output exists, none of the following was compared and no mismatch claim is made:

- convergence/iteration identity;
- converged `V` or policy arrays;
- labels/directions;
- `BB`, `AAH`, `Bswitch`, full `A`, or post-convergence sparse patterns/values;
- representative rates;
- solver-output differences;
- Bellman/operator diagnostics across languages.

Complete failure list contains exactly the Python component-nonnegativity rejection above. Scientific mismatch list is empty because comparator calls remained zero.

## Scope, prohibited operations, and closeout

No designated MATLAB source was modified. No corrected/reference production module was modified. No KFE, stationary distribution, aggregate, steady state, corrected D1/D2/D3, asset-tail, transition, IRF, dynamics, calibration extension, or Results action occurred.

Final changed path is exactly:

- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_REPORT.md`.

Pre-publication worktree contains only this report. The unaccepted faithful full-HJB candidate was reverted; no production implementation is accepted or published by this task.

Acceptance level: full-HJB source audit, source-defined initialization, engineering preflights, and one valid MATLAB HJB-only output are evidence only. MATLAB/Python full-HJB/operator parity is not accepted.

The PASS-only next gate—MATLAB-faithful contaminated-row KFE—is not authorized. A new live task is required to adjudicate the source-faithful treatment of negative iteration-`BB` components and, if authorized, grant a replacement Python HJB/comparator budget. It must preserve the frozen MATLAB output and must not rerun that MATLAB batch unless explicitly authorized.

`MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_BLOCKED`
