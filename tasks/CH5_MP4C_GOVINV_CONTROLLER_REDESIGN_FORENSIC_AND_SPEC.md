# Chapter 5 MP4C GovInv controller redesign forensic and specification

Date: 2026-09-11. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Perform a zero-science forensic and redesign specification for the province-level GovInv controller after the accepted G1 experiment established that residual initialization aligns initial capital but the unchanged historical clipped-return controller recreates the same GovInv overshoot.

Do not implement a new production controller and do not run a scientific trajectory.

## 2. Required authority

Fresh-read live `origin/main`, then at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- G1 isolated diagnostic report and Reviewer acceptance;
- initial private-K residual GovInv probe report and acceptance;
- accepted G0 25-turn report and acceptance;
- accepted GovInv/labor redesign spec and acceptance;
- current corrected-2018 runtime, controller/adaptation harness, firm and capital allocation code;
- protected MATLAB `HANK_mp_1eq.m`, `HANK_mp_1turn.m`, `HANK_firm.m` if accessible, read-only.

## 3. Frozen accepted facts

Treat as accepted evidence, not hypotheses:

- G1 `GovInv0=max(Ktarget-Kt_supply_initial,0)` aligned initial accounting K to target for 31/31 under diagnostic beta=1.
- G1 turn-1 median total-K/target = 1.0.
- unchanged controller then produced 0/289/486 decrease/increase/hold actions, identical to G0 totals.
- turns 20-25 G1 pooled median total-K/target = 2.353363495591088.
- turns 20-25 G1 pooled median GovInv/target = 2.3503561274071445.
- turns 20-25 G1 pooled median private-K/target = 0.0029186382400614363.
- selected-turn raw-ra region counts were identical to G0.
- HJB/KFE blockers remain independent; Results eligibility is false.

## 4. Recover exact historical controller semantics

Document source timing and inputs precisely:

- when `maxKNratiogap<0.1` opens the adaptation gate;
- whether Zt adjustment occurs before GovInv adjustment;
- whether the GovInv trigger uses raw or clipped `ra`;
- thresholds relative to `ramin/ramax`;
- exact `*0.9`, `*1.1`, or hold behavior;
- when `tKNratio` is updated and damped;
- whether the controller has any explicit Ktarget/Kt residual term;
- whether GovInv is interpreted economically as public capital, a residual stock, or only a numerical control variable in source.

## 5. Explain the failure mechanism

Using only accepted ledgers and static algebra, explain why a high-ra signal can repeatedly trigger `GovInv*=1.1` even after G1 initializes K at target.

Separate:

- return-side trigger;
- capital-level target;
- KN/Y/Z feedback;
- clipped-return information loss;
- multiplicative compounding;
- adaptation-gate intermittency.

Do not infer causality beyond evidence.

## 6. Candidate controller families

Compare at least four families without implementing them:

C0 — historical controller

`ra` near bounds -> GovInv `*0.9/*1.1`.

C1 — capital-target residual controller

GovInv updated from the gap between target productive K and private K, e.g. a generic form

`GovInv_next = max(GovInv + lambda_K*(Ktarget - (Kprivate + GovInv)),0)`

or an equivalent residual-level formulation.

Do not choose `lambda_K`.

C2 — return-target controller

Use an interior target return `ra_target` rather than bound proximity, with explicit signed error. Do not choose target or gain unless source/data authority uniquely identifies it.

C3 — staged/hybrid controller

First close capital-level alignment, then only after a declared gate use return/GDP/KN corrections. Specify state-machine logic conceptually and identify hysteresis/damping decisions that would require Owner approval.

Optionally add C4 only if source evidence motivates another distinct family.

## 7. Required comparison dimensions

For every family report:

- control objective;
- observed signal;
- target/reference object;
- sign logic;
- positivity handling;
- whether Ktarget enters directly;
- whether clipped or raw ra enters;
- expected response to the accepted G1 path;
- dimensional consistency;
- source authority;
- economic interpretation;
- numerical-stability risk;
- tuning degrees of freedom;
- risk of convergence-driven overfitting;
- interaction with Zt and tKNratio;
- interaction with normalized labor if later activated;
- minimum future scientific call budget required for testing.

## 8. Static counterfactual replay

Allowed: replay accepted G1 ledger values through controller formulas as pure post-processing with zero model calls.

For C0, reproduce recorded actions exactly.

For C1/C2/C3, only if a candidate can be written without choosing unapproved coefficients, report symbolic action direction or normalized unit-gain diagnostic geometry. Do not invent gains and do not claim trajectory outcomes.

If useful, compute province-turn signs such as:

- `Ktarget - totalK`;
- `ra_raw - ra_reference` only where a reference is source-authorized;
- whether C0 action direction moves total K toward or away from Ktarget in the next static accounting sense.

## 9. Key forensic question

Quantify from accepted G1 ledgers how often the historical controller action is directionally inconsistent with the observed capital-level gap.

Example classification:

- total K above target + controller increases GovInv -> `CAPITAL_GAP_WORSENING_DIRECTION`;
- total K below target + controller decreases GovInv -> same classification;
- otherwise `CAPITAL_GAP_CLOSING_OR_NEUTRAL_DIRECTION`.

This is a static directional classification only, not a dynamic causal estimate.

## 10. Owner decision matrix

Explicitly isolate decisions that Reviewer must not make automatically, including:

- whether GovInv is to be economically interpreted as public capital or retained as a residual/numerical balancing stock;
- whether controller objective should primarily target K level, return, or a staged combination;
- whether raw `ra` may replace clipped `ra` as controller signal;
- whether damping/under-relaxation is admissible;
- whether hysteresis is admissible;
- whether Zt and GovInv should be adjusted in the same turn;
- whether a fixed Ktarget should remain the controller reference during iteration;
- whether public-capital data should be introduced later.

## 11. No-science boundary

Scientific/model calls must all be zero:

- HJB/KFE/household;
- migration/normalized migration;
- firm;
- controller runtime;
- outer turn/trajectory;
- steady state;
- root/Brent scientific solves;
- MATLAB runtime;
- GE/annual/IRF/Results.

Allowed: source reading, accepted-ledger parsing, deterministic arithmetic, static replay, tests, serialization, hashes.

## 12. Required outputs

At minimum:

- `docs/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC.md`;
- `reports/mp4c_govinv_controller_redesign_20260911/controller_source_timing_map.md`;
- `.../controller_candidate_matrix.csv`;
- `.../g1_static_directional_forensic.csv`;
- `.../controller_direction_summary.json`;
- `.../owner_decision_matrix.csv`;
- `.../zero_scientific_call_ledger.json`;
- source/hash receipt;
- focused static test receipt;
- manifest/readback.

## 13. Required answers

1. Why does C0 recreate overshoot after G1?
2. How often does C0 move GovInv in a direction that worsens the current Ktarget gap?
3. Is C0 fundamentally a return-bound controller rather than a capital-target controller?
4. Is C1 structurally coherent with the now-accepted G1 initialization?
5. What additional scientific choices are required before C1 can be implemented?
6. Would C2 or C3 require more unverified tuning than C1?
7. Should initialization and controller remain separate in the production architecture?
8. What is the lowest-risk next implementation experiment after Owner review?

## 14. Allowed verdicts

- `GOVINV_CONTROLLER_REDESIGN_SPEC_PASS__HISTORICAL_CONTROLLER_FAILURE_MECHANISM_QUANTIFIED_AND_CANDIDATES_SEPARATED`
- `GOVINV_CONTROLLER_REDESIGN_SPEC_PARTIAL__OWNER_OBJECTIVE_OR_SIGNAL_DECISION_REQUIRED`
- `GOVINV_CONTROLLER_REDESIGN_SPEC_BLOCKED__ACCEPTED_EVIDENCE_INSUFFICIENT_FOR_CONTROLLER_FORENSIC`

PASS/PARTIAL are design evidence only and do not authorize a new controller automatically.

## 15. Git boundary

Dedicated branch/worktree; no force push/reset/clean/stash; explicit staging only; commit and non-force push; do not merge main; do not publish a successor scientific task; Results eligibility remains FALSE.
