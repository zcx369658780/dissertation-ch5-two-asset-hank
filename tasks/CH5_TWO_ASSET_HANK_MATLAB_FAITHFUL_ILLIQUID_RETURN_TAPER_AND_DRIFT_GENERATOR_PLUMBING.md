# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Implement and freeze the second bounded production primitive under the MATLAB-faithful reconstruction route: the designated MATLAB illiquid-return upper-grid taper

```matlab
raah = rah.*(1 - 0.1*(ahmax./ah).^(-9));
```

and prove, without running the HJB, that the resulting faithful illiquid drift can be consumed unchanged by the already-aligned directional asset generator.

This task must **not** yet switch the full HJB/policy system to the faithful taper. The current policy/corner/KKT system still contains corrected-track algebra that requires a separate bounded HJB/policy audit. The objective here is to establish an explicit faithful taper primitive, an explicit faithful drift primitive, and a verified drift-to-generator plumbing contract that the next HJB task can safely adopt.

Controlling accepted reports:

- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_REPORT.md`

Accepted predecessor terminal:

`MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_PASS`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Required taper marker:

`MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`

Historical corrected-equation evidence remains:

`CORRECTED_EQUATION_RECONSTRUCTION_TRACK_ACCEPTED_REFERENCE_EVIDENCE`

## 2. Live authority and continuity

Task-authoring parent observed before publication:

`1b5f4b6d820b52e52ea16e1030d29f52d80aecee`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and both controlling reports exist on live `main`;
3. record live start SHA;
4. verify the MATLAB-faithful authority markers;
5. verify designated MATLAB source identity before source mutation;
6. confirm the predecessor bare-`a` FOC implementation is present and unchanged;
7. record worktree status and do not start from uncommitted scientific source changes.

## 3. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- the two controlling reports above
- designated MATLAB `HANK_2ASSETS_HJB.m`
- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/generator.py`
- `tests/test_generators_and_kfe_contract.py`
- `tests/test_economics_boundaries.py`

Do not modify `policies.py`, `contracts.py`, or `generator.py` in this task unless the static audit proves a source-level plumbing contradiction that makes the bounded faithful primitive impossible. If that happens, stop and return BLOCKED rather than broadening scope.

## 4. Designated MATLAB authority

Designated MATLAB root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Required source:

- `HANK_2ASSETS_HJB.m` SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

Verify the exact relevant source chain, including at minimum:

```matlab
raah = rah.*(1 - 0.1*(ahmax./ah).^(-9));
```

its broadcast/placement into the effective illiquid-return array `Rah`, and the actual illiquid drift terms using the effective return multiplied by the illiquid asset grid.

The faithful numerical contract is:

`MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`

Interpretation:

- `rah` / current Python `r_a` remains the economic/base illiquid return parameter;
- the taper is a numerical finite-grid stabilization, not a structural economic state-dependent-return claim;
- the faithful numerical effective return depends on the current illiquid grid location and `a_max`;
- coefficient `0.1`, exponent `-9`, and upper-grid scale are frozen;
- the faithful implementation must reproduce MATLAB values on the designated nonnegative illiquid grid.

Do not redesign the taper.

## 5. Exact lower-bound interpretation

The MATLAB expression contains `ahmax./ah`. At the economic lower bound `a=0`, MATLAB floating-point evaluation yields an infinite ratio and therefore a zero value after raising that ratio to power `-9`, so the taper factor tends to one.

For the faithful Python primitive, the algebraically equivalent nonnegative-grid expression

```text
r_a_eff(a) = r_a * (1 - 0.1 * (a / a_max)^9)
```

is authorized because, for `a>0`,

```text
(a_max/a)^(-9) = (a/a_max)^9
```

and at `a=0` it directly gives the same finite MATLAB limit `r_a_eff(0)=r_a` without divide-by-zero warnings.

Do not introduce any extra epsilon floor in `a`, do not reuse `a_bar`, and do not alter the coefficient or exponent.

## 6. Current Python starting point

Current `HouseholdInputs.r_a` is a scalar base return.

Current corrected/reference drift primitive in `economics.py` is:

```python
mu_a = inputs.r_a * a + transfer
```

The gap audit classified this as insufficient for final MATLAB-faithful production because the effective return taper is absent.

Current `generator._asset_generator` already converts an externally supplied drift into forward/backward transition rates using the grid spacing. The gap audit classified this directional drift-to-rate plumbing as aligned and not requiring redesign.

Therefore this task should add a faithful taper/drift primitive while leaving the existing generator algorithm unchanged.

## 7. Required faithful taper primitive

Modify `src/ch5_two_asset_hank/economics.py` to add an explicit vectorizable helper with an unambiguous faithful name, preferably:

`matlab_faithful_illiquid_return`

or an equally clear name consistent with module style.

Required semantic inputs:

- illiquid asset level(s) `a`;
- illiquid upper-grid bound `a_max`;
- base illiquid return `r_a`.

Required semantics:

```python
r_eff = r_a * (1.0 - 0.1 * (a / a_max) ** 9)
```

with validations limited to faithful domain requirements:

- finite `a`, `a_max`, `r_a`;
- `a_max > 0`;
- `a >= 0`;
- `a <= a_max` for the designated finite-grid helper.

Return scalar/array behavior may follow existing NumPy style, but pointwise values must match the MATLAB contract to machine precision.

At minimum prove:

- `a=0` -> `r_eff=r_a`;
- `a=a_max` -> `r_eff=0.9*r_a`;
- one strict interior point matches the MATLAB formula;
- a vector of positive grid points matches direct evaluation of the designated formula.

Do not use `a_bar` in this helper.

## 8. Required faithful drift primitive

Add an explicit faithful drift helper in `economics.py`, preferably:

`asset_drifts_matlab_faithful`

or an equally unambiguous name.

It must preserve the existing budget/cost/labor-income calculations and differ from the corrected/reference `asset_drifts` only in the illiquid-return term:

```text
mu_b = unchanged existing expression
cost = unchanged existing adjustment_cost
mu_a = r_a_eff(a,a_max) * a + transfer
```

The helper must accept the required `a_max` explicitly. Do not hide the grid dependence in a global variable, environment flag, or mutable route selector.

The current `asset_drifts` constant-`r_a` behavior must remain available as corrected-track/reference behavior in this task. Do not silently rewrite every existing call site yet.

Add concise documentation distinguishing:

- MATLAB-faithful tapered drift;
- historical corrected/reference constant-return drift.

## 9. Drift/generator plumbing verification

Do not modify `generator.py` if the static audit confirms the gap report.

Establish with a narrow test that the already-existing generator consumes a faithful tapered `mu_a` exactly as an externally supplied drift.

The test must use a small valid uniform `GridSpec`, create a synthetic `PolicySnapshot` or equivalent existing test helper with a `mu_a` field derived from the faithful taper/drift primitive, and verify at minimum:

1. the sign/direction of the generated `g_a` transition agrees with the faithful `mu_a`;
2. the transition rate equals `|mu_a| / da` at a selected interior asset node;
3. the generator's linear action on the illiquid coordinate reproduces the supplied faithful drift where the drift is admissible;
4. no taper logic is duplicated inside `generator.py`;
5. row-sum/conservative behavior remains unchanged.

Use a transfer/drift fixture that avoids illegal outward drift at computational boundaries. Do not change generator tolerance to make the test pass.

## 10. Static HJB propagation audit only

Read `policies.py` and report, without mutation:

- every direct `asset_drifts` call site that a future faithful HJB task must migrate to the tapered drift;
- every direct use of `inputs.r_a * a` or algebraically equivalent constant-return expression in policy/corner/root construction;
- which zero-drift/boundary/corner candidates depend on the illiquid return and therefore must be audited together when the taper is wired into HJB;
- whether any helper currently lacks access to `a_max` and will require explicit argument threading in the next HJB task.

Do not partially wire the taper into only some policy branches in this task.

The report must explicitly state that a partial HJB integration would be unsafe because corner/zero-drift algebra must move consistently.

## 11. Corrected-track preservation

Do not delete or rewrite historical corrected-equation tests/evidence.

The existing constant-`r_a` `asset_drifts` behavior remains corrected/reference evidence until the future faithful HJB route has explicit entry points.

If a test currently asserts constant-`r_a` behavior, either:

- leave it untouched and classify it as corrected/reference regression; or
- if a narrow new faithful test is required, add a clearly named faithful test alongside it.

Do not make old corrected-track fixtures falsely claim final faithful acceptance.

## 12. Authorized files

Production source mutation is limited to:

- `src/ch5_two_asset_hank/economics.py`

Test mutation is limited to one or both of:

- `tests/test_economics_boundaries.py`
- `tests/test_generators_and_kfe_contract.py`

A new narrowly named `tests/test_matlab_faithful_taper.py` may be added if that produces a cleaner separation; prefer the smallest clear change.

Required report may be added under `docs/`.

No mutation is authorized in:

- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/generator.py`
- KFE/steady-state modules.

## 13. Verification and execution budget

Allowed execution is taper/drift/generator-micro only.

Required:

1. Python static compilation/import check for modified/new files;
2. targeted faithful taper/drift tests;
3. targeted generator plumbing test;
4. rerun `tests/test_economics_boundaries.py` only if it is modified or needed to prove the predecessor bare-`a` primitive remains intact.

Do not run the full test suite.

Do not run:

- HJB solver;
- policy fixture scientific reruns;
- KFE;
- steady state;
- D1/D2/D3;
- asset-tail;
- transition/IRF/dynamics;
- calibration extension or Results.

If targeted tests expose an out-of-scope policy dependency, stop and report it rather than partially modifying HJB code.

## 14. Acceptance requirements

Use PASS only if all are true:

- designated MATLAB hash/formula and drift use are verified;
- faithful taper helper matches MATLAB pointwise, including `a=0`, interior, and `a=a_max`;
- no `a_bar`/epsilon regularization is introduced into the taper;
- faithful drift uses tapered effective return and preserves `mu_b`/cost exactly;
- corrected/reference constant-return drift remains available;
- generator source remains unchanged and consumes the faithful drift with exact directional/rate plumbing under the targeted fixture;
- the static HJB propagation audit identifies all deferred integration surfaces;
- predecessor bare-`a` FOC remains unchanged;
- only authorized paths changed;
- no HJB/KFE/steady-state/dynamics execution or mutation occurs.

This task does not accept faithful HJB policy parity or any stationary-distribution result.

## 15. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_REPORT.md`

Report at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. designated MATLAB hash and exact taper/drift source locations;
4. exact faithful taper implementation diff;
5. exact faithful drift implementation diff;
6. proof that predecessor bare-`a` FOC and adjustment-cost denominator floor remain unchanged;
7. taper pointwise table at `a=0`, at least one interior `a`, and `a=a_max`;
8. positive-vector MATLAB-formula parity result;
9. faithful-vs-constant-return drift comparison with unchanged `mu_b` and cost;
10. generator plumbing test inputs, expected/observed rate, direction, linear action, row sum;
11. targeted commands/results;
12. static `policies.py` propagation audit: all drift/constant-return call sites and missing `a_max` threading surfaces;
13. changed-path list;
14. statement that `policies.py`, `generator.py`, KFE, steady state, MATLAB, D1-D3, HJB, dynamics were not modified/executed;
15. git status;
16. acceptance level;
17. exact recommended next gate.

## 16. Terminal classifications

Return exactly one.

### PASS

`MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_PASS`

### BLOCKED

`MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_BLOCKED`

Use BLOCKED if the designated source conflicts, a faithful taper/drift helper cannot be implemented within the authorized primitive surface, generator plumbing is not actually source-aligned, or safe implementation requires partial HJB mutation.

## 17. Next gate boundary

If PASS, recommend only:

**MATLAB-faithful HJB/policy integration and parity audit**, including consistent taper threading through every policy/root/corner path and the deferred max-scale shadow/KKT/corner algebra.

Do not authorize KFE, steady state, asset-tail, or dynamics from this task alone.
