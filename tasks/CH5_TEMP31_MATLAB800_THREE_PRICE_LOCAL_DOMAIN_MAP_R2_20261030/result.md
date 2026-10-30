# TEMP31 MATLAB800 discrete three-price map R2

TASK_ID=CH5_TEMP31_MATLAB800_THREE_PRICE_LOCAL_DOMAIN_MAP_R2_20261030
Candidate=codex/ch5-temp31-matlab800-three-price-local-domain-r2-20261030
Fixed source/parent=56447829ce0e6c3c85552c53c351b26a2452a4bd; source tree7b7cb29dd5b37be92561e7f1bc688c0d29789732.
All12 points were executed once in frozen order, each with a fresh true800-state initializer and one unchanged HJB driver. No historical point was rerun and no adaptive points were added.

New HJB converged: D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11.
New HJB not converged: D00; KFE not run at these points.
Source KFE executed: 11; exploratory interior candidates: D01, D02, D03, D04, D05, D06, D07, D08, D09, D11.
B_UPPER_BOUNDARY_WARNING points: D01, D02, D07, D08.
Strict economic stationarity certified points: [].
Actual counts: {"initializer_calls": 12, "root_cells": 9600, "brentq_calls": 9600, "hjb_calls": 12, "hjb_iterations": 350, "hjb_policy_cells": 280000, "operator_assemblies": 362, "hjb_linear_solves": 350, "kfe_calls": 11, "kfe_linear_solves": 11, "kfe_contaminated_row_index_calls": 11}.

The unchanged source KFE can compute finite normalized distributions with original-stationarity warnings. Those outputs are not certified invariant economic distributions or formal31-province capital supply. New results and historical7-point reference provenance are separate in point_result_matrix.md. This is a19-point observed cloud, not a certified continuous three-dimensional feasible box.

No existing scientific file, policy, operator, HJB, KFE, bootstrap or production path was edited. MATLAB full-system parity remains unproved. Source initializer's effective-return-squared temp and all source boundary/selector formulas are preserved, not silently corrected. Nonconvergent points and any external homecrit/implicit residual warnings remain visible. Native BLAS thread counts are NOT_MEASURED; six environment limits are1; Windows Job process committed memory1GiB and active-child limit1 were actually enforced; RSS is a different measure.

Payload/seal final Git identities and exact remote byte verification are recorded in receipts, avoiding self-reference. Scientific budget is closed; terminal after delivery STOP__AWAITING_GPT_INDEPENDENT_ABC. P3=BLOCKED; FORMAL_SOURCE_FREEZE=FALSE; V010=UNCHANGED; V011=NOT_STARTED; Results=FALSE; model_activation=FALSE; REAL_GE=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED.
