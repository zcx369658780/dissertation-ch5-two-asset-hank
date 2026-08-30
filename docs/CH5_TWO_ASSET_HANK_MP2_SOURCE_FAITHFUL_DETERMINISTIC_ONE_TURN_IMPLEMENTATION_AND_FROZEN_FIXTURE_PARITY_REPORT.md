# MP2 source-faithful deterministic one-turn implementation report

## Terminal classification

`MP2_SOURCE_FAITHFUL_DETERMINISTIC_ONE_TURN_IMPLEMENTATION_AND_FROZEN_FIXTURE_PARITY_PASS`

Frozen acceptance markers:

- `MP2_SOURCE_FAITHFUL_MIGRATION_LABOR_PARITY_ACCEPTED`
- `MP2_AT_ONLY_CAPITAL_AND_RAH_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_FIRM_BLOCK_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_COMPOSITE_WAGE_PARITY_ACCEPTED`
- `MP2_TAYLOR_AND_FISCAL_DIAGNOSTIC_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_ONE_TURN_COMPONENT_PARITY_ACCEPTED`
- `MP2_NO_HOUSEHOLD_SOLVER_OR_LEGACY_RUNTIME_DEPENDENCY_ACCEPTED`

This is deterministic three-province source-formula evidence only. It is not a fixed point, annual calibration, GE, transition, IRF, dynamics, or Results acceptance.

## Live authority and prerequisites

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Execution-start accepted MP1 parent: `87a1e30d4f8c3cb0bfe1afaf2b80e4c374a7e6a2`.
- Live MP2 task authority after fresh fetch and fast-forward: `178e9dfe32b0da82be92d663e6cbfc4fed94179c`.
- Start worktree: clean and `HEAD == origin/main`.
- Frozen fixture: `tests/fixtures/multi_province/mp1_asymmetric_one_turn.json`, SHA-256 `7B8ACDB78F8BA92C9BAEA162A83F56CF4558DEE2802277281EDAF8B43D092219`.
- Fixture classification: `NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE`.
- Independent evaluator: `validators/multi_province/mp1_fixture_arithmetic.py`, SHA-256 `876940E58E7FF59FE5AD6E4C7D30437893965F1ABE0189196A09292E1E350D10`.
- Accepted standalone household oracle remained byte-identical, SHA-256 `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.

The frozen JSON, independent evaluator, MP1 contract/adapter modules, and accepted household/oracle source were not modified.

## Protected MATLAB source map

The protected MATLAB tree was read only and never executed.

| Source | SHA-256 | Bound implementation |
|---|---|---|
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` | labor supply 21-26; At-only capital and rah 28-40; firm/wage 44-53; Taylor/fiscal 60-66 |
| `Lt_seperate.m` | `D30519AD81837E8EB5EBFE74BF25CC770E40B5C5AE5A254951AD97D436CACE26` | destination-row/origin-column labor 6-14 |
| `HANK_firm.m` | `EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5` | feasible steady-state firm branch 5-98 |
| `wage_caculate.m` | `0FB84B51E2BE50CD3D065D33385882311A31E12596AEEB0CE2C808A8C36B6A63` | origin household composite wage 4-16 |

The labor formula preserves origin-indexed tax; the wage formula preserves destination-indexed tax. Productive contribution is exactly `q_i * At_i * N_i`; `Bt` is absent from the capital API. `rah`, firm clipping/tax adjustments, Taylor assignment, and fiscal diagnostic retain literal source ordering.

## Files written

- `src/ch5_two_asset_hank/multi_province/migration_labor.py`
- `src/ch5_two_asset_hank/multi_province/capital_allocation.py`
- `src/ch5_two_asset_hank/multi_province/firm.py`
- `src/ch5_two_asset_hank/multi_province/wage.py`
- `src/ch5_two_asset_hank/multi_province/monetary.py`
- `src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py`
- `src/ch5_two_asset_hank/multi_province/one_turn.py`
- bounded exports in `src/ch5_two_asset_hank/multi_province/__init__.py`
- `tests/test_mp2_source_faithful_one_turn.py`
- this report

No raw/binary data, calibration cache, figure, or Results artifact was added.

## Public API and update order

The component APIs expose immutable inputs/results and literal arithmetic. The composed public boundary is:

- `PreFrozenHouseholdOutputBatch`
- `OneTurnInputs`
- `OneTurnResult`
- `run_source_faithful_one_turn` / `compose_one_turn`
- `SOURCE_UPDATE_ORDER`

The complete batch of already-computed household outputs is mandatory; there is no callback and no household solver import. The frozen order is:

1. pre-frozen household outputs;
2. migration labor and destination `Lt_supply`;
3. At-only productive contribution, `Kt_supply`, and pre-firm `rah`;
4. province firm blocks using `Lt_supply`;
5. household composite wage;
6. Taylor `it` and `rb`;
7. fiscal diagnostics.

No outer-loop convergence, damping, `Zt`/`GovInv` heuristic, or update-map controller is present.

## Complete frozen-fixture parity

Every listed object was compared both to the immutable JSON and to the independent evaluator. The production and evaluator binary64 arithmetic produced exact Python equality for every frozen value; the predeclared fallback bound `rtol=1e-12, atol=1e-12` also passed and was not loosened.

| Object | JSON | Independent evaluator | Classification |
|---|---|---|---|
| `Lt_mat` | PASS | PASS | EXACT |
| `Lt_supply` | PASS | PASS | EXACT |
| productive contribution | PASS | PASS | EXACT |
| `Kt_supply` | PASS | PASS | EXACT |
| `rah` | PASS | PASS | EXACT |
| firm `Kt` | PASS | PASS | EXACT |
| firm `Lt` | PASS | PASS | EXACT |
| firm `Yt` | PASS | PASS | EXACT |
| firm `mt` | PASS | PASS | EXACT |
| firm `KNratio` | PASS | PASS | EXACT |
| firm `wt0` | PASS | PASS | EXACT |
| firm `wjt` | PASS | PASS | EXACT |
| firm `rk` | PASS | PASS | EXACT |
| firm `Thetat` | PASS | PASS | EXACT |
| firm `It` | PASS | PASS | EXACT |
| firm `PIt` | PASS | PASS | EXACT |
| firm `Corptax` | PASS | PASS | EXACT |
| firm `ra0` | PASS | PASS | EXACT |
| firm `ra` | PASS | PASS | EXACT |
| firm `Govinc` | PASS | PASS | EXACT |
| household composite wage | PASS | PASS | EXACT |
| Taylor `rb` | PASS | PASS | EXACT |
| `Govinc` vector | PASS | PASS | EXACT |
| national `GovSurplus` | PASS | PASS | EXACT |

Material mismatch list: empty. Unresolved scientific residual list: empty within MP2. Source/environment failure list: empty.

## Negative, invariance, and branch tests

Focused tests prove:

- a transposed destination/origin matrix changes parity, while order and shape violations fail closed;
- negative labor and wage power bases fail closed;
- `At+Bt` productive capital fails parity;
- a `Bt`-only perturbation leaves contribution and `Kt_supply` exactly unchanged;
- generic/simple-average `rah` fails parity;
- firm `Lt` equals destination `Lt_supply`, not household `Lt`;
- return clipping and its corporate-tax adjustment are exercised by the frozen fixture;
- synthetic source-formula branch tests exercise return lower clipping, wage lower/upper clipping, their tax adjustments, and the negative-profit floor;
- `GovSurplus` remains a nonzero diagnostic, so no balanced-budget reinterpretation is imposed;
- AST checks find no production import from `validators`, `tests`, or `chapter5_model`;
- AST checks find no household/HJB/KFE/fixed-point/transition/dynamics/IRF solver invocation.

## Checks and execution ledger

- Focused MP2 plus MP1 regression: `34 passed`.
- Python compile check for MP2 source and test: PASS.
- `git diff --check`: PASS.
- Complete exact-equality classification script: all compared objects EXACT.
- Independent read-only review: recorded before publication.

| Scientific/model call | Count |
|---|---:|
| MATLAB | 0 |
| modular HJB / KFE | 0 / 0 |
| standalone HA / HJB / KFE / aggregate | 0 |
| legacy R5 model | 0 |
| fixed point / GE | 0 / 0 |
| annual 31-province execution | 0 |
| AR1 / shocks | 0 / 0 |
| transition / dynamics / IRF | 0 / 0 / 0 |
| Results | 0 |

Allowed deterministic MP2 fixture arithmetic, imports, hashes, static checks, compile checks, and focused tests were the only executions.

## Forbidden-operation check and closeout

PASS: no MATLAB or scientific solver was run; no household/oracle, MP1 immutable evidence, protected MATLAB, legacy R5 repository, roadmap, annual/cache provenance, transition/dynamics/IRF, or Results path was modified or invoked. Production imports neither tests/validators nor the historical runtime.

Publication uses explicit-path staging, one commit, one non-force push, and live read-back of every changed path. Final commit identity, `HEAD == origin/main`, `0/0` ahead/behind, and clean-worktree evidence are reported in the execution handoff after the commit exists.

## Acceptance level and next gate

Acceptance is MP2 component and deterministic one-turn parity on the frozen asymmetric fixture only.

The only recommended next gate is **MP3 manual update-map and fixed-point semantics implementation/validation on frozen tiny multi-turn fixtures**. Full annual 31-province execution remains excluded until the later Owner provenance checkpoint.
