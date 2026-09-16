# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`Q0_KFE_FAIL_CLOSED_ACCEPTED__SECONDARY_DIAGONAL_REAGGREGATION_AUDIT_RECLASSIFIED__BOUNDED_RERUN_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted scientific checkpoint

Owner-adopted D1/D2/D3 corrected semantics、lower-a zero-kink multiplier handling、interior zero-liquid Z switching、Option-A 800-cell complete policy map、accepted Q0 conservative generator以及一次 direct HJB step均继续有效。Source-faithful/production paths remain frozen。

## Q0 KFE design

`docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_REPORT.md` 已接受：Q0 可直接用于 operator-level、source-free KFE validation；无需先进行 V1 policy remap。冻结 forward equation 为 `Q0.T @ p = 0`，F-order `(20,20,2)`，`omega=70/361`，pin-free homogeneous nullspace，唯一 full `gesvd`，以及 SCC/rank/nullity/nonnegative-mass/source-free residual 检查。

## First runtime attempt

Builder candidate `d4f643f1d26ad5a28395f60a58c545447abda7ba` 已接受为有效 fail-closed evidence。该 run 验证 exact Q0 identity、有限 CSR、zero negative offdiagonal、`Q0@1` within frozen bound 以及四个资产边界 exact-zero outward flux，但在 secondary sparse offdiagonal reaggregation 上得到 `3.552713678800501e-15` 而非 exact zero，因此按旧 task 停在 SCC/SVD 之前。

Reviewer 已裁定：accepted D2 receipt 中相对于 retained-outgoing construction array 的 `diagonal_construction_error=0.0` 仍是 exact construction authority；从 serialized CSR offdiagonals 独立重聚合是不同浮点 reduction，不应要求 bitwise exact zero。该 secondary audit 改为固定 prospective bound `<=5.222144858126786e-14`，差值必须原样持久化，不能清零或调参。

Authority: `docs/CH5_MP4C_2018_KFE_D123_Q0_KFE_STRUCTURAL_AUDIT_ARITHMETIC_REAGGREGATION_ACCEPTANCE_20260916.md`。

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_RERUN_WITH_BOUND_REAGGREGATION_20260916.md`。

Fresh rerun only. Scientific ceilings remain: Q0 load 1, structural audit 1, `Q0@1` 1, SCC 1, full dense GESVD 1, normalized candidate 1, `Q0.T@p` 1; retries/solver substitutions/row replacement/iterative eigensolver are zero. Selector/root/policy-map/D2/HJB/V1 remap/MATLAB/downstream remain zero.

A future PASS validates only the invariant mass of accepted V0-policy operator Q0. It is not nonlinear HJB convergence, joint HJB-KFE fixed point, steady state, production readiness or Results authority.
