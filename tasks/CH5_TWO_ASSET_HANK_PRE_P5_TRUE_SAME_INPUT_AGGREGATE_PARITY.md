# CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY

## Task

Execute one final **true same-input aggregate parity test** for the two-asset HA household block before Owner P5 acceptance.

The Owner explicitly selected this route because the previous native robustness experiment compared different MATLAB/Python calibrations. This task therefore must **not** use the Jiangsu native snapshot as the scientific input object and must **not** compare two different native calibrations.

Instead, construct one synthetic but economically valid common household fixture from scratch, feed the same economic parameters, asset grids, productivity states/operator, prices, transfers, numerical tolerances, aggregation measure, and two `r_a` values to both accepted implementations, then compare the resulting household steady-state aggregates.

The goal is exactly:

> same household inputs -> MATLAB accepted HJB/KFE implementation vs Python accepted HJB/KFE implementation -> compare `C_hh`, effective `L_hh`, assets, stationary mass, and the `r_a: 0.040 -> 0.041` response.

This is a final supplementary parity/diagnostic gate. It does **not** itself issue Owner P5 acceptance and does not authorize dynamics, AR(1), transition, IRF, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted evidence and source identities

Fresh-read live GitHub `main` and preserve all accepted P1-P4 evidence.

Accepted Python scientific source baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Accepted P1-P4 numerical evidence commit:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Latest completed native-robustness report commit:

`e5271f3e218244fa77ec080b3e4a7005cfb1447d`

Accepted MATLAB source identities:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

Do not rerun P1-P4.

## Required live read-back

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_PYTHON_BOOLEAN_SERIALIZATION_CORRECTION_AND_CL_RA_COMPLETION_REPORT.md`
- accepted Python `economics.py`, `productivity.py`, `generator.py`, `hjb.py`, `kfe.py`, `contracts.py`, `policies.py`, `boundaries.py`, and relevant indexing/diagnostic code.

Verify live Python `src/tests` remains scientifically unchanged from the accepted baseline. If not, stop:

`BLOCKED_TRUE_SAME_INPUT_AGGREGATE_PYTHON_SOURCE_DRIFT`

## Important correction to prior aggregate semantics

The accepted MATLAB source defines:

`Lt = sum(zzz .* l .* g * dah * db, 'all')`

so MATLAB `Lt` is **effective labor**, not raw hours.

The accepted Python pointwise labor object returned by `labor_from_vb` is raw labor/hours `l`; labor income multiplies it by productivity `z`.

Therefore this task must report both:

- raw hours:
  `H_hh = sum(mass * l)`
- effective labor, the object comparable to MATLAB `Lt`:
  `L_hh = sum(mass * z * l)`

**The parity comparison for `L_hh` must use effective labor on both sides.**

Do not compare MATLAB `Lt` with Python `sum(mass*l)`.

## Common fixture design principle

This fixture is intentionally chosen so every `a` grid point satisfies `a >= a_bar`. This excludes the already accepted MATLAB low-`a` legacy transfer-FOC limitation from this particular aggregate test, allowing the test to focus on the common formula region.

This does not revoke or hide the accepted O1 low-`a` redesign decision. It is a controlled shared-formula aggregate fixture.

## Frozen common economic parameters

Use exactly:

- `rho = 0.05`
- consumption risk aversion / curvature: `gamma_c = 1.0`
- labor curvature: `phi = 1.0`
- `chi_0 = 0.05`
- `chi_1 = 1.0`
- `a_bar = 0.5`
- `r_b = 0.03`
- transfer/tax wedge `tau = 0.0`
- wage `w = 1.0`
- migration cost `0.0`
- scalar labor weight `1.0`
- no external transfer beyond the household budget objects already required by the accepted equations
- baseline `r_a = 0.040`
- perturbation `r_a = 0.041`

For the accepted Python productivity law use:

- `mu_z = 0.2`
- `sigma_z = 0.1`

No economic parameter may differ across MATLAB/Python.

## Frozen common grids

Use exactly:

### Illiquid asset

`a = [0.5, 1.0, 1.5, 2.0, 2.5]`

### Liquid asset

`b = [0.0, 1.25, 2.5, 3.75, 5.0]`

### Productivity

`z = linspace(0.5, 1.5, 9)`

Thus the common state space has:

`5 x 5 x 9 = 225` states.

All grids are identical across implementations.

## Frozen common productivity operator

Before any scientific solve, construct the `9 x 9` productivity backward generator `Q_z_common` **once** from the accepted Python production function:

`build_z_generator(common_grid, common_params)`

using the frozen `z`, `mu_z=0.2`, and `sigma_z=0.1` above.

Persist `Q_z_common` outside the repository with SHA-256 and full numerical contents.

MATLAB must use this exact `Q_z_common` as its exogenous productivity generator. Do not reconstruct a separate MATLAB productivity process from a different formula.

Python must independently call its accepted production `build_z_generator` during preflight and prove its resulting matrix is exactly/machine-identical to the frozen `Q_z_common`.

If the accepted original MATLAB HJB cannot accept an arbitrary `N_z=9` productivity grid/operator through its existing `grid/param` interface without production-source modification, stop before scientific execution:

`BLOCKED_TRUE_SAME_INPUT_AGGREGATE_MATLAB_PRODUCTIVITY_INTERFACE_INCOMPATIBLE`

Do not modify MATLAB production source to force compatibility.

## Common finite-state measure

For this diagnostic fixture, treat productivity as the finite Markov state represented by `Q_z_common`.

The common stationary probability cell measure must therefore use the same asset-cell measure on both sides and no separate continuous-`z` quadrature factor:

`cell_weight = da * db`

for every `(a,b,z)` state.

With the frozen uniform grids:

- `da = 0.5`
- `db = 1.25`
- common cell weight = `0.625`

MATLAB native density normalization and Python KFE `cell_weights` must both correspond to this same finite-state measure.

After conversion to probability mass `m`, require:

`sum(m) = 1` within the frozen normalization tolerance.

Do not use the Python R4 trapezoidal continuous-`z` quadrature in this common finite-state test.

## MATLAB common-input construction audit

Before scientific execution, read the accepted original `HANK_2ASSETS_HJB.m` and identify every field it reads from:

- `param`
- `grid`
- `num`
- `CHI`
- `results_in`

Construct these structures externally from the frozen common fixture only.

Do not use the 2016 Jiangsu cache as the economic input object.

A cache may be read only if needed to learn non-scientific field naming/schema, but no economic value may be copied from it unless that value is explicitly frozen above.

The common MATLAB tuple must contain no province-specific wage, tax, transfer, migration, asset return, productivity, or state value outside the frozen common fixture.

If the accepted source requires an additional scientifically material field not specified above and no unambiguous shared mapping exists, stop before execution:

`BLOCKED_TRUE_SAME_INPUT_AGGREGATE_UNRESOLVED_REQUIRED_INPUT`

Do not invent a value.

## Numerical settings

Use common semantically mapped HJB settings where both implementations expose them:

- max iterations `500`
- change tolerance `1e-8`
- HJB residual acceptance `1e-7`
- generator row-sum/off-diagonal acceptance `1e-11`
- drift zero tolerance `1e-12`
- KKT validity `1e-7`
- KFE stationarity/normalization `1e-10`
- nonnegative mass tolerance `1e-12`
- pseudo-time/Delta `10` if the MATLAB field is semantically the same object; otherwise record the exact mapping and stop if no defensible common setting exists.

No tolerance may be tuned after execution begins.

## Pre-scientific compatibility gate

Before any HJB solve:

1. verify MATLAB/Python source identities;
2. freeze the complete common economic manifest;
3. freeze grids and `Q_z_common` with SHA-256;
4. verify `a >= a_bar` at every common `a` point;
5. prove all MATLAB/Python economically mapped inputs are identical;
6. prove orientation adapter and state count `225`;
7. verify MATLAB can consume `N_z=9` and exact `Q_z_common` without source changes;
8. verify Python can construct the exact common grid and use the common finite-state KFE cell weights;
9. verify JSON/MAT persistence plumbing with synthetic outputs;
10. freeze all external harnesses.

No HJB/KFE/model solve may occur during this preflight.

If preflight fails, stop and report a named BLOCKED classification. Do not partially execute one implementation.

## Scientific execution budget

If and only if preflight passes, execute exactly four scientific solves:

1. MATLAB common baseline `r_a=0.040` — once;
2. Python common baseline `r_a=0.040` — once;
3. MATLAB common perturbation `r_a=0.041` — once;
4. Python common perturbation `r_a=0.041` — once.

The order may be paired by rate, but each is exactly once.

Immediately persist each raw/summary output before any later scientific run.

At any failure after a scientific run starts:

- stop fail-closed;
- do not edit harnesses;
- do not rerun;
- do not tune parameters/tolerances.

## Required per-run outputs

For every completed run report:

- `C_hh`
- raw hours `H_hh`
- effective labor `L_hh`
- `A_hh`
- `B_hh`
- stationary mass normalization
- minimum mass / negative count
- HJB convergence and residual if exposed
- KKT/boundary residual if exposed
- generator row-sum/off-diagonal diagnostics
- KFE stationarity residual
- iteration count

Aggregate definitions must be common:

`C_hh = sum(mass * c)`

`H_hh = sum(mass * l)`

`L_hh = sum(mass * z * l)`

`A_hh = sum(mass * a)`

`B_hh = sum(mass * b)`

For MATLAB, independently verify its native `Ct/Lt/At/Bt` map to these common formulas under the common measure. If a native stored aggregate uses a different measure, compute the common aggregate from raw policies/mass and report both rather than silently equating them.

## Required detailed parity diagnostics

For each `r_a` rate, after applying the accepted MATLAB-to-Python orientation adapter, report where available:

- max absolute difference in `c(a,b,z)`;
- max absolute difference in raw labor `l(a,b,z)`;
- max absolute difference in effective labor `z*l`;
- max absolute difference in transfer `d`;
- max absolute difference in `mu_a` and `mu_b`;
- max absolute difference in stationary probability mass;
- policy/direction mismatch counts;
- aggregate level differences.

Do not hide a mismatch behind aggregate cancellation.

## Frozen comparison tolerances

Because these are independently converged HJB/KFE solutions rather than direct formula evaluations, use these fixed pre-execution aggregate acceptance bounds:

For each of `C_hh`, `H_hh`, `L_hh`, `A_hh`, `B_hh`:

`abs(MATLAB - Python) <= 1e-6 * max(1, abs(MATLAB), abs(Python))`

For stationary probability mass:

`max_abs(m_M_mapped - m_P) <= 1e-6`

For each within-language response delta (`0.041 - 0.040`) and the cross-language difference in that delta:

`abs(delta_M - delta_P) <= 1e-6 * max(1, abs(delta_M), abs(delta_P))`

Do not widen these bounds after seeing results.

Pointwise policy differences are required as diagnostics but are not automatically a terminal failure unless they produce material unexplained aggregate/mass mismatch or violate accepted validity contracts. Any substantial structured policy discrepancy must be discussed explicitly.

## Required compact result tables

### Levels

| implementation | r_a | C_hh | H_hh | L_hh | A_hh | B_hh |
|---|---:|---:|---:|---:|---:|---:|
| MATLAB | 0.040 | ... | ... | ... | ... | ... |
| Python | 0.040 | ... | ... | ... | ... | ... |
| MATLAB | 0.041 | ... | ... | ... | ... | ... |
| Python | 0.041 | ... | ... | ... | ... | ... |

### Responses

For each implementation report:

- `Delta C_hh`
- `%Delta C_hh`
- `Delta H_hh`
- `%Delta H_hh`
- `Delta L_hh`
- `%Delta L_hh`
- `Delta A_hh`
- `Delta B_hh`

Then report MATLAB-Python differences in each level and each delta.

## Classification

Return exactly one terminal classification:

- `TRUE_SAME_INPUT_AGGREGATE_PARITY_PASS__P5_OWNER_ACCEPTANCE_RECOMMENDED`
- `TRUE_SAME_INPUT_AGGREGATE_PARITY_NEEDS_DIAGNOSTIC__P5_BLOCKED`
- `TRUE_SAME_INPUT_AGGREGATE_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT`

Use `PASS` only if:

- all four runs complete and are scientifically valid;
- common inputs are proven identical;
- the effective-labor semantic mapping is correct;
- all aggregate levels pass the frozen common-input tolerance;
- all response deltas pass the frozen common-input tolerance;
- stationary mass passes its frozen bound;
- no unexplained material structured policy discrepancy remains.

If valid solves complete but aggregate/mass/delta parity fails, use `NEEDS_DIAGNOSTIC`; do not repair or rerun in the same task.

## Output report

Write exactly one repository report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_REPORT.md`

The report must include:

- live/source identities;
- full frozen common manifest;
- MATLAB field mapping;
- productivity-operator proof;
- finite-state measure proof;
- common labor semantic mapping;
- preflight evidence and harness hashes;
- exact execution counts;
- per-run validity diagnostics;
- complete level/response tables;
- pointwise policy/mass diagnostics;
- frozen tolerance evaluations;
- terminal classification;
- forbidden-operation check;
- recommendation for P5 or diagnostic successor.

## Commit/push authorization

Only the report may be added to the repository.

If and only if it is the sole repository change:

- stage only the report;
- create one commit;
- fresh-fetch remote `main`;
- fast-forward push only if remote `main` has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Record true same-input HA aggregate parity`

## Forbidden operations

Do not:

- modify MATLAB or Python production source/tests;
- use the Jiangsu native snapshot as the common scientific input;
- change any frozen economic parameter, grid, productivity operator, measure, or tolerance;
- use different labor aggregate semantics across languages;
- use different productivity processes across languages;
- use different stationary measures across languages;
- rerun P1-P4;
- rerun any consumed scientific solve;
- tune after seeing results;
- issue P5 acceptance directly;
- enter AR(1), transition, IRF, calibration extension, dynamics, or Results work;
- merge, rebase, reset, or force-push.

## Recommended next gate

If terminal classification is:

`TRUE_SAME_INPUT_AGGREGATE_PARITY_PASS__P5_OWNER_ACCEPTANCE_RECOMMENDED`

then the next and only gate is:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

If terminal classification is `NEEDS_DIAGNOSTIC`, P5 remains blocked and the report must identify the smallest evidence-based diagnostic successor.