# Chapter 5 Two-Asset HANK MATLAB-Faithful HJB/Policy Local Integration and Parity Report

Date: 2026-08-30

## Terminal classification

`MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_PASS`

The first distinct MATLAB-faithful local policy/upwind path is implemented without changing the corrected/reference selector or the full HJB driver. A pre-frozen, source-extracted 11-case MATLAB/Python local comparison passed with zero continuous differences and zero categorical mismatches. This is local policy/upwind acceptance only; it is not converged HJB, KFE, steady-state, or dynamics acceptance.

## Live authority and source identities

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Worktree: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Fresh-fetched live start and execution-authority `origin/main`: `c800bd7277e8f620f9fa580d067b7db950604b5a`.
- Pre-publication final `origin/main`: `c800bd7277e8f620f9fa580d067b7db950604b5a`; the publication commit and final GitHub read-back are recorded in the executor handoff because a commit cannot embed its own SHA.
- Start worktree: clean after fast-forward.
- Primary authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Accepted primitives remained present and unchanged: `MATLAB_FAITHFUL_TRANSFER_FOC_USES_BARE_A` and `MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`.

All four designated source hashes matched before mutation:

| Source | Observed and required SHA-256 |
|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` |

## Exact designated MATLAB policy/upwind source map

MATLAB logical storage is `(i,j,nz)=(b,a,z)`, with `I` liquid nodes, `J` illiquid nodes, and `Nz` productivity nodes (`HANK_2ASSETS_HJB.m:10-20,46-63`). Python's existing canonical logical storage is `(a,b,z)`; the local scalar path therefore has no orientation ambiguity.

| MATLAB lines | Exact role and formula |
|---|---|
| 79-80 | `rb_neg=rb+rb_gap`; `Rb=rb` for `bbb>=0`, otherwise `rb_neg`. |
| 81-88 | `raah=rah.*(1-0.1*(ahmax./ah).^(-9))`, broadcast over `b,z` into `Rah`. |
| 90-113 | Auxiliary `tempMat`; `lab_solve2` root at every cell; baseline `l0`; initial `c0` and value. `lab_solve2.m:1-11` is exactly `l - (alphac/alphal*(1-tau)*w*z)^frisch_l*(l*(1-tau)*w*z+tempMat)^(-ga*frisch_l)`. The bounded local fixture supplies the already-computed local `l0`/baseline labor and does not claim a native initialization-root execution. |
| 116-123 | `VbF/VbB` finite differences; liquid endpoint derivatives replaced by marginal utility of endpoint resources. `VahF/VahB` finite differences; `VahF(:,J,:)=0`, `VahB(:,1,:)=0`. |
| 124-130 | `C_B/C_F=max(Vb,1e-6)^(-1/ga)`; `l_B/l_F=(max(Vb,1e-6)*(1-tau)*w*z/alphal)^frisch_l`; `sc_B/sc_F=(1-tau)wzl+Tt+Rb*b-C`. |
| 131-136 | `Ic_B=(sc_B<-1e-12)`; `Ic_F=(sc_F>1e-12)*(1-Ic_B)`; otherwise `Ic_0`; select `C,l`; flow utility `u=C^(1-ga)/(1-ga)-alphal*l^(1+1/frisch_l)/(1+1/frisch_l)` because `alphac=1`. |
| 137-140 | Four bare-`a` `HANK3_FOC` calls: `dhBB=(VahB,VbB)`, `dhBF=(VahF,VbB)`, `dhFB=(VahB,VbF)`, `dhFF=(VahF,VbF)`. `HANK3_FOC.m:19` uses the threshold times raw `a/chi1`. |
| 141-147 | `dh_B` combines positive `dhBF` and negative `dhBB`; `dh_F` combines positive `dhFF` and negative `dhFB`. At `a=0`, retain only positive forward-`a` candidates. At `a=a_max`, retain only negative backward-`a` candidates. At joint lower `b,a`, `dh_B=max(dh_B,0)`. |
| 148-154 | `sdh=-d-HANK3_cost(d,a)`; `Idh_F=(sdh_F>1e-12)`; `Idh_B=(sdh_B<-1e-12)*(1-Idh_F)`; lower `b` disables `Idh_B`; upper `b` forces `Idh_B=1, Idh_F=0`; otherwise `Idh_0`. `HANK3_cost.m:22` retains `max(a,a_bar)` only in the quadratic denominator. |
| 155-188 | Liquid generator `BB`: backward contribution from `Ic_B*sc_B + Idh_B*sdh_B`; forward contribution from `Ic_F*sc_F + Idh_F*sdh_F`; rates are divided by `db` and assembled in MATLAB column-major `(b,a,z)` order. |
| 190-198 | Derivative-side illiquid controls: `dhB=Idh_B*dhBB+Idh_F*dhFB`, `dhF=Idh_B*dhBF+Idh_F*dhFF`; `MhB=min(dhB,0)`; `MhF=max(dhF,0)+Rah*a`; at `a_max`, `MhB=dhB+Rah*a_max`, `MhF=0`; divide by `dah`. |
| 199-232 | Assemble `AAH` from `MhB/MhF`; form `A=BB+AAH+Bswitch`. No candidate Hamiltonian enumeration, multiplier recovery, or KKT veto appears. |
| 240-245 | Implicit HJB update uses selected flow `u` and `A`; not executed in this task. |
| 262-264 | Final selected `dh=Idh_B*dh_B+Idh_F*dh_F`; liquid drift `s=(1-tau)wzl+Rb*b+Tt-dh-cost-C`; illiquid drift `mh=dh+Rah*a`. Thus `Idh_0` means `d=0`, not `mh=0`. |
| 265-332 | Final `BB` and `AAH` rates are reconstructed directly from signs of `s` and `mh`; no KKT/candidate veto is applied. |

The auxiliary line 90 expression is preserved as source provenance but is outside the bounded local policy parity object because the manifest supplies `baseline_labor` after the initialization root. The evidence is therefore explicitly labeled `MATLAB_SOURCE_EXTRACTED_LOCAL_POLICY_PARITY`, not native/full-HJB execution.

## MATLAB branch matrix

| Branch | Derivative/control rule | Return and drift | Boundary/selection rule | MATLAB multiplier/KKT veto |
|---|---|---|---|---|
| Interior `a`, interior `b` | Four FOCs; build `dh_B` from `BF+/BB-`, `dh_F` from `FF+/FB-` | `Rah`; final `mh=d+Rah*a` | `Idh_F` first, then `Idh_B`, else `Idh_0` | None |
| Lower `a=0` | `dh_B=dhBF` only if positive; `dh_F=dhFF` only if positive; bare-`a` makes all FOC transfers zero | `raah(0)=rah` finite limit; `Rah*a=0` | lower-`a` overrides lines 142,146; joint lower `b,a` clips `dh_B>=0` | None |
| Upper `a=a_max` | `dh_B=dhBB` only if negative; `dh_F=dhFB` only if negative | `raah=0.9*rah`; derivative-side `MhB=dhB+Rah*a_max`, `MhF=0` | upper-`a` overrides lines 143,147,194-195 | None |
| Lower `b=b_min` | ordinary `Ic` construction; `Idh_B=0` | state-dependent `Rb`; final drifts unchanged | explicit transfer/backward-liquid constraint at line 152; no separate `Ic_B` override | None |
| Upper `b=b_max` | ordinary `Ic`; force `Idh_B=1`, `Idh_F=0` | state-dependent `Rb`; selected `d_B` | line 153 | None |
| Positive transfer | normally selected from positive `dh_B` when its `sdh_B<0` | all `mu_a` use `Rah*a+d` | `Idh_B`, subject to liquid boundaries | None |
| Negative transfer | normally selected from negative `dh_F` when its `sdh_F>0` | all `mu_a` use `Rah*a+d` | `Idh_F`, unless upper `b` overrides | None |
| Zero transfer | no qualifying `Idh_B/F`; `d=0` | `mu_a=Rah*a`, generally nonzero away from `a=0` | `Idh_0` | None |
| Negative liquid drift | selected `Ic_B*sc_B` plus transfer-cost `Idh_B*sdh_B` | backward rate `-mu_b/db` | strict `<-1e-12` | None |
| Positive liquid drift | selected `Ic_F*sc_F` plus `Idh_F*sdh_F` | forward rate `mu_b/db` | strict `>1e-12`, after `Ic_B` priority | None |
| Zero liquid drift | neither sign indicator | zero rate | `Ic_0`/zero combined drift | None |
| Negative/positive illiquid drift | selected transfer plus tapered `Rah*a` | backward/forward rate by sign; derivative-side HJB `AAH` uses lines 190-198 | exact lower/upper-`a` overrides above | None |

The frozen 11-case manifest reached `Ic_B`, `Ic_F`, `Ic_0`, `Idh_B`, `Idh_F`, `Idh_0`, lower/upper asset boundaries, below/at/above `a_bar`, negative `b`, both liquid boundaries, positive/negative/zero transfer, and positive/negative/zero drift directions.

## Corrected-track mechanism disposition

| Existing corrected/reference mechanism | Required classification | Source-based disposition |
|---|---|---|
| Hamiltonian candidate enumeration and winner selection | `CORRECTED_TRACK_REFERENCE_ONLY` | MATLAB directly applies `Ic/Idh` indicator algebra and never enumerates/vetoes candidate Hamiltonians. |
| Endogenous zero-illiquid-drift candidate `d=-r_a*a` | `CORRECTED_TRACK_REFERENCE_ONLY` | MATLAB `Idh_0` sets `d=0`; it does not impose `mu_a=0`. No constant- or tapered-return zero-drift candidate exists in the source selector. |
| Lower/upper state constraints as a concept | `MATLAB_FAITHFUL_EQUIVALENT_REQUIRED` | Faithful route must reproduce lines 142-147, 152-153, and 194-195 exactly, not corrected candidate formulas. |
| Separate corrected lower/upper state-constraint candidate objects | `CORRECTED_TRACK_REFERENCE_ONLY` | MATLAB realizes constraints through direct indicator/array overrides. |
| Corrected dual/upper-corner root helpers | `CORRECTED_TRACK_REFERENCE_ONLY` | No separate MATLAB upper-corner root or candidate selection exists. |
| Multiplier recovery | `MATLAB_FAITHFUL_DIAGNOSTIC_ONLY` | No multiplier is recovered for MATLAB production selection. It may be observed after selection but cannot veto it. |
| KKT residual certification/veto | `MATLAB_FAITHFUL_DIAGNOSTIC_ONLY` | No equivalent veto exists in the designated production block; faithful selection must not be rejected or replaced by corrected KKT diagnostics. |
| Lower-`b` F/Z canonicalization | `CORRECTED_TRACK_REFERENCE_ONLY` | MATLAB uses the explicit `Idh_B(1,:,:)=0` override and has no F/Z alias canonicalization. |
| `max(a,a_bar)` shadow/KKT relations | `CORRECTED_TRACK_REFERENCE_ONLY` | MATLAB uses bare `a` in FOC and the floor only in `HANK3_cost`; it has no matching shadow reconstruction. |
| `max(a,a_bar)` adjustment-cost denominator floor | `MATLAB_FAITHFUL_EQUIVALENT_REQUIRED` | Exact `HANK3_cost` production formula. |

`OWNER_PROVENANCE_REQUIRED`: none. The designated source plus frozen Owner authority resolved every disposition needed for this bounded local path.

## Production architecture and threading audit

New production module:

`src/ch5_two_asset_hank/matlab_faithful_policy.py`

It exposes the immutable `MatlabFaithfulLocalPolicy` result and `select_matlab_faithful_local_policy`. The selector:

- calls production bare-`a` `transfer_candidate` for all four MATLAB FOCs;
- calls `matlab_faithful_illiquid_return` and never duplicates the taper coefficient/formula;
- calls `asset_drifts_matlab_faithful` for final drifts and accepted adjustment-cost plumbing;
- passes explicit `a_max`, `da`, `db`, boundary flags, transfer income, and borrowing-rate gap;
- uses the tapered effective return in derivative-side `AAH` rates and final `mu_a` for every branch;
- implements MATLAB's strict `1e-12` indicator rules and `1e-6` derivative floor;
- contains no KKT veto, multiplier recovery, candidate Hamiltonian enumeration, route flag, global switch, or environment selector.

The transfer-income term is threaded through the accepted drift helper by passing `consumption-transfer_income`, algebraically preserving its unchanged liquid-budget implementation. The corrected/reference `policies.py`, `boundaries.py`, and all historical tests remain unchanged. `solve_hjb` still imports and uses the corrected/reference `select_policy`; no driver switch occurred.

## Frozen local parity identities and provenance

Successor artifact root:

`D:\ProjectTemp\ch5-matlab-faithful-hjb-policy-local-parity-20260830-001`

Frozen before any scientific case execution:

| Object | SHA-256 |
|---|---|
| `case_manifest.json` | `873028F52F329DEBA292484B5525129642FB0A386A01A42D2B4C19039AB7B157` |
| `matlab_local_policy_evaluator.m` | `8AA8E0A5EBFCEF136813FF1A880DE8C96BE63D5B958BC947EEE6D8EEBADAC8EA` |
| faithful selector source | `95D74893BAD22082FB1C731AD4E35E19A69039DFC30B477F7AAACC54ED3F446E` |
| `python_local_policy_runner.py` | `0310C08BFF16E8D71ED372B5460D2D8EDD33212B1BC341E1C2C295DEE99DFB86` |
| `compare_local_policy.py` | `6A96A188A471787E00068E2D6BAA479BB654B712CF89161C78685D812AEB84C8` |
| pre-execution `execution_ledger.json` | `E770B6396885A5400BC8C55469F195110DC26109E6DFC40ADCF85F976F35229C` |

The MATLAB evaluator is external and does not modify designated source. It source-extracts exact formulas from `HANK_2ASSETS_HJB.m:79-87,124-198,262-267` and directly calls the designated `HANK3_FOC` and `HANK3_cost`. Evidence label:

`MATLAB_SOURCE_EXTRACTED_LOCAL_POLICY_PARITY`

An empty-case MATLAB container/serialization preflight returned `[]` before freeze and evaluated no scientific case.

## Scientific call ledger and comparison

| Scientific action | Calls | Budget | Result/output SHA-256 |
|---|---:|---:|---|
| MATLAB local policy batch | 1 | 1 | PASS, 11 rows; `8317CD5E616F197531778E515B797E71AB3E2175FD1C25DBBEA17E8F8EA64B37` |
| Python faithful local batch | 1 | 1 | PASS, 11 rows; `448B07F842259B03E38C212D9951733CA05FB299B1F6996270CF3DAD01AB7F66` |
| Frozen comparator | 1 | 1 | PASS; `B8630A9D0576BEC5C9CA9D71BE784C43A1146A43DF3D09CD09A5FF16880C8A9D` |

No batch or comparator was rerun. Cases, formulas, branches, and tolerance were not changed after freeze.

Comparison rule was frozen as `128*eps64*max(1,abs(x),abs(y))`, with exact equality required for transfer and categorical values.

| Continuous field | Maximum absolute difference | Worst case |
|---|---:|---|
| consumption | 0 | none |
| labor | 0 | none |
| transfer | 0 | none |
| adjustment cost | 0 | none |
| effective illiquid return | 0 | none |
| `mu_a` | 0 | none |
| `mu_b` | 0 | none |
| utility | 0 | none |
| local backward/forward `b` rates | 0 / 0 | none |
| local backward/forward `a` rates | 0 / 0 | none |

Categorical mismatch counts:

- liquid upwind label: `0`;
- transfer/illiquid FOC label: `0`;
- liquid drift direction: `0`;
- illiquid drift direction: `0`.

Complete mismatch/failure list: empty.

## Verification, scope, and closeout

Allowed checks executed:

- static compilation of production selector, Python runner, and comparator: PASS;
- static selector import: `STATIC_IMPORT_PASS`;
- empty-case MATLAB evaluator/container preflight: PASS;
- frozen local MATLAB/Python/comparator sequence: PASS as recorded above;
- predecessor primitive regressions only: `pytest -q tests/test_economics_boundaries.py tests/test_matlab_faithful_taper.py` -> `18 passed in 0.64s`;
- final `py_compile` and `git diff --check`: PASS.

Repository changed paths are exactly:

- `src/ch5_two_asset_hank/matlab_faithful_policy.py`;
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_REPORT.md`.

Not modified: `economics.py`, `policies.py`, `boundaries.py`, `contracts.py`, `generator.py`, `hjb.py`, KFE, steady state, existing tests, or any MATLAB source.

Not executed: full pytest, converged/full HJB, R4, corrected D1/D2/D3, KFE, steady state, asset-tail, transition, IRF, dynamics, calibration, or Results.

Pre-publication git status contains only the two authorized paths above. Final clean status and GitHub read-back are publication evidence recorded in the executor handoff.

Acceptance level: exact local MATLAB-faithful policy/upwind construction and source-extracted same-input parity only. It does not claim full HJB convergence/operator parity or authorize KFE, steady state, or dynamics.

The only recommended next gate is **MATLAB-faithful full HJB driver integration and converged same-input HJB/operator parity**.

`MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_PASS`
