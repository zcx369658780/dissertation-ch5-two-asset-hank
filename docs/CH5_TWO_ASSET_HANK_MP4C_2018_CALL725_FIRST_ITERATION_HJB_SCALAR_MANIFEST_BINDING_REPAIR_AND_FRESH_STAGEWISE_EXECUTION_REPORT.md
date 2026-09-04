# MP4C 2018 call-725 scalar-manifest binding repair and first-iteration forensic

## Terminal

`MP4C_2018_CALL725_SCALAR_BINDING_REPAIR_AND_FIRST_ITERATION_FORENSIC_BLOCKED__NO_KFE_NO_GE_NO_PRODUCTION_CHANGE`

Classification:

`CALL725_FIRST_ITERATION_FORENSIC_BLOCKED__WRAPPER_POST_CALL_INSTRUMENTATION_FAILURE__NO_PRODUCTION_CHANGE`

The scalar-binding repair and zero-science exact-MAT wrapper certification passed.  The one authorized MATLAB scientific invocation reached its direct solve but failed in post-call residual instrumentation before durable stage persistence.  The task forbids repair/retry after that invocation, so Python and all downstream work were not started.

## Live authority and frozen inputs

- Fresh starting `origin/main` and final task checkout: `9184c1ccb0957764e2a15d34fe2c8df4317bbc4c`; direct parent `8f3baa1a8dda8e02d5cf13ddf41e460c397a3959`.
- Active task blob: `c44f86798964d1c2df7ff50ad44076bbf11447ea`.
- Before execution, `HEAD == origin/main`, ahead/behind was `0/0`, and the tracked worktree was clean.
- Read: repository `AGENTS.md`; the four task-required CURRENT project rules; this task; the parent exact-MAT task/report; initialization-array parity; Python and MATLAB call-725 replay reports; and the accepted propagation-aware HJB parity report.
- The three bound repository blobs, four protected MATLAB hashes, MATLAB replay manifest `87500FF3121ECBBEE1E18A0A574371E06AC2B03B6B24B13465FCFBBF1E02457B`, parent blocked-execution manifest `1A2A72FA19C7E745F9C5C303FDA10A508A5C342887143BAE385F7F4FD6472E29`, and initialization supplemental manifest `817845439CDC77E2C3873AA3D9675E16704E0AB48263F02CFBD653626245D07C` all matched.  The authoritative HJB100 MAT SHA-256 was `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`.

## Phase 0 scalar repair and certification

- The actual historical contract was `call725_matlab_active_input_contract.json`, SHA-256 `02ED3D70AC8217435E7B14122E63F2981FFAB8EF1EDECBA9CDD4EB7317F0DB8E`.  It has `active_inputs`, `phase_a_numerics`, and `grid.switch_matrix`, but no `parameters` or `numerics`; its grid arrays were audited only and did not feed the strict pair.  `historical_scalar_contract_value_map.json` records every consumed value at its exact historical JSON path.
- Missing frozen scalar provenance was read from `hjb100_manifest.json`, SHA-256 `F81A91DD9DED49C01521CEF2EEC02A5B5BC1DA405AAD8206F68FD698B01B16C0`.
- Task-owned `call725_first_iteration_scalar_binding.json` was created with SHA-256 `A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`.  It contains only call provenance, frozen scalar/matrix values, and source paths; it excludes `b`, `ah`, `z`, `v0`, and `l0`.
- Both fresh external wrappers direct-loaded only those five MAT fields.  Their SHA-256 values are `131E1EFA53C260322CC79E30B19B12E18CFD2D8171F97D5345E8EC8510D300FC` (MATLAB) and `63612FBF57A76EF70FF640A7E3AD9D2CE38535F22F324469B407FA8AC43F7B0E` (Python).  Persisted exact diffs classify every change as `SCALAR_BINDING_OR_PERSISTENCE_ONLY`; formula/source-expression normalization passed.
- MATLAB `checkcode`, MATLAB certify-only ingestion, Python certify-only ingestion, exact scalar checks, and canonical MAT hashes passed.  The certification marker was exactly `MP4C_2018_CALL725_SCALAR_MANIFEST_BINDING_REPAIRED_AND_EXACT_MAT_WRAPPER_CERTIFIED__FRESH_FIRST_ITERATION_BUDGET_OPEN`.

## Authorized MATLAB invocation and stop

The MATLAB exact-MAT/common-scalar wrapper was invoked once.  It computed the direct-solve `updated` object, then failed at:

`norm(matrix*updated-rhs,inf)`

`matrix` is `800 x 800`, while `updated` is `(20,20,2)`.  The post-call residual diagnostic omitted the required F-order vectorization, so MATLAB raised a dimension error before the stage artifact could be saved.  This is a wrapper post-call instrumentation/persistence failure, not evidence of a source-formula, scalar-binding, `M`, RHS, or solver-parity defect.

There was no retry and no repair after this failure.  No durable `matlab_stagewise.mat` exists; therefore no stagewise comparison, earliest material scientific divergence, `M`/RHS/V1 parity, backward-error comparison, or Python native-init amplification conclusion is available.

## Call ledger and boundaries

| Category | Count / state |
| --- | --- |
| MATLAB certify-only wrapper | `1` |
| Python certify-only wrapper | `1` |
| MATLAB scientific iteration-1 invocation | `1` |
| MATLAB completed/durably persisted HJB iterations | `0` |
| MATLAB direct solve reached | `1` |
| Python strict-common iteration / native probe | `0 / 0` |
| Retries, KFE, household, GE/stationary/annual, R/PLM, shock/IRF/Results | `0` each |

No production, test, validator, protected MATLAB, parameter, tolerance, solver, controller, grid, or `maxit` source changed.  No KFE, 2018 GE, annual run, shock, or IRF was run.

## Evidence and publication boundary

External no-overwrite evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-first-iteration-scalar-binding-repair-20260904-001`

Its primary audit manifest SHA-256 is:

`3DB3C482F8626A344EDF4D9D6670874DD750DC53A8CB5DAE59E034B46D3B804C`

The authority/source supplement is `001AB7727D3F5BAAD441640E53C86CB45A23F16A46417B94A8A29A693F5D8F0F`; its 28 entries rehashed successfully.  The final value-map supplement is `F0A4E2E43973658D52AA8E207A7B4E28A311902676B289DB848640709A97517D`; its 32 entries rehashed successfully.  The root contains the schema audit, explicit scalar paths/values, scalar manifest/provenance, exact MAT receipts, both wrapper sources and exact diffs, checkcode/certify-only evidence, the MATLAB failure log, immutable Phase 0 and final call ledgers, classification, and audit readback.

Acceptance remains with ChatGPT L3 and Owner.  A new live GitHub task and fresh budget would be required before any repair of the post-call residual serialization, another first-iteration attempt, Python execution, or any scientific/production follow-up.
