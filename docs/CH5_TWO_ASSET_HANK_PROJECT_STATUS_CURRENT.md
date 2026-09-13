# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC_CANDIDATE_PUBLISHED__INDEPENDENT_REVIEW_REQUIRED`。

最新 accepted HJB mechanism candidate：`c6d89327933edef2b942f10f462b58cfa6b52954`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTANCE.md`。
Owner/Reviewer fixed-point intervention freeze：`docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_FREEZE_CURRENT.md`。
当前 active Builder task：NONE。最新完成的 exact task 为 `tasks/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC.md`；未发布 successor task。
Results eligibility=`FALSE`。

Accepted mechanism evidence继续有效：62/62 exact-input replay；instrumentation parity PASS；turn1 `20/31`、turn2 `2/31`；failed calls表现为policy chattering与non-monotone value-update oscillation，derivative-floor activation通常更晚；不支持pure two-cycle、monotone-slow或仅延长100-iteration ceiling。

Owner已批准第一 isolated same-input fixed-point intervention：value-update relaxation `omega=0.5`。每次HJB iteration保持accepted policy/selector/operator/RHS/direct solve不变，先得到`V_solve`，之后仅改变下一iteration的value state：`V_next=0.5*V_old+0.5*V_solve`。accepted baseline等价于`omega=1`。

为避免false convergence，treatment convergence使用raw fixed-point gap：`||V_solve-V_old||_inf < 1e-7`；relaxed update单独记录；100-iteration ceiling不变。

Completed candidate复用了accepted turn1/turn2 G2-control、D1-OFF的62个proven-exact inputs，未重新跑完整baseline。一个accepted converged call和一个accepted ceiling-failure call的`omega=1` exact-equivalence gate通过后，对62个exact inputs各执行一次`omega=0.5` treatment replay。总HJB calls=64；KFE、outer trajectory/turn advancement、MATLAB、firm runtime、K1B/K2、GE/IRF/Results均为0；scientific retry=0。

继续冻结：annual continuous time；`rho=.05`、`rb=.02`、borrowing gap `.07`、`delta=.10`、`Q_z=1/3`、`chi0=.1`、`chi1=2`；transfer FOC/selector/boundary；derivative floor；HJB economic equation；accepted pseudo-time/direct-solve matrix/RHS/linear solver；tolerance、100-iteration ceiling、grid；G2 return guard；wage safeguard；K1A fixed theta、`beta_distance=2`、`beta_return=0`、same-S、source-faithful labor、C1 unchanged；D1 OFF；K1B/K2 OFF。

不得观察结果后调整`omega`；不授权damping ladder、adaptive damping、solver替换、tolerance/grid/price guard/derivative floor/FOC/boundary/KKT/economic parameter变化。

KFE仍=`DIAGNOSTIC_ONLY`；finite-box upper-b leakage与MATLAB-style pinning独立未解决。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。长期仍要求`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

Builder candidate classification：`PARTIAL_SUPPORT__SYSTEMATIC_CHATTERING_REDUCTION__NET_ONE_CONVERGENCE_GAIN__TURN2_NONE_AND_ENDPOINT_DIVERGENCE_OUTLIERS`。62/62 exact-input coverage；omega=1 two-call parity PASS；64 HJB calls、4,823 direct solves、scientific retry=0；baseline/treatment convergence分别为turn1 20/31→23/31、turn2 2/31→0/31、all 22/62→23/62。Policy-switch mean在57/62、two-step reversion mean在59/62、raw-gap non-monotonicity在58/62下降，但7个baseline-converged calls丢失，both-converged endpoint也非普遍一致。全部62 treatment outputs经metadata adjudication后finite/shape/domain normal；Results eligibility=`FALSE`。

唯一下一gate：ChatGPT Reviewer独立ACCEPT/REJECT；若接受，只向Owner提交 `OWNER_HJB_RELAXATION_MIXED_EVIDENCE_AND_TURN2_FIXED_POINT_COHERENCE_REVIEW`，不得自动进入production contract或发布 successor task。
