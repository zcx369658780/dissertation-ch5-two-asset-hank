# MP4C 2018 diagnostic production-path parity repair and zero-science certification

## Terminal

`MP4C_2018_DIAGNOSTIC_PRODUCTION_PATH_PARITY_CERTIFIED__PHI_ATTAX_AND_BATCH_SEMANTICS_MATCH_PRODUCTION__ZERO_SCIENCE__READY_FOR_ONE_FINAL_DURABLE_2018_REEXECUTION_TASK`

## Authority and scope

- Live task authority: `1ee5ab688895efdc0c5311fa6c726d6f1d86750e`, direct child of `e7f014fd35252f69237c0eb34b84dc9d658ac31b`.
- The sole scientific-code change is in the diagnostic wrapper `validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`; the production worker, HJB, KFE, grid, parameters, controller, migration, firm, wage, fiscal, and Owner-A input route were not changed.
- The only test change is the focused diagnostic test file.
- No frozen 2018 scientific input was read. No scientific child, stationary, household, production HJB, production KFE, MATLAB, R/PLM, shock, or IRF execution occurred.

## Field-by-field source audit

The source-grounded audit is preserved externally as `production_vs_diagnostic_path_audit.csv` and `.md`. It found exact matches for grid construction, `EconomicParams`, HJB numerics, Owner-A state construction, initial phi allocation, `sigmau_destination_origin`, `_source_initial_arrays`, household inputs, post-loop HJB path, aggregate fields, `OnlineStationaryInputs` parameters, threshold, outer-turn cap, `steady_state`, province order, migration wedge, one-turn ordering, and the shared controller.

The HJB/KFE wrappers are `DIAGNOSTIC_ONLY_OBSERVABILITY_DIFFERENCE__STATE_NEUTRAL`: in the normal path they invoke the same faithful exports while retaining the certified ledgers and capture-first fail-closed boundary.

Two `PRODUCTION_PATH_MISMATCH__MUST_REPAIR` findings were confirmed:

1. Production recalculates `prod = Yt/Lt` and mutates destination-row by origin-column `phi` before each household batch; the predecessor diagnostic had retained all ones.
2. Production computes `AtTax` from `a_ss`, `rah`, the faithful illiquid-return helper, density, and KFE cell weight; the predecessor diagnostic had hardcoded zero.

## Repair

The diagnostic now performs the literal production `phi[:]` update at batch entry, before any household call, preserving the matrix object held by `OnlineStationaryInputs`. It now materializes each batch with production-literal `AtTax` and the existing `PreFrozenHouseholdOutputBatch` field order. The helper is exactly `exports.matlab_faithful_two_asset_ha.matlab_faithful_illiquid_return`; no approximation or solver change was introduced.

## Zero-science certification

`python -m py_compile validators/multi_province/mp4c_2018_first_singularity_diagnostic.py tests/test_mp4c_2018_first_singularity_diagnostic.py` passed.

`python -m pytest -q tests/test_mp4c_2018_first_singularity_diagnostic.py` passed: `6 passed, 1 warning`. The warning is the pre-existing intentional dummy `MatrixRankWarning` used only to certify raw capture and is not a production KFE call.

Focused tests establish:

- literal phi equality, destination-row/origin-column orientation, in-place second-turn recomputation, and rejection of all-ones/stale phi;
- nonzero synthetic `AtTax` equality to the production literal expression using the faithful helper;
- complete batch-field equality using injected dummy HJB/KFE/aggregate results;
- pure deterministic one-turn sensitivity: phi changes change migration/composite-wage path and AtTax changes change firm/fiscal `Govinc` path;
- the certified durable-ledger, raw-capture-before-postmortem, and separate postmortem tests remain passing.

## Predecessor reclassification

`2018_SINGULARITY_NOT_REPRODUCED_UNDER_DIAGNOSTIC_PATH_WITH_NONPRODUCTION_PHI_AND_ATTAX_SEMANTICS__NOT_PRODUCTION_PATH_EVIDENCE`

The prior 2,015-call non-reproduction remains historical diagnostic evidence only. It is not a 2018 pass, does not establish 2009–2022 coverage or MATLAB/Python parity, and does not create a Results claim.

## Evidence and next gate

Fresh no-overwrite evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-diagnostic-production-path-parity-zero-science-20260903-001`

It contains the production-path audit, phi/AtTax/batch/instrumentation receipts, compiler and pytest stdout/stderr, the zero-science ledger, and SHA-256 audit manifest.

This task grants no scientific reexecution. A new live GitHub task must explicitly authorize the one final durable 2018 reexecution.
