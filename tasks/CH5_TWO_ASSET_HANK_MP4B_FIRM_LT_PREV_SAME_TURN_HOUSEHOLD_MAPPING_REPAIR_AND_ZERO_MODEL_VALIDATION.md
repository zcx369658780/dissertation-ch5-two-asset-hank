# CH5_TWO_ASSET_HANK_MP4B_FIRM_LT_PREV_SAME_TURN_HOUSEHOLD_MAPPING_REPAIR_AND_ZERO_MODEL_VALIDATION

Date: 2026-09-01

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / source-faithful implementation repairer

Owner: final scientific authority

## 1. Authority basis and accepted defect

Accepted predecessor execution:

`MP4B_L3_READ_ONLY_TURN1_SOURCE_LAYER_NUMERICAL_ATTRIBUTION_AND_FIRST_ACTIONABLE_DIVERGENCE_PASS`

Execution commit:

`7904149cd4b1c941684ff6609c0021aa590d6674`

Accepted strongest classification:

`MP4B_SAME_INPUT_SOURCE_LAYER_PYTHON_IMPLEMENTATION_DEFECT_CONFIRMED`

The accepted read-only evidence establishes a bounded Python implementation defect in the multi-province one-turn firm-input mapping:

- protected MATLAB firm path consumes same-turn household `results.Lt` as carried `Lt_1`;
- Python `run_source_faithful_one_turn` constructs `firm_source = dict(provinces[index])`, maps only same-turn `AtTax`, and leaves old-turn `Lt_prev` unchanged;
- for turn-1 Beijing this incorrectly supplies old `Lt_prev = 186000.0` instead of the same-turn household aggregate `household_lt = 0.647623598114104` in the Python runtime path;
- with source-correct same-turn household-Lt substitution, the protected firm `mt` arithmetic reproduces the MATLAB value exactly: `1.0121097874161467`;
- firm `Yt` itself was separately shown to follow the same source formula on each side and is upstream-input-driven;
- the household block remains accepted numerical non-identity within its frozen comparator envelope and is not reopened by this task.

This task authorizes the minimum source-faithful Python repair only. It introduces no new economic equation, parameter, grid, solver algorithm, controller rule, threshold, tolerance, shock design, or Results claim.

## 2. Required live continuity

Required execution-start predecessor:

`7904149cd4b1c941684ff6609c0021aa590d6674`

At execution start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as the direct child of `7904149cd4b1c941684ff6609c0021aa590d6674`;
3. require clean worktree, `HEAD == origin/main`, ahead/behind `0/0`;
4. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
   - `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`;
   - `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`;
   - predecessor task/report;
   - accepted source-semantics map;
   - protected MATLAB `HANK_mp_1turn.m` and `HANK_firm.m` source evidence named by the source map;
   - current `src/ch5_two_asset_hank/multi_province/one_turn.py`;
   - current `src/ch5_two_asset_hank/multi_province/firm.py`;
   - all existing focused tests that exercise MP2 one-turn / firm semantics.

Any authority, identity, or protected-source readability failure => stop before mutation with the BLOCKED terminal in Section 10.

## 3. Frozen starting identities

At task publication the accepted starting blobs are:

- `src/ch5_two_asset_hank/multi_province/one_turn.py`: `0353fbe77856f0f4bad7c1aebd1fcb5c1d11cfd6`;
- `src/ch5_two_asset_hank/multi_province/firm.py`: `1f7d37247e2d712fc0477a9f562dce81d1b367ce`.

The executor must fresh-read and verify these identities before mutation. If live main differs for an authorized reason, do not silently adapt; stop and report the identity mismatch for L3 review.

## 4. Exact authorized implementation change

The required semantic repair is narrowly frozen:

Immediately before the call to `evaluate_firm(...)` for province `index`, the firm source record must carry the **same-turn household aggregate labor** for the protected MATLAB `Lt_1` role.

In the current Python naming contract this means:

`firm_source["Lt_prev"] = float(household.household_lt[index])`

while retaining the existing same-turn tax mapping:

`firm_source["AtTax"] = float(household.at_tax[index])`.

No other firm-source field may be remapped by this task.

Important semantic distinction:

- `household.household_lt[index]` supplies the carried previous/reference labor term used inside the firm `mt` formula (`Lt_1` in protected MATLAB semantics, `Lt_prev` in Python naming);
- `migration.lt_supply[index]` remains the current destination firm labor supplied as the separate `lt_supply` argument to `evaluate_firm` and therefore remains the firm's current `Lt`;
- do **not** replace current destination `lt_supply` with household labor;
- do **not** change `FirmResult.Lt`, migration accounting, capital allocation, wage logic, controller logic, or outer-state semantics.

The preferred source mutation is exactly one new mapping assignment in `run_source_faithful_one_turn`, plus the minimum tests/report needed to freeze it.

## 5. Hard zero-model-execution budget

This is an implementation-and-unit-validation task, not a scientific rerun.

Forbidden scientific/model execution counts are exactly zero:

- MATLAB processes / `checkcode`: `0`;
- MATLAB stationary/HJB/KFE/household/firm/controller: `0`;
- Python corrected-2009 stationary: `0`;
- Python household/HJB/KFE scientific execution: `0`;
- Python MP2/MP3 scientific replay against empirical data: `0`;
- comparator / chronology replay: `0`;
- other year / annual batch: `0`;
- shocks / AR(1) / transition / dynamics / IRF: `0`;
- R5 / Results: `0`.

Allowed validation activity:

- source inspection and hashing;
- `py_compile`;
- focused deterministic unit tests on synthetic fixtures;
- existing non-empirical MP2/firm regression tests;
- AST/static-source contract checks;
- monkeypatch/stub tests that verify the object passed to `evaluate_firm` without invoking any household/HJB/KFE/stationary solver;
- pure scalar reproduction of the already frozen Beijing `mt` formula using persisted evidence, if useful for the report.

Do not invoke the empirical 2009 driver, `run_online_stationary`, a household solver, or a MATLAB executable.

## 6. Required focused validation

The repair must be protected by tests that establish all of the following.

### A. Same-turn household-Lt mapping

For a deterministic synthetic multi-province `OneTurnInputs` object in which old `Lt_prev` is deliberately very different from `household_outputs.household_lt`, verify that the firm-source record passed to `evaluate_firm` contains:

`Lt_prev == household_outputs.household_lt[index]`

for every province.

Prefer monkeypatching/stubbing `evaluate_firm` or an equivalent bounded method so this test verifies mapping semantics rather than re-running scientific model logic.

### B. Current destination labor remains migration labor

Verify separately that the positional/keyword `lt_supply` passed to `evaluate_firm` remains:

`migration.lt_supply[index]`

and is **not** replaced by `household_outputs.household_lt[index]`.

### C. AtTax mapping is preserved

Verify:

`firm_source["AtTax"] == household_outputs.at_tax[index]`.

### D. Old state is not mutated

Verify the immutable/frozen `old_provinces` input remains unchanged after one-turn composition/mapping validation.

### E. No unrelated semantic mutation

Static diff review must establish that the repair does not alter:

- migration equations/orientation;
- capital allocation;
- `evaluate_firm` formula/order;
- wage module;
- monetary/fiscal blocks;
- controller/steady-state code;
- household/HJB/KFE code;
- grids, parameters, thresholds, tolerances, convergence criteria;
- canonical/overlay bindings or validation comparator.

### F. Focused regression

Run the smallest existing non-empirical MP2/firm test subset that covers one-turn and firm behavior. If an existing expected value changes specifically because it encoded the confirmed wrong `Lt_prev` semantics, update only that expected value with explicit report justification. Do not broadly regenerate fixtures.

## 7. Required implementation markers

A PASS report must establish all of:

- `MP4B_FIRM_LT_PREV_SAME_TURN_HOUSEHOLD_MAPPING_REPAIRED`
- `MP4B_CURRENT_FIRM_LT_SUPPLY_REMAINS_MIGRATION_DESTINATION_LABOR`
- `MP4B_FIRM_ATTAX_SAME_TURN_MAPPING_PRESERVED`
- `MP4B_CONFIRMED_SOURCE_LAYER_PYTHON_DEFECT_REPAIRED_ZERO_MODEL`

## 8. Allowed repository mutations

Allowed source path:

- `src/ch5_two_asset_hank/multi_province/one_turn.py`

Allowed focused test mutation:

- preferably one existing MP2/one-turn focused test file if clearly suitable; otherwise create exactly one new focused test file under `tests/` with a descriptive MP4B mapping name.

Required report:

- `docs/CH5_TWO_ASSET_HANK_MP4B_FIRM_LT_PREV_SAME_TURN_HOUSEHOLD_MAPPING_REPAIR_AND_ZERO_MODEL_VALIDATION_REPORT.md`

Do not modify `firm.py` unless the task becomes blocked by a demonstrable interface issue; if that occurs, stop for L3 review rather than expanding scope.

Do not modify validators, canonical data, overlay data, MATLAB, comparator, project rules, roadmap, stationary driver, household code, MP3 steady-state/controller code, or prior reports/tasks.

## 9. Closeout requirements

Before commit:

1. verify changed paths are within Section 8;
2. run `py_compile` on changed Python files;
3. run the focused unit/regression tests frozen in the report;
4. require all tests PASS;
5. record a complete zero-model/science ledger;
6. stage explicit paths only;
7. run `git diff --check --cached` and require PASS.

Then:

- exactly one execution commit;
- exactly one non-force push;
- fresh GitHub read-back of every changed path;
- require `HEAD == origin/main`;
- require ahead/behind `0/0`;
- require clean worktree.

The report must include pre/post source blob/SHA identities, exact diff summary, tests run, marker evidence, zero-model ledger, and exactly one recommended next gate.

## 10. Terminal verdicts

PASS only if the exact bounded source-faithful repair and focused zero-model validation are complete:

`MP4B_FIRM_LT_PREV_SAME_TURN_HOUSEHOLD_MAPPING_REPAIR_AND_ZERO_MODEL_VALIDATION_PASS`

BLOCKED if authority, source identity, protected semantics, or bounded implementation cannot be established without expanding scope:

`MP4B_FIRM_LT_PREV_SAME_TURN_HOUSEHOLD_MAPPING_REPAIR_AND_ZERO_MODEL_VALIDATION_BLOCKED`

A PASS does **not** authorize stationary execution.

## 11. Exactly one recommended next gate

On PASS, recommend exactly one independent L3 review of the repaired source/test evidence, followed only if accepted by a separately authorized **single Python corrected-2009 stationary re-execution** against the already admissible MATLAB chronology.

Do not run that stationary re-execution from this task.
