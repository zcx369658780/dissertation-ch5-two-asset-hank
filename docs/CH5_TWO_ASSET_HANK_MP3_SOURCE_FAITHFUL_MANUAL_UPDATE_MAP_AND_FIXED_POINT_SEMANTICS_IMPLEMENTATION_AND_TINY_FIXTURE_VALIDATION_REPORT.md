# MP3 source-faithful manual update-map and tiny-fixture validation report

## Terminal classification

`MP3_SOURCE_FAITHFUL_MANUAL_UPDATE_MAP_AND_FIXED_POINT_SEMANTICS_IMPLEMENTATION_AND_TINY_FIXTURE_VALIDATION_PASS`

Frozen markers:

- `MP3_SOURCE_ORDERED_MANUAL_UPDATE_MAP_ACCEPTED`
- `MP3_SOURCE_CONVERGENCE_PREDICATE_ACCEPTED`
- `MP3_SOURCE_ZT_ADAPTIVE_UPDATE_ACCEPTED`
- `MP3_SOURCE_GOVINV_ADAPTIVE_UPDATE_ACCEPTED`
- `MP3_SOURCE_TKNRATIO_DAMPING_ACCEPTED`
- `MP3_SOURCE_MAX_ITERATION_FAILURE_SEMANTICS_ACCEPTED`
- `MP3_MANUAL_UPDATE_MAP_AND_CONVERGENCE_PARITY_ACCEPTED`
- `MP3_NO_HOUSEHOLD_SOLVER_GE_OR_LEGACY_RUNTIME_DEPENDENCY_ACCEPTED`

This acceptance is limited to bounded synthetic manual-controller semantics. It is not empirical GE, annual calibration, transition, IRF, dynamics, or Results authority.

## Live authority and prerequisites

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Accepted MP2 implementation: `ebf26b1167baefaf5468a80c16ea3f443131597a`.
- Live MP3 task authority after fresh fetch: `7f3324fceb2b548c3fd582d707bee93873250081`, a direct child of MP2.
- Execution start: clean worktree and fast-forward-only synchronization to live `origin/main`.
- Accepted MP2 `one_turn.py` remained byte-identical, SHA-256 `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`.
- MP1 fixture/evaluator and accepted standalone oracle remained unchanged.

## Protected source identity and line contract

Protected MATLAB was read only and never executed.

| Source | SHA-256 | Controller contract |
|---|---|---|
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` | complete controller, lines 3-66 |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` | old-state one-turn boundary and returned fields |
| `mpHANK_equilibrium_2000.m` | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` | initialization and controller call, lines 22-72 |
| `multi_prov_HANK_12sts.m` | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` | `reg_threshold=1e-9` line 16; `max3iter=500` line 22 |

Exact `HANK_mp_1eq.m` contract:

| Lines | Frozen semantics |
|---|---|
| 3-5 | initialize `tKNratio=3`, `finish=0`, and results from the supplied old state |
| 7-8 | one-based loop `1:num.max3iter`; complete one-turn call precedes diagnostics |
| 10-12 | zero raw gaps and convergence/bound counters each iteration |
| 13-23 | exact-equality counts for `ra` and `wjt` upper/lower bounds |
| 26-34 | `abs(KNratio/tKNratio-1)`, `abs(Yt/Yt_1-1)`, and summed household flags |
| 35-36 | maximum province gaps; no generic residual norm |
| 42-45 | strict `<` on both maxima, all household flags, and zero `ra` bound counts; wage counts excluded; immediate success |
| 47-51 | adaptation gate `maxKNgap<0.1 && steady_state==1`; strict outside ±1%; literal `Zt=Yt0*Kt^(-alpha)*Lt^(alpha-1)` |
| 52-56 | low `ra < ramin+0.02` gives `GovInv*=0.9`; otherwise high `ra > ramax-0.02` gives `GovInv*=1.1` |
| 60-62 | every nonterminal turn damps `tKNratio=0.6*KNratio+0.4*tKNratio` after adaptation |
| 64-65 | final nonconverged iteration raises failure after update bookkeeping |

`Yt_1` is the output entering the firm turn and is compared with the newly produced `Yt`. The firm snapshot also advances `Kt_prev`, `Lt_prev`, `Zt_1`, `pit_1`, and `rk` before the next complete household batch. No province observes another province's partially adapted state inside the same turn. MATLAB's literal `convergent_total==31` is represented as equality to the complete declared fixture province count, which is the required tiny-fixture analogue and does not introduce a vectorized GE ordering.

## Source pseudocode

```text
tKNratio[:] = 3
for j = 1..max3iter:
    consume one complete pre-frozen household batch
    result = accepted_MP2_one_turn(old_state, batch)
    build complete post-turn state and Yt_1 snapshot
    compute raw KN/Y gaps, household count, ra counts, wage counts
    if strict source predicate:
        return immediately without adaptation or damping
    if max(KN gap) < 0.1 and steady_state:
        apply source Zt and GovInv branches province by province
    tKNratio = 0.6*KNratio + 0.4*tKNratio
    if j == max3iter:
        raise source-equivalent nonconvergence failure
```

## Files written

- `src/ch5_two_asset_hank/multi_province/steady_state.py`
- bounded exports in `src/ch5_two_asset_hank/multi_province/__init__.py`
- `validators/multi_province/mp3_update_map_arithmetic.py`
- `tests/fixtures/multi_province/mp3_tiny_multi_turn.json`
- `tests/test_mp3_manual_update_map.py`
- this report

No accepted MP1/MP2 arithmetic, household/oracle source, roadmap, raw data, calibration cache, MATLAB, legacy R5, dynamic, or Results file was modified.

## Public API and state types

- `ManualSteadyStateInputs`
- `ManualSteadyStateResult`
- `IterationRecord`
- `AdaptiveAction`
- `SteadyStateConvergenceError`
- `run_manual_steady_state`
- `SOURCE_MAX_ITERATIONS=500`
- explicit convergence and exhaustion termination constants

Inputs require a complete ordered old state and an explicit finite sequence of immutable pre-frozen household batches. Missing batches fail closed. Iteration history retains entering state, MP2 result, pre-adaptation state, next-turn state, raw vectors/counts, actions, damping references, predicate, and one-based iteration index.

## Fixture and independent-validator identities

- Tiny fixture: `tests/fixtures/multi_province/mp3_tiny_multi_turn.json`.
- Fixture SHA-256: `38F78B72D3FB4BEC1CB4564E66F7465187B02E19DD69CF992F5F21A4EA8A16CF`.
- Classification: `NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE`.
- Independent evaluator: `validators/multi_province/mp3_update_map_arithmetic.py`.
- Evaluator SHA-256: `5E58359534B4EEC2277574E967715AF3B9AFC9D4FAE1B0BFE0EC980FA8A786A4`.
- Production controller SHA-256 before report publication: `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C`.

The independent evaluator imports no production `steady_state.py`; it reconstructs controller arithmetic from source and uses the already independent MP1 arithmetic for each deterministic turn.

## Complete tiny-fixture comparison

Every raw vector, count, boolean, action, pre/post value, `tKNratio`, `Yt_1`, termination, iteration count, and selected final-state field was compared recursively. All seven scenarios were exact Python binary64/categorical matches; the frozen fallback bound `rtol=atol=1e-12` was not needed.

| Scenario | Iterations | Terminal | Key evidence | Classification |
|---|---:|---|---|---|
| delayed convergence | 9 | `SOURCE_CONVERGED` | eight rejected turns; exact raw gap and `tKNratio` histories; all household flags; no `ra` veto at turn 9 | EXACT |
| adaptive updates | 1 | `SOURCE_MAX_ITERATION_EXHAUSTED` | Zt reset in A; low-ra `0.9` in A; high-ra `1.1` in B; no-op in C; exact damping | EXACT |
| household veto | 1 | exhaustion | numeric gaps pass fixture threshold but only 2/3 household flags | EXACT |
| ra boundary veto | 1 | exhaustion | numeric and household tests pass; one exact upper-bound `ra` veto | EXACT |
| wage diagnostic only | 1 | `SOURCE_CONVERGED` | two upper wage-bound counts do not veto | EXACT |
| strict threshold equality | 1 | exhaustion | maximum KN gap equals threshold; strict `<` rejects | EXACT |
| max-iteration exhaustion | 2 | exhaustion | two complete rejected turns, then source-equivalent exception result | EXACT |

Adaptive frozen values for the first record:

| Province | Zt action | Zt pre → post | GovInv action | GovInv pre → post |
|---|---|---|---|---|
| Synthetic-A | reset | `1.1 → 0.5202957134673135` | low-ra decrease | `0.3 → 0.27` |
| Synthetic-B | none | `0.9 → 0.9` | high-ra increase | `0.5 → 0.55` |
| Synthetic-C | none | `1.2 → 1.2` | none | `0.2 → 0.2` |

## Convergence, update, and failure proofs

- A generic residual norm differs from the source maximum-component tests and is not present in production.
- Exact threshold equality is rejected, proving strict `<` rather than `<=`.
- Omitting either the household-all-converged condition or `ra` boundary veto would incorrectly accept dedicated fixtures.
- Adding a wage-bound veto would incorrectly reject the accepted wage-bound fixture.
- The 1.5% synthetic output discrepancy triggers the exact 1% Zt rule, while 0.5% does not; replacing `Yt0` with current `Yt` changes the frozen value.
- Reversing GovInv multiplier directions changes frozen actions/values.
- Reversing the `0.6/0.4` damping weights changes delayed-fixture history.
- Pre-adaptation and next-turn snapshots prove adaptations cannot leak into another province inside the current turn.
- Missing a required batch raises before an unauthorized implicit household call.
- Exhaustion raises `SteadyStateConvergenceError` carrying an auditable non-success result; it cannot be reported as convergence.

## Tests and checks

- Focused MP1+MP2+MP3 regression: `48 passed`.
- MP3 production/validator/test compile check: PASS.
- Recursive exact-parity classifier: all seven scenarios EXACT.
- `git diff --check`: PASS before explicit staging.
- Static AST scan: no forbidden production imports or solver calls.

## Scientific/model execution ledger

| Scientific/model call | Count |
|---|---:|
| MATLAB | 0 |
| modular HJB / KFE | 0 / 0 |
| standalone HA / HJB / KFE / aggregate | 0 |
| legacy R5 | 0 |
| empirical GE | 0 |
| 31-province annual execution | 0 |
| AR1 / shocks | 0 / 0 |
| transition / dynamics / IRF | 0 / 0 / 0 |
| Results | 0 |

Only accepted MP2 arithmetic on bounded synthetic fixtures, independent fixture evaluation, focused tests, hashes, imports, compile, and static checks were executed.

## Forbidden-operation check and residuals

PASS: no forbidden scientific/model operation occurred. Production imports neither `chapter5_model`, `validators`, nor `tests`; it imports no household/HJB/KFE/standalone solver, transition, dynamics, IRF, Brent, Newton, fsolve, least-squares, Jacobian, or residual-vector solver. No empirical workbook/cache was opened or executed.

- Material mismatch list: empty.
- Unresolved scientific residual list within MP3: empty.
- Source/environment failure list: empty.
- MP4 baseline-year/multi-year and calibration-cache provenance remain explicitly unresolved later-stage Owner decisions; they are not MP3 failures.

## Git closeout

Publication uses explicit-path staging, one commit, one non-force push, and live read-back of every changed path. The final handoff records the resulting commit, `HEAD == origin/main`, `0/0` ahead/behind, and clean worktree after the commit exists.

## Acceptance level and recommended next gate

Acceptance level is MP3 source-ordered manual update-map/fixed-point-controller semantics on frozen tiny synthetic fixtures only.

The only recommended next gate is **MP4 provenance-resolution / annual-route preparation**. It must first obtain Owner decisions on baseline-versus-multi-year contract and calibration-cache authority. This report does not authorize a full annual solve.
