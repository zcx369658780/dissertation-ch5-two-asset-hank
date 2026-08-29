# CH5_TWO_ASSET_HANK_PRE_P5_SAME_INPUT_PARITY_ADAPTER_DESIGN_AND_CONFORMANCE

## Task

Resolve the two production-interface blockers discovered by the failed true same-input aggregate parity preflight, without modifying either accepted production source tree and without running any scientific HJB/KFE solve.

The Owner still requires one final same-input aggregate integration test before P5. The previous attempt proved that an unchanged-native direct invocation is impossible because:

1. accepted Python `GridSpec` requires `a[0] == 0`, while the previous fixture started at `a=0.5`;
2. accepted original MATLAB `HANK_2ASSETS_HJB.m` hard-codes exactly two productivity states and cannot consume `Nz=9` / arbitrary `9x9 Q_z` through its unchanged interface.

These are interface incompatibilities, not parity failures.

The scientifically authorized route for the successor experiment is therefore a **test-only parity-adapter integration fixture** using only two already accepted structural exceptions:

- O1: MATLAB low-`a` transfer FOC is a legacy limitation and must not be inherited; the accepted common equation uses `m(a)=max(a,a_bar)`;
- O2: productivity representation differs; a common finite-state productivity operator may be injected through an explicit adapter for parity.

This task prepares and audits those adapters. It does not execute the final four scientific runs.

## Repository and accepted evidence

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Fresh-read live GitHub `main`.

Accepted Python scientific source baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Accepted P1-P4 evidence:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Latest failed same-input preflight report:

`1435176971de0bee1b7426482d8cfc18452dc130`

Accepted Owner structural audit must remain authoritative, especially O1 and O2:

`docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`

Do not rerun P1-P4.

## Required live read-back

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_REPORT.md`
- accepted Python `contracts.py`, `economics.py`, `policies.py`, `boundaries.py`, `generator.py`, `productivity.py`, `hjb.py`, `kfe.py`, `kfe_contract.py`, `indexing.py`, and diagnostics used by R4.

Verify `src/tests` are unchanged from the accepted Python baseline. Stop on drift:

`BLOCKED_SAME_INPUT_PARITY_ADAPTER_PYTHON_SOURCE_DRIFT`

## MATLAB source identities

Read-only verify:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

No file in the designated MATLAB tree may be modified.

## Frozen successor common fixture

Prepare the following exact common fixture for the later execution task.

### Economic parameters

- `rho = 0.05`
- `gamma_c / ga = 1.0`
- `phi / frisch mapping = 1.0`
- `chi_0 = 0.05`
- `chi_1 = 1.0`
- `a_bar = 0.5`
- `r_b = 0.03`
- `w = 1.0`
- `tau = 0.0`
- migration cost = `0.0`
- scalar labor weight = `1.0`
- external transfer = `0.0`
- `rb_gap = 0.0`
- baseline `r_a / rah = 0.040`
- perturbation `r_a / rah = 0.041`

### Common grids

Use only grids both unchanged interfaces can represent:

- `a = [0.0, 0.5, 1.0, 1.5, 2.0]`
- `b = [0.0, 1.25, 2.5, 3.75, 5.0]`
- `z = [0.8, 1.3]`

State count: `5 x 5 x 2 = 50`.

This deliberately satisfies Python `a[0]==0` and MATLAB `Nz==2`.

### Common productivity generator

Reuse the already accepted P3 common finite-state generator:

```text
Q_z_common = [
  [-0.4,  0.4],
  [ 0.3, -0.3]
]
```

This exact matrix must be used by both implementations in the successor execution.

MATLAB may receive it directly as its two-state `la_mat`.

Python production `build_z_generator` must **not** be called for this adapter fixture because accepted O2 explicitly treats the native reflected diffusion and MATLAB two-state chain as different objects. The Python test-only adapter must inject this exact `Q_z_common` while leaving asset drifts, policy selection, HJB iteration, residual logic, and KFE logic unchanged.

## Adapter A — MATLAB O1 FOC correction, test-only

Create an external temporary helper with the same function signature expected by the accepted original HJB.

It must be a copy of the accepted `HANK3_FOC.m` with the **only scientifically material domestic-branch change**:

`a` scale -> `max(a,a_bar)`

so the domestic transfer FOC exactly matches the accepted equation and Python `economics.transfer_candidate` below `a_bar`.

Requirements:

- accepted original `HANK_2ASSETS_HJB.m` remains byte-identical and is the main HJB executed later;
- accepted original `HANK3_cost.m` remains byte-identical;
- the test-only corrected FOC helper must be outside the production tree;
- MATLAB path resolution for the successor must intentionally resolve the temporary corrected helper and the accepted original main HJB/cost helper;
- produce a complete textual diff against accepted `HANK3_FOC.m`;
- prove no foreign-branch or unrelated formula change is introduced unless the accepted HJB actually enters it; domestic scalar HA is the intended route;
- analytically/numerically verify the corrected helper equals the accepted Python transfer FOC at representative `a=0`, `0<a<a_bar`, `a=a_bar`, and `a>a_bar` derivative pairs without solving HJB.

If a one-line/strictly bounded O1 correction cannot be isolated, stop:

`BLOCKED_SAME_INPUT_PARITY_ADAPTER_MATLAB_O1_NOT_ISOLATABLE`

## Adapter B — Python common-Qz operator injection, test-only

Do not modify Python production source.

Prepare an external adapter that allows accepted production `solve_hjb` to use the exact common two-state `Q_z_common` by replacing only the runtime `build_operator` binding used inside `hjb.py`.

The adapter must:

- use accepted production asset-generator logic for `G_a` and `G_b` without reimplementing policy/drift formulas;
- construct `G_z = kron(Q_z_common, I_{a*b})` using the accepted canonical orientation/indexing;
- return the same `OperatorBundle` contract with the same generator diagnostics;
- leave `compute_derivatives`, `select_policy`, implicit HJB matrix solve, HJB residual calculation, convergence rules, KKT logic, and all policy formulas byte-for-byte production implementations;
- leave KFE production solver and transpose contract unchanged;
- never call production `build_z_generator` in the successor common fixture;
- prove on a synthetic policy object that the injected operator's `G_a` and `G_b` are exactly equal to production asset-generator outputs and that `G_z` equals the frozen P3 common `Q_z` block under the accepted orientation adapter.

The report must explicitly state which runtime name is rebound, when, and that no repository source is written.

If this cannot be done without changing scientific logic beyond the O2 productivity adapter, stop:

`BLOCKED_SAME_INPUT_PARITY_ADAPTER_PYTHON_O2_NOT_ISOLATABLE`

## Common measure and aggregate semantics

Prepare a single common measure contract for the later execution.

Productivity is a finite Markov state. Do not multiply by a continuous-z quadrature weight.

Asset spacing:

- `da = 0.5`
- `db = 1.25`

For a density representation, probability-cell mass is `density * da * db`; after conversion require `sum(mass)=1`.

Common aggregates:

- `C_hh = sum(mass * c)`
- raw hours `H_hh = sum(mass * l)`
- effective labor `L_hh = sum(mass * z * l)`
- `A_hh = sum(mass * a)`
- `B_hh = sum(mass * b)`

MATLAB `Lt` is effective labor. The successor parity comparison must compare MATLAB `Lt` with Python `sum(mass*z*l)`, not Python raw hours.

## Initialization and numerical-map audit

Without solving the model, audit how accepted MATLAB initializes its HJB from `results_in` and how accepted Python receives `initial_value`.

The successor experiment does not require byte-identical iterative initialization if the two production interfaces cannot express the same initialization, but the report must:

- document both exact initial-value constructions;
- identify whether a common logical initial value can be represented through external inputs without source modification;
- if yes, freeze that common initialization;
- if no, classify initialization as an implementation-level numerical detail and justify why the converged fixed-point comparison remains valid under the existing HJB residual/convergence tolerances.

Any scientifically material unresolved field required by MATLAB or Python blocks execution:

`BLOCKED_SAME_INPUT_PARITY_ADAPTER_UNRESOLVED_REQUIRED_INPUT`

## Numerical settings for successor

Prepare semantically common settings:

- max iterations `500`
- change tolerance `1e-8`
- HJB residual acceptance `1e-7`
- generator tolerance `1e-11`
- drift tolerance `1e-12`
- KKT tolerance `1e-7`
- KFE stationarity/normalization `1e-10`
- nonnegative mass tolerance `1e-12`
- pseudo-time/Delta `10` if both interfaces map this quantity semantically; otherwise document exact discrepancy before execution authority is issued.

Do not tune values.

## No scientific solve in this task

Allowed:

- source reads;
- exact hashes;
- external adapter creation;
- static/synthetic unit-style adapter checks;
- path-resolution checks that do not invoke HJB/KFE;
- serialization/persistence preflight;
- common manifest creation.

Forbidden:

- any MATLAB HJB call;
- any Python `solve_hjb` call;
- any KFE solve;
- any P1-P4 rerun;
- any production source/test edit.

## Required report

Write exactly one repository report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_SAME_INPUT_PARITY_ADAPTER_DESIGN_AND_CONFORMANCE_REPORT.md`

The report must contain:

- live/source identities;
- exact reason unchanged-native true same-input execution is impossible;
- full frozen 50-state common manifest;
- exact `Q_z_common`;
- MATLAB corrected-helper full diff and conformance checks;
- Python operator-adapter implementation description/hash and synthetic conformance checks;
- path/runtime binding proof;
- common measure and labor semantics;
- MATLAB/Python required-field mapping;
- initialization audit;
- numerical-setting mapping;
- persistence/serialization preflight;
- proof no scientific solve occurred;
- one terminal classification;
- exact successor execution contract if READY.

## Terminal classification

Return exactly one:

- `SAME_INPUT_PARITY_ADAPTER_READY_FOR_EXECUTION`
- `SAME_INPUT_PARITY_ADAPTER_BLOCKED_MATLAB`
- `SAME_INPUT_PARITY_ADAPTER_BLOCKED_PYTHON`
- `SAME_INPUT_PARITY_ADAPTER_BLOCKED_UNRESOLVED_MAPPING`

Use READY only if both adapters are isolated to the already accepted O1/O2 differences, all common economic inputs are frozen, the common measure/labor mapping is resolved, and no production file change is required.

## Successor execution contract if READY

The next task, and only the next task, may authorize exactly four one-shot scientific solves on the frozen 50-state common fixture:

1. MATLAB `r_a=0.040` using accepted original HJB + accepted original cost helper + test-only O1-corrected FOC helper + exact `Q_z_common`;
2. Python `r_a=0.040` using accepted production HJB/policies/KKT/KFE + test-only O2 common-Qz operator adapter;
3. MATLAB `r_a=0.041` under identical non-`r_a` inputs;
4. Python `r_a=0.041` under identical non-`r_a` inputs.

The successor must persist each output immediately and compare pointwise policies, mass, `C_hh`, `H_hh`, effective `L_hh`, `A_hh`, `B_hh`, and response deltas using pre-authorized tolerances.

This design task does not issue that execution authority.

## Commit/push authorization

Only the report may be added to the repository.

If and only if the report is the sole repository change, commit once and fast-forward push after fresh remote verification.

Suggested commit subject:

`Prepare same-input HA parity adapters`

## Forbidden operations

Do not:

- modify accepted MATLAB production source/helpers;
- modify Python `src` or tests;
- run any scientific HJB/KFE/model solve;
- alter the frozen common fixture after adapter checks;
- silently treat test-only adapters as production source;
- rerun P1-P4;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, dynamics, or Results;
- merge, rebase, reset, or force-push.
