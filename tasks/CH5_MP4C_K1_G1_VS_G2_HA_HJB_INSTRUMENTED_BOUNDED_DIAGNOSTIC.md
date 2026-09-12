# CH5 MP4C K1 — G1 vs G2 HA/HJB instrumented bounded diagnostic

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: bounded scientific runtime diagnostic with observation-only instrumentation.

## 1. Goal

Repeat the already accepted annual G1/G2 five-turn continuation design with scientific inputs unchanged, while adding task-bounded diagnostic instrumentation needed to identify where G2 first departs from G1 inside the HA/HJB solve.

The key scientific distinction is:

- turn 2: G1/G2 enter from the same completed turn-1 scientific state; differences are an immediate common-entering-state response to the two frozen HJB return guards;
- turns 3-5: paths have endogenous state-history divergence and must be analyzed as propagation, not same-state causal comparisons.

This task does not tune or repair the model.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`, record actual SHA, and verify this exact task is active. Read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_REPORT.md`;
- `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC_ACCEPTANCE.md`;
- `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC_REPORT.md`;
- active HJB/policy/economics/household adapter source.

Do not redo data, annual-time-base, capital-network, parity or source-provenance audits.

## 3. Frozen science

Use exactly the accepted annual K1A contract:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`;
- `rb=.02/year`;
- borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`;
- `Q_z` off-diagonal `1/3/year`;
- annual corrected `Y/K` and after-tax profit/K unchanged;
- `ra0_annual=rk+after_tax_profit_over_K-.10`;
- `chi0=.1`, `chi1=2 years`;
- fixed theta;
- `beta_distance=2`;
- `beta_return=0`;
- accepted destination-by-origin `S`;
- same `S` for capital quantity and payoff;
- source-faithful labor;
- smoothing OFF;
- partial adjustment OFF;
- C1 unchanged;
- K1B/K2 OFF.

Price safeguards remain frozen:

- G1 HJB `r_a in [-.05,.20]`;
- G2 HJB `r_a in [-.10,.35]`;
- firm wage safeguard `wjt in [.8,1.3]` in both paths.

No guard value may be changed.

## 4. Two-path runtime design

Run exactly G1 and G2, each from byte-identical accepted initialization, at most 5 completed outer turns.

Turn 1 must remain the common bootstrap and must be scientifically identical across paths.

Turns 2-5 use each path's own immediately prior completed annual raw `ra0 @ S`, followed only by the frozen path-specific HJB-interface return guard.

No cross-path borrowing and no same-turn return feedback.

## 5. Observation-only instrumentation rule

Instrumentation may expose and persist existing intermediate values, but must not alter any value used by the accepted scientific calculation.

The instrumented and non-instrumented result for a given scientific input must be numerically identical within exact/accepted floating readback tolerance. Before the full trajectories, prove this on focused single-call fixtures or accepted small fixtures without changing the scientific algorithm.

Instrumentation must never:

- clip, floor, normalize or replace an intermediate;
- reorder candidate selection;
- change floating formulas;
- add a solver stopping rule;
- change matrix/operator assembly;
- change policy labels;
- change call ordering that alters scientific state.

If an intermediate cannot be exposed without altering science, mark it `UNAVAILABLE_WITHOUT_SCIENCE_CHANGE` and continue with the remaining authorized instrumentation.

## 6. Mandatory HJB iteration trace

For every province HJB call, persist per HJB iteration, at least:

- iteration number;
- convergence statistic `max(abs(V_new-V_old))`;
- converged flag / final iteration count;
- min/median/p95/p99/max or abs-max of `V` where practical;
- count of NaN/Inf;
- counts of liquid and transfer selected labels;
- counts of derivative-floor/safeguard activations if the active source already computes or can expose them without science change.

Do not store every full array at every iteration if that would be excessive; compact per-iteration summaries plus selected checkpoint arrays are preferred. Persist full arrays for explicitly selected diagnostic checkpoints below where feasible.

## 7. Directional/value derivative instrumentation

Expose existing directional/raw derivative objects actually used by the HJB/policy code, including where available:

- liquid forward/backward derivatives;
- illiquid forward/backward derivatives;
- raw `V_b` object used in transfer FOC;
- any derivative floor applied before consumption/FOC;
- floor activation count and grid coordinates;
- min/median/p95/p99/max/abs-max per derivative object.

Names must follow source semantics. Do not invent `V_a`/`V_b` variants not present in source.

## 8. Pre-selector candidate instrumentation

Before final liquid/transfer policy selection, persist the candidate objects already computed by active source, where available:

- candidate consumption/labor controls;
- transfer candidates `d`;
- adjustment cost by candidate;
- candidate `mu_a` and `mu_b`;
- candidate effective illiquid return contribution;
- candidate Hamiltonian / comparison score / selector criterion actually used;
- candidate inward/outward feasibility indicators;
- boundary-specific candidates/guards;
- selected candidate label.

For every extreme selected cell, preserve the candidate table that led to selection if available without science change.

Do not infer missing candidate scores from final labels alone.

## 9. Turn-2 common-entering-state causal window

Turn 2 is the highest-priority diagnostic because G1/G2 have the same completed turn-1 scientific state before different return guards are applied.

For all 31 provinces at turn 2, verify and persist:

- entering household state hash/equality before the return guard;
- same raw annual `ra0` source and converted `rah` before guard;
- G1/G2 consumed `r_a`;
- same wage input before/after the unchanged wage guard;
- same grids, parameters and initial HJB value state;
- first iteration where any persisted HJB intermediate differs;
- first iteration where selected liquid/transfer labels differ;
- first iteration where convergence statistic materially diverges;
- first iteration/cell where `|d|`, cost, `|mu_a|` or `|mu_b|` crosses the matched path by a large finite factor; report exact values, do not create a new pass threshold.

The turn-2 comparison may be described as `COMMON_ENTERING_STATE_IMMEDIATE_RESPONSE` because scientific state is common before guard application.

## 10. Turns 3-5 propagation window

For turns 3-5, label comparisons:

`PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL`.

Persist the same iteration/candidate summaries, but do not claim a direct causal effect of the guard at a later turn without a same-state replay.

No new same-state replay is authorized in this task unless it can be produced without additional scientific calls from already entered states. Do not add hidden re-solves.

## 11. Priority province/cell checkpoints

At minimum give high-resolution instrumentation for:

- 湖北 turn 2, including the previously observed interior global extreme cell `(i_b=1,i_a=18,i_z=0)`;
- 四川 turn 4, including the prior worst-HJB upper-b context;
- 山东 turn 2 as a previously newly-unsaturated high-statistic case;
- at least one G1-extreme case that improved sharply under G2, e.g. 云南 turn 4, if reached and persisted.

Also include the worst newly observed turn-2 common-state divergence if it differs from these preregistered checkpoints.

## 12. Price-bound monitoring

Continue the Owner-required MATLAB-style monitoring for every province and turn:

Return:
- raw `ra0_annual`;
- converted `rah`;
- guarded HJB `r_a`;
- upper/lower/unsaturated flag;
- province-name lists and counts/shares.

Wage:
- raw/pre-guard wage if available;
- guarded `wjt`;
- upper/lower/unsaturated flag using the frozen active criterion;
- province-name lists and counts/shares.

Ideal long-run target remains `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`; this task does not attempt to reach it.

## 13. Pre-run gates

Before scientific execution prove:

1. live task and baseline identity;
2. exact annual calibration;
3. exact G1/G2 return guards;
4. exact wage guard `[.8,1.3]`;
5. G1/G2 initial payload equality except path/guard designation;
6. turn-1 common bootstrap contract;
7. instrumentation-on versus instrumentation-off focused parity for scientific outputs on small/accepted fixtures;
8. instrumentation does not modify source equations/selection/scientific outputs;
9. same-S/K1/C1/source-faithful labor contracts unchanged;
10. solver/grid/tolerance/boundary/KKT laws unchanged;
11. K1B/K2 OFF.

Any failure blocks science.

## 14. Runtime budget

Maximum:

- trajectory invocations: 2 total;
- G1: at most 5 completed turns;
- G2: at most 5 completed turns;
- HJB calls: at most 310 total;
- KFE calls: at most 310 total;
- MATLAB: 0;
- standalone KFE: 0;
- K1B/K2/GE/annual downstream/shock/IRF/Results: 0.

Scientific retries after state advancement: 0.

One pre-state-update engineering retry is allowed only for instrumentation serialization/output-shape defects with byte-identical scientific inputs.

## 15. Stop conditions

Stop affected path on:

- scientific output differs because instrumentation is enabled;
- NaN/Inf in key HJB arrays or controls;
- scientific exception;
- same-turn feedback/provenance failure;
- same-S/capital/C1 failure;
- unauthorized parameter/guard/grid/tolerance/solver/equation change.

Do not tune after stop.

## 16. Required analysis

The final report must answer:

1. In turn 2, with common entering state, what is the earliest HJB iteration/object where G1/G2 diverge?
2. Does divergence first appear in value derivatives, transfer candidates, selector scores/labels, or only after policy/drift assembly?
3. Which derivative-floor or safeguard activations differ first, if any?
4. At the 湖北 turn-2 extreme cell, which exact candidate and selector transition generates the huge G2 `d/cost/mu` values?
5. Is the extreme caused by an already-extreme pre-selector candidate being selected, or by candidate construction itself exploding before selection?
6. Are turn-2 immediate effects predominantly interior or boundary-linked?
7. How do later turns differ from the common-state turn-2 mechanism as path history propagates?
8. Does wage-bound status coincide with the earliest turn-2 mechanism, or is it unchanged when the first divergence arises?
9. Which currently frozen scientific object is the smallest plausible next calibration gate: transfer/adjustment-cost parameters, derivative safeguard, price-interface guard, boundary law, or something else?
10. If evidence still cannot identify this, say so and recommend no science change.

## 17. Interpretation boundary

All turns 3-5 associations remain descriptive/path-history evidence.

Only turn 2 may support immediate common-entering-state attribution, and only for differences downstream of the frozen G1/G2 HJB return input.

Do not call an intermediate a KKT residual unless the accepted code explicitly defines it as such. If standalone KKT residual is still absent, report `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`.

## 18. Final classification and next gate

Choose one truthful classification, e.g.:

- `TURN2_COMMON_STATE_DIVERGENCE_LOCALIZED_TO_TRANSFER_CANDIDATE_CONSTRUCTION__OWNER_TRANSFER_COST_CALIBRATION_DECISION_REQUIRED`;
- `TURN2_COMMON_STATE_DIVERGENCE_LOCALIZED_TO_VALUE_DERIVATIVE_SAFEGUARD_AND_SELECTOR_INTERACTION__OWNER_HA_NUMERICAL_CONTRACT_DECISION_REQUIRED`;
- `TURN2_COMMON_STATE_DIVERGENCE_LOCALIZED_TO_POLICY_SELECTION_WITH_FINITE_CANDIDATES__BOUNDARY_OR_SELECTOR_AUTHORITY_REVIEW_REQUIRED`;
- `INSTRUMENTED_RUNTIME_STILL_DOES_NOT_IDENTIFY_A_SINGLE_MECHANISM__NO_PARAMETER_CHANGE_AUTHORIZED`;
- or a more precise evidence-based variant.

Recommend exactly one next gate. Do not authorize longer G2, G3/G4, wage relaxation, K1B/K2, steady-state acceptance or Results from this Builder task.

## 19. Allowed tracked changes

Allowed only as task-bounded diagnostics:

- observation-only instrumentation hooks/wrappers;
- bounded runner/finalizer;
- compact instrumentation evidence;
- focused tests;
- report `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC_REPORT.md`;
- evidence under `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_instrumented/`;
- truthful CURRENT closeout docs.

Production scientific equations/parameters/guards/grids/tolerances/solver semantics must not change. Any instrumentation modification inside scientific modules must be observational only and proven output-parity under instrumentation OFF/ON; prefer wrappers/hooks where possible.

## 20. Git/local safety

Fresh isolated worktree from live main. Explicit stage paths. No `git add .` / `git add -A`. No reset/clean/stash/force push. Preserve accepted evidence. One coherent commit, non-force push, one remote commit/report readback. Do not merge main and do not publish a successor task.

## 21. Final response

Return:

- classification;
- actual baseline, branch/worktree/candidate SHA;
- changed paths;
- pre-run instrumentation parity gate;
- exact frozen G1/G2 science;
- call ledgers/completed turns/retries;
- turn-1 equality;
- turn-2 common-state earliest-divergence findings;
- derivative/floor traces;
- pre-selector candidate findings;
- selector/policy transition findings;
- priority extreme-cell reconstruction;
- turns3-5 path-history findings;
- return/wage hit monitoring;
- K1/C1/same-S/provenance gates;
- NaN/Inf/hard-stop status;
- KKT availability;
- KFE caveat;
- exactly one next gate;
- Results eligibility=`FALSE`.

Stop. Do not enter G3/K1B/K2.
