# CH5 MP4C K1 — HJB convergence-mechanism turn1/turn2 exact-input diagnostic

Date: 2026-09-13
Task ID: `CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC`
Type: bounded scientific diagnostic / observation-only HJB replay.

## Goal
Explain the accepted annual G2 control-path HJB convergence collapse from turn1 `20/31` converged calls to turn2 `2/31` without changing any scientific parameter, guard, equation, grid, tolerance, iteration ceiling or solver semantics.

The task is mechanism diagnosis, not repair. Determine whether failed calls are best characterized by monotone-slow convergence, stagnation, oscillation/short-cycle behavior, policy chattering, derivative-safeguard domination/pathology, operator/value-update amplification, price-input-associated regime change, or another source-backed mechanism.

## Mandatory authority
Read live `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`, `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT_20260913_D1.md`, `docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_REVIEW_FREEZE_CURRENT.md`, D1 freeze, raw-census acceptance, D1 runtime acceptance/report, and accepted annual-HJB / price-guard / bilateral-capital / same-S / C1 authority docs. Read the currently active HJB implementation and the accepted G2-control evidence producer before changing diagnostics.

## Frozen science
Keep exactly unchanged:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`, `rb=.02/year`, borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`, `Q_z` off-diagonal `1/3/year`;
- `chi0=.1`, `chi1=2 years`;
- accepted transfer FOC, candidate generation, selector scoring/labels and boundary/KKT law;
- derivative floor/safeguard and all derivative formulas;
- HJB equation, pseudo-time/update law, linear solver, tolerance, 100-iteration ceiling and grids;
- G2 return guard `r_a in [-.10,.35]`;
- wage safeguard `wjt in [.8,1.3]`;
- fixed theta, `beta_distance=2`, `beta_return=0`;
- accepted destination-by-origin `S`, same-S quantity/payoff, source-faithful labor and C1 accounting;
- K1B/K2 OFF.

Primary replay object is accepted fresh G2 **control with D1 OFF**. Do not run D1 treatment, D2/D3/OFF continuation, G3/G4 or wage relaxation.

## Phase 0 — exact evidence/input reconstruction, zero science

Use the accepted D1-control sealed/compact evidence and task-owned accepted runtime artifacts to reconstruct the exact HJB call inputs for all 31 provinces at control turn1 and control turn2.

For every reconstructable call, persist an identity receipt covering at least province, turn, entering `V` identity/hash, grid identity, numerical parameters, consumed `r_a`, wage and guard state, transfer-control state=D1 OFF, relevant source/config identity and any state needed to replay the accepted HJB call.

Cross-check reconstructable inputs against persisted accepted receipts/hashes. Do not approximate, interpolate or substitute a nearby state. If a call cannot be proven exact, mark it `REPLAY_INPUT_IDENTITY_UNPROVEN` and do not replay that call.

Prefer the full 62-call cross-section. Missing exact-input identity for a subset is not permission to synthesize inputs; report the coverage limitation.

## Phase 1 — observation-only instrumentation

Add narrowly scoped, default-OFF HJB instrumentation sufficient to record per-iteration evidence without altering scientific outputs or solver control flow.

Required per-iteration observations where defined:

1. existing convergence statistic;
2. `||V_new-V_old||_inf`, argmax cell and signed `V_new-V_old` at that cell;
3. optional `||V_n-V_{n-2}||_inf` from stored diagnostic history, computed outside scientific state, to expose 2-cycle signatures;
4. policy/selector-label switch count from previous HJB iteration and two-step reversion count where labels permit it;
5. raw versus safeguarded `V_b^F`, `V_b^B`, `V_a^F`, `V_a^B` summaries, derivative-floor hit counts/shares, nonpositive/nonfinite raw derivative counts, and max raw-to-used derivative deviation;
6. consumption, labor, selected transfer, adjustment cost, `mu_a`, `mu_b`, liquid/illiquid drift extrema and selected quantiles needed for event ordering;
7. HJB operator diagnostics available without changing construction: max absolute row-sum defect, minimum off-diagonal entry or equivalent accepted generator/admissibility diagnostic;
8. linear/direct solve residual `||A V_new-rhs||` or equivalent residual from the exact accepted solve expression, computed post-solve only and not fed back;
9. consumed return/wage values and return/wage guard-hit state.

Raw quantities and safeguarded/used quantities must remain separately identifiable. Diagnostic arrays may be downsampled or summarized for repository evidence, but the external run artifact must retain enough information to reproduce classifications and first-event ordering.

Instrumentation must not change call order, candidate values, policy selection, sparse operator, RHS, solve expression, value update, convergence test or iteration count.

## Phase 2 — instrumentation parity gate

Before the cross-section replay, prove observation-only behavior on one exact accepted call input using exactly two HJB calls:

- instrumentation OFF;
- instrumentation ON.

Require exact equality of scientific outputs, convergence flag, iteration count, final values/controls/policies/operator-relevant outputs and any existing deterministic scientific receipt fields, excluding only newly added diagnostics/metadata.

If exact parity fails, hard stop before cross-section replay. Do not repair by changing tolerance or scientific arithmetic.

## Phase 3 — bounded exact-input replay

Replay each proven-exact accepted control input at most once with instrumentation ON:

- 31 province calls for turn1 where identity is proven;
- 31 province calls for turn2 where identity is proven.

No KFE and no outer-state advancement. These are isolated HJB call replays only.

Scientific budget:

- parity gate: exactly 2 HJB calls;
- cross-section replay: at most 62 HJB calls, one per proven-exact province-turn input;
- total HJB calls: at most 64;
- HJB internal iterations/direct solves: whatever the frozen accepted 100-iteration ceiling naturally produces, counted truthfully;
- KFE=0;
- MATLAB=0;
- outer multi-province turns/trajectory advancements=0;
- standalone KFE=0;
- K1B/K2/GE/annual downstream/shock/IRF/Results=0;
- scientific retries after an HJB call begins=0.

One engineering retry is allowed only before any HJB invocation for path/import/serialization/output-shape defects. After scientific calls begin, preserve failures and do not rerun a consumed province-turn call.

## Pre-registered analysis metrics

Do not invent a pass/fail threshold after seeing outcomes. Report continuous metrics first.

For every call record:

- converged or ceiling-hit;
- iterations used;
- full convergence-stat trajectory;
- final/initial and last-20 convergence-stat ratios;
- fraction of last-20 steps in which the convergence statistic decreases;
- last-20 range and coefficient of variation where finite;
- one-step value-update norm and two-step value-distance norm trajectories;
- two-step/one-step norm ratio where defined;
- policy switch and two-step reversion trajectories;
- derivative-floor hit trajectory and raw-to-used derivative deviations;
- operator and solve-residual trajectories;
- price inputs/guard states.

Mechanism labels may be assigned only from these preregistered traces. If a numerical threshold beyond exact zero/finite/invariant checks is introduced after observing outcomes, label that conclusion `POST_HOC_DESCRIPTIVE`, not a gate.

## Required comparison groups

Produce province-level and aggregate summaries for:

1. turn1 converged;
2. turn1 ceiling/failure;
3. turn2 converged;
4. turn2 ceiling/failure.

Also identify provinces that transition from turn1 converged to turn2 failed and compare their event sequences. This is a sequential-state association, not a same-state causal comparison.

The report must explicitly distinguish:

- direct replay facts;
- cross-group association;
- temporal/event ordering;
- causal claims that are **not** supported.

## Earliest-event review

For each failed replay, identify the earliest iteration at which any preregistered pathology indicator becomes materially visible in the raw trace, without retroactively tuning a threshold. At minimum inspect ordering among:

`price inputs/guard state -> raw derivatives -> derivative safeguard hits -> candidate/policy switching -> drifts/operator -> linear-solve residual -> value update -> next-iteration derivatives/statistic`.

Then determine whether one event family consistently precedes the convergence plateau/oscillation across failed calls and whether the same event is absent/weaker in converged calls.

If no common early mechanism is supported, say so rather than forcing a single cause.

## Questions to answer

1. Is the dominant failure signature monotone-slow, stagnating, oscillatory/short-cycle, policy-chattering, derivative-safeguard dominated, operator/solve dominated, price-associated, mixed, or unresolved?
2. What distinguishes turn1 converged from turn1 failed calls?
3. What changes most systematically between turn1 and turn2, especially for provinces that switch from converged to failed?
4. Do derivative-floor hits precede failure, merely co-occur, or remain weakly related?
5. Do operator invariants or linear-solve residuals fail before value/policy instability?
6. Are return/wage guard states strongly associated with failure after conditioning on turn/group, without changing the guards?
7. Is there evidence that the current 100-iteration HJB map is simply too slow, or does it exhibit plateau/cycle behavior that makes a longer ceiling scientifically unmotivated?
8. Which **one** next isolated family is best supported for a future Owner gate: derivative/value contract, return interface, wage interface, HJB solution-method contract, boundary/selector, or unresolved/no intervention?

## Hard stops

Stop scientific execution on:

- instrumentation ON/OFF scientific parity failure;
- exact replay-input identity failure for the parity call;
- any diagnostic code feeding values back into scientific state/control flow;
- scientific NaN/Inf exception not already represented by the accepted call semantics;
- unauthorized parameter/equation/guard/grid/tolerance/solver/iteration-ceiling change;
- same-S/provenance corruption discovered in the reconstructed accepted inputs.

For a subset-specific replay identity failure, skip that call and continue only with independently proven-exact calls; report coverage. Do not synthesize a replacement input.

## Allowed changes

Only:

- default-OFF observation-only instrumentation in the accepted HJB path or a task-owned wrapper that can prove exact scientific parity;
- task-owned exact-input reconstruction/replay/analysis scripts;
- focused tests for diagnostic identities and serialization;
- report `docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2/`;
- truthful closeout updates to CURRENT status/rule-index/handoff only if needed by the completed task.

Do not modify original protected MATLAB or unrelated source.

## Git / publication

Fresh-fetch live main before starting and record actual baseline. Use a fresh isolated worktree/branch. Preserve unrelated dirty work. No reset/clean/stash/force push. Explicitly stage authorized paths; no `git add .` or `git add -A`.

One coherent Builder commit, non-force push, remote readback. Do not merge main and do not publish a successor task. External run artifacts use a fresh no-overwrite evidence root; compact evidence may be committed subject to repository size policy.

## Required report/final response

Return outcome first and include:

- classification;
- actual baseline, branch, worktree and candidate SHA;
- changed paths;
- exact-input replay coverage out of 62;
- instrumentation parity result;
- complete scientific call ledger;
- turn1/turn2 convergence reproduction;
- four-group mechanism summaries;
- province transition analysis;
- derivative-floor/value-update/policy/operator/solve-residual findings;
- return/wage association findings without guard changes;
- earliest-event ordering assessment;
- whether a longer iteration ceiling is supported or not;
- exactly one recommended next Owner gate;
- KFE/KKT caveat;
- `Results eligibility=FALSE`.

Stop after publication. Reviewer performs independent acceptance and decides any next scientific intervention.
