# CH5 Two-Asset HANK Session Handoff after Pre-P5 Same-Input Convergence Block

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## 1. Handoff purpose

This handoff freezes the current Chapter 5 two-asset HA reconstruction state before changing the common same-input diagnostic fixture/parameters.

The immediate scientific goal remains unchanged:

> determine whether the accepted Python two-asset HA rewrite is structurally and numerically correct before any dynamic extension.

Do not enter AR(1), transition dynamics, IRFs, calibration extension, or Results work until the HA parity route reaches explicit Owner P5 acceptance.

## 2. GitHub authority and roles

GitHub `main` is the sole repository-state authority.

ChatGPT role:

- independent L3 reviewer;
- scientific route authority;
- GitHub task issuer;
- acceptance-gate reviewer.

Codex role:

- bounded Builder/executor;
- must fresh-read live GitHub `main` and exact task authority before execution;
- chat instructions alone do not replace a published task.

Owner role:

- final scientific authority;
- explicit Owner acceptance is required for P5.

Required governance reads at the start of the next session:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`

## 3. Current live scientific state before this handoff publication

Latest scientific execution/report commit before handoff publication:

`47c27947dec9c008c95d3830ba28b2e423c8b027`

Report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_INITIALIZATION_EXECUTION_REPORT.md`

Terminal classification:

`TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_NEEDS_DIAGNOSTIC__P5_BLOCKED`

P5 is **not accepted**.

## 4. Accepted Python scientific baseline

Accepted Python implementation baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

All later parity/report/task commits have repeatedly verified that accepted Python `src/tests` remain scientifically unchanged from this baseline.

Important accepted Python behavior:

- two-asset state `(a,b,z)`;
- lower illiquid bound `a=0`;
- lower liquid bound `b=b_bar`;
- accepted KKT/state-constraint logic;
- accepted low-`a` adjustment scale `m(a)=max(a,a_bar)`;
- accepted reflected productivity redesign in production Python;
- accepted KFE uses forward operator `G^T` and uniqueness/connectivity checks.

## 5. Accepted MATLAB source authority

Designated MATLAB tree:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Accepted source identities:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `lab_solve2.m`
  - SHA-256 `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

MATLAB is not treated as an unquestioned oracle. Accepted redesigns are validated against dissertation/equation authority.

## 6. Structural parity status

Structural review is closed under:

`OWNER_STRUCTURAL_PARITY_CLOSED__NUMERICAL_PARITY_REQUIRED`

Key accepted structural decisions include:

- O1: MATLAB low-`a` transfer FOC is a legacy limitation; accepted equation/Python use `max(a,a_bar)` consistently.
- O2: MATLAB two-state productivity and Python reflected productivity are different accepted representations; common-object parity may use an explicit test-only productivity adapter.
- O3-O12: boundary/KKT, zero-drift candidate, upper/corner closure, F/Z canonicalization, drift signs, labor mapping, generator/KFE transpose, stationary uniqueness, mass/density, and legacy initialization differences have been reviewed and accepted under the existing reports.

Primary structural report:

`docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`

## 7. Accepted numerical parity P1-P4

P1-P4 remain accepted and must not be rerun without new authority.

Accepted P1-P4 evidence commit:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Key evidence:

- P1 pointwise primitives: 432 shared-input cases; comparable fields matched at machine/exact level; controlled low-`a` legacy counterexamples documented.
- P2 policy/local HJB cases: 10/10 completed after pure harness corrections; common comparable cases matched exactly; accepted redesign cases validated separately.
- P3 generator parity: mapped `G_a`, `G_b`, `G_z`, and total `G` matched; generator validity passed.
- P4 KFE/stationary parity: stationary mapped mass, normalization, stationarity residual, and aggregate `A_hh/B_hh` matched at machine-scale numerical precision.

Primary reports:

- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_PYTHON_HARNESS_API_ARITY_CORRECTION_AND_COMPLETION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`

These provide strong evidence that the Python rewrite is structurally/numerically correct on all already-defined comparable objects, but the Owner requested one final full same-input HJB->KFE->aggregate integration test before P5.

## 8. Accepted Python R4 steady-state evidence

Accepted R4 steady-state evidence commit:

`8931eacf4e9f503b9ab12b75399f098177196dfb`

Representative accepted diagnostics:

- HJB residual approximately `8.4e-10`;
- KKT residual approximately `9e-15`;
- generator row-sum approximately `2.7e-15`;
- one recurrent class including all illiquid-asset layers;
- left nullity `1`;
- KFE stationarity approximately `3.9e-16`;
- normalization/mass-density consistency at machine precision.

This shows the accepted Python production HA solves its own frozen R4 object robustly.

## 9. Native robustness experiment completed before same-input route

A native partial-equilibrium robustness check was completed at `r_a/rah=0.040 -> 0.041`.

MATLAB native snapshot and Python R4 were **different calibrations**, so their levels were not exact-parity objects.

Persisted native levels:

- MATLAB `C_hh`: `9.093838085759417 -> 9.088797065167160`
- MATLAB effective `L_hh`: `0.7208465448372894 -> 0.7201767277365387`
- Python `C_hh`: `0.5570429699260410 -> 0.5570955509235596`
- Python raw labor object in that older supplementary table: `0.9990139906201341 -> 0.9988855345043183`

Important later semantic correction:

MATLAB native `Lt` is **effective labor** `sum(mass*z*l)`, whereas Python pointwise labor is raw hours `l`. Future parity must distinguish:

- `H_hh = sum(mass*l)` raw hours;
- `L_hh = sum(mass*z*l)` effective labor.

The final parity object for MATLAB `Lt` is Python effective labor, not raw hours.

## 10. Same-input route history and resolved blockers

### A. First unchanged-native common fixture

Attempted common fixture with positive `a` lower bound and `Nz=9` was blocked before execution because:

- Python `GridSpec` requires `a[0]==0`;
- accepted MATLAB HJB hard-codes a two-state productivity block.

This was an interface blocker, not a parity failure.

### B. Test-only adapter design

Two narrow adapters were designed and conformance-tested without changing production source.

MATLAB O1 test-only FOC helper:

- SHA-256 `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315`;
- sole scientifically material change: domestic transfer-FOC scale `a -> max(a,a_bar)`;
- 12 representative points matched accepted Python `transfer_candidate` exactly.

Python O2 test-only common-Q adapter:

- SHA-256 `D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225`;
- rebinds only `ch5_two_asset_hank.hjb.build_operator`;
- retains production `_asset_generator` for `G_a/G_b`;
- injects common `G_z=kron(Q_z_common,I)`;
- restores original binding after solve.

No third adapter has been accepted.

### C. Gamma=1 blocker

A common `gamma=1` fixture was rejected because accepted MATLAB main uses CRRA `C^(1-ga)/(1-ga)` without a `ga==1` log branch.

Resolution: common fixture refrozen at `gamma=2`; no log-utility adapter was added.

### D. Cross-rate initialization blocker

MATLAB internally constructs a rate-dependent HJB starting guess. The earlier requirement that `v02(0.040)==v02(0.041)` was recognized as an over-strong verification condition.

Corrected protocol:

- Python 0.040 must use mapped MATLAB `v02_0040`;
- Python 0.041 must use mapped MATLAB `v02_0041`;
- cross-rate initial values may differ.

This corrected preflight passed.

## 11. Current failed common gamma2 fixture

Frozen common fixture used by the latest scientific attempt:

- `rho=0.05`
- `gamma_c/ga=2.0`
- `phi=1.0`, `frisch_l=1.0`
- labor weight `1.0`
- `chi_0=0.05`
- `chi_1=1.0`
- `a_bar=0.5`
- `r_b=0.03`
- `w=1.0`
- `tau=0`
- migration cost `0`
- `Tt=0`
- `rb_gap=0`
- `fixcost=0`, `fixcost2=0`
- `r_a/rah=0.040/0.041`
- `a=[0,0.5,1.0,1.5,2.0]`
- `b=[0,1.25,2.5,3.75,5.0]`
- `z=[0.8,1.3]`
- `Q_z_common=[[-0.4,0.4],[0.3,-0.3]]`
- 50 states
- finite-state mass cell weight `da*db=0.625`.

Rate-matched initialization preflight passed exactly.

Scientific execution then began once:

- MATLAB baseline `rah=0.040`: exactly one run;
- returned `convergent=false`;
- raw result persisted/read back;
- all later runs stopped fail-closed.

Observed failed-run diagnostics:

- MATLAB `convergent=false`;
- stationary solve emitted near-singular warning at `HANK_2ASSETS_HJB.m:340`;
- `RCOND = 1.280574e-18`;
- returned arrays finite;
- stationary mass sum `1.0`;
- minimum mass `-1.3896874805456546e-18` (machine-scale signed roundoff);
- descriptive failed-run aggregates:
  - `C_hh=1.0489158011797988`
  - raw `H_hh=0.9842018950457534`
  - effective `L_hh=1.0489158011797988`
  - `A_hh≈0`
  - `B_hh≈0`.

These are descriptive outputs from a non-converged MATLAB run and are **not accepted parity evidence**.

## 12. Current scientific interpretation

The latest failure does **not** establish that Python is wrong:

- Python was not run in the latest same-input experiment;
- P1-P4 already pass on materially comparable objects;
- Python R4 solves robustly;
- the latest failure is the MATLAB common fixture failing its own convergence flag before cross-language comparison.

The strongest evidence-based hypothesis is that the chosen synthetic 50-state common fixture is numerically/economically unsuitable for the accepted legacy MATLAB HJB, but this has not yet been proven. Do not silently tune parameters.

## 13. Required next-session route

The next session must **first change/design the common fixture parameters under a new published diagnostic/design task**, then rerun parity only after the fixture is proven suitable.

Recommended next gate name:

`CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_PARAMETER_REDESIGN_AND_MATLAB_CONVERGENCE_QUALIFICATION`

The immediate task should be diagnostic/design, not full parity execution.

Required principles:

1. Do not modify accepted Python or MATLAB production source.
2. Keep only the already conformed O1/O2 test-only adapters unless new Owner authority is explicitly granted.
3. Determine why the latest MATLAB common fixture returned `convergent=false` and near-singular stationary system.
4. Use source evidence and previously successful MATLAB/native configurations to propose a **small, auditable candidate set** of common parameters/grids that both implementations can represent.
5. Prefer changing fixture parameters/grid bounds/resolution rather than solver tolerances.
6. Do not tune after seeing scientific outputs in the same task.
7. Qualify a candidate for MATLAB convergence before consuming a new four-run cross-language parity budget.
8. Once one common fixture is frozen and qualified, publish a separate final same-input four-run parity task.
9. P5 remains blocked until that final integration gate passes or the Owner explicitly changes the acceptance standard.

Potential dimensions to audit before selecting the next fixture include:

- asset grid ranges and resolution (`a` upper bound, `b` borrowing range, number of nodes);
- `a_bar`, adjustment-cost parameters `chi_0/chi_1`;
- `r_b`, wage, and labor curvature/Frisch mapping;
- whether the synthetic non-borrowing `b>=0` grid created a degenerate stationary distribution;
- exact native MATLAB parameter ranges known to converge, while preserving a scientifically common object representable in Python;
- connectivity/recurrent-class implications of the common fixture.

Do not assume any one of these is the cause before the next diagnostic task.

## 14. Do-not-cross boundaries

Until P5:

- no AR(1) extension;
- no transition dynamics;
- no IRFs;
- no calibration extension;
- no Results drafting based on the new Python rewrite;
- no production-source mutation solely to manufacture MATLAB-Python equality;
- no rerun of consumed one-shot experiments without new GitHub authority;
- no silent tolerance widening.

## 15. P5 acceptance target remains

Final Owner acceptance marker remains:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

A future P5 gate should be considered only after:

- the final common fixture itself is scientifically/numerically qualified;
- all four MATLAB/Python baseline/perturbation runs complete;
- validity diagnostics pass;
- common aggregates/mass/deltas meet pre-frozen criteria;
- no material unexplained structured pointwise mismatch survives accepted adapters;
- Owner explicitly accepts the complete evidence.

## 16. Next-session first action

Fresh-fetch live GitHub `main`, read this handoff and the latest rate-matched execution report, then publish/execute only the parameter-redesign and MATLAB-convergence-qualification task. Do not jump directly to another four-run parity experiment.
