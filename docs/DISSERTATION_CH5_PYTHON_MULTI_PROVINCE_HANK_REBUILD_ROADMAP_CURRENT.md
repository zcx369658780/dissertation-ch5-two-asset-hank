# CURRENT Python multi-province Chapter 5 HANK rebuild roadmap

Status: `CURRENT`. This document supersedes the 2026-08-22 R5 Python/AR1 route and all stale multi-province status documents that predate accepted MATLAB-faithful two-asset household parity. Historical files remain evidence, not authority.

## Accepted baseline and boundaries

- Numerical authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Frozen household oracle: `exports/matlab_faithful_two_asset_ha.py`, SHA-256 `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.
- Accepted markers: faithful HJB/operator parity, stationary KFE/density parity, stationary distribution parity, household aggregate parity, standalone single-file export acceptance.
- Regression anchors: `C_ss=1.1296890749136979`, `L_ss=0.7341069339182127`, `A_ss=0.44059476682729026`, `B_ss=0.4601208223181049`, `A_ss+B_ss=0.9007155891453952`.
- Current GE state: `MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_OWNER_PROVENANCE_REQUIRED`.
- Historical R5 live identity: `9e73f7189865958fbe38a3cad4547b06b3d17aa3`; evidence-only synthetic two-region one-asset code.
- Repository strategy: extend `dissertation-ch5-two-asset-hank` (strategy B). Do not import old scientific authority. Owner may override to a dedicated successor before MP1.

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
references/legacy_r5/        # manifests/decision records, never imports
```

The adapter passes source-defined household inputs and returns `Ct,Lt,At,Bt,AtTax` plus accepted diagnostics without editing the oracle. Capital allocation consumes `At*N`; `Bt` remains liquid. Firm labor consumes `Lt_supply`.

## Legacy disposition summary

- `KEEP`: no-overwrite IO and bounded CI/type/lint/provenance utilities after path review.
- `ADAPT`: immutable config parsing, hash/manifests, diagnostic containers, limited firm formula shell, generic test patterns.
- `REPLACE`: one-asset HJB/KFE/grids, synthetic `W`, symmetric Brent GE, balanced fiscal/goods/NFI/CA closures, steady-state and transition runners.
- `DEFER`: old AR1 and transition until source/dissertation laws, timing, accounting, and terminal contracts are accepted.

The full file-level matrix is in the companion audit report.

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
- Successor: MP1 only.

### MP1 — province/data contracts and household adapter fixture freeze

- Objective: freeze province order, annual schemas, calibration/cache lineage fields, source orientations, a static accepted-oracle API/hash adapter, and deterministic one-turn fixture inputs/expected outer-block outputs.
- Authority: protected MATLAB sources plus accepted oracle; no old R5 science.
- Targets: `provenance.py`, `province_contracts.py`, `household_adapter.py`, validator fixtures/contracts only.
- Budget: exactly zero scientific/model calls, including standalone oracle calls; only static hash/import/API-schema and fixture-arithmetic checks.
- Diagnostics: byte hashes, province/order/orientation assertions, At/Bt separation, adapter schema, no hidden defaults.
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

### MP5 — shock/AR1 source-law reconciliation

- Objective: decide whether the deterministic MATLAB decay/shock levels, dissertation law, or another approved source controls shocks; adjudicate old AR1 recursion utilities.
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
- Blocker: new source/Owner specification is mandatory; old R5 transition is not authority.

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
| repository strategy | B is recommended; Owner override must occur before MP1 writes implementation paths |

## Reuse versus redo

| Class | Evidence-based range | Contents |
|---|---:|---|
| reusable essentially unchanged | 10-15% | no-overwrite primitives, limited CI/lint/type/hash utilities |
| reusable after adaptation | 10-20% | config/provenance/diagnostic shells, test patterns, limited formula containers |
| scientifically replaced | 35-50% | one-asset HJB/KFE, W allocation, Brent GE, balanced fiscal/goods/NFI/CA |
| new future work | 25-40% | province data contracts, faithful one-turn/manual loop, two-asset dynamics and integration |

Ranges overlap in implementation effort and depend on MP1/MP6 authority; they are planning bands, not measured completion percentages. Overall engineering reuse is approximately 20-30%, while scientific replacement/new work is approximately 70-80%.

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
- legacy R5 only as engineering-pattern evidence.

Proposed allowed paths:

- new contract/validator modules under `src/ch5_two_asset_hank/multi_province/` and `validators/multi_province/`;
- one task-specific report under `docs/`;
- task-specific tests/fixtures under `tests/fixtures/multi_province/`;
- no modification to accepted household source/oracle.

Scientific-call budget: exactly zero for MATLAB, current modular HA, standalone HA, legacy HA/KFE/steady state/transition, AR1/model response, GE, dynamics, and IRF. Only static import/hash/API-schema checks and fixture arithmetic are permitted.

Acceptance outputs: hashed province/order/data schemas; explicit origin/destination and issuer/holder conventions; At/Bt and Lt/Lt_supply invariants; adapter input/output schema; asymmetric hand-check fixture; frozen one-turn expected intermediate objects; provenance manifest; no hidden economic defaults.

Stop boundary: stop after contracts, adapter conformance, and fixture freeze. Do not implement the one-turn production algorithm, solve a fixed point, select a baseline year/cache, implement shocks/dynamics, or create Results.

This task is proposed only. It was not created or executed by MP0.
