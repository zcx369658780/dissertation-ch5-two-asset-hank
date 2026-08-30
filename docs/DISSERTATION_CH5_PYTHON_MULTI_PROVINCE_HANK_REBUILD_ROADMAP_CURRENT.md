# CURRENT Python multi-province Chapter 5 HANK rebuild roadmap

Status: `CURRENT`. This document supersedes the 2026-08-22 R5 Python/AR1 route and all stale multi-province status documents that predate accepted MATLAB-faithful two-asset household parity. Historical files remain evidence, not authority.

## Owner route override — 2026-08-30

The Owner has rejected the prior repository-retention strategy B as a continuing program-version policy and frozen a stronger replacement route:

- `OWNER_SINGLE_ACTIVE_CODEBASE_TWO_ASSET_HANK_ONLY`
- `LEGACY_ONE_ASSET_R5_SUPERSEDED_NO_ACTIVE_PROGRAM_AUTHORITY`
- `ACTIVE_MODEL_REPOSITORY_DISSERTATION_CH5_TWO_ASSET_HANK`

For this Chapter 5 project, the historical one-asset Python R5 implementation cannot represent the source-faithful household structure of the multi-province model and must not remain an active program version. The only active model codebase going forward is:

`zcx369658780/dissertation-ch5-two-asset-hank`

The historical repository:

`zcx369658780/dissertation-ch5-r5-python-model`

is frozen as read-only historical/audit evidence only. It must not receive new scientific features, bug-fix development, model extensions, calibration, transition work, or Results work. No active production module may import it or depend on it.

“Replacement/coverage” means **active-code and scientific-authority supersession**, not destructive rewriting of Git history. Historical commits/reports may remain available for audit. Any reusable engineering idea from the old repository must be independently reviewed and reintroduced under the current two-asset repository; direct retention of the old one-asset scientific runtime is forbidden.

## Accepted baseline and boundaries

- Numerical authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Frozen household oracle: `exports/matlab_faithful_two_asset_ha.py`, SHA-256 `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.
- Accepted markers: faithful HJB/operator parity, stationary KFE/density parity, stationary distribution parity, household aggregate parity, standalone single-file export acceptance.
- Regression anchors: `C_ss=1.1296890749136979`, `L_ss=0.7341069339182127`, `A_ss=0.44059476682729026`, `B_ss=0.4601208223181049`, `A_ss+B_ss=0.9007155891453952`.
- Current GE state: `MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_OWNER_PROVENANCE_REQUIRED`.
- Historical R5 live identity: `9e73f7189865958fbe38a3cad4547b06b3d17aa3`; evidence-only synthetic two-region one-asset code, now explicitly superseded as an active program version.
- Repository strategy: **Owner replacement route**. The current two-asset repository is the sole active model repository. No dedicated successor and no continuing one-asset implementation are planned.

No Results claim follows from these baselines.

## Source-faithful target architecture

Production modules should be separate from validators and historical references:

```text
src/ch5_two_asset_hank/multi_province/
  provenance.py              # immutable source/data/cache identities
  province_contracts.py      # order, annual data, calibration schemas
  household_adapter.py       # frozen oracle-compatible interface only
  migration_labor.py         # Lt_mat origin/destination and Lt_supply
  capital_allocation.py      # productive illiquid At*N; never Bt
  firm.py                    # MATLAB firm block
  wage.py                    # source wage aggregator
  monetary.py                # Taylor rb and declared price objects
  fiscal_diagnostics.py      # diagnostics, not invented balanced closure
  one_turn.py                # faithful HANK_mp_1turn update map
  steady_state.py            # manual HANK_mp_1eq iteration, no root redesign
  annual.py                  # data/cache orchestration
  shocks.py                  # only after source-law freeze
  dynamic_household.py       # future time-dependent two-asset HJB/KFE
  transition.py              # future spatial/fiscal transition integration
  diagnostics.py
  io_contracts.py
validators/multi_province/   # source-extracted fixtures/comparators
```

Historical one-asset source is not part of the active package tree. Audit references stay in GitHub reports and commit history rather than as importable runtime modules.

The adapter passes source-defined household inputs and returns `Ct,Lt,At,Bt,AtTax` plus accepted diagnostics without editing the oracle. Capital allocation consumes `At*N`; `Bt` remains liquid. Firm labor consumes `Lt_supply`.

## Legacy disposition summary under the Owner replacement route

The MP0 `KEEP/ADAPT/REPLACE/DEFER` matrix remains useful only as an **engineering-pattern audit**. It no longer implies that any old R5 executable module will remain as a supported program version.

- `DIRECT_ACTIVE_CODE_REUSE_FROM_LEGACY_ONE_ASSET_R5`: `FORBIDDEN` for scientific/runtime modules.
- `ENGINEERING_PATTERN_REUSE_AFTER_REVIEW`: allowed for no-overwrite IO, hashing, manifests, CI/type/lint patterns, immutable configuration patterns, and generic test structure.
- `SCIENTIFIC_REPLACEMENT_REQUIRED`: one-asset HJB/KFE/grids, synthetic `W`, symmetric Brent GE, balanced fiscal/goods/NFI/CA closures, steady-state and transition runners.
- `DEFERRED_CONCEPTUAL_REFERENCE_ONLY`: old AR1/transition timing concepts until source/dissertation authority is accepted.

No legacy scientific module gains authority by being copied, renamed, or wrapped. Any useful engineering pattern must be reintroduced as new current-repository code with current tests and provenance.

## Structure-first validation policy

**Do not jump from the accepted single-household fixture directly to a full 31-province annual run.**

Required evidence sequence:

1. hand-calculated asymmetric tiny-province fixture to expose origin/destination, issuer/holder, and wage/capital orientation;
2. deterministic one-turn fixture with pre-frozen household outputs, isolating migration, capital, rah, firm, wage, Taylor, and fiscal arithmetic;
3. same-input annual-data snapshot with exact row/province/cache identities at MP4;
4. manual multi-turn update-map parity before any full production solve;
5. an oracle-backed bridge only in a later separately authorized task after static adapter and every outer component pass.

Every fixture is immutable, hashed, source-line bound, and fail-closed on order, shape, category, unit, or provenance mismatch.

## Stage dependency graph

`MP0 -> MP1 -> MP2 -> MP3 -> MP4 -> MP5 -> MP6 -> MP7 -> MP8 -> MP9 -> MP10`

MP5 may audit shock law earlier, but no dynamic implementation begins before MP4 stationary acceptance and MP6 specification freeze.

### MP0 — source/migration audit and roadmap

- Objective: reconstruct MATLAB architecture/dynamic evidence and adjudicate R5 reuse.
- Authority: live task `40274572...` and static sources.
- Budget: all scientific calls zero.
- Acceptance: `MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_ROADMAP_PASS`.
- Owner post-MP0 override: only the current two-asset repository remains an active model codebase.
- Successor: MP1 only.

### MP1 — province/data contracts and household adapter fixture freeze

- Objective: freeze province order, annual schemas, calibration/cache lineage fields, source orientations, a static accepted-oracle API/hash adapter, and deterministic one-turn fixture inputs/expected outer-block outputs.
- Authority: protected MATLAB sources plus accepted oracle; no old R5 science or runtime imports.
- Targets: `provenance.py`, `province_contracts.py`, `household_adapter.py`, validator fixtures/contracts only, all inside the current two-asset repository.
- Budget: exactly zero scientific/model calls, including standalone oracle calls; only static hash/import/API-schema and fixture-arithmetic checks.
- Diagnostics: byte hashes, province/order/orientation assertions, At/Bt separation, adapter schema, no hidden defaults, and proof that no legacy R5 runtime import exists.
- Acceptance: `MP1_SOURCE_FAITHFUL_CONTRACTS_ADAPTER_AND_ONE_TURN_FIXTURE_FREEZE_ACCEPTED`.
- Fixture: a clearly labeled `NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE`, not an annual empirical row. Baseline/cache authority is recorded but not required until MP4.

### MP2 — faithful deterministic one-turn implementation

- Objective: implement `HANK_mp_1turn` equivalent component by component.
- Authority: MATLAB line-bound formulas and MP1 fixtures.
- Targets: migration, capital allocation, firm, wage, monetary, fiscal diagnostics, `one_turn.py`.
- Budget: tiny fixture only; no fixed point/full 31-province annual run.
- Diagnostics: asymmetric orientation, At-only capital, Lt_supply, rah, clipping, Taylor/fiscal values and update order.
- Acceptance: `MP2_SOURCE_FAITHFUL_ONE_TURN_COMPONENT_PARITY_ACCEPTED`.
- Successor: MP3.

### MP3 — manual update-map and fixed-point semantics

- Objective: reproduce `HANK_mp_1eq` ordering, convergence, damping, clipping/veto, Zt/GovInv heuristics, and failure behavior.
- Authority: MATLAB update-map source; never Brent/Newton/fsolve redesign.
- Targets: `steady_state.py` and validators.
- Budget: frozen tiny/synthetic multi-turn fixtures only, explicitly capped.
- Diagnostics: old-state household simultaneity, convergence flags/gaps, bound veto, max-iteration failure.
- Acceptance: `MP3_MANUAL_UPDATE_MAP_AND_CONVERGENCE_PARITY_ACCEPTED`.
- Blocker: Owner vector ordering only if a vector API is proposed.

### MP4 — annual/cache orchestration and 31-province stationary acceptance

- Objective: source-faithful data routing, annual cache behavior, and controlled 31-province stationary validation.
- Authority: accepted MP1-3 plus Owner-approved year/cache/data provenance.
- Targets: `annual.py`, production provenance and run manifests.
- Budget: separately frozen one-shot annual/model budgets; none inherited from earlier stages.
- Diagnostics: data row/calendar year, province order, input hashes, component traces, convergence and cache identity.
- Acceptance: `MP4_MULTI_PROVINCE_STATIONARY_ROUTE_ACCEPTED`.
- Blocking Owner decisions: baseline vs multi-year contract and calibration-cache authority.

#### MP4 execution status — 2026-08-30

- MP1, MP2, and MP3 remain accepted and unchanged.
- MP4A correctly stopped at `YEAR_MAPPING_SOURCE_CONFLICT_BLOCKED`: the protected
  annual wrapper coupled output position, calibration cell, and workbook row.
- Owner/L3 adjudication resolved that blocker by freezing distinct annual identities.
  Calendar 2009 means `analysis_index=1`, `data_MAT_index=1`, explicit workbook
  numeric row `10`, output year `2009`, and regression-vintage key `10`; fixed-2020
  `IND_Zt` remains a numerical initialization anchor rather than a calendar identity.
- MP4A2 prepares a primary-workbook canonical 2009 input, reconciles the cache only
  as a runtime representation, and prepares non-destructive MATLAB/Python parity
  entries. Its model-call budget is zero.
- Reauthorized MP4B established exact MATLAB/Python pre-solver identity, then its
  sole MATLAB top-level invocation stopped before any provincial HJB because the
  validation entry did not bind protected-source global `N_prov=31`. The Python
  scientific call remained unconsumed under the required failure ordering.
- MP4B stationary parity is therefore blocked, not accepted. The next eligible gate
  is a bounded wrapper/source-binding repair review with separately authorized rerun
  budgets. Shocks and the 2010--2023 batch remain closed.
- The source-binding successor proved that `N_prov=31` is the only missing
  computational upper-entry binding and restored it, but its new fail-closed helper
  path check incorrectly treated logical C-junction and resolved physical D paths as
  different roots. The fresh MATLAB call stopped with zero household calls and the
  Python run remained closed. Stationary parity is still not accepted.
- The next path-equivalence successor verified the C junction to the exact D
  target and passed static guard review, but its non-scientific MATLAB smoke
  failed on validation-helper char concatenation before `which` or any model
  call. Presolver and both fresh scientific budgets remained unconsumed.
- The bounded filename-concatenation successor repaired all four active MP4B
  char-plus suffix sites, completed the non-scientific logical/physical smoke,
  and re-established exact presolver equality. Scientific execution remained
  zero and requires a separately published parity authority.
- The fresh scientific MP4B authority established its complete preflight and
  completed one corrected calendar-2009 MATLAB stationary invocation in 184
  outer turns with 5,704 household calls. The authorized Python invocation then
  failed at direct-script bootstrap, before any household or outer-turn call,
  because the validation entry could not import the repository-local `exports`
  package. No repair or rerun occurred. Stationary parity remains blocked; the
  next eligible gate is a bounded Python entry bootstrap repair/static
  direct-invocation proof plus a separately reauthorized Python-only one-shot
  comparison against the preserved MATLAB result. A MATLAB rerun is not needed.
- The Python-only successor repaired the direct-file bootstrap with exact
  current-repository and `src` bindings, passed the direct subprocess smoke with
  zero model calls, and freshly reconfirmed presolver mismatch count zero. Its
  single authorized Python invocation entered outer turn 1 but failed before
  completing the first household: the validation-only initial-labor `brentq`
  evaluated a negative consumption base to a fractional power at the lower
  endpoint and returned NaN. Household completions/calls were `0/0`; no rerun or
  scientific repair occurred. The preserved MATLAB run remains immutable and
  stationary parity remains unaccepted. The next eligible gate is one bounded
  Python initial-labor domain/source-semantics diagnosis and repair authority;
  MATLAB rerun, MP5, and annual batch execution remain closed.

### MP5 — shock/AR1 source-law reconciliation

- Objective: decide whether the deterministic MATLAB decay/shock levels, dissertation law, or another approved source controls shocks; adjudicate old AR1 concepts without retaining the old executable engine as authority.
- Authority: designated dissertation path plus MATLAB source and MP4 stationary baseline.
- Targets: shock specification/validators; no response run.
- Budget: static/audit zero initially; later path generation separately authorized.
- Acceptance: `MP5_SHOCK_LAW_ROLE_AND_RESPONSE_DEFINITION_ACCEPTED`.
- Blockers: dissertation source path and ambiguity of named MATLAB IRF route.

### MP6 — genuine dynamic/transition specification freeze

- Objective: freeze time-dependent two-asset HJB/KFE, timing, terminal conditions, price/wage/return paths, spatial/fiscal accounting, and convergence.
- Authority: Owner-designated primary evidence. Current MATLAB tree has no genuine dynamic solver.
- Targets: contracts only.
- Budget: zero solver calls.
- Acceptance: `MP6_TWO_ASSET_DYNAMIC_TRANSITION_SPECIFICATION_ACCEPTED`.
- Blocker: new source/Owner specification is mandatory; old R5 transition is not authority and will not remain an active program path.

### MP7 — time-dependent two-asset household implementation

- Objective: implement and validate backward HJB/forward KFE against MP6.
- Authority: MP6 plus accepted stationary oracle boundary cases.
- Budget: tiny deterministic grids first; capped calls.
- Diagnostics: terminal/initial conditions, generator orientation, mass, policies, stationary-limit regression.
- Acceptance: `MP7_TWO_ASSET_DYNAMIC_HOUSEHOLD_ACCEPTED`.

### MP8 — multi-province transition integration

- Objective: integrate dynamic household with migration, spatial capital, firm, monetary, fiscal, and timing contracts.
- Authority: MP2-7.
- Budget: tiny-province transition fixtures only before production.
- Diagnostics: stock timing, accounting identities authorized by source, orientation, path convergence.
- Acceptance: `MP8_MULTI_PROVINCE_TRANSITION_INTEGRATION_ACCEPTED`.

### MP9 — conditional transition/IRF numerical validation

- Objective: controlled same-input responses, robustness, horizon/tail sensitivity, and provenance.
- Authority: accepted MP4-8 and MP5 response definition.
- Budget: separately frozen formal-run count; no implicit reruns.
- Diagnostics: shock identity, baseline identity, response normalization, numerical error and robustness.
- Acceptance: `MP9_TRANSITION_IRF_NUMERICAL_VALIDATION_ACCEPTED`.

### MP10 — formal Results eligibility

- Objective: independently review stationary, dynamic, transition, shock, provenance, robustness, and manuscript claim boundaries.
- Authority: all prior accepted evidence plus Owner review.
- Budget: review first; any additional run needs a new task.
- Acceptance: `MP10_FORMAL_RESULTS_ELIGIBILITY_ACCEPTED` or fail closed.

## Owner provenance checkpoints

| Decision | Earliest blocking point |
|---|---|
| baseline year vs multi-year acceptance | MP4; MP1 only needs an explicitly named fixture row |
| calibration cache authority | MP4; MP1 records lineage/status |
| dissertation Chapter 5 primary evidence path | MP5 and MP6 |
| vectorized manual-update ordering | MP3 only if vector API is required |
| interpretation/authority of MATLAB named IRF route | MP5/MP6 |
| repository/program-version strategy | **RESOLVED 2026-08-30**: two-asset repository is the sole active program codebase; legacy one-asset R5 is historical evidence only |

## Reuse versus redo after the Owner replacement decision

The old one-asset repository is no longer counted as a retained executable codebase.

| Class | Planning range | Meaning under the two-asset-only route |
|---|---:|---|
| accepted current two-asset household implementation | 100% retained | faithful stationary HJB/KFE/density/aggregates/oracle already accepted |
| direct active scientific-code reuse from legacy one-asset R5 | 0% | prohibited as an active runtime dependency |
| legacy engineering-pattern reuse | about 20-30% of engineering ideas | IO/no-overwrite, hashing, manifests, CI/type/lint/test patterns, only after current-repo review |
| multi-province scientific outer model to rebuild | substantial | province contracts, migration, At-only capital, wage/rah/firm/fiscal, ordered fixed point, annual orchestration |
| genuine dynamics | new future work | current MATLAB has no source-backed backward-HJB/forward-KFE transition solver |

The earlier MP0 20-30% engineering reuse estimate referred to reusable mechanisms/patterns, not to maintaining the old program as a second supported implementation. There will be only one active program version.

## Results boundary

No paper IRF or Results claim is permitted until the multi-province steady state, dynamic two-asset household, transition/spatial/fiscal accounting, shock provenance/response definition, formal run provenance, and robustness gates are each accepted. A plotted MATLAB `IRF` name or an old R5 conditional response is not Results authority.

## Exactly one proposed next task — design only

Task name: `CH5_TWO_ASSET_HANK_MP1_SOURCE_FAITHFUL_MULTI_PROVINCE_CONTRACTS_ACCEPTED_HA_ADAPTER_AND_DETERMINISTIC_ONE_TURN_FIXTURE_FREEZE`.

Purpose: freeze source-faithful province/data/calibration/orientation contracts, a non-mutating adapter interface to the accepted standalone oracle, and one asymmetric deterministic one-turn outer-logic fixture with pre-frozen household outputs.

Inputs:

- live MP0 report and this roadmap;
- protected MATLAB files/hashes listed in MP0;
- accepted oracle/hash;
- explicitly designated asymmetric synthetic/source-formula province subset with no empirical calibration claim;
- legacy R5 only as historical engineering-pattern evidence; no runtime import or active code dependency.

Proposed allowed paths:

- new contract/validator modules under `src/ch5_two_asset_hank/multi_province/` and `validators/multi_province/`;
- one task-specific report under `docs/`;
- task-specific tests/fixtures under `tests/fixtures/multi_province/`;
- no modification to accepted household source/oracle;
- no modification to the historical one-asset R5 repository.

Scientific-call budget: exactly zero for MATLAB, current modular HA, standalone HA, legacy HA/KFE/steady state/transition, AR1/model response, GE, dynamics, and IRF. Only static import/hash/API-schema checks and fixture arithmetic are permitted.

Acceptance outputs: hashed province/order/data schemas; explicit origin/destination and issuer/holder conventions; At/Bt and Lt/Lt_supply invariants; adapter input/output schema; asymmetric hand-check fixture; frozen one-turn expected intermediate objects; provenance manifest; no hidden economic defaults; explicit proof that the active package has no legacy R5 runtime dependency.

Stop boundary: stop after contracts, adapter conformance, and fixture freeze. Do not implement the one-turn production algorithm, solve a fixed point, select a baseline year/cache, implement shocks/dynamics, or create Results.

This task is proposed only. It was not created or executed by MP0.
