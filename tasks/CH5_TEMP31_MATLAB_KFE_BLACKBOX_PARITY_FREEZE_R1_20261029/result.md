# TEMP31 MATLAB KFE parity / version-freeze candidate

TASK_ID=CH5_TEMP31_MATLAB_KFE_BLACKBOX_PARITY_FREEZE_R1_20261029
Candidate=codex/ch5-temp31-kfe-matlab-blackbox-freeze-r1-20261029
Fixed parent=56447829ce0e6c3c85552c53c351b26a2452a4bd
Decision=KFE_SOURCE_MATCH_NO_CODE_CHANGE
Scientific implementation edits=0; new validator=1; KFE-only replays=4/4.

Core and export KFE result type, row-index helper and solve function have identical ASTs ignoring source locations. Transpose, pin index, unit row, rhs .007, linear solve, db*da normalization and Fortran reshape match the frozen MATLAB excerpt on the authenticated 800-state archives. Both existing source files retain their original bytes and Blobs. No parity defect requiring a patch was proved.

| Point | raw/density max difference | normalization difference | original residual | non-pin residual | raw pinned-system residual | strict certified |
|---|---:|---:|---:|---:|---:|---|
| P0 | 0 | 0 | 4.686593832556138 | 1.6518372191536135e-15 | 2.8456122435781354e-17 | FALSE |
| P2 | 0 | 0 | 0.32557163336740258 | 1.0148132334464322e-16 | 1.3064636178450328e-17 | FALSE |
| P4 | 0 | 0 | 3.7634433046985296 | 9.4368957093138306e-16 | 1.4619788669609224e-17 | FALSE |
| P5 | 0 | 0 | 3.4077708099368875 | 1.5569143196891844e-15 | 1.9827347229328662e-17 | FALSE |

All four raw vectors and density arrays are exactly equal to their prior archives (also equal hashes); normalization and all 20 a/b marginal bins and At/Bt match within the frozen 1e-12 comparison tolerance. The independent dense pinned-matrix construction differs by zero. Each point used exactly one real frozen core solve and one SciPy spsolve, with 30s timeout and 1GiB committed-memory limit enforced before imports. All returned normally without retry.

MATLAB_KFE_METHOD_EXECUTED=TRUE for four points.
ORIGINAL_STATIONARITY_DIAGNOSTIC=STATIONARITY_WARNING for four points.
STRICT_ECONOMIC_STATIONARITY_CERTIFIED=FALSE for four points.
Compatibility label=SOURCE_KFE_COMPUTED_WITH_STATIONARITY_WARNING; contract alias=SOURCE_METHOD_COMPUTED_WITH_STATIONARITY_WARNING.
Old KFE_NOT_CERTIFIED reports remain byte-identical. This new explanation does not revise old independent reviews or activate any outer workflow.

The original residual maximum occurs at zero-based row295 (MATLAB296) in all four actual archives; outside it, residuals are near machine precision. Replacing a row removes that original equation. Solving the pinned system therefore does not establish the removed stationarity equation. Post row-sum loss and boundary mass remain disclosed, without clipping, diagonal adjustment, alternative solver or source changes.

MATLAB_RAW_LOCAL_VERIFICATION=NOT_AVAILABLE. MATLAB runtime execution=NOT_RUN. Comparison uses only contract/Owner frozen excerpts. Full post-operator spdiags, boundary and end-to-end HJB parity remain BOUNDED/BLOCKED; this is not formal global source freeze or certified economic steady state.

source_identity.json records the preparation snapshot (its NO_KFE_REPLAY_YET label is as-of preparation); budget.json and four point receipts record the later actual execution. Final Git identities are recorded by the payload/seal receipts to avoid self-reference.

P3=BLOCKED; V010=UNCHANGED; V011=NOT_STARTED; Results=FALSE; FORMAL_SOURCE_FREEZE=FALSE; model_activation=FALSE; REAL_GE=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED.
Terminal after delivery: STOP__AWAITING_GPT_INDEPENDENT_ABC.
