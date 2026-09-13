# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_DESIGN_FROZEN__TASK_PENDING_PUBLICATION`。

最新 accepted HJB mechanism candidate：`c6d89327933edef2b942f10f462b58cfa6b52954`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTANCE.md`。
Owner/Reviewer mechanism review freeze：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_REVIEW_FREEZE_CURRENT.md`。
Owner/Reviewer fixed-point intervention freeze：`docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_FREEZE_CURRENT.md`。
当前 active Builder task：NONE，等待 exact task publication。
Results eligibility=`FALSE`。

Accepted mechanism evidence继续有效：62/62 exact-input replay；instrumentation parity PASS；turn1 `20/31`、turn2 `2/31`；failed calls表现为policy chattering与non-monotone value-update oscillation，derivative-floor activation通常更晚；不支持pure two-cycle、monotone-slow或仅延长100-iteration ceiling。

Owner已批准第一 isolated same-input fixed-point intervention：value-update relaxation `omega=0.5`。

每次HJB iteration保持accepted policy/selector/operator/RHS/direct solve不变，先得到`V_solve`，之后仅改变传给下一iteration的value state：

`V_next = 0.5*V_old + 0.5*V_solve`。

accepted baseline等价于`omega=1`。该干预是temporary numerical fixed-point diagnostic，不是经济参数或新HJB方程。

为避免damping机械缩小update而造成false convergence，treatment convergence必须继续以raw fixed-point gap判定：`||V_solve-V_old||_inf < 1e-7`；100-iteration ceiling不变。同时单独记录relaxed state update `||V_next-V_old||_inf`。

下一task应复用accepted turn1/turn2 G2-control、D1-OFF的62个proven-exact inputs，不重新跑完整baseline。先用一个accepted converged call和一个accepted ceiling-failure call证明generalized wrapper在`omega=1`时与accepted map exact-equal；之后对62个exact inputs各做一次`omega=0.5` replay。

继续冻结：annual continuous time；`rho=.05`、`rb=.02`、borrowing gap `.07`、`delta=.10`、`Q_z=1/3`、`chi0=.1`、`chi1=2`；transfer FOC/selector/boundary；derivative floor；HJB economic equation；accepted pseudo-time/direct-solve matrix/RHS/linear solver；tolerance、100-iteration ceiling、grid；G2 return guard；wage safeguard；K1A fixed theta、`beta_distance=2`、`beta_return=0`、same-S、source-faithful labor、C1 unchanged；D1 OFF；K1B/K2 OFF。

不得观察结果后调整`omega`，本阶段不授权damping ladder、adaptive damping、solver替换、tolerance/grid/price guard/derivative floor/FOC/boundary/KKT/economic parameter变化。

KFE仍=`DIAGNOSTIC_ONLY`；finite-box upper-b leakage与MATLAB-style pinning独立未解决。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。长期仍要求`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

下一步：发布exact task `CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC`，完成后由ChatGPT Reviewer独立验收。
