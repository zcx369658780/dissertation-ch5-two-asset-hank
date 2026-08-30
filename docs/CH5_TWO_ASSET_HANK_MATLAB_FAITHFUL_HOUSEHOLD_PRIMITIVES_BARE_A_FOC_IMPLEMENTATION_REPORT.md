# Chapter 5 Two-Asset HANK MATLAB-faithful household primitives bare-a FOC implementation report

## Terminal classification

`MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_PASS`

The production household transfer primitive now implements the designated MATLAB bare-`a` FOC. The adjustment-cost denominator floor remains unchanged, and the prior corrected-equation max-scale candidate remains available under an explicit reference-only helper. Targeted primitive verification passed. This task does not establish faithful taper, HJB, generator, KFE, steady-state, or dynamics parity.

## Live authority and source identity

- Live start `origin/main`: `9057696483c1dce3d970f137b33c5958ba03c0d6`.
- Start branch/HEAD after fast-forward: `codex/ch5-adjustment-boundary-redesign` / `9057696483c1dce3d970f137b33c5958ba03c0d6`.
- Primary authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Primitive authority: `MATLAB_FAITHFUL_TRANSFER_FOC_USES_BARE_A`.
- Final `origin/main` immediately before publication: `9057696483c1dce3d970f137b33c5958ba03c0d6`; the publication commit is recorded by push/read-back and final handoff.

Designated MATLAB sources were verified before mutation:

| Source | SHA-256 | Exact authority |
|---|---|---|
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | `(min(pa./pb - 1 + chi0,0) + max(pa./pb - 1 - chi0,0)).*a/chi1` |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | `chi0.*abs(d) + chi1.*d.^2/2.*(max(a,a_bar)).^(-1)` |

The hashes and formulas matched exactly. MATLAB sources were not modified.

## Production implementation

Authorized production file: `src/ch5_two_asset_hank/economics.py`.

The public production function retains its signature and validation but now uses raw `a`:

```diff
 def transfer_candidate(v_a, v_b, a, params):
+    """Return the production MATLAB-faithful bare-a transfer candidate."""
     if not np.isfinite([v_a, v_b, a]).all() or v_b <= 0:
         raise ValueError(...)
     q = v_a / v_b - 1.0
     threshold = min(q + params.chi_0, 0.0) + max(q - params.chi_0, 0.0)
-    return max(a, params.a_bar) * threshold / params.chi_1
+    return a * threshold / params.chi_1
```

Historical corrected-equation behavior was not erased. It was moved under the explicit reference helper:

```python
def transfer_candidate_corrected_max_scale(v_a, v_b, a, params):
    """Retain the historical corrected-equation max-scale reference candidate."""
    ...
    return max(a, params.a_bar) * threshold / params.chi_1
```

The helper preserves the same finite-input and positive-`v_b` fail-closed validation. No route flag, environment selector, mutable global, or hidden configuration was added.

`adjustment_cost` was not changed. It continues to use:

```python
scale = np.maximum(np.asarray(a, dtype=float), params.a_bar)
return chi_0 * abs(d) + 0.5 * chi_1 * d**2 / scale
```

Thus `max(a,a_bar)` remains only the authorized numerical denominator floor on this primitive surface.

## Test split and exact results

Authorized test file: `tests/test_economics_boundaries.py`.

The former coupled `test_adjustment_cost_and_foc_share_frozen_max_scale` was split rather than deleted:

1. `test_adjustment_cost_retains_matlab_denominator_floor` independently preserves the cost-floor evidence.
2. `test_matlab_faithful_transfer_candidate_uses_bare_a_positive_branch` covers `a=0`, `0<a<a_bar`, and `a=a_bar`.
3. `test_matlab_faithful_transfer_candidate_uses_bare_a_negative_branch` covers the negative-threshold branch.
4. `test_corrected_max_scale_reference_preserves_historical_foc_evidence` explicitly retains corrected-track behavior at `a=0` and `a<a_bar` and proves it differs from faithful production behavior when the threshold is nonzero.

With `chi_0=0.1`, `chi_1=2`, and `a_bar=0.5`:

| Branch/input | `a` | Faithful result | Corrected reference result |
|---|---:|---:|---:|
| `v_a=1.5`, `v_b=1.0`, threshold `0.4` | `0.0` | `0.0` | `0.1` |
| same positive branch | `0.25` | `0.05` | `0.1` |
| same positive branch | `0.5` | `0.1` | `0.1` |
| `v_a=0.5`, `v_b=1.0`, threshold `-0.4` | `0.25` | `-0.05` | not required |

The faithful below-floor values scale linearly with raw `a`; the corrected reference continues to use the `a_bar` floor.

## Static propagation audit

Direct `transfer_candidate` call sites in `src/ch5_two_asset_hank/policies.py`:

- line 136, `_controls_from_shadow_values`: `transfer_candidate(v_a, shadow_b, a, params)`;
- line 526, candidate enumeration in `select_policy`: `transfer_candidate(v_a, v_b, a, params)`.

Neither requires a signature change. Both receive `a` from the intended illiquid state grid. `GridSpec` requires `a[0]==0` and a uniform ordered grid, and the faithful economic domain is `a>=0`; no intended direct call supplies negative `a`.

Corrected-track max-scale algebra deliberately deferred to the future faithful HJB/policy audit:

- `policies.py:247` — interior-zero-illiquid shadow reconstruction;
- `policies.py:300` — dual-upper shadow reconstruction;
- `policies.py:365` — upper-a/lower-b corner reconstruction;
- `policies.py:429` — upper-a/interior-b reconstruction;
- `policies.py:448` — budget-root scale;
- `boundaries.py:85` — multiplier scale;
- `boundaries.py:146` — KKT transfer stationarity scale.

None was modified. This primitive propagation does not constitute faithful HJB or policy parity acceptance.

## Verification

Allowed checks only were executed:

- `python -m py_compile src/ch5_two_asset_hank/economics.py tests/test_economics_boundaries.py`: PASS.
- Static import with repository `PYTHONPATH=src`: `STATIC_IMPORT_PASS`.
- `pytest -q tests/test_economics_boundaries.py`: `10 passed in 0.92s`.
- Primitive-only pointwise micro-check: matched every table value above.

An initial standalone import probe without `PYTHONPATH=src` returned `ModuleNotFoundError`; it imported no model and was immediately resolved by using the repository's standard source path. The required static import then passed. Pytest was not rerun.

The full test suite was not run.

## Scope and closeout

Changed paths:

- `src/ch5_two_asset_hank/economics.py`;
- `tests/test_economics_boundaries.py`;
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_REPORT.md`.

Not modified: MATLAB, `policies.py`, `boundaries.py`, `generator.py`, `kfe.py`, `steady_state.py`, or any other production/test path.

Not executed: full pytest, HJB, policy scientific fixtures, taper/generator parity, KFE, steady state, D1/D2/D3, asset-tail, transition, IRF, dynamics, calibration extension, or Results.

Acceptance level: the MATLAB-faithful bare-`a` household transfer primitive and preserved corrected-track reference helper are accepted at the primitive-only level. Faithful taper integration, HJB/policy parity, generator parity, KFE, steady state, and dynamics remain unaccepted.

Exact recommended next gate: only **MATLAB `raah` illiquid-return taper implementation and drift/generator plumbing audit**. Do not authorize HJB, KFE, steady state, or dynamics yet.
