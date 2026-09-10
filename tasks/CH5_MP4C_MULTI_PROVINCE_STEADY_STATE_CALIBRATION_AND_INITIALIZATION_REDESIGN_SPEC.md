# CH5 MP4C multi-province steady-state calibration and initialization redesign specification

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization after explicit Owner scientific agreement.

## 1. Objective

Produce a **design/specification and static source-mapping task only** for the multi-province Chapter 5 steady-state route. The task shall translate the newly agreed scientific/numerical principles into an auditable implementation contract before any model rerun.

The immediate goal is to preserve the original MATLAB economic structure and efficient single-loop calibration philosophy while repairing legacy data-unit, initialization, and convergence-control weaknesses that can generate large `ra -> rah -> At -> K -> ra` oscillations.

This task does **not** authorize HANK/HJB/KFE/firm/outer-loop execution or production source modification.

## 2. Owner-frozen scientific decisions

Treat the following as decided for this specification:

1. **2018 GDP / population**: use correct 2018 values, not the legacy mixed-year object.
2. **Capital**: use a PIM capital stock with explicit depreciation. The previously used annual depreciation `delta=0.096` is acceptable for Chapter 5; it does not need to be changed merely because alternative estimates exist. The paper/report must state that capital is model-derived rather than an official published stock.
3. **PIM timing**: preserve the already accepted lagged-flow form unless source review identifies a direct conflict:
   `K_t = (1-delta) K_(t-1) + I_(t-1)`.
4. **Alpha**: retain the original admissible-range philosophy. Owner recalls and approves `[0.2, 0.8]` as the model range. Re-estimated raw alpha should be preserved, while the model-used alpha may be clipped to the nearest boundary if raw alpha lies outside `[0.2,0.8]`, with both raw and used values explicitly saved. Current re-estimated raw alpha `0.7380939146868483` is inside the range and therefore should remain unchanged.
5. **Units**: all objects entering the household/allocation/firm loop must have a single explicit model-unit contract. Legacy unexplained multipliers must not be inherited silently.
6. **Initialization**: replace legacy generic extreme starts (`ra=.09`, `rah=.09`, `wjt=.6`, household `w=20`) with data-consistent or source-equation-consistent initial values derived from 2018 `Y, K, L, Z, alpha` and the existing firm/accounting equations. Retain raw and used initial values if safety clipping is applied.
7. **Price bounds / empirical safety region**: existing `ra`/wage safety bounds are historical numerical devices and may remain as bounded safeguards. Do not widen/narrow them in this task. Record their exact current values and source locations.
8. **Under-relaxation**: it is approved in principle for `w` and `rah` (and, if source mapping supports it, for controller states such as `GovInv`) because it changes the path, not the fixed point, when implemented as convex damping of old/new values. Exact coefficients are **not yet frozen**; this task must propose candidates and a validation protocol, not silently choose production coefficients.
9. **Calibration architecture**: preserve the original efficient **single-loop, near-steady-state online calibration** philosophy. Do **not** replace it with a fully nested `steady state -> calibrate -> recompute steady state` architecture.
10. **Staged calibration**: refine the single loop into explicit stages/gates: far-from-steady stabilization; near-steady calibration; final freeze/confirmation. A hysteresis-style enter/exit gate is approved in principle to avoid calibration chatter, but exact thresholds are not frozen here.
11. **Solver family**: do not replace the ordered update map with Newton/Broyden/Brent/fsolve/Anderson or another nonlinear solver in this task.

## 3. Required authorities and sources

Read live GitHub current docs first:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`;
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`;
- `docs/CH5_MP4C_2018_MATLAB_INPUT_DATA_AND_INITIAL_STATE_COMPARISON_AUDIT_REPORT.md`;
- `docs/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_REPORT.md` and its acceptance;
- the current accepted 31-province ledgers needed to understand units and 2018 calibration objects.

Read protected original MATLAB files **read-only** from:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

At minimum inspect:

- `load_GDPdata.m`;
- `It_to_Kt.m`;
- `multi_prov_HANK_12sts.m`;
- `mpHANK_equilibrium_2000.m`;
- `HANK_mp_1eq.m`;
- `HANK_mp_1turn.m`;
- `HANK_firm.m`;
- `wage_caculate.m`;
- `Lt_seperate.m`.

Do not modify the protected tree.

## 4. Scientific/model call budget

All actual model calls are **zero**:

- MATLAB HANK/HJB/KFE: 0;
- Python household/HJB/KFE: 0;
- firm/wage/migration/capital-allocation execution: 0;
- outer-turn / steady-state / GE / annual / IRF / Results: 0;
- scientific root/direct/iterative/eigen solves: 0.

Allowed:

- static source inspection;
- read-only accepted data/result inspection;
- deterministic equation algebra;
- unit conversions/checks using already accepted values;
- source-to-contract mapping;
- pseudocode/specification;
- synthetic/non-scientific unit tests of helper contracts if needed.

If a conclusion requires running a model function, mark it as a future validation requirement rather than executing it.

## 5. Workstream A — reconstruct and freeze the model-unit contract

Build a source-backed table for every key object:

- raw GDP `Y0`;
- raw population / labor proxy `N` or `L0`;
- raw/PIM capital `K0`;
- `GovInv`;
- household `At`, `Bt`, `Lt`, `Ct`;
- `At*N`;
- `Kt_supply`;
- total productive `Kt=Kt_supply+GovInv`;
- `Zt`;
- `alpha`;
- `ra`, `rah`, `rb`, `wjt`, household `w`.

For each object record:

- source/raw unit;
- existing legacy multiplier;
- intended model unit;
- equation consumers;
- whether multiplication by `N` occurs before/after conversion;
- whether legacy code currently mixes units;
- proposed single explicit conversion rule.

The specification must identify the exact point where household asset units are bridged to macro productive-capital units. Do not solve unit mismatches by arbitrary rescaling chosen to make results converge.

## 6. Workstream B — alpha contract

Map exact current `load_GDPdata.m` behavior for alpha, including any existing boundary treatment.

Specify the successor contract:

- save `alpha_raw`;
- model range `[0.2,0.8]`;
- `alpha_used = min(max(alpha_raw,0.2),0.8)` if and only if raw is outside the range;
- save a clipping flag and reason;
- current raw `0.7380939146868483` should map exactly to the same used value;
- never retune alpha within the steady-state loop merely to obtain convergence.

If original MATLAB logic differs materially from Owner memory, report both source-faithful behavior and the newly frozen Owner design; do not conceal the difference.

## 7. Workstream C — data-consistent initialization design

Statically map the current legacy initial state and identify every generic initial value overwritten before/after first household or firm calls.

Design a replacement initialization contract based on same-year 2018 data and existing firm equations.

At minimum specify how to obtain candidate initial:

- productive capital `Kt0`;
- labor input/proxy `Lt0`;
- output target `Y0`;
- `Zt0`;
- `alpha_used`;
- raw firm-side wage candidate;
- raw firm-side capital-return candidate;
- used/clipped `wjt0` and `ra0`;
- initial household composite `rah0` from the existing cross-province return mapping;
- initial household wage `w0` from the existing wage aggregator / migration-weighted logic, or a clearly defined static approximation if exact computation would require a model call.

Do not invent a new economic equation. Derive from existing `HANK_firm.m`, `wage_caculate.m`, allocation/orientation contracts and accepted data objects.

If exact `rah0` or `w0` cannot be constructed without an actual allocation/firm call, specify the minimal future bounded initialization probe needed rather than running it.

## 8. Workstream D — under-relaxed single-loop update specification

Map the current ordered update sequence exactly.

Then propose a successor ordered update with explicit raw/used states, conceptually:

`household old state -> household outputs -> labor/capital allocation -> firm raw prices -> composite household raw prices -> damped used prices -> convergence/calibration gates -> controller update`.

For approved candidate price damping, use the generic contracts:

`w_used_(n+1) = (1-lambda_w) w_used_n + lambda_w w_raw_(n+1)`

`rah_used_(n+1) = (1-lambda_rah) rah_used_n + lambda_rah rah_raw_(n+1)`

with `0 < lambda <= 1`.

Do not freeze `lambda_w` or `lambda_rah` yet. Propose a small pre-registered candidate set/range and a bounded future validation protocol. The protocol must compare convergence behavior without changing equations, tolerances, calibration targets, or final fixed-point definitions.

Distinguish clearly:

- raw firm/composite price;
- clipped price if the source uses a safety bound;
- damped price passed to the next household turn;
- diagnostic residual/gap.

Specify the order of clipping vs damping and justify it from source/economic semantics. If multiple defensible orderings exist, surface them for Reviewer/Owner choice.

## 9. Workstream E — staged online calibration, not nested steady states

Preserve one outer iteration loop and formalize three phases:

### Stage A — stabilization / far from steady state

- household-firm updates continue;
- price damping active if implemented;
- avoid unnecessary large calibration moves while convergence gaps are large;
- diagnostics identify whether `ra`/wage safety bounds are being hit.

### Stage B — near-steady online calibration

Once a pre-defined proximity condition is satisfied, allow the original calibration logic to operate:

- adjust `Zt` toward GDP target;
- adjust `GovInv` in response to `ra` being too high/low;
- preserve bounded/damped controller philosophy;
- do not wait for full steady-state convergence before calibration.

### Stage C — calibration freeze and final confirmation

Once GDP target, `ra` admissibility and calibration-state changes are sufficiently stable for a pre-defined number of turns:

- freeze `Zt` and `GovInv`;
- continue the same household-firm fixed-point iteration to final convergence;
- if final confirmation materially destabilizes, report/reopen calibration rather than hiding it.

This task must propose explicit observable gate variables and candidate thresholds based on current source quantities (`KNratio/tKNratio`, `Y/Y_prev`, GDP target gap, `ra` bound counts, controller change sizes). Exact production thresholds are proposals only unless they are unchanged source constants already accepted.

## 10. Hysteresis design

Propose an enter/exit contract for Stage B to avoid gate chatter:

- `epsilon_enter` for entering near-steady calibration;
- `epsilon_exit > epsilon_enter` for leaving it after a destabilization;
- optional minimum consecutive-turn count before changing stage.

Do not pick values after observing a model trajectory. Recommend a small candidate grid based on source tolerances and numerical scales for a future bounded validation task.

## 11. GovInv controller audit

Map exact existing `GovInv` update logic in `HANK_mp_1eq.m`, including:

- thresholds/conditions based on `ra`;
- multiplicative `0.9/1.1` or other factors;
- relation to `ra` clipping range;
- whether updates occur before/after convergence diagnostics;
- whether any existing damping/implicit under-relaxation already exists.

Recommend only minimal structural changes needed to integrate it with staged calibration. Do not redefine government capital economically in this task.

## 12. Required deliverables

Create repository-safe outputs:

- `docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md`;
- `reports/mp4c_multi_province_steady_state_redesign_20260910/source_to_successor_contract.csv`;
- `reports/mp4c_multi_province_steady_state_redesign_20260910/unit_contract.csv`;
- `reports/mp4c_multi_province_steady_state_redesign_20260910/initialization_contract.md`;
- `reports/mp4c_multi_province_steady_state_redesign_20260910/update_order_contract.md`;
- `reports/mp4c_multi_province_steady_state_redesign_20260910/calibration_stage_contract.md`;
- `reports/mp4c_multi_province_steady_state_redesign_20260910/future_validation_matrix.csv`;
- source/hash receipt for protected MATLAB files actually read;
- zero scientific-call ledger;
- focused static tests / consistency checks;
- manifest/readback.

The main report must distinguish:

- `UNCHANGED_SOURCE_LOGIC`;
- `OWNER_FROZEN_CORRECTION`;
- `NUMERICAL_PATH_STABILIZATION_PROPOSAL`;
- `FUTURE_VALIDATION_REQUIRED`.

## 13. Required report answers

At the top of the report answer:

1. Where exactly are unit inconsistencies or unexplained legacy multipliers in the original route?
2. What single unit contract should replace them?
3. What is the exact original alpha clipping/range behavior, and how does it compare with the Owner-frozen `[0.2,0.8]` contract?
4. Which initialization values are legacy arbitrary starts, and which can be derived statically from 2018 data/equations?
5. What exact source-consistent initialization sequence is recommended?
6. Where does the current code already use damping/under-relaxation?
7. What additional `w/rah` damping contract is recommended without changing the fixed point?
8. How should the existing single-loop near-steady calibration be staged without introducing a costly nested steady-state/calibration loop?
9. What hysteresis/gating candidates should be tested later?
10. What remains an Owner/Reviewer choice before implementation?
11. Confirm all HANK/HJB/KFE/firm/outer-loop/steady-state model calls are zero.

## 14. Stop conditions

Stop and report instead of guessing if:

- source unit semantics cannot be reconciled with accepted data objects;
- source alpha behavior materially contradicts the frozen design in a way that changes economic interpretation beyond simple clipping;
- initialization would require a new economic equation;
- an exact value can only be established through a model run;
- protected source would need modification.

## 15. Git/publication

Use a dedicated branch/worktree where practical.

- preserve unrelated dirty/untracked files;
- no reset/clean/stash;
- explicit staging only;
- no force push;
- commit and push the specification/report package on a dedicated branch;
- do not merge main;
- do not implement production changes;
- do not publish a successor execution task.

Allowed primary verdicts:

- `STEADY_STATE_REDESIGN_SPEC_PASS__UNIT_INIT_DAMPING_AND_STAGED_CALIBRATION_CONTRACT_READY`;
- `STEADY_STATE_REDESIGN_SPEC_PARTIAL__OWNER_OR_UNIT_DECISION_REMAINS`;
- `STEADY_STATE_REDESIGN_SPEC_BLOCKED__SOURCE_CONTRACT_INSUFFICIENT`.
