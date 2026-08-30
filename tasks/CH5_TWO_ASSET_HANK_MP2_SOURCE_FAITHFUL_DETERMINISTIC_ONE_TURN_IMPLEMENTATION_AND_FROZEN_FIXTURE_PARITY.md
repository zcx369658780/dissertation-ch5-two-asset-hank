# CH5_TWO_ASSET_HANK_MP2_SOURCE_FAITHFUL_DETERMINISTIC_ONE_TURN_IMPLEMENTATION_AND_FROZEN_FIXTURE_PARITY

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / source-faithful outer-block implementer

Owner: final scientific authority

## 1. Purpose

Implement **MP2 only**: the deterministic MATLAB-faithful multi-province **one-turn outer block** on the frozen MP1 asymmetric three-province fixture.

The production implementation must reproduce the source-defined arithmetic and ordering around already-computed household outputs:

`pre-frozen household outputs -> migration labor -> At-only productive capital and rah -> firm -> household composite wage -> Taylor rb -> fiscal diagnostics`.

This task does **not** call the household solver and does **not** solve the multi-province fixed point. It creates the production one-turn component layer required before MP3.

## 2. Controlling authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MP1_SOURCE_FAITHFUL_MULTI_PROVINCE_CONTRACTS_ACCEPTED_HA_ADAPTER_AND_DETERMINISTIC_ONE_TURN_FIXTURE_FREEZE_REPORT.md`

Owner route remains frozen:

- `OWNER_SINGLE_ACTIVE_CODEBASE_TWO_ASSET_HANK_ONLY`
- `LEGACY_ONE_ASSET_R5_SUPERSEDED_NO_ACTIVE_PROGRAM_AUTHORITY`
- `ACTIVE_MODEL_REPOSITORY_DISSERTATION_CH5_TWO_ASSET_HANK`

Primary numerical/source authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

MP1 accepted markers are prerequisites and must remain unchanged:

- `MP1_SOURCE_FAITHFUL_CONTRACTS_ADAPTER_AND_ONE_TURN_FIXTURE_FREEZE_ACCEPTED`
- `MP1_PROVINCE_ORDER_AND_ORIENTATION_CONTRACT_ACCEPTED`
- `MP1_AT_ONLY_PRODUCTIVE_CAPITAL_CONTRACT_ACCEPTED`
- `MP1_ACCEPTED_TWO_ASSET_HA_STATIC_ADAPTER_CONTRACT_ACCEPTED`
- `MP1_NO_LEGACY_R5_RUNTIME_DEPENDENCY_ACCEPTED`
- `MP1_ASYMMETRIC_ONE_TURN_OUTER_FIXTURE_ACCEPTED`

## 3. Live continuity

Expected execution-start parent / MP1 implementation commit:

`87a1e30d4f8c3cb0bfe1afaf2b80e4c374a7e6a2`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` as a direct child of the MP1 implementation commit;
3. require clean worktree;
4. verify MP1 report and frozen fixture identities;
5. verify the accepted standalone household oracle remains byte-identical;
6. verify no legacy `chapter5_model` runtime import exists in active source.

If continuity fails, stop BLOCKED.

## 4. Protected MATLAB read-only authority

Read only from:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Re-verify source hashes before implementation, at minimum:

- `HANK_mp_1turn.m` — `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF`
- `Lt_seperate.m` — `D30519AD81837E8EB5EBFE74BF25CC770E40B5C5AE5A254951AD97D436CACE26`
- `HANK_firm.m` — `EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5`
- `wage_caculate.m` — `0FB84B51E2BE50CD3D065D33385882311A31E12596AEEB0CE2C808A8C36B6A63`

Use exact source lines recorded by MP1/MP0. Do not modify or run MATLAB.

## 5. Frozen independent validation authority

The following MP1 artifacts are immutable in MP2 and must not be edited:

- `tests/fixtures/multi_province/mp1_asymmetric_one_turn.json`
  - expected SHA-256: `7B8ACDB78F8BA92C9BAEA162A83F56CF4558DEE2802277281EDAF8B43D092219`
  - classification: `NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE`
- `validators/multi_province/mp1_fixture_arithmetic.py`
- MP1 contract modules under `src/ch5_two_asset_hank/multi_province/`

The MP1 validator remains the independent fixture oracle for MP2. Production code must not import from `validators/` or `tests/`.

If MP2 exposes a contradiction in an accepted MP1 contract/fixture, do not silently repair MP1. Stop with the appropriate non-PASS terminal and report the contradiction for L3/Owner adjudication.

## 6. Required production modules

Create only the source-faithful component layer under:

`src/ch5_two_asset_hank/multi_province/`

Authorized new production paths:

- `migration_labor.py`
- `capital_allocation.py`
- `firm.py`
- `wage.py`
- `monetary.py`
- `fiscal_diagnostics.py`
- `one_turn.py`

A bounded update to:

- `src/ch5_two_asset_hank/multi_province/__init__.py`

is allowed only to expose accepted MP2 public objects.

Do not modify accepted household/HJB/KFE/oracle source.

## 7. Exact one-turn semantics to implement

### 7.1 Input boundary

The production one-turn function must consume a **complete batch of already-computed household outer outputs** for all provinces plus the old-turn province state/parameters required by the MATLAB formulas.

It must not call:

- `solve_matlab_faithful_hjb`;
- stationary KFE;
- `solve_household_steady_state`;
- any current modular HA solver;
- any legacy R5 solver.

This preserves MATLAB one-turn simultaneity: all province household outputs are conceptually computed from the copied old state before any cross-province outer update uses them.

The production API must make the pre-frozen-household-output boundary explicit; do not hide it behind an optional callback or implicit solver invocation.

### 7.2 Migration labor — literal source orientation

Implement `Lt_seperate.m` source arithmetic with:

- matrix orientation: `Lt_mat[destination, origin]`;
- columns = origin households;
- rows = destination firms;
- `Lt_supply[destination] = sum_origin Lt_mat[destination, origin]`;
- consumption and population indexed by origin;
- `wjt` indexed by destination;
- preserve the exact source tax/migration/phi index placement frozen by MP1.

Important source quirk to preserve and test:

- `Lt_seperate` and `wage_caculate` do not use identical tax indexing. Do not “harmonize” them.

Fail closed if the power base is negative/non-real or inputs violate frozen shape/order/finite contracts.

### 7.3 Productive capital and household illiquid return

Implement the literal `HANK_mp_1turn.m` capital/return formulas frozen by MP1:

- private productive contribution from province `i` is only `inter_prv_ratio[i] * At[i] * N[i]`;
- `Bt` is liquid and must never enter productive capital;
- changing only `Bt` must leave productive-capital objects invariant;
- destination `Kt_supply` uses the exact source exclusion/division formula;
- `rah` uses the exact literal ratio placement from source, not generic `W @ ra`, not normalized portfolio weights, and not `At+Bt`.

Expose the intermediate contribution vector so parity can localize errors before `Kt_supply`.

### 7.4 Firm block

Implement the source-backed feasible steady-state branch of `HANK_firm.m` used by the MP1 fixture.

At minimum expose and validate:

- `Kt = Kt_supply + GovInv`;
- firm labor = `Lt_supply`;
- `Yt`;
- `mt`;
- `KNratio`;
- unclipped `wt0`;
- clipped `wjt` and associated corporate-tax adjustment;
- `rk`;
- Rotemberg adjustment object `Thetat`;
- investment `It`;
- profit `PIt`;
- `Corptax`;
- unclipped `ra0`;
- clipped `ra` and associated corporate-tax adjustment;
- `Govinc`.

Preserve MATLAB clipping bounds and ordering literally. Do not redesign the firm problem.

If the fixture exercises only one source branch, implement only the source-defined branches necessary for a faithful one-turn production function **if all branch behavior is explicitly covered by source-bound unit tests**. Prefer full source branch coverage when feasible without introducing new economic assumptions.

### 7.5 Household composite wage

Implement `wage_caculate.m` exactly:

- output indexed by origin household province;
- destination firm wage enters each destination term;
- preserve exact source destination/origin tax, migration wedge and `phi` placement;
- preserve source exponents and `alphal` scaling;
- fail closed on non-real/invalid power bases.

Do not collapse this to a generic average wage.

### 7.6 Monetary block

Implement the exact one-turn Taylor assignment:

`it = istar + rho_pi * totalpit + epsilon_pi`

`rb = it - totalpit`

Keep `rb_gap` separate; it is a household borrowing spread, not part of productive return or the Taylor assignment.

### 7.7 Fiscal diagnostics

Implement source-defined diagnostic objects only:

- province `Govinc` from firm block;
- national `GovSurplus = sum_i(Govinc_i - Bt_i * rb_i * N_i)` using the source role/indexing;

Do not impose a balanced-budget equation or target surplus to zero.

### 7.8 One-turn result and update order

`one_turn.py` must compose components in the source order:

1. accept the complete pre-frozen household-output batch;
2. reconstruct migration labor and `Lt_supply`;
3. construct productive-capital contributions / `Kt_supply` and pre-firm `rah` from the old-turn source objects required by source;
4. run the firm block for every province;
5. compute household composite wages from firm wages;
6. compute Taylor `rb`;
7. compute fiscal diagnostics;
8. return a typed/immutable auditable result containing all frozen intermediate objects needed by MP3.

Do not implement `Zt`/`GovInv` heuristic adjustment, `tKNratio` damping, convergence tests, or the outer loop. Those belong to MP3.

Do not call the household solver inside `one_turn.py`.

## 8. Validation contract

### 8.1 Frozen fixture parity

Against the immutable MP1 fixture and independent MP1 evaluator, compare at minimum:

- `Lt_mat`;
- `Lt_supply`;
- capital contribution vector;
- `Kt_supply`;
- `rah`;
- every firm field frozen in fixture;
- household composite wage;
- Taylor `rb`;
- `Govinc`;
- `GovSurplus`.

The independent evaluator and frozen JSON must not import production MP2 code.

For identical Python binary64 formulas/arithmetic order, require exact equality where representation permits. Where deterministic floating reduction/order differs despite source-equivalent arithmetic, use only the already frozen MP1 fixture comparison bound `rtol=1e-12, atol=1e-12`; do not loosen it and explicitly classify every non-exact field.

No post-hoc tolerance selection.

### 8.2 Required negative/invariance tests

Tests must prove at minimum:

- transposed origin/destination labor orientation fails;
- province reordering/shape mismatch fails;
- negative/non-real labor/wage power bases fail closed;
- replacing `At` with `At+Bt` fails fixture parity;
- a `Bt`-only perturbation leaves productive-capital contribution and `Kt_supply` unchanged;
- generic `W`/simple-average replacement for `rah` fails;
- firm uses `Lt_supply`, not household aggregate `Lt`;
- removing/altering wage or return clipping fails relevant tests;
- balanced-budget reinterpretation is absent;
- legacy `chapter5_model` runtime import remains absent;
- production code does not import `validators` or `tests`;
- production one-turn path contains no HA/HJB/KFE/fixed-point/dynamic solver invocation.

### 8.3 Source branch tests

Add focused source-line-bound tests for any firm/wage/labor clipping or conditional branch implemented beyond the main frozen fixture branch. Synthetic branch fixtures are allowed only when clearly labeled source-formula tests and not calibration evidence.

## 9. Scientific/model execution budget

Forbidden calls in MP2:

- MATLAB scientific execution: `0`;
- current modular HJB/KFE scientific calls: `0/0`;
- standalone HA/HJB/KFE/aggregate calls: `0`;
- legacy R5 model calls: `0`;
- multi-province fixed-point / GE calls: `0`;
- annual 31-province solve: `0`;
- AR1 / shock response / transition / dynamics / IRF calls: `0`.

Allowed execution:

- deterministic MP2 component and one-turn arithmetic on the frozen three-province fixture;
- focused unit tests and source-formula branch tests;
- import/compile/type/static checks;
- independent fixture comparator.

No empirical data/calibration execution is authorized.

## 10. Allowed repository changes

On PASS, authorized changed paths are limited to:

- the seven MP2 production modules listed in Section 6;
- bounded `multi_province/__init__.py` update;
- MP2-focused tests under `tests/`;
- optional clearly labeled tiny source-formula fixtures under `tests/fixtures/multi_province/` if needed for branch testing;
- one MP2 report under `docs/`.

Do not modify:

- MP1 frozen JSON fixture;
- MP1 independent evaluator;
- accepted MP1 contract/adapter source unless a contradiction causes non-PASS and a later task authorizes repair;
- accepted household/HJB/KFE/oracle source;
- protected MATLAB;
- historical one-asset R5 repository;
- CURRENT roadmap in this execution task.

Do not add raw `.mat`, `.xlsx`, large/binary output, calibration cache, figures, or Results files.

## 11. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP2_SOURCE_FAITHFUL_DETERMINISTIC_ONE_TURN_IMPLEMENTATION_AND_FROZEN_FIXTURE_PARITY_REPORT.md`

Include at minimum:

1. terminal classification;
2. live start/final pre-publication authority;
3. MP1 prerequisite identities and fixture/validator hashes;
4. MATLAB source hashes and exact line/formula map;
5. files written;
6. public production API;
7. source update order;
8. complete frozen-fixture comparison table;
9. exact vs within-frozen-bound classification for every compared object;
10. all negative/invariance tests;
11. source branch test coverage;
12. no-household-solver/no-fixed-point/no-legacy-import proof;
13. scientific/model call ledger;
14. material mismatch list;
15. unresolved scientific residual list;
16. source/environment failure list;
17. forbidden-operation check;
18. tests/static checks;
19. git closeout;
20. recommended next gate.

## 12. Acceptance markers and terminals

PASS terminal:

`MP2_SOURCE_FAITHFUL_DETERMINISTIC_ONE_TURN_IMPLEMENTATION_AND_FROZEN_FIXTURE_PARITY_PASS`

On PASS freeze:

- `MP2_SOURCE_FAITHFUL_MIGRATION_LABOR_PARITY_ACCEPTED`
- `MP2_AT_ONLY_CAPITAL_AND_RAH_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_FIRM_BLOCK_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_COMPOSITE_WAGE_PARITY_ACCEPTED`
- `MP2_TAYLOR_AND_FISCAL_DIAGNOSTIC_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_ONE_TURN_COMPONENT_PARITY_ACCEPTED`
- `MP2_NO_HOUSEHOLD_SOLVER_OR_LEGACY_RUNTIME_DEPENDENCY_ACCEPTED`

MATERIAL terminal:

`MP2_SOURCE_FAITHFUL_DETERMINISTIC_ONE_TURN_IMPLEMENTATION_AND_FROZEN_FIXTURE_PARITY_MATERIAL_MISMATCH`

BLOCKED terminal:

`MP2_SOURCE_FAITHFUL_DETERMINISTIC_ONE_TURN_IMPLEMENTATION_AND_FROZEN_FIXTURE_PARITY_BLOCKED`

An accepted MP1 contradiction must not be hidden inside MP2; stop non-PASS and report it.

## 13. Repository closeout

If PASS:

- explicitly stage only authorized MP2 paths;
- no `git add .` / `git add -A`;
- one commit;
- one non-force push;
- GitHub read-back every changed path;
- require `HEAD == origin/main`;
- require ahead/behind `0/0`;
- require clean worktree.

On non-PASS, restore any unaccepted production/test candidates and publish report only, unless preserving a bounded diagnostic artifact is explicitly justified by this task without creating active scientific authority.

## 14. Explicit prohibitions

Do not:

- call or modify the two-asset household solver/oracle;
- implement the MP3 fixed-point loop;
- implement `Zt`/`GovInv` heuristic adjustment or convergence/damping controller;
- select baseline year or calibration-cache authority;
- execute 31-province annual model;
- create or retain a legacy one-asset runtime dependency;
- implement or run shocks, AR1, transition, dynamics, IRF, or Results;
- reinterpret MATLAB comparative-statics IRF as genuine dynamics;
- replace source formulas with cleaner generic economics;
- use `At+Bt` as productive capital;
- introduce balanced fiscal/goods/NFI/CA closures from historical R5.

## 15. Next gate boundary

If and only if PASS, recommend only:

**MP3 manual update-map and fixed-point semantics implementation/validation on frozen tiny multi-turn fixtures.**

MP3 must still exclude full annual 31-province execution until the Owner resolves the MP4 baseline-year/cache provenance checkpoint.