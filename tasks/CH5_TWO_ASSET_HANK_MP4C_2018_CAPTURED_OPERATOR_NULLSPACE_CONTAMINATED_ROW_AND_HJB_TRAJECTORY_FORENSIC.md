# CH5_TWO_ASSET_HANK_MP4C_2018_CAPTURED_OPERATOR_NULLSPACE_CONTAMINATED_ROW_AND_HJB_TRAJECTORY_FORENSIC

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / read-only numerical-forensic analyst

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`01956ca46f117e4faab9f4ff4bba96ecbb780ea3`

with terminal:

`MP4C_2018_FINAL_PRODUCTION_PATH_FAITHFUL_FIRST_SINGULARITY_CAPTURED__POSTMORTEM_CLASSIFIED_OR_BOUNDED__NO_REPAIR_NO_RETRY`

Accepted facts from the published execution report:

- exactly one production-path-faithful 2018 scientific child was run; reruns = 0;
- first singularity occurred at outer iteration 24, household call 725, 安徽, province index 11;
- the failing HJB did not converge: 100 iterations, convergence statistic `0.3038218386543494`;
- KFE entered through the accepted MATLAB-faithful post-loop-after-HJB-nonconvergence path;
- captured operator A is 800×800, nnz 3106, finite;
- captured solve emitted `MatrixRankWarning: Matrix is exactly singular` and the raw solve vector is fully non-finite;
- postmortem reported A transpose rank 799/nullity 1 and contaminated matrix rank 799/nullity 1 at the stated SVD tolerance;
- graph postmortem reported 139 SCCs and 3 closed SCCs of sizes 2, 24 and 4;
- no repair, alternate solver, changed row, rerun, shock or Results work occurred.

The next scientific question is not yet “how to fix 2018”. First determine the exact algebraic reason that the source-faithful contaminated-row KFE matrix remained singular, and separate that proximal cause from any upstream association with the nonconverged HJB operator.

## 2. Task type and hard boundary

Task type:

`READ_ONLY_CAPTURED_OPERATOR_FORENSIC__NO_MODEL_RERUN__NO_REPAIR`

This task authorizes only read-only analysis of already captured evidence plus repository source inspection.

Forbidden:

- reading or regenerating a new 2018 scientific input for execution;
- any stationary/household/HJB/KFE model call;
- MATLAB or R/PLM execution;
- any new scientific PID;
- changing HJB/KFE/model source;
- changing the contaminated row in production;
- solving a new annual steady state;
- regularization, pseudoinverse, fallback, parameter/grid/controller edits;
- shock/IRF/Results work.

No production/model/test source edits are authorized. Any helper code must live only in the external evidence root and must consume captured matrices/CSV/JSON as data.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` and direct child of `01956ca46f117e4faab9f4ff4bba96ecbb780ea3`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, all CURRENT rules, predecessor execution task/report, faithful KFE source, current diagnostic wrapper, and any prior KFE parity reports needed to interpret the captured object.

## 4. Frozen external evidence

Primary captured evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`

Before analysis verify the existing audit manifest and hashes. At minimum verify the published ledger hashes:

- `household_call_ledger.csv` SHA-256 `78F1BAFC3664D1ED644293FE98FA384468B23291F9CE8E42400EE0F63BB06A9F`;
- `hjb_return_ledger.csv` SHA-256 `7D914989AD3CD047FA45CABA5A9209563465BE1799410BB01699F51CF542DA3F`.

Verify raw artifacts exist and match the predecessor audit manifest:

- `first_singularity_operator_A.npz`;
- `first_singularity_operator_transpose.npz`;
- `first_singularity_contaminated_matrix.npz`;
- `first_singularity_rhs.npy`;
- `first_singularity_raw_solve_vector.npy`;
- localization/HJB/warning evidence;
- existing postmortem JSON files.

Hash mismatch or missing raw evidence: STOP.

## 5. Fixed contaminated-row geometry

The faithful source implementation uses:

`row = floor(0.37 * state_count) - 1`.

For state_count = 800, independently verify the zero-based contaminated row index and map it to the frozen Fortran state ordering:

`index = b_index + a_index * Nb + z_index * Nb * Na`, with Nb=20, Na=20, Nz=2.

Record:

- zero-based and one-based row index;
- `(b_index, a_index, z_index)`;
- actual `(b,a,z)` grid coordinates under b∈[-2,5], a∈[0,10], z∈{0.8,1.3}.

Also state whether this row belongs to any closed SCC under each graph threshold used below.

## 6. Nullspace analysis — central gate

Using the captured A transpose only, compute the one-dimensional numerical null direction with at least two independent numerical methods when feasible, e.g. dense SVD plus a sparse smallest-singular/eigen method.

For each method record:

- tolerance/scaling;
- residual `||A' v||` in absolute and scale-normalized form;
- vector normalization convention;
- sign structure;
- min/max/median absolute component;
- component at the faithful contaminated row;
- ratio `|v[row]| / max(|v|)`;
- number and indices of components below multiple explicit relative thresholds such as `1e-14`, `1e-12`, `1e-10`, `1e-8` of max abs component.

Then verify directly the row-replacement geometry:

- let B be the captured contaminated matrix;
- evaluate `||B v||`;
- show whether the only newly imposed equation is effectively `v[row]=0`;
- determine whether the captured null direction survives the faithful row replacement to numerical precision.

If `v[row]` is effectively zero and `B v` remains null-scale, classify this as evidence for a **proximal contaminated-row gauge degeneracy**. Do not yet call it the full upstream scientific cause.

## 7. Diagnostic counterfactual row-rank test — no KFE solve

This section is linear-algebra forensic only. Do not solve for a density and do not feed any counterfactual object into the model.

Construct row-replaced copies of captured A transpose for a small predeclared diagnostic set:

- faithful fixed row;
- index of max `|v_i|`;
- one index with large `|v_i|` inside the dominant null-support SCC if identified;
- one or two indices with near-zero `|v_i|`.

For each, replace the row by the corresponding unit row exactly as the faithful method does, but perform only rank/smallest-singular-value/conditioning diagnostics.

Report whether a row with nonzero null-vector component raises numerical rank from 799 to 800 while near-zero-component rows remain rank 799. This is a diagnostic theorem check, not authorization to change the production row.

Do not call `spsolve` on these alternative matrices.

## 8. Conservation and scale analysis

The predecessor report gives max absolute row-sum residual `5.209558481541731`, while operator rates reach about `1.5e8`. Determine whether this is:

- ordinary floating cancellation relative to enormous rates;
- materially nonconservative rows;
- concentrated in specific states/SCCs.

For each row compute:

- ordinary float64 row sum;
- a compensated/high-precision sum from the stored row coefficients where practical (`math.fsum` or equivalent);
- row scale such as `|diag| + sum(|offdiag|)`;
- relative conservation residual `|row_sum| / row_scale`.

Report max/median/quantiles; faithful contaminated row; states in each closed SCC; and rows with the largest absolute/relative residuals.

Do not infer “generator construction defect” from the absolute 5.2 number alone. Use scale-normalized and compensated evidence.

## 9. SCC / stationary-support reconciliation

The predecessor graph analysis reported 3 closed SCCs while numerical nullity was 1. Reconcile these facts rather than treating them as automatically consistent.

Recompute SCC/closed-class structure under a threshold sweep tied to operator scale, including at least:

- exact positive stored off-diagonals (`>0`);
- predecessor threshold;
- relative thresholds such as `max_rate * 1e-14`, `1e-12`, `1e-10` where numerically meaningful.

For each closed SCC report:

- member indices and mapped `(b,a,z)` states;
- whether faithful contaminated row is inside;
- total/relative null-vector mass on the SCC;
- subblock conservation residuals;
- whether the subblock itself has a near-zero eigen/singular direction.

Determine whether “3 closed SCCs” is robust topology, threshold-sensitive topology, or partly an artifact of nonconservative/near-zero transitions.

## 10. HJB trajectory evidence from existing ledgers only

Do not rerun HJB.

From `hjb_return_ledger.csv` and `household_call_ledger.csv`, reconstruct 安徽’s trajectory across outer iterations 1–24 and the immediate same-turn neighborhood around call 725.

At minimum report for 安徽 by outer iteration:

- global call number;
- HJB converged flag;
- HJB iterations;
- convergence statistic;
- `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap`, `Yt`, `Lt`, `Kt`, `Zt`, `GovInv`.

Explicitly compare:

- 安徽 at outer 23 vs outer 24;
- calls 714–725 in outer 24;
- whether prior 安徽 nonconverged HJB calls, if any, nevertheless passed KFE;
- whether HJB nonconvergence is new at the failure or recurrent.

This determines whether `HJB_NONCONVERGED_POSTLOOP_OPERATOR` is a sufficient proximal explanation, only an association, or neither.

## 11. Required causal ladder

The report must distinguish three levels:

1. **Proximal algebraic cause of MatrixRankWarning** — why the captured contaminated matrix is rank deficient.
2. **Structural property of the captured operator** — null support, reducibility/topology, conservation/scale, etc.
3. **Upstream model-solver association** — whether HJB nonconvergence plausibly generated or intensified that structure.

Do not collapse levels 1–3 into one claim without evidence.

Allowed strongest classifications include:

- `FIXED_CONTAMINATED_ROW_FAILS_TO_REMOVE_UNIQUE_NULL_DIRECTION__ZERO_OR_NEAR_ZERO_NULL_COMPONENT_AT_SOURCE_ROW`;
- `CAPTURED_OPERATOR_NULLSPACE_SUPPORT_AND_REDUCIBILITY_EXPLAIN_ROW_GAUGE_FAILURE`;
- `HJB_NONCONVERGENCE_ASSOCIATED_WITH_FAILURE_BUT_NOT_SUFFICIENTLY_CAUSAL`;
- `CAPTURED_OPERATOR_CONSERVATION_OR_CONSTRUCTION_PATHOLOGY_REQUIRES_SEPARATE_REPAIR_REVIEW`;
- `ROOT_CAUSE_REMAINS_BOUNDED_AFTER_CAPTURED_OPERATOR_FORENSIC`.

Multiple compatible classifications may be reported with explicit hierarchy.

## 12. No repair decision in this task

Even if the forensic shows that another row would be full-rank, do not patch the KFE row and do not run a counterfactual density solve.

Even if HJB nonconvergence looks upstream, do not increase HJB max iterations or change the post-loop contract.

The next repair task, if any, will require L3/Owner scientific review of the evidence generated here.

## 13. Evidence outputs

Create a fresh analysis root, preferred:

`D:\ProjectTemp\ch5-mp4c-2018-captured-operator-nullspace-forensic-20260903-001`

Persist at minimum:

- `source_evidence_identity.json`;
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
- analysis stdout/stderr if applicable;
- SHA-256 audit manifest.

## 14. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_CAPTURED_OPERATOR_NULLSPACE_CONTAMINATED_ROW_AND_HJB_TRAJECTORY_FORENSIC_REPORT.md`

The report must include exact numerical evidence and the strongest supported causal ladder. It must not contain a repair implementation or Results claim.

## 15. Publication authority and terminal

If analysis completes consistently, one report-only commit and push is authorized. No production/model/test file may be changed.

Suggested commit message:

`Diagnose MP4C 2018 captured KFE singularity geometry`

After push: fresh-fetch and require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean.

PASS terminal:

`MP4C_2018_CAPTURED_OPERATOR_NULLSPACE_AND_CONTAMINATED_ROW_FORENSIC_COMPLETE__PROXIMAL_CAUSE_CLASSIFIED_OR_BOUNDED__NO_REPAIR_NO_RERUN`

If evidence identities fail or required analysis cannot be completed without a new scientific run:

`MP4C_2018_CAPTURED_OPERATOR_FORENSIC_BLOCKED__NO_REPAIR_NO_RERUN`