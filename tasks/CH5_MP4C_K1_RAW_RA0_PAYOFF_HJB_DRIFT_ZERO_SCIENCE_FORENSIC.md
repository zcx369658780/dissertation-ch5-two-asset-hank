# CH5 MP4C K1 raw `ra0` payoff HJB/drift zero-science forensic

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: zero-science forensic; no model runtime.

## 1. Goal

Use only the accepted persisted Control/Raw common-turn-1 bootstrap evidence and current source code to localize and classify the severe HJB nonconvergence and drift/control amplification caused after raw `ra0` first enters the household block at turn 2.

This task must not modify model science or run HJB/KFE/firm/trajectory. Its purpose is to determine whether the observed stress is primarily attributable to payoff-scale exposure, state/boundary concentration, accepted boundary-law interaction, or an unresolved model/numerical-authority issue that requires a new Owner decision.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`, record SHA, verify this task remains active, then read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_COMMON_TURN1_BOOTSTRAP_SAFETY_ACCEPTANCE.md`
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_COMMON_TURN1_BOOTSTRAP_SAFETY_REPORT.md`
- compact receipts under `docs/evidence/ch5_mp4c_k1_raw_ra0_payoff_bootstrap_safety/`
- accepted HJB/boundary source and prior boundary-law acceptance documents directly needed to interpret labels/drifts.

Do not restart historical parity, K1A, KFE, distance or data gates.

## 3. Scientific-call budget

New model/scientific calls are all zero:

- trajectory 0
- HJB 0
- KFE 0
- firm 0
- household 0
- MATLAB 0
- K1B 0
- K2 0
- GE/annual/IRF/Results 0.

Allowed: static source inspection, parsing persisted arrays/CSVs/JSON, hashes, NumPy/pandas calculations, zero-science scripts/tests, serialization/readback.

## 4. Required forensic decomposition

For treatment turns 2-5, compare Control versus Raw using matched province-turn and, where persisted, matched HJB state-grid coordinates.

At minimum quantify:

1. HJB convergence flag/statistic/iterations by province and turn;
2. `rah` level and Raw/Control ratio by province and turn;
3. max/percentiles of liquid drift, illiquid drift, transfer `d`, adjustment cost, consumption and any persisted controls;
4. locations of extreme finite values in `(a,b,z)` grid when coordinates are available;
5. lower/upper `a` and `b` boundary labels/policy labels for extreme cells;
6. counts/share of outward raw drifts at each boundary;
7. whether extreme Raw cells coincide with cells/provinces that were already extreme in Control;
8. whether HJB nonconvergence is concentrated in provinces with highest `rah`, highest raw `ra0`, largest drift amplification, or particular boundary regimes;
9. direct descriptive associations among `rah`, HJB statistic, iteration ceiling, drift extrema, adjustment cost and boundary counts.

All associations are descriptive, not causal estimates.

## 5. Baseline-versus-incremental attribution

The report must explicitly separate:

- large magnitudes already present under Control;
- incremental amplification unique to Raw;
- new boundary/outward-drift events that appear only after Raw payoff enters;
- cases where Raw is smaller than Control.

Do not describe a magnitude as a raw-payoff pathology merely because it is large in absolute terms if Control is similarly large.

## 6. Source-law tracing

Trace, with exact source path/line evidence, how `r_a/rah` enters the accepted HJB and how it affects:

- effective illiquid return;
- consumption/FOCs where applicable;
- transfer `d`/adjustment-cost terms;
- liquid and illiquid drifts;
- accepted boundary selectors/laws.

Do not infer equations from variable names when source evidence is available.

## 7. KKT/boundary authority

The accepted runtime return object lacks a standalone KKT residual. Do not fabricate one.

Use only already-persisted policy/boundary labels and source-law invariants. If a required KKT object is unavailable, classify it `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`.

## 8. Required classification

End with one evidence-based classification, e.g. a truthful variant of:

- `RAW_PAYOFF_STRESS_PRIMARILY_SCALE_EXPOSURE_WITH_ACCEPTED_BOUNDARY_LAWS`
- `RAW_PAYOFF_STRESS_CONCENTRATED_IN_SPECIFIC_BOUNDARY_REGIMES__OWNER_DECISION_REQUIRED`
- `RAW_PAYOFF_STRESS_NOT_ATTRIBUTABLE_WITH_CURRENT_PERSISTED_EVIDENCE__NEW_DIAGNOSTIC_AUTHORITY_REQUIRED`

Do not authorize runtime changes yourself.

## 9. Next-gate recommendation

Recommend exactly one next gate:

A. Owner scientific decision on payoff mapping/scale interpretation;
B. a bounded diagnostic-only runtime with additional existing-output instrumentation but no science change;
C. a source/boundary-law authority review;
D. another zero-science provenance closure.

Do not enter K1B/K2 or extend to 25 turns.

## 10. Allowed tracked changes

Allowed:

- one zero-science forensic script if needed;
- focused zero-science tests;
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC_REPORT.md`;
- compact receipts under `docs/evidence/ch5_mp4c_k1_raw_ra0_hjb_drift_forensic/`;
- truthful CURRENT closeout docs.

Prohibited:

- any `src/` model-science change;
- payoff mapping change;
- caps/bounds/normalization/smoothing;
- HJB/KFE equations;
- boundary laws/KKT law;
- firm/C1/labor/capital-network science;
- calibration/grid/tolerance/solver changes;
- K1B/K2/Results.

## 11. Git/publication

Use fresh isolated worktree/branch, explicit stage paths, one coherent commit, non-force push, one remote readback. Do not merge main or publish successor task.

## 12. Final Builder response

Return classification, baseline SHA, worktree/branch/commit, changed paths, zero-call ledger, province/turn/grid forensic findings, baseline-vs-incremental attribution, source-law trace, KKT availability statement, unique recommended next gate, and Results eligibility=`FALSE`.
