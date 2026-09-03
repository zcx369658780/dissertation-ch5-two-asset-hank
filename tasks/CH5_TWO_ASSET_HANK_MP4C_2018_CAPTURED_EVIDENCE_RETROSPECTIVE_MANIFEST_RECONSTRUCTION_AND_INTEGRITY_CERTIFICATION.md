# CH5_TWO_ASSET_HANK_MP4C_2018_CAPTURED_EVIDENCE_RETROSPECTIVE_MANIFEST_RECONSTRUCTION_AND_INTEGRITY_CERTIFICATION

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / evidence-integrity certifier

Owner: final scientific authority

## 1. Authority basis

Immediate live predecessor authority:

`aa6a1534873fb4cd90d2c783c10607752d5530fa`

The prior read-only forensic task stopped before analysis with terminal:

`MP4C_2018_CAPTURED_OPERATOR_FORENSIC_BLOCKED__NO_REPAIR_NO_RERUN`

because the preserved execution evidence root did not contain the `audit_manifest.json` that the forensic task required as a capture-time identity gate.

Accepted facts from that blocked attempt:

- live authority and direct-parent continuity were valid;
- published ledger hashes matched exactly;
- no forensic linear algebra was run;
- no HJB/KFE/stationary/model/MATLAB/R execution occurred;
- no new scientific PID, repair, rerun, helper analysis root, repository edit or commit occurred.

The published execution report at `01956ca46f117e4faab9f4ff4bba96ecbb780ea3` already anchors two ledger hashes and multiple exact structural facts about the captured singularity, but it did not publish raw-artifact hashes. Therefore this task authorizes a **retrospective evidence-integrity certification**, not a fictitious reconstruction of a capture-time manifest.

## 2. Hard provenance rule

Do **not** create or describe any new file as an original/capture-time manifest.

The original execution root lacked `audit_manifest.json`; that historical fact must remain explicit.

Allowed new manifest name:

`retrospective_execution_evidence_manifest.json`

Classification must explicitly state:

`RETROSPECTIVE_MANIFEST__NOT_CAPTURE_TIME_HASH_RECORD`

This task may certify the current preserved raw artifacts by:

1. hashing them now;
2. binding them to the already published ledger hashes and execution report facts;
3. proving exact internal relations among A, A transpose, contaminated matrix, RHS, raw solve, localization, HJB status and receipts.

It must **not** claim cryptographic proof that unanchored raw files were unchanged during the interval between the original capture and this retrospective certification.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `aa6a1534873fb4cd90d2c783c10607752d5530fa`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read `AGENTS.md`, all CURRENT rules, the final 2018 execution task/report, and the blocked forensic task.

## 4. Hard no-science boundary

This is evidence-governance work only.

Forbidden:

- frozen-input execution or regeneration;
- stationary/household/HJB/KFE model calls;
- MATLAB;
- R/PLM;
- any new scientific PID;
- new postmortem/root-cause analysis beyond the exact integrity checks below;
- new SVD/nullspace/SCC/conservation forensic;
- any model/source/test changes;
- any repair, rerun, shock, IRF or Results work.

Helper scripts are allowed only in a fresh external certification root and may only load/hash/compare existing evidence files.

## 5. Preserved execution root

Primary root:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`

Do not overwrite, rename, normalize or rewrite any existing file in that root.

The only optional addition allowed inside the original root is the new no-overwrite sidecar:

`retrospective_execution_evidence_manifest.json`

Prefer generating the manifest first in the fresh certification root, validating it, then writing the identical sidecar bytes into the original root only after PASS.

## 6. Published anchors that must match

From the repository-published execution report:

- `household_call_ledger.csv` SHA-256:
  `78F1BAFC3664D1ED644293FE98FA384468B23291F9CE8E42400EE0F63BB06A9F`;
- `hjb_return_ledger.csv` SHA-256:
  `7D914989AD3CD047FA45CABA5A9209563465BE1799410BB01699F51CF542DA3F`;
- household rows = 725;
- HJB-return rows = 725;
- first capture = outer iteration 24 / global call 725 / 安徽 / province index 11;
- HJB converged = false;
- HJB iterations = 100;
- HJB convergence statistic = `0.3038218386543494`;
- KFE path = `MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE`;
- warning = `MatrixRankWarning: Matrix is exactly singular`;
- raw solve vector has 800 non-finite entries;
- A shape = 800x800;
- A nnz = 3106;
- stored A data finite = true;
- published postmortem A-transpose rank/nullity = 799/1;
- published postmortem contaminated rank/nullity = 799/1;
- published SCC count = 139;
- published closed SCC count = 3, sizes 2,24,4.

Any contradiction with a published anchor: FAIL and STOP.

## 7. Mandatory file inventory and hashes

Inventory every regular file already present in the preserved execution root before creating any sidecar.

For every file record:

- relative path;
- bytes;
- SHA-256;
- extension/type label;
- read timestamp for this certification only.

At minimum the manifest must bind:

- `household_call_ledger.csv`;
- `hjb_return_ledger.csv`;
- `first_singularity_operator_A.npz`;
- `first_singularity_operator_transpose.npz`;
- `first_singularity_contaminated_matrix.npz`;
- `first_singularity_rhs.npy`;
- `first_singularity_raw_solve_vector.npy`;
- `first_singularity_localization.json`;
- `first_singularity_hjb_status.json`;
- `first_singularity_warning_and_traceback.txt`;
- `diagnostic_execution_receipt.json`;
- `diagnostic_child_terminal_sentinel.json`;
- `zero_or_bounded_science_ledger.json`;
- launch/preflight/input/code-identity receipts if present;
- existing postmortem JSON files.

Missing mandatory raw file: FAIL.

## 8. Exact raw-object internal-consistency certification

These checks are identity/integrity checks, not scientific forensic.

### A and transpose

Load captured A and captured A-transpose as sparse matrices.

Require:

- both are 800x800;
- A nnz = 3106;
- finite stored values;
- after canonical CSR normalization, captured transpose is exactly equal to `A.transpose()` in shape, sparsity indices and binary64 data values.

### Faithful contaminated matrix

Independently derive the faithful zero-based row:

`floor(0.37 * 800) - 1 = 295`.

From captured A-transpose, reconstruct a temporary matrix in memory only by:

- clear row 295;
- set `(295,295)=1.0`.

Require the reconstructed matrix to equal the captured contaminated matrix after canonical sparse normalization.

Do not write this temporary matrix back to the preserved root.

### RHS

Require captured RHS:

- shape `(800,)`;
- finite;
- exactly one nonzero;
- nonzero index = 295;
- value = exactly the stored binary64 representation of `0.007` used by the source path.

### Raw solve

Require:

- shape `(800,)`;
- non-finite count = 800, matching the published report.

Do not attempt another solve.

## 9. Context / HJB / warning / receipts consistency

Require localization and HJB files to agree with the published report and the final rows of the two ledgers:

- outer iteration 24;
- global call 725;
- 安徽;
- province index 11;
- HJB false / 100 / `0.3038218386543494`;
- post-loop nonconvergence KFE classification.

Require warning evidence to contain the captured exact-singularity warning.

Require terminal sentinel / execution receipt / bounded-science ledger to agree on:

- one diagnostic/scientific run;
- one child / one worker / one subprocess where those fields exist;
- reruns = 0;
- household calls = 725;
- first capture = true;
- terminal = fail-closed first-singularity capture;
- no normal-completion summary.

If launch/input/code-identity receipts are present, compare them against the published report's PID/input/code identities. Report any absent optional receipt separately; do not invent it.

## 10. Existing postmortem-file consistency

Do not rerun postmortem in this task.

Read the existing postmortem JSON files only and require their stored values to agree with the published report for:

- A shape/nnz/finite flag;
- max row-sum residual `5.209558481541731`;
- SCC count 139;
- closed SCC count 3 and sizes 2,24,4;
- transpose rank/nullity 799/1;
- contaminated rank/nullity 799/1;
- SVD tolerance `3.821460885301736e-05`.

This check certifies report-to-file consistency only. It is not a new numerical forensic computation.

## 11. Retrospective manifest schema

Write in the fresh certification root:

`retrospective_execution_evidence_manifest.json`

At minimum include:

- schema/version;
- classification exactly `RETROSPECTIVE_MANIFEST__NOT_CAPTURE_TIME_HASH_RECORD`;
- preserved execution-root path;
- final execution report Git commit `01956ca46f117e4faab9f4ff4bba96ecbb780ea3` and report blob `f708b6b854ed7838ebd2c005bcb60cb6ec42f5e3`;
- current certification task authority;
- complete pre-sidecar file inventory with SHA-256/bytes;
- published-anchor verification results;
- A/transpose exact-relation result;
- contaminated-matrix exact-reconstruction result;
- RHS exact-contract result;
- raw-vector nonfinite-count result;
- context/HJB/receipt consistency results;
- existing-postmortem consistency results;
- explicit provenance limitation statement.

After validating the manifest, compute its SHA-256.

If all checks PASS, write identical no-overwrite bytes as:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001\retrospective_execution_evidence_manifest.json`

Then read it back byte-for-byte and verify the SHA.

Do not create a file named `audit_manifest.json` in the original root.

## 12. Fresh certification root

Use:

`D:\ProjectTemp\ch5-mp4c-2018-retrospective-evidence-integrity-certification-20260903-001`

Fresh no-overwrite only.

Persist at minimum:

- pre-sidecar file inventory CSV/JSON;
- published-anchor verification receipt;
- raw-object relation verification receipt;
- report/postmortem consistency receipt;
- provenance-limitations receipt;
- `retrospective_execution_evidence_manifest.json`;
- manifest SHA receipt;
- helper stdout/stderr if applicable.

## 13. Acceptance classification

PASS only if all mandatory files exist and all published anchors/internal exact relations agree.

PASS terminal:

`MP4C_2018_CAPTURED_EVIDENCE_RETROSPECTIVE_MANIFEST_CERTIFIED__CURRENT_RAW_ARTIFACTS_INTERNALLY_CONSISTENT_AND_BOUND_TO_PUBLISHED_EXECUTION_REPORT__CAPTURE_TIME_HASH_GAP_EXPLICIT__READY_FOR_READ_ONLY_FORENSIC_REISSUE`

FAIL terminal:

`MP4C_2018_CAPTURED_EVIDENCE_INTEGRITY_CERTIFICATION_FAILED__FORENSIC_REMAINS_BLOCKED__NO_REPAIR_NO_RERUN`

The PASS classification means the current preserved evidence is sufficiently identity-bound for a subsequent read-only forensic task under an explicit retrospective-provenance caveat. It does **not** retroactively create capture-time cryptographic proof.

## 14. Repository report and publication

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_CAPTURED_EVIDENCE_RETROSPECTIVE_MANIFEST_AND_INTEGRITY_CERTIFICATION_REPORT.md`

The report must publish the SHA-256 values of the five raw numerical artifacts plus localization/HJB/warning files and the retrospective manifest itself, so future forensic work can verify them against GitHub-published anchors.

If PASS, one report-only commit + push is authorized. Do not commit external raw artifacts or helper scripts.

Suggested commit message:

`Certify MP4C 2018 captured evidence retrospectively`

After push, fresh-fetch and require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean.

If FAIL, report-only publication of the strongest accurate failure classification is allowed; no forensic or repair continuation is authorized.