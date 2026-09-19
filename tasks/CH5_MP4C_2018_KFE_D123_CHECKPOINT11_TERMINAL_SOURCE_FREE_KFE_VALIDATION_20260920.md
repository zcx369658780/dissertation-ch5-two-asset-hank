# Task — checkpoint-11 terminal source-free topology/KFE validation

Date: 2026-09-20

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_20260920`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live `main` is repository-state authority.

Absolute prohibition:

`zcx369658780/deep-learning-hank`

must never be entered, read, searched, used or modified.

Fresh-fetch live `origin/main`. Read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT10_TO_CHECKPOINT12_BOUNDED_NONLINEAR_CONTINUATION_ACCEPTANCE_20260920.md`
6. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`
7. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_ACCEPTANCE_20260916.md`
9. exact accepted checkpoint-11 evidence.

No new scientific law is authorized.

## Objective

Validate the exact accepted same-value checkpoint-11 generator Q11 as the terminal finite-state Markov generator and obtain, if admissible, its unique normalized nonnegative source-free invariant mass.

This is the terminal household KFE gate for the accepted HJB convergence candidate.

Do not rerun or regenerate the checkpoint-11 policy map, utility map, D2 assembly or Q11. Do not execute any additional HJB update.

## Exact accepted checkpoint 11

- V11: `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F`
- P11: `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3`
- u11: `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648`
- Q11 artifact: `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD`
- Q11 CSR data: `9D489C6A5C8E4A1F705CEC228EDE380FF0A5F51D569CA31DE9BCF9B4BC56537A`
- Q11 CSR indices: `9A1E128BD9B13A6711B20FB992699DB405DEF5450543921ACAB69B57FA5474E6`
- Q11 CSR indptr: `63190CF1D9F4C98D89C81A9990736462F19170B45F97E03AD7B507D492D9C327`
- checkpoint-11 identity: `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B`
- checkpoint arrays: `F620823F15CEB71A168437880AC8655FCBC075D0B7894CBA013780759A8157B2`
- B11: `5.456747553811425e-11`
- D11: `5.4012647243695255e-08`
- D2: PASS
- evidence root:
  `reports/ch5_mp4c_2018_kfe_d123_checkpoint10_to_checkpoint12_bounded_nonlinear_continuation_20260920_run001/`
- sealed manifest:
  `5E67E595B32024213EC5E6517389A7DCA6462A24FB735B06EB2F85D6E1621E41`
- manifest entries: `819`
- manifest bytes: `13,089,592`.

Bind all of these before terminal science. Any mismatch fails closed.

Known non-blocking diagnostic note: the predecessor `identity_change_count=800` is a tuple/list representation artifact. It is not a terminal-KFE input or guard. Do not rerun HJB or remap policies because of it.

## Frozen source-free KFE contract

Reuse the already accepted Q1 terminal/operator validator mathematics unchanged, generalized only from exact Q1 to exact Q11.

State/grid contract:

- `N=800`
- shape `(20,20,2)`
- flattening F order, `b` fastest
- backward generator orientation: rows are origins
- forward operator: `A = Q11.T`
- probability mass vector: `p`
- density view: `g=p/omega`
- `omega=(7/19)*(10/19)=70/361`.

No row replacement, pin equation, RHS/source injection or balancing source.

### Structural/topology stage

1. Load and SHA-bind exact Q11 once.
2. Audit exact CSR shape and finite data.
3. Require nonnegative off-diagonals within the frozen D2 construction semantics.
4. Bind the accepted D2 receipt; do not reassemble Q11.
5. Evaluate `Q11 @ 1` exactly once.
6. Construct the exact-positive off-diagonal directed graph exactly once.
7. Run exactly one SCC decomposition.
8. Require exactly one closed communicating class.
9. Persist the discovered class membership; do not impose the historical Q1 membership as an expected Q11 result.
10. If there is not exactly one closed class, fail closed before SVD.

### Numerical nullspace stage

Form `A=Q11.T` without removing or replacing any row.

Run exactly one full dense:

`scipy.linalg.svd(A, full_matrices=True, lapack_driver="gesvd", check_finite=True)`.

No iterative eigensolver, alternate LAPACK driver, sparse nullspace solver or retry.

Use only the right singular vector associated with the smallest singular value.

Frozen rank rule:

- binary64 epsilon
- `gamma_m = m*eps/(1-m*eps)`
- `tau_rank = gamma_(N+64) * max(1, sigma_max)`.

Require simultaneously:

- numerical rank `799`
- numerical nullity `1`
- exactly one singular value `<=tau_rank`
- second-smallest singular value strictly `>tau_rank`
- structural closed-class count equals numerical nullity.

Any ambiguity fails closed. No threshold tuning.

### Orientation, normalization, stationarity and nonnegativity

Permit only:

- one global sign orientation of the selected null vector;
- one scalar total-mass normalization.

Then persist original normalized signs; do not clip, take absolute values, truncate or renormalize a second time.

Evaluate exactly one `Q11.T @ p`.

Reuse the accepted Q1 formulas exactly:

- `stationarity_scale=max(1, ||Q11.T||inf * ||p||inf)`
- `tau_stationarity=gamma_(N+64)*stationarity_scale`
- normwise backward ratio `=||Q11.T@p||inf/stationarity_scale <= gamma_(N+64)`
- global source bound `=gamma_(N+64)*max(1, N*||Q11.T||inf*||p||inf)`
- probability-mass bound `=gamma_N*max(1,sum(abs(p)))`
- grouped density bound `=gamma_(N+2)*max(1,omega*sum(abs(g)))`
- `tau_nonnegative=gamma_(N+64)*max(1,||p||inf)`
- total negative mass bound `=N*tau_nonnegative`.

Require:

- finite p and g;
- source-free residual within `tau_stationarity`;
- backward ratio within `gamma_(N+64)`;
- `fsum(Q11.T@p)`, `dot(Q11@1,p)` and their discrepancy within the global source bound;
- `math.fsum(p)` normalized to one within the probability-mass bound;
- `omega*math.fsum(g)` normalized to one within the grouped density bound;
- `min(p)>=-tau_nonnegative`;
- total negative mass `<=N*tau_nonnegative`.

No clipping, tolerance fitting, scientific retry or solver substitution.

## Scientific/runtime budget

Maximum terminal science:

- exact Q11 artifact load: 1
- structural/conservation audit: 1
- `Q11 @ 1`: 1
- SCC decomposition: 1
- full dense `gesvd`: 1
- normalized stationary candidate: 1
- `Q11.T @ p`: 1
- HJB solves/updates: 0
- policy maps/selectors/roots: 0
- D2/Q11 assemblies: 0
- checkpoint-12 work: 0
- scientific retries: 0
- solver substitutions: 0
- row-replaced/direct KFE solves: 0
- iterative eigensolver/nullspace solves: 0
- damping/relaxation/adaptive Delta/continuation: 0
- clipping/artificial diffusion/parameter continuation: 0
- MATLAB/production/outer/firm/GE/annual/shock/IRF/welfare/Results: 0
- wall time: <=300 seconds
- resident memory: <=2 GiB.

Ordinary static checks, serialization, hashes, manifest/readback and focused synthetic tests do not consume scientific budget.

## Implementation boundary

Builder may add the minimum checkpoint-11 terminal validation driver/test/report/evidence plumbing needed to reuse the accepted Q1 source-free KFE mathematics.

Do not modify selector, D1/D2/D3 science, convergence law, grid, calibration, checkpoint-11 scientific artifacts or production/source-faithful code.

If a routine representation/serialization issue occurs before science, repair it within task scope and rerun the affected ordinary check. If terminal science has been entered, no scientific retry is available.

## Stop conditions

Stop immediately and fail closed on the first:

- checkpoint-11 identity/provenance mismatch;
- structural/D2-binding failure;
- nonfinite or invalid CSR;
- more or fewer than one closed communicating class;
- SVD warning/failure;
- rank/nullity ambiguity or contract failure;
- graph/numerical nullity disagreement;
- stationarity failure;
- normalization failure;
- nonnegativity failure;
- source-free accounting failure;
- resource ceiling breach.

Do not repair topology, add source mass, pin a row, tune a tolerance, expand the domain or change a boundary law inside this task.

## Deliverables

Create a fresh no-overwrite evidence root and persist at minimum:

- checkpoint-11 binding receipt
- pre-execution scientific-code freeze
- structural/conservation receipt
- SCC receipt
- SVD/rank/nullity receipt
- stationary-mass arrays artifact containing p and g
- stationarity/normalization/nonnegativity/source-free receipt
- exact execution ledger
- terminal receipt
- post-execution code-freeze check
- sealed manifest and independent readback.

Write:

`docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_REPORT.md`.

Terminal PASS marker:

`PASS__CHECKPOINT11_UNIQUE_SOURCE_FREE_INVARIANT_MASS__HOUSEHOLD_HJB_KFE_FIXED_POINT_CANDIDATE`.

A PASS remains a conditional household-block fixed-point candidate under frozen prices/calibration. It does not authorize production replacement, market clearing, GE, annual dynamics, shocks, IRFs, welfare or Results.

Git workflow:

- isolated task branch
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not merge main
- do not modify CURRENT files
- do not publish successor.
