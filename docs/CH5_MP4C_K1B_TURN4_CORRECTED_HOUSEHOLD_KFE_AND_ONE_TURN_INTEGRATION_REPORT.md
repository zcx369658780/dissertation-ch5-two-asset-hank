# CH5 MP4C K1B turn4 corrected household/KFE and one-turn integration report

Date: 2026-09-21

Task: `CH5_MP4C_K1B_TURN4_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921`

## Terminal

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

The unique authorized turn4 run stopped at the first scientific failure. Eleven provinces completed corrected HJB and unique-closed-class KFE. Province 11, 安徽, reached a selector `NO_ADMISSIBLE_POLICY` at checkpoint 4, flat 364. No rescue, retry, parameter change, alternate solver, or integration was performed.

Results eligibility remains `FALSE`. No successor is published by this task.

## Authority and frozen input binding

- Live-main baseline: `ea2b4a99ac7ce12f950b43170bc86e8bfeede37f`.
- Turn4 input blob: `ee779174c614980a0e6182d710ea5aaec8afb6f5`.
- Turn4 input SHA-256: `35CA47135CF3B17ADACDD6C39FBA30CC0E55AE1C103C5F42064D6722AF28310C`.
- Entering classification: `TURN4_K1B_INPUT_CANDIDATE_ONLY__TURN4_HOUSEHOLD_NOT_RUN`.
- Entering `rah` SHA-256: `7DE65A71206F52AB3D2DA98D6D01C43A8A69D8B2C423BE49A15D5D287C434BE9`.
- Frozen share-plan blob: `a37647bb68ed1bec6259071d7035f8de07591c9f`.
- Frozen share-plan SHA-256: `41B7DDA4DE2C33C6EADFAB3F324C3592D119B0E91DC7AE8E23968653A881522A`.
- Frozen turn4 `S_K1B` SHA-256: `5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`.
- Completed-turn3 raw `ra0` binding: `1C587932F4E8471209663D2262DB1BB308857EEEA1198D7868E4721CFB031E8F`.
- Accepted production-source binding: PASS.
- Pre/post source freeze: exact PASS.
- Production-source changes: 0.

## Reached-province status

| # | Province | Status | Turn4 checkpoint | B | D |
|---:|---|---|---:|---:|---:|
| 0 | 北京 | HJB/KFE PASS | 12 | 1.1982387304598774e-11 | 1.1984232717310306e-08 |
| 1 | 天津 | HJB/KFE PASS | 12 | 4.4950987376779494e-12 | 4.479242088351043e-09 |
| 2 | 河北 | HJB/KFE PASS | 13 | 2.5907331835384184e-12 | 2.585785363606874e-09 |
| 3 | 山西 | HJB/KFE PASS | 12 | 4.8138021346844084e-12 | 4.795133179413824e-09 |
| 4 | 内蒙古 | HJB/KFE PASS | 13 | 3.878009025015672e-13 | 3.9016656572243846e-10 |
| 5 | 辽宁 | HJB/KFE PASS | 13 | 1.1578238368059601e-13 | 1.1716139169948292e-10 |
| 6 | 吉林 | HJB/KFE PASS | 13 | 5.281747261776104e-12 | 5.193172114559275e-09 |
| 7 | 黑龙江 | HJB/KFE PASS | 13 | 4.0815545387928864e-12 | 4.04900157846555e-09 |
| 8 | 上海 | HJB/KFE PASS | 11 | 3.5233607698081926e-11 | 3.523143110584215e-08 |
| 9 | 江苏 | HJB/KFE PASS | 12 | 3.2853580966829554e-12 | 3.2804019500787263e-09 |
| 10 | 浙江 | HJB/KFE PASS | 12 | 3.746947196958672e-12 | 3.739817788783739e-09 |
| 11 | 安徽 | FIRST FAILURE | last complete checkpoint 3 | — | — |

The 11 completed provinces have maximum `B=3.5233607698081926e-11` and maximum `D=3.523143110584215e-08`, both within the frozen convergence thresholds.

## First scientific failure

- Province: 安徽, index 11.
- Checkpoint: 4.
- Flat index: 364.
- Cell: `v004_f0364_b004_a018_z000`.
- Cell receipt SHA-256: `F1170662F50FEB38BB6D26B233725B672B12397EA891C15CBBDC559DBA6DCB65`.
- Grid index `(b,a,z)`: `(4,18,0)`.
- State location: `b=-0.5263157894736843`, `a=9.473684210526315`, `z=0.8`.
- Raw derivatives:
  - `p_a_backward=8.895604077208148e-05`
  - `p_a_forward=-0.000536125311776913`
  - `p_b_backward=0.0015039676061569449`
  - `p_b_forward=0.008487587452625978`
- `effective_r_a=0.6165207360573086`.
- `effective_r_b=0.09000000000000001`.
- Selector outcome: `NO_ADMISSIBLE_POLICY`.
- Admissible comparison count: 0.
- Selector evaluation ordinal within province: 3,565.

All four ordinary derivative combinations have positive `q_b` and are D2-assembler admissible, but each is rejected by the existing A or B derivative-direction consistency law. The two zero-kink candidates have `d=0`, but their transfer KKT residuals are outside their recorded target intervals; one also fails B-direction consistency. Positive-transfer candidates are rejected by transfer-sign/KKT conditions and A or B direction consistency. No switching root was invoked for this cell.

This report records the production result only. It does not classify the failure as an implementation defect and does not authorize a selector change or forensic extrapolation.

## Scientific ledger at stop

- Source-native initializations: 12.
- Scalar labor roots attempted/returned: 9,600 / 9,600.
- Corrected policy maps / D2-Q assemblies: 151 / 151.
- Selector evaluations: 120,800.
- Selector root invocations: 52,895.
- Interior-Z root invocations: 11,495.
- Direct HJB updates: 140.
- Post-update checkpoint evaluations: 139.
- Corrected aggregate evaluations: 11.
- SCC / restricted GESVD / normalized stationary candidates / full-Q checks: 11 / 11 / 11 / 11.
- Full-space 800x800 GESVD: 0.
- Scientific retries / solver substitutions: 0 / 0.
- Adaptive controller, clipping, artificial diffusion, alternate continuation: 0.
- Household batch constructions: 0.
- Source-faithful labor, frozen turn4 allocation, C1, firms, wage, monetary, fiscal: all 0.
- Completed-turn4 raw `ra0`: 0.
- Turn5 preparation and turn5 household: 0 / 0.
- K2, MATLAB, GE/annual/shock/IRF/welfare/Results: all 0.
- Wall time: `857.8603612000006` seconds.

## Relaxation ledger

- Helper invocations: 140.
- Alpha candidates evaluated: 142.
- `alpha=1`: 138.
- `alpha=0.5`: 2.
- Exhaustion: 0.
- Relaxation failure: none.
- Minimum accepted raw b slope among reached provinces: `0.0003402771545246075` for 内蒙古.

The task stopped on the selector outcome, not on the monotonicity-preserving relaxation law.

## Cross-turn diagnostics

The portion available before the first failure is descriptive only:

- For the first 11 provinces, turn3 direct-update count was 135 and turn4 count was 136.
- Ten of these provinces have the same terminal checkpoint as turn3.
- 辽宁 changed from checkpoint 12 to checkpoint 13.
- No sign or direction is an acceptance condition.

The task-authorized full cross-turn panel requires completed-turn4 raw `ra0`, turn5 z-score/share/payoff, C1 and completed aggregate states. Those objects are `UNAVAILABLE__NOT_COMPUTED_AFTER_FIRST_SCIENTIFIC_FAILURE`. A full cross-turn panel was therefore not constructed, preserving the first-failure stop rule.

## Conditional integration status

The 31/31 gate was not met. Consequently:

- household batch: 0
- source-faithful labor: 0
- frozen-turn4 `S_K1B` quantity allocation: 0
- C1: 0
- firms: 0
- completed-turn4 raw `ra0`: 0
- turn5 score/share/payoff candidate: 0
- turn5 household: 0.

## Evidence integrity

- Evidence root: `reports/ch5_mp4c_k1b_turn4_corrected_household_kfe_and_one_turn_integration_20260921_run001/`.
- Sealed manifest entries: 2,114.
- Sealed bytes: 29,129,317.
- Manifest SHA-256: `964E9996697698A0199F474F4AE8B9D728B8F86E3CA6C2F0F0DC7CFC3C1BB584`.
- Independent readback: PASS.
- Bad paths: 0.
- Readback scientific calls: 0.
- Focused tests: 6/6 PASS.

## Boundary

The task is stopped at the first scientific failure. The evidence does not authorize a rerun, selector repair, turn4 integration, turn5 household, K2, a longer outer path, GE, Results, CURRENT modification, main merge, or successor publication.
