# Task — monotonicity-preserving HJB relaxation scientific design gate

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_SCIENTIFIC_DESIGN_GATE_20260921`

Status: `ACTIVE`

Results eligibility: `FALSE`

## Roles and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer / scientific-route authority. Codex is bounded Builder / scientific numerical analyst. GitHub live main is repository-state authority.

Absolutely do not enter, read, search, use or modify:

`zcx369658780/deep-learning-hank`.

## Required reads

Fresh-fetch live main, then read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_EMERGENCE_FORENSIC_ACCEPTANCE_20260921.md`
6. `docs/CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_ACCEPTANCE_20260921.md`
7. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`
8. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`
9. current nonlinear continuation / turn2 HJB update source, read-only
10. this exact task.

## Purpose

This is a scientific design gate only.

The accepted forensic proves that a numerically accurate full implicit update from checkpoint2 to checkpoint3 creates the first negative raw liquid slopes.

The current production iteration law remains frozen and authoritative.

Determine whether a **global convex relaxation / backtracking safeguard on the value update**

`V_{n+1}(alpha)=(1-alpha)V_n+alpha*Vhat_{n+1}`

with `0<alpha<=1`, where `Vhat_{n+1}` is the existing full implicit direct-solve output, can be justified as a generic corrected-HJB numerical law that:

1. preserves the fixed-point equations;
2. preserves strict positive liquid marginal-value finite differences required by the consumption FOC;
3. does not clip/project individual cells or derivatives;
4. does not change D1/D2/D3 economics;
5. remains fail-closed and prospectively specified;
6. is not tuned to make F0063 pass.

No implementation is authorized.

## Anchor evidence

Use the accepted 黑龙江 checkpoint2→3 pair:

- old state `V2`
- full implicit candidate `Vhat3`
- accepted checkpoint2 policy/Q/utility
- accepted negative-slope forensic evidence.

No new linear solve is allowed.

## Part A — fixed-point invariance

Derive whether, for any deterministic `alpha(V_n,Vhat_{n+1}) in (0,1]`, the relaxed iteration has the same fixed points as the original map provided alpha never becomes zero at a non-fixed point.

Separate:

- fixed-point equivalence;
- convergence behavior;
- monotonicity/invariant-domain behavior.

Do not claim global convergence unless proved.

## Part B — exact liquid-slope feasibility interval

Because every raw b finite difference is affine in alpha, derive for every b-grid edge:

`s_e(alpha)=s_e(V_n)+alpha*(s_e(Vhat)-s_e(V_n))`.

For the accepted checkpoint2→3 pair:

1. compute all 760 raw b-edge slopes at V2 and Vhat3;
2. derive the exact alpha interval for which every raw b edge remains strictly positive;
3. identify the binding edges and critical alpha values;
4. independently verify the F0062/F0063 edge;
5. determine whether alpha=1 fails and how much relaxation is needed.

Do the same diagnostic calculation for checkpoint0→1 and checkpoint1→2 to show whether the safeguard would have been inactive there.

No production derivative helper may be called.

## Part C — candidate generic safeguard designs

Compare at least:

### Design 0 — current full update

`alpha=1`.

Preserves current authority but fails at checkpoint2→3.

### Design 1 — deterministic halving backtrack

Start `alpha=1`. If the full relaxed candidate contains any nonpositive raw b edge, set `alpha=alpha/2` until all raw b edges are strictly positive or a preregistered finite backtrack ceiling is exhausted.

Analyze:

- fixed-point invariance;
- absence of derivative clipping;
- deterministic/fail-closed semantics;
- whether halving is scientifically/numerically principled or merely convenient;
- operation-budget implications.

### Design 2 — maximal admissible alpha from exact edge inequalities

Compute the supremum alpha permitted by all raw b-edge positivity inequalities.

Because strict positivity cannot use the exact zero-crossing endpoint, propose a deterministic representation-safe rule, if one exists, that stays strictly inside the admissible interval without introducing an economically meaningful derivative floor.

Possible constructions may be analyzed, not assumed authoritative, for example:

- one floating-point predecessor of the critical alpha;
- an arithmetic-bound-separated alpha;
- another prospectively defined interior rule.

Explain numerical robustness and whether the rule creates near-zero q_b pathologies.

### Design 3 — value/derivative projection or clipping

Analyze as a comparator only. It is expected to alter the solved iterate locally and is not authorized.

### Design 4 — adaptive Delta / new direct solve

Analyze only as a comparator. It requires a new linear solve and changes the current numerical method; no runtime experiment is authorized in this task.

## Part D — economic/numerical invariant

Assess whether strict positivity of raw liquid finite differences is a legitimate invariant of the corrected HJB iteration.

Address:

- monotonicity of the value function in liquid wealth under the model's utility/budget structure;
- distinction between an economically required value-function property and a numerical iterate property;
- whether enforcing positivity by convex relaxation preserves the HJB fixed point rather than altering the target;
- whether enforcing positivity only when the full candidate exits the admissible derivative domain is better interpreted as an invariant-domain line search than as outcome tuning.

Use repository equations/authority; do not claim a theorem beyond available support.

## Part E — zero-science replay on persisted updates

Using only persisted V states and direct-solve candidate arrays:

1. apply the candidate alpha rules arithmetically to update 0→1, 1→2 and 2→3;
2. report alpha chosen by each proposed design;
3. reconstruct raw b derivative sign census after relaxation;
4. report value-change norm under relaxation;
5. compute the frozen-checkpoint2 linear-system residual of the relaxed 2→3 state as a diagnostic only, explicitly noting that a relaxed state is not expected to solve the frozen linear system exactly;
6. do not run selector, Q rebuild or same-value Bellman map at relaxed V.

This is not an HJB rerun.

## Part F — interaction with accepted convergence law

A proposed relaxation law must specify how the existing metrics are interpreted:

- `D_n=||V_n-V_{n-1}||_inf` uses the accepted relaxed state;
- same-value Bellman `B_n` can only be computed after a fresh policy/Q map at that accepted state in a future implementation task;
- exact/approximate cycle identities use accepted relaxed checkpoints;
- the 100-update ceiling counts every accepted relaxed update;
- one full direct solve plus relaxation is one HJB update, not a scientific retry;
- if the relaxation safeguard cannot find a legal positive-slope state within its finite rule, stop fail closed.

No convergence threshold may change.

## Required outcome

End with exactly one:

### 1. Adoption-ready generic relaxation law

`PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_DESIGN_GATE__GENERIC_LAW_PROPOSAL_COMPLETE__OWNER_ADOPTION_REQUIRED__NO_IMPLEMENTATION`

Requires a fully specified prospective law:

- trigger;
- alpha selection;
- strict positivity test;
- finite backtrack/representation rule;
- failure terminal;
- fixed-point argument;
- convergence-metric interaction;
- operation accounting;
- evidence contract;
- implementation/reexecution plan.

### 2. Relaxation not scientifically justified

`PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_DESIGN_GATE__RELAXATION_NOT_JUSTIFIED__CURRENT_ITERATION_FAIL_CLOSED_RECOMMENDED__NO_IMPLEMENTATION`

### 3. Scientific ambiguity

`BLOCKED__MONOTONICITY_PRESERVING_HJB_RELAXATION_DESIGN_GATE__OWNER_ADJUDICATION_REQUIRED__NO_IMPLEMENTATION`

Use only when two or more genuinely defensible numerical laws remain and evidence cannot distinguish them.

## Zero-science boundary

Allowed:

- persisted V/direct-update/Q/utility reads;
- independent arithmetic;
- finite-difference reconstruction;
- convex-combination diagnostics;
- persisted CSR matvec/residual calculations;
- symbolic derivation.

Forbidden:

- production derivative helper;
- production selector/root helpers;
- HJB direct-update execution;
- new linear solve;
- D2/Q rebuild;
- KFE/SVD;
- aggregate/integration;
- turn2 rerun;
- turn3;
- MATLAB;
- production source changes;
- tuning against future outcomes.

Scientific/model calls remain zero.

## No implementation

Do not modify `src/ch5_two_asset_hank/**`.

Do not modify CURRENT.

Do not publish a successor.

Fresh evidence:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_scientific_design_gate_20260921_run001/`

Validator:

`validators/multi_province/monotonicity_preserving_hjb_relaxation_scientific_design_gate/**`

Optional test:

`tests/test_mp4c_monotonicity_preserving_hjb_relaxation_scientific_design_gate.py`

Report:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_SCIENTIFIC_DESIGN_GATE_REPORT.md`

## Required evidence

Persist:

- authority/source binding;
- fixed-point invariance derivation;
- full-edge alpha-feasibility analysis for updates 0→1,1→2,2→3;
- binding-edge table;
- candidate design comparison;
- invariant-domain scientific memo;
- persisted-update arithmetic replay;
- convergence-law interaction contract;
- proposal-only law if supported;
- zero-science ledger;
- focused tests;
- sealed manifest/readback;
- final classification.

Commit + ordinary non-force push, then STOP.
