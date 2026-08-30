# Chapter 5 Two-Asset HANK MATLAB-Faithful Illiquid-Return Taper and Drift/Generator Plumbing Report

Date: 2026-08-30

Terminal classification:

`MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_PASS`

## Authority and start state

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Execution worktree: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`
- Branch: `codex/ch5-adjustment-boundary-redesign`
- Fresh-fetched live start `origin/main`: `15f64253f1fd705520e2565b61d9f558802b3cc3`
- Pre-publication final `origin/main`: `15f64253f1fd705520e2565b61d9f558802b3cc3`; the publication commit and GitHub read-back are recorded in the executor handoff because a commit cannot embed its own SHA.
- Start worktree: clean.
- Accepted predecessor was present: `MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_PASS`.
- Governing authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Taper authority: `MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`.

The required rules, both controlling reports, designated MATLAB source, and the task-listed Python source/test surfaces were read before mutation.

## Designated MATLAB verification

Designated file:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

Observed SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

This exactly matches the task authority. The verified source chain is:

- line 81: `raah = rah.*(1 - 0.1*(ahmax./ah).^(-9));`
- lines 82–87: `raah` is broadcast/placed into effective-return array `Rah`;
- lines 193–194 and 264: the illiquid drift uses `Rah.*aaah`.

No MATLAB file was modified or executed.

## Authorized implementation

Only `src/ch5_two_asset_hank/economics.py` was changed in production source.

The new vectorized helper `matlab_faithful_illiquid_return(a, a_max, r_a)` implements exactly:

```python
r_a * (1.0 - 0.1 * (a / a_max) ** 9)
```

It validates finite inputs, `a_max > 0`, and the designated finite-grid domain `0 <= a <= a_max`. It introduces no `a_bar`, epsilon, route flag, global switch, or altered coefficient/exponent.

The new explicit helper `asset_drifts_matlab_faithful(..., a_max)` retains the existing adjustment-cost and labor/liquid-budget expressions and changes only the illiquid return term:

```python
r_a_effective = float(matlab_faithful_illiquid_return(a, a_max, inputs.r_a))
mu_a = r_a_effective * a + transfer
```

The historical corrected/reference `asset_drifts` remains available and unchanged with constant `inputs.r_a * a`. The predecessor production `transfer_candidate` still uses bare `a`, while `adjustment_cost` independently retains `maximum(a, a_bar)` as its denominator floor. Neither predecessor expression was altered.

## Taper and drift evidence

With `r_a=0.04` and `a_max=2.0`:

| `a` | faithful effective return | required value |
|---:|---:|---:|
| 0.0 | 0.04 | 0.04 |
| 1.0 | 0.0399921875 | `0.04*(1-0.1*0.5^9)` |
| 2.0 | 0.036000000000000004 | `0.9*0.04` |

For positive vector `[0.25, 0.5, 1.0, 2.0]`, comparison against direct evaluation of `0.04*(1-0.1*(2.0/a)^(-9))` produced maximum absolute difference `0.0`.

For the controlled drift fixture `a=1.0`, `b=-0.5`, `z=1.0`, consumption `0.8`, labor `[0.4]`, transfer `0.2`, and `a_max=2.0`:

- corrected/reference constant-return result: `mu_a=0.24000000000000002`, `mu_b=-0.39`, cost `0.06000000000000001`;
- MATLAB-faithful result: `mu_a=0.2399921875`, `mu_b=-0.39`, cost `0.06000000000000001`.

Thus only the illiquid-return contribution changes; `mu_b` and adjustment cost are exactly unchanged.

## Generator plumbing evidence

The micro-test used uniform grids `a=[0,1,2]`, `b=[-1,0]`, and `z=[0.5,1.0,1.5]`. The upper-`a` transfer neutralized outward boundary drift. At selected interior node `(a,b,z)=(1,-1,0.5)` with `da=1`:

- supplied faithful `mu_a`: `0.0399921875` (positive, hence forward in `a`);
- expected rate `abs(mu_a)/da`: `0.0399921875`;
- observed forward `g_a` rate: `0.0399921875`;
- observed generator linear action on the illiquid coordinate: `0.0399921875`;
- maximum absolute `g_a` row sum: `0.0`.

Static source inspection also confirmed that `generator.py` contains neither the faithful helper name nor the frozen taper coefficient. The generator consumes the supplied drift without duplicating taper logic, and `generator.py` was unchanged.

## Static HJB/policy propagation audit

`policies.py` was read only. Direct `asset_drifts` call sites requiring migration together in a future faithful HJB task occur at lines approximately 152, 160, 181, 221, 284, 342, 411, 531, 567, 606, 649, and 696.

Direct constant-return constructions using `-inputs.r_a * a` occur in:

- `_interior_zero_illiquid_controls` near line 211;
- `_dual_upper_corner_controls` near line 274;
- `_upper_a_lower_b_controls` near line 332;
- `_upper_a_interior_b_controls` near line 401;
- candidate fallback near line 529.

These zero-drift, boundary, corner, root, and fallback paths depend on the illiquid return and must be audited and migrated consistently. The listed helpers and `select_policy` currently lack `a_max`, so the future HJB task must thread the upper-grid bound explicitly rather than partially switching call sites.

Deferred corrected-track max-scale shadow/KKT/corner surfaces remain in `policies.py` near lines 247, 300, 365, 429, and 448 and in `boundaries.py` near lines 85 and 146. They require the separately authorized faithful HJB/policy audit. Partial HJB integration would be unsafe because drift, zero-drift, corner, root, shadow, and KKT algebra must move together.

This primitive implementation does not establish or claim HJB faithfulness.

## Verification record

Executed only static and taper/drift/generator-micro checks:

```text
python -m py_compile src/ch5_two_asset_hank/economics.py tests/test_matlab_faithful_taper.py
python -c "from ch5_two_asset_hank.economics import ..."
pytest -q tests/test_matlab_faithful_taper.py tests/test_economics_boundaries.py
pytest -q tests/test_matlab_faithful_taper.py
```

Results:

- static compilation: PASS;
- static import: `STATIC_IMPORT_PASS`;
- initial combined targeted run: predecessor economics boundaries `10/10 PASS`; new taper file had `7 PASS / 1 FAIL` because the synthetic generator fixture used `N_z=2` while the frozen productivity generator requires `N_z>=3`;
- bounded fixture-only correction: changed synthetic `z` grid to three points; no scientific equation, tolerance, or production source changed;
- final new-file rerun: `8 passed in 0.66s`;
- `git diff --check`: PASS (only Git's informational LF/CRLF warning appeared).

A subsequent read-only report-value extraction script first had an unclosed parenthesis and exited at Python parse time; the corrected primitive-only extraction then passed. No model solver or scientific workflow was started by that syntax-error attempt.

## Scope and changed paths

Changed paths are exactly:

- `src/ch5_two_asset_hank/economics.py`
- `tests/test_matlab_faithful_taper.py`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_REPORT.md`

No mutation occurred in `policies.py`, `boundaries.py`, `contracts.py`, `generator.py`, KFE, steady state, or MATLAB. No full pytest suite, HJB, policy fixture scientific rerun, KFE, steady state, D1/D2/D3, asset-tail, transition, IRF, dynamics, calibration extension, or Results execution occurred.

Pre-publication git status contains only the three authorized paths above. Final clean status and GitHub read-back are publication-layer evidence recorded in the executor handoff.

## Acceptance and next gate

Acceptance level is primitive-only MATLAB-faithful taper/drift implementation plus directional generator-plumbing evidence. It does not accept HJB/policy parity, KFE, steady state, asset-tail, or dynamics.

The only recommended next gate is **MATLAB-faithful HJB/policy integration and parity audit**, including consistent taper threading through every policy/root/corner path and the deferred max-scale shadow/KKT/corner algebra.

`MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_PASS`
