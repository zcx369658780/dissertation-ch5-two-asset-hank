# CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_INITIALIZATION_EXECUTION

## Task

Execute the final true same-input aggregate parity experiment for the two-asset HA household block, correcting only the predecessor verification protocol's over-strong requirement that the `r_a=0.040` and `r_a=0.041` cases share one identical numerical initial value.

The predecessor preflight established that MATLAB constructs its HJB initial guess internally and that the initial guess depends on the externally supplied household return `rah`. This is not a scientific-model discrepancy: `rah` is an exogenous household input, and a rate-dependent HJB starting guess is a numerical initialization choice.

The correct parity requirement is therefore **rate-matched initialization**, not cross-rate-identical initialization:

- at `r_a/rah=0.040`, Python must use the exact MATLAB-generated `v02` for the `0.040` case after orientation mapping;
- at `r_a/rah=0.041`, Python must use the exact MATLAB-generated `v02` for the `0.041` case after orientation mapping;
- `v02(0.040)` is allowed to differ from `v02(0.041)` because these are different economic parameter cases.

No new scientific adapter is authorized by this correction.

This task authorizes exactly one four-run scientific execution if all corrected pre-scientific gates pass.

It does not itself issue P5 acceptance and does not authorize dynamics, AR(1), transition, IRF, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted evidence and authority

Fresh-read live GitHub `main`.

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Accepted P1-P4 numerical evidence:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Predecessor adapter-conformance report:

`c849c48dd78518dd22ffed20e6c3d9125bdd9488`

Predecessor blocked gamma2 execution report:

`4fdb31f46ce48753b060ca279b7a289a2e8d36c7`

Accepted MATLAB source identities remain:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- production `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `lab_solve2.m`
  - SHA-256 `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

Do not rerun P1-P4.

## Required live read-back

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_SAME_INPUT_PARITY_ADAPTER_DESIGN_AND_CONFORMANCE_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_EXECUTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- accepted Python `contracts.py`, `economics.py`, `hjb.py`, `generator.py`, `kfe.py`, `policies.py`, `boundaries.py`, `indexing.py`, and relevant diagnostics.

Verify live Python `src/tests` remain scientifically unchanged from the accepted baseline. If not, stop:

`BLOCKED_GAMMA2_RATE_MATCHED_PARITY_PYTHON_SOURCE_DRIFT`

## Scientific interpretation of initialization

The following distinction is frozen for this task:

### Economic inputs

The only economic input changed across the baseline/perturbation pair is:

`r_a / rah: 0.040 -> 0.041`.

All other economic parameters, prices, grids, productivity states/operator, transfers/wedges, adjustment-cost parameters, and labor parameters remain identical.

### Numerical initialization

The HJB initial value is a numerical starting guess, not a household primitive.

The accepted MATLAB implementation constructs this starting guess internally from the current `rah`. Therefore:

`v02_M(0.040)` may differ from `v02_M(0.041)`.

For parity, Python must use:

`v0_P(0.040) = orientation_map(v02_M(0.040))`

and

`v0_P(0.041) = orientation_map(v02_M(0.041))`.

Require exact/machine identity **within each rate pair** after orientation mapping.

Do not require:

`v02_M(0.040) == v02_M(0.041)`.

Do not add a MATLAB external-initial-value adapter.

The predecessor measured a cross-rate `v02` max difference of `5.538445613240128e-06`; this is accepted as a numerical-initialization difference and is not itself a parity criterion.

## Frozen common gamma2 fixture

Use exactly:

- `rho = 0.05`
- `gamma_c / ga = 2.0`
- `phi = 1.0`
- `frisch_l = 1.0`
- scalar labor weight = `1.0`
- `chi_0 = 0.05`
- `chi_1 = 1.0`
- `a_bar = 0.5`
- `r_b = 0.03`
- `w = 1.0`
- `tau = 0.0`
- migration cost = `0.0`
- `Tt = 0.0`
- `rb_gap = 0.0`
- `fixcost = 0.0`
- `fixcost2 = 0.0`
- baseline `r_a / rah = 0.040`
- perturbation `r_a / rah = 0.041`

Common grids:

- `a = [0.0, 0.5, 1.0, 1.5, 2.0]`
- `b = [0.0, 1.25, 2.5, 3.75, 5.0]`
- `z = [0.8, 1.3]`

Common productivity backward generator:

```text
Q_z_common =
[[-0.4,  0.4],
 [ 0.3, -0.3]]
```

State count: `5 * 5 * 2 = 50`.

Finite-state measure:

- `da = 0.5`
- `db = 1.25`
- cell weight = `0.625`
- no separate z quadrature factor.

## Only authorized scientific adapters

Exactly the two predecessor-conformed adapters remain authorized.

### MATLAB O1 low-a FOC adapter

Production main and cost helper remain byte-identical.

Use the already conformance-tested external temporary `HANK3_FOC.m` whose only scientifically material domestic change is:

`a -> max(a,a_bar)`.

Require the predecessor adapter SHA-256:

`B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315`.

Before execution, prove path resolution:

- `HANK_2ASSETS_HJB` -> accepted original main;
- `HANK3_cost` -> accepted original cost helper;
- `HANK3_FOC` -> exact frozen external O1 helper;
- `lab_solve2` -> accepted original helper.

### Python O2 common-Q operator adapter

Use the already conformance-tested external adapter with SHA-256:

`D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225`.

It may rebind only:

`ch5_two_asset_hank.hjb.build_operator`.

It must:

- retain production `_asset_generator` for `G_a/G_b`;
- inject exactly `G_z = kron(Q_z_common, I_25)`;
- return the unchanged production `OperatorBundle` shape/diagnostics;
- restore the original binding in `finally`.

It must not replace derivatives, policy selection, FOCs, KKT, implicit solve, HJB residual, convergence logic, KFE, aggregation, or other scientific code.

No third adapter is authorized.

## Corrected pre-scientific gates

Before any HJB/KFE scientific run:

1. verify live/source identities and no Python source/test drift;
2. verify the complete frozen common gamma2 economic manifest;
3. verify Python `GridSpec` accepts the 50-state grid;
4. verify MATLAB/Python gamma2 CRRA utility and consumption FOC conformance at representative positive values;
5. verify the exact O1 helper hash/path resolution and prior 12-point conformance evidence;
6. verify the exact O2 adapter hash and sparse synthetic `G_a/G_b/G_z` conformance;
7. verify orientation adapter MATLAB `[b,a,z]` <-> Python `[a,b,z]`;
8. independently reconstruct MATLAB's internal initialization for `rah=0.040` without calling HJB;
9. independently reconstruct MATLAB's internal initialization for `rah=0.041` without calling HJB;
10. persist/hash both reconstructed MATLAB `v02` arrays separately;
11. map each array to Python orientation separately;
12. freeze Python `initial_value_0040` as exactly the mapped MATLAB `v02_0040`;
13. freeze Python `initial_value_0041` as exactly the mapped MATLAB `v02_0041`;
14. prove machine/exact identity within each corresponding rate pair;
15. explicitly report the allowed cross-rate initial-value difference but do not gate on it;
16. verify common finite-state measure and KFE cell weights;
17. run synthetic persistence/serialization preflight for all planned raw/summary outputs;
18. freeze/hash all execution harnesses before scientific execution.

No HJB, policy solve, generator-based household solve, or KFE solve may occur during these gates.

If any corrected gate fails, stop before scientific execution with:

`TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_BLOCKED_SOURCE_OR_ENVIRONMENT`.

Do not partially execute one implementation.

## Scientific execution budget

If and only if all corrected preflight gates pass, execute exactly four scientific solves:

1. MATLAB common baseline `rah=0.040` — exactly once;
2. Python common baseline `r_a=0.040` using `initial_value_0040` — exactly once;
3. MATLAB common perturbation `rah=0.041` — exactly once;
4. Python common perturbation `r_a=0.041` using `initial_value_0041` — exactly once.

Immediately persist and read back every completed raw/summary output before starting the next scientific run.

No reruns.

At the first failure after scientific execution starts:

- stop fail-closed;
- do not edit harnesses/adapters;
- do not rerun;
- do not tune inputs or tolerances.

## Required validity checks

For every completed Python run require/report:

- HJB converged flag;
- HJB iterations and iteration change;
- HJB residual sup;
- KKT residual;
- boundary violation;
- generator maximum row sum and minimum off-diagonal;
- recurrent class count/size and left nullity where available;
- KFE stationarity residual;
- probability normalization error;
- minimum mass and negative-mass count;
- finite values;
- O2 binding restored after the solve.

For MATLAB require/report every validity object exposed by the accepted original source, including:

- `convergent`;
- finite policy/value/output arrays;
- stationary normalization;
- minimum probability mass / signed-roundoff scale;
- aggregate consistency identities;
- any generator validity that can be audited externally from persisted output.

The lack of a MATLAB residual field must be reported as `NOT_EXPOSED_BY_ACCEPTED_ORIGINAL_SOURCE`, not invented.

## Common aggregate semantics

For both implementations compute the same probability-mass aggregates:

`C_hh = sum(mass * c)`

`H_hh = sum(mass * l)`

`L_hh = sum(mass * z * l)`

`A_hh = sum(mass * a)`

`B_hh = sum(mass * b)`

`L_hh` is effective labor. Do not compare MATLAB `Lt` with Python raw hours.

For MATLAB independently derive the common-mass aggregates from raw policy/mass arrays after orientation mapping; also report native `Ct/Lt/At/Bt` and prove whether they coincide under the common measure.

## Required pointwise parity diagnostics

For each rate, after the accepted orientation adapter, report where semantically common:

- max absolute value-function difference;
- max absolute `c` difference;
- max absolute raw `l` difference;
- max absolute effective `z*l` difference;
- max absolute transfer `d` difference;
- max absolute adjustment-cost difference;
- max absolute `mu_a` difference;
- max absolute `mu_b` difference;
- max absolute stationary probability-mass difference;
- policy/direction mismatch counts and locations;
- any mismatch attributable solely to an already accepted representation adapter.

Do not allow aggregate cancellation to hide a structured statewise discrepancy.

## Frozen tolerances

Do not change these after seeing results.

For each aggregate level `C_hh`, `H_hh`, `L_hh`, `A_hh`, `B_hh`:

`abs(MATLAB - Python) <= 1e-6 * max(1, abs(MATLAB), abs(Python))`.

Stationary probability mass:

`max_abs(m_M_mapped - m_P) <= 1e-6`.

For each within-language response delta and its cross-language difference:

`abs(delta_M - delta_P) <= 1e-6 * max(1, abs(delta_M), abs(delta_P))`.

Pointwise differences are diagnostics; a material structured discrepancy that survives the O1/O2 adapters blocks P5 even if aggregate tolerances pass.

## Required result tables

### Levels

| implementation | r_a | C_hh | H_hh | L_hh | A_hh | B_hh |
|---|---:|---:|---:|---:|---:|---:|
| MATLAB | 0.040 | ... | ... | ... | ... | ... |
| Python | 0.040 | ... | ... | ... | ... | ... |
| MATLAB | 0.041 | ... | ... | ... | ... | ... |
| Python | 0.041 | ... | ... | ... | ... | ... |

### Responses

For each implementation report:

- `Delta C_hh`, `%Delta C_hh`;
- `Delta H_hh`, `%Delta H_hh`;
- `Delta L_hh`, `%Delta L_hh`;
- `Delta A_hh`;
- `Delta B_hh`.

Then report MATLAB-Python differences in every level and every delta against the frozen tolerances.

## Terminal classification

Return exactly one:

- `TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_PASS__P5_OWNER_ACCEPTANCE_RECOMMENDED`
- `TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_NEEDS_DIAGNOSTIC__P5_BLOCKED`
- `TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_BLOCKED_SOURCE_OR_ENVIRONMENT`

Use `PASS` only if:

- all four runs complete exactly once;
- all scientific validity checks pass;
- all economic inputs are common except the intentionally varied `r_a`;
- initialization is rate-matched exactly within each MATLAB/Python pair;
- aggregate levels pass frozen tolerances;
- response deltas pass frozen tolerances;
- stationary probability mass passes its frozen bound;
- no material unexplained structured pointwise discrepancy remains after the authorized O1/O2 adapters.

If scientifically valid four-run results complete but parity fails, return `NEEDS_DIAGNOSTIC` and do not repair/rerun in the same task.

## Output report

Write exactly one repository report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_INITIALIZATION_EXECUTION_REPORT.md`

The report must include:

- live/source identities;
- full common gamma2 manifest;
- corrected initialization semantics and both rate-specific initialization hashes;
- O1/O2 adapter identities and conformance reuse;
- preflight evidence/harness hashes;
- exact four-run execution counts;
- all validity diagnostics;
- pointwise parity diagnostics;
- stationary-mass comparison;
- aggregate level and response tables;
- frozen-tolerance evaluations;
- terminal classification;
- forbidden-operation check;
- recommendation for P5 or diagnostic successor.

## Commit/push authorization

Only the report may be added to the repository.

If and only if it is the sole repository change:

- stage only the report;
- create one commit;
- fresh-fetch remote `main`;
- fast-forward push only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Run rate-matched gamma2 same-input HA aggregate parity`

## Forbidden operations

Do not:

- modify accepted MATLAB production main/helpers;
- modify Python `src/tests`;
- add a third scientific adapter;
- force one cross-rate common initial value;
- alter any economic input other than the frozen `r_a/rah` pair;
- change the common grid, Q_z, measure, or tolerances;
- rerun P1-P4;
- rerun any consumed scientific solve;
- tune after seeing results;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, dynamics, or Results;
- merge, rebase, reset, or force-push.

## Recommended next gate

If terminal classification is:

`TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_PASS__P5_OWNER_ACCEPTANCE_RECOMMENDED`

then the next and only HA gate should be:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`.

If `NEEDS_DIAGNOSTIC`, P5 remains blocked and the report must identify the smallest failing object for one targeted diagnostic task.