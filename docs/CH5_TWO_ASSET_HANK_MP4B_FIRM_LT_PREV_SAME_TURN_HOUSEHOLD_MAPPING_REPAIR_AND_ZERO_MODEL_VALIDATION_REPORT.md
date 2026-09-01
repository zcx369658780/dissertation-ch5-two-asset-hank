# MP4B firm Lt_prev same-turn household mapping repair report

Date: 2026-09-01

## Terminal verdict

`MP4B_FIRM_LT_PREV_SAME_TURN_HOUSEHOLD_MAPPING_REPAIR_AND_ZERO_MODEL_VALIDATION_PASS`

Established:

- `MP4B_FIRM_LT_PREV_SAME_TURN_HOUSEHOLD_MAPPING_REPAIRED`
- `MP4B_CURRENT_FIRM_LT_SUPPLY_REMAINS_MIGRATION_DESTINATION_LABOR`
- `MP4B_FIRM_ATTAX_SAME_TURN_MAPPING_PRESERVED`
- `MP4B_CONFIRMED_SOURCE_LAYER_PYTHON_DEFECT_REPAIRED_ZERO_MODEL`

A PASS is implementation/test evidence only and does not authorize stationary execution.

## Live continuity and frozen identities

- live task/entry HEAD: `5745c3030b6d829914dcafcbdb36461d7f0b26e8`
- required direct parent: `7904149cd4b1c941684ff6609c0021aa590d6674`
- entry: clean, `HEAD == origin/main`, ahead/behind `0/0`
- `one_turn.py` starting blob/SHA-256: `0353fbe77856f0f4bad7c1aebd1fcb5c1d11cfd6` / `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`
- `firm.py` frozen blob/SHA-256: `1f7d37247e2d712fc0477a9f562dce81d1b367ce` / `F0AEA719A4121F5562AAA9CCF3F219CC8AFD6C51F84CC2F64A2FE486CEF7FB69`

All controlling authorities, predecessor evidence, source-semantics map, protected `HANK_mp_1turn.m`/`HANK_firm.m`, current Python source and focused tests were read before mutation. The protected source binds same-turn household `results.Lt` to firm reference `Lt_1`, separately from current destination `Lt=results.Lt_supply`.

## Exact repair

The sole production change is immediately after the preserved same-turn tax assignment and before `evaluate_firm`:

```python
firm_source["AtTax"] = float(household.at_tax[index])
firm_source["Lt_prev"] = float(household.household_lt[index])
```

The `evaluate_firm` call remains:

```python
evaluate_firm(
    firm_source,
    float(capital.kt_supply[index]),
    float(migration.lt_supply[index]),
    inputs.params,
)
```

Thus `household_lt` supplies only the protected carried/reference role; current firm labor remains migration destination `lt_supply`. `firm.py`, migration, capital, firm formulas, wage, monetary/fiscal/controller, household/HJB/KFE, grids, parameters, thresholds, tolerances and bindings are unchanged.

Post-repair `one_turn.py`: blob `e5d6835cdc9e6d182e1c84e11f4d51938be592e1`, SHA-256 `3F2C6C4CD44F06D90D43C2B60B69DEF8141C0AB002A3B3D11972659A4D579A00`, 9,454 bytes. `firm.py` retained its exact starting identities.

## TDD and focused validation

The existing `tests/test_mp2_source_faithful_one_turn.py` received one mapping-focused synthetic tracer test. Its same-turn labor `[10,11,12]` and tax `[0.5,1.5,2.5]` deliberately differ from old source values. A spy on the symbol bound by `one_turn` captures every province's firm source and current labor argument.

RED after the fixture snapshot was corrected: captured `Lt_prev=[1.4,1.8,2.5]`, expected `[10,11,12]`; 1 failed, 8 deselected. GREEN after the single assignment: 1 passed, 8 deselected.

The tracer proves for every synthetic province:

1. `firm_source["Lt_prev"] == household.household_lt[index]`;
2. the current `lt_supply` argument equals `result.migration.lt_supply` and differs from household labor;
3. `firm_source["AtTax"] == household.at_tax[index]`;
4. `old_provinces` is value-identical after composition.

Validation results:

- `python -m py_compile src/.../one_turn.py tests/test_mp2_source_faithful_one_turn.py`: PASS
- `python -m pytest tests/test_mp2_source_faithful_one_turn.py tests/test_mp1_asymmetric_one_turn_fixture.py -q`: `16 passed in 0.82s`
- unstaged `git diff --check`: PASS
- independent scope/source pre-review: PASS; no `firm.py` interface blocker

Post-test file: blob `efe6ca8beb8e8c7da8ae2a0b1faa9756bebfffc6`, SHA-256 `4B884306DEE559A576D8B570C6919A55A0AC6DE0876002A043DC47283E1F57E3`, 12,460 bytes.

## Changed-path and zero-model audit

Allowed changed paths only:

- `src/ch5_two_asset_hank/multi_province/one_turn.py`
- `tests/test_mp2_source_faithful_one_turn.py`
- this report

Scientific/model ledger: MATLAB process/checkcode/model 0; Python stationary 0; household/HJB/KFE 0; empirical MP2/MP3 replay 0; comparator/chronology replay 0; other years/batch 0; shocks/AR1/transition/dynamics/IRF 0; R5/Results 0. Only source reads/hashes, compilation and deterministic synthetic unit/regression tests ran.

## Exactly one recommended next gate

Independent L3 review of this exact repair and test evidence; only if accepted may a separate live task authorize one Python corrected-2009 stationary re-execution against the existing admissible MATLAB chronology.
