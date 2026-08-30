# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Implement only the first bounded production change under the newly accepted MATLAB-faithful reconstruction route: restore the designated MATLAB **bare-`a` transfer FOC** while preserving the already-aligned adjustment-cost denominator floor `max(a,a_bar)`.

This task must also split/reclassify the existing corrected-equation primitive regression so that the prior `max(a,a_bar)` FOC behavior remains preserved as historical corrected-track reference evidence rather than being deleted.

This task stops before `raah` taper implementation, HJB/policy parity, generator changes, KFE, steady state, or dynamics.

Controlling accepted report:

`docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`

Accepted terminal:

`MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_PASS`

Primary authority marker:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Supporting marker for this task:

`MATLAB_FAITHFUL_TRANSFER_FOC_USES_BARE_A`

Historical corrected-equation evidence remains:

`CORRECTED_EQUATION_RECONSTRUCTION_TRACK_ACCEPTED_REFERENCE_EVIDENCE`

Historical P5 scope remains:

`P5_ACCEPTED_FOR_CORRECTED_EQUATION_TRACK_NOT_FINAL_MATLAB_FAITHFUL_PARITY`

## 2. Live authority and continuity

Task-authoring parent observed before publication:

`32c697af4fc8aacbabdc2de1b023e3c07fac0e54`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and the controlling audit report exist on live `main`;
3. record live start SHA;
4. verify the MATLAB-faithful authority markers above;
5. verify designated MATLAB hashes before modification;
6. record repository worktree status;
7. do not start from uncommitted scientific source changes.

## 3. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- designated MATLAB `HANK3_FOC.m`
- designated MATLAB `HANK3_cost.m`
- `src/ch5_two_asset_hank/economics.py`
- `tests/test_economics_boundaries.py`
- static call sites of `transfer_candidate` in `src/ch5_two_asset_hank/policies.py`

Do not modify `policies.py` in this task.

## 4. Designated MATLAB authority to verify

Designated MATLAB root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Required hashes:

- `HANK3_FOC.m` SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `HANK3_cost.m` SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`

Verify the exact designated formulas.

Adjustment cost:

```matlab
chi0.*abs(d) + chi1.*d.^2/2.*(max(a,a_bar)).^(-1)
```

Transfer FOC:

```matlab
(min(pa./pb - 1 + chi0,0) + max(pa./pb - 1 - chi0,0)).*a/chi1
```

Freeze the interpretation:

- `max(a,a_bar)` is retained **only as the numerical denominator floor in adjustment cost**;
- the faithful transfer FOC scales by the raw illiquid asset `a`;
- at `a=0`, the direct faithful transfer candidate is exactly zero;
- liquid-asset borrowing/domain logic is outside this mutation and must remain unchanged.

If the designated source/hash/formula does not match, stop before source mutation and return BLOCKED.

## 5. Current Python starting point

Current `src/ch5_two_asset_hank/economics.py` contains:

```python
def adjustment_cost(...):
    scale = np.maximum(np.asarray(a, dtype=float), params.a_bar)
    ... / scale
```

This is already faithful and must remain semantically unchanged.

Current transfer candidate contains the corrected-track scaling:

```python
return max(a, params.a_bar) * threshold / params.chi_1
```

This is the sole direct primitive production gap authorized for correction here.

The current `tests/test_economics_boundaries.py` couples the two assumptions in:

`test_adjustment_cost_and_foc_share_frozen_max_scale`

This test must be split/reclassified rather than deleted.

## 6. Required production implementation

Modify only the bounded household primitive surface.

### 6.1 Faithful production `transfer_candidate`

The existing public/production name:

`transfer_candidate`

must become the MATLAB-faithful bare-`a` implementation.

Preserve all existing finite-input and `v_b>0` fail-closed validation unless an exact source-level reason requires otherwise.

The faithful numerical expression must be equivalent to:

```python
q = v_a / v_b - 1.0
threshold = min(q + params.chi_0, 0.0) + max(q - params.chi_0, 0.0)
return a * threshold / params.chi_1
```

Do not replace raw `a` by `abs(a)`, `max(a,0)`, `max(a,a_bar)`, or any other regularization.

Do not change `adjustment_cost` denominator-floor behavior.

### 6.2 Preserve corrected-equation reference helper

Do not erase the previously accepted corrected-equation primitive.

Introduce an explicitly named reference helper in `economics.py`, preferably:

`transfer_candidate_corrected_max_scale`

or another equally unambiguous name approved by the existing module style.

It must reproduce the exact prior behavior:

```python
max(a, params.a_bar) * threshold / params.chi_1
```

It is historical/reference-only evidence and must not silently become the faithful production function.

Add a concise docstring/comment that distinguishes:

- production MATLAB-faithful bare-`a` behavior;
- corrected-equation max-scale reference behavior.

Do not add a broad mode flag, environment switch, mutable global route selector, or hidden configuration in this task. Keep the two primitives explicit.

## 7. Test split and required cases

Update/split `tests/test_economics_boundaries.py` so the old coupled test no longer asserts that faithful FOC and cost share the same max scale.

### 7.1 Cost-floor faithful test

Retain the existing denominator-floor fact independently:

```python
adjustment_cost(2.0, 0.0, PARAMS) == adjustment_cost(2.0, PARAMS.a_bar, PARAMS)
```

This test must not infer anything about the FOC scale.

### 7.2 Faithful bare-`a` FOC tests

Using the existing test parameterization where possible, establish exact/source-backed behavior at minimum for:

- `a=0` -> faithful `transfer_candidate(...) == 0`;
- one `0<a<a_bar` case;
- `a=a_bar`;
- one positive-threshold branch;
- one negative-threshold branch.

For example with existing `PARAMS` (`chi_0=0.1`, `chi_1=2`, `a_bar=0.5`):

For `v_a=1.5`, `v_b=1.0`, threshold is `0.4`, so expected faithful values include:

- `a=0.0` -> `0.0`;
- `a=0.25` -> `0.05`;
- `a=0.5` -> `0.10`.

For `v_a=0.5`, `v_b=1.0`, threshold is `-0.4`, so `a=0.25` -> `-0.05`.

Use exact/isclose assertions consistent with existing test style; do not introduce loose tolerances.

### 7.3 Corrected-track regression test

Retain the old max-scale FOC behavior explicitly against the new corrected-reference helper.

At minimum prove that for `a=0` and `a<a_bar`, the corrected helper still uses `a_bar` scaling and therefore differs from the faithful production helper when the threshold is nonzero.

The test name must make its historical scope explicit, e.g. contain `corrected_track` or `corrected_max_scale_reference`.

Do not delete the corrected-track regression simply because it is no longer final faithful authority.

## 8. Static propagation audit only

Because `policies.py` imports/calls `transfer_candidate`, the primitive change will become the input to the future faithful HJB route.

In this task:

- statically list every direct `transfer_candidate` call site;
- confirm no call site supplies a negative illiquid state `a` under the intended faithful state domain;
- report which policy/corner/KKT routines still contain corrected-track `max(a,a_bar)` algebra requiring the later faithful HJB/policy audit;
- do **not** modify those routines here;
- do **not** claim full HJB faithfulness from this primitive task.

If a direct call site requires a different signature to adopt bare-`a`, stop and report rather than broadening scope.

## 9. Authorized files

Production source mutation is limited to:

- `src/ch5_two_asset_hank/economics.py`

Test mutation is limited to:

- `tests/test_economics_boundaries.py`

A new narrowly named primitive-only test file may be added only if strictly necessary; prefer splitting the existing file to minimize change.

Required report may be added under `docs/` as specified below.

No other production/test path is authorized for mutation.

## 10. Verification and execution budget

Allowed execution is primitive-only.

Required:

1. Python static compilation/import check for the modified module/test;
2. targeted test execution:

```text
pytest -q tests/test_economics_boundaries.py
```

3. optional direct primitive-only micro-checks if needed to record the exact faithful/corrected outputs above.

Do not run:

- full test suite;
- HJB solver;
- policy fixture reruns beyond the targeted primitive test file;
- generator scientific parity;
- KFE;
- steady state;
- D1/D2/D3;
- taper tests (not implemented yet);
- dynamics/IRF.

If the targeted primitive tests expose failures caused by out-of-scope HJB/policy assumptions, do not broaden the task; report them for the next faithful HJB gate.

## 11. Acceptance requirements

Use PASS only if all are true:

- designated MATLAB hashes/formulas match;
- `adjustment_cost` retains the same denominator floor behavior;
- production `transfer_candidate` uses bare `a` exactly;
- at `a=0`, faithful candidate is exactly zero for nonzero threshold input;
- below `a_bar`, faithful candidate scales linearly with raw `a`;
- corrected max-scale behavior remains available under an explicit reference helper;
- corrected-track regression test remains preserved/reclassified;
- targeted primitive tests pass;
- no unauthorized production/test file changes;
- no taper/HJB/generator/KFE/steady-state/dynamics execution or mutation occurs.

This task does **not** accept faithful HJB parity, faithful taper integration, faithful KFE, or faithful steady state.

## 12. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_REPORT.md`

Report at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. designated MATLAB hashes/formulas;
4. exact production diff;
5. exact test diff/split;
6. faithful bare-`a` pointwise results at `a=0`, `0<a<a_bar`, and `a=a_bar`;
7. positive/negative threshold branch results;
8. corrected-reference helper pointwise regression results;
9. targeted pytest command/result;
10. static `transfer_candidate` call-site list;
11. list of deferred max-scale policy/KKT/corner surfaces for the future HJB audit;
12. changed-path list;
13. statement that taper/HJB/generator/KFE/steady state/D1-D3/dynamics were not executed or modified;
14. git status;
15. acceptance level;
16. exact recommended next gate.

## 13. Terminal classifications

Return exactly one.

### PASS

`MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_PASS`

### BLOCKED

`MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_BLOCKED`

Use BLOCKED if the designated source conflicts, the primitive change cannot remain within authorized files/semantics, or targeted primitive tests expose an unresolved out-of-scope dependency that prevents safe primitive acceptance.

## 14. Next gate boundary

If PASS, recommend only the next faithful implementation gate:

**MATLAB `raah` illiquid-return taper implementation and drift/generator plumbing audit.**

Do not authorize HJB parity, KFE, steady state, or dynamics from this task alone.
