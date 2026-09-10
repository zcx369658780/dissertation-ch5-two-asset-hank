# Chapter 5 MP4C corrected-2018 HJB nonconvergence propagation and 25-turn K/L rerun repair

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Repair the corrected-2018 multi-turn Python diagnostic harness so that a household HJB return with `converged=false` is recorded and propagated as a household convergence flag, rather than being treated as an immediate hard abort when finite returned arrays are available. Then rerun exactly one bounded 25-turn corrected-2018 K/L reconciliation trajectory under the already accepted runtime contract.

This task responds to Reviewer rejection of candidate `a0e117ade98f8197bb76cd2471f7932d545afbcc` for a non-source-backed premature stop rule.

The task has two ordered phases:

1. implementation repair + zero-science tests;
2. only after the repair passes static/pre-science gates, one bounded 25-turn scientific trajectory.

No parameter tuning or economic redesign is authorized.

## 2. Required authorities

Fresh-read live `origin/main`, then at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_CORRECTED_2018_25_TURN_KL_TARGET_RECONCILIATION_DIAGNOSTIC_REJECTION.md`;
- `docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_ACCEPTANCE.md`;
- accepted MATLAB multi-province logic audit;
- accepted corrected-2018 runtime source;
- rejected candidate `a0e117a...` only as historical evidence.

Protected MATLAB remains read-only.

## 3. Source-faithful household convergence contract

The accepted MATLAB audit is authority for turn ordering:

31 household calls -> migration/labor -> `At*N` capital allocation -> rah -> firm -> wage -> controller/convergence.

Household convergence flags are part of the final source steady-state predicate. They are not an independently established immediate per-province abort rule.

Therefore successor Python behavior must be:

- if HJB call returns an object with finite required arrays/scalars but `converged=false`:
  - persist the HJB return;
  - mark the province `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`;
  - continue to the source-style KFE/aggregate path if the returned operator and required arrays are finite and structurally usable;
  - carry `hjb_converged=false` into the 31-province batch and outer convergence diagnostics;
  - never count that household as converged;
  - never allow final source steady-state acceptance unless all 31 household convergence flags are true.

- stop immediately only when continuation is actually impossible, including:
  - no usable HJB return object;
  - nonfinite required HJB state/arrays/operator;
  - KFE solve raises or returns unusable/nonfinite required state;
  - malformed dimensions/order;
  - nonfinite downstream state;
  - unrecoverable exception.

KFE/HJB diagnostic-only labels remain independent scientific blockers.

## 4. Frozen corrected-2018 runtime

Use only the already accepted runtime contract:

- actual 2018 GDP;
- actual 2018 population;
- raw-NBS GFCF Track-A PIM capital;
- `delta_pim=.096`;
- `alpha=.7380939146868483`;
- `MU=10万元`, `NU=100 persons`;
- same-year Zt0;
- firm depreciation `.025`;
- GovInv0 source-faithful rule `GovInv0=Ktarget_TrackA_MU`;
- source bounds unchanged;
- source-lagged rah;
- `beta_a=1` diagnostic only;
- no new damping;
- no new hysteresis;
- no GovInv redesign;
- no Lt_seperate redesign;
- no HJB/KFE equation/tolerance/grid change.

## 5. Phase A — implementation repair

Modify the active corrected-2018 multi-turn harness only as needed to remove the unconditional rule equivalent to:

`if not hjb.converged: raise RuntimeError(...)`

Replace it with explicit diagnostic propagation.

Required metadata per province/turn:

- `hjb_converged`;
- `hjb_iterations`;
- `hjb_statistic`;
- `hjb_acceptance_classification`;
- whether downstream KFE was attempted;
- whether downstream KFE returned;
- continuation reason/status.

Do not change the household solver itself.

## 6. Phase A tests — zero science

Before any trajectory, add focused tests proving:

1. synthetic finite HJB return with `converged=false` does not trigger immediate harness abort;
2. its convergence flag remains false in the batch;
3. final source convergence predicate cannot pass with any false household convergence flag;
4. nonfinite/unusable HJB return still fails closed;
5. malformed KFE/downstream state fails closed;
6. corrected runtime pre-science binding still passes 31/31;
7. old-scale injection still fails before science;
8. no HJB/KFE/outer scientific call is required for these unit tests.

Phase A must produce a zero-science repair receipt before Phase B can start.

## 7. Phase B — one bounded 25-turn rerun

After Phase A tests pass, run exactly one corrected-2018 trajectory.

Budget:

- one trajectory only;
- maximum 25 outer turns;
- maximum 775 province household calls;
- no parameter cell comparison;
- no scientific rerun;
- no post-hoc tuning.

Engineering retry allowed only before science advances and must be logged.

A household `converged=false` flag alone is not a stop reason.

Stop early only for:

- final source steady-state predicate; or
- true hard failure preventing continuation under section 3.

## 8. K/L reconciliation outputs

If turns complete, preserve the exact prior K/L task contract.

For every province/turn record:

- Ktarget_2018_MU;
- Kt_supply_private_MU;
- GovInv before/after;
- firm total K;
- total/private/GovInv K ratios to Ktarget;
- Ltarget proxy N0_NU;
- destination firm Lt_supply;
- Lt_supply/Ltarget proxy;
- household A/B/L/C;
- raw/used ra;
- rah;
- raw/used wage;
- household composite wage;
- Y/Zt;
- controller action;
- HJB convergence/diagnostic classification;
- KFE diagnostic classification.

Focus on turns 20-25 if reached.

## 9. Additional required diagnostic

Because the previous corrected run exposed Anhui HJB nonconvergence at turn 1, report for each turn:

- number of HJB converged provinces;
- number of HJB nonconverged-but-continued provinces;
- names of those provinces;
- whether their HJB statistic improves/worsens over time;
- whether any nonconverged household later returns to converged status.

This is descriptive only. Do not tune HJB parameters from these results.

## 10. Required interpretation

At completion answer:

1. Was the previous turn-1 stop solely caused by the Python premature-abort policy?
2. Can source-style downstream K/L objects be formed despite some household nonconvergence flags?
3. What are turn-20-to-25 total K/private K/GovInv ratios to Track-A targets, if reached?
4. What are turn-20-to-25 destination labor ratios to the population proxy, if reached?
5. Does `GovInv0=Ktarget` produce observed K overshoot once private supply is included?
6. Does the controller reduce that overshoot by the late window?
7. Which provinces are HJB nonconverged over the path?
8. Are KFE/HJB diagnostic blockers still present independently?

No Results claim is allowed.

## 11. Outputs

Use a fresh evidence root such as:

`D:\ProjectTemp\ch5-corrected-2018-hjb-propagation-kl-rerun-20260910-001`

Commit at minimum:

- repaired harness/source files;
- focused tests;
- `docs/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_REPORT.md`;
- `reports/mp4c_corrected_2018_hjb_propagation_25turn_kl_20260910/phase_a_zero_science_repair_receipt.json`;
- `.../province_turn_kl_ledger.csv`;
- `.../national_turn_summary.csv`;
- `.../late_window_20_25_province_summary.csv`;
- `.../hjb_convergence_path.csv`;
- `.../anhui_trace.csv`;
- `.../govinv_k_decomposition_summary.csv`;
- `.../labor_migration_proxy_summary.csv`;
- `.../scientific_validity_ledger.csv`;
- `.../call_ledger.json`;
- runtime input receipt;
- source/hash receipt;
- tests/static-check receipts;
- manifest/readback.

Do not commit private raw XLS or protected MATLAB files.

## 12. Allowed verdicts

- `HJB_PROPAGATION_REPAIR_AND_25TURN_KL_PASS__LATE_WINDOW_RECONCILIATION_COMPLETE`;
- `HJB_PROPAGATION_REPAIR_PASS__25TURN_KL_PARTIAL_TRUE_HARD_FAILURE_BEFORE_LATE_WINDOW`;
- `HJB_PROPAGATION_REPAIR_BLOCKED__SOURCE_STYLE_CONTINUATION_NOT_IMPLEMENTABLE_WITH_CURRENT_RETURN_OBJECTS`.

PASS means the diagnostic task completed, not that the economic model is accepted.

## 13. Git and stop boundary

Use a dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- explicit staging only;
- preserve unrelated files;
- commit and non-force push;
- do not merge main;
- do not publish successor task;
- no second trajectory;
- Results eligibility remains FALSE.

Return to ChatGPT Reviewer with verdict, branch, candidate SHA, Phase-A test results, actual completed turns, HJB convergence path summary, K/L late-window summary if available, Anhui trace, call ledger, and report path.
