# Task — corrected Option-B initial-turn terminal-KFE topology serialization repair and run003 reexecution

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_TERMINAL_KFE_TOPOLOGY_SERIALIZATION_REPAIR_AND_RUN003_REEXECUTION_20260920`

Status: `ACTIVE`

## Governance and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_RUN002_TERMINAL_KFE_TOPOLOGY_SERIALIZATION_EXCEPTION_ACCEPTANCE_20260920.md`
6. run002 report and run002 sealed evidence
7. run001 acceptance/evidence for lineage only
8. predecessor scientific task and all of its direct accepted authorities.

No new economic, HJB, KFE, boundary, KKT, calibration, solver or tolerance law is authorized.

## Objective

Repair exactly two confirmed engineering defects:

1. terminal-KFE topology receipt serialization after the already completed SCC call;
2. exception-path accumulation of already-consumed terminal-KFE call counts.

Prove both repairs with zero-science regression checks, freeze code, then perform exactly one fresh run003 of the same initial-turn scientific objective.

Run003 starts from the same accepted 31-province outer-turn-1 initialization authority. It does not resume from run002's in-memory state.

## Authorized repair A — JSON-safe topology receipt

The scientific topology call remains exactly:

`analyze_exact_positive_topology(Q)`

with the existing exact-positive graph and one SCC decomposition.

The returned in-memory object must continue to drive the existing scientific checks unchanged.

Only persistence representation may change.

Authorized path:

`src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py`

Within terminal KFE only:

- do not write the raw CSR `adjacency` object directly to JSON;
- do not write raw NumPy `labels` directly to JSON;
- create a deterministic JSON-safe topology receipt from the already computed result;
- preserve scientific scalar/list fields such as exact-positive edge count, component count/sizes, closed labels/members, closed-class count, transient-state count and condensation information;
- include deterministic identity evidence for the non-JSON carriers:
  - CSR adjacency identity/hash;
  - integer-label vector hash;
- do not run a second SCC or reconstruct topology independently for persistence;
- do not change `analyze_exact_positive_topology`, its graph rule, SCC call, component/closed-class semantics, or downstream KFE decisions.

The accepted JSON-safe SCC receipt design in `q1_kfe_validation.py` may be used as representational guidance, not as a replacement topology solver.

Do not make a generic serializer that silently coerces arbitrary scientific objects. The repair must be explicit and topology-specific.

## Authorized repair B — exception-path ledger accounting

Authorized path:

`src/ch5_two_asset_hank/corrected_diagnostic/optionb_initial_turn_integration.py`.

The province-local terminal-KFE counters must be accumulated into the run-level scientific ledger even if terminal KFE raises after consuming one or more calls.

Use deterministic `try/finally` or an equivalent fail-closed mechanism around the existing terminal-KFE invocation.

Requirements:

- no duplicate accumulation on success;
- no call counter increment created merely by serialization;
- actual SCC/GESVD/normalized-mass/`Q.T@p` counts reflect consumed calls on both success and exception paths;
- the current terminal-KFE exactly-once scientific contract remains unchanged.

## Focused tests and zero-science gate

Allowed focused test changes:

`tests/test_mp4c_corrected_optionb_initial_turn_integration.py`

and, only if needed for the topology-specific projection helper, one focused corrected-diagnostic test file.

Before any source-native initialization, selector, root, D2/Q, HJB, SCC, SVD or KFE science:

1. regression-test a synthetic topology object containing CSR adjacency and NumPy labels through the JSON-safe projection helper;
2. prove the result is JSON serializable and preserves required scalar/list topology content plus deterministic carrier identities;
3. prove no SCC or SVD is called by the projection test;
4. regression-test terminal-KFE ledger accumulation on a stubbed success path and a stubbed exception-after-counter-increment path;
5. prove no duplicate accumulation on success;
6. rerun the run002 checkpoint-0 diagnostics regression suite;
7. run focused tests, `py_compile`, `git diff --check`;
8. verify authority blobs, 31-row initialization order, run001 and run002 sealed lineage;
9. verify the only pre-science code changes are the explicitly authorized persistence/accounting/test paths;
10. freeze code hashes.

Engineering test retries before science are allowed. They do not authorize model science.

If this zero-science gate fails, stop without model science.

## Scientific contract for the one fresh run003

After the zero-science gate passes, execute one fresh run under exactly the previously accepted scientific laws.

Province order: `0..30`.

For each reached province:

- exactly one source-native V/l initialization;
- exactly 800 scalar labor roots;
- unchanged corrected D1/D2/D3, KKT, boundary, upwind and switching authority;
- fixed `Delta=1000`;
- HJB convergence iff same checkpoint `B<=1e-8 AND D<=1e-7`;
- only `scipy.sparse.linalg.spsolve`;
- direct-solve normwise backward error `<=1e-12`;
- maximum 50 direct HJB updates;
- unchanged exact/approximate period-2/3 cycle law;
- no damping, relaxation, adaptive Delta, clipping, artificial diffusion, continuation, solver substitution or tolerance tuning;
- first scientific failure stops the whole run.

For every converged province, execute terminal KFE exactly once:

- exact-positive graph;
- exactly one SCC decomposition;
- exactly one closed communicating class required;
- `A=Q.T`;
- exactly one full dense `scipy.linalg.svd(..., full_matrices=True, lapack_driver="gesvd", check_finite=True)`;
- frozen rank threshold;
- rank/nullity `799/1`;
- structural closed-class count equals numerical nullity;
- smallest right singular vector only;
- one global sign orientation;
- one total-mass normalization;
- no clipping/abs/truncation/second normalization;
- exactly one `Q.T@p`;
- unchanged stationarity, normalization and arithmetic nonnegativity bounds;
- no pin, row replacement, source RHS, balancing source, iterative eigensolver, alternate SVD driver or KFE retry.

Only after one province's HJB+KFE PASS may its Ct/Lt/At/Bt/total-assets/AtTax be generated.

Only if all 31 household blocks PASS:

- construct exactly one `PreFrozenHouseholdOutputBatch`;
- source-faithful labor only;
- K1A `beta_distance=2`;
- `beta_return=0`;
- fixed accepted theta;
- same-S quantity/payoff accounting;
- C1 `GovInv=max(Ktarget-Kprivate,0)`;
- 31 firm evaluations;
- raw next payoff exactly
  `ra0_turn1_by_destination @ S_destination_origin`.

Do not run turn 2.

## Scientific budget for run003

Maximum for this one fresh run:

### Initialization
- source-native province initializations: 31
- scalar labor roots: 24,800
- initialization retries: 0

### HJB
- direct HJB updates per province: 50
- total direct HJB updates: 1,550
- policy/D2 maps per province: 51
- total policy maps/D2 assemblies: 1,581
- selector evaluations: 1,264,800
- scientific retries: 0
- solver substitutions: 0

### Terminal KFE
- SCC decompositions: 31
- dense GESVD calls: 31
- normalized stationary candidates: 31
- `Q.T@p` calls: 31
- KFE retries: 0

### Integration
- corrected aggregate evaluations: 31
- household batch constructions: 1
- source-faithful labor reconstruction: 1
- K1A allocation: 1
- C1 construction: 1
- firm evaluations: 31
- composite-wage batch: 1
- monetary assignment: 1
- fiscal batch: 1
- raw-next-payoff construction: 1

Forbidden:

- turn-2 household calls: 0
- second outer turn: 0
- K1B: 0
- K2: 0
- adaptive controller: 0
- MATLAB science: 0
- GE/annual/shock/IRF/welfare/Results: 0
- payoff clipping/annualization/rescaling/smoothing/risk-adjustment/z-score repair: 0.

Historical run001 and run002 scientific consumption remains separately preserved. Run003 receives its own one-run ceiling; this does not erase or rename prior consumption.

## Run003 evidence and lineage

Use a fresh root ending in:

`..._20260920_run003`

Never overwrite run001 or run002.

Persist:

- startup/authority binding;
- topology serialization repair contract receipt;
- exception-path ledger repair contract receipt;
- zero-science focused-test receipt;
- run001/run002 cumulative historical-consumption lineage receipt, including run002 actual SCC=1 versus sealed-ledger SCC=0 reconciliation;
- pre/post code freeze;
- 31-state initialization receipt;
- per-province compact HJB history;
- terminal topology/KFE receipts;
- aggregates;
- household batch;
- integration accounting;
- raw-next-payoff same-S receipt;
- next-state candidate;
- exact run003 scientific ledger;
- terminal receipt;
- sealed manifest and independent readback.

Write:

`docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_TERMINAL_KFE_TOPOLOGY_SERIALIZATION_REPAIR_AND_RUN003_REEXECUTION_REPORT.md`.

If successful, terminal marker:

`PASS__TERMINAL_KFE_TOPOLOGY_SERIALIZATION_REPAIR__CORRECTED_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_HJB_KFE_AND_K1A_C1_INTEGRATION__RAW_NEXT_PAYOFF_READY__TURN2_NOT_RUN`

This PASS means exactly one corrected initial multi-province turn is internally closed. It does not establish outer fixed-point convergence, K1B, GE or Results.

## Git workflow

- isolated task branch
- explicit staging only
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish successor.
