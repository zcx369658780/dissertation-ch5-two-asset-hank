# CH5_TWO_ASSET_HANK_MP1_SOURCE_FAITHFUL_MULTI_PROVINCE_CONTRACTS_ACCEPTED_HA_ADAPTER_AND_DETERMINISTIC_ONE_TURN_FIXTURE_FREEZE

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / source-contract implementer / fixture freezer

Owner: final scientific authority

## 1. Purpose

Implement **MP1 only** under the Owner-frozen two-asset-only route.

This task must freeze the source-faithful multi-province contracts needed before any outer-model implementation:

1. province order and annual/data/cache provenance schemas;
2. exact origin/destination and issuer/holder orientation contracts;
3. `At`/`Bt`, household-labor/firm-labor, wage/return role separation;
4. a static, non-mutating adapter contract to the already accepted two-asset HA implementation;
5. one asymmetric deterministic **outer-logic one-turn fixture** with pre-frozen household outputs;
6. expected intermediate/output arithmetic for that fixture, bound to MATLAB source formulas;
7. explicit proof that the active package has no runtime dependency on the superseded one-asset R5 repository.

This task is not authority to implement the actual one-turn production algorithm, solve a fixed point, run a household solver, choose an empirical baseline year, or run dynamics/IRFs.

## 2. Owner route authority

The controlling Owner decision is frozen in the CURRENT roadmap at live main:

- `OWNER_SINGLE_ACTIVE_CODEBASE_TWO_ASSET_HANK_ONLY`
- `LEGACY_ONE_ASSET_R5_SUPERSEDED_NO_ACTIVE_PROGRAM_AUTHORITY`
- `ACTIVE_MODEL_REPOSITORY_DISSERTATION_CH5_TWO_ASSET_HANK`

The only active model repository is:

`zcx369658780/dissertation-ch5-two-asset-hank`

The historical repository:

`zcx369658780/dissertation-ch5-r5-python-model`

is read-only historical/audit evidence only. Do not modify it, import it, copy its scientific runtime into this task, or preserve it as a second supported program version.

“Coverage/replacement” is active-code and scientific-authority supersession, not destructive Git-history deletion.

## 3. Live continuity

Expected task-authoring parent:

`1158954fcb3d482a70c5ba45f4a3a311fbefdd91`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` and directly follows the Owner-route roadmap update;
3. verify clean worktree;
4. verify repository identity;
5. verify the CURRENT roadmap contains the three Owner route markers above;
6. verify accepted household source/oracle identities below;
7. stop if unrelated tracked dirty state exists.

## 4. Required context to read

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_STANDALONE_LABEL_ENCODING_CANONICALIZATION_AND_EXPORT_CLOSEOUT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`

Primary numerical authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Accepted household authorities remain frozen.

## 5. Accepted two-asset HA identity

Required standalone oracle path:

`exports/matlab_faithful_two_asset_ha.py`

Required SHA-256:

`276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`

Designated MATLAB household source:

`HANK_2ASSETS_HJB.m`

Required SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

Do not modify the oracle or any already accepted household scientific source.

MP1 may inspect/import module metadata and public symbols but must not execute HJB/KFE/aggregate scientific solves.

## 6. Protected MATLAB source authority — read only

Protected root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Treat this D path as the physical MatlabProgram storage boundary and preserve the project no-overwrite/read-only rules.

At minimum inspect and source-bind:

- `multi_prov_HANK_12sts.m`
- `mpHANK_equilibrium_2000.m`
- `HANK_mp_1eq.m`
- `HANK_mp_1turn.m`
- `HANK_2ASSETS_HJB.m`
- `Lt_seperate.m`
- `HANK_firm.m`
- `wage_caculate.m`
- `load_distdata.m`
- `load_GDPdata.m`

Use the MP0 hashes/report as continuity evidence but re-read the exact source lines required for every MP1 contract. Do not rely on memory when a source formula can be read.

Do not run MATLAB.

## 7. Dissertation consistency boundary

The dissertation is corroborating economic evidence, not a replacement for the MATLAB numerical authority in this task.

Important source-backed conceptual checkpoint to verify where locally available:

- Chapter 5 multi-province household is a **two-asset** household with liquid `b` and illiquid `a`;
- multi-province labor choices are reduced to a composite household wage/labor object before the classical two-asset HJB is solved, then destination-specific labor is reconstructed outside the household HJB;
- the multi-province model does not endogenize 31 separate illiquid asset states.

If the local dissertation source is not available, record that as provenance status only. It does not block MP1 because the required numerical formulas/orientations come from the designated MATLAB sources and accepted HA oracle.

Do not invent a dissertation path.

## 8. Scientific/model execution budget

Exactly zero scientific/model solver calls:

- MATLAB: `0`
- current modular Python HJB: `0`
- current modular Python KFE: `0`
- standalone HA solver: `0`
- standalone KFE/aggregate: `0`
- legacy R5 model: `0`
- steady-state fixed point: `0`
- GE: `0`
- shock/AR1 response: `0`
- transition/dynamics/IRF: `0`

Allowed execution is limited to:

- source parsing/read-only inspection;
- SHA/hash checks;
- imports that do not execute scientific solves;
- static API/schema inspection;
- pure deterministic fixture arithmetic;
- unit tests of contracts/validators/fixture arithmetic;
- lint/type/static tests relevant to changed paths.

## 9. Mandatory province order contract

Freeze the exact 31-province order from the designated data/source route.

Expected MP0 order is:

1. 北京
2. 天津
3. 河北
4. 山西
5. 内蒙古
6. 辽宁
7. 吉林
8. 黑龙江
9. 上海
10. 江苏
11. 浙江
12. 安徽
13. 福建
14. 江西
15. 山东
16. 河南
17. 湖北
18. 湖南
19. 广东
20. 广西
21. 海南
22. 重庆
23. 四川
24. 贵州
25. 云南
26. 西藏
27. 陕西
28. 甘肃
29. 青海
30. 宁夏
31. 新疆

Re-verify from source/data-loading code. If source evidence differs, stop and report; do not silently edit the order.

The contract must fail closed on:

- wrong count;
- duplicate province;
- reordered province list;
- unknown province label;
- shape mismatch for province vectors/matrices.

## 10. Mandatory state/flow/orientation contracts

Freeze with source-line references and tests:

### 10.1 Household outputs

Per origin province, distinguish at minimum:

- `Ct`
- household aggregate `Lt`
- `At`
- `Bt`
- `AtTax`
- household convergence flag/diagnostics required by the outer loop

Do not let household `Lt` silently become final firm labor.

### 10.2 Migration labor orientation

Freeze:

`Lt_mat(j,i)` = labor from origin province `i` allocated to destination province `j`.

Therefore:

- columns = origin;
- rows = destination;
- `Lt_supply(j) = sum_i Lt_mat(j,i)`.

The MP1 asymmetric fixture must make a transpose error visibly fail.

### 10.3 Productive capital

Freeze:

- productive private household capital comes from illiquid `At(i) * N(i)` only;
- `Bt` is liquid and must never be included in productive private capital;
- `At + Bt` is forbidden as productive capital;
- firm capital is source-defined `Kt_supply + GovInv`.

Add an invariant/test proving a synthetic change in `Bt` alone cannot change the MP1 productive-capital allocation expected values.

### 10.4 Cross-province illiquid return

Freeze exact source formula/orientation for `rah` from `HANK_mp_1turn.m`, including:

- `inter_prv_ratio` role;
- home component;
- outside-province component;
- `N_prov-1` normalization;
- issuer-return vs household-return orientation.

Do not replace with a generic `W @ r` formula.

### 10.5 Wage roles

Distinguish:

- firm wage `wjt`;
- household composite wage `w`;
- migration costs / labor-disutility objects;
- destination-specific labor reconstructed by `Lt_seperate`;
- `Lt_supply` consumed by the firm.

Re-read `wage_caculate.m` and `Lt_seperate.m`. Freeze exact matrix orientation and exponents/weights needed for later MP2.

### 10.6 Liquid return and fiscal objects

Freeze roles only, with exact source formulas where used in the one-turn fixture:

- Taylor-derived `rb`;
- `rb_gap` as borrowing spread, not productive return;
- `Tt`, `tau` source roles;
- `Govinc` and national `GovSurplus` as source diagnostics;
- no invented balanced-budget target.

## 11. Household adapter contract — static only

Create a static adapter layer under the current repository. It must bind the multi-province outer state to the accepted two-asset HA API without modifying the accepted HA implementation.

The adapter contract must explicitly answer from live source/API:

1. which multi-province fields are passed into the household solver;
2. which fields are already reduced/composite before the household HJB;
3. whether the accepted current HA API expects scalar/composite wage/labor objects or a vector labor-choice object;
4. exact mapping of `rah -> r_a`, `rb -> r_b`, tax, transfer, borrowing spread, productivity/distribution inputs, and any labor preference object;
5. exact outputs required by the outer model;
6. which outer quantities are reconstructed after the household solve rather than solved inside it.

Do not guess an adapter based on class names alone.

If the accepted HA API and MATLAB outer-call interface cannot be mapped without changing accepted household science, stop `BLOCKED` and report the exact mismatch. Do not edit the oracle.

The adapter may expose dataclasses/protocols/builders and static validation. In MP1 it must not call the scientific solver.

Required invariant:

`NO_LEGACY_R5_RUNTIME_DEPENDENCY`

Static inspection/tests must prove no active MP1 module imports `chapter5_model` from the superseded repository or depends on that repository path.

## 12. Data and cache provenance schemas

Create schemas/manifests for the source-identified external inputs without committing raw data.

Bind at minimum the MP0-identified source identities/statuses:

- `中国各省省会地理距离矩阵.xlsx`
- `2000年后各省数据_填充NA.xlsx`
- `2000年后各省数据.xlsx`
- `R语言估计结果_plm估计.xlsx`
- `数据估计结果_1000_100_0.mat`
- `Multi_Province_12sts_<year>.mat`

Record:

- role;
- expected hash if already source-verified;
- source/cache classification;
- whether raw source or derived cache;
- year-index semantics status;
- Owner-approval requirement;
- no-overwrite/read-only status.

Do not commit any `.xlsx`, `.mat`, private/raw/purchased data, or large output.

The unresolved mapping between source `ii`, dataset row, and `ii+2008` cache filename must remain explicit and fail closed for annual execution. Do not choose a baseline year.

## 13. MP1 deterministic asymmetric one-turn fixture freeze

Create one small, deterministic, source-formula fixture designed only to validate later MP2 outer arithmetic.

Classification must be exactly:

`NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE`

Recommended dimension: `3` synthetic provinces unless exact source formulas require another minimum dimension.

The fixture must be deliberately asymmetric in:

- population `N`;
- pre-frozen household `At`;
- pre-frozen household `Bt`;
- household `Ct`/`Lt` if consumed by source formulas;
- migration/labor allocation inputs;
- firm-return/wage inputs or primitive firm inputs;
- any source-specific allocation/migration coefficients.

Do not use actual province data or claim empirical calibration.

### 13.1 Household outputs are pre-frozen inputs

The fixture must **not call the HA solver**.

Provide pre-frozen household outputs for each synthetic origin province sufficient to drive the outer source formulas.

### 13.2 Expected source-formula objects

Freeze expected intermediate/output values, with source-line provenance, for as many of the following as the exact one-turn source allows without requiring a scientific solve:

- `Lt_mat`;
- `Lt_supply`;
- source capital-contribution matrix/vector;
- `Kt_supply`;
- `rah`;
- firm `Kt`, `Lt`, `Yt`, factor prices/returns and clipping branches where feasible;
- household composite wage update;
- Taylor `rb`;
- province `Govinc` and national `GovSurplus` diagnostic;
- any required `KNratio`/one-turn bookkeeping used by MP3.

If a formula requires a source object not suitable for a non-calibration fixture, explicitly mark that component `DEFER_TO_MP2_SOURCE_FIXTURE` rather than inventing a value.

### 13.3 Fixture independence

The expected values must come from a task-specific source-formula evaluator/hand calculation that is **not** the future production `one_turn.py` implementation.

MP1 must not create the production one-turn function.

The fixture must include at least these negative assertions:

- transposing `Lt_mat` changes expected destination labor and fails;
- using `At+Bt` instead of `At` changes expected capital and fails;
- replacing source `rah` with a generic matrix-average formula fails;
- changing province order fails;
- introducing a legacy R5 import fails.

## 14. Allowed repository changes

Create only bounded MP1 contract/validator/fixture files under the current two-asset repository.

Suggested/allowed paths:

- `src/ch5_two_asset_hank/multi_province/__init__.py`
- `src/ch5_two_asset_hank/multi_province/provenance.py`
- `src/ch5_two_asset_hank/multi_province/province_contracts.py`
- `src/ch5_two_asset_hank/multi_province/household_adapter.py`
- `validators/multi_province/` contract/fixture arithmetic helpers
- `tests/fixtures/multi_province/` small text/JSON/CSV fixtures/manifests
- focused MP1 tests under `tests/`
- required MP1 report under `docs/`

Do not create yet:

- `migration_labor.py`
- `capital_allocation.py`
- `firm.py`
- `wage.py`
- `monetary.py`
- `fiscal_diagnostics.py`
- `one_turn.py`
- `steady_state.py`
- `annual.py`
- shock/dynamic/transition production code

unless a name is used only inside `validators/` for independent fixture arithmetic and cannot be imported as production code.

Do not modify accepted household source/oracle.

Do not modify the historical one-asset repository.

## 15. Tests and checks

Run only tests/checks that do not execute scientific solvers.

At minimum verify:

- oracle SHA exact;
- MATLAB designated source SHA exact;
- province order/count contract;
- matrix/vector shape rejection;
- origin/destination asymmetric orientation;
- `At`/`Bt` separation and Bt-invariance of productive-capital fixture;
- source `rah` orientation/formula fixture;
- household adapter field/schema mapping;
- no hidden economic defaults;
- no legacy R5 runtime import/dependency;
- fixture expected-value reproducibility;
- unknown cache/year authority fails closed;
- no raw/binary data added;
- static import/compile/lint/type checks for changed paths as available.

Do not run the accepted household regression because that would consume a scientific model call outside this task.

## 16. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP1_SOURCE_FAITHFUL_MULTI_PROVINCE_CONTRACTS_ACCEPTED_HA_ADAPTER_AND_DETERMINISTIC_ONE_TURN_FIXTURE_FREEZE_REPORT.md`

Include at minimum:

1. terminal classification;
2. live task/start/final pre-publication SHA;
3. Owner route markers;
4. scientific/model call ledger proving all zeros;
5. protected MATLAB source/hash table used by MP1;
6. accepted current HA source/oracle identities;
7. exact province order and shape contract;
8. household input/output adapter map with source lines and current Python symbols;
9. proof of composite/reconstructed labor role separation;
10. `At`/`Bt` productive-capital invariant;
11. `Lt_mat` orientation;
12. `rah` orientation/formula;
13. wage/firm/Taylor/fiscal role table;
14. data/cache provenance schema and unresolved year/cache items;
15. complete asymmetric fixture specification;
16. expected intermediate/output fixture table;
17. negative-test results;
18. no-legacy-runtime-dependency proof;
19. files written;
20. tests/checks;
21. forbidden-operation check;
22. git closeout;
23. acceptance level;
24. exactly one recommended successor: MP2 only.

## 17. Terminal classifications

PASS:

`MP1_SOURCE_FAITHFUL_CONTRACTS_ADAPTER_AND_ONE_TURN_FIXTURE_FREEZE_PASS`

On PASS freeze:

- `MP1_SOURCE_FAITHFUL_CONTRACTS_ADAPTER_AND_ONE_TURN_FIXTURE_FREEZE_ACCEPTED`
- `MP1_PROVINCE_ORDER_AND_ORIENTATION_CONTRACT_ACCEPTED`
- `MP1_AT_ONLY_PRODUCTIVE_CAPITAL_CONTRACT_ACCEPTED`
- `MP1_ACCEPTED_TWO_ASSET_HA_STATIC_ADAPTER_CONTRACT_ACCEPTED`
- `MP1_NO_LEGACY_R5_RUNTIME_DEPENDENCY_ACCEPTED`
- `MP1_ASYMMETRIC_ONE_TURN_OUTER_FIXTURE_ACCEPTED`

If an implementation-critical source/API ambiguity cannot be frozen without Owner provenance:

`MP1_SOURCE_FAITHFUL_CONTRACTS_ADAPTER_AND_ONE_TURN_FIXTURE_FREEZE_OWNER_PROVENANCE_REQUIRED`

Use this only for a genuine MP1 blocker. Baseline year/cache authority by itself is **not** an MP1 blocker; it belongs to MP4 and must be carried forward.

If source/files/environment prevent controlled completion:

`MP1_SOURCE_FAITHFUL_CONTRACTS_ADAPTER_AND_ONE_TURN_FIXTURE_FREEZE_BLOCKED`

## 18. Repository closeout

On PASS stage only MP1-authorized source/contracts/validators/fixtures/tests/report.

Requirements:

- explicit path staging only;
- no `git add .` or `git add -A`;
- no raw/private/binary data;
- one commit;
- one non-force push;
- GitHub read-back of all changed paths or a complete changed-path manifest;
- `HEAD == origin/main`;
- ahead/behind `0/0`;
- clean worktree.

On non-PASS, restore any unaccepted production-contract code unless the task report justifies retaining a documentation-only blocker artifact; default to report-only publication.

## 19. Explicit prohibitions

Do not:

- run MATLAB;
- run any HJB/KFE/HA solve;
- run GE/fixed point;
- implement `HANK_mp_1turn` production code;
- implement `HANK_mp_1eq`;
- choose an empirical baseline year;
- approve a calibration cache;
- import/maintain the old one-asset R5 runtime;
- use `At+Bt` as productive capital;
- replace source migration/capital formulas with legacy synthetic `W`;
- invent balanced fiscal/goods/NFI/CA closures;
- implement AR1/shocks/dynamics/IRF;
- create Results;
- modify protected MATLAB source;
- modify accepted two-asset household source/oracle;
- delete or rewrite historical Git evidence.

If PASS, recommend only MP2 source-faithful deterministic one-turn implementation on the frozen asymmetric fixture. Do not authorize MP3 or any full 31-province run.
