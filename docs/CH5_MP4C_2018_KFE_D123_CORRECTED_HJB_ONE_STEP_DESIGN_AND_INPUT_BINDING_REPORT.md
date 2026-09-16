# CH5 MP4C 2018 KFE D1-D3 corrected HJB one-step design and input binding

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_ZERO_SCIENCE_20260916`

Role: bounded Builder design/provenance task; zero scientific execution

## Verdict

`BLOCKED__NO_UNIQUE_AUTHORITY_BACKED_CORRECTED_HJB_SEED_OR_INPUT_CONTRACT`

Repository authority uniquely supports the call-725 grid, household scalars, corrected D1/D3 cell contract, corrected D2 generator, and the algebraic form of one implicit direct step. It does **not** uniquely select a starting value function.

At least two distinct, fully identified value objects are scientifically plausible but have different meanings: the source-native call-725 `V0` and the supplied post-step143 historical terminal state. A third distinct object is the output of one MATLAB-faithful replay from that terminal state. None is a corrected-target fixed point, and no accepted document designates one of them as the corrected experiment's seed. Selecting the near-terminal object because it is closer to a historical fixed point, or selecting source-native `V0` because it is convenient to regenerate, would be an unauthorized scientific initialization choice.

Therefore no corrected policy-map or direct HJB execution is authorized by this report. The common non-seed contract is frozen below so that the unresolved Owner decision is narrow and explicit.

## Git identity and changed path

- Fresh-fetched `origin/main`: `5a5c150e642a507915170e0619fb31ecd2061286`
- Branch: `codex/ch5-mp4c-2018-kfe-d123-corrected-hjb-one-step-design-input-binding-zero-science-20260916`
- Candidate SHA convention: the exact candidate is the commit containing this report and must be returned in the final handoff with remote readback; embedding that SHA in its own content would change it.
- Exact changed path: `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_REPORT.md`

The corrected source reviewed at this baseline has Git blobs:

| Source | Git blob |
|---|---|
| `corrected_diagnostic/contracts.py` | `41186454de5ba1f55d3ba273f7ce57457ded11ca` |
| `corrected_diagnostic/selector.py` | `c83c1c6d280d729d727bafe0d064d6129a86a765` |
| `corrected_diagnostic/generator.py` | `f86234340c6e09c7129225da1677614669754177` |
| `matlab_faithful_hjb.py` | `e06f9871b361c8e1c8df7aab5c43c2dbd3b09b50` |

The frozen source-faithful formula reference remains Git blob `9e7dc9556a2b76811e78f89999abecc045886106`.

## Exact authority and provenance read

Repository authority:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
- `tasks/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_ZERO_SCIENCE_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_ACCEPTANCE_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_REPORT.md`
- `docs/CH5_MP4C_2018_KFE_D123_TEN_CELL_REEXECUTION_FAIL_CLOSED_ACCEPTANCE_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_SELECTOR_ACTIVE_EQUALITY_CANONICALIZATION_AND_TEN_CELL_REEXECUTION_REPORT.md`
- `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`
- `docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_REPORT.md`
- `docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_ACCEPTANCE.md`
- `docs/CH5_MP4C_CALL725_FIRST_ITERATION_CLOSURE_REPORT.md`
- `docs/CH5_MP4C_CALL725_FIRST_ITERATION_CLOSURE_ACCEPTANCE.md`
- `docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_INITIALIZATION_ARRAY_NUMERICAL_PARITY_AND_LABOR_ROOT_FORENSIC_REPORT.md`

Repository evidence and source:

- `reports/call725_boundary_generator_repair_spec_20260907/binding_identity.json`
- `reports/call725_boundary_generator_repair_spec_20260907/consumed_inputs.json`
- `reports/call725_boundary_generator_repair_spec_20260907/snapshots.json`
- `reports/call725_boundary_generator_repair_spec_20260907/source_map.json`
- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/derivatives.py`
- `src/ch5_two_asset_hank/hjb.py`
- `src/ch5_two_asset_hank/matlab_faithful_hjb.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/contracts.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/generator.py`
- frozen `exports/matlab_faithful_two_asset_ha.py` blob `9e7dc9556a2b76811e78f89999abecc045886106`

External, already accepted read-only provenance:

- `call725_first_iteration_scalar_binding.json`, 2,732 bytes, SHA-256 `A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`
- `hjb100_initialization.mat`, 13,362 bytes, SHA-256 `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`
- `states.json`, 1,849 bytes, SHA-256 `6D8494665168C8C2029E5C209B1D302BE9C28F84EAE60B96F80F92363FA6C9AE`
- `M143_FINAL.mat`, 10,998 bytes, SHA-256 `30CC73326C072FCB12EC216BE0C2FB23CBEB122E2260A7584A853768DF3D61D7`
- `matlab_M143_FINAL/step_0001.mat`, 213,246 bytes, SHA-256 `4EAA6695A07F8C32B42515631D1AF95AD48190990627934D7895EC7EFC9CCE63`
- MATLAB trajectory step 52, 213,238 bytes, SHA-256 `AA9DB0664FB0476AFA097C9716AAC88EB56F5779EC1A1346EEA27ED406D12FA3`
- MATLAB trajectory step 57, 211,918 bytes, SHA-256 `81AC0E3F06E8D268C05E4E78B67F64FD6351FC55924282DB4DD44FF99EA77DDA`

Only MAT metadata, named arrays, hashes, shapes, finite status, extrema, and direct array comparisons were read. No model module was imported or executed.

## Starting value / seed options

Field hashes below are newly computed audit identities over native little-endian float64 field bytes serialized in `(b,a,z)` F-order. Every listed value tensor is finite, shape `(20,20,2)`, and 6,400 bytes under this convention.

| Option | Exact object and identity | Provenance and meaning | Corrected-target status | Authority disposition |
|---|---|---|---|---|
| A | `hjb100_initialization.mat:v0`; field SHA-256 `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665`; range `[-2.6471989790143082,-1.710759724165037]` | Source-native call-725 initialization generated from the frozen initialization formula and baseline labor roots; accepted Python/MATLAB numerical parity | Numerical initialization for the historical source path, not a corrected-target fixed point | Plausible fresh-start seed, but not preferred by current authority over B |
| B | `M143_FINAL.mat:v0`; field SHA-256 `116E0E8A35E21F1F9050C53FE065FDE8646CF28432176E2061E44755628857F3`; range `[-1.9778880627040374,-1.515214336024235]` | `states.json` binds this exactly to MATLAB trajectory `step_0143.mat:updated`; accepted supplied historical terminal common state | Source-faithful historical near-fixed-point state, not a corrected-target fixed point | Plausible continuation seed, but not preferred by current authority over A |
| C | `matlab_M143_FINAL/step_0001.mat:updated`; field SHA-256 `6DBA26D544F8F913E4BD517D57D41AD79D82A2A8F2233AC8D1F9B350A93DD940` | One MATLAB-faithful replay output from B; differs from B by maximum absolute `2.6173063716328215e-11` | Historical replay output, not corrected-target | Distinct but not designated as a new initialization authority |
| D | trajectory step52/step57 `initial_value`; field SHA-256 `8F158A5EA09FEA1488FB51BB15469E4E23D5C7D6E73CCCE0A65B7577865E5C0F` / `37AA07F189596DF7E74F444F042F45D233B3EB878E46779D5603DA6EE74859FC` | Historical intermediate observation states used for bounded trajectory evidence and selected-cell receipts | Historical only | No authority identifies either as the full corrected-map seed |
| E | corrected-target value object | No such persisted object was found in current authority | Would be the scientifically aligned seed if defined | Missing; creating one requires an explicit initialization law or Owner selection |

A and B are materially distinct: their maximum absolute difference is `1.0515540876143132`. Existing authority establishes provenance and historical meaning but supplies no ranking criterion between a fresh source initialization and a near-terminal historical continuation. Numerical proximity, anticipated selector success, or reduced runtime are forbidden tie-breakers.

## Exact unresolved Owner decision

Owner must explicitly choose one of the following before a scientific successor can be issued:

1. adopt Option A as the corrected diagnostic's numerical start while acknowledging that the first corrected map may be far from the historical terminal state;
2. adopt Option B as a historical continuation seed while acknowledging that it inherits a value state produced by the source-faithful policy/operator rather than the corrected D1-D3 map;
3. designate another exact existing object, with path/field/hash and scientific rationale; or
4. define a new corrected-target initialization law and separately authorize its construction and validation.

Option C must be separately named if preferred; it is not interchangeable with B despite their small difference. Options D are observational trajectory states and have no present full-map seed authority. The decision must be scientific/provenance based, not outcome based, and must occur before any selector evaluation.

## Common input contract that is already uniquely supported

The following contract is conditional only on Owner choosing a seed from the exact call-725 grid family. It is not permission to execute.

### 1. Grid and domain

- State order: `(b,a,z)`.
- Shape: `(20,20,2)`; 800 cells.
- Flatten/unflatten order for the corrected map, generator, RHS and solution: F-order.
- Liquid grid: 20 exact nodes from `-2.0` to `5.0`, uniform source spacing approximately `0.368421052631579`; native-byte SHA-256 `A3FF663C18A2088A75B0E76C8ADA982EAF6D33ACFECB8DAA17C6D7DDE0533A76`.
- Illiquid grid: 20 exact nodes from `0.0` to `10.0`, uniform source spacing approximately `0.5263157894736842`; native-byte SHA-256 `AE3A3A789FBC0DC9900B8153DEC717264C74AAB6FDA356C21C0EB22EEAC52567`.
- Productivity nodes: `[0.8,1.3]`; native-byte SHA-256 `A35F6FAB6E4564C6F4B1962A2ADE64E477F808432F747ABC7ACCF5E70B0B39B7`.
- Productivity generator: `[[-1/3,1/3],[1/3,-1/3]]` using the exact binary64 values in the scalar binding.
- `b=-2` and `a=0` retain their economic lower-bound identity. `b=5` and `a=10` are D1 artificial upper numerical state constraints.

This is the exact call-725 / ten-cell-panel grid. The later practical `I=20,J=160`, `a=[0,100]`, `b=[-2,20]` grid is a different scientific object and is excluded from this gate.

### 2. Prices and calibration

The hash-bound scalar binding fixes:

| Quantity | Value / construction |
|---|---|
| province / call | 安徽, zero-based province 11, outer iteration 24, global household call 725 |
| base illiquid return | `r_a=0.09` |
| liquid return | `r_b=0.02` |
| borrowing gap | `0.07` when `b<0`, giving effective `R_b=0.09`; otherwise `R_b=0.02` |
| tax and wage | `tau=0.05`, `w=16.82014806560587` |
| net wage | `(1-tau)*w*z`, equal to `12.783312529860462` at `z=0.8` and `20.772882861023252` at `z=1.3` |
| transfer income | `T=0.1` |
| discount and preferences | `rho=0.05`, `gamma_c=2`, `phi=5`, labor weight `1` |
| adjustment cost | `chi_0=0.1`, `chi_1=2`, `a_bar=1e-6`; `C(d,a)=chi_0*abs(d)+chi_1*d^2/(2*max(a,a_bar))` |
| effective illiquid return | `R_a(a)=0.09*(1-0.1*(a/10)^9)`, from the frozen source formula |
| pseudo-time step | `Delta=1000` |

The historical `convergence_tolerance=1e-7` is recorded provenance, not a one-step convergence claim or permission for iteration. Historical derivative floor `1e-6`, fixed costs, old boundary resource derivatives, and historical split-rate assembly are not inputs to the corrected map.

No price, wage, return, transfer, calibration, grid or switch matrix may be recalculated by an outer/firm block in the successor.

### 3. Derivative construction

Let the selected seed be `V0[i_b,i_a,i_z]` on the exact grid.

- At interior liquid nodes, form both raw differences
  `p_b^F=(V0[i_b+1]-V0[i_b])/(b[i_b+1]-b[i_b])` and
  `p_b^B=(V0[i_b]-V0[i_b-1])/(b[i_b]-b[i_b-1])`.
- At interior illiquid nodes, form both raw differences
  `p_a^F=(V0[i_a+1]-V0[i_a])/(a[i_a+1]-a[i_a])` and
  `p_a^B=(V0[i_a]-V0[i_a-1])/(a[i_a]-a[i_a-1])`.
- At a lower face only the forward one-sided derivative is scientifically valid; at an upper face only the backward one-sided derivative is valid.
- The current finite `CellDerivatives` carrier has no validity masks. A future zero-science adapter must duplicate the valid inward raw derivative into the unused outward field solely to satisfy the finite carrier, persist an `UNUSED_BOUNDARY_SLOT_DUPLICATES_INWARD_RAW_DERIVATIVE` marker, and statically verify that the selector consumes only the inward branch at that face. The duplicate is not an additional derivative candidate.
- Do not insert the historical source's post-boundary marginal-resource values, historical post-boundary derivative arrays, a derivative floor, or any state-constraint shadow value into the raw derivative arrays.
- Face multipliers enter only through the accepted relation `q_i=p_i+t_i*lambda_i`; they are selector outputs, not finite-difference inputs.

### 4. Corrected policy-map contract

Traverse cells once in F-order (`b` fastest, then `a`, then `z`). For each cell construct one `CorrectedSelectorCell` from the frozen grid, prices and four derivative carrier values, then call the accepted `select_constrained_policy` exactly once with one shared global budget.

For each cell persist its identity, raw derivative receipt, active-set/regime comparison set, roots consumed, selected controls, total drifts, utility/Hamiltonian, multipliers, slacks, complementarity, transfer KKT, active-equality raw/bound/canonical receipts, and source/code identities before proceeding.

A cell passes only with outcome `SELECTED_ADMISSIBLE`, exactly one selected consumed policy after same-policy deduplication/Hamiltonian comparison, finite controls and drifts, D1 primal feasibility, nonnegative multipliers, complementarity, derivative-direction consistency, transfer KKT, and exact active-equality canonical representation under the already accepted prospective arithmetic bound. `NO_ADMISSIBLE_POLICY`, `NO_UNIQUE_ADMISSIBLE_POLICY`, an exception, nonfinite value, or budget exhaustion is a terminal map failure.

Stop at the first failed cell. A direct solve is allowed only after all 800 cells pass and all 800 durable receipts exist. No warm start, branch substitution, floor, cap, retry, tolerance change or continuation is permitted.

### 5. Corrected D2 generator

Only after a complete policy map, call `assemble_consumed_drift_generator` once with the selected total drifts `mu_b=g_b`, `mu_a=g_a`, the exact corrected grid and the frozen two-state productivity generator.

- D2 first applies the strict zero-tolerance closed-face test. Any outward drift, including the smallest positive binary64 value at an upper face or negative value at a lower face, is terminal.
- For each nonzero total drift, retain exactly one inward neighbor rate `abs(mu_x)/actual_adjacent_spacing`; no historical split cash/transfer rates or shadow labels are used.
- Offdiagonals must be nonnegative. The asset diagonal is the negative sum of retained asset rates; the productivity diagonal is the negative sum of productivity transitions.
- Require `diagonal_construction_error==0`, `minimum_offdiagonal>=0`, and `max_abs(Q*1)` no larger than the generator's prospective `_arithmetic_bound(Q)`.
- Coordinate checks compare `Q*b` and `Q*a` with the consumed total drifts. Require both maximum absolute coordinate errors to be no larger than the repair specification's prospective operation-count bound `gamma_n*sum(abs(products))` plus exact-spacing representation error, with `n` fixed from the pre-outcome row support. The current generator receipt exposes the coordinate errors but not this separate coordinate bound, so the successor must compute and persist that bound before examining the errors. No outcome-fitted tolerance is allowed.

Any D2 rejection or invariant failure stops before the linear solve.

### 6. One-step linear HJB equation

If and only if the seed is Owner-bound, the 800-cell map is complete and D2 passes, form

`M = (rho + 1/Delta) * I_800 - Q0`

and

`rhs = vec_F(u0) + vec_F(V0)/Delta`,

then perform at most one sparse direct solve

`vec_F(V1) = solve(M,rhs)`.

Here `rho=0.05`, `Delta=1000`, `Q0` is the corrected D2 generator from the consumed policy map, and `u0` is the selected policy utility. No nonlinear update, damping, line search, convergence loop, second map, second solve, solver substitution or KFE follows.

The solve must persist `M`/`rhs` identities, solver identity, finite status, `||M*vec_F(V1)-rhs||_inf`, and normwise backward error
`||r||_inf/(||M||_inf*||V1||_inf+||rhs||_inf)`. Exception, nonfinite inputs/output, shape/order mismatch, or nonfinite residual is terminal. A finite or small backward error is a numerical diagnostic only; it is not HJB convergence or economic admissibility.

### 7. One-step outputs and failed-cell diagnostics

The only scientific output would be the single `V1` tensor plus its identity, the complete pre-solve corrected policy map and D2 generator. From `V1`, construct and persist a fresh set of raw one-sided derivative arrays under the same law, but do not execute a second selector map.

Because the frozen grid is exactly the historical panel grid, the diagnostic coordinates are exact, not interpolated:

- historical Cell 4: `(19,19,0)`;
- historical Cell 8: `(19,19,1)`;
- historical Cell 10: `(19,18,0)`.

At those coordinates record `V0`, `V1`, raw valid inward/interior derivatives, derivative signs, and `V1-V0`. These observations may show how one corrected direct step changes the local derivative state. They do not prove a fixed point, selector admissibility under `V1`, nonlinear convergence, KFE existence, or economic nonexistence.

## Proposed finite successor runtime/call budget

This is a design ceiling, not current execution authority.

| Operation | Ceiling |
|---|---:|
| corrected policy maps | 1 |
| real-cell selector evaluations | 800 |
| scalar roots | 264 |
| D2 generator assemblies | 1 |
| sparse direct HJB solves | 1 |
| nonlinear HJB iterations after the direct step | 0 |
| selector evaluations on `V1` | 0 |
| adverse-outcome or adverse-numerics retries | 0 |
| KFE / MATLAB / outer / firm / wage-return / GE / annual / shock / IRF / Results | 0 |

The root ceiling follows the frozen enumeration rather than an arbitrary per-cell multiplier: 720 cells interior in `b` have no active liquid face and use zero roots; 72 liquid-face/noncorner cells permit at most three roots each; eight corners permit at most six each, giving `72*3+8*6=264`.

The finite runtime budget is the exact operation-count ceiling table above, not an outcome-dependent allowance. Existing authority supplies no scientifically meaningful wall-clock duration, so this report does not invent one. Any externally imposed process timeout, hardware failure or interruption produces an incomplete receipt and no retry; it does not enlarge any operation ceiling.

## Fail-closed rules

Stop before the first selector call if any of the following holds:

1. Owner has not selected an exact seed path/field/hash and rationale.
2. Any seed, grid, scalar-binding, switch-matrix or source hash differs from the accepted identity.
3. Shape, `(b,a,z)` order, F-order mapping, finite status or cell-coordinate identity is unresolved.
4. Any price/calibration field is missing or would require outer/firm/wage-return recalculation.
5. The derivative adapter cannot prove that unused boundary carrier slots are never consumed.
6. Scientific code or the accepted D1/D2/D3 law changes after the execution freeze.

After execution starts, stop without retry at the first failed selector cell, budget breach, missing durable receipt, D2 rejection/invariant failure, nonfinite/failed direct solve, hash drift, or evidence persistence failure. Never select a different seed after observing an outcome.

## Exact successor definition

No successor experiment can be exactly published under this verdict because the seed is unresolved. If Owner later supplies the single seed decision without changing the common contract, Reviewer may publish a fresh task that:

1. binds the selected seed and all hashes before execution;
2. implements/verifies only the boundary derivative-carrier adapter if needed;
3. freezes scientific code after focused zero-science checks;
4. performs at most one 800-cell corrected policy map;
5. assembles D2 once only after a complete map;
6. performs at most one direct solve of the equation above;
7. records `V1` derivatives at the exact three coordinates without a second map; and
8. stops with no KFE, iteration, retry, production replacement or successor publication.

## Zero-call ledger

| Operation | Calls |
|---|---:|
| real selector/evaluator | 0 |
| synthetic selector executing scientific policy logic | 0 |
| scalar roots | 0 |
| HJB policy maps / iterations / direct solves | 0 |
| KFE solves | 0 |
| MATLAB | 0 |
| outer / firm / wage-return recalculation | 0 |
| GE / annual / shock / IRF / Results | 0 |

Static text/source inspection, Git/hash checks, MAT metadata reads, named-array identity reads and pure comparisons only were performed. No scientific code, test, calibration, grid, tolerance or prior evidence was modified.

## Limitations and interpretation boundary

This report does not choose a seed, run a corrected policy map, establish full-grid selector admissibility, solve an HJB, test convergence, solve a KFE, validate a stationary density, replace production, recalibrate the model, or support GE/annual/shock/IRF/Results claims. Results eligibility remains `FALSE`.

The existing historical failures remain derivative-state incompatibilities, not corrected-HJB nonexistence evidence. Conversely, choosing a seed and obtaining one finite `V1` would remain a single-step diagnostic, not evidence of a corrected fixed point or economic solution.

No merge to `main` and no successor publication are authorized by this report.
