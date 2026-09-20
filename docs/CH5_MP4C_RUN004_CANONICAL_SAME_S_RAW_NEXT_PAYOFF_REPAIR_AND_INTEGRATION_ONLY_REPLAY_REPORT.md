# Chapter 5 run004 canonical same-S integration-only replay

## Terminal verdict

`PASS__RUN004_ACCEPTED_31_PROVINCE_HOUSEHOLD_KFE__CANONICAL_SAME_S_INTEGRATION_REPLAY_PASS__RAW_NEXT_PAYOFF_READY__TURN2_NOT_RUN`

The accepted run004 household batch was reconstructed exactly. No household HJB, KFE, stationary-mass or aggregate science was rerun. One integration-only replay passed all accounting gates.

## Accepted batch binding

- Reconstructed identity: `8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05`.
- Province terminal receipts: `31`; stationary aggregate receipts: `31`.

## Canonical same-S payoff

- Raw-ra0 SHA-256: `E8C85E4C29D44151C4D89D94F7F68136231917507ADECE30D5ACC7C322DF397A`.
- S SHA-256: `AC8DD36BB21E2B907D7521C98F8E65DCA3803291B54296AA7C2681E8CC6F226F`.
- Ordered product terms SHA-256: `19E65998D0A1F9BC65372B7C8364A9571FEA507642513C215C983A8E49358474`.
- Canonical payoff SHA-256: `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`.
- Canonical versus BLAS max absolute difference: `2.2204460492503131e-16`; bitwise equal entries: `15/31`.

## Integration accounting

- source_update_order: `True`.
- k1a_share_columns: `True`.
- national_private_capital: `True`.
- home_retained_capital: `True`.
- c1_residual_exact: `True`.
- firm_k_accounting: `True`.
- all_firm_outputs_finite: `True`.
- raw_ra0_finite: `True`.
- same_exact_s_for_quantity_and_payoff: `True`.
- canonical_raw_next_payoff_finite: `True`.
- no_payoff_transformation: `True`.

National origin private wealth and destination private productive capital are both `127341904.64894083`; the conservation residual is exactly `0`. Total C1 residual GovInv is `2354651002.2516108`.

## Firm and next-state diagnostics

- Firm rows: `31`; all outputs finite.
- Firm K range: `6325734.32618382` to `210016973.075811`.
- Firm Y range: `5668698.1158054` to `149601455.321782`.
- Firm wage range: `0.8` to `1.3`.
- Raw firm ra0 range: `0.24620984639967106` to `0.9499860199715977`.
- Historical used-ra diagnostic range: `0.09` to `0.09`; it was not used for the payoff vector.
- Next composite wage range: `12.879055911932856` to `17.524321872552765`.
- Next rb: `0.02`.
- Next-state candidate rows: `31`; raw-next-payoff SHA-256: `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`.

## Scientific ledger

- run004_manifest_loads: `1`.
- province_terminal_receipt_loads: `31`.
- stationary_aggregate_receipt_loads: `31`.
- household_batch_reconstructions: `1`.
- source_faithful_labor_reconstructions: `1`.
- k1a_capital_network_allocations: `1`.
- c1_residual_govinv_constructions: `1`.
- firm_evaluations: `31`.
- composite_wage_batches: `1`.
- monetary_assignments: `1`.
- fiscal_diagnostic_batches: `1`.
- canonical_raw_next_payoff_constructions: `1`.
- source_native_initializations: `0`.
- selector_or_root_calls: `0`.
- d2_q_assemblies: `0`.
- hjb_or_direct_solve_calls: `0`.
- scc_or_topology_calls: `0`.
- restricted_gesvd_calls: `0`.
- full_space_gesvd_calls: `0`.
- stationary_mass_candidate_calls: `0`.
- q_transpose_p_calls: `0`.
- corrected_aggregate_evaluations: `0`.
- second_integration_replays: `0`.
- turn2_household_calls: `0`.
- second_outer_turns: `0`.
- k1b_calls: `0`.
- k2_calls: `0`.
- adaptive_controller_calls: `0`.
- matlab_calls: `0`.
- ge_annual_shock_irf_welfare_results_calls: `0`.
- scientific_retries: `0`.
- payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls: `0`.

## Evidence

- Evidence root: `reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/`.
- Sealed manifest SHA-256: `79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D`.
- Manifest entries/bytes: `17` / `126733`.
- Independent readback: `PASS`; bad paths: `0`.
- Pre/post code-freeze hashes match exactly.
- Focused tests: `5 passed`; `py_compile` and `git diff --check`: PASS.

Turn 2 was not run. K1B, K2, GE and Results were not run. CURRENT files were not modified and no successor was published.
