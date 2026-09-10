# Chapter 5 MP4C initial private-K observation and residual-GovInv probe

Date: 2026-09-11. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Test the Owner-approved residual-initialization idea without yet changing the production steady-state runtime:

`GovInv0_residual_j = max(Ktarget_j - Kt_supply_initial_j, 0)`.

The task must obtain exactly one clearly timed initial household observation under the accepted corrected-2018 initial state, construct At-only private productive capital using the existing source allocation, and compare the residual GovInv initialization against the historical/source-faithful `GovInv0=Ktarget` start.

This is an initialization probe, not an outer-turn trajectory, not controller redesign, and not Results.

## 2. Required authority

Fresh-read live `origin/main`, then read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_IMPLEMENTATION_ACCEPTANCE.md`;
- `docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md` and acceptance;
- `docs/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_REPORT.md` and acceptance;
- `docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_ACCEPTANCE.md`;
- `src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py`;
- `src/ch5_two_asset_hank/multi_province/capital_allocation.py`;
- current household/HJB/KFE oracle and the accepted corrected initialization harness.

Protected MATLAB remains read-only. If available, inspect `HANK_mp_1turn.m`, `HANK_mp_1eq.m`, and `HANK_firm.m` only for source timing/accounting confirmation.

## 3. Frozen corrected-2018 initial contract

Use the accepted active corrected-2018 route only:

- actual 2018 GDP and population;
- raw-NBS GFCF Track-A PIM capital;
- `delta_pim=.096`;
- `alpha=.7380939146868483`;
- `MU=10万元`, `NU=100 persons`;
- accepted same-year `Zt0`;
- accepted initial household prices/returns/wage states from the repaired runtime;
- firm depreciation `.025` remains separate;
- source bounds unchanged;
- no damping, hysteresis, controller change, grid change, HJB/KFE equation change, or tolerance tuning.

The accepted 31/31 pre-science validator must pass before the single observation begins.

## 4. Scientific timing contract

The probe has one and only one household-initialization observation stage:

1. Build and validate corrected-2018 initial states.
2. For each of 31 provinces, solve the household HJB/KFE once under those fixed predeclared initial prices/states.
3. Aggregate `At`, `Bt`, `Lt`, `Ct` once.
4. Do **not** update wages, `ra`, `rah`, `Zt`, `GovInv`, or any province state from these returns.
5. After all 31 household outputs are collected, run the existing **At-only productive-capital allocation** exactly once to construct `Kt_supply_initial`.
6. Compute the two accounting starts:
   - historical/source start: `GovInv0_G0 = Ktarget`;
   - probe residual start: `GovInv0_G1 = max(Ktarget - Kt_supply_initial, 0)`.
7. Compute implied accounting total capital under each start, but do not call the firm or controller.

This observation is not outer turn 1 and must not be followed by migration, wage, firm, controller, or steady-state execution.

## 5. HJB/KFE continuation rule

Use the already accepted continuation policy:

- finite, structurally usable HJB return with `converged=false` may continue as `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`, preserving the false flag;
- nonfinite/malformed/unusable HJB or KFE output fails closed;
- KFE diagnostic-only status must be preserved and reported;
- this probe cannot claim scientific household validity merely because an aggregate is numerically available.

## 6. Private-capital definition

`Kt_supply_initial` must be the existing productive-capital allocation based on **At only**. `Bt` must not enter productive capital.

Preserve the accepted source ordering/orientation and inter-province allocation semantics. Do not redesign capital allocation.

For this probe only, retain the existing source-faithful diagnostic bridge:

`K_private_MU = At_grid * beta_a * N_NU`, with `beta_a=1` labelled `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`.

Do not promote `beta_a=1` to production or Results authority. Do not choose `beta_a` from convergence or target matching.

## 7. Bridge forensic and scale sensitivity

Because the absolute At-grid→MU bridge remains scientifically unresolved, the report must separate:

- **observed probe under beta_a=1 diagnostic bridge**;
- **symbolic bridge dependence**.

For each province, write the affine dependence of private capital on an arbitrary positive bridge scalar `beta_a`:

`Kt_supply_initial(beta_a) = beta_a * Kt_supply_initial(beta_a=1)`

provided the source allocation is homogeneous as expected; verify this algebraically from the allocation implementation without extra household solves.

Compute the province-specific threshold

`beta_a_star_j = Ktarget_j / Kt_supply_initial_j(beta_a=1)`

when denominator is positive. This is the bridge value at which residual GovInv becomes zero for that province. This is diagnostic geometry only, not a calibrated beta choice.

Do not run parameter cells.

## 8. Required province ledger

For all 31 provinces record at least:

- province index/name;
- `Ktarget_2018_MU`;
- household HJB convergence flag / iterations / statistic;
- KFE diagnostic classification;
- `At_initial`, `Bt_initial`, `Lt_initial`, `Ct_initial`;
- origin population `N_NU`;
- pre-allocation source private capital mass `At*N` under beta=1 if available;
- `Kt_supply_initial_MU_beta1` after existing cross-province capital allocation;
- `private_K_over_target_beta1`;
- `GovInv0_G0_MU = Ktarget`;
- `firm_K_accounting_G0 = Ktarget + Kt_supply_initial`;
- `firm_K_G0_over_target`;
- `GovInv0_G1_residual_MU`;
- `firm_K_accounting_G1 = Kt_supply_initial + GovInv0_G1`;
- `firm_K_G1_over_target`;
- `beta_a_star`;
- residual-rule binding flag (`PRIVATE_BELOW_TARGET`, `PRIVATE_AT_OR_ABOVE_TARGET`);
- validity labels.

## 9. National summary

Report national sums and province distributions for:

- Ktarget;
- initial private K under beta=1;
- G0 GovInv;
- G0 total K;
- G1 residual GovInv;
- G1 total K;
- G0 and G1 total-K/target ratios;
- private-K/target ratios;
- number of provinces with G1 residual clipped at zero;
- min/median/max `beta_a_star`.

If every province has private K below target under beta=1, state that G1 exactly aligns accounting total K to Ktarget by construction under this diagnostic bridge. If any private K exceeds target, identify those provinces and report unavoidable overshoot under nonnegative GovInv.

## 10. Anhui trace

Provide a dedicated Anhui receipt containing:

- accepted `Y0`, `N0`, `Ktarget`, `alpha`, `Zt0`;
- initial fixed household prices/returns;
- HJB/KFE status;
- `At`, `Bt`, `Lt`, `Ct`;
- `Kt_supply_initial_beta1`;
- private-K/target;
- G0 GovInv and total K;
- G1 GovInv and total K;
- `beta_a_star`.

## 11. Required interpretations

Answer directly:

1. Is a one-pass `Kt_supply_initial` numerically available for 31/31 provinces under the accepted initial state?
2. Are those objects scientifically diagnostic-only because of HJB/KFE blockers, and if so which blockers remain?
3. Under beta=1, how large is initial private K relative to Track-A Ktarget?
4. Does G1 remove the mechanical `Ktarget + private K` overshoot at initialization for all provinces where private K is below target?
5. Does any province have private K >= Ktarget, forcing residual GovInv to zero and leaving overshoot?
6. How sensitive is G1 to the unresolved At→MU bridge, as summarized by `beta_a_star`?
7. Is there enough evidence to implement G1 as the next **diagnostic successor initialization route**, still with beta=1 explicitly diagnostic-only?
8. Does this task provide any reason to redesign the existing `HANK_mp_1eq.m` controller now? The expected answer should distinguish initialization from controller behavior.

## 12. Scientific-call budget

Maximum scientific calls:

- one scientific process;
- 31 household observations maximum;
- 31 HJB returns maximum;
- 31 KFE returns maximum;
- 31 household aggregates maximum;
- exactly one deterministic At-only capital-allocation composition after the full batch.

Forbidden:

- second household observation pass;
- migration-labor execution;
- normalized migration execution;
- firm calls;
- wage calculation;
- GovInv controller calls;
- outer turn;
- steady state;
- GE/annual/IRF/Results;
- any parameter/tolerance/grid tuning;
- any second beta parameter cell.

Engineering retry is allowed only before scientific state advances and must be logged.

## 13. Implementation boundary

Do not change production `GovInv0` yet.

It is allowed to add a pure helper/schema for residual GovInv arithmetic and deterministic validation, but it must not be wired into active steady-state/trajectory runtime in this task.

Do not modify the newly accepted normalized labor route except for imports/tests strictly necessary to prove it is untouched.

## 14. Required outputs

At minimum:

- `docs/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE_REPORT.md`;
- `reports/mp4c_initial_private_k_residual_govinv_probe_20260911/province_initial_private_k_ledger.csv`;
- `.../national_capital_initialization_summary.json`;
- `.../anhui_initialization_receipt.json`;
- `.../bridge_sensitivity_beta_star.csv`;
- `.../household_validity_ledger.csv`;
- `.../residual_govinv_contract.md`;
- `.../call_ledger.json`;
- runtime/source/hash receipts;
- focused tests/static checks;
- manifest/readback;
- reproducible one-pass invocation receipt.

Do not commit private raw workbooks or protected MATLAB source.

## 15. Allowed verdicts

- `INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_PASS__ONE_PASS_PRIVATE_K_OBSERVED_AND_RESIDUAL_INITIALIZATION_ACCOUNTING_VALIDATED`
- `INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_PARTIAL__HOUSEHOLD_OR_KFE_VALIDITY_LIMITS_NUMERICAL_OBSERVATION`
- `INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_BLOCKED__PRIVATE_K_BRIDGE_OR_ALLOCATION_NOT_OBSERVABLE_WITH_CURRENT_AUTHORITY`

A PASS does not identify beta_a, does not accept HJB/KFE scientifically, does not change the production GovInv rule, and does not authorize a trajectory.

## 16. Git boundary

Use a dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit and non-force push candidate;
- do not merge main;
- do not publish successor task;
- Results eligibility remains FALSE.

Return to ChatGPT Reviewer with verdict, branch, candidate SHA, 31-province observation status, HJB/KFE validity summary, private-K/target distribution, G0 vs G1 accounting comparison, beta-star distribution, Anhui receipt, call ledger, and report path.
