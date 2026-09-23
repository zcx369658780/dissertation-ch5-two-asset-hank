# Complete outer-state stopping, failure and budget contract — proposal only

Task `CH5_OUTER_STOP_FAILURE_BUDGET_CONTRACT_PROPOSAL_20260923`; dispatch `276a7e4e3594b0bbd7f6d52e83f589253505b0ad`, parent `71c4479636b729c07c3725c76a14ecd757ce55b6`, frozen `src` tree `00682b2e1a7ba23665f6e16f6acf48ad35874883`. **All stopping rules, terminal classes and new budget ceilings below are `PROPOSED_NOT_ADOPTED`.** This task ran zero science. Turn7 household remains unrun; Results eligibility is `FALSE`.

## Accepted facts versus proposed law

The bounded K1B route has completed turns 5 and 6 and sealed a turn7 entering bundle. Independent Work reviews accepted the quality of the complete-state design, the unit/precision dossier and the sealed static comparison. The Owner agreed to `1e-6` as an **observation-only diagnostic precision**; `1e-12` class precision is an eventual aspiration. In C4→C5 and C5→C6, only `Kt_prev` was strictly below `1e-6`. All C4/C5/C6 checkpoints report 31/31 clipped `ra` upper hits. These facts neither adopt a stop law nor establish a fixed point. Exact source identities are in the JSON receipt.

The proposed same-stage checkpoint `C_n` requires 31/31 legal household HJB/KFE, exactly one complete integration, completed raw `ra0_n`, and a sealed/read-back next entering input/plan with `S_(n+1),rah_(n+1)`. Its carrier is eight canonical 31-province vectors `Yt,Lt,wjt,rk,Kt_prev,w,raw_ra0_n,rah_(n+1)` plus destination-by-origin 31×31 `S_(n+1)`. Frozen inputs, province order, source and file identities are bound. Raw `ra0_n` enters only following-turn attractiveness/payoff; same-turn return feedback is forbidden. C6 is completed turn6 with a prepared turn7 input, not C7.

| Component | Exact static formula | Unit |
|---|---|---|
| `Yt,Lt,wjt,w` | `max_i abs(new_i/old_i - 1)`; old denominators finite and nonzero | dimensionless |
| `Kt_prev` | `max_i abs(new_i-old_i)/Kt0_i`; positive, bitwise-frozen `Kt0_i` | dimensionless |
| `rk,raw_ra0,rah` | `max_i abs(new_i-old_i)` | decimal one-model-period return |
| `S` | `max_(destination,origin) abs(new-old)` | dimensionless share |

A proposed stopping comparison would require **each** component strictly `<1e-6` at a legal adjacent pair, only if Owner adopts the carrier, level, strictness, boundary policy and failure protocol. No formula is silently changed. The accepted static comparison remains an observation, not an adopted stopping test.

## Three routes and recommendation

| Route | Proposed test | Establishes | Does not establish |
|---|---|---|---|
| R1: one valid pass | One complete legal C6→C7 transition with all nine strictly below level. | One observed adjacent-state bounded-map comparison. | Persistence, same-state repeatability, error bound, contraction or fixed point. |
| R2: two consecutive valid passes | Both C6→C7 and C7→C8 complete/legal and all nine below level; stop before turn9 household. | Persistence across two adjacent updates of the same frozen bounded map. | Same-state repeatability, error bound, contraction or fixed point. |
| R3: separately budgeted same-frozen-state repeat first | Independently evaluate the full outer map multiple times at one exactly frozen input, under its own task/budget; then return to Owner. | Empirical repeatability at that input, if the full receipts permit comparison. | A general outer-map error bound or automatic turn7 authority. |

**Recommended sequence (`PROPOSED_NOT_ADOPTED`):** obtain R3 evidence before adopting `1e-6` as a stop level, since full outer-map repeatability and an error bound are `UNAVAILABLE`. If Owner nevertheless adopts a bounded diagnostic stopping rule, R2 is preferable to R1 as a persistence check. R3 has a separate, presently zero, budget and cannot be hidden inside the two-turn envelope below. A finite repeat sample cannot prove a general numerical error bound.

## Legality-first state machine

1. **Precall:** verify sealed C6 JSON/NPZ/manifest hashes, frozen source/input identity, 31-province order, shapes, `S[destination,origin]`, column/share identity and raw→following-turn payoff timing. Require finite values, nonzero finite old denominators for relative comparisons, and positive finite `Kt0` bitwise unchanged across checkpoints. First mismatch: `FAIL__OUTER_INPUT_OR_FROZEN_IDENTITY`; zero new model calls.
2. **Household:** canonical source-native initialization; each province must pass accepted selector/D1–D3, one-solve HJB with deterministic relaxation and existing B/D gate, then accepted unique-closed-class KFE including stationary/full-Q checks. First defect: `FAIL__OUTER_HOUSEHOLD_HJB_OR_KFE`, with exact province/checkpoint and consumed counts; stop globally. No per-province borrowing.
3. **Integration:** only after 31/31 HJB/KFE PASS, perform exactly one source-faithful labor/frozen same-S K1B/C1/31-firm/wage/monetary/fiscal integration. Check capital and C1 identities, S columns, raw/payoff lag, finite outputs, completed raw return and next input. First defect: `FAIL__OUTER_INTEGRATION_OR_TIMING`; stop globally.
4. **Seal:** persist next candidate/plan plus manifest and readback. A missing or failed seal is `FAIL__OUTER_INCOMPLETE_CHECKPOINT`; no partial state is compared.
5. **Compare:** only two complete legal adjacent checkpoints may be compared. A legal value at or above `1e-6` is `VALID__NINE_COMPONENT_LEVEL_NOT_MET`, not a scientific failure or divergence; continue only within an adopted budget.
6. **Budget:** count attempted calls, including failed attempts. Refuse an impending call beyond any province/turn/combined ceiling. Mid-turn exhaustion is `FAIL__OUTER_INCOMPLETE_CHECKPOINT__BUDGET_EXHAUSTED`; budget reached after legal checkpoints without the chosen pass count is `VALID__LEVEL_NOT_MET_AT_BUDGET`. No retry, warm start, fallback, alternate solver/alpha, threshold relaxation, rescue or tuning.

Proposed first-failure detail labels preserve the earliest failing operation: `FAIL__OUTER_INPUT_OR_FROZEN_IDENTITY` (precall identity, axis, denominator or `Kt0`); `FAIL__OUTER_SELECTOR_OR_D2` (policy/generator legality); `FAIL__OUTER_HJB` (direct solve, residual or convergence); `FAIL__OUTER_RELAXATION_EXHAUSTED` (accepted alpha schedule exhausted); `FAIL__OUTER_KFE` (topology, restricted solve or full-Q validation); `FAIL__OUTER_CAPITAL_OR_C1` (capital/share/C1 identity); `FAIL__OUTER_FIRM_OR_DOWNSTREAM` (firm, wage, monetary or fiscal); `FAIL__OUTER_RAW_PAYOFF_TIMING` (lagged raw return or same-S mismatch); and `FAIL__OUTER_INCOMPLETE_CHECKPOINT` (seal/readback). These are proposed reporting labels, not changes to existing inner terminals. Preserve the original inner terminal and exact location as nested evidence.

The first failed gate is terminal. No second integration, borrowed allowance or repaired rerun follows it. Record clipped `ra` boundary hits at every checkpoint. Whether they disqualify the new nine-component criterion is an explicit Owner decision; the original MATLAB zero-hit predicate is separate and cannot be claimed passed from this new comparison.

## Proposed maximum two new complete turns from sealed C6

This is an algebraic ceiling proposal, **not execution permission**. The source is the prior exact turn5-turn6 task's `Scientific ceilings for the two-turn task` section, cross-checked where equivalent with its combined ledger's `ceilings`. Each of 31 provinces has at most 50 direct HJB updates. An initial policy map plus up to 50 post-update maps gives 51 maps per province; each map has 800 selector evaluations. Each update has one relaxation helper and up to 53 arithmetic alpha candidates (`1,2^-1,...,2^-52`). All failed attempts consume their category budget. Per-turn and combined ceilings are distinct.

| Category | Per turn | Two turns | Derivation / boundary |
|---|---:|---:|---|
| source-native initializations | 31 | 62 | 31 x 1 |
| scalar labor roots attempted | 24,800 | 49,600 | 31 x 800 |
| scalar labor roots returned | 24,800 | 49,600 | at most attempts; may be fewer on failure |
| corrected policy maps | 1,581 | 3,162 | 31 x (1 initial + 50 updates) |
| D2/Q assemblies | 1,581 | 3,162 | 31 x (1 initial + 50 updates) |
| selector evaluations | 1,264,800 | 2,529,600 | 31 x 51 x 800 |
| direct HJB solves/updates | 1,550 | 3,100 | 31 x 50; one spsolve/update |
| post-update HJB checkpoints | 1,550 | 3,100 | 31 x 50 |
| relaxation helper invocations | 1,550 | 3,100 | 31 x 50 |
| alpha arithmetic candidates | 82,150 | 164,300 | 31 x 50 x 53 |
| SCC decompositions | 31 | 62 | 31 x 1 |
| restricted GESVD | 31 | 62 | 31 x 1 |
| normalized stationary candidates | 31 | 62 | 31 x 1 |
| full-Q stationary checks | 31 | 62 | 31 x 1 |
| corrected aggregate evaluations | 31 | 62 | 31 x 1 |
| household batches | 1 | 2 | one after 31/31 HJB/KFE |
| source-faithful labor reconstructions | 1 | 2 | one/integration |
| frozen K1B quantity allocations | 1 | 2 | one with entering S |
| C1 residual GovInv constructions | 1 | 2 | one/integration |
| firm evaluations | 31 | 62 | 31 x 1 |
| composite wage batches | 1 | 2 | one/integration |
| monetary assignments | 1 | 2 | one/integration |
| fiscal diagnostic batches | 1 | 2 | one/integration |
| completed raw ra0 vectors | 1 | 2 | one/completed turn |
| lagged next K1B preparations | 1 | 2 | one/from completed ra0 |
| same-S raw next payoff constructions | 1 | 2 | one/from same S |
| full-space 800x800 GESVD | 0 | 0 | forbidden |
| scientific retries | 0 | 0 | forbidden |
| solver substitutions | 0 | 0 | forbidden |
| household after proposed turn8 | 0 | 0 | stop before turn9; new proposed boundary |
| K2/GE/MATLAB/Results | 0 | 0 | closed route; inherited zero |

The original task/ledger do not give separate numeric ceilings for `scalar_selector_root_invocations`, standalone KFE total calls, or an independently defined K1B feedback operation. These remain `UNRESOLVED`; observed old counts cannot be converted into new caps. The zero post-turn8 household boundary is a **new proposed boundary**, not the literal old turn7-zero rule. Same-frozen-state repeats have no allowance in this table and require separate authorization.

## Proposed terminal classes

| First terminal condition | `PROPOSED_NOT_ADOPTED` class |
|---|---|
| Identity, household, integration or timing legality failure | Preserve the exact first `FAIL__...` label, location and consumed-call ledger; stop. |
| Incomplete checkpoint, including seal/readback failure or mid-turn budget exhaustion | `FAIL__OUTER_INCOMPLETE_CHECKPOINT` with reason; use `FAIL__OUTER_INCOMPLETE_CHECKPOINT__BUDGET_EXHAUSTED` for a cap. |
| Two complete legal new turns and neither all-nine pass | `VALID__LEVEL_NOT_MET_AT_BUDGET`. |
| Exactly one of two legal adjacent comparisons passes | `VALID__ONE_PASS_UNCONFIRMED_AT_BUDGET`. |
| C6→C7 and C7→C8 both legal and pass all nine | `CRITERION_MET_FOR_BOUNDED_K1B_MAP_ONLY__INDEPENDENT_REVIEW_PENDING`. |

Even the final label would mean only that a predetermined numerical criterion for the frozen bounded K1B map was met, pending independent Work review. It is not contraction, a mathematical fixed point, the original MATLAB outer predicate, steady state, GE, calibration validity or Results eligibility.

## Explicit Owner decisions

| Choice | Pending decision/evidence |
|---|---|
| Carrier/formulas | Adopt or reject same-stage eight-vector/one-matrix carrier, frozen identity, four formula families and strict comparator. |
| `1e-6` | Decide whether agreed diagnostic precision becomes a stopping level. General outer numerical error bound remains `UNAVAILABLE`; `1e-12` remains aspirational. |
| Pass count | Choose R1, R2 or R3 evidence first. Recommended R3 first; R2 conditional on a later stop-law adoption. |
| Clipped `ra` | Choose whether 31/31 upper hits are disqualifying or reported only for this new criterion. Original MATLAB required zero hits. |
| Maximum turns and calls | Adopt/reject up to two complete new turns, 50 updates/province and every category ceiling; resolve independently counted root/KFE/feedback categories if needed. Repeat budget separate. |
| Failure/uncertainty | Adopt/reject legality-first labels and no-retry protocol. Same-state repeatability is absent and general outer-map error bound `UNAVAILABLE`. |
| Subsequent execution | Only after substantive Owner adoption and Work review may Work issue a separate bounded turn7/turn8 task with exact input hashes, budget, stop paths and review gate. This proposal authorizes no call. |
