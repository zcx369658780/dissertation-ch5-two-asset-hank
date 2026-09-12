# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_INSTRUMENTED_HA_HJB_MECHANISM_ACCEPTED__TEMPORARY_TRANSFER_CONTROL_SAFEGUARD_POLICY_FROZEN__ZERO_SCIENCE_NUMERIC_DESIGN_ACTIVE`。

最新 accepted instrumented candidate：`5d28382f5914d161817642bab9f3c6d73b41c935`。
Reviewer acceptance：`docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`。
Owner transfer-control safeguard freeze：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_TEMPORARY_ADMISSIBILITY_SAFEGUARD_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN.md`。
Results eligibility=`FALSE`。

## 已接受：turn2 common-state mechanism localization
Instrumentation ON/OFF scientific outputs exact-parity。Turn2 iteration1 的 derivatives、floors、pre-selector transfer candidates、policy labels仍一致；最先差异来自 frozen G1/G2 return guard 导致的 `effective_illiquid_return` 与 `mu_a` / illiquid-drift assembly，随后 operator与`V_new`分叉。Iteration2 后 value derivatives 与 transfer candidates 全面分叉；湖北 turn2 interior checkpoint 显示后期 huge transfer/cost 并非 selector 将温和 candidate 放大，而是 raw pre-selector transfer candidate 已经在 value-derivative / transfer-FOC feedback 中爆炸后被选中。

## Owner 最新 scientific decision
Owner 同意先建立 **temporary transfer-control admissibility safeguard**，同时保持 `chi0=.1`、`chi1=2 years` 与其他 frozen science 不变。

该 safeguard 只属于 `TEMPORARY_NUMERICAL_CONTINUATION_SAFEGUARD`，不是结构经济约束。其作用层级冻结为：raw transfer candidate 由既有 FOC 生成后、进入 final selector / drift / cost assembly 前做 admissibility 判断；raw candidate 必须完整保存，不得静默改写 FOC。

目前只冻结 safeguard policy，尚未冻结任何 `d` 数值上下界，也未授权 runtime。

## 当前 active gate
当前 exact task 是纯 zero-science design：只读取 accepted G1/G2 instrumented traces，分析 raw pre-selector transfer candidates 与 selected `d` 的中心区域、heavy tail、sign asymmetry、branch identity、asset/grid scale，以及湖北/山东/广东/四川/云南等 priority checkpoints。

任务必须比较 candidate rejection、candidate clipping、fallback-to-zero/no-transfer 三种 safeguard semantics，并在证据足够时提出一个 3–4 stage + OFF 的 preregistered continuation ladder及静态 hit shares；若证据不足则明确保留 Owner numeric decision，不得为了追求 convergence 反推阈值。

## Frozen boundary
本 gate 不允许任何 scientific/model runtime，也不得修改：`chi0/chi1`、derivative floor、return/wage guards、annual calibration、transfer FOC、selector/boundary/KKT law、grid、tolerance、solver、capital network、C1、labor science。不得 longer G2、G3/G4、wage relaxation、K1B/K2。

Price-bound hit monitoring继续强制执行；长期目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`，且最终经济结果也不应依赖 binding temporary transfer-control cap。

KFE仍为`DIAGNOSTIC_ONLY`，finite-box upper-b leakage与MATLAB-style pinning独立未解决。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

Results eligibility=`FALSE`。
