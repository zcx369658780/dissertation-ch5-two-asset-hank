# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC_TASK_ACTIVE`。

最新 accepted HJB mechanism candidate：`c6d89327933edef2b942f10f462b58cfa6b52954`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTANCE.md`。
Owner/Reviewer fixed-point intervention freeze：`docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Accepted mechanism evidence继续有效：62/62 exact-input replay；instrumentation parity PASS；turn1 `20/31`、turn2 `2/31`；failed calls表现为policy chattering与non-monotone value-update oscillation，derivative-floor activation通常更晚；不支持pure two-cycle、monotone-slow或仅延长100-iteration ceiling。

Owner已批准第一 isolated same-input fixed-point intervention：value-update relaxation `omega=0.5`。每次HJB iteration保持accepted policy/selector/operator/RHS/direct solve不变，先得到`V_solve`，之后仅改变下一iteration的value state：`V_next=0.5*V_old+0.5*V_solve`。accepted baseline等价于`omega=1`。

为避免false convergence，treatment convergence使用raw fixed-point gap：`||V_solve-V_old||_inf < 1e-7`；relaxed update单独记录；100-iteration ceiling不变。

Active task复用accepted turn1/turn2 G2-control、D1-OFF的62个proven-exact inputs，不重新跑完整baseline。先用一个accepted converged call和一个accepted ceiling-failure call做`omega=1` exact-equivalence gate；通过后对最多62个exact inputs各做一次`omega=0.5` treatment replay。总HJB budget最多64；KFE、outer trajectory/turn advancement、MATLAB、firm runtime、K1B/K2、GE/IRF/Results均为0；scientific retry=0。

继续冻结：annual continuous time；`rho=.05`、`rb=.02`、borrowing gap `.07`、`delta=.10`、`Q_z=1/3`、`chi0=.1`、`chi1=2`；transfer FOC/selector/boundary；derivative floor；HJB economic equation；accepted pseudo-time/direct-solve matrix/RHS/linear solver；tolerance、100-iteration ceiling、grid；G2 return guard；wage safeguard；K1A fixed theta、`beta_distance=2`、`beta_return=0`、same-S、source-faithful labor、C1 unchanged；D1 OFF；K1B/K2 OFF。

不得观察结果后调整`omega`；不授权damping ladder、adaptive damping、solver替换、tolerance/grid/price guard/derivative floor/FOC/boundary/KKT/economic parameter变化。

KFE仍=`DIAGNOSTIC_ONLY`；finite-box upper-b leakage与MATLAB-style pinning独立未解决。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。长期仍要求`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

下一gate：Builder完成active task后，由ChatGPT Reviewer独立ACCEPT/REJECT并决定是否进入production HJB solution-method contract讨论或重定向路线。
