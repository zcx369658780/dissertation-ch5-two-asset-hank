# Task — K1A raw-ra0 corrected-household fixed-price three-point safety panel

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_K1A_RAW_RA0_CORRECTED_HOUSEHOLD_FIXED_PRICE_THREE_POINT_SAFETY_PANEL_20260920`

Status: `ACTIVE`

## Governance and startup

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition:

`zcx369658780/deep-learning-hank`

must never be entered, read, searched, used or modified.

Fresh-fetch `origin/main`, then read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1A_RAW_RA0_PAYOFF_OWNER_ADOPTION_20260920.md`
6. `docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_ACCEPTANCE.md`
7. `docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_ACCEPTANCE_20260920.md`
8. `docs/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_ACCEPTANCE_20260920.md`
9. exact accepted checkpoint-11 HJB evidence
10. accepted K1A payoff-return evidence file:
   `docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/static_no_feedback_payoff_counterfactual.csv`.

No new economic law is authorized.

## Objective

Test whether the newly Owner-adopted raw-`ra0` payoff levels can enter the **corrected household HJB law** without immediate selector, D2-generator or direct-linear-solve failure.

This is deliberately a fixed-price, fixed-calibration, one-step stress panel. It is not a convergence experiment and not a multi-province outer-loop experiment.

Only `r_a` changes relative to the accepted checkpoint-11 household object.

## Owner-adopted payoff authority

Use raw completed-iteration payoff levels with:

- no `.02/.09` clipping;
- no annualization;
- no rescaling;
- no smoothing;
- no risk adjustment;
- no z-score transformation of payoff levels.

K1B attractiveness is outside this task.

## Exact three-point preregistered panel

The panel is taken from the accepted **Path B geographic beta=2** static same-S raw-payoff counterfactual and is frozen before execution.

Execute in ascending payoff order:

1. `LOW`
   - accepted source row: turn 5, Qinghai
   - raw portfolio payoff `r_a = 0.11048158315647279`

2. `MEDIAN`
   - accepted source row: turn 12, Hunan
   - raw portfolio payoff `r_a = 0.26259451366691877`
   - this is the exact 775-observation Path-B median

3. `HIGH`
   - accepted source row: turn 4, Beijing
   - raw portfolio payoff `r_a = 1.037811238406538`

Builder must independently recompute these min/median/max identities from the accepted CSV before any scientific call. Any mismatch fails closed.

Do not substitute destination firm `ra0` for these portfolio-weighted `S'ra0` household payoff values.

## Exact fixed household authority

For every panel point, reuse the accepted checkpoint-11 object as the common starting value:

- V11 `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F`
- accepted grid shape `(20,20,2)`, F-order, b fastest
- accepted productivity generator
- D1/D2/D3
- all accepted KKT/boundary/switching laws
- lower-a zero-kink law
- interior-liquid Z law
- one-axis interior-a switching
- simultaneous two-axis switching
- repaired lower-b negative branch representation.

Freeze every non-payoff scalar to the accepted checkpoint-11 values:

- `r_b=0.02`
- borrowing-rate gap `0.07`
- `tau=0.05`
- wage `16.82014806560587`
- transfer income `0.1`
- `rho=0.05`
- `gamma_c=2`
- `phi=5`
- `chi_0=0.1`
- `chi_1=2`
- `a_bar=1e-6`
- labor weight `1`
- `Delta=1000`.

The existing state-dependent taper remains:

`effective_r_a(a) = r_a * (1 - 0.1*(a/10)^9)`.

Do not modify the taper.

## Scientific execution for each panel point

Use a fresh no-overwrite subdirectory per point.

For each reached point, in the preregistered order:

1. bind exact accepted V11/grid/scalars and the exact panel `r_a`;
2. derive the V11 derivative fields under unchanged finite-difference/boundary law;
3. execute exactly one complete corrected 800-cell policy map;
4. stop on first selector failure; do not repair scientific logic;
5. after all 800 cells pass, assemble exactly one D2 conservative Q;
6. require all unchanged D2 structural/conservation checks to pass;
7. compute the same-value Bellman residual at V11 under the panel `r_a`:
   `B_seed = ||rho*V11 - u(r_a,V11) - Q(r_a,V11)V11||inf`;
8. execute exactly one frozen direct implicit HJB update:
   `[(rho+1/Delta)I-Q] V_plus = u + V11/Delta`;
9. use only `scipy.sparse.linalg.spsolve`;
10. require finite shape/order and normwise backward error `<=1e-12`;
11. compute `D_step = ||vec_F(V_plus-V11)||inf`;
12. persist policy/switching/operator diagnostics and exact call ledger;
13. move to the next higher panel point only if the current point passes every required one-step safety gate.

`B_seed` and `D_step` are diagnostics only. They must **not** be classified using the frozen HJB convergence rule because V11 is not the previous iterate generated under the new raw payoff.

No second update is authorized at any panel point.

## Panel comparison

After all three pass, provide a compact comparison across LOW/MEDIAN/HIGH:

- B_seed
- D_step
- direct-solve backward error
- selected policy canonical identity
- identity-change count relative to accepted P11 using serialization-normalized comparison
- active-constraint counts
- transfer-branch counts
- interior-a / liquid-Z / joint-switching counts
- Q nnz
- Q row-sum conservation
- minimum off-diagonal
- maximum absolute continuous-control change relative to accepted P11 controls.

Do not infer monotonicity beyond the three points and do not fit a trend or threshold.

## Hard scientific budget

Maximum across the whole task:

- new policy maps: `3`
- selector evaluations: `2400`
- D2/Q assemblies: `3`
- direct HJB solves/updates: `3 / 3`
- complete one-step panel evaluations: `3`
- scalar-root invocations: `<=933768`
- liquid-Z root invocations: `<=855360`
- interior-a switching root invocations: `<=2400`
- joint-switching root invocations: `<=2400`
- scientific retries: `0`
- solver substitutions: `0`
- KFE/SVD/eigen/nullspace/stationary mass: `0`
- household aggregate adapter evaluations: `0`
- capital-network calls: `0`
- firm/wage/return calls: `0`
- outer-loop/steady-state/trajectory calls: `0`
- MATLAB scientific calls: `0`
- K1B feedback: `0`
- GE/annual/shock/IRF/welfare/Results: `0`.

The large root ceilings are only structural ceilings implied by at most 2400 selector evaluations; they do not authorize extra maps, retries or root-only experiments.

## Engineering boundary

Builder may add a minimum isolated fixed-price safety-panel driver and focused tests.

Do not modify:

- selector scientific law;
- D1/D2/D3;
- KKT/boundary/upwind/switching law;
- convergence thresholds;
- `Delta`;
- grid;
- productivity generator;
- payoff taper;
- default source-faithful multi-province runtime;
- K1/K1A/K1B scientific formulas;
- firm equations;
- Results code.

Routine pre-science import/path/serialization issues may be repaired within task scope. Once a panel scientific call has begun, no scientific retry of that panel is available.

## Stop conditions

Stop immediately on the first:

- authority/provenance mismatch;
- accepted CSV panel-value mismatch;
- selector failure;
- D2 failure;
- nonfinite policy/Q/V;
- direct-solve warning, shape failure or backward error above `1e-12`;
- scientific-code mutation after freeze;
- budget breach.

If LOW fails, do not execute MEDIAN/HIGH.
If MEDIAN fails, do not execute HIGH.

Do not clip or transform the raw payoff to rescue a failure.

## Deliverables

Create a fresh compact evidence root under `reports/` containing at least:

- startup/authority binding
- accepted CSV panel derivation receipt
- per-point policy-map receipts
- per-point D2/Q receipts
- per-point Bellman and one-step receipts
- per-point direct-solve accuracy
- panel comparison
- exact scientific ledger
- pre/post scientific-code freeze
- terminal receipt
- sealed manifest and independent readback.

Write:

`docs/CH5_MP4C_K1A_RAW_RA0_CORRECTED_HOUSEHOLD_FIXED_PRICE_THREE_POINT_SAFETY_PANEL_REPORT.md`.

Terminal PASS marker:

`PASS__RAW_RA0_FIXED_PRICE_THREE_POINT_CORRECTED_HOUSEHOLD_ONE_STEP_SAFETY_PANEL__LONGER_RUNTIME_NOT_YET_AUTHORIZED`.

A PASS means only that the adopted raw-payoff range represented by the preregistered LOW/MEDIAN/HIGH points survives one corrected-household policy/D2/direct-update step at fixed non-payoff inputs.

It does not establish raw-payoff HJB convergence, terminal KFE, a 31-province household batch, outer-loop stability, K1B, GE or Results.

Git workflow:

- isolated task branch
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not merge main
- do not modify CURRENT files
- do not publish successor.
