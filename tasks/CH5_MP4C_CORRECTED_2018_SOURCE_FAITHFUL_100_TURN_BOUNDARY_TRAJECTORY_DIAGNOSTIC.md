# CH5 MP4C corrected-2018 source-faithful 100-turn boundary trajectory diagnostic

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Run exactly one bounded, source-faithful corrected-2018 multi-province trajectory of at most 100 outer turns to answer a narrow question:

> Do the large initial firm-price boundary-hit counts decline toward the admissible interior under the existing ordered MATLAB-style update map, or do they persist/oscillate after 50-100 turns?

This is a diagnostic trajectory, not a production steady-state acceptance and not Results.

## 2. Required authority

Fresh-read live main and at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_FIRM_PRICE_NORMALIZATION_AND_HOUSEHOLD_MACRO_BRIDGE_FORENSIC_REPORT.md`;
- its Reviewer acceptance;
- `docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_REPORT.md`;
- accepted corrected/raw-NBS 2018 data reports;
- accepted MATLAB multi-province logic audit;
- current Python multi-province implementation/harness source actually used for execution.

Protected MATLAB remains read-only.

## 3. Frozen scientific inputs

Use the already accepted diagnostic 2018 contract:

- actual 2018 GDP;
- actual 2018 population;
- raw-NBS GFCF Track-A PIM capital;
- `delta_pim=.096`;
- `alpha_raw=.7380939146868483`;
- `alpha_used=.7380939146868483`;
- common macro units `MU=10万元`, `NU=100 persons`;
- protected firm depreciation `.025` remains separate from PIM depreciation;
- protected/source `mt` equation, including the accepted `mt0=.92` initialization finding;
- existing `ra` safety bounds `[.02,.09]`;
- existing `wjt` bounds `[.8,1.3]`;
- existing GovInv/Zt controller logic and ordering unless the current accepted Python source already differs and the difference is explicitly reported.

No parameter may be tuned after execution starts.

## 4. Source-faithful numerical choices for this diagnostic

Freeze the baseline to minimize redesign contamination:

- household-to-macro asset bridge: source-faithful implicit `beta_a=1`, **diagnostic only**;
- `rah` timing: source-lagged prior-clipped-`ra` route;
- new `w/rah` damping: OFF for this baseline (`lambda_w=lambda_rah=1`);
- no new hysteresis beyond current source logic;
- no new GovInv damping;
- no new price bounds;
- no solver-family replacement;
- no KFE boundary repair;
- no HJB-loop repair.

These choices do not become production authority even if the trajectory improves.

## 5. Execution budget

One trajectory only.

Maximum:

- outer turns: 100;
- province household updates: at most `100*31=3100`;
- no second trajectory;
- no rerun with different parameters;
- no retry after a scientifically completed trajectory;
- engineering retry only if execution fails before any scientific state is advanced, and it must be logged.

Stop early only if:

1. the source final steady-state predicate is satisfied; or
2. a hard scientific failure occurs (nonfinite state, household nonconvergence where source contract requires stopping, malformed operator/density that prevents continuation, unrecoverable exception).

Do not stop merely because some provinces hit price bounds.

## 6. Mandatory per-turn ledger

For every completed turn, record at least:

- turn index;
- `ra_lower_hit_count`;
- `ra_upper_hit_count`;
- `wjt_lower_hit_count`;
- `wjt_upper_hit_count`;
- province names for each hit set;
- raw `ra` min/median/max;
- used/clipped `ra` min/median/max;
- raw `wjt` min/median/max;
- used/clipped `wjt` min/median/max;
- household composite `rah` min/median/max;
- household composite `w` min/median/max;
- household convergence count;
- max `abs(KNratio/tKNratio-1)`;
- max `abs(Y/Y_prev-1)`;
- max `abs(Y/Y0-1)`;
- number of provinces with Zt adjustment;
- number of provinces with GovInv decrease/increase/hold;
- min/median/max GovInv;
- min/median/max At, Bt, Lt, Ct when available;
- KFE/density validity diagnostics already required by current scientific gates, including upper-b leakage/source-free residual if available from the current implementation;
- any source final-convergence predicate component.

The trajectory ledger must be machine-readable.

## 7. Boundary-decay analysis

Analyze turn windows:

- 1-10;
- 11-25;
- 26-50;
- 51-75;
- 76-100 (if reached).

For both `ra` and `wjt`, classify the boundary path as one of:

- `BOUNDARY_HITS_DECAY_TO_ZERO`;
- `BOUNDARY_HITS_MATERIALLY_DECLINE_BUT_NOT_ZERO`;
- `BOUNDARY_HITS_PERSIST_HIGH`;
- `BOUNDARY_HITS_OSCILLATE_WITHOUT_DECAY`;
- `INSUFFICIENT_TURNS_DUE_TO_EARLY_HARD_FAILURE`.

Use counts and province identities, not visual impressions.

Also identify provinces that remain on the same bound for the longest consecutive run.

## 8. No false steady-state claim

Even if the source final predicate happens to pass, separately report:

- source convergence status;
- household/HJB convergence;
- KFE/source-free stationarity validity;
- HJB-loop operator validity;
- whether any known diagnostic blocker remains.

A source-loop convergence event does not automatically make Results eligible.

## 9. Anhui trace

Provide a dedicated Anhui turn-by-turn or selected-turn trace for:

- raw/used `ra`;
- raw/used `wjt`;
- `rah`;
- household `w`;
- At, Bt, Lt, Ct;
- Kt_supply if available;
- GovInv;
- firm K;
- Y;
- Zt;
- K/N gap;
- GDP gap;
- KFE validity flag.

Selected-turn summary must at least include turns 1,2,3,5,10,25,50,75,100 when they exist.

## 10. Required interpretations

At completion answer directly:

1. Do `ra` boundary hits decline toward zero by turn 50 or 100?
2. Do wage-bound hits decline, despite unresolved absolute wage normalization?
3. Which provinces are persistent boundary offenders?
4. Does GovInv/Zt control move the system toward or away from the admissible region?
5. Is the path convergent, slowly convergent, oscillatory, or divergent by the recorded gaps?
6. Does the corrected-data path reproduce the previously observed turn2->turn3 asset collapse?
7. If an asset collapse occurs, does it precede, coincide with, or follow a major `rah/ra/w/GovInv/Zt` change?
8. Are KFE/HJB diagnostic blockers still present, and do they prevent economic acceptance even if the outer path improves?

Do not change parameters to improve these answers.

## 11. Evidence root and outputs

Use fresh root:

`D:\ProjectTemp\ch5-corrected-2018-100turn-boundary-trajectory-20260910-001`

Required repo-safe outputs:

- `docs/CH5_MP4C_CORRECTED_2018_100_TURN_BOUNDARY_TRAJECTORY_DIAGNOSTIC_REPORT.md`;
- `reports/mp4c_corrected_2018_100turn_boundary_trajectory_20260910/turn_ledger.csv`;
- `.../boundary_hit_province_ledger.csv`;
- `.../window_decay_summary.csv`;
- `.../anhui_trace.csv`;
- `.../controller_action_summary.csv`;
- `.../scientific_validity_ledger.csv`;
- `.../call_ledger.json`;
- focused tests/static checks;
- manifest/readback;
- reproducible bounded execution harness or explicit invocation receipt.

Do not commit private raw XLS/workbooks or protected MATLAB files.

## 12. Allowed primary verdicts

- `CORRECTED_2018_100TURN_DIAGNOSTIC_PASS__BOUNDARY_HITS_DECAY_AND_SOURCE_PATH_APPROACHES_INTERIOR`;
- `CORRECTED_2018_100TURN_DIAGNOSTIC_PARTIAL__BOUNDARY_HITS_DECLINE_BUT_PERSIST`;
- `CORRECTED_2018_100TURN_DIAGNOSTIC_FAIL__BOUNDARY_HITS_PERSIST_OR_OSCILLATE`;
- `CORRECTED_2018_100TURN_DIAGNOSTIC_BLOCKED__EARLY_HARD_SCIENTIFIC_FAILURE`.

These verdicts describe trajectory behavior only.

## 13. Git and stop boundary

Use a dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit and push once evidence is complete;
- do not merge main;
- do not publish a successor task;
- do not run a second parameter cell;
- Results eligibility remains FALSE.
