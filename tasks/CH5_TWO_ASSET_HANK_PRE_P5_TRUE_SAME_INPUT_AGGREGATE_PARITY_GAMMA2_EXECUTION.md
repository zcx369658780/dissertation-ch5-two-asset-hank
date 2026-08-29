# CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_EXECUTION

## Task

Execute the final true same-input aggregate parity experiment for the two-asset HA household block using a common curvature that both accepted implementations can represent without adding a third scientific adapter.

The predecessor adapter-design task established:

- MATLAB O1 test-only low-`a` FOC adapter: PASS;
- Python O2 test-only common-productivity operator adapter: PASS;
- the only remaining blocker was the previously frozen `gamma_c/ga=1.0`, because the accepted MATLAB main HJB implements CRRA as `C^(1-ga)/(1-ga)` without a log-utility branch.

The Owner's goal is same-input integration parity, not preservation of `gamma=1` specifically. Therefore this task resolves the blocker by **refreezing the common fixture at `gamma_c=ga=2.0`**, which is natively representable by both accepted utility implementations.

Do **not** add a MATLAB log-utility adapter. Do **not** modify either production source tree.

This task authorizes exactly one four-run scientific execution if all pre-scientific gates pass.

It does not itself issue P5 acceptance and does not authorize dynamics, AR(1), transition, IRF, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted predecessor evidence

Fresh-read live GitHub `main`.

Accepted Python scientific source baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Accepted P1-P4 numerical evidence:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Predecessor adapter design/conformance report commit:

`c849c48dd78518dd22ffed20e6c3d9125bdd9488`

Predecessor adapter task commit:

`4c0afddfa93aeb082b55b3612a522fe25f4a0301`

Accepted MATLAB source identities:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- production `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

P1-P4 must not be rerun.

## Required live GitHub read-back

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_SAME_INPUT_PARITY_ADAPTER_DESIGN_AND_CONFORMANCE_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_REPORT.md`
- accepted Python `economics.py`, `contracts.py`, `hjb.py`, `generator.py`, `kfe.py`, `policies.py`, `boundaries.py`, indexing and diagnostics used by the run.

Verify Python `src/tests` remain scientifically unchanged from `7a2388a2ba89073e307f05a909570e8c40a4be13`. If not, stop:

`BLOCKED_GAMMA2_TRUE_SAME_INPUT_PARITY_PYTHON_SOURCE_DRIFT`

## Scientific resolution of the `ga=1` blocker

Freeze the common curvature at:

`gamma_c = ga = 2.0`

Reason:

- accepted Python production flow utility already supports generic CRRA `gamma_c != 1`;
- accepted MATLAB production main directly supports `ga=2` through its existing CRRA formula;
- this avoids introducing any new main-HJB scientific adapter beyond the already accepted O1/O2 test-only bridges;
- the objective is to validate same-input HJB -> generator -> KFE -> aggregate integration, so `gamma=2` is a valid common test point.

Before scientific execution, prove on representative positive consumption values that MATLAB and Python CRRA consumption utility at curvature `2.0` are numerically identical to machine precision, and prove the consumption FOC mapping is the same common equation.

If any material utility/FOC mismatch remains, stop:

`BLOCKED_GAMMA2_TRUE_SAME_INPUT_PARITY_UTILITY_MAPPING`

Do not change curvature after execution begins.

## Frozen common economic fixture

Use exactly:

- `rho = 0.05`
- `gamma_c / ga = 2.0`
- Python labor curvature `phi = 1.0`
- MATLAB `frisch_l = 1.0`
- scalar labor weight / MATLAB corresponding labor coefficient = `1.0`
- `chi_0 = 0.05`
- `chi_1 = 1.0`
- `a_bar = 0.5`
- `r_b = 0.03`
- wage `w = 1.0`
- `tau = 0.0`
- migration cost `0.0`
- external transfer `Tt = 0.0`
- `rb_gap = 0.0`
- neutral domestic fixed-cost bookkeeping fields `fixcost = 0.0`, `fixcost2 = 0.0`
- baseline `r_a / rah = 0.040`
- perturbation `r_a / rah = 0.041`

No province-specific or cache-derived economic input may be used.

## Frozen common grids

Use exactly:

`a = [0.0, 0.5, 1.0, 1.5, 2.0]`

`b = [0.0, 1.25, 2.5, 3.75, 5.0]`

`z = [0.8, 1.3]`

State count:

`5 x 5 x 2 = 50`

Frozen common productivity generator:

```text
Q_z_common =
[[-0.4,  0.4],
 [ 0.3, -0.3]]
```

Asset spacings:

- `da = 0.5`
- `db = 1.25`
- finite-state cell weight `da*db = 0.625`

Productivity is a finite Markov state; use no continuous-`z` quadrature factor.

## Authorized test-only adapters

Exactly two scientific adapters are authorized, both already conformance-tested in the predecessor report.

### Adapter A — MATLAB O1 low-a FOC

Production files remain unchanged.

Use an external temporary `HANK3_FOC.m` whose only scientifically material domestic change is:

`a -> max(a,a_bar)`

The future execution must recreate or reuse an artifact exactly equivalent to the predecessor conformance adapter and record its bytes/SHA-256 and complete diff against production.

Path resolution must prove before execution:

- `HANK_2ASSETS_HJB` -> accepted original main;
- `HANK3_cost` -> accepted original cost helper;
- `HANK3_FOC` -> temporary O1-corrected helper.

No MATLAB main-HJB utility modification is authorized.

### Adapter B — Python O2 common-Q operator

Do not modify repository source.

Runtime-rebind only:

`ch5_two_asset_hank.hjb.build_operator`

to an external adapter that:

- calls production `_asset_generator` unchanged for `G_a`;
- calls production `_asset_generator` unchanged for `G_b`;
- injects exact `G_z = kron(Q_z_common, I_25)`;
- returns the normal production `OperatorBundle`;
- restores the original binding in `finally`.

All other Python HJB logic remains production:

- `compute_derivatives`
- `select_policy`
- policy candidates / KKT / boundary logic
- implicit HJB solve
- HJB residual
- convergence logic
- production KFE

## Initialization parity

The accepted MATLAB main constructs its own initial value before HJB iteration. At `ga=2` that initialization is finite.

Before scientific execution:

1. reproduce the MATLAB initialization externally from the exact common fixture without calling the HJB solver;
2. map MATLAB `[b,a,z]` to Python `[a,b,z]`;
3. use that mapped common initial value as the Python `initial_value` for both rates if and only if it is exactly reconstructible from the accepted MATLAB formula and common fixture;
4. prove the common initial value is finite and identical across the two rates.

If the initialization cannot be reconstructed unambiguously, stop:

`BLOCKED_GAMMA2_TRUE_SAME_INPUT_PARITY_INITIALIZATION_MAPPING`

Do not substitute the prior R4 initial value.

## Numerical settings

Freeze common settings before execution:

- maximum HJB iterations `500`
- change tolerance `1e-8`
- pseudo-time / Delta `10`
- HJB residual acceptance `1e-7`
- generator validity `1e-11`
- drift-zero threshold `1e-12`
- KKT acceptance `1e-7`
- KFE stationarity/normalization `1e-10`
- nonnegative mass tolerance `1e-12`

Use semantic mappings proven in the predecessor report.

Do not tune after seeing any scientific output.

## Common measure and aggregate semantics

Convert each stationary object to the same probability mass `m` satisfying:

`sum(m) = 1`

with common finite-state cell weight `0.625` for density-to-mass conversion.

Report:

- `C_hh = sum(mass * c)`
- raw hours `H_hh = sum(mass * l)`
- effective labor `L_hh = sum(mass * z * l)`
- `A_hh = sum(mass * a)`
- `B_hh = sum(mass * b)`

MATLAB native `Lt` is effective labor and may be compared only with Python `sum(mass*z*l)`.

Also independently recompute all MATLAB aggregates from its mapped raw policy/mass arrays under the common measure rather than relying only on stored scalars.

## Pre-scientific gates

Before any scientific HJB/KFE solve:

1. verify all live/source identities;
2. verify only one report commit was added by the predecessor task;
3. freeze the complete gamma2 common manifest;
4. prove `GridSpec` accepts the 50-state common grid;
5. prove MATLAB `ga=2` utility and Python `gamma_c=2` utility/consumption FOC match at representative values;
6. re-establish MATLAB O1 adapter conformance and path resolution without calling HJB;
7. re-establish Python O2 adapter sparse-matrix conformance without calling `solve_hjb`;
8. prove exact common `Q_z_common` and orientation;
9. reconstruct and prove the common initial value mapping;
10. verify finite-state measure and aggregation code;
11. run synthetic persistence/serialization preflight for all four outputs;
12. freeze/hash all external harnesses and adapters.

No scientific model solve during preflight.

If any gate fails, stop fail-closed and do not partially execute one implementation.

## Scientific execution budget

If and only if every pre-scientific gate passes, execute exactly four scientific runs:

1. MATLAB common baseline `rah=0.040` — once;
2. Python common baseline `r_a=0.040` — once;
3. MATLAB common perturbation `rah=0.041` — once;
4. Python common perturbation `r_a=0.041` — once.

Immediately persist and read back each completed output before entering the next scientific run.

At any failure after scientific execution starts:

- stop fail-closed;
- do not edit the frozen harness/adapters;
- do not rerun a consumed rate;
- do not tune any scientific or numerical input.

## Required validity diagnostics

For every completed run report where available:

- HJB convergence flag, iterations, iteration change, residual;
- KKT/boundary residual;
- generator row-sum and minimum off-diagonal;
- stationary/KFE residual;
- normalization error;
- minimum mass and negative count;
- finite checks;
- MATLAB source-exposed diagnostics plus independently computed common diagnostics.

A run that violates its accepted validity contract cannot be used for parity.

## Required pointwise parity diagnostics

For each `r_a`, after applying the accepted `[b,a,z] <-> [a,b,z]` orientation adapter, compare:

- value function where semantically common;
- `c(a,b,z)`;
- raw labor `l(a,b,z)`;
- effective labor `z*l`;
- transfer `d`;
- adjustment cost;
- `mu_a`;
- `mu_b`;
- stationary probability mass;
- available policy/direction classes.

Report maximum absolute differences and mismatch counts.

Do not hide structured pointwise mismatch behind aggregate cancellation.

## Frozen parity tolerances

Freeze these before execution and do not widen them:

For each aggregate level `C_hh`, `H_hh`, `L_hh`, `A_hh`, `B_hh`:

`abs(MATLAB - Python) <= 1e-6 * max(1, abs(MATLAB), abs(Python))`

For mapped stationary probability mass:

`max_abs(m_M - m_P) <= 1e-6`

For each response delta between `0.041` and `0.040`:

`abs(delta_M - delta_P) <= 1e-6 * max(1, abs(delta_M), abs(delta_P))`

Pointwise diagnostics do not have a new ad hoc tolerance; report exact maxima and interpret them against the accepted structural O1-O12 set. Any material unexplained structured discrepancy blocks P5 even if aggregates happen to pass.

## Required result tables

### Levels

| implementation | r_a | C_hh | H_hh | L_hh | A_hh | B_hh |
|---|---:|---:|---:|---:|---:|---:|
| MATLAB | 0.040 | ... | ... | ... | ... | ... |
| Python | 0.040 | ... | ... | ... | ... | ... |
| MATLAB | 0.041 | ... | ... | ... | ... | ... |
| Python | 0.041 | ... | ... | ... | ... | ... |

### Responses

For both implementations report:

- `Delta C_hh`, `%Delta C_hh`
- `Delta H_hh`, `%Delta H_hh`
- `Delta L_hh`, `%Delta L_hh`
- `Delta A_hh`
- `Delta B_hh`

Then report MATLAB-Python level differences and delta differences with explicit tolerance evaluation.

## Terminal classification

Return exactly one:

- `TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_PASS__P5_OWNER_ACCEPTANCE_RECOMMENDED`
- `TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_NEEDS_DIAGNOSTIC__P5_BLOCKED`
- `TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_BLOCKED_SOURCE_OR_ENVIRONMENT`

Use PASS only if:

- all four scientific runs complete;
- all validity diagnostics pass;
- common economic and numerical inputs are proven identical;
- only the authorized O1/O2 adapters are active;
- aggregate levels and response deltas pass frozen tolerances;
- stationary mass passes its frozen tolerance;
- no material unexplained structured pointwise discrepancy remains.

Do not issue P5 acceptance in this task.

## Output report

Write exactly one repository report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_EXECUTION_REPORT.md`

The report must include:

- live/source identities;
- gamma2 scientific-resolution rationale;
- complete common manifest;
- utility/FOC conformance proof;
- adapter hashes/diffs/path/binding proofs;
- initialization mapping proof;
- persistence preflight;
- exact run counts;
- all validity diagnostics;
- complete pointwise parity diagnostics;
- levels and response tables;
- all frozen tolerance evaluations;
- terminal classification;
- forbidden-operation check;
- P5 recommendation or next diagnostic blocker.

## Commit/push authorization

Only the report may be added to the repository.

If and only if it is the sole repository change:

- stage only the report;
- create one commit;
- fresh-fetch remote `main`;
- fast-forward push only if remote `main` has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Run gamma2 true same-input HA aggregate parity`

## Forbidden operations

Do not:

- modify accepted MATLAB production main/helpers;
- modify Python `src/tests`;
- add a MATLAB log-utility adapter;
- activate any scientific adapter beyond O1/O2 described above;
- use province/cache economic inputs;
- rerun P1-P4;
- tune fixture, curvature, grids, Q, initialization, equations, tolerances, or parity bounds after scientific execution starts;
- rerun a consumed scientific rate;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, dynamics, or Results;
- merge, rebase, reset, or force-push.

## Recommended successor

If terminal classification is `TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_PASS__P5_OWNER_ACCEPTANCE_RECOMMENDED`, the next and only HA gate should be:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

If parity is scientifically valid but fails, publish a narrow diagnostic task. Do not silently repair the current execution.