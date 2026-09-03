# CH5_TWO_ASSET_HANK_MP4C_2018_CAPTURED_OPERATOR_FORENSIC_REISSUE_AFTER_RETROSPECTIVE_INTEGRITY_CERTIFICATION

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / read-only numerical-forensic analyst

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`e3f1fdc56c30bc094aa66b997dcadb3147b652c2`

with terminal:

`MP4C_2018_CAPTURED_EVIDENCE_RETROSPECTIVE_MANIFEST_CERTIFIED__CURRENT_RAW_ARTIFACTS_INTERNALLY_CONSISTENT_AND_BOUND_TO_PUBLISHED_EXECUTION_REPORT__CAPTURE_TIME_HASH_GAP_EXPLICIT__READY_FOR_READ_ONLY_FORENSIC_REISSUE`

This task reissues the previously blocked captured-operator forensic after the evidence-integrity gate was repaired by retrospective certification.

The original execution root historically lacked `audit_manifest.json`. That fact remains permanent and must not be rewritten. The accepted replacement identity gate is now:

1. GitHub-published retrospective certification report at `e3f1fdc56c30bc094aa66b997dcadb3147b652c2`;
2. retrospective manifest SHA-256 `D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490`;
3. exact raw-artifact SHA-256 anchors published in that report;
4. explicit provenance classification `RETROSPECTIVE_MANIFEST__NOT_CAPTURE_TIME_HASH_RECORD`.

This replacement gate is sufficient for the bounded read-only forensic below, but it does **not** erase the capture-time-hash gap.

## 2. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `e3f1fdc56c30bc094aa66b997dcadb3147b652c2`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
   - all CURRENT rules;
   - `docs/CH5_TWO_ASSET_HANK_MP4C_2018_FINAL_PRODUCTION_PATH_FAITHFUL_DURABLE_EXECUTION_REPORT.md`;
   - `docs/CH5_TWO_ASSET_HANK_MP4C_2018_CAPTURED_EVIDENCE_RETROSPECTIVE_MANIFEST_AND_INTEGRITY_CERTIFICATION_REPORT.md`;
   - prior blocked forensic task `tasks/CH5_TWO_ASSET_HANK_MP4C_2018_CAPTURED_OPERATOR_NULLSPACE_CONTAMINATED_ROW_AND_HJB_TRAJECTORY_FORENSIC.md`;
   - faithful KFE source and current diagnostic wrapper only as source references.

## 3. Hard boundary

Task type:

`READ_ONLY_CAPTURED_OPERATOR_FORENSIC__NO_MODEL_RERUN__NO_REPAIR`

Forbidden:

- any new 2018 scientific input execution or regeneration;
- stationary / household / HJB / KFE model calls;
- MATLAB or R/PLM execution;
- any new scientific PID;
- any source/model/test modification;
- production contaminated-row changes;
- alternate density solve;
- `spsolve` on counterfactual rows;
- regularization, pseudoinverse, fallback, parameter/grid/controller edits;
- shock/IRF/Results work.

Any helper code must live only in a fresh external analysis root and consume already captured evidence as data.

## 4. Mandatory retrospective identity gate

Primary preserved execution root:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`

Require sidecar:

`retrospective_execution_evidence_manifest.json`

Require exact SHA-256:

`D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490`

Require classification:

`RETROSPECTIVE_MANIFEST__NOT_CAPTURE_TIME_HASH_RECORD`

Require the following current raw-file SHA-256 values exactly:

- `first_singularity_operator_A.npz` = `A17AA9CF512D4D3FDD79235D0D1897CFB20486D2EF5FAA68850910C849AA1B42`;
- `first_singularity_operator_transpose.npz` = `7C1ADEDEE5B26BB30B5A8CC1C9D3D0E83DFF18FAE7860C39986E9E6C2D8FDA66`;
- `first_singularity_contaminated_matrix.npz` = `B04F5A4B99135272FCFF61BEAE220A2C25F5455E478F7994C1394CD6EC869EF4`;
- `first_singularity_rhs.npy` = `C8ADAA98B7B1B7484CAF2A1C4E44D7FD0106D62BCC8FB10084D11CD877CDABFB`;
- `first_singularity_raw_solve_vector.npy` = `F4D51DC00DBAB73F63322A73692EBEA13CAEC2D0A1204A514CBE39329DF8B8E2`;
- `first_singularity_localization.json` = `3628725A54B97344F501C0E44D32338A0B5CF6733D6022B9DD7A4C82C890BD63`;
- `first_singularity_hjb_status.json` = `2B2436E575BB057C9C4BD51F1F6CC5979CBBDACB78D9C9A452BFE90B6181CAF5`;
- `first_singularity_warning_and_traceback.txt` = `45C63691B33BEB75F651DD15F09E725D4B919EB78222DD09812473290B72141D`;
- `household_call_ledger.csv` = `78F1BAFC3664D1ED644293FE98FA384468B23291F9CE8E42400EE0F63BB06A9F`;
- `hjb_return_ledger.csv` = `7D914989AD3CD047FA45CABA5A9209563465BE1799410BB01699F51CF542DA3F`.

The retrospective certification already established A↔A' exact relation, faithful-row contaminated-matrix reconstruction, RHS identity, raw-vector shape/nonfinite count, context/HJB/receipt consistency, and agreement with the published execution report. Reverify hashes before forensic; do not rerun those integrity checks as scientific analysis unless needed to detect drift.

Any hash mismatch or missing mandatory artifact: STOP with forensic blocked.

The final report must explicitly retain this limitation:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`

## 5. Fixed contaminated-row geometry

Independently verify:

`row0 = floor(0.37 * 800) - 1 = 295`.

Map row 295 under Fortran ordering:

`index = b_index + a_index*Nb + z_index*Nb*Na`, `Nb=20`, `Na=20`, `Nz=2`.

Record:

- zero-based and one-based index;
- `(b_index,a_index,z_index)`;
- actual `(b,a,z)` coordinates for b grid `linspace(-2,5,20)`, a grid `linspace(0,10,20)`, z `{0.8,1.3}`;
- membership in closed SCCs under every graph threshold used below.

## 6. Central nullspace geometry

Using captured A transpose only, compute the numerical null direction with at least two independent methods when feasible, e.g. dense SVD and a sparse smallest-singular/eigen method.

For each method report:

- algorithm and scaling;
- rank/nullity tolerance;
- normalization of v;
- `||A'v||` absolute and scale-normalized;
- sign structure;
- min/max/median `|v_i|`;
- `v[295]`;
- `|v[295]|/max|v|`;
- counts and exact indices below relative thresholds `1e-14`, `1e-12`, `1e-10`, `1e-8` of max absolute component.

Then, for captured contaminated matrix B, evaluate:

- `||Bv||` absolute and scale-normalized;
- whether row replacement imposes only `v[295]=0` relative to A'v=0;
- whether the null direction survives the faithful row replacement.

If supported, classify proximal algebraic cause as:

`FIXED_CONTAMINATED_ROW_FAILS_TO_REMOVE_UNIQUE_NULL_DIRECTION__ZERO_OR_NEAR_ZERO_NULL_COMPONENT_AT_SOURCE_ROW`.

Do not yet call this the upstream model cause.

## 7. Row-replacement rank counterfactual — no density solve

Construct temporary in-memory row-replaced copies of captured A transpose for a small deterministic diagnostic set:

- faithful row 295;
- `argmax |v_i|`;
- one high-|v| row inside dominant null-support SCC if identifiable;
- one or two near-zero-|v| rows.

For each, replace the chosen row by the corresponding unit row exactly as the source method does, but perform only:

- numerical rank/nullity;
- smallest singular values;
- condition diagnostics.

Do **not** call `spsolve` and do not calculate any counterfactual density.

Determine whether rows with materially nonzero null component lift numerical rank to 800 while near-zero rows preserve rank 799.

## 8. Conservation / scale analysis

For each A row compute:

- ordinary float64 row sum;
- compensated sum (`math.fsum` or equivalent) from stored coefficients;
- row scale `|diag| + sum|offdiag|`;
- absolute conservation residual;
- relative conservation residual.

Report max/median/quantiles, faithful row, closed-SCC rows, and largest absolute/relative residual rows.

The published absolute maximum `5.209558481541731` must be interpreted relative to operator rates up to about `1.52e8`; do not classify a generator defect from the absolute number alone.

## 9. SCC / nullity reconciliation

Recompute graph topology from captured A using off-diagonal source transitions `i→j iff A_ij > threshold`.

Sweep at least:

- exact positive stored offdiagonals `>0`;
- predecessor threshold;
- `max_positive_rate*1e-14`;
- `max_positive_rate*1e-12`;
- `max_positive_rate*1e-10`, where meaningful.

For each threshold report:

- SCC count;
- closed SCC count/sizes/exact members;
- mapped `(b,a,z)` states;
- faithful-row membership;
- null-vector support/mass on each closed SCC;
- conservation residuals of each closed subblock;
- smallest singular/eigen diagnostics of closed subblocks where feasible.

Reconcile the previously reported 3 closed SCCs with numerical nullity 1 and classify topology as robust, threshold-sensitive, or confounded by nonconservation/near-zero transitions.

## 10. Existing HJB trajectory only

Do not rerun HJB.

From the two captured ledgers reconstruct 安徽 across outer iterations 1–24, reporting:

- global household call;
- HJB converged flag;
- HJB iterations;
- convergence statistic;
- `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap`, `Yt`, `Lt`, `Kt`, `Zt`, `GovInv`.

Also extract outer-24 calls 714–725.

Explicitly answer:

- 安徽 outer23 vs outer24 change;
- whether 安徽 had earlier nonconverged HJB calls whose KFE nevertheless succeeded;
- whether HJB nonconvergence is new at failure or recurrent;
- whether nonconvergence is sufficient proximal explanation, associated only, or neither.

## 11. Causal ladder

The report must separate:

1. proximal algebraic cause of the MatrixRankWarning;
2. structural property of the captured operator;
3. upstream association with HJB nonconvergence.

Allowed strongest classifications include:

- `FIXED_CONTAMINATED_ROW_FAILS_TO_REMOVE_UNIQUE_NULL_DIRECTION__ZERO_OR_NEAR_ZERO_NULL_COMPONENT_AT_SOURCE_ROW`;
- `CAPTURED_OPERATOR_NULLSPACE_SUPPORT_AND_REDUCIBILITY_EXPLAIN_ROW_GAUGE_FAILURE`;
- `HJB_NONCONVERGENCE_ASSOCIATED_WITH_FAILURE_BUT_NOT_SUFFICIENTLY_CAUSAL`;
- `CAPTURED_OPERATOR_CONSERVATION_OR_CONSTRUCTION_PATHOLOGY_REQUIRES_SEPARATE_REPAIR_REVIEW`;
- `ROOT_CAUSE_REMAINS_BOUNDED_AFTER_CAPTURED_OPERATOR_FORENSIC`.

Use multiple classifications only with explicit hierarchy and numerical support.

## 12. Evidence outputs

Fresh preferred root:

`D:\ProjectTemp\ch5-mp4c-2018-captured-operator-nullspace-forensic-reissue-20260903-001`

Persist at minimum:

- `source_evidence_identity.json`;
- `provenance_limitation.json`;
- `contaminated_row_state_mapping.json`;
- `nullspace_geometry.json`;
- `row_replacement_rank_counterfactuals.csv`;
- `conservation_residuals.csv`;
- `conservation_summary.json`;
- `scc_threshold_sweep.json`;
- `closed_scc_support.csv`;
- `anhui_hjb_trajectory.csv`;
- `outer24_local_call_window.csv`;
- `causal_ladder.json`;
- analysis stdout/stderr as applicable;
- fresh analysis-root `audit_manifest.json` hashing the newly created forensic outputs.

The new forensic-root manifest is allowed and must not be confused with the historically absent execution-root capture-time manifest.

## 13. No repair

Even if another row is full rank, do not patch the KFE and do not solve a counterfactual density.

Even if HJB nonconvergence is strongly associated, do not change HJB max iterations, tolerances, or post-loop semantics.

No scientific repair or rerun is authorized in this task.

## 14. Required report and publication

Write:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_CAPTURED_OPERATOR_NULLSPACE_CONTAMINATED_ROW_AND_HJB_TRAJECTORY_FORENSIC_REPORT.md`

The report must include exact numerical evidence, the provenance caveat, and the causal ladder.

On consistent completion, one report-only commit and push is authorized. No production/model/test file may change.

Suggested commit message:

`Diagnose MP4C 2018 captured KFE singularity geometry`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean.

PASS terminal:

`MP4C_2018_CAPTURED_OPERATOR_NULLSPACE_AND_CONTAMINATED_ROW_FORENSIC_COMPLETE__PROXIMAL_CAUSE_CLASSIFIED_OR_BOUNDED__CAPTURE_TIME_HASH_GAP_EXPLICIT__NO_REPAIR_NO_RERUN`

Blocked terminal:

`MP4C_2018_CAPTURED_OPERATOR_FORENSIC_REISSUE_BLOCKED__NO_REPAIR_NO_RERUN`
